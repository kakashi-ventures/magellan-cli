"""Graph store for Knowledge Objects and edges.

File-based JSON storage in knowledge/graph/. Consistent with MAGELLAN's
existing state management pattern (state/session.json, knowledge/discovery-log.json).
"""

import json
import os
from datetime import datetime, timezone

from . import config


def _ensure_dir():
    os.makedirs(config.GRAPH_DIR, exist_ok=True)


def _read_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def _write_json(path, data):
    _ensure_dir()
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


# --- KO Operations ---

def load_kos():
    """Load all KOs from disk."""
    return _read_json(config.KOS_PATH)


def save_kos(kos):
    """Write all KOs to disk."""
    _write_json(config.KOS_PATH, kos)


def get_ko(ko_id):
    """Get a single KO by ID."""
    for ko in load_kos():
        if ko["id"] == ko_id:
            return ko
    return None


def upsert_ko(ko):
    """Insert or update a KO. Matches on id."""
    kos = load_kos()
    for i, existing in enumerate(kos):
        if existing["id"] == ko["id"]:
            kos[i] = ko
            save_kos(kos)
            return
    kos.append(ko)
    save_kos(kos)


def query_kos(cls=None, regime=None, min_k=None, session_id=None, agent=None):
    """Query KOs with optional filters."""
    results = load_kos()
    if cls:
        results = [ko for ko in results if ko.get("class") == cls]
    if regime:
        if isinstance(regime, list):
            results = [ko for ko in results if ko.get("regime") in regime]
        else:
            results = [ko for ko in results if ko.get("regime") == regime]
    if min_k is not None:
        results = [ko for ko in results if ko.get("scores", {}).get("K", 0) >= min_k]
    if session_id:
        results = [ko for ko in results if ko.get("meta", {}).get("session_id") == session_id]
    if agent:
        results = [ko for ko in results if ko.get("meta", {}).get("agent") == agent]
    return results


# --- Edge Operations ---

def load_edges():
    """Load all edges from disk."""
    return _read_json(config.EDGES_PATH)


def save_edges(edges):
    """Write all edges to disk."""
    _write_json(config.EDGES_PATH, edges)


def add_edge(edge):
    """Add an edge. Deduplicates by id."""
    edges = load_edges()
    for existing in edges:
        if existing["id"] == edge["id"]:
            return  # already exists
    edges.append(edge)
    save_edges(edges)


def get_edges_for(ko_id, direction="both"):
    """Get edges involving a KO.

    direction: 'incoming' (target=ko_id), 'outgoing' (source=ko_id), 'both'
    """
    edges = load_edges()
    results = []
    for e in edges:
        if direction in ("both", "incoming") and e.get("target") == ko_id:
            results.append(e)
        if direction in ("both", "outgoing") and e.get("source") == ko_id:
            results.append(e)
    return results


def get_edges_by_type(edge_type):
    """Get all edges of a given type."""
    return [e for e in load_edges() if e.get("type") == edge_type]


# --- Index Operations ---

def build_adjacency_index():
    """Build adjacency lists for efficient graph traversal.

    Returns: {ko_id: {"incoming": [edges], "outgoing": [edges]}}
    """
    edges = load_edges()
    index = {}
    for e in edges:
        src, tgt = e.get("source"), e.get("target")
        if src not in index:
            index[src] = {"incoming": [], "outgoing": []}
        if tgt not in index:
            index[tgt] = {"incoming": [], "outgoing": []}
        index[src]["outgoing"].append(e)
        index[tgt]["incoming"].append(e)
    return index


def graph_stats():
    """Return summary statistics about the graph."""
    kos = load_kos()
    edges = load_edges()
    class_counts = {}
    regime_counts = {}
    for ko in kos:
        c = ko.get("class", "UNKNOWN")
        r = ko.get("regime", "unknown")
        class_counts[c] = class_counts.get(c, 0) + 1
        regime_counts[r] = regime_counts.get(r, 0) + 1
    edge_type_counts = {}
    for e in edges:
        t = e.get("type", "UNKNOWN")
        edge_type_counts[t] = edge_type_counts.get(t, 0) + 1
    return {
        "total_kos": len(kos),
        "total_edges": len(edges),
        "by_class": class_counts,
        "by_regime": regime_counts,
        "by_edge_type": edge_type_counts,
    }


# --- Factory Helpers ---

def make_ko_id(session_id, cls, seq):
    """Generate a KO ID. e.g. KO-MAG-S22-H-003"""
    prefix = session_id.replace("-", "")[:8] if session_id else "UNKNOWN"
    class_initial = cls[0] if cls else "X"
    return f"KO-MAG-{prefix}-{class_initial}-{seq:03d}"


def make_edge_id(source_id, edge_type, target_id):
    """Generate an edge ID."""
    return f"E-{source_id}-{edge_type}-{target_id}"


def make_ko(ko_id, cls, content, summary, session_id, cycle, agent,
            regime="working", confidence=0.5, koc=None, depth="mechanism",
            entity="", domain="", source_ko_id=None):
    """Create a new KO with proper defaults."""
    now = datetime.now(timezone.utc).isoformat()
    epoch = f"{session_id}-C{cycle}" if session_id else "unknown"
    variant = "v1-original"

    if not koc:
        koc = f"{entity}|{domain}|{cls}|{epoch}|{depth}|{agent}|{variant}"

    return {
        "id": ko_id,
        "koc": koc,
        "class": cls,
        "regime": regime,
        "content": content,
        "summary": summary[:200] if summary else content[:200],
        "scores": {
            "K": config.SEED_K.get(cls, 0.5),
            "confidence": confidence,
            "freshness": 1.0,
            "urgency": 0.0,
            "contradiction": 0.0,
        },
        "meta": {
            "session_id": session_id,
            "cycle": cycle,
            "agent": agent,
            "model": "claude-opus-4-6" if agent in (
                "scout", "generator", "critic", "quality-gate",
                "target-evaluator", "holdout-evaluator",
            ) else "claude-sonnet-4-6",
            "created_at": now,
            "updated_at": now,
            "quality_gate_score": None,
            "survival_status": "pending",
            "evolution_count": 0,
            "source_ko_id": source_ko_id,
        },
    }


def make_edge(source_id, edge_type, target_id, created_by, evidence=None):
    """Create a new edge with proper defaults."""
    return {
        "id": make_edge_id(source_id, edge_type, target_id),
        "type": edge_type,
        "source": source_id,
        "target": target_id,
        "coeff": config.EDGE_COEFFICIENTS.get(edge_type, 0.0),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "created_by": created_by,
        "evidence": evidence,
    }
