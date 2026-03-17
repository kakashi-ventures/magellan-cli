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
You come back to find hypothesis cards in `results/`.

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

Eight agents. Orchestrator dispatches to all — never executes phases inline:

| Agent | Role |
|---|---|
| **Scout** | Finds WHERE to look (8 strategies, parametric + web) |
| **Literature Scout** | MCP mandatory first, then WebSearch fallback |
| **Orchestrator** | Dispatches to agents, guard logic, session health |
| **Generator** | Creates hypotheses (parametric + literature context) |
| **Critic** | Attacks hypotheses (8 vectors + min adversarial standard) |
| **Ranker** | 6-dimension scoring (mandatory per-hypothesis table) + diversity |
| **Evolver** | Recombines with diversity constraint |
| **Quality Gate** | 9-point rubric + web novelty/grounding verification |

## State Management

All structured state lives in `state/session.json`.
Human-readable outputs in `results/*.md`.
Every agent reads/writes `state/session.json` as source of truth.

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

## Key Design Decisions (v5)
1. **Parametric generation + retrieval validation** — LLM generates,
   external sources validate. Not parametric-only, not retrieval-only.
2. **Groundedness scoring** (20% weight) — prevents fluent hallucinations
   from scoring high.
3. **Diversity constraint** — Evolver tracks conceptual distance between
   hypotheses to prevent convergence.
4. **Structured state** — JSON state file survives context compaction.
5. **Agent Teams for Phase 0** — Scout + Literature Scout run in parallel.
6. **Mandatory agent dispatch** — Orchestrator has no WebSearch/WebFetch,
   maxTurns=50. Cannot execute phases inline. Must dispatch to sub-agents.
7. **MCP-first literature retrieval** — Semantic Scholar + PubMed MCP
   tools are mandatory first step before any WebSearch.
8. **Quality Gate as separate agent** — Dedicated Opus agent with web
   tools for 9-point rubric + novelty verification.

## Documentation Rules
When modifying the pipeline (agents, hooks, skills, commands), update:
- `CLAUDE.md` — Architecture table, design decisions
- `README.md` — Architecture, phase list, project structure
- `docs/methodology-v5.md` — Full methodology with evidence
Keep all three aligned. Docs drift = architectural confusion.
