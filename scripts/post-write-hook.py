#!/usr/bin/env python3
"""PostToolUse hook for the Write tool. Fires on every Write, so it stays silent on
success to avoid per-write noise (state and results are already tracked in
state/session.json and the dispatch log). Errors are surfaced via the canonical
`systemMessage` field; the previous `feedback` field is not recognized by Claude Code
and was silently dropped."""
import sys, json

try:
    json.load(sys.stdin)  # consume the hook stdin payload
    sys.exit(0)           # silent on success
except Exception as e:
    print(json.dumps({"systemMessage": f"post-write hook error: {e}"}))
    sys.exit(0)
