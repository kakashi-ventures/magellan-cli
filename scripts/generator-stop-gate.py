#!/usr/bin/env python3
"""Generator SubagentStop gate. BLOCKS (exit 2) if < 3 hypotheses produced."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        cycle = d.get("cycle", 1)
        raw = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("raw", [])
        count = len(raw) if isinstance(raw, list) else 0

        if count < 3:
            print(json.dumps({
                "decision": "block",
                "reason": f"BLOCKED: Generator produced only {count} hypotheses (minimum 3). Use ALL techniques and produce at least 4."
            }), file=sys.stderr)
            sys.exit(2)
        else:
            print(json.dumps({
                "feedback": f"Generator gate PASSED: {count} hypotheses in cycle {cycle}."
            }))
            sys.exit(0)
    else:
        print(json.dumps({
            "decision": "block",
            "reason": "BLOCKED: state/session.json not found after Generator run."
        }), file=sys.stderr)
        sys.exit(2)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: generator gate error: {e}. Allowing through."}))
    sys.exit(0)
