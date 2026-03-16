# MAGELLAN
### Multi-Agent Generative Exploration of Latent Links Across kNowledge

Autonomous AI experiment in cross-disciplinary scientific discovery.
Can a multi-agent system autonomously find real scientific connections
that humans haven't made yet? This project tests that question.

No domain expertise required from the user. Type `/discover`, walk away.
Come back to find testable hypothesis cards, then validate cross-model.

## Quick Start

```bash
cd magellan
claude --permission-mode auto
```

### Primary mode (fully autonomous — the whole point)
```
/discover
```

### Alternative modes (for targeted testing)
```
/discover circadian biology × tumor immune evasion
/discover solve: antibiotic resistance
```

## What Happens When You Run /discover

```
Phase 0:  Scout + Literature Scout (parallel) find WHERE to look
Phase 1:  Orchestrator merges results, selects best target
Phase 2:  Generator creates 6-8 hypotheses (parametric + lit. context)
Phase 3:  Critic attacks all hypotheses (adversarial + web search)
Phase 4:  Ranker scores on 6 dimensions + diversity check
Phase 5:  Evolver recombines top candidates
          ── Cycle 2: Phases 2-5 repeat with evolved + fresh hypotheses ──
Phase 6:  Quality Gate (Orchestrator) — checklist pass/fail
Phase 7:  Web grounding — final novelty + counter-evidence search
Phase 8:  Session summary → results/
```

Typical runtime: 15-45 minutes. Check progress with `/status`.

## After Discovery: Cross-Model Validation

```
/export gpt       → produces results/export-gpt.md
```
Copy the file content into ChatGPT (GPT-5.4 Thinking/Pro + Deep Research).
See `prompts/orchestration-guide.md` for step-by-step instructions.

## Commands

| Command | What it does |
|---|---|
| `/discover` | Full autonomous (Scout finds targets) |
| `/discover [A] × [C]` | Targeted discovery between two fields |
| `/discover [topic]` | Open exploration from one domain |
| `/discover solve: [problem]` | Problem-driven discovery |
| `/validate [hypothesis]` | Deep novelty + counter-evidence check |
| `/evolve` | Another evolutionary cycle on current results |
| `/export gpt` | Self-contained prompt for GPT-5.4 validation |
| `/export gemini` | Self-contained prompt for Gemini Deep Think |
| `/status` | Check pipeline progress mid-run |

## Project Structure

```
CLAUDE.md                                    ← Project memory
.claude/
  settings.json                              ← Permissions, hooks, Agent Teams
  agents/
    discovery-orchestrator.md                 ← Coordinates all phases + Quality Gate
    sde-scout.md                             ← Finds WHERE (8 strategies)
    sde-literature-scout.md                  ← Retrieves literature context
    sde-generator.md                         ← Creates hypotheses
    sde-critic.md                            ← Attacks hypotheses
    sde-ranker.md                            ← 6-dimension scoring + diversity check
    sde-evolver.md                           ← Recombines with diversity constraint
  commands/
    discover.md                              ← /discover (main entry point)
    validate.md                              ← /validate deep check
    evolve.md                                ← /evolve refinement cycle
    export.md                                ← /export for cross-model validation
    status.md                                ← /status pipeline progress
  skills/
    discovery-engine/SKILL.md                ← Core methodology + hypothesis card format
    hypothesis-validation/SKILL.md           ← Validation protocol + groundedness
    literature-retrieval/SKILL.md            ← Search patterns for scientific DBs
    domain-life-sciences/SKILL.md            ← Bio/med domain knowledge
    domain-physics-math/SKILL.md             ← Physics/math domain knowledge
prompts/
  gpt-validation.md                          ← GPT-5.4 validation prompt
  gemini-deep-think.md                       ← Gemini mathematical structure prompt
  orchestration-guide.md                     ← Cross-model validation step-by-step
docs/
  methodology-v4.md                          ← Full methodology with evidence
state/                                       ← JSON state (machine-readable)
results/                                     ← Markdown output (human-readable)
```

## Design Rationale

See `docs/methodology-v4.md` for the full evidence-based rationale,
including comparison with Google AI Co-Scientist, FutureHouse Kosmos,
MOOSE-Chem, and Aletheia.

## License

MIT
