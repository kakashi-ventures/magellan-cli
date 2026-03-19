#!/usr/bin/env python3
"""Session Analyst SubagentStop gate. WARN-ONLY — never blocks.
Checks that meta-insights file was produced."""
import sys, json, os

try:
    state_path = "state/session.json"
    results_dir = "results"

    if os.path.exists(state_path):
        d = json.load(open(state_path))
        results_dir = d.get("results_dir", "results")

    analysis_file = os.path.join(results_dir, "session-analysis.md")
    meta_file = "knowledge/meta-insights.md"

    warnings = []
    if not os.path.exists(analysis_file):
        warnings.append(f"session-analysis.md not found in {results_dir}")
    if not os.path.exists(meta_file):
        warnings.append("knowledge/meta-insights.md not created/updated")

    if warnings:
        print(json.dumps({
            "feedback": f"Session analyst PASSED with warnings: {'; '.join(warnings)}"
        }))
    else:
        analysis_size = os.path.getsize(analysis_file)
        meta_size = os.path.getsize(meta_file)
        print(json.dumps({
            "feedback": f"Session analyst PASSED: session-analysis.md ({analysis_size}B), meta-insights.md ({meta_size}B)"
        }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: session-analyst gate error: {e}. Allowing through."}))
    sys.exit(0)
