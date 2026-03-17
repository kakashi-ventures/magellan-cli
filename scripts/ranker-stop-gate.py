#!/usr/bin/env python3
"""Ranker SubagentStop gate. BLOCKS if ranked output is too thin (< 3KB)."""
import sys, json, os, glob

try:
    state_path = "state/session.json"
    cycle = 1

    if os.path.exists(state_path):
        d = json.load(open(state_path))
        cycle = d.get("cycle", 1)

    ranked_file = f"results/ranked-cycle{cycle}.md"

    if not os.path.exists(ranked_file):
        print(json.dumps({
            "decision": "block",
            "reason": f"BLOCKED: {ranked_file} does not exist. Ranker must write output."
        }), file=sys.stderr)
        sys.exit(2)

    size = os.path.getsize(ranked_file)
    if size < 3072:  # 3KB minimum
        print(json.dumps({
            "decision": "block",
            "reason": f"BLOCKED: {ranked_file} is only {size} bytes (minimum 3KB). Use MANDATORY per-hypothesis scoring table format with 2+ sentence justifications per dimension."
        }), file=sys.stderr)
        sys.exit(2)

    print(json.dumps({
        "feedback": f"Ranker gate PASSED: {ranked_file} is {size} bytes."
    }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: ranker gate error: {e}. Allowing through."}))
    sys.exit(0)
