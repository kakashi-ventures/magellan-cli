#!/usr/bin/env python3
"""PostCompact hook. Re-injects critical state from session.json after context compaction."""
import json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        mode = d.get("mode", "unknown")
        phase = d.get("phase", "?")
        cycle = d.get("cycle", "?")
        target = d.get("selected_target", None)
        hyps = d.get("metadata", {}).get("total_hypotheses_generated", 0)

        target_summary = ""
        if target:
            if isinstance(target, dict):
                target_summary = target.get("title", str(target))[:120]
            else:
                target_summary = str(target)[:120]

        feedback = (
            f"CONTEXT RESTORED after compaction. "
            f"Mode: {mode}, Phase: {phase}, Cycle: {cycle}, "
            f"Hypotheses generated: {hyps}"
        )
        if target_summary:
            feedback += f", Target: {target_summary}"
        feedback += ". Read state/session.json for full state. Continue pipeline from current phase."

        print(json.dumps({"feedback": feedback}))
    else:
        print(json.dumps({"feedback": "No state/session.json found. If running discovery pipeline, initialize state first."}))
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: post-compact hook error: {e}"}))
