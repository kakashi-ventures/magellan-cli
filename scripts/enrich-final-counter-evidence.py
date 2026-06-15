#!/usr/bin/env python3
"""
Carry the typed adversarial record (counter-evidence / contradictions) through to final.json.

WHY
  MAGELLAN generates rich counter-evidence -- the Critic's per-vector attack findings and
  SURVIVE/WOUNDED/KILLED verdicts, the Quality Gate's per-claim failures and key risks -- and
  already persists it as TYPED JSON per phase (cycle*-critiqued.json, quality-gate.json). But
  final.json, the authoritative published artifact, drops every adversarial field, keeping only
  {id, verdict, composite, mechanism, ...}. That (a) violates the project rule "Every hypothesis
  MUST have ... counter-evidence" and (b) loses the contradictions that shaped each verdict, so a
  consumer of final.json sees the surviving conclusion but not the attacks it survived.

WHAT
  Enrich final.json IN PLACE by attaching a typed `counter_evidence` block to each hypothesis,
  assembled DETERMINISTICALLY from JSON sources ONLY -- never by scraping markdown. Deterministic
  assembly is compression-immune and reproducible (no LLM re-derivation of facts already on disk).

SCHEMA TOLERANCE (intentional)
  The Critic and Quality Gate JSON schemas are NOT stable across sessions/pipeline versions:
    quality-gate.json : hypotheses[]  with claims_failed/claims_unverifiable/verdict_rationale/rubric_scores
                        OR gated_hypotheses[] with fail_reasons/rubric_details/conditions_for_conditional_pass
    cycle*-critiqued.json : {attacks_summary, survival_note, revised_confidence}   (cycle-2 shape)
                        OR {attack_findings, severity_per_attack, key_recoverable_weakness}  (cycle-1 shape)
  This script normalizes across all observed variants via candidate-field lookup, so the block
  populates regardless of which pipeline version produced the session.

SOURCES (matched to each final hypothesis by id, then by cycle-stripped id, then by title)
  quality-gate.json  -> verdict, verdict_rationale, key_risk, claims_failed, claims_unverifiable,
                        conditions, counter_evidence_handling score   (QG pool: always present)
  cycle*-critiqued.json -> Critic verdict + per-vector attacks + survival note + critic_questions.

USAGE
  enrich-final-counter-evidence.py [results_dir] [--check]
    results_dir : path to results/{session-id}/ (default: current directory)
    --check     : report coverage and print one sample block to stdout; DO NOT write final.json.

  Idempotent: re-running refreshes the block deterministically. A one-time final.json.bak is kept.
  Exit 0 on success; 1 if final.json or quality-gate.json is missing.
"""
import sys
import os
import json
import glob
import re


def _norm(s):
    """Normalize an id/title for fallback matching: lowercase alphanumerics only."""
    return "".join(ch for ch in str(s).lower() if ch.isalnum())


def _strip_cycle_prefix(ident):
    """'C1-H4' -> 'h4' so a final id matches a Critic record keyed 'H4'."""
    return _norm(re.sub(r"^[cC]\d+[-_]?", "", str(ident)))


def pick(d, *names, default=None):
    """First present, non-None value among candidate field names (schema tolerance)."""
    for n in names:
        if isinstance(d, dict) and d.get(n) is not None:
            return d.get(n)
    return default


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def record_list(obj, *keys):
    """Return a list of hypothesis records whether obj is a top-level list or a dict wrapping one."""
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for k in keys:
            v = obj.get(k)
            if isinstance(v, list):
                return v
    return []


def qg_hypotheses(qg):
    """Per-hypothesis list across QG schema variants (hypotheses / gated_hypotheses)."""
    return record_list(qg, "hypotheses", "gated_hypotheses", "gated")


def build_qg_index(qg):
    by_id, by_title = {}, {}
    for h in qg_hypotheses(qg):
        if not isinstance(h, dict):
            continue
        by_id[h.get("id")] = h
        by_title[_norm(h.get("title"))] = h
    return by_id, by_title


def normalize_critic_record(rec, source_file):
    """Collapse the two Critic schemas (cycle1 attack_findings / cycle2 attacks_summary) into one shape."""
    attacks = pick(rec, "attacks_summary", "attack_findings", "attack_results", default={})
    severity = rec.get("severity_per_attack")
    survival = pick(rec, "survival_note", "key_recoverable_weakness",
                    "conditions_for_survival", "key_weaknesses")
    out = {
        "verdict": rec.get("verdict"),
        "revised_confidence": rec.get("revised_confidence"),
        "attacks": attacks or {},
        "survival_note": survival,
        "critic_questions": rec.get("critic_questions", []),
        "source": os.path.basename(source_file),
    }
    if severity:
        out["attack_severity"] = severity
    if rec.get("kill_reasons"):
        out["kill_reasons"] = rec.get("kill_reasons")
    return out


def build_critic_index(results_dir):
    """id/title -> normalized critic record across every cycle*-critiqued.json. Latest cycle wins."""
    by_id, by_title = {}, {}
    for f in sorted(glob.glob(os.path.join(results_dir, "cycle*-critiqued.json"))):
        try:
            raw = load_json(f)
        except (ValueError, OSError):
            continue
        for rec in record_list(raw, "critiqued_hypotheses", "hypotheses"):
            if not isinstance(rec, dict):
                continue
            norm = normalize_critic_record(rec, f)
            if rec.get("id") is not None:
                by_id[rec["id"]] = norm
            if rec.get("title"):
                by_title[_norm(rec["title"])] = norm
    return by_id, by_title


def lookup(by_id, by_title, ident, title):
    """Match by exact id, then normalized id, then cycle-stripped id, then normalized title."""
    if ident in by_id:
        return by_id[ident]
    nid = _norm(ident)
    sid = _strip_cycle_prefix(ident)
    for k, v in by_id.items():
        if _norm(k) in (nid, sid) or _strip_cycle_prefix(k) in (nid, sid):
            return v
    return by_title.get(_norm(title))


def ce_handling_score(qg_rec):
    """Best-effort extraction of the counter-evidence-handling rubric score across rubric schemas."""
    for key in ("rubric_scores", "rubric_details", "rubric"):
        rub = qg_rec.get(key)
        if isinstance(rub, dict):
            v = pick(rub, "counter_evidence_handling", "counter_evidence", "counterevidence")
            if v is not None:
                return v
    return None


def is_covered(block):
    """A hypothesis carries real adversarial signal if QG flagged risk/failures or the Critic attacked it."""
    qg = block.get("qg", {})
    cr = block.get("critic")
    if qg.get("claims_failed") or qg.get("claims_unverifiable") or qg.get("key_risk") or qg.get("conditions"):
        return True
    if cr and (cr.get("attacks") or cr.get("survival_note") or cr.get("critic_questions")):
        return True
    return False


def build_block(hyp, qg_by_id, qg_by_title, cr_by_id, cr_by_title):
    ident, title = hyp.get("id"), hyp.get("title")
    qg = lookup(qg_by_id, qg_by_title, ident, title) or {}
    critic = lookup(cr_by_id, cr_by_title, ident, title)
    return {
        "qg": {
            "verdict": pick(qg, "verdict"),
            "verdict_rationale": pick(qg, "verdict_rationale", "novelty_justification"),
            "key_risk": pick(qg, "key_risk"),
            "claims_failed": pick(qg, "claims_failed", "fail_reasons", default=[]),
            "claims_unverifiable": pick(qg, "claims_unverifiable", default=[]),
            "conditions": pick(qg, "conditions_for_conditional_pass"),
            "counter_evidence_handling_score": ce_handling_score(qg),
        },
        "critic": critic,
        "_provenance": "deterministic merge of quality-gate.json + cycle*-critiqued.json (no markdown scraping)",
    }


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    results_dir = args[0] if args else os.getcwd()
    check_only = "--check" in flags

    final_path = os.path.join(results_dir, "final.json")
    qg_path = os.path.join(results_dir, "quality-gate.json")
    for p in (final_path, qg_path):
        if not os.path.exists(p):
            sys.stderr.write(f"[enrich-counter-evidence] missing required file: {p}\n")
            return 1

    final = load_json(final_path)
    qg_by_id, qg_by_title = build_qg_index(load_json(qg_path))
    cr_by_id, cr_by_title = build_critic_index(results_dir)

    covered, total = 0, len(final)
    sample = None
    for hyp in final:
        block = build_block(hyp, qg_by_id, qg_by_title, cr_by_id, cr_by_title)
        hyp["counter_evidence"] = block
        if is_covered(block):
            covered += 1
            if sample is None:
                sample = (hyp.get("id"), block)

    sess = os.path.basename(os.path.normpath(results_dir))
    print(f"[enrich-counter-evidence] {sess}: {covered}/{total} hypotheses carry adversarial signal; "
          f"markdown-scrape fallbacks: 0 (JSON sources only)")

    if check_only:
        if sample:
            sid, block = sample
            print(f"--- sample counter_evidence block ({sid}) ---")
            print(json.dumps(block, indent=2, ensure_ascii=False)[:2200])
        else:
            print("--- no hypothesis carried adversarial signal (check id/schema matching) ---")
        return 0

    bak = final_path + ".bak"
    if not os.path.exists(bak):
        with open(bak, "w", encoding="utf-8") as fh:
            json.dump(load_json(final_path), fh, indent=2, ensure_ascii=False)
    with open(final_path, "w", encoding="utf-8") as fh:
        json.dump(final, fh, indent=2, ensure_ascii=False)
    print(f"[enrich-counter-evidence] wrote {final_path} ({covered}/{total} enriched; backup at {os.path.basename(bak)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
