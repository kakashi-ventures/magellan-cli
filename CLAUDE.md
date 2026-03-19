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

## Architecture

Eleven agents. Orchestrator dispatches to all — never executes phases inline.

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
| **Orchestrator** | Opus | Pure dispatcher: guard logic, adaptive cycles, session health, meta-learning metrics. No WebSearch/WebFetch |

**Model selection principle**: Opus for deep cross-disciplinary reasoning (Scout, Target Evaluator, Generator, Critic, Quality Gate). Sonnet for structured, search-intensive tasks (Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst).

## State Management

All structured state lives in `state/session.json`.
Human-readable outputs in `results/{session-id}/*.md` (session-scoped directories).
Every agent reads/writes `state/session.json` as source of truth.
Dispatch log in `state/dispatch-log.json` tracks every agent dispatch with timestamps.

## Commands
- `/discover` — Full autonomous (Scout finds targets)
- `/discover [A] × [C]` — Targeted discovery
- `/discover [topic]` — Open exploration
- `/discover solve: [problem]` — Problem-driven
- `/validate [hypothesis]` — Deep validation check
- `/evolve` — Another evolutionary cycle
- `/export gpt` — Self-contained prompt for GPT-5.4 validation
- `/export gemini` — Self-contained prompt for Gemini Deep Think
- `/status` — Check pipeline progress

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

### Operational
- **Session-scoped results** — Each session writes to `results/{session-id}/`.
- **Plan mode auto-exit** — `/discover` automatically exits plan mode.
- **Hook schema** — All hooks use correct Claude Code schema (`"approve"/"block"`,
  stdin for PostToolUse, `"verdict"` field for kill detection).
- **MCP-first retrieval** — Semantic Scholar + PubMed MCP tools mandatory before WebSearch.
- **Structured state** — JSON state file survives context compaction.

## Documentation Rules
When modifying the pipeline (agents, hooks, skills, commands), update:
- `CLAUDE.md` — Architecture table, design principles
- `README.md` — Architecture, phase list, project structure
- `docs/methodology-v5.md` — Full methodology with evidence
- `docs/CHANGELOG.md` — Version history with motivations and evidence
Keep all four aligned. Docs drift = architectural confusion.
