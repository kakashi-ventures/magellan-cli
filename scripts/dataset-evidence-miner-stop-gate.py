#!/usr/bin/env python3
"""Dataset Evidence Miner SubagentStop gate. WARN-ONLY — never blocks.
Checks that evidence report and JSON were produced."""
import sys, json, os

try:
    state_path = "state/session.json"
    results_dir = "results"

    if os.path.exists(state_path):
        d = json.load(open(state_path))
        results_dir = d.get("results_dir", "results")

    report = os.path.join(results_dir, "dataset-evidence-report.md")
    data = os.path.join(results_dir, "dataset-evidence.json")

    parts = []
    warnings = []

    if os.path.exists(data):
        size = os.path.getsize(data)
        parts.append(f"dataset-evidence.json={size}B")
        try:
            edata = json.load(open(data))
            ev = edata.get("dataset_evidence", {})
            agg = ev.get("aggregate", {})
            confirmed = agg.get("confirmed", 0)
            total = agg.get("total_claims", 0)
            parts.append(f"confirmed={confirmed}/{total}")
        except Exception:
            pass
    else:
        warnings.append("dataset-evidence.json not found")

    if os.path.exists(report):
        parts.append(f"report={os.path.getsize(report)}B")
    else:
        warnings.append("dataset-evidence-report.md not found")

    if warnings:
        parts.append(f"warnings=[{'; '.join(warnings)}]")

    print(json.dumps({
        "feedback": f"Dataset evidence miner PASSED: {', '.join(parts)}"
    }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: dataset-evidence-miner gate error: {e}. Allowing through."}))
    sys.exit(0)
