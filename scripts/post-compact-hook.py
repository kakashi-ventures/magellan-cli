#!/usr/bin/env python3
"""PostCompact hook. Re-injects critical state from session.json after context compaction.
If session.json is missing or corrupted, restores from backup."""
import json, os, shutil

try:
    state_path = "state/session.json"
    backup_path = "state/session.json.backup"

    # Check if state file exists and is valid
    state_ok = False
    if os.path.exists(state_path):
        try:
            d = json.load(open(state_path))
            # Basic integrity check: must have session_id or mode
            if d.get("session_id") or d.get("mode"):
                state_ok = True
        except (json.JSONDecodeError, ValueError):
            state_ok = False

    # Restore from backup if state is missing or corrupted
    if not state_ok and os.path.exists(backup_path):
        shutil.copy2(backup_path, state_path)
        feedback_prefix = "STATE RESTORED from backup after compaction. "
    elif not state_ok:
        print(json.dumps({"feedback": "No state/session.json found and no backup available. If running discovery pipeline, initialize state first."}))
        raise SystemExit(0)
    else:
        feedback_prefix = "CONTEXT RESTORED after compaction. "

    d = json.load(open(state_path))
    mode = d.get("mode", "unknown")
    phase = d.get("phase", "?")
    cycle = d.get("cycle", "?")
    hyps = d.get("metadata", {}).get("total_hypotheses_generated", 0)
    status = d.get("status", "running")

    target = d.get("selected_target", None)
    target_summary = ""
    if target:
        if isinstance(target, dict):
            target_summary = target.get("title", str(target))[:120]
        else:
            target_summary = str(target)[:120]

    progress = d.get("progress", {})
    phases_done = progress.get("phases_completed", [])
    current_phase = progress.get("current_phase", phase)

    feedback = (
        f"{feedback_prefix}"
        f"Mode: {mode}, Phase: {current_phase}, Cycle: {cycle}, "
        f"Status: {status}, Hypotheses generated: {hyps}"
    )
    if phases_done:
        phase_names = [p.get("phase", "?") if isinstance(p, dict) else str(p) for p in phases_done]
        feedback += f", Completed phases: {', '.join(phase_names)}"
    if target_summary:
        feedback += f", Target: {target_summary}"
    feedback += ". Read state/session.json for full state. Continue pipeline from current phase."

    print(json.dumps({"feedback": feedback}))

except SystemExit:
    pass
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: post-compact hook error: {e}"}))
