#!/usr/bin/env python3
"""Critic agent stop hook. Warn-only (critic can legitimately kill all hypotheses)."""
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
            survivors = 0
            killed = 0
            if isinstance(critiqued, list):
                for h in critiqued:
                    if isinstance(h, dict) and h.get("verdict", "").upper() == "KILLED":
                        killed += 1
                    else:
                        survivors += 1
                total = len(critiqued)
            else:
                total = 1
                survivors = 1

            feedback = f"Critic output OK: {total} hypotheses critiqued in cycle {cycle}."
            if survivors == 0:
                feedback += " WARNING: ALL hypotheses killed. Guard logic in orchestrator will handle retry."
            else:
                feedback += f" Survivors: {survivors}, Killed: {killed}."
            print(json.dumps({"feedback": feedback}))
    else:
        print(json.dumps({"feedback": "WARNING: state/session.json not found after Critic run."}))
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: critic stop hook error: {e}"}))
