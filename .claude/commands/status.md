---
description: "Check current pipeline progress. Shows phase, cycle, hypothesis count, health status, and progress timeline."
allowed-tools: Read, Bash
---

# Pipeline Status

Read state/session.json and display:

```bash
if [ -f state/session.json ]; then
  python3 -c "
import json
d = json.load(open('state/session.json'))
phase = d.get('phase', 'unknown')
cycle = d.get('cycle', 0)
mode = d.get('mode', 'unknown')
status = d.get('status', 'running')
reason = d.get('status_reason', '')
total = d.get('metadata', {}).get('total_hypotheses_generated', 0)
kill = d.get('metadata', {}).get('kill_rate', 0)
nfinal = len(d.get('final', []))
targets = len(d.get('scout_targets', []))

# Health counters
health = d.get('health', {})
h_targets = health.get('scout_targets_found', targets)
h_generated = health.get('hypotheses_generated', total)
h_survived = health.get('survived_critique', '?')
h_passed = health.get('passed_quality_gate', nfinal)
fallback = health.get('fallback_used', False)
retries = health.get('retries_needed', 0)
web_fails = health.get('web_search_failures', 0)

# Progress timeline
progress = d.get('progress', {})
phases_done = progress.get('phases_completed', [])
current = progress.get('current_phase', phase)

print(f'Mode: {mode}')
print(f'Status: {status}' + (f' ({reason})' if reason else ''))
print(f'Current phase: {current} | Cycle: {cycle}')
print()
print('--- Pipeline Progress ---')
for p in phases_done:
    if isinstance(p, dict):
        print(f'  [{p.get(\"phase\", \"?\")}] {p.get(\"outcome\", \"\")}  ({p.get(\"timestamp\", \"\")})')
    else:
        print(f'  [{p}]')
if not phases_done:
    print('  (no phases completed yet)')
print()
print('--- Health Counters ---')
print(f'  Scout targets found: {h_targets}')
print(f'  Hypotheses generated: {h_generated}')
print(f'  Survived critique: {h_survived}')
print(f'  Passed quality gate: {h_passed}')
print(f'  Fallback used: {fallback}')
print(f'  Retries needed: {retries}')
print(f'  Web search failures: {web_fails}')
print()
print(f'Kill rate: {kill}%')
print(f'Final approved: {nfinal}')
"
else
  echo "No active session. Run /discover to start."
fi
```

Display the output to the user. If phase is "complete", also mention
that `/export gpt` or `/export gemini` is the recommended next step.
If status is "failed" or "degraded", explain what happened and suggest
running `/discover` again.

Also scan for interrupted sessions that can be resumed:
```bash
for f in results/*/session-state.json; do
  [ -f "$f" ] || continue
  python3 -c "
import json, sys
d = json.load(open('$f'))
phase = d.get('phase', '')
status = d.get('status', '')
if phase not in ('complete', 'failed') and status == 'running':
    sid = d.get('session_id', '?')
    cp = d.get('progress', {}).get('current_phase', phase)
    lu = d.get('metadata', {}).get('last_updated', '?')
    print(f'  {sid}: interrupted at {cp} (last update: {lu})')
" 2>/dev/null
done
```
If any interrupted sessions are found, show them under "--- Interrupted Sessions ---"
and tell the user they can resume with: "Ask Claude to resume session {session-id}".
