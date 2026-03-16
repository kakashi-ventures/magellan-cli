#!/usr/bin/env python3
"""Stop hook for orchestrator. Blocks premature termination if pipeline is incomplete."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        phase = d.get("phase", None)
        status = d.get("status", None)

        # Allow stop if pipeline completed or explicitly failed
        if phase in ("complete", "failed") or status in ("success", "partial", "degraded", "failed"):
            print(json.dumps({"decision": "allow"}))
            sys.exit(0)

        # Allow stop if no session active (no mode set = not a discovery run)
        if not d.get("mode"):
            print(json.dumps({"decision": "allow"}))
            sys.exit(0)

        # Block: pipeline is mid-run
        progress = d.get("progress", {})
        current = progress.get("current_phase", phase)
        print(json.dumps({
            "decision": "block",
            "reason": f"Pipeline at phase {current}, not complete. Read state/session.json and continue from current phase."
        }))
        sys.exit(0)
    else:
        # No state file = not a discovery session, allow stop
        print(json.dumps({"decision": "allow"}))
        sys.exit(0)

except Exception as e:
    # On error, allow stop to prevent deadlock
    print(json.dumps({"decision": "allow"}))
    sys.exit(0)
