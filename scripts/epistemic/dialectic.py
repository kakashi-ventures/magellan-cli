"""Dialectic engine — tension field detection and routing.

Transforms MAGELLAN's adversarial pipeline from stateless to stateful.
Detects persistent epistemic tensions in the KO graph and routes them
to the agents best equipped to resolve them (§5 of architecture spec).

Tension types:
  - Unresolved questions (high urgency, no addressing hypothesis)
  - Active contradictions (hypothesis with CONTRADICTS edges)
  - Evidence conflicts (evidence supporting contradictory hypotheses)
  - Convergence candidates (independent results reaching same conclusion)
  - Constraint violations (hypothesis contradicting known constraints)
"""

from . import config
from . import store


def _get_addressing_hypotheses(question_id, adj_index):
    """Find hypotheses that address a question (via BASED_ON, IMPLEMENTS)."""
    incoming = adj_index.get(question_id, {}).get("incoming", [])
    addressing = []
    for e in incoming:
        if e.get("type") in ("BASED_ON", "IMPLEMENTS"):
            source_ko = store.get_ko(e.get("source"))
            if source_ko and source_ko.get("class") == "HYPOTHESIS":
                addressing.append(source_ko)
    return addressing


def detect_unresolved_questions(min_urgency=0.5, adj_index=None):
    """Find QUESTION KOs with high urgency and no addressing hypothesis.

    These are priority targets for Scout and Generator.
    """
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    questions = store.query_kos(cls="QUESTION")
    tensions = []

    for q in questions:
        urgency = q.get("scores", {}).get("urgency", 0.0)
        if urgency < min_urgency:
            continue

        addressing = _get_addressing_hypotheses(q["id"], adj_index)
        surviving = [h for h in addressing
                     if h.get("meta", {}).get("survival_status") == "survived"]

        if not surviving:
            tensions.append({
                "type": "unresolved_question",
                "ko_id": q["id"],
                "urgency": urgency,
                "summary": q.get("summary", ""),
                "attempts": len(addressing),
                "sessions_unresolved": _count_sessions_since(q),
                "recommended_agents": ["scout", "generator"],
            })

    return sorted(tensions, key=lambda t: t["urgency"], reverse=True)


def detect_active_contradictions(adj_index=None):
    """Find hypotheses with unresolved CONTRADICTS edges.

    These are priority targets for Evolver (to resolve) or Critic (to deepen).
    """
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    hypotheses = store.query_kos(cls="HYPOTHESIS")
    tensions = []

    for h in hypotheses:
        if h.get("meta", {}).get("survival_status") == "killed":
            continue

        incoming = adj_index.get(h["id"], {}).get("incoming", [])
        contradictions = [e for e in incoming if e.get("type") == "CONTRADICTS"]
        supports = [e for e in incoming if e.get("type") == "SUPPORTS"]

        if contradictions:
            tension_score = len(contradictions) / max(1, len(contradictions) + len(supports))
            tensions.append({
                "type": "active_contradiction",
                "ko_id": h["id"],
                "summary": h.get("summary", ""),
                "contradiction_count": len(contradictions),
                "support_count": len(supports),
                "tension_score": round(tension_score, 3),
                "contradiction_pressure": h.get("scores", {}).get("contradiction", 0),
                "recommended_agents": ["critic", "evolver"],
            })

    return sorted(tensions, key=lambda t: t["tension_score"], reverse=True)


def detect_evidence_conflicts(adj_index=None):
    """Find evidence KOs that support contradictory hypotheses.

    When EVIDENCE A supports HYPOTHESIS X and EVIDENCE B supports HYPOTHESIS Y,
    but X and Y have CONTRADICTS edges between them.
    """
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    # Build hypothesis conflict pairs
    contradicts_edges = store.get_edges_by_type("CONTRADICTS")
    conflict_pairs = set()
    for e in contradicts_edges:
        src_ko = store.get_ko(e.get("source"))
        tgt_ko = store.get_ko(e.get("target"))
        if (src_ko and tgt_ko
                and src_ko.get("class") == "HYPOTHESIS"
                and tgt_ko.get("class") == "HYPOTHESIS"):
            pair = tuple(sorted([e["source"], e["target"]]))
            conflict_pairs.add(pair)

    # Find evidence supporting both sides
    tensions = []
    for h1_id, h2_id in conflict_pairs:
        h1_supporters = _get_supporting_evidence(h1_id, adj_index)
        h2_supporters = _get_supporting_evidence(h2_id, adj_index)

        if h1_supporters and h2_supporters:
            h1 = store.get_ko(h1_id)
            h2 = store.get_ko(h2_id)
            tensions.append({
                "type": "evidence_conflict",
                "hypothesis_a": h1_id,
                "hypothesis_b": h2_id,
                "summary_a": h1.get("summary", "") if h1 else "",
                "summary_b": h2.get("summary", "") if h2 else "",
                "evidence_for_a": len(h1_supporters),
                "evidence_for_b": len(h2_supporters),
                "recommended_agents": ["critic", "generator"],
            })

    return tensions


def detect_convergence_candidates(adj_index=None):
    """Find independent results converging on the same conclusion.

    KOs from different sessions/agents reaching similar conclusions
    without direct edges between them.
    """
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    # Look for existing CONVERGES_WITH edges
    convergence_edges = store.get_edges_by_type("CONVERGES_WITH")
    clusters = {}
    for e in convergence_edges:
        pair = tuple(sorted([e["source"], e["target"]]))
        if pair not in clusters:
            clusters[pair] = []
        clusters[pair].append(e)

    tensions = []
    for (ko_a_id, ko_b_id), edges in clusters.items():
        ko_a = store.get_ko(ko_a_id)
        ko_b = store.get_ko(ko_b_id)
        if ko_a and ko_b:
            # Independent if from different sessions or agents
            independent = (
                ko_a.get("meta", {}).get("session_id")
                != ko_b.get("meta", {}).get("session_id")
            )
            tensions.append({
                "type": "convergence_candidate",
                "ko_a": ko_a_id,
                "ko_b": ko_b_id,
                "summary_a": ko_a.get("summary", ""),
                "summary_b": ko_b.get("summary", ""),
                "independent": independent,
                "edge_count": len(edges),
                "recommended_agents": ["convergence-scanner", "session-analyst"],
            })

    return tensions


def detect_constraint_violations(adj_index=None):
    """Find hypotheses that contradict known constraints."""
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    constraints = store.query_kos(cls="CONSTRAINT")
    tensions = []

    for constraint in constraints:
        c_id = constraint["id"]
        incoming = adj_index.get(c_id, {}).get("incoming", [])
        violations = [e for e in incoming if e.get("type") == "CONTRADICTS"]

        for v in violations:
            violator = store.get_ko(v.get("source"))
            if violator and violator.get("class") == "HYPOTHESIS":
                tensions.append({
                    "type": "constraint_violation",
                    "hypothesis_id": v["source"],
                    "constraint_id": c_id,
                    "hypothesis_summary": violator.get("summary", ""),
                    "constraint_summary": constraint.get("summary", ""),
                    "recommended_agents": ["quality-gate", "critic"],
                })

    return tensions


def detect_all_tensions(min_urgency=0.5):
    """Run all tension detectors and return combined results."""
    adj_index = store.build_adjacency_index()
    return {
        "unresolved_questions": detect_unresolved_questions(min_urgency, adj_index),
        "active_contradictions": detect_active_contradictions(adj_index),
        "evidence_conflicts": detect_evidence_conflicts(adj_index),
        "convergence_candidates": detect_convergence_candidates(adj_index),
        "constraint_violations": detect_constraint_violations(adj_index),
        "total_tensions": 0,  # filled below
    }


def _get_supporting_evidence(hypothesis_id, adj_index):
    """Get evidence KOs that support a hypothesis."""
    incoming = adj_index.get(hypothesis_id, {}).get("incoming", [])
    evidence_ids = []
    for e in incoming:
        if e.get("type") == "SUPPORTS":
            source = store.get_ko(e.get("source"))
            if source and source.get("class") in ("EVIDENCE", "OBSERVATION"):
                evidence_ids.append(e["source"])
    return evidence_ids


def _count_sessions_since(ko):
    """Estimate sessions elapsed since KO creation (heuristic)."""
    age_days = 0
    try:
        from datetime import datetime, timezone
        created = datetime.fromisoformat(
            ko.get("meta", {}).get("created_at", "").replace("Z", "+00:00")
        )
        age_days = (datetime.now(timezone.utc) - created).days
    except (ValueError, TypeError):
        pass
    # Rough estimate: 1 session per 2 days on average
    return max(1, age_days // 2)


# Update total count after all detectors run
_orig_detect_all = detect_all_tensions


def detect_all_tensions(min_urgency=0.5):
    result = _orig_detect_all(min_urgency)
    result["total_tensions"] = sum(
        len(v) for k, v in result.items()
        if isinstance(v, list)
    )
    return result
