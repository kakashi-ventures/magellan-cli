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
npm run db:seed                            # Parse results, upsert to Postgres
npx tsx scripts/generate-summaries.ts      # Generate plain-language summaries via Claude API
git add . && git commit && git push        # Auto-deploys to Vercel
```
The seed script reads `results/{session-id}/` markdown files. New sessions must be added to the `SESSIONS` array in `scripts/seed.ts`.
Website repo: https://github.com/kakashi-ventures/magellan-web

## Architecture

Twelve agents. Orchestrator dispatches to all — never executes phases inline.

| Agent | Model | Role |
|---|---|---|
| **Scout** | Opus | Finds WHERE to look: 8 strategies, bridge concepts, strategy diversification, TARGET QUALITY CHECK reflection |
| **Target Evaluator** | Opus | Adversarial challenge of Scout targets on 4 axes (popularity bias, vagueness, structural impossibility, local-optima) |
| **Literature Scout** | Sonnet | MCP-first retrieval (Semantic Scholar, PubMed), WebSearch fallback, full-text papers, disjointness verification |
| **Computational Validator** | Sonnet | Programmatic bridge verification: KEGG, STRING, PubMed co-occurrence, back-of-envelope physics |
| **Generator** | Opus | Hypotheses from parametric knowledge + literature + computational validation. SELF-CRITIQUE with claim-level verification |
| **Critic** | Opus | 9 adversarial attack vectors including claim-level fact verification. META-CRITIQUE reflection. Writes critic_questions |
| **Ranker** | Sonnet | 6-dimension weighted scoring, per-hypothesis table, diversity check, Elo tournament sanity check |
| **Evolver** | Sonnet | Genetic operations with diversity constraint. EVOLUTION QUALITY CHECK reflection. Conditionally skippable |
| **Quality Gate** | Opus | 10-point rubric + web novelty + per-claim grounding verification. META-VALIDATION reflection |
| **Session Analyst** | Sonnet | Post-pipeline meta-learning: strategy performance, kill patterns, bridge type analysis → knowledge/meta-insights.md |
| **Cross-Model Validator** | Sonnet | Calls GPT-5.4 Pro + Gemini 3.1 Pro APIs for independent hypothesis validation. Generates consensus report |
| **Orchestrator** | Opus | Pure dispatcher: guard logic, adaptive cycles, session health, meta-learning metrics. No WebSearch/WebFetch |

**Model selection principle**: Opus for deep cross-disciplinary reasoning (Scout, Target Evaluator, Generator, Critic, Quality Gate). Sonnet for structured, search-intensive tasks (Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator).

## State Management (v5.6 — Slim Index + Phase Files)

State is split into a **slim coordination index** and **per-phase data files**:
- `state/session.json` — Slim index (~3KB): phase, cycle, status, selected_target,
  health counters, progress. NEVER contains hypothesis content.
- `state/phases/{session-id}/*.json` — Per-phase structured data, scoped by session:
  scout targets, hypotheses (IDs, titles, scores, verdicts), quality gate results,
  cross-model consensus.
- `results/{session-id}/*.md` — Human-readable outputs with full hypothesis text.
- `state/dispatch-log.json` — Tracks every agent dispatch with timestamps.

**Principle**: Full hypothesis text lives ONLY in `results/`. Phase files contain
lightweight metadata. session.json contains ONLY coordination state.
Agents receive data via dispatch prompts, never read state files directly.

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
- **Life sciences optimization** — Retrieval tools (PubMed, KEGG, STRING),
  scoring weights (60% on Testability + Groundedness + Mechanistic Specificity),
  and hypothesis format are structurally optimized for life sciences.
  Other domains are supported but scores reflect infrastructure asymmetry.

### Architecture
- **Mandatory agent dispatch** — Orchestrator has no WebSearch/WebFetch,
  maxTurns=80. Cannot execute phases inline. Must dispatch to sub-agents.
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
- **Cross-model validation** (v5.6) — After Quality Gate, surviving hypotheses
  are automatically sent to GPT-5.4 Pro (empirical validation) and Gemini 3.1
  Pro (structural analysis) via their APIs. Consensus report synthesizes where
  models agree/diverge. Requires `OPENAI_API_KEY` and/or `GEMINI_API_KEY`
  (stored in `.env.local` — agents must source this file before checking);
  falls back to export file generation if keys are absent. Non-blocking.

### Operational
- **Session-scoped results** — Each session writes to `results/{session-id}/`.
- **Plan mode auto-exit** — `/discover` automatically exits plan mode.
- **Hook schema** — All hooks use correct Claude Code schema (`"approve"/"block"`,
  stdin for PostToolUse, `"verdict"` field for kill detection).
- **MCP-first retrieval** — Semantic Scholar + PubMed MCP tools mandatory before WebSearch.
- **Slim state + phase files** (v5.6) — session.json is a ~3KB coordination index.
  Per-phase data in `state/phases/{session-id}/*.json`. Full text only in `results/*.md`.
  Prevents state bloat and reduces context consumption by agents.

## Documentation Rules
When modifying the pipeline (agents, hooks, skills, commands), update:
- `CLAUDE.md` — Architecture table, design principles
- `README.md` — Architecture, phase list, project structure
- `docs/methodology-v5.md` — Full methodology with evidence
- `docs/CHANGELOG.md` — Version history with motivations and evidence
Keep all four aligned. Docs drift = architectural confusion.
