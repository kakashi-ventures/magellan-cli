#!/bin/bash
# Initialize a new MAGELLAN discovery session
# Usage: bash scripts/init-session.sh <MODE> <NEXT_NUM>
# Creates state/session.json and results/{SESSION_ID}/papers/ directory

set -euo pipefail

MODE="${1:?Usage: init-session.sh <MODE> <NEXT_NUM>}"
NEXT_NUM="${2:?Usage: init-session.sh <MODE> <NEXT_NUM>}"

# Read contributor key if connected to MAGELLAN web profile
CONTRIBUTOR_KEY=$(cat .magellan/config.json 2>/dev/null | grep -o '"contributor_key":"[^"]*"' | cut -d'"' -f4)

# Generate session_id, then create directories
SESSION_ID="$(date +%Y-%m-%d)-${MODE}-$(printf '%03d' "$NEXT_NUM")"
mkdir -p "results/${SESSION_ID}/papers" knowledge state

cat > state/session.json << EOF
{
  "session_id": "${SESSION_ID}",
  "mode": "",
  "phase": "init",
  "cycle": 1,
  "status": "running",
  "status_reason": "",
  "results_dir": "results/${SESSION_ID}",
  "selected_target": null,
  "_selected_target_schema": "When populated by Orchestrator: {field_a, field_c, bridge_concepts, strategy, disjointness_status, impact_potential, impact_type}",
  "disjointness_status": null,
  "metadata": {
    "start_time": "",
    "model": "opus-4.6",
    "contributor_key": "${CONTRIBUTOR_KEY:-null}",
    "total_hypotheses_generated": 0,
    "kill_rate": 0,
    "fallback_used": false,
    "literature_unavailable": false,
    "generation_degraded": false,
    "web_search_failures": 0,
    "retries_needed": 0,
    "cycle_decision": null,
    "evolver_skipped": false,
    "literature_reinforcement": false
  },
  "progress": {
    "phases_completed": [],
    "current_phase": null
  },
  "health": {
    "scout_targets_found": 0,
    "hypotheses_generated": 0,
    "survived_critique": 0,
    "passed_quality_gate": 0,
    "fallback_used": false,
    "retries_needed": 0,
    "web_search_failures": 0,
    "impact_potential_score": null
  }
}
EOF

echo "${SESSION_ID}"
