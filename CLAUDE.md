# MAGELLAN — Multi-Agent Generative Exploration of Latent Links Across kNowledge

Autonomous AI experiment in cross-disciplinary scientific discovery. Tests
whether a multi-agent system with frontier models (March 2026) can find real
connections between existing bodies of knowledge that humans haven't
linked yet — with zero human input on what to explore.

## How to Run

### Primary mode (fully autonomous — this is the point)
```
/discover
```
The Scout autonomously decides WHERE to look. The full pipeline runs.
You come back to find hypothesis cards in `results/{session-id}/`.
**IMPORTANT**: Do NOT run `/discover` in plan mode. The pipeline auto-exits plan mode if active.

### Alternative modes (for testing/debugging)
```
/discover circadian biology × tumor immune evasion
/discover solve: antibiotic resistance
/discover quantum coherence in biology
```

### Launch mode
```
claude --permission-mode auto
```

### Publishing results to the website
After a session completes, publish to the MAGELLAN website (`../magellan-web/`):
```bash
cd ../magellan-web
npm run sync                               # Auto-discovers new sessions, ingests, generates summaries
git add . && git commit && git push        # Auto-deploys to Vercel
```
The sync script reads `results/{session-id}/ingest.json` manifests (written by the orchestrator),
parses markdown, upserts to Postgres, and generates plain-language summaries for new hypotheses.
Flags: `--force` (re-ingest all), `--no-summaries`, `--session <id>`.
Website repo: https://github.com/kakashi-ventures/magellan-web

## Architecture

Fifteen agents. Orchestrator dispatches to all — never executes phases inline.

| Agent | Model | Effort | Role |
|---|---|---|---|
| **Scout** | Opus | max | Finds WHERE to look: 10 strategies (incl. structural isomorphism + serendipity), bridge concepts, strategy diversification, exploration slot, rotating creativity constraint, TARGET QUALITY CHECK reflection |
| **Target Evaluator** | Opus | max | Adversarial challenge of Scout targets on 4 axes (popularity bias, vagueness, structural impossibility, local-optima) |
| **Literature Scout** | Sonnet | high | MCP-first retrieval (Semantic Scholar, PubMed), WebSearch fallback, full-text papers, disjointness verification |
| **Computational Validator** | Sonnet | high | Programmatic bridge verification: KEGG, STRING, PubMed co-occurrence, back-of-envelope physics |
| **Generator** | Opus | max | Hypotheses from parametric knowledge + literature + computational validation. Bisociation + multi-level abstraction. SELF-CRITIQUE with claim-level verification |
| **Critic** | Opus | max | 9 adversarial attack vectors including claim-level fact verification. META-CRITIQUE reflection. Writes critic_questions |
| **Ranker** | Sonnet | high | 6-dimension weighted scoring, per-hypothesis table, diversity check, Elo tournament sanity check, cross-domain creativity bonus (+0.5 for 2+ discipline boundaries) |
| **Evolver** | Sonnet | high | Genetic operations with diversity constraint. EVOLUTION QUALITY CHECK reflection. Conditionally skippable |
| **Quality Gate** | Opus | max | 10-point rubric + web novelty + per-claim grounding verification. META-VALIDATION reflection |
| **Session Analyst** | Sonnet | high | Post-pipeline meta-learning: strategy performance, kill patterns, bridge type analysis, creativity metrics (disciplinary distance, abstraction level, novelty type) → knowledge/meta-insights.md |
| **Cross-Model Validator** | Sonnet | high | Calls GPT-5.4 Pro (web search + code interpreter) + Gemini 3.1 Pro (code execution + Google Search grounding) APIs for independent hypothesis validation. Generates consensus report |
| **Convergence Scanner** | Sonnet | high | Post-QG: searches ClinicalTrials.gov, NIH Reporter, patents for independent convergence signals. Finds partial mechanism confirmations from sources not consulted by pipeline |
| **Dataset Evidence Miner** | Sonnet | high | Post-QG: queries bioinformatics databases (HPA, GWAS Catalog, ChEMBL, UniProt, PDB) to verify specific molecular claims in passing hypotheses |
| **Holdout Evaluator** | Opus | max | Validation framework: compares MAGELLAN output against known post-cutoff discoveries. Contamination check + mechanism similarity scoring |
| **Orchestrator** | Opus | max | Pure dispatcher: guard logic, adaptive cycles, session health, meta-learning metrics, disjointness hard constraint, rotating creativity constraint. No WebSearch/WebFetch |

**Model selection principle**: Opus for deep cross-disciplinary reasoning (Scout, Target Evaluator, Generator, Critic, Quality Gate, Holdout Evaluator). Sonnet for structured, search-intensive tasks (Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator, Convergence Scanner, Dataset Evidence Miner). Effort levels are pinned per agent (Opus: max, Sonnet: high) to guarantee quality regardless of the user's session-level effort setting.

## State Management (v5.7 — Unified Results Directory)

State is split into a **slim coordination index** and **per-session results directories**:
- `state/session.json` — Slim index (~3KB): phase, cycle, status, selected_target,
  health counters, progress. NEVER contains hypothesis content.
- `state/dispatch-log.json` — Tracks every agent dispatch with timestamps.
- `results/{session-id}/` — All session outputs live here: human-readable markdown
  (*.md) and structured phase data (*.json) side by side. Phase JSON files contain
  lightweight metadata (IDs, titles, scores, verdicts). Full hypothesis text lives
  in the markdown files.
- `results/{session-id}/ingest.json` — Self-contained manifest for website ingestion.
  Contains session metadata, pipeline stats, and contributor key. The website seed
  script reads this instead of parsing markdown or session.json.

**Principle**: session.json contains ONLY coordination state. All session data
(both markdown and JSON) lives in `results/{session-id}/`.
Agents receive data via dispatch prompts, never read state files directly.

### Orchestrator Support Files
The orchestrator delegates operational code and reference schemas to external files
(read on-demand to minimize startup context):
- `scripts/init-session.sh` — Session initialization (creates state/session.json + results dir)
- `scripts/upload-session.mjs` — Website upload (reads ingest.json, POSTs to API)
- `prompts/session-summary-format.md` — Session summary formatting per status type
- `prompts/ingest-schema.json` — Schema for the ingest manifest
- `prompts/knowledge-schema.json` — Schema for discovery-log entries

## Commands
- `/discover` — Full autonomous (Scout finds targets)
- `/discover [A] × [C]` — Targeted discovery
- `/discover [topic]` — Open exploration
- `/discover solve: [problem]` — Problem-driven
- `/discover --context "text"` — Provide domain expertise as context for Scout/Generator
- `/discover --papers DOI1,DOI2` — Provide seed papers for Literature Scout
- `/discover --interactive` — Pause after Scout for target approval before proceeding
- `/connect <mgln_key>` — Link this CLI to your MAGELLAN web profile for discovery attribution
- `/validate [hypothesis]` — Deep validation check
- `/evolve` — Another evolutionary cycle
- `/export gpt` — Self-contained prompt for GPT-5.4 validation
- `/export gemini` — Self-contained prompt for Gemini Deep Think
- `/status` — Check pipeline progress
- `/validate-holdout` — Run holdout validation test (rediscovery check against known post-cutoff discoveries)

## Contributor Connection

Link your CLI to your MAGELLAN web profile so discoveries are attributed to you:
1. Create an account at https://magellan-discover.ai/sign-in
2. Go to your profile and generate a contributor key
3. Run `/connect mgln_your_key` in the CLI
4. Key is saved in `.magellan/config.json` (gitignored)
5. All subsequent `/discover` sessions embed the key in results
6. When results are seeded to the website, sessions are auto-attributed to your profile

## Quality Rules
Every hypothesis MUST have: specific mechanism, falsifiable prediction,
literature-verified novelty, counter-evidence, test protocol, calibrated
confidence, groundedness assessment.

## Key Design Principles

### Core paradigm
- **Parametric generation + retrieval validation** — LLM generates cross-domain
  connections from parametric knowledge; external sources validate. Neither
  parametric-only nor retrieval-only.
- **Creativity-first ideation** — The Scout's 10 strategies are elicitation
  mechanisms, not search tools. The most creative connections come from
  parametric reasoning (structural isomorphism, bisociation, serendipity),
  not from WebSearch. WebSearch validates; parametric knowledge creates.
- **Life sciences optimization** — Retrieval tools (PubMed, KEGG, STRING),
  scoring weights (60% on Testability + Groundedness + Mechanistic Specificity),
  and hypothesis format are structurally optimized for life sciences.
  Other domains are supported but scores reflect infrastructure asymmetry.

### Architecture
- **Mandatory agent dispatch** — Orchestrator has no WebSearch/WebFetch,
  maxTurns=200 (circuit breaker only). Sub-agents have no turn limit (stop hooks validate output quality). Cannot execute phases inline. Must dispatch to sub-agents.
- **GOAL/CONSTRAINTS/STRATEGIES prompt structure** — Agent prompts define
  the goal and hard constraints, with strategies as advisory. Better models
  find better reasoning paths; constraints maintain quality floor.
- **Reflection loops** — SELF-CRITIQUE (Generator), META-CRITIQUE (Critic),
  TARGET QUALITY CHECK (Scout), META-VALIDATION (Quality Gate), RETRIEVAL
  QUALITY CHECK (Literature Scout), EVOLUTION QUALITY CHECK (Evolver).
- **Adaptive cycles** — Orchestrator can early-complete (cycle 1 top-3 >= 7.0),
  extend to cycle 3 (survival < 30%), or skip Evolver (cycle 2 top-3 >= 6.5).
- **Bidirectional feedback** — Critic writes critic_questions to state;
  Orchestrator forwards to Generator in cycle 2.

### Quality safeguards
- **Groundedness scoring** (20% weight) — prevents fluent hallucinations
  from scoring high. Always integer 1-10 in JSON.
- **Claim-level fact verification** — Generator SELF-CRITIQUE verifies each
  [GROUNDED] tag. Critic has a dedicated attack vector for per-claim web search.
  Quality Gate verifies every [GROUNDED] claim individually. Citation
  hallucination or fabricated protein property = automatic FAIL.
- **Diversity constraint** — Double-level: Ranker diversity check + Evolver
  diversity constraint. Prevents hypothesis convergence.
- **Elo tournament sanity check** — Ranker runs pairwise comparisons on top-6
  as diagnostic against the linear composite ranking.

### Meta-learning
- **Target evaluation** — Adversarial challenge of Scout targets before pipeline
  investment. Prevents wasted sessions on trendy, vague, or impossible targets.
- **Computational validation** — Programmatic bridge verification (KEGG, STRING,
  PubMed co-occurrence, physics checks) catches quantitatively impossible
  mechanisms before the Critic.
- **Session analysis** — Post-pipeline extraction of strategy performance, kill
  patterns, bridge type survival rates → `knowledge/meta-insights.md`.
  Scout and Generator read this in future sessions.
- **Strategy diversification** — Scout must use at least 2 different strategies
  across 3 targets, with at least 1 not used in the last 2 sessions.
  At least 1 target must use a strategy with < 2 sessions of primary data
  (exploration slot) to prevent convergence on safe-but-boring strategies.
- **Rotating creativity constraint** — Orchestrator assigns a different
  creativity constraint per session (mod 5): cross-discipline bridge,
  mathematical bridge, temporal gap, tool transfer, unsolved problem.
- **Disjointness hard constraint** — If DISJOINT targets with score >= 5
  exist, orchestrator NEVER selects PARTIALLY_EXPLORED. Based on 9 sessions:
  DISJOINT 84% pass+cond rate vs PARTIALLY_EXPLORED 30%.
- **Cross-model validation** (v5.6, tools v5.12) — After Quality Gate, surviving
  hypotheses are automatically sent to GPT-5.4 Pro (empirical validation with
  web search + code interpreter) and Gemini 3.1 Pro (structural analysis with
  code execution + Google Search grounding) via their APIs. GPT verifies novelty
  against current literature and checks arithmetic computationally. Gemini verifies
  formal mappings computationally. Consensus report synthesizes where models
  agree/diverge. Requires `OPENAI_API_KEY` and/or `GEMINI_API_KEY`
  (stored in `.env.local` — agents must source this file before checking);
  falls back to export file generation if keys are absent. Non-blocking.
- **Empirical validation layer** (v5.13) — Two post-QG agents provide evidence
  from sources the pipeline never consults: Convergence Scanner searches
  ClinicalTrials.gov, NIH Reporter, and patents for independent convergence
  signals. Dataset Evidence Miner queries HPA, GWAS Catalog, ChEMBL, UniProt,
  PDB via `scripts/query-biodata.py` to verify specific molecular claims.
  Both are non-blocking. Produces Empirical Evidence Score (EES) alongside
  composite score (not replacing it). Distinction from Computational Validator:
  CV operates on bridge concepts pre-generation; DEM operates on specific
  hypothesis claims post-generation.
- **Holdout validation framework** (v5.13) — Separate from production pipeline.
  Tests MAGELLAN against known post-cutoff discoveries via `/validate-holdout`.
  Pipeline runs normally on `[Field A] × [Field C]`, then Holdout Evaluator
  checks: (1) contamination — did the pipeline find the answer paper?
  (2) mechanism similarity — how close did MAGELLAN get? Verdicts:
  GENUINE_REDISCOVERY, PARTIAL_REDISCOVERY, ADJACENT_DISCOVERY, CONTAMINATED,
  MISSED. Curated holdouts in `validation/holdout-discoveries.json`.

### Operational
- **Session-scoped results** — Each session writes to `results/{session-id}/`.
- **Plan mode auto-exit** — `/discover` automatically exits plan mode.
- **Hook schema** — All hooks use correct Claude Code schema (`"approve"/"block"`,
  stdin for PostToolUse, `"verdict"` field for kill detection).
- **MCP-first retrieval** — Semantic Scholar + PubMed MCP tools mandatory before WebSearch.
- **Unified results directory** (v5.7) — session.json is a ~3KB coordination index.
  Per-phase JSON data and markdown outputs colocate in `results/{session-id}/`.
  Prevents state bloat and reduces context consumption by agents.

## Documentation Rules
When modifying the pipeline (agents, hooks, skills, commands), update:
- `CLAUDE.md` — Architecture table, design principles
- `README.md` — Architecture, phase list, project structure
- `docs/methodology-v5.md` — Full methodology with evidence
- `docs/CHANGELOG.md` — Version history with motivations and evidence
Keep all four aligned. Docs drift = architectural confusion.
