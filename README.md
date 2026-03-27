# MAGELLAN
### Multi-Agent Generative Exploration of Latent Links Across kNowledge

Autonomous AI experiment in cross-disciplinary scientific discovery.
Can a multi-agent system autonomously find real scientific connections
that humans haven't made yet? This project tests that question.

No domain expertise required from the user. Type `/discover`, walk away.
Come back to find testable hypothesis cards, then validate cross-model.
Optimized for cross-disciplinary life sciences discovery (retrieval tools,
scoring weights, hypothesis format); other domains are supported but
scores reflect infrastructure asymmetry, not hypothesis quality.
Impact-aware prioritization (v5.14) steers the pipeline toward high-impact
directions via tiebreakers, decomposed scoring, and meta-learning — without
sacrificing novelty or rigor.

## Quick Start

```bash
cd magellan-cli
claude --enable-auto-mode
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
Phase 0a: Scout generates 5-6 candidates (10 strategies + bridge concepts
            + strategy diversification + exploration slot
            + rotating creativity constraint)
Phase 0b: Literature Scout verifies disjointness for ALL candidates
            (domain-aware retrieval + bridge validation)
Phase 0c: Orchestrator narrows to 3 (DISJOINT priority + strategy diversity)
Phase 0d: Target Evaluator — adversarial challenge on 4 axes
Phase 1:  Orchestrator selects best target
          (hard constraint: DISJOINT preferred over PARTIALLY_EXPLORED)
          → Computational Validator — KEGG, STRING, PubMed co-occurrence,
            back-of-envelope physics checks
Phase 2:  Generator builds Structured Relationship Map, then creates
          6-8 hypotheses (parametric + literature + computational validation
            + bisociation + multi-level abstraction)
          → SELF-CRITIQUE + claim-level verification before output
Phase 3:  Critic attacks all hypotheses (9 vectors + web search)
          → META-CRITIQUE reflection + critic_questions for Generator
          → Groundedness reinforcement (if majority LOW/SPECULATIVE)
Phase 4:  Ranker scores on 6 dimensions + diversity check + Elo sanity check
          → ADAPTIVE CYCLE DECISION: early-complete | standard | extended
Phase 5:  Evolver recombines top candidates (conditionally skippable)
          ── Cycle 2: Phases 2-5 repeat with evolved + fresh hypotheses ──
          ── Critic questions forwarded to Generator in cycle 2 ──
          ── Conditional: skip Evolver if cycle 2 top-3 >= 6.5 ──
Phase 6:  Quality Gate — 10-point rubric + web grounding + per-claim verification
          → META-VALIDATION reflection before output
          → Session Analyst — meta-learning metrics → knowledge/meta-insights.md
Phase 7:  Cross-Model Validation — GPT-5.4 Pro (web search + code interpreter) +
          Gemini 3.1 Pro (code execution + Google Search grounding) → consensus report
          (automatic if API keys set, export files only otherwise)
Phase 7b: Convergence Scanner — ClinicalTrials.gov, NIH Reporter, patents (non-blocking)
          Dataset Evidence Miner — HPA, GWAS, ChEMBL, UniProt, PDB queries (non-blocking)
Phase 8:  Session summary → results/{session-id}/
Phase 9:  Knowledge persistence → knowledge/discovery-log.json + strategy metrics
```

Typical runtime: 20-55 minutes. Check progress with `/status`.

## After Discovery: Cross-Model Validation

**Automatic (v5.6+)**: If `OPENAI_API_KEY` and/or `GEMINI_API_KEY` are set,
the pipeline automatically calls GPT-5.4 Pro (with web search + code interpreter)
and Gemini 3.1 Pro (with code execution + Google Search grounding) for
independent validation and generates a consensus report.

```bash
# Enable automatic cross-model validation (optional)
export OPENAI_API_KEY="sk-..."
export GEMINI_API_KEY="AI..."
npm install   # one-time setup for API dependencies
```

**Manual fallback**: If no API keys are set, export files are generated:
```
/export gpt       → produces results/{session-id}/export-gpt.md
/export gemini    → produces results/{session-id}/export-gemini.md
```
Copy into ChatGPT / Gemini AI Studio.
See `prompts/orchestration-guide.md` for step-by-step instructions.

## Commands

| Command | What it does |
|---|---|
| `/discover` | Full autonomous (Scout finds targets) |
| `/discover [A] × [C]` | Targeted discovery between two fields |
| `/discover [topic]` | Open exploration from one domain |
| `/discover solve: [problem]` | Problem-driven discovery |
| `/discover --context "text"` | Provide domain expertise as context for Scout/Generator |
| `/discover --papers DOI1,DOI2` | Provide seed papers for Literature Scout |
| `/discover --interactive` | Pause after Scout for target approval before proceeding |
| `/connect <key>` | Link CLI to your MAGELLAN web profile for attribution |
| `/validate [hypothesis]` | Deep novelty + counter-evidence check |
| `/evolve` | Another evolutionary cycle on current results |
| `/export gpt` | Self-contained prompt for GPT-5.4 validation |
| `/export gemini` | Self-contained prompt for Gemini Deep Think |
| `/status` | Check pipeline progress mid-run |
| `/validate-holdout` | Run holdout validation test (rediscovery check) |

Flags can be combined: `/discover ferroptosis × serpentinization --context "I study lipid peroxidation in hepatocytes" --papers 10.1038/s41586-024-xxxxx --interactive`

## Contribute Your Discoveries

Connect to the [MAGELLAN website](https://magellan-discover.ai) so your discoveries
are publicly attributed to you:

1. Create an account at [magellan-discover.ai/sign-in](https://magellan-discover.ai/sign-in)
2. Go to your profile and generate a **Contributor Key**
3. In the CLI: `/connect mgln_your_key_here`
4. All subsequent `/discover` sessions are attributed to your profile

Your discoveries appear on the public leaderboard with your name, institution,
and rank (Cabin Boy → Navigator → Cartographer → Captain → Admiral).

Scientists with domain expertise can use `--context` and `--papers` to direct
discovery toward their areas of interest, and review hypotheses on the website
as expert reviewers.

## Project Structure

```
CLAUDE.md                                    ← Project instructions for Claude Code
.mcp.json                                   ← MCP servers (Semantic Scholar, PubMed)
.claude/
  settings.json                              ← Permissions, hooks, Agent Teams
  agents/
    discovery-orchestrator.md                 ← Dispatches to agents, guard logic [Opus, max]
    scout.md                                 ← Finds WHERE (10 strategies) [Opus, max]
    target-evaluator.md                      ← Adversarial target challenge [Opus, max]
    literature-scout.md                      ← Retrieves literature context [Sonnet, high]
    computational-validator.md               ← Programmatic bridge checks [Sonnet, high]
    generator.md                             ← Creates hypotheses [Opus, max]
    critic.md                                ← Attacks hypotheses (9 attack vectors) [Opus, max]
    ranker.md                                ← 6-dimension scoring + Elo sanity check [Sonnet, high]
    evolver.md                               ← Recombines with diversity constraint [Sonnet, high]
    quality-gate.md                          ← 10-point rubric + web grounding [Opus, max]
    session-analyst.md                       ← Post-pipeline meta-learning [Sonnet, high]
  commands/
    discover.md                              ← /discover (main entry point)
    connect.md                               ← /connect contributor key
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
  session-summary-format.md                  ← Session summary formatting per status type
  ingest-schema.json                         ← Schema for website ingest manifest
  knowledge-schema.json                      ← Schema for discovery-log entries
docs/
  methodology-v5.md                          ← Full methodology with evidence
  CHANGELOG.md                               ← Pipeline evolution history
scripts/                                     ← Hook scripts + orchestrator support scripts
  init-session.sh                            ← Session initialization (state + results dir)
  upload-session.mjs                         ← Website upload (ingest → API)
state/                                       ← Coordination state (machine-readable)
  session.json                               ← Slim coordination index (~3KB)
  dispatch-log.json                          ← Agent dispatch log with timestamps
results/                                     ← All session outputs (markdown + JSON)
  {session-id}/                              ← Session-scoped directory
    papers/                                  ← Full-text papers retrieved by Literature Scout
    scout-targets.md                         ← Scout output
    scout.json                               ← Scout targets + quality scores (structured)
    target-evaluation.md                     ← Target Evaluator output
    literature.json                          ← Literature context + paper metadata
    computational-validation.md              ← Computational Validator output
    computational.json                       ← Computational readiness checks
    raw-hypotheses-cycle{N}.md               ← Generation output
    cycle{N}-raw.json                        ← Raw hypotheses (IDs, titles, scores)
    critiqued-cycle{N}.md                    ← Critique output
    cycle{N}-critiqued.json                  ← Critique verdicts + critic_questions
    ranked-cycle{N}.md                       ← Ranking output
    cycle{N}-ranked.json                     ← Rankings + composite scores
    evolved-cycle{N}.md                      ← Evolution output
    cycle{N}-evolved.json                    ← Evolved hypotheses with lineage
    quality-gate.md                          ← Quality Gate rubric
    quality-gate.json                        ← Quality gate verdicts
    final-hypotheses.md                      ← Final hypothesis cards
    final.json                               ← PASS/CONDITIONAL_PASS only
    session-analysis.md                      ← Session Analyst output
    meta-insights.json                       ← Session analyst structured output
    export-gpt.md                            ← GPT validation prompt
    export-gemini.md                         ← Gemini validation prompt
    validation-gpt.md                        ← GPT-5.4 Pro response (if API key set)
    validation-gemini.md                     ← Gemini 3.1 Pro response (if API key set)
    cross-model-consensus.md                 ← Consensus report (if any API key set)
    cross-model.json                         ← Cross-model validation consensus
    session-summary.md                       ← Session overview
knowledge/                                   ← Persistent data across sessions
  discovery-log.json                         ← Explored pairs, productive bridges, kill reasons
  meta-insights.md                           ← Cumulative meta-learning insights
```

## Architecture

15 specialized agents with model differentiation (Opus for deep reasoning, Sonnet for structured tasks). Effort levels are pinned per agent (Opus: max, Sonnet: high) to guarantee quality regardless of the user's session-level effort setting:

- **Scout** [Opus, max] — 10 strategies to find WHERE undiscovered connections hide (incl. structural isomorphism + serendipity). TARGET QUALITY CHECK + strategy diversification + exploration slot + rotating creativity constraint
- **Target Evaluator** [Opus, max] — Adversarial challenge of Scout targets on 4 axes (popularity, vagueness, impossibility, local-optima)
- **Literature Scout** [Sonnet, high] — MCP servers (mandatory first step) + WebSearch fallback + full-text paper retrieval + RETRIEVAL QUALITY CHECK reflection
- **Computational Validator** [Sonnet+Bash, high] — Programmatic bridge verification: KEGG, STRING, PubMed co-occurrence, back-of-envelope physics
- **Generator** [Opus, max] — Parametric creativity + literature + computational validation → 6-8 hypotheses per cycle. SELF-CRITIQUE + claim-level verification reflection
- **Critic** [Opus, max] — 9 adversarial attack vectors (incl. claim-level fact verification) + META-CRITIQUE reflection + critic_questions feedback
- **Ranker** [Sonnet, high] — 6-dimension scoring (Impact decomposed into Paradigm 5% + Translational 5%) + diversity check + Elo tournament sanity check
- **Evolver** [Sonnet, high] — Crossover, mutation, specification with diversity constraint + EVOLUTION QUALITY CHECK reflection (conditionally skippable)
- **Quality Gate** [Opus, max, 35 turns] — 10-point rubric + web novelty + per-claim grounding verification + impact annotation (informational) + META-VALIDATION reflection
- **Session Analyst** [Sonnet, high] — Post-pipeline meta-learning: strategy performance, kill patterns, bridge type analysis → knowledge/meta-insights.md
- **Cross-Model Validator** [Sonnet, high] — Calls GPT-5.4 Pro (web search + code interpreter) + Gemini 3.1 Pro (code execution + Google Search grounding) APIs for independent validation → consensus report (requires API keys; falls back to export files)
- **Convergence Scanner** [Sonnet, high] — Post-QG: searches ClinicalTrials.gov, NIH Reporter, patents for independent convergence signals + partial mechanism confirmations from non-pipeline sources
- **Dataset Evidence Miner** [Sonnet, high] — Post-QG: queries HPA, GWAS Catalog, ChEMBL, UniProt, PDB via `scripts/query-biodata.py` to verify specific molecular claims in passing hypotheses
- **Holdout Evaluator** [Opus, max] — Validation framework: compares MAGELLAN output against known post-cutoff discoveries with contamination check + mechanism similarity scoring
- **Orchestrator** [Opus, max, 200 turns circuit breaker] — Dispatches to all agents, adaptive cycle decisions, guard logic, session health, meta-learning metrics

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
evidence-based design rationale, and risk analysis. See `docs/CHANGELOG.md` for
the evolution history of the pipeline.

## License

MIT — Copyright (c) 2026 Alberto Trivero / Kakashi Venture Accelerator

Built where science meets AI. [kakashi.ventures](https://kakashi.ventures)
