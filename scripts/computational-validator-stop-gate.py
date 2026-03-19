#!/usr/bin/env python3
"""Computational Validator SubagentStop gate. WARN-ONLY — never blocks.
Reports computational readiness status for pipeline awareness."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        cv = d.get("computational_readiness", {})

        if not cv:
            print(json.dumps({
                "feedback": "WARNING: computational-validator produced no readiness data. Proceeding anyway."
            }))
            sys.exit(0)

        # Summarize checks
        checks = []
        if "kegg_cross_check" in cv:
            kegg = cv["kegg_cross_check"]
            connected = kegg.get("connected", False)
            checks.append(f"KEGG: {'connected' if connected else 'not connected'}")

        if "string_scores" in cv:
            string = cv["string_scores"]
            max_score = string.get("max_interaction", 0)
            checks.append(f"STRING: max={max_score}")

        if "pubmed_cooccurrence" in cv:
            pubmed = cv["pubmed_cooccurrence"]
            count = pubmed.get("count", -1)
            checks.append(f"PubMed co-occurrence: {count}")

        if "quantitative_checks" in cv:
            quant = cv["quantitative_checks"]
            if isinstance(quant, list):
                plausible = sum(1 for q in quant if isinstance(q, dict) and q.get("result") == "plausible")
                checks.append(f"Quantitative: {plausible}/{len(quant)} plausible")

        summary = "; ".join(checks) if checks else "no checks completed"
        print(json.dumps({
            "feedback": f"Computational validator PASSED (warn-only): {summary}"
        }))
        sys.exit(0)
    else:
        print(json.dumps({
            "feedback": "WARNING: state/session.json not found. Allowing through."
        }))
        sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: computational-validator gate error: {e}. Allowing through."}))
    sys.exit(0)
