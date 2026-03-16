# Scientific Discovery Engine v4

Experiment in fully autonomous AI scientific discovery. Tests whether
a multi-agent system with frontier models (March 2026) can find real
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

Seven agent files + Quality Gate inline in Orchestrator:

| Agent | Role |
|---|---|
| **Scout** | Finds WHERE to look (8 strategies, parametric + web) |
| **Literature Scout** | Retrieves scientific literature for grounding |
| **Orchestrator** | Coordinates all phases, manages state, runs Quality Gate |
| **Generator** | Creates hypotheses (parametric + literature context) |
| **Critic** | Attacks hypotheses (adversarial + web search) |
| **Ranker** | Scores 6 dimensions (incl. Groundedness 20%) + diversity check |
| **Evolver** | Recombines with diversity constraint |

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

## Key Design Decisions (v4)
1. **Parametric generation + retrieval validation** — LLM generates,
   external sources validate. Not parametric-only, not retrieval-only.
2. **Groundedness scoring** (20% weight) — prevents fluent hallucinations
   from scoring high.
3. **Diversity constraint** — Evolver tracks conceptual distance between
   hypotheses to prevent convergence.
4. **Structured state** — JSON state file survives context compaction.
5. **Agent Teams for Phase 0** — Scout + Literature Scout run in parallel.
