#!/usr/bin/env python3
"""PostToolUse hook for Write tool. Inspects file path and provides context-aware feedback."""
import sys, json, os

try:
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")

    if path.endswith("state/session.json"):
        d = json.load(open("state/session.json"))
        phase = d.get("phase", "?")
        cycle = d.get("cycle", "?")
        hyps = d.get("metadata", {}).get("total_hypotheses_generated", 0)
        print(json.dumps({"feedback": f"State OK \u2014 phase={phase}, cycle={cycle}, hypotheses={hyps}"}))
    elif "/results/" in path and path.endswith(".md"):
        print(json.dumps({"feedback": f"Result file saved: {os.path.basename(path)}"}))
    # Other files: exit silently
except Exception as e:
    print(json.dumps({"feedback": f"WARNING: post-write hook error: {e}"}))
