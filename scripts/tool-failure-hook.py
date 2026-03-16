#!/usr/bin/env python3
"""PostToolUseFailure hook. Tracks WebSearch/WebFetch failures in state."""
import sys, json, os

try:
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "unknown")

    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        meta = d.setdefault("metadata", {})
        failures = meta.get("web_search_failures", 0)
        meta["web_search_failures"] = failures + 1

        with open(state_path, "w") as f:
            json.dump(d, f, indent=2)

        feedback = (
            f"{tool_name} failed (total failures: {failures + 1}). "
            f"Try alternative query or different search terms. "
            f"If 3+ failures, consider switching to parametric-only mode."
        )
        print(json.dumps({"feedback": feedback}))
    else:
        print(json.dumps({"feedback": f"{tool_name} failed. No state file to track failure count."}))

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: tool-failure hook error: {e}"}))
