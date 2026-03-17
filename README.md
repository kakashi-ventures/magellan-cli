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
Phase 0:  Scout (8 strategies + mandatory bridge concepts)
          + Literature Scout (web search + full-text paper retrieval
            + disjointness verification) — in parallel
Phase 1:  Orchestrator merges results, selects best target
Phase 2:  Generator builds Structured Relationship Map, then creates
          6-8 hypotheses (parametric + lit. context + full papers)
Phase 3:  Critic attacks all hypotheses (adversarial + web search)
Phase 4:  Ranker scores on 6 dimensions + diversity check
Phase 5:  Evolver recombines top candidates
          ── Cycle 2: Phases 2-5 repeat with evolved + fresh hypotheses ──
Phase 6:  Quality Gate (dedicated agent) — 9-point rubric + web grounding
Phase 7:  Session summary → results/
Phase 8:  Knowledge persistence → knowledge/discovery-log.json
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
.mcp.json                                   ← MCP servers (Semantic Scholar, PubMed)
.claude/
  settings.json                              ← Permissions, hooks, Agent Teams
  agents/
    discovery-orchestrator.md                 ← Dispatches to agents, guard logic [Opus]
    scout.md                                 ← Finds WHERE (8 strategies) [Opus]
    literature-scout.md                      ← Retrieves literature context [Sonnet]
    generator.md                             ← Creates hypotheses [Opus]
    critic.md                                ← Attacks hypotheses (8 attack vectors) [Opus]
    ranker.md                                ← 6-dimension scoring + diversity check [Sonnet]
    evolver.md                               ← Recombines with diversity constraint [Sonnet]
    quality-gate.md                          ← 9-point rubric + web grounding [Opus]
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
  methodology-v5.md                          ← Full methodology with evidence
scripts/                                     ← Hook scripts (stop gates, failure tracking)
state/                                       ← JSON state (machine-readable)
results/                                     ← Markdown output (human-readable)
  papers/                                    ← Full-text papers retrieved by Literature Scout
knowledge/                                   ← Persistent discovery log across sessions
  discovery-log.json                         ← Explored pairs, productive bridges, kill reasons
```

## Architecture

8 specialized agents with model differentiation (Opus for deep reasoning, Sonnet for structured tasks):

- **Scout** [Opus] — 8 strategies to find WHERE undiscovered connections hide
- **Literature Scout** [Sonnet] — MCP servers (mandatory first step) + WebSearch fallback + full-text paper retrieval
- **Generator** [Opus] — Parametric creativity + literature context → 6-8 hypotheses per cycle
- **Critic** [Opus] — 8 adversarial attack vectors + minimum adversarial standard (30-50% kill rate)
- **Ranker** [Sonnet] — 6-dimension scoring (mandatory per-hypothesis table) + diversity check
- **Evolver** [Sonnet] — Crossover, mutation, specification with diversity constraint
- **Quality Gate** [Opus] — 9-point rubric + web novelty/grounding verification
- **Orchestrator** [Opus] — Dispatches to all agents (no inline execution), guard logic, session health

## Conceptual Foundation

MAGELLAN operationalizes Don Swanson's **Undiscovered Public Knowledge** (1986):
logically connected knowledge that exists across disjoint scientific literatures
but hasn't been linked because researchers don't read across fields. Swanson's
method was bibliometric (citation graphs, MeSH co-occurrences). MAGELLAN replaces
the method with frontier LLMs — models trained on both literatures already *have*
the connections latent in their parameters. The challenge shifts from detecting
citation disjointness to **eliciting cross-domain connections** through structured
multi-agent reasoning.

## State of the Art (March 2026)

MAGELLAN sits in a sparsely populated niche: **fully autonomous** target selection.
Most comparable systems (Google AI Co-Scientist, FutureHouse Kosmos, SciAgents)
require human-specified research objectives.

Key validations from the field:
- **MOOSE-Chem** (ICLR 2025): LLMs encode "latent scientific knowledge associations not yet recognized by humans" — direct validation of MAGELLAN's UPK thesis
- **FrontierScience Benchmark**: 52-point gap between structured (77%) and open-ended research (25%) tasks validates multi-agent approach
- **Google AI Co-Scientist**: 3 experimentally validated discoveries using parallel architecture (Generate/Reflect/Rank/Evolve)

See `docs/methodology-v5.md` for full comparison with state-of-the-art systems,
evidence-based design rationale, and risk analysis.

## License

MIT
