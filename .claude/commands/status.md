---
description: "Check current pipeline progress. Shows phase, cycle, hypothesis count, and estimated remaining work."
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
total = d.get('metadata', {}).get('total_hypotheses_generated', 0)
kill = d.get('metadata', {}).get('kill_rate', 0)
nfinal = len(d.get('final', []))
targets = len(d.get('scout_targets', []))
print(f'Mode: {mode}')
print(f'Phase: {phase} | Cycle: {cycle}')
print(f'Scout targets found: {targets}')
print(f'Hypotheses generated: {total}')
print(f'Kill rate: {kill}%')
print(f'Final approved: {nfinal}')
"
else
  echo "No active session. Run /discover to start."
fi
```

Display the output to the user. If phase is "complete", also mention
that `/export gpt` or `/export gemini` is the recommended next step.
