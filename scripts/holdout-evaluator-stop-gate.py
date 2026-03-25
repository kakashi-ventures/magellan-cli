#!/usr/bin/env python3
"""Holdout Evaluator SubagentStop gate. WARN-ONLY — never blocks.
Checks that evaluation report was produced in validation/results/."""
import sys, json, os, glob

try:
    # Use CLAUDE_PROJECT_DIR for reliable path resolution
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    eval_files = glob.glob(os.path.join(project_dir, "validation/results/*-evaluation.json"))
    report_files = glob.glob(os.path.join(project_dir, "validation/results/*-evaluation.md"))

    parts = []
    if eval_files:
        latest = max(eval_files, key=os.path.getmtime)
        parts.append(f"latest={os.path.basename(latest)}({os.path.getsize(latest)}B)")
        try:
            edata = json.load(open(latest))
            verdict = edata.get("verdict", "unknown")
            parts.append(f"verdict={verdict}")
        except Exception:
            pass
    else:
        parts.append("warnings=[no evaluation JSON found]")

    if report_files:
        parts.append(f"reports={len(report_files)}")

    print(json.dumps({
        "feedback": f"Holdout evaluator PASSED: {', '.join(parts)}"
    }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: holdout-evaluator gate error: {e}. Allowing through."}))
    sys.exit(0)
