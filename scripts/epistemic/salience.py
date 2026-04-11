"""Dual-salience computation engine.

Computes epistemic (S_epi) and action (S_act) salience for each KO,
combined via agent-specific ρ weighting (§4 of architecture spec).

S = ρ * S_epi + (1 - ρ) * S_act

Epistemic salience rewards: high urgency, contradiction tension,
freshness, surprise signals, and cross-domain connections.

Action salience rewards: high K-score, task relevance, freshness,
and low contradiction (stable knowledge).
"""

import math

from . import config
from . import store


def compute_epistemic_salience(ko, adj_index=None):
    """Compute epistemic salience for a KO.

    S_epi = w_K * K + w_urg * urgency + w_contr * contradiction
            + w_fresh * freshness + w_surprise * surprise

    Epistemic agents need: gaps, tensions, novel signals.
    """
    scores = ko.get("scores", {})
    k = scores.get("K", 0.0)
    urgency = scores.get("urgency", 0.0)
    contradiction = scores.get("contradiction", 0.0)
    freshness = scores.get("freshness", 0.0)

    # Surprise: KOs with both SUPPORTS and CONTRADICTS edges
    surprise = 0.0
    if adj_index:
        ko_id = ko["id"]
        incoming = adj_index.get(ko_id, {}).get("incoming", [])
        has_support = any(e.get("type") == "SUPPORTS" for e in incoming)
        has_contradict = any(e.get("type") == "CONTRADICTS" for e in incoming)
        if has_support and has_contradict:
            surprise = 0.8  # Epistemic conflict = high surprise

    # For QUESTION class, urgency dominates
    if ko.get("class") == "QUESTION":
        return (0.15 * k + 0.40 * urgency + 0.10 * contradiction
                + 0.20 * freshness + 0.15 * surprise)

    # For HYPOTHESIS, contradiction and surprise dominate
    if ko.get("class") == "HYPOTHESIS":
        return (0.20 * k + 0.05 * urgency + 0.30 * contradiction
                + 0.20 * freshness + 0.25 * surprise)

    # Default: balanced
    return (0.25 * k + 0.15 * urgency + 0.20 * contradiction
            + 0.25 * freshness + 0.15 * surprise)


def compute_action_salience(ko, adj_index=None):
    """Compute action salience for a KO.

    S_act = w_K * K + w_fresh * freshness + w_stability * (1 - contradiction)
            + w_confidence * confidence

    Action agents need: reliable, high-confidence, stable knowledge.
    """
    scores = ko.get("scores", {})
    k = scores.get("K", 0.0)
    freshness = scores.get("freshness", 0.0)
    contradiction = scores.get("contradiction", 0.0)
    confidence = scores.get("confidence", 0.5)
    stability = 1.0 - contradiction

    # For EVIDENCE class, confidence and stability dominate
    if ko.get("class") == "EVIDENCE":
        return 0.30 * k + 0.15 * freshness + 0.25 * stability + 0.30 * confidence

    # For CONSTRAINT, K and stability dominate
    if ko.get("class") == "CONSTRAINT":
        return 0.35 * k + 0.10 * freshness + 0.35 * stability + 0.20 * confidence

    # Default: balanced toward reliability
    return 0.30 * k + 0.20 * freshness + 0.25 * stability + 0.25 * confidence


def compute_salience(ko, agent_id, adj_index=None):
    """Compute combined salience for a KO given an agent's ρ value.

    S = ρ * S_epi + (1 - ρ) * S_act
    """
    rho = config.AGENT_RHO.get(agent_id, 0.50)
    s_epi = compute_epistemic_salience(ko, adj_index)
    s_act = compute_action_salience(ko, adj_index)
    return rho * s_epi + (1.0 - rho) * s_act


def rank_kos_for_agent(agent_id, kos=None, adj_index=None):
    """Rank all eligible KOs by salience for a given agent.

    Applies regime filtering (agents only see allowed regimes)
    and returns sorted list with salience scores.
    """
    if kos is None:
        kos = store.load_kos()
    if adj_index is None:
        adj_index = store.build_adjacency_index()

    # Filter by allowed regimes
    allowed_regimes = config.AGENT_REGIMES.get(agent_id, ["canonical", "event"])
    eligible = [ko for ko in kos if ko.get("regime") in allowed_regimes]

    # Exclude dormant KOs (K < 0.05) unless agent is highly epistemic
    rho = config.AGENT_RHO.get(agent_id, 0.50)
    if rho < 0.80:
        eligible = [ko for ko in eligible
                    if ko.get("scores", {}).get("K", 0) >= config.DORMANT_K_THRESHOLD]

    # Compute salience and sort
    scored = []
    for ko in eligible:
        s = compute_salience(ko, agent_id, adj_index)
        scored.append((s, ko))

    scored.sort(key=lambda x: x[0], reverse=True)

    # Apply max KO limit
    max_kos = config.AGENT_MAX_KOS.get(agent_id, 10)
    return scored[:max_kos]
