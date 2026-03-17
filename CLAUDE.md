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

Eight agents. Orchestrator dispatches to all — never executes phases inline.
Agent prompts use GOAL/CONSTRAINTS/STRATEGIES structure (v5.1) with v5.2 prompt engineering best practices:

| Agent | Role |
|---|---|
| **Scout** | Finds WHERE to look (8 strategies, parametric + web). TARGET QUALITY CHECK reflection |
| **Literature Scout** | MCP mandatory first, then WebSearch fallback. RETRIEVAL QUALITY CHECK reflection |
| **Orchestrator** | Dispatches to agents, guard logic, adaptive cycles, session health |
| **Generator** | Creates hypotheses (parametric + literature context). SELF-CRITIQUE reflection |
| **Critic** | Attacks hypotheses (8 vectors + META-CRITIQUE reflection). Writes critic_questions for Generator |
| **Ranker** | 6-dimension scoring (mandatory per-hypothesis table) + diversity |
| **Evolver** | Recombines with diversity constraint. EVOLUTION QUALITY CHECK reflection. Conditionally skippable |
| **Quality Gate** | 9-point rubric + web novelty/grounding + META-VALIDATION reflection |

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

## Key Design Decisions (v5/v5.1/v5.2/v5.3)
1. **Parametric generation + retrieval validation** — LLM generates,
   external sources validate. Not parametric-only, not retrieval-only.
2. **Groundedness scoring** (20% weight) — prevents fluent hallucinations
   from scoring high. Always integer 1-10 in JSON.
3. **Diversity constraint** — Evolver tracks conceptual distance between
   hypotheses to prevent convergence.
4. **Structured state** — JSON state file survives context compaction.
5. **Agent Teams for Phase 0** — Scout + Literature Scout run in parallel.
6. **Mandatory agent dispatch** — Orchestrator has no WebSearch/WebFetch,
   maxTurns=80. Cannot execute phases inline. Must dispatch to sub-agents.
7. **MCP-first literature retrieval** — Semantic Scholar + PubMed MCP
   tools are mandatory first step before any WebSearch.
8. **Quality Gate as separate agent** — Dedicated Opus agent with web
   tools for 9-point rubric + novelty verification.
9. **GOAL/CONSTRAINTS/STRATEGIES prompt structure** (v5.1) — Agent prompts
   define the goal and hard constraints, with strategies as advisory.
   Better models find better reasoning paths; constraints maintain floor.
10. **Reflection loops** (v5.1) — SELF-CRITIQUE (Generator), META-CRITIQUE
    (Critic), TARGET QUALITY CHECK (Scout), META-VALIDATION (Quality Gate).
    Reflection multiplies capability — better models reflect more effectively.
11. **Adaptive cycles** (v5.1) — Orchestrator can early-complete (cycle 1
    top-3 >= 7.0), extend to cycle 3 (survival < 30%), or skip Evolver
    (cycle 2 top-3 >= 6.5). Prevents wasting compute on already-good results.
12. **Bidirectional feedback** (v5.1) — Critic writes critic_questions to
    state; Orchestrator forwards to Generator in cycle 2. Indirect feedback
    preserves centralized pattern.
13. **Prompt engineering alignment (v5.2)** — Agent prompts follow
    2026 best practices: XML tags for content separation, role sentences,
    WHY explanations on constraints, few-shot examples (Generator, Critic,
    Ranker, Evolver), reduced MUST/CRITICAL language for Opus 4.6,
    data-top/task-bottom dispatch structure, reflection loops for
    Literature Scout and Evolver, Sonnet-specific scaffolding, model-specific
    export prompts (GPT-5.4: output contracts + verification loops,
    Gemini 3.1: few-shot + context-first + strict grounding).
14. **Session-scoped results (v5.3)** — Each session writes to
    `results/{session-id}/` to prevent file conflicts between sessions.
    No more need for manual archiving.
15. **Plan mode auto-exit (v5.3)** — `/discover` automatically exits plan
    mode before launching. The pipeline is fully autonomous and cannot
    operate under plan mode's read-only constraint.
16. **Hook schema compliance (v5.3)** — All hooks use correct Claude Code
    schema (`"approve"/"block"` not `"allow"`, stdin for PostToolUse,
    `"verdict"` field for kill detection).

## Documentation Rules
When modifying the pipeline (agents, hooks, skills, commands), update:
- `CLAUDE.md` — Architecture table, design decisions
- `README.md` — Architecture, phase list, project structure
- `docs/methodology-v5.md` — Full methodology with evidence
Keep all three aligned. Docs drift = architectural confusion.
