"""Agent context injection layer.

Prepares filtered, salience-ranked KO context for injection into
MAGELLAN agent dispatch prompts (§4.1 of architecture spec).

Each agent receives a structured KO briefing instead of raw text,
with class tags, confidence levels, and contradiction status.
"""

import json

from . import config
from . import store
from . import salience as sal
from . import dialectic


def format_ko_for_context(ko, salience_score=None):
    """Format a single KO as a structured context line.

    Format: [{CLASS}] [{regime}] (K:{K}, conf:{confidence}) {summary}
    """
    scores = ko.get("scores", {})
    regime = ko.get("regime", "event").upper()
    cls = ko.get("class", "UNKNOWN")
    k = scores.get("K", 0.0)
    conf = scores.get("confidence", 0.5)
    urgency = scores.get("urgency", 0.0)
    contradiction = scores.get("contradiction", 0.0)
    summary = ko.get("summary", ko.get("content", "")[:200])

    parts = [f"[{cls}]", f"[{regime}]", f"(K:{k:.2f}, conf:{conf:.2f})"]

    if cls == "QUESTION" and urgency > 0.3:
        parts.append(f"(urgency:{urgency:.2f})")
    if contradiction > 0.2:
        parts.append(f"(tension:{contradiction:.2f})")
    if salience_score is not None:
        parts.append(f"(sal:{salience_score:.3f})")

    parts.append(summary)
    return " ".join(parts)


def format_tension_for_context(tension):
    """Format a tension field as a context briefing line."""
    t_type = tension.get("type", "unknown")
    if t_type == "unresolved_question":
        return (
            f"[TENSION:UNRESOLVED] urgency:{tension.get('urgency', 0):.2f} "
            f"attempts:{tension.get('attempts', 0)} — {tension.get('summary', '')}"
        )
    if t_type == "active_contradiction":
        return (
            f"[TENSION:CONTRADICTION] score:{tension.get('tension_score', 0):.2f} "
            f"({tension.get('contradiction_count', 0)} against, "
            f"{tension.get('support_count', 0)} for) — {tension.get('summary', '')}"
        )
    if t_type == "constraint_violation":
        return (
            f"[TENSION:VIOLATION] {tension.get('hypothesis_summary', '')} "
            f"violates: {tension.get('constraint_summary', '')}"
        )
    if t_type == "evidence_conflict":
        return (
            f"[TENSION:CONFLICT] {tension.get('summary_a', '')} vs "
            f"{tension.get('summary_b', '')}"
        )
    if t_type == "convergence_candidate":
        ind = "independent" if tension.get("independent") else "same-session"
        return (
            f"[CONVERGENCE:{ind}] {tension.get('summary_a', '')} ↔ "
            f"{tension.get('summary_b', '')}"
        )
    return f"[TENSION:{t_type}] {json.dumps(tension)}"


def build_agent_context(agent_id, session_id=None, include_tensions=True):
    """Build complete context injection payload for an agent.

    Returns a dict with:
      - briefing: formatted text for prompt injection
      - kos: list of (salience_score, ko) tuples
      - tensions: list of tension dicts (if applicable)
      - stats: context statistics
    """
    kos = store.load_kos()
    adj_index = store.build_adjacency_index()

    # Get salience-ranked KOs
    ranked = sal.rank_kos_for_agent(agent_id, kos, adj_index)

    # Build formatted briefing
    lines = []
    lines.append(f"--- Epistemic Context for {agent_id} ---")
    lines.append(f"Graph: {len(kos)} KOs total, showing top {len(ranked)} by salience")
    lines.append("")

    # Group by class for readability
    by_class = {}
    for score, ko in ranked:
        cls = ko.get("class", "UNKNOWN")
        if cls not in by_class:
            by_class[cls] = []
        by_class[cls].append((score, ko))

    # Order classes by relevance to agent
    rho = config.AGENT_RHO.get(agent_id, 0.5)
    if rho >= 0.7:
        # Epistemic agents: questions first, then hypotheses, evidence
        class_order = ["QUESTION", "HYPOTHESIS", "OBSERVATION", "EVIDENCE",
                       "EVALUATION", "CONSTRAINT", "DECISION", "NARRATIVE", "PLAN"]
    else:
        # Action agents: evidence first, then constraints, evaluations
        class_order = ["EVIDENCE", "CONSTRAINT", "EVALUATION", "HYPOTHESIS",
                       "DECISION", "OBSERVATION", "NARRATIVE", "QUESTION", "PLAN"]

    for cls in class_order:
        items = by_class.get(cls, [])
        if items:
            lines.append(f"## {cls} ({len(items)})")
            for score, ko in items:
                lines.append(format_ko_for_context(ko, score))
            lines.append("")

    # Add tension briefing for epistemic agents
    tension_lines = []
    if include_tensions and rho >= 0.5:
        tensions = dialectic.detect_all_tensions(min_urgency=0.3)
        relevant = _filter_tensions_for_agent(agent_id, tensions)
        if relevant:
            tension_lines.append("## Active Tensions")
            for t in relevant[:5]:  # Max 5 tensions per briefing
                tension_lines.append(format_tension_for_context(t))
            tension_lines.append("")

    briefing = "\n".join(lines + tension_lines)

    return {
        "briefing": briefing,
        "kos": ranked,
        "tensions": relevant if include_tensions and rho >= 0.5 else [],
        "stats": {
            "agent": agent_id,
            "rho": rho,
            "total_graph_kos": len(kos),
            "injected_kos": len(ranked),
            "tension_count": len(relevant) if include_tensions and rho >= 0.5 else 0,
            "estimated_tokens": len(briefing) // 4,  # rough estimate
        },
    }


def _filter_tensions_for_agent(agent_id, tensions):
    """Filter tensions to those relevant for a specific agent."""
    relevant = []

    for category, items in tensions.items():
        if not isinstance(items, list):
            continue
        for t in items:
            recommended = t.get("recommended_agents", [])
            if agent_id in recommended:
                relevant.append(t)

    # Sort by urgency/score
    def sort_key(t):
        return t.get("urgency", t.get("tension_score", 0))

    return sorted(relevant, key=sort_key, reverse=True)


def inject_context_to_prompt(agent_id, base_prompt, session_id=None):
    """Inject epistemic context into an agent's dispatch prompt.

    Inserts the context briefing after the first line of the prompt.
    """
    ctx = build_agent_context(agent_id, session_id)

    if not ctx["kos"]:
        return base_prompt  # No context to inject

    briefing = ctx["briefing"]
    stats = ctx["stats"]

    injection = (
        f"\n\n<epistemic-context>\n"
        f"{briefing}\n"
        f"<!-- {stats['injected_kos']} KOs, ~{stats['estimated_tokens']} tokens, "
        f"ρ={stats['rho']} -->\n"
        f"</epistemic-context>\n\n"
    )

    # Insert after first paragraph break
    parts = base_prompt.split("\n\n", 1)
    if len(parts) == 2:
        return parts[0] + injection + parts[1]
    return base_prompt + injection
