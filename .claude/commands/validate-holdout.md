---
description: "Run a holdout validation test — execute MAGELLAN on a known post-cutoff discovery and evaluate if it rediscovers the connection. Usage: /validate-holdout [holdout-id], /validate-holdout --curate, /validate-holdout --report"
allowed-tools: Read, Write, Agent, Bash, Glob, Grep
user-invocable: true
---

# Holdout Validation Test

Tests whether MAGELLAN can independently rediscover a known scientific
connection. The pipeline runs blind (only seeing the two fields, never
the known mechanism), then the holdout-evaluator agent compares results
against the answer.

## User Input
$ARGUMENTS

## Step 1: Parse Arguments

Parse `$ARGUMENTS` to determine mode:

- **Empty or holdout ID** (e.g., `holdout-001`) → **VALIDATION RUN**
- **`--curate`** → **CURATE MODE** (discover and add new holdout entries)
- **`--report`** → **REPORT MODE** (aggregate metrics from completed evaluations)

## Step 2A: Validation Run (default)

### 2A.1: Load Holdout Discovery

Read `validation/holdout-discoveries.json`. This file contains an array of
known post-cutoff discoveries, each with:
```json
{
  "id": "holdout-001",
  "field_a": "...",
  "field_c": "...",
  "known_mechanism": "...",
  "key_paper": {
    "doi": "...",
    "pmid": "...",
    "title": "...",
    "first_author": "...",
    "year": 2025
  },
  "difficulty": "easy|medium|hard",
  "status": "pending|completed|contaminated"
}
```

**If a holdout ID is specified**: Select that entry by ID. If not found,
list available IDs and ask the user to pick one.

**If no ID specified**: Select a random entry with `status: "pending"`.
If no pending entries remain, inform the user and suggest `--curate`.

### 2A.2: Present to User (Blind)

Show the user what MAGELLAN will explore, WITHOUT revealing the answer:

> **Holdout Validation Test: {holdout_id}**
> - Difficulty: {difficulty}
> - Field A: {field_a}
> - Field C: {field_c}
> - MAGELLAN will attempt to find connections between these fields.
> - The known mechanism is hidden until evaluation.

Do NOT show `known_mechanism` or `key_paper` at this point.

### 2A.3: Run Discovery Pipeline in BLIND MODE

**DO NOT use `/discover`.** Dispatch the `discovery-orchestrator` agent
directly with BLIND MODE instructions. This prevents the pipeline from
finding the holdout paper via web search — the key requirement for a
valid holdout test.

Initialize session state first:
```bash
mkdir -p state
cat > state/session.json << 'EOF'
{"phase":"init","cycle":0,"scout_targets":[],"hypotheses":{},"final":[],"metadata":{"total_hypotheses_generated":0}}
EOF
```

Then dispatch the orchestrator with this prompt:

> Run a full TARGETED discovery session in **BLIND MODE** (holdout validation).
> Field A: {field_a}
> Field C: {field_c}
> Skip Scout. Launch Literature Scout, then run 2 complete generation cycles.
> Do not stop for user input.
>
> **BLIND MODE RESTRICTIONS** (pass these to EVERY sub-agent dispatch):
>
> **Literature Scout**: Do NOT use WebSearch or WebFetch. Use ONLY PubMed
> MCP and Semantic Scholar MCP tools. RESTRICT all searches to papers
> published BEFORE June 2025 (use year filters: `year: "2020-2025"` for
> Semantic Scholar, date range `"2020":"2025/05"` for PubMed). This provides
> background context about each field without revealing post-cutoff discoveries.
>
> **Critic**: Do NOT use WebSearch or WebFetch. Perform ALL critique
> (novelty, counter-evidence, claim verification) using ONLY parametric
> knowledge. Skip web-based novelty search and counter-evidence search.
>
> **Quality Gate**: Do NOT use WebSearch or WebFetch. Validate claims
> using ONLY parametric knowledge. Skip web-based novelty verification
> and per-claim web grounding. Apply the 10-point rubric using only what
> the model already knows.
>
> **Generator**: Normal operation (WebSearch already forbidden).
> **Ranker**: Normal operation (no WebSearch needed).
> **Evolver**: Normal operation (no WebSearch needed).
> **Computational Validator**: Normal operation (uses APIs, not web search
> for the specific paper — KEGG, STRING, PubMed co-occurrence are fine).
>
> **SKIP these post-QG agents entirely**:
> - Cross-Model Validator (GPT/Gemini have current web search)
> - Convergence Scanner (uses WebSearch)
>
> **DO run**: Dataset Evidence Miner (uses bioinformatics APIs, not web search)
>
> This is a holdout validation test. The integrity of the test depends on
> the pipeline NOT finding the answer via web search.

Wait for the pipeline to complete. Read `state/session.json` to get the
`results_dir` and confirm the session finished.

### 2A.4: Dispatch Holdout Evaluator

After the pipeline completes, dispatch the `holdout-evaluator` agent with
all information needed for evaluation:

> Evaluate this MAGELLAN session against a known holdout discovery.
>
> **Holdout Discovery:**
> - holdout_id: {id}
> - field_a: {field_a}
> - field_c: {field_c}
> - known_mechanism: {known_mechanism}
> - key_paper DOI: {doi}
> - key_paper PMID: {pmid}
> - key_paper title: {title}
> - key_paper first_author: {first_author}
>
> **Session Results:**
> - results_dir: {results_dir}
> - session_id: {session_id}
>
> Perform contamination check, mechanism comparison, and write evaluation
> to validation/results/{holdout_id}-evaluation.json and .md.

### 2A.5: Update Holdout Status

After evaluation completes, read `validation/results/{holdout_id}-evaluation.json`
for the verdict. Update `validation/holdout-discoveries.json`:
- Set `status` to `"completed"` (or `"contaminated"` if verdict is CONTAMINATED)
- Add `last_session_id` and `last_verdict` fields

### 2A.6: Present Results

Read and display `validation/results/{holdout_id}-evaluation.md` to the user.
Highlight the verdict and key findings.

---

## Step 2B: Curate Mode (`--curate`)

Help the user find and add new holdout discoveries to the test bank.

### 2B.1: Search for Candidates

Use WebSearch to find recent cross-disciplinary scientific discoveries
published after May 2025. Good candidates:
- Connect two fields that seem unrelated
- Have a clear, specific mechanism (not just a correlation)
- Are published in peer-reviewed journals with a citable DOI
- Are surprising enough that parametric knowledge alone might miss them

Search queries to try:
- "unexpected connection between [field] and [field] 2025 2026"
- "surprising discovery links [domain] [domain] mechanism"
- "cross-disciplinary breakthrough biology 2025 2026"

### 2B.2: Present Candidates

For each candidate, present:
- Title and citation
- Field A and Field C
- The core mechanism (A -> B -> C)
- Why it is a good holdout (specific, surprising, verifiable)
- Estimated difficulty: easy (obvious bridge), medium, hard (obscure bridge)

### 2B.3: User Selection

Ask the user which candidates to add. For each selected candidate, create
a new entry in `validation/holdout-discoveries.json` with:
- Auto-generated ID (`holdout-NNN`, incrementing from highest existing)
- All required fields populated
- `status: "pending"`

---

## Step 2C: Report Mode (`--report`)

Generate aggregate metrics from all completed holdout evaluations.

### 2C.1: Collect Results

Read all `validation/results/*-evaluation.json` files. If none exist,
inform the user that no evaluations have been completed yet.

### 2C.2: Calculate Metrics

Compute:
- **Total evaluations**: count of completed holdout tests
- **Verdicts breakdown**: count per verdict type
- **Rediscovery rate**: (GENUINE + PARTIAL) / (total - CONTAMINATED)
- **Contamination rate**: CONTAMINATED / total
- **Average best similarity score** (excluding contaminated)
- **By difficulty**: rediscovery rate per difficulty level
- **Confidence distribution**: HIGH / MEDIUM / LOW counts

### 2C.3: Write Report

Write `validation/results/aggregate-report.md`:

```markdown
# MAGELLAN Holdout Validation — Aggregate Report

Generated: {date}

## Summary
- **Total evaluations**: N
- **Rediscovery rate**: X% (N genuine + N partial out of N non-contaminated)
- **Contamination rate**: Y% (N out of N total)

## Verdict Breakdown
| Verdict | Count | % |
|---------|-------|---|
| GENUINE_REDISCOVERY | N | X% |
| PARTIAL_REDISCOVERY | N | X% |
| ADJACENT_DISCOVERY | N | X% |
| MISSED | N | X% |
| CONTAMINATED | N | X% |

## By Difficulty
| Difficulty | Tests | Rediscovery Rate | Avg Similarity |
|------------|-------|------------------|----------------|
| Easy | N | X% | Y.Z |
| Medium | N | X% | Y.Z |
| Hard | N | X% | Y.Z |

## Individual Results
| Holdout | Fields | Verdict | Similarity | Confidence |
|---------|--------|---------|------------|------------|
| holdout-001 | A x C | GENUINE_REDISCOVERY | 8 | HIGH |
| ... | ... | ... | ... | ... |

## Analysis
{Narrative analysis of patterns, strengths, weaknesses}
```

Present the report summary to the user.

## CRITICAL RULES
- NEVER reveal the known mechanism to MAGELLAN during the discovery run
- The pipeline MUST run in BLIND MODE — no WebSearch for Literature Scout,
  Critic, or Quality Gate. This is the only way to ensure a valid test.
  If any agent uses WebSearch, the test is contaminated.
- Contamination honesty is paramount — do not downplay contamination
- If the pipeline fails or produces no surviving hypotheses, still run
  the evaluator (it will record MISSED with appropriate context)
- Skip Cross-Model Validator and Convergence Scanner (both use web search)
