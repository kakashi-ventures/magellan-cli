---
description: "Run an autonomous scientific discovery session. Primary mode: /discover (no arguments) — Scout autonomously finds where undiscovered connections are hiding. Alternative modes: /discover [A] × [C], /discover [topic], /discover solve: [problem]."
allowed-tools: Agent, Read, Write, Bash, Glob, Grep, ExitPlanMode
---

# Autonomous Scientific Discovery Session v5

This system tests whether AI can autonomously discover real scientific
connections. The user is NOT expected to have domain expertise.

## User Input
$ARGUMENTS

## Step 0: Exit Plan Mode (if active)

The discovery pipeline is fully autonomous and CANNOT run in plan mode.
If plan mode is active, call ExitPlanMode IMMEDIATELY before proceeding.
Do not write a plan file. Do not ask for confirmation.

## Step 1: Parse Flags and Determine Mode

Parse `$ARGUMENTS` for optional flags before determining mode:
- `--context "..."` → Extract quoted text as contributor domain context
- `--papers DOI1,DOI2,...` → Extract comma-separated DOIs/identifiers as seed papers
- `--interactive` → Enable interactive target review (pause after Scout for user approval)

Remove parsed flags from $ARGUMENTS, then determine mode from remaining text:
- **Empty or generic** → **SCOUT MODE** (fully autonomous)
- Contains "×" or " x " or " and " between two fields → **TARGETED MODE**
- Starts with "solve" or "problem" → **PROBLEM MODE**
- Single specific topic → **OPEN MODE**

## Step 2: Initialize

Read contributor config if available, then create session state:
```bash
CONTRIBUTOR_KEY=$(cat .magellan/config.json 2>/dev/null | grep -o '"contributor_key":"[^"]*"' | cut -d'"' -f4)
mkdir -p state
cat > state/session.json << EOF
{"phase":"init","cycle":0,"scout_targets":[],"hypotheses":{},"final":[],"metadata":{"total_hypotheses_generated":0,"contributor_key":"${CONTRIBUTOR_KEY:-null}"}}
EOF
```

## Step 3: Launch Orchestrator

Launch `discovery-orchestrator` agent via Agent IMMEDIATELY.
Do NOT ask for confirmation. Do NOT present a plan first.

Include these in the orchestrator dispatch if present:
- If `--context` was provided: "Contributor domain context: [text]"
- If `--papers` was provided: "Seed papers (contributor-provided): [DOIs]"
- If `--interactive` was set: "INTERACTIVE MODE: Pause after Scout target selection for user approval before proceeding."

**SCOUT MODE:**
> Run a full SCOUT MODE discovery session.
> Phase 0: Launch scout and literature-scout in parallel.
> Scout identifies 3 promising targets; Literature Scout provides
> landscape context. Select best target and run 2 complete cycles.
> Do not stop for user input (unless --interactive). Write all results to results/{session-id}/.
> Manage state in state/session.json.

**TARGETED MODE:**
> Run a full TARGETED discovery session.
> Field A: [extracted field 1]
> Field C: [extracted field 2]
> Skip Scout. Launch Literature Scout for these specific fields.
> Then run 2 complete generation cycles.
> Do not stop for user input.

**OPEN MODE:**
> Run a full OPEN discovery session.
> Starting domain: [topic]
> Launch Literature Scout to identify 3 fields that [topic] might
> connect to unexpectedly. Pick the best and run targeted discovery.

**PROBLEM MODE:**
> Run a full PROBLEM-DRIVEN discovery session.
> Unsolved problem: [problem]
> Launch Literature Scout to identify 3 unrelated fields whose insights
> might help solve this. Pick best and run targeted discovery.

## CRITICAL RULES
- If $ARGUMENTS is empty → SCOUT MODE
- Do NOT ask "which fields are you interested in?"
- Do NOT ask "shall I proceed?"
- Just launch the orchestrator and let it run
