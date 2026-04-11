"""Regime promotion and lifecycle management.

Handles KO regime transitions (§3, §6 of architecture spec):
  working → event    : at session completion
  event → canonical  : when consolidation score ≥ 0.70
  event → tacit      : statistical pattern detected across ≥5 sessions
  * → archived       : K < 0.15 after 180 days (excluded from retrieval)
  * → dormant        : K < 0.05 (excluded from gravity computation)

Consolidation score:
  C(KO) = 0.30 * cross_session_survival
        + 0.25 * independent_confirmation
        + 0.25 * relational_centrality
        + 0.20 * methodological_stability
"""

from datetime import datetime, timezone

from . import config
from . import store


def _age_days(ko):
    """Get age in days from created_at."""
    try:
        created = datetime.fromisoformat(
            ko.get("meta", {}).get("created_at", "").replace("Z", "+00:00")
        )
        return (datetime.now(timezone.utc) - created).days
    except (ValueError, TypeError):
        return 0


def _get_sessions_containing(ko_id, all_edges):
    """Get set of session IDs where this KO has edges."""
    sessions = set()
    for e in all_edges:
        if e.get("source") == ko_id or e.get("target") == ko_id:
            # Extract session from edge timestamp or connected KOs
            for connected_id in (e.get("source"), e.get("target")):
                connected = store.get_ko(connected_id)
                if connected:
                    sid = connected.get("meta", {}).get("session_id")
                    if sid:
                        sessions.add(sid)
    return sessions


def compute_consolidation_score(ko, all_kos=None, all_edges=None):
    """Compute consolidation score for canonical promotion.

    C(KO) = 0.30 * cross_session_survival
           + 0.25 * independent_confirmation
           + 0.25 * relational_centrality
           + 0.20 * methodological_stability
    """
    if all_edges is None:
        all_edges = store.load_edges()
    if all_kos is None:
        all_kos = store.load_kos()

    ko_id = ko["id"]
    w = config.CONSOLIDATION_WEIGHTS

    # 1. Cross-session survival: fraction of sessions where this KO
    #    or its descendants survived critique
    sessions = _get_sessions_containing(ko_id, all_edges)
    own_session = ko.get("meta", {}).get("session_id", "")
    cross_sessions = sessions - {own_session}
    total_sessions = len(set(k.get("meta", {}).get("session_id", "") for k in all_kos)) or 1
    cross_session_survival = min(1.0, len(cross_sessions) / max(1, total_sessions - 1))

    # 2. Independent confirmation: distinct agents/models that produced
    #    SUPPORTS or CONVERGES_WITH edges
    incoming = [e for e in all_edges if e.get("target") == ko_id]
    confirming_agents = set()
    for e in incoming:
        if e.get("type") in ("SUPPORTS", "CONVERGES_WITH"):
            confirming_agents.add(e.get("created_by", ""))
    independent_confirmation = min(1.0, len(confirming_agents) / 3.0)

    # 3. Relational centrality: degree normalized by max possible
    outgoing = [e for e in all_edges if e.get("source") == ko_id]
    degree = len(incoming) + len(outgoing)
    max_degree = max(1, max(
        sum(1 for e in all_edges if e.get("source") == k["id"] or e.get("target") == k["id"])
        for k in all_kos
    )) if all_kos else 1
    relational_centrality = min(1.0, degree / max_degree)

    # 4. Methodological stability: K-score variance proxy
    #    High K with low contradiction = stable
    k = ko.get("scores", {}).get("K", 0.0)
    contradiction = ko.get("scores", {}).get("contradiction", 0.0)
    methodological_stability = k * (1.0 - contradiction)

    score = (
        w["cross_session_survival"] * cross_session_survival
        + w["independent_confirmation"] * independent_confirmation
        + w["relational_centrality"] * relational_centrality
        + w["methodological_stability"] * methodological_stability
    )

    return {
        "consolidation_score": round(score, 4),
        "components": {
            "cross_session_survival": round(cross_session_survival, 4),
            "independent_confirmation": round(independent_confirmation, 4),
            "relational_centrality": round(relational_centrality, 4),
            "methodological_stability": round(methodological_stability, 4),
        },
        "eligible_for_canonical": score >= config.CONSOLIDATION_THRESHOLD,
    }


def promote_working_to_event(session_id):
    """Promote all working KOs from a completed session to event regime.

    Called at session end.
    """
    kos = store.query_kos(regime="working", session_id=session_id)
    promoted = 0
    for ko in kos:
        ko["regime"] = "event"
        ko["meta"]["updated_at"] = datetime.now(timezone.utc).isoformat()
        store.upsert_ko(ko)
        promoted += 1
    return {"promoted": promoted, "session_id": session_id}


def check_canonical_promotions():
    """Check all event KOs for canonical promotion eligibility.

    Returns list of promoted KO IDs.
    """
    all_kos = store.load_kos()
    all_edges = store.load_edges()
    event_kos = [ko for ko in all_kos if ko.get("regime") == "event"]

    promoted = []
    for ko in event_kos:
        # Only promote DECISION, EVIDENCE, CONSTRAINT, NARRATIVE classes
        if ko.get("class") not in ("DECISION", "EVIDENCE", "CONSTRAINT", "NARRATIVE"):
            continue

        result = compute_consolidation_score(ko, all_kos, all_edges)
        if result["eligible_for_canonical"]:
            ko["regime"] = "canonical"
            ko["meta"]["updated_at"] = datetime.now(timezone.utc).isoformat()
            store.upsert_ko(ko)
            promoted.append({
                "id": ko["id"],
                "class": ko["class"],
                "summary": ko.get("summary", ""),
                "consolidation_score": result["consolidation_score"],
            })

    return promoted


def detect_tacit_patterns(min_sessions=5):
    """Detect statistical patterns across sessions for tacit promotion.

    Tacit KOs are meta-patterns: "topological analogies work better for
    material science transfers", "hypotheses with mechanism clarity > 7
    survive 3x more".
    """
    all_kos = store.load_kos()
    all_edges = store.load_edges()

    # Count sessions
    sessions = set(ko.get("meta", {}).get("session_id", "") for ko in all_kos)
    if len(sessions) < min_sessions:
        return []

    # Look for NARRATIVE/DECISION KOs that appear across many sessions
    candidates = [
        ko for ko in all_kos
        if ko.get("class") in ("NARRATIVE", "DECISION")
        and ko.get("regime") == "event"
    ]

    promoted = []
    for ko in candidates:
        connected_sessions = _get_sessions_containing(ko["id"], all_edges)
        if len(connected_sessions) >= min_sessions:
            ko["regime"] = "tacit"
            ko["meta"]["updated_at"] = datetime.now(timezone.utc).isoformat()
            store.upsert_ko(ko)
            promoted.append({
                "id": ko["id"],
                "class": ko["class"],
                "summary": ko.get("summary", ""),
                "sessions_connected": len(connected_sessions),
            })

    return promoted


def archive_stale_kos():
    """Archive event KOs older than 180 days with K < 0.15.

    Archived KOs are retained in storage but excluded from retrieval
    unless explicitly queried.
    """
    all_kos = store.load_kos()
    archived = []

    for ko in all_kos:
        if ko.get("regime") != "event":
            continue
        if _age_days(ko) < config.ARCHIVAL_AGE_DAYS:
            continue
        if ko.get("scores", {}).get("K", 1.0) >= config.ARCHIVAL_K_THRESHOLD:
            continue

        ko["meta"]["survival_status"] = "archived"
        ko["meta"]["updated_at"] = datetime.now(timezone.utc).isoformat()
        store.upsert_ko(ko)
        archived.append(ko["id"])

    return {"archived_count": len(archived), "ko_ids": archived}


def run_lifecycle(session_id=None):
    """Run full lifecycle management.

    1. Promote working → event (if session_id provided)
    2. Check canonical promotions
    3. Detect tacit patterns
    4. Archive stale KOs
    """
    results = {}

    if session_id:
        results["working_to_event"] = promote_working_to_event(session_id)

    results["canonical_promotions"] = check_canonical_promotions()
    results["tacit_detections"] = detect_tacit_patterns()
    results["archival"] = archive_stale_kos()

    return results
