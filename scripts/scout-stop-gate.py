#!/usr/bin/env python3
"""Scout SubagentStop gate. BLOCKS (exit 2) if scout produced 0 targets."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        targets = d.get("scout_targets", [])
        count = len(targets) if isinstance(targets, list) else 0

        if count == 0:
            print(json.dumps({
                "decision": "block",
                "reason": "BLOCKED: Scout produced 0 targets. Re-run with broader search."
            }), file=sys.stderr)
            sys.exit(2)
        else:
            print(json.dumps({
                "feedback": f"Scout gate PASSED: {count} targets found. Continue pipeline."
            }))
            sys.exit(0)
    else:
        print(json.dumps({
            "decision": "block",
            "reason": "BLOCKED: state/session.json not found after Scout run."
        }), file=sys.stderr)
        sys.exit(2)

except Exception as e:
    # On hook error, allow through to avoid deadlock
    print(json.dumps({"feedback": f"WARNING: scout gate error: {e}. Allowing through."}))
    sys.exit(0)
