#!/usr/bin/env python3
"""Generator agent stop hook. Verifies at least 4 hypotheses were written to state."""
import json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        cycle = d.get("cycle", 1)
        raw = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("raw", [])
        count = len(raw) if isinstance(raw, list) else 0

        if count < 4:
            print(json.dumps({"feedback": f"WARNING: Generator produced only {count} hypotheses (minimum 4 expected). Consider re-running or supplementing."}))
        else:
            print(json.dumps({"feedback": f"Generator output OK: {count} hypotheses in cycle {cycle}."}))
    else:
        print(json.dumps({"feedback": "WARNING: state/session.json not found after Generator run."}))
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: generator stop hook error: {e}"}))
