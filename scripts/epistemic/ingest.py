"""KO ingestion pipeline.

Converts MAGELLAN agent outputs (JSON files in results/{session-id}/) into
Knowledge Objects and edges in the epistemic graph.

Mapping (§2.5 of architecture spec):
  scout.json         → QUESTION, OBSERVATION, CONSTRAINT KOs
  cycle*-raw.json    → HYPOTHESIS KOs (BASED_ON → source observations)
  cycle*-critiqued   → EVALUATION KOs (CONTRADICTS/SUPPORTS → hypotheses)
  quality-gate.json  → EVALUATION KOs (composite assessments)
  cycle*-evolved     → HYPOTHESIS KOs (SUPERSEDES → previous versions)
  cross-model.json   → EVIDENCE KOs (SUPPORTS/CONVERGES_WITH)
  convergence.json   → NARRATIVE/EVIDENCE KOs (CONVERGES_WITH)
  dataset-evidence   → OBSERVATION/EVIDENCE KOs (SUPPORTS/CONTRADICTS)
  final.json         → Update survival_status on hypothesis KOs
"""

import json
import os
import re

from . import config
from . import store


class SessionIngester:
    """Ingests a single session's results into the KO graph."""

    def __init__(self, results_dir, session_id=None):
        self.results_dir = results_dir
        self.session_id = session_id or os.path.basename(results_dir)
        self._seq = {"Q": 0, "H": 0, "O": 0, "E": 0, "V": 0, "D": 0, "C": 0, "N": 0, "P": 0}
        self.created_kos = []
        self.created_edges = []

    def _next_id(self, cls):
        initial = cls[0]
        self._seq[initial] = self._seq.get(initial, 0) + 1
        prefix = self.session_id.replace("-", "")[:8]
        return f"KO-MAG-{prefix}-{initial}-{self._seq[initial]:03d}"

    def _read_json(self, filename):
        path = os.path.join(self.results_dir, filename)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return None

    def _create_ko(self, cls, content, summary, agent, cycle=1,
                   confidence=0.5, regime="event", depth="mechanism",
                   entity="", domain="", source_ko_id=None):
        ko_id = self._next_id(cls)
        ko = store.make_ko(
            ko_id=ko_id, cls=cls, content=content, summary=summary,
            session_id=self.session_id, cycle=cycle, agent=agent,
            regime=regime, confidence=confidence, depth=depth,
            entity=entity, domain=domain, source_ko_id=source_ko_id,
        )
        store.upsert_ko(ko)
        self.created_kos.append(ko_id)
        return ko_id

    def _create_edge(self, source_id, edge_type, target_id, created_by, evidence=None):
        edge = store.make_edge(source_id, edge_type, target_id, created_by, evidence)
        store.add_edge(edge)
        self.created_edges.append(edge["id"])
        return edge["id"]

    def ingest_scout(self):
        """Ingest scout.json → QUESTION + OBSERVATION + CONSTRAINT KOs."""
        data = self._read_json("scout.json")
        if not data:
            return []

        ko_ids = []
        targets = data if isinstance(data, list) else data.get("targets", [data])

        for target in targets:
            field_a = target.get("field_a", "")
            field_c = target.get("field_c", "")
            bridges = target.get("bridge_concepts", [])
            strategy = target.get("strategy", "")
            domain = f"{field_a}×{field_c}" if field_a and field_c else ""

            # Main QUESTION KO
            q_content = (
                f"Can {', '.join(bridges)} bridge {field_a} and {field_c}? "
                f"Strategy: {strategy}. "
                f"Disjointness: {target.get('disjointness_status', 'unknown')}."
            )
            q_summary = f"[{strategy}] {field_a} × {field_c} via {', '.join(bridges[:2])}"
            q_id = self._create_ko(
                "QUESTION", q_content, q_summary, "scout",
                depth="observation", domain=domain,
                entity="-".join(bridges[:2]).lower().replace(" ", "-") if bridges else "unknown",
            )
            ko_ids.append(q_id)

            # Bridge concepts as OBSERVATION KOs
            for bridge in bridges:
                o_content = f"Bridge concept '{bridge}' identified between {field_a} and {field_c}."
                o_id = self._create_ko(
                    "OBSERVATION", o_content, f"Bridge: {bridge} ({field_a}↔{field_c})",
                    "scout", depth="observation", domain=domain,
                )
                ko_ids.append(o_id)
                self._create_edge(q_id, "BASED_ON", o_id, "scout")

            # Constraints from target metadata
            for constraint in target.get("constraints", []):
                c_id = self._create_ko(
                    "CONSTRAINT", constraint, constraint[:200],
                    "scout", depth="theory", confidence=0.9,
                )
                ko_ids.append(c_id)

        return ko_ids

    def ingest_hypotheses(self, cycle=1):
        """Ingest cycle{N}-raw.json → HYPOTHESIS KOs."""
        filename = f"cycle{cycle}-raw.json"
        data = self._read_json(filename)
        if not data:
            return []

        ko_ids = []
        hypotheses = data if isinstance(data, list) else data.get("hypotheses", [data])

        for hyp in hypotheses:
            title = hyp.get("title", "Untitled hypothesis")
            mechanism = hyp.get("mechanism", hyp.get("description", ""))
            content = f"{title}\n\nMechanism: {mechanism}"
            if hyp.get("test_protocol"):
                content += f"\n\nTest protocol: {hyp['test_protocol']}"

            confidence = hyp.get("confidence", 0.5)
            if isinstance(confidence, str):
                try:
                    confidence = float(confidence.strip("%")) / 100
                except (ValueError, AttributeError):
                    confidence = 0.5

            h_id = self._create_ko(
                "HYPOTHESIS", content, title[:200], "generator",
                cycle=cycle, confidence=min(1.0, max(0.0, confidence)),
                depth="mechanism",
            )
            ko_ids.append(h_id)

            # Link to scout QUESTION KOs from this session
            scout_questions = store.query_kos(
                cls="QUESTION", session_id=self.session_id
            )
            for q in scout_questions:
                self._create_edge(h_id, "BASED_ON", q["id"], "generator")

        return ko_ids

    def ingest_critiques(self, cycle=1):
        """Ingest cycle{N}-critiqued.json → EVALUATION KOs with edges."""
        filename = f"cycle{cycle}-critiqued.json"
        data = self._read_json(filename)
        if not data:
            return []

        ko_ids = []
        hypotheses = data if isinstance(data, list) else data.get("hypotheses", [data])

        # Get hypothesis KOs from this session to link
        session_hypotheses = store.query_kos(
            cls="HYPOTHESIS", session_id=self.session_id
        )
        hyp_by_title = {}
        for h in session_hypotheses:
            title_line = h.get("content", "").split("\n")[0]
            hyp_by_title[title_line.lower().strip()] = h["id"]

        for hyp in hypotheses:
            title = hyp.get("title", "")
            attacks = hyp.get("critique", hyp.get("attacks", hyp.get("evaluation", "")))
            verdict = hyp.get("verdict", hyp.get("survival", "unknown"))

            content = f"Critique of '{title}': {attacks}"
            e_id = self._create_ko(
                "EVALUATION", content, f"Critique: {title[:150]}",
                "critic", cycle=cycle, confidence=0.7,
            )
            ko_ids.append(e_id)

            # Link to target hypothesis
            target_id = hyp_by_title.get(title.lower().strip())
            if target_id:
                if verdict in ("killed", "failed", "rejected"):
                    self._create_edge(e_id, "CONTRADICTS", target_id, "critic")
                else:
                    self._create_edge(e_id, "SUPPORTS", target_id, "critic")

        return ko_ids

    def ingest_quality_gate(self):
        """Ingest quality-gate.json → EVALUATION KOs (composite)."""
        data = self._read_json("quality-gate.json")
        if not data:
            return []

        ko_ids = []
        hypotheses = data if isinstance(data, list) else data.get("hypotheses", data.get("results", []))
        if isinstance(hypotheses, dict):
            hypotheses = [hypotheses]

        for hyp in hypotheses:
            title = hyp.get("title", hyp.get("hypothesis", ""))
            score = hyp.get("composite_score", hyp.get("score", hyp.get("composite", 0)))
            verdict = hyp.get("verdict", "unknown")

            content = (
                f"Quality Gate assessment of '{title}': "
                f"Score {score}/10, Verdict: {verdict}"
            )
            e_id = self._create_ko(
                "EVALUATION", content, f"QG: {title[:120]} [{score}/10, {verdict}]",
                "quality-gate", confidence=0.8,
            )
            ko_ids.append(e_id)

            # Update hypothesis survival status
            session_hyps = store.query_kos(cls="HYPOTHESIS", session_id=self.session_id)
            for h in session_hyps:
                if title.lower() in h.get("content", "").lower():
                    h["meta"]["quality_gate_score"] = score
                    h["meta"]["survival_status"] = (
                        "survived" if verdict.lower() in ("pass", "conditional_pass", "conditional pass")
                        else "killed"
                    )
                    store.upsert_ko(h)
                    edge_type = "SUPPORTS" if "pass" in verdict.lower() else "CONTRADICTS"
                    self._create_edge(e_id, edge_type, h["id"], "quality-gate")
                    break

        return ko_ids

    def ingest_evolved(self, cycle=2):
        """Ingest cycle{N}-evolved.json → new HYPOTHESIS KOs with SUPERSEDES edges."""
        filename = f"cycle{cycle}-evolved.json"
        data = self._read_json(filename)
        if not data:
            return []

        ko_ids = []
        hypotheses = data if isinstance(data, list) else data.get("hypotheses", [data])

        for hyp in hypotheses:
            title = hyp.get("title", "")
            mechanism = hyp.get("mechanism", hyp.get("description", ""))
            parent_title = hyp.get("parent", hyp.get("evolved_from", ""))

            content = f"{title}\n\nMechanism: {mechanism}"
            h_id = self._create_ko(
                "HYPOTHESIS", content, f"[evolved] {title[:180]}", "evolver",
                cycle=cycle, depth="mechanism",
            )
            ko_ids.append(h_id)

            # Link SUPERSEDES to parent hypothesis
            if parent_title:
                session_hyps = store.query_kos(cls="HYPOTHESIS", session_id=self.session_id)
                for parent in session_hyps:
                    if parent_title.lower() in parent.get("content", "").lower():
                        self._create_edge(h_id, "SUPERSEDES", parent["id"], "evolver")
                        parent["meta"]["evolution_count"] = parent["meta"].get("evolution_count", 0) + 1
                        store.upsert_ko(parent)
                        break

        return ko_ids

    def ingest_cross_model(self):
        """Ingest cross-model.json → EVIDENCE KOs."""
        data = self._read_json("cross-model.json")
        if not data:
            return []

        ko_ids = []
        results = data if isinstance(data, list) else data.get("results", data.get("hypotheses", [data]))
        if isinstance(results, dict):
            results = [results]

        for result in results:
            title = result.get("title", result.get("hypothesis", ""))
            gpt_verdict = result.get("gpt_verdict", result.get("gpt", ""))
            gemini_verdict = result.get("gemini_verdict", result.get("gemini", ""))
            consensus = result.get("consensus", "")

            content = (
                f"Cross-model validation of '{title}': "
                f"GPT: {gpt_verdict}. Gemini: {gemini_verdict}. "
                f"Consensus: {consensus}"
            )
            ev_id = self._create_ko(
                "EVIDENCE", content, f"Cross-model: {title[:140]}", "cross-model-validator",
                confidence=0.75,
            )
            ko_ids.append(ev_id)

            # Link to hypothesis
            session_hyps = store.query_kos(cls="HYPOTHESIS", session_id=self.session_id)
            for h in session_hyps:
                if title.lower() in h.get("content", "").lower():
                    self._create_edge(ev_id, "SUPPORTS", h["id"], "cross-model-validator")
                    break

        return ko_ids

    def ingest_convergence(self):
        """Ingest convergence.json → EVIDENCE/NARRATIVE KOs with CONVERGES_WITH."""
        data = self._read_json("convergence.json")
        if not data:
            return []

        ko_ids = []
        signals = data if isinstance(data, list) else data.get("signals", data.get("results", []))
        if isinstance(signals, dict):
            signals = [signals]

        for signal in signals:
            title = signal.get("title", signal.get("hypothesis", ""))
            source_type = signal.get("source", signal.get("type", ""))
            evidence_text = signal.get("evidence", signal.get("description", ""))
            strength = signal.get("strength", "moderate")

            cls = "EVIDENCE" if strength in ("strong", "confirmed") else "NARRATIVE"
            content = f"Convergence signal for '{title}' from {source_type}: {evidence_text}"
            c_id = self._create_ko(
                cls, content, f"Convergence [{strength}]: {title[:130]}",
                "convergence-scanner", confidence=0.6 if strength == "moderate" else 0.8,
            )
            ko_ids.append(c_id)

        return ko_ids

    def ingest_dataset_evidence(self):
        """Ingest dataset-evidence.json → OBSERVATION/EVIDENCE KOs."""
        data = self._read_json("dataset-evidence.json")
        if not data:
            return []

        ko_ids = []
        claims = data if isinstance(data, list) else data.get("claims", data.get("results", []))
        if isinstance(claims, dict):
            claims = [claims]

        for claim in claims:
            hypothesis = claim.get("hypothesis", claim.get("title", ""))
            db_source = claim.get("database", claim.get("source", ""))
            result = claim.get("result", claim.get("finding", ""))
            confirmed = claim.get("confirmed", claim.get("status", "")) in (
                True, "confirmed", "supported"
            )

            cls = "EVIDENCE" if confirmed else "OBSERVATION"
            content = f"Dataset evidence for '{hypothesis}' from {db_source}: {result}"
            d_id = self._create_ko(
                cls, content, f"[{db_source}] {hypothesis[:150]}",
                "dataset-evidence-miner", confidence=0.7 if confirmed else 0.4,
            )
            ko_ids.append(d_id)

            # Link to hypothesis
            session_hyps = store.query_kos(cls="HYPOTHESIS", session_id=self.session_id)
            for h in session_hyps:
                if hypothesis.lower() in h.get("content", "").lower():
                    edge_type = "SUPPORTS" if confirmed else "CONTRADICTS"
                    self._create_edge(d_id, edge_type, h["id"], "dataset-evidence-miner")
                    break

        return ko_ids

    def ingest_session_meta(self):
        """Create meta-learning KOs from session analyst output."""
        data = self._read_json("final.json")
        if not data:
            return []

        ko_ids = []
        summary = data.get("summary", {})
        status = summary.get("session_status", data.get("status", ""))

        # Session NARRATIVE KO
        n_content = (
            f"Session {self.session_id}: {status}. "
            f"Generated {summary.get('total_hypotheses', '?')} hypotheses, "
            f"{summary.get('passed_quality_gate', '?')} passed QG."
        )
        n_id = self._create_ko(
            "NARRATIVE", n_content, f"Session {self.session_id} summary",
            "session-analyst", regime="event",
        )
        ko_ids.append(n_id)

        return ko_ids

    def ingest_all(self):
        """Run full ingestion pipeline for a session."""
        all_ids = []
        all_ids.extend(self.ingest_scout())
        all_ids.extend(self.ingest_hypotheses(cycle=1))
        all_ids.extend(self.ingest_critiques(cycle=1))
        all_ids.extend(self.ingest_hypotheses(cycle=2))
        all_ids.extend(self.ingest_evolved(cycle=2))
        all_ids.extend(self.ingest_critiques(cycle=2))
        all_ids.extend(self.ingest_quality_gate())
        all_ids.extend(self.ingest_cross_model())
        all_ids.extend(self.ingest_convergence())
        all_ids.extend(self.ingest_dataset_evidence())
        all_ids.extend(self.ingest_session_meta())

        # Promote all session KOs from working to event
        for ko_id in all_ids:
            ko = store.get_ko(ko_id)
            if ko and ko.get("regime") == "working":
                ko["regime"] = "event"
                store.upsert_ko(ko)

        return {
            "session_id": self.session_id,
            "kos_created": len(self.created_kos),
            "edges_created": len(self.created_edges),
            "ko_ids": self.created_kos,
            "edge_ids": self.created_edges,
        }
