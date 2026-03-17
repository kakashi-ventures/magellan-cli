#!/usr/bin/env python3
"""PostToolUse hook for Agent tool. Logs which agents were dispatched to state/dispatch-log.json."""
import sys, json, os
from datetime import datetime, timezone

try:
    # Read hook input from environment
    tool_input = os.environ.get("CLAUDE_TOOL_INPUT", "{}")
    tool_params = json.loads(tool_input) if tool_input else {}

    # Extract agent type from the tool input
    agent_type = tool_params.get("subagent_type", tool_params.get("name", "unknown"))

    # Also try to extract from the prompt (agent names are often in the dispatch)
    prompt = tool_params.get("prompt", "")

    dispatch_log_path = "state/dispatch-log.json"

    # Read existing log or create new
    if os.path.exists(dispatch_log_path):
        log = json.load(open(dispatch_log_path))
    else:
        os.makedirs("state", exist_ok=True)
        log = {"dispatches": []}

    # Append this dispatch
    log["dispatches"].append({
        "agent": agent_type,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "prompt_preview": prompt[:100] if prompt else ""
    })

    # Write back
    with open(dispatch_log_path, "w") as f:
        json.dump(log, f, indent=2)

    # Always allow — this is a logging hook, not a gate
    sys.exit(0)

except Exception as e:
    # On error, allow through silently
    sys.exit(0)
