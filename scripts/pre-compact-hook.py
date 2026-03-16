#!/usr/bin/env python3
"""PreCompact hook. Backs up state/session.json before context compaction."""
import json, os, shutil

try:
    state_path = "state/session.json"
    backup_path = "state/session.json.backup"

    if os.path.exists(state_path):
        shutil.copy2(state_path, backup_path)

        d = json.load(open(state_path))
        phase = d.get("phase", "?")
        progress = d.get("progress", {})
        current = progress.get("current_phase", phase)

        print(json.dumps({
            "feedback": f"State backed up to session.json.backup. Current phase: {current}. Continue pipeline from this phase after compaction."
        }))
    else:
        print(json.dumps({"feedback": "No state/session.json to backup before compaction."}))

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: pre-compact backup error: {e}"}))
