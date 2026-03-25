#!/usr/bin/env python3
"""Convergence Scanner SubagentStop gate. WARN-ONLY — never blocks.
Checks that convergence report and JSON were produced."""
import sys, json, os

try:
    state_path = "state/session.json"
    results_dir = "results"

    if os.path.exists(state_path):
        d = json.load(open(state_path))
        results_dir = d.get("results_dir", "results")

    report = os.path.join(results_dir, "convergence-report.md")
    data = os.path.join(results_dir, "convergence.json")

    parts = []
    warnings = []

    if os.path.exists(data):
        size = os.path.getsize(data)
        parts.append(f"convergence.json={size}B")
        try:
            cdata = json.load(open(data))
            conv = cdata.get("convergence", {})
            agg = conv.get("aggregate", {})
            strong = agg.get("strong_count", 0)
            moderate = agg.get("moderate_count", 0)
            parts.append(f"strong={strong},moderate={moderate}")
        except Exception:
            pass
    else:
        warnings.append("convergence.json not found")

    if os.path.exists(report):
        parts.append(f"report={os.path.getsize(report)}B")
    else:
        warnings.append("convergence-report.md not found")

    if warnings:
        parts.append(f"warnings=[{'; '.join(warnings)}]")

    print(json.dumps({
        "feedback": f"Convergence scanner PASSED: {', '.join(parts)}"
    }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: convergence-scanner gate error: {e}. Allowing through."}))
    sys.exit(0)
