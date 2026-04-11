"""Epistemic infrastructure constants.

All values derived from OIDA × MAGELLAN architecture spec (§2-4).
Runtime overrides loaded from prompts/epistemic-config.json.
"""

import json
import os

# --- Epistemic Classes ---

CLASSES = [
    "QUESTION", "HYPOTHESIS", "OBSERVATION", "EVIDENCE", "EVALUATION",
    "DECISION", "CONSTRAINT", "NARRATIVE", "PLAN",
]

SEED_K = {
    "QUESTION": 0.30, "HYPOTHESIS": 0.30, "OBSERVATION": 0.40,
    "EVIDENCE": 0.80, "EVALUATION": 0.55, "DECISION": 1.00,
    "CONSTRAINT": 0.90, "NARRATIVE": 0.70, "PLAN": 0.65,
}

DECAY_TYPE = {
    "QUESTION": "inverse", "HYPOTHESIS": "exponential", "OBSERVATION": "exponential",
    "EVIDENCE": "exponential", "EVALUATION": "exponential", "DECISION": "none",
    "CONSTRAINT": "none", "NARRATIVE": "none", "PLAN": "exponential",
}

HALF_LIFE_DAYS = {
    "HYPOTHESIS": 120, "OBSERVATION": 180, "EVIDENCE": 730,
    "EVALUATION": 120, "PLAN": 90,
}

# --- Edge Vocabulary ---

EDGE_TYPES = [
    "SUPPORTS", "CONTRADICTS", "BASED_ON", "SUPERSEDES", "IMPLEMENTS",
    "BLOCKS", "REFINES", "ENABLES", "PRECEDES", "DERIVES_FROM",
    "CONVERGES_WITH", "ANALOGOUS_TO",
]

EDGE_COEFFICIENTS = {
    "SUPPORTS": 1.0, "CONTRADICTS": -0.6, "BASED_ON": 0.8,
    "SUPERSEDES": 0.6, "IMPLEMENTS": 0.7, "BLOCKS": -0.4,
    "REFINES": 0.5, "ENABLES": 0.4, "PRECEDES": 0.3,
    "DERIVES_FROM": 0.5, "CONVERGES_WITH": 0.9, "ANALOGOUS_TO": 0.3,
}

# --- Agent Routing ---

AGENT_RHO = {
    "scout": 0.90, "convergence-scanner": 0.90, "session-analyst": 0.85,
    "critic": 0.80, "evolver": 0.60, "generator": 0.55,
    "ranker": 0.45, "quality-gate": 0.35, "cross-model-validator": 0.25,
    "dataset-evidence-miner": 0.20, "orchestrator": 0.15,
}

AGENT_MAX_KOS = {
    "scout": 20, "generator": 15, "critic": 12, "evolver": 12,
    "quality-gate": 8, "ranker": 10, "cross-model-validator": 8,
    "dataset-evidence-miner": 8, "convergence-scanner": 15,
    "session-analyst": 15, "orchestrator": 7,
}

AGENT_REGIMES = {
    "scout":                  ["canonical", "event", "tacit"],
    "generator":              ["canonical", "event"],
    "critic":                 ["canonical", "event"],
    "evolver":                ["canonical", "event"],
    "quality-gate":           ["event"],
    "ranker":                 ["canonical", "event"],
    "cross-model-validator":  ["event"],
    "dataset-evidence-miner": ["event"],
    "convergence-scanner":    ["canonical", "event", "tacit"],
    "session-analyst":        ["canonical", "event", "tacit"],
    "orchestrator":           ["canonical", "event"],
}

# --- Regime Parameters ---

REGIME_GRAVITY = {
    "working": 0.0, "event": 1.0, "canonical": 1.6, "tacit": 0.8,
}

# --- Memory Zones ---

ZONE_THRESHOLDS = {"core": 0.40, "working": 0.15, "peripheral": 0.05, "dormant": 0.0}

# --- Consolidation ---

CONSOLIDATION_WEIGHTS = {
    "cross_session_survival": 0.30,
    "independent_confirmation": 0.25,
    "relational_centrality": 0.25,
    "methodological_stability": 0.20,
}
CONSOLIDATION_THRESHOLD = 0.70

# --- KGE Cycle ---

KGE_PROPAGATION_DAMPING = 0.15
KGE_MAX_DELTA = 0.10
KGE_CONVERGENCE_THRESHOLD = 0.001
KGE_MAX_ITERATIONS = 50

# --- QUESTION Urgency ---

URGENCY_AGE_DENOM = 20
URGENCY_AGE_WEIGHT = 0.30
URGENCY_BLOCKING_WEIGHT = 0.20
URGENCY_SALIENCE_WEIGHT = 0.50

# --- Pruning ---

WORKING_TTL_HOURS = 72
ARCHIVAL_AGE_DAYS = 180
ARCHIVAL_K_THRESHOLD = 0.15
DORMANT_K_THRESHOLD = 0.05

# --- Paths ---

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAPH_DIR = os.path.join(REPO_ROOT, "knowledge", "graph")
KOS_PATH = os.path.join(GRAPH_DIR, "kos.json")
EDGES_PATH = os.path.join(GRAPH_DIR, "edges.json")
CONFIG_PATH = os.path.join(REPO_ROOT, "prompts", "epistemic-config.json")


def load_runtime_config():
    """Load runtime overrides from prompts/epistemic-config.json if present."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}
