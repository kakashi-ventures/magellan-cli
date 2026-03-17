#!/usr/bin/env python3
"""PostToolUse hook for Agent tool. Logs which agents were dispatched to state/dispatch-log.json.
Reads tool input from stdin (PostToolUse hook protocol)."""
import sys, json, os
from datetime import datetime, timezone

try:
    # PostToolUse hooks receive data via stdin
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input", {})

    # Extract agent type from the tool input
    agent_type = tool_input.get("subagent_type", tool_input.get("name", "unknown"))
    prompt = tool_input.get("prompt", "")
    description = tool_input.get("description", "")

    # Extract result info if available
    tool_result = data.get("tool_result", "")
    result_preview = str(tool_result)[:200] if tool_result else ""

    dispatch_log_path = "state/dispatch-log.json"

    # Read existing log or create new
    if os.path.exists(dispatch_log_path):
        log = json.load(open(dispatch_log_path))
    else:
        os.makedirs("state", exist_ok=True)
        log = {"dispatches": []}

    # Ensure dispatches is a list (handle corrupted state)
    if not isinstance(log.get("dispatches"), list):
        log["dispatches"] = []

    # Append this dispatch
    log["dispatches"].append({
        "agent": agent_type,
        "description": description,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "prompt_preview": prompt[:150] if prompt else "",
        "result_preview": result_preview
    })

    # Update stage marker
    log["stage"] = "running"

    # Write back
    with open(dispatch_log_path, "w") as f:
        json.dump(log, f, indent=2)

    # Always allow — this is a logging hook, not a gate
    sys.exit(0)

except Exception as e:
    # On error, allow through silently
    sys.exit(0)
