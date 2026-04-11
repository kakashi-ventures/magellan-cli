"""Knowledge Graph Engine (KGE) cycle runner.

Implements the core K-score update algorithm from OIDA, recalibrated for
scientific discovery (§2.3, §3.2 of architecture spec).

KGE cycle:
  1. Compute class-specific decay for each KO
  2. Propagate edge contributions (weighted coefficients)
  3. Apply regime gravity multipliers
  4. Update K-scores with damping and clamping
  5. Classify KOs into memory zones
  6. Update QUESTION urgency (inverse decay)
"""

import math
from datetime import datetime, timezone

from . import config
from . import store


def _age_days(created_at_str):
    """Compute age in days from ISO timestamp."""
    try:
        created = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return max(0.0, (now - created).total_seconds() / 86400.0)
    except (ValueError, TypeError, AttributeError):
        return 0.0


def _compute_decay(ko):
    """Compute decay delta for a KO based on its class.

    Returns the decayed K value (not a delta).
    """
    cls = ko.get("class", "")
    decay_type = config.DECAY_TYPE.get(cls, "none")
    seed_k = config.SEED_K.get(cls, 0.5)
    current_k = ko.get("scores", {}).get("K", seed_k)
    age = _age_days(ko.get("meta", {}).get("created_at"))

    if decay_type == "none":
        return current_k

    if decay_type == "exponential":
        half_life = config.HALF_LIFE_DAYS.get(cls, 120)
        if half_life <= 0:
            return current_k
        decay_factor = math.exp(-math.log(2) * age / half_life)
        return seed_k * decay_factor

    if decay_type == "inverse":
        # QUESTION: urgency grows, K is maintained via edge support
        return current_k

    return current_k


def _compute_urgency(ko, adj_index):
    """Compute urgency for QUESTION KOs (inverse decay — grows over time).

    urgency(t) = clamp(age/20 * 0.3 + B * 0.2 + S * 0.5, 0, 1)
    where B = blocking_factor, S = salience_factor
    """
    if ko.get("class") != "QUESTION":
        return ko.get("scores", {}).get("urgency", 0.0)

    age = _age_days(ko.get("meta", {}).get("created_at"))
    ko_id = ko["id"]

    # Blocking factor: fraction of outgoing edges that are BLOCKS
    edges = adj_index.get(ko_id, {}).get("outgoing", [])
    total_out = len(edges) if edges else 1
    blocking_count = sum(1 for e in edges if e.get("type") == "BLOCKS")
    blocking_factor = blocking_count / total_out

    # Salience factor: whether any HYPOTHESIS addresses this question
    incoming = adj_index.get(ko_id, {}).get("incoming", [])
    has_addressing = any(
        e.get("type") in ("IMPLEMENTS", "BASED_ON", "SUPPORTS")
        for e in incoming
    )
    salience_factor = 0.0 if has_addressing else 1.0

    urgency = (
        min(age / config.URGENCY_AGE_DENOM, 1.0) * config.URGENCY_AGE_WEIGHT
        + blocking_factor * config.URGENCY_BLOCKING_WEIGHT
        + salience_factor * config.URGENCY_SALIENCE_WEIGHT
    )
    return max(0.0, min(1.0, urgency))


def _compute_edge_delta(ko, adj_index, ko_lookup):
    """Compute K-score delta from incoming edges.

    For each incoming edge: delta += coeff * source.K * damping
    Mixed-sign edges can cancel out (critical for convergence at high degree).
    """
    ko_id = ko["id"]
    incoming = adj_index.get(ko_id, {}).get("incoming", [])
    if not incoming:
        return 0.0

    delta = 0.0
    for edge in incoming:
        source_ko = ko_lookup.get(edge.get("source"))
        if not source_ko:
            continue
        source_k = source_ko.get("scores", {}).get("K", 0.0)
        coeff = edge.get("coeff", config.EDGE_COEFFICIENTS.get(edge.get("type"), 0.0))
        # Apply regime gravity of source
        source_regime = source_ko.get("regime", "event")
        gravity = config.REGIME_GRAVITY.get(source_regime, 1.0)
        delta += coeff * source_k * gravity * config.KGE_PROPAGATION_DAMPING

    return delta


def _compute_contradiction(ko, adj_index):
    """Compute accumulated contradiction pressure from CONTRADICTS edges."""
    ko_id = ko["id"]
    incoming = adj_index.get(ko_id, {}).get("incoming", [])
    contradicts_count = sum(1 for e in incoming if e.get("type") == "CONTRADICTS")
    # Saturating function: 1 - exp(-0.5 * count)
    if contradicts_count == 0:
        return 0.0
    return 1.0 - math.exp(-0.5 * contradicts_count)


def _compute_freshness(ko):
    """Compute freshness score (1.0 = just created, decays over 30 days)."""
    age = _age_days(ko.get("meta", {}).get("created_at"))
    return math.exp(-math.log(2) * age / 30.0)


def _classify_zone(k_score):
    """Classify K-score into memory zone."""
    if k_score >= config.ZONE_THRESHOLDS["core"]:
        return "core"
    if k_score >= config.ZONE_THRESHOLDS["working"]:
        return "working"
    if k_score >= config.ZONE_THRESHOLDS["peripheral"]:
        return "peripheral"
    return "dormant"


def run_cycle(verbose=False):
    """Execute one KGE cycle over the entire graph.

    Returns: dict with cycle statistics.
    """
    kos = store.load_kos()
    if not kos:
        return {"status": "empty", "kos_processed": 0}

    edges = store.load_edges()
    adj_index = store.build_adjacency_index()
    ko_lookup = {ko["id"]: ko for ko in kos}

    now = datetime.now(timezone.utc).isoformat()
    stats = {
        "kos_processed": len(kos),
        "edges_processed": len(edges),
        "zone_distribution": {"core": 0, "working": 0, "peripheral": 0, "dormant": 0},
        "max_delta": 0.0,
        "updates": [],
    }

    for ko in kos:
        old_k = ko.get("scores", {}).get("K", 0.0)

        # Step 1: Class-specific decay
        decayed_k = _compute_decay(ko)

        # Step 2: Edge propagation
        edge_delta = _compute_edge_delta(ko, adj_index, ko_lookup)

        # Step 3: Regime gravity on self (canonical KOs resist decay)
        regime = ko.get("regime", "event")
        self_gravity = config.REGIME_GRAVITY.get(regime, 1.0)

        # Step 4: Combine — decay sets baseline, edges adjust, gravity modulates
        if regime == "working":
            # Working KOs don't participate in global gravity
            new_k = decayed_k
        else:
            new_k = decayed_k * self_gravity + edge_delta

        # Step 5: Clamp delta and final K
        delta = new_k - old_k
        clamped_delta = max(-config.KGE_MAX_DELTA, min(config.KGE_MAX_DELTA, delta))
        new_k = max(0.0, min(1.0, old_k + clamped_delta))

        # Step 6: Update scores
        ko["scores"]["K"] = round(new_k, 6)
        ko["scores"]["freshness"] = round(_compute_freshness(ko), 4)
        ko["scores"]["contradiction"] = round(_compute_contradiction(ko, adj_index), 4)
        ko["scores"]["urgency"] = round(_compute_urgency(ko, adj_index), 4)
        ko["meta"]["updated_at"] = now

        # Track stats
        zone = _classify_zone(new_k)
        stats["zone_distribution"][zone] += 1
        abs_delta = abs(new_k - old_k)
        if abs_delta > stats["max_delta"]:
            stats["max_delta"] = abs_delta

        if verbose and abs_delta > 0.001:
            stats["updates"].append({
                "id": ko["id"],
                "class": ko.get("class"),
                "old_K": round(old_k, 4),
                "new_K": round(new_k, 4),
                "delta": round(new_k - old_k, 4),
                "zone": zone,
            })

    # Write updated KOs
    store.save_kos(kos)

    stats["status"] = "completed"
    if not verbose:
        del stats["updates"]
    return stats


def run_until_convergence(max_iterations=None, verbose=False):
    """Run KGE cycles until K-scores converge or max iterations reached."""
    max_iter = max_iterations or config.KGE_MAX_ITERATIONS
    all_stats = []

    for i in range(max_iter):
        stats = run_cycle(verbose=verbose)
        stats["iteration"] = i + 1
        all_stats.append(stats)

        if stats.get("max_delta", 1.0) < config.KGE_CONVERGENCE_THRESHOLD:
            stats["converged"] = True
            break
    else:
        if all_stats:
            all_stats[-1]["converged"] = False

    return all_stats
