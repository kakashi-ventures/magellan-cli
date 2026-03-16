#!/usr/bin/env python3
"""Critic agent stop hook. Verifies critiqued output exists in state."""
import json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        cycle = d.get("cycle", 1)
        critiqued = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("critiqued", None)

        if not critiqued:
            print(json.dumps({"feedback": f"WARNING: Critic finished but no critiqued data found for cycle {cycle} in state. Verify critic wrote results."}))
        else:
            count = len(critiqued) if isinstance(critiqued, list) else 1
            print(json.dumps({"feedback": f"Critic output OK: {count} hypotheses critiqued in cycle {cycle}."}))
    else:
        print(json.dumps({"feedback": "WARNING: state/session.json not found after Critic run."}))
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: critic stop hook error: {e}"}))
