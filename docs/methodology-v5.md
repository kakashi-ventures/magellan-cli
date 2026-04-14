# MAGELLAN — Methodology
### Multi-Agent Generative Exploration of Latent Links Across kNowledge

**Repository**: [github.com/kakashi-ventures/magellan-cli](https://github.com/kakashi-ventures/magellan-cli) | **Website**: [magellan-discover.ai](https://magellan-discover.ai)

## Guiding principle

MAGELLAN is an **experiment in whether modern agentic AI systems can make autonomous scientific discoveries**. The core hypothesis: a well-designed multi-agent architecture running frontier models (March 2026) can find real connections between existing bodies of knowledge that humans have not yet linked — operating in full autonomy, with zero domain input from the user.

It is not a tool for researchers. It is a capability test. The user runs `/discover`, leaves the room, and comes back to find testable scientific hypotheses. These are then cross-model validated and, ideally, submitted to domain experts for evaluation.

Built for Claude Code (March 2026) with Opus 4.6 (deep reasoning) and Sonnet 4.6 (structured tasks), it leverages Agent Teams, deterministic hooks, MCP servers for structured retrieval, and a hybrid **parametric-generation + retrieval-validation** paradigm.

---

## Conceptual foundation: Swanson's Undiscovered Public Knowledge

At its core, MAGELLAN is a machine for finding **Undiscovered Public Knowledge (UPK)** — a concept formulated by Don R. Swanson in 1986.

### The concept

Swanson observed that the scientific literature contains logical connections that no one has made yet — not because the information is secret, but because it resides in **disjoint literatures**: bodies of knowledge that never cite each other. The foundational example: the literature on magnesium (vasodilatory effects, platelet anti-aggregation) and the literature on migraine (vasoconstriction, platelet aggregation) contained all the premises to hypothesize that magnesium could treat migraine. No one had made the connection because the two fields did not talk to each other. Swanson made it in 1988, and subsequent clinical trials confirmed the hypothesis.

Swanson formalized this as the **ABC model**: Field A and Field C do not cite each other, but they share an intermediate concept B (the *bridge term*) that appears in both. Discovery consists of identifying B and constructing the inference A→B→C.

### The original method (superseded)

To find these connections, Swanson developed a **bibliometric method**: co-occurrence analysis of MeSH terms, citation graphs, frequency matrices. Systems like Arrowsmith, BITOLA, and more recently automated LBD tools have refined this approach for decades.

This method is **superseded by 2026 frontier models**, for a fundamental reason: the UPK problem exists because no human researcher can read both literatures. An LLM trained on millions of papers has already *absorbed* both. The problem is no longer detecting citation disjunction — it is **eliciting the latent connections** from the model's parametric knowledge.

The evidence confirms this: none of the AI-driven breakthroughs of 2025–2026 (GPT-5 + Ginkgo, Google AI Co-Scientist, Aletheia) used bibliometric analysis. All of them use parametric knowledge + multi-agent architecture + debate/evolution.

### How MAGELLAN inherits the concept and supersedes the method

| Swanson (1986) | MAGELLAN (2026) |
|---|---|
| The problem: UPK exists between disjoint literatures | Same problem, same motivation |
| The bridge: shared concept B between A and C | **Mandatory bridge concepts** in every Scout target |
| The method: bibliometric analysis (MeSH, citations) | **Parametric knowledge** of the LLM as universal reader |
| Detection: statistical co-occurrences | **Elicitation**: Structured Relationship Map, facet recombination, adversarial probing |
| Validation: manual database search | **Automated retrieval**: Literature Scout + MCP servers + disjunction verification |
| Scale: one A–C pair per study, months of work | **10 parallel strategies**, 2 evolutionary cycles, 15–45 minutes |

The ABC model remains the structural backbone of the output: every MAGELLAN hypothesis takes the form `Field A → Bridge mechanism → Field C`. The difference is *how* the bridge is found — not through citation statistics, but through parametric reasoning by a model that has already read both literatures.

---

## Architecture: 15 agents, 3 phases

```
PHASE 1 — EXPLORATION (Sequential Narrowing)
┌──────────────┐
│    Scout      │  Phase 0a: generates 5–6 candidates
│  [Opus]       │
│ 10 strategies │
│ + diversif.   │
│ + exploration │
│   slot        │
│ + creativity  │
│   constraint  │
└──────┬───────┘
       ▼
┌──────────────────┐
│ Literature Scout  │  Phase 0b: verifies disjointness for ALL
│    [Sonnet]       │  + domain-aware retrieval
│ MCP + WebSearch   │  + bridge validation
└──────┬───────────┘
       ▼
  Orchestrator [Opus]   Phase 0c: narrows from 5–6 to 3
  (DISJOINT priority    (WELL_EXPLORED excluded, DISJOINT preferred)
   + strategy diversity)
       ▼
┌──────────────────────┐
│  Target Evaluator     │  Phase 0d: adversarial challenge
│  [Opus] 4 attack axes │
└──────────┬───────────┘
       ▼
  Orchestrator [Opus]   Phase 1: select + dispatch
  (disjointness hard constraint)
       ▼
┌──────────────────────────┐
│  Computational Validator  │  KEGG, STRING, PubMed
│  [Sonnet + Bash]         │  co-occurrence, physics
└──────────┬───────────────┘
       ▼

PHASE 2 — GENERATION & CRITIQUE (2 cycles)
┌────────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Generator  │──▶│  Critic   │──▶│  Ranker   │──▶│  Evolver  │
│   [Opus]    │   │  [Opus]   │   │ [Sonnet]  │   │ [Sonnet]  │
│ parametric  │   │ 9 attack  │   │ 6 dimens. │   │ evolution │
│ + lit.contxt│   │ + web     │   │ + grounded│   │ + diversit│
│ + comp.val. │   │           │   │ + Elo chk │   │           │
│ + bisociat. │   │           │   │           │   │           │
│ + multi-lvl │   │           │   │           │   │           │
└────────────┘   └──────────┘   └──────────┘   └──────┬────┘
       ▲                                              │
       └──────────── cycle 2 ◀────────────────────────┘

PHASE 3 — FINAL VALIDATION + META-LEARNING
┌──────────────────┐   ┌──────────────────┐
│  Quality Gate     │   │ Session Analyst   │
│    [Opus]         │──▶│   [Sonnet]        │
│ 10-point rubric   │   │ meta-learning     │
│ + web grounding   │   │ → meta-insights   │
└──────────┬───────┘   └──────────┬───────┘
           └──────────┬───────────┘
                      ▼
┌──────────────────────────┐
│  Cross-Model Validator    │  GPT-5.4 Pro + Gemini 3.1 Pro
│    [Sonnet]               │  consensus report
└──────────┬───────────────┘
           ▼
┌──────────────────────┐   ┌───────────────────────┐
│  Convergence Scanner  │   │ Dataset Evidence Miner │
│    [Sonnet]           │   │    [Sonnet]            │
│ ClinicalTrials, NIH   │   │ HPA, GWAS, ChEMBL,    │
│ Reporter, patents     │   │ UniProt, PDB           │
└──────────┬───────────┘   └──────────┬────────────┘
           └──────────┬───────────────┘
                      ▼
    Session Health → results/{session-id}/*.md + state/session.json
                   + knowledge/meta-insights.md

CROSS-CUTTING LAYER — GUARDS & HOOKS
┌─────────────────────────────────────────────────┐
│  Post-phase guards (retry → fallback → abort)   │
│  Blocking SubagentStop hooks (exit 2)           │
│  Stop hook (anti-premature-termination)         │
│  PostToolUse dispatch logging (verify-dispatch)  │
│  PreCompact/PostCompact (backup/restore state)  │
│  PostToolUseFailure (tracking WebSearch fails)  │
└─────────────────────────────────────────────────┘
```

### The 15 agents

| Agent | Model | Effort | Role |
|---|---|---|---|
| **Scout** | Opus | max | Identifies WHERE to look: 10 strategies (incl. structural isomorphism + serendipity), mandatory bridge concepts, strategy diversification, exploration slot, rotating creativity constraint, TARGET QUALITY CHECK reflection |
| **Target Evaluator** | Opus | max | Adversarial challenge of Scout targets on 4 axes: popularity bias, vagueness, structural impossibility, local-optima |
| **Literature Scout** | Sonnet | high | Structured retrieval: MCP servers (Semantic Scholar, PubMed) mandatory + WebSearch fallback + full-text + disjunction verification + RETRIEVAL QUALITY CHECK reflection |
| **Computational Validator** | Sonnet | high | Programmatic bridge concept verification: KEGG pathway cross-check, STRING interaction scores, PubMed co-occurrence, back-of-envelope physics |
| **Generator** | Opus | max | Structured Relationship Map + 6–8 hypotheses (parametric + lit. context + computational validation) + SELF-CRITIQUE with claim-level verification |
| **Critic** | Opus | max | 9 attack vectors (incl. claim-level fact verification) + META-CRITIQUE reflection + critic_questions feedback |
| **Ranker** | Sonnet | high | Scoring across 6 dimensions with fixed canonical weights + mandatory per-hypothesis table + diversity check + Elo tournament sanity check |
| **Evolver** | Sonnet | high | Evolutionary operations with diversity constraint + EVOLUTION QUALITY CHECK reflection. Conditionally skippable |
| **Quality Gate** | Opus | max | 10-point rubric (incl. per-claim grounding verification) + web grounding + META-VALIDATION reflection |
| **Session Analyst** | Sonnet | high | Post-pipeline meta-learning: strategy performance, kill patterns, bridge type analysis → knowledge/meta-insights.md |
| **Cross-Model Validator** | Sonnet | high | Calls GPT-5.4 Pro (reasoning high, web search, code interpreter) + Gemini 3.1 Pro (thinking HIGH, code execution, Google Search grounding) via API for independent validation → consensus report. Falls back to export files if API keys are absent |
| **Convergence Scanner** | Sonnet | high | Post-QG: searches for convergence signals on ClinicalTrials.gov, NIH Reporter, patents + partial sub-mechanism confirmations from sources not consulted by the pipeline |
| **Dataset Evidence Miner** | Sonnet | high | Post-QG: verifies specific molecular claims against HPA, GWAS Catalog, ChEMBL, UniProt, PDB via `scripts/query-biodata.py`. Complements the pre-generation CV |
| **Holdout Evaluator** | Opus | max | Validation framework: compares MAGELLAN output against known post-cutoff discoveries. Contamination check + mechanistic similarity scoring |
| **Orchestrator** | Opus | max | Mandatory dispatch, adaptive cycles, guard logic, session health, knowledge log, meta-learning metrics |

Model selection follows a clear principle: **Opus for deep, creative reasoning; Sonnet for structured, search-intensive tasks**. Effort levels are pinned per agent (Opus: max, Sonnet: high) to guarantee quality regardless of the user's session-level effort setting. Scout, Target Evaluator, Generator, Critic, Quality Gate, and Holdout Evaluator require cross-disciplinary reasoning and deep evaluation. Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator, Convergence Scanner, and Dataset Evidence Miner execute more structured tasks where judgment matters but does not demand Opus-level depth.

### Mandatory dispatch

The Orchestrator is a pure coordinator: it has NO access to WebSearch/WebFetch and CANNOT execute phases inline. Every phase is dispatched to the specialized sub-agent via the Agent tool. This guarantees:
- **Tool isolation**: the Generator cannot run web searches, the Critic cannot generate hypotheses
- **Specialization**: each agent loads only the relevant skills
- **Fresh context**: each dispatch starts with a clean conversational context, preventing degradation in late phases
- **Auditability**: `state/dispatch-log.json` tracks every dispatch for post-session audit

### GOAL/CONSTRAINTS/STRATEGIES prompt structure

All agent prompts (except the Orchestrator) are structured in 3 sections:

1. **GOAL** (immutable) — What the agent must produce, defined by output quality criteria
2. **CONSTRAINTS** (hard) — Requirements that must be met regardless of approach
3. **STRATEGIES** (advisory) — Suggested approaches, explicitly marked as recommended but not mandatory

**Why this scales**: A more capable model, given a goal and constraints, finds better reasoning paths than if forced to follow prescribed steps. CONSTRAINTS preserve the quality floor. STRATEGIES remain as guidance for less capable models. SubagentStop hooks catch sub-threshold output regardless of model.

The Orchestrator is NOT restructured this way — it is a dispatcher, not a reasoner. Its prompt is procedural by design (read state → dispatch → read state → check gate → dispatch next).

### Reflection loops

Six agents have self-review sections before producing final output:

| Agent | Reflection | What it does |
|--------|-----------|---------|
| **Generator** | SELF-CRITIQUE | Verifies mechanism specificity, bridge duplication, parametric error sources |
| **Critic** | META-CRITIQUE | Calibrates kill rate, identifies the strongest reason to kill each SURVIVES, verifies web search completeness |
| **Scout** | TARGET QUALITY CHECK | Verifies bridge specificity, strategic diversity, non-obviousness |
| **Quality Gate** | META-VALIDATION | Verifies confidence in PASS verdicts, web search completeness, impact of UNVERIFIABLE claims |
| **Literature Scout** | RETRIEVAL QUALITY CHECK | Verifies MCP completeness, paper count per field, gap analysis specificity |
| **Evolver** | EVOLUTION QUALITY CHECK | Verifies genuine improvement over parent, bridge duplication, crossover coherence |

Reflection is a capability multiplier: a better model reflects more effectively. External evaluation structures (SubagentStop hooks, ranker 3KB gate) prevent reflection from degenerating into self-congratulation.

### Adaptive cycles

The Orchestrator has 3 decision points to adapt the pipeline to output quality:

1. **Groundedness Reinforcement** (after cycle 1 critique): If most hypotheses have LOW/SPECULATIVE Groundedness, re-dispatch the Literature Scout with targeted searches on the specific mechanisms. This feeds the Generator in cycle 2.

2. **Adaptive Cycle Decision** (after cycle 1 ranking):
   - Top-3 ≥ 7.0 AND diversity passed → **early complete** (dispatch Quality Gate, skip cycle 2)
   - Survival < 30% OR top-3 < 4.0 → **extended** (require cycle 2, consider cycle 3)
   - Otherwise → **standard** (normal cycle 2)

3. **Conditional Evolution** (cycle 2, after ranking): If top-3 ≥ 6.5, diversity passed, no shared bridges → skip Evolver, proceed to Quality Gate. `orchestrator-stop-gate.py` updated to not block on legitimate evolver skips.

**Why this scales**: A better model produces higher-quality output earlier in the pipeline. Without adaptivity, the system wastes compute. With it, Opus 5 could complete in 1 cycle what Opus 4.6 needs 2.

### Indirect bidirectional feedback

The Critic can write specific questions in `results/{session-id}/cycle{N}-critiqued.json` under `critic_questions` when a mechanism is too vague to be attacked properly. The Orchestrator forwards these questions to the Generator in the cycle 2 dispatch. Indirect feedback (via state JSON) preserves the centralized dispatch pattern.

---

## The hybrid paradigm: Parametric Generation + Retrieval Validation

### The evidence

Frontier models (Opus 4.6, GPT-5.2, Gemini 3.1 Pro) score 91–94% on GPQA Diamond — PhD-level questions in biology, physics, and chemistry. This is a 55-point jump from GPT-4 (39%, 2023). Parametric knowledge has improved enormously.

However:
- **AA-Omniscience** (open factual recall): the best model reaches only 55% accuracy
- **Hallucination rate**: 22–48% depending on model and benchmark
- **FrontierScience-Research** (open research): GPT-5.2 achieves only 25.3%
- Peer-reviewed scientific literature behind paywalls is largely absent from training data

### The MAGELLAN compromise

Parametric knowledge is **the generative engine** — it is where the non-obvious cross-disciplinary connections reside. But every factual claim is verified through retrieval. The flow:

1. **Scout (parametric)**: Identifies WHERE to look using deep reasoning with 10 strategies. Produces **mandatory bridge concepts** — specific mechanisms connecting Field A to Field C. Generates 5–6 candidates (wide pool). Consults `knowledge/discovery-log.json` and `knowledge/meta-insights.md` to avoid re-exploration, reuse productive bridges, and prioritize strategies with high survival rates
1b. **Literature Scout (verification)**: Verifies disjointness for ALL 5–6 Scout candidates using domain-appropriate sources. Validates bridge concepts. The Orchestrator then filters down to 3 candidates (DISJOINT priority)
2. **Target Evaluator (adversarial)**: Challenges the 3 filtered targets on 4 axes: popularity bias, vagueness, structural impossibility, local-optima. Prevents wasted sessions on targets that look interesting but are already explored, vague, or structurally impossible
3. **Literature Scout (retrieval)**: Verifies that targets are not already explored; finds recent literature in the target fields. Uses **MCP servers** (Semantic Scholar, PubMed) as the primary source and WebSearch as fallback. **Retrieves full text for the top 5–10 papers**. Performs a **disjunction verification** to confirm the connection is genuinely UPK
4. **Computational Validator (programmatic)**: Verifies bridge concepts through KEGG pathway cross-check, STRING interaction scores, PubMed co-occurrence, and back-of-envelope calculations. Catches quantitatively impossible mechanisms before the pipeline invests in generation. Warn-only: absence of evidence in databases is not evidence of absence
5. **Generator (parametric + literature context + computational validation)**: First builds a **Structured Relationship Map** (on-the-fly parametric KG) for each field, then generates hypotheses using reasoning + context + full papers + Computational Validator signals
6. **Critic (parametric + web search)**: Attacks each hypothesis with 9 attack vectors (including claim-level fact verification), searches for counter-evidence via web, runs the hallucination-as-novelty check
7. **Ranker**: Scores across 6 dimensions including **Groundedness** (20%), diversity check, Elo tournament sanity check
8. **Evolver**: Operates on top hypotheses with a **diversity constraint**
9. **Session Analyst**: Post-Quality-Gate, analyzes strategy performance, kill patterns, bridge type survival rates, disjointness correlation. Produces `knowledge/meta-insights.md` for subsequent sessions
10. **Cross-Model Validator**: Post-Session-Analyst. Generates validation prompts tailored to specific hypotheses, then calls the OpenAI (GPT-5.4 Pro, reasoning high) and Google (Gemini 3.1 Pro, thinking HIGH) APIs in parallel via `scripts/validate-crossmodel.mjs`. Produces a consensus report identifying convergences and divergences between models. If API keys are not configured, generates only export files for manual validation. **Non-blocking**: failures do not change session status
11. **Knowledge Persistence**: At session end, the Orchestrator updates both `knowledge/discovery-log.json` (structured: explored pairs, productive bridges, surviving and killed hypotheses, strategy performance metrics) and `knowledge/meta-insights.md` (cumulative prose: strategy performance trends, bridge type survival rates, kill pattern observations). Both files are required -- skipping either means the session's insights are lost to future sessions

---

## Structured retrieval

### MCP Servers (mandatory step)

Retrieval via WebSearch/WebFetch is fragile and requires HTML parsing. MAGELLAN integrates MCP servers as the **mandatory first step** for bibliographic search:

- **Semantic Scholar MCP** (`@xbghc/semanticscholar-mcp`): `search_papers`, `get_paper`, `get_paper_citations`, `get_paper_references`, `get_recommendations`, `batch_get_papers`
- **PubMed MCP** (`pubmed-mcp`): `pubmed_search`, `pubmed_abstract`, `pubmed_full_text`, `pubmed_open_access`, `pubmed_cited_by`, `pubmed_cites`, `pubmed_similar`

Configured in `.mcp.json` at the project root. The Literature Scout MUST call MCP tools **before** any WebSearch. Fallback to WebSearch only if MCP returns a connection error or insufficient results. This provides a structured retrieval channel independent of generic web search, with machine-readable metadata (authors, citations, abstracts, MeSH terms) without HTML parsing.

### Structured APIs (via WebFetch)

Beyond MCP servers and web search, the Literature Scout queries REST APIs for machine-readable data invisible to web search:

- **PubMed E-Utilities (NCBI)**: Structured metadata, MeSH terms, citation graphs
- **KEGG REST API**: Pathway cross-referencing — maps genes → pathways → diseases → drugs. Discovery pattern: gene from Field A → KEGG pathway → shared pathway with gene from Field C → latent mechanistic link
- **STRING Protein Interaction Network**: Protein-protein interaction data with confidence scores. Validates whether proteins from seemingly unrelated fields have known or predicted interactions

### Full-text paper retrieval

The Literature Scout does not stop at search snippets. For the top 5–10 papers per field, it uses WebFetch to retrieve full text and saves it in `results/papers/`. The Generator reads these papers directly, reasoning at the sentence and mechanism level rather than at the abstract level.

The difference: "Field A studies autophagy" vs. "paragraph 3.2 of Zhang et al. describes an ATG5-BECN1 pathway that is structurally analogous to the pathway Smith et al. describe in Field C, but with different substrates."

### Disjunction verification (Novelty Sanity Check)

Before finalizing the literature context, the Literature Scout verifies that the proposed connection is genuinely underexplored:
- Searches for reviews, surveys, and meta-analyses explicitly linking the two fields
- Classifies the result as **DISJOINT** (no cross-field literature), **PARTIALLY EXPLORED** (some connections but gaps in mechanisms), or **WELL-EXPLORED** (connection already widely published)

This prevents the pipeline from wasting cycles on connections that are not genuinely UPK. A "WELL-EXPLORED" result is high-value information — not a failure.

---

## The Scout: 10 strategies

1. **Recent Breakthrough Radiation** — Implications of recent discoveries for non-obvious fields
2. **Anomaly Hunting** — Reproducible but unexplained phenomena
3. **Converging Vocabularies** — Fields that use similar terminology/frameworks without knowing it
4. **Tool Transfer Opportunities** — Tools from Field A applicable to Field C
5. **Scale Bridging Gaps** — Phenomena understood at one scale but absent at adjacent scales
6. **Failed Paradigm Recycling** — Ideas abandoned in one field that might work elsewhere
7. **Swanson ABC Bridging** — Systematic identification of disjoint literatures with shared intermediate concepts. Foundational method of Literature-Based Discovery (Swanson 1986). The Literature Scout systematically searches for "B terms" that appear in both Fields A and C without A and C citing each other
8. **Contradiction Mining** — Active search for contradictions in the literature as hypothesis sources. Inspired by FutureHouse's ContraCrow. If two papers in different fields make mutually exclusive claims, resolving the contradiction often reveals a non-trivial connection
9. **Structural Isomorphism Discovery** — Seeks fields that share the SAME formal structure (mathematical equations, network topology, information-theoretic constraints, phase transition dynamics) but with COMPLETELY different physical substrates. The bridge concept is the MATHEMATICAL OBJECT itself, not a molecule or pathway. This strategy is domain-agnostic — it works for any scientific field. Example: percolation theory connects epidemiology and fracture mechanics
10. **Serendipity Through Random Encounter** — Instead of purposeful search, exposure to unexpected knowledge: (1) pick a domain NEVER explored in previous sessions, (2) find the most SURPRISING recent discovery in that domain, (3) ask "which DISTANT field would be most transformed by knowing about this discovery?" The connection must cross at least 2 disciplinary boundaries. Mimics the serendipity of browsing a physical library

### Mandatory bridge concepts

Bridge concepts are **mandatory for every target**, not just for the Swanson strategy. Even for Anomaly Hunting, Tool Transfer, or Scale Bridging, the Scout must articulate the concrete connection mechanism (molecules, pathways, mathematical structures, physical principles). This forces more structured reasoning and gives the Generator a richer starting point than a bare pair of fields.

### Strategy diversification + exploration slot

Of the 3 selected targets, at least 2 must use different strategies and at least 1 must use a strategy not employed in the last 2 sessions (verified via discovery-log). This prevents strategic path-lock: less-used strategies are not necessarily worse — they are less explored.

**Exploration slot**: At least 1 of the 3 targets MUST use a strategy with fewer than 2 sessions of primary data. This prevents the pipeline from always converging on the strategy with the best QG pass rate (e.g., network_gap_analysis at 39%) at the expense of more creative but less tested strategies.

### Rotating creativity constraint

The Orchestrator assigns the Scout a different creativity constraint each session (mod 5 rotation): cross-discipline bridge, mathematical/formal bridge, temporal gap >50 years, tool transfer, unsolved problem. This forces the Scout to explore territory it would otherwise avoid, preventing convergence toward "safe" zones.

### Cross-session knowledge persistence

Before beginning exploration, the Scout consults `knowledge/discovery-log.json` to:
- Avoid re-exploring previously investigated pairs
- Reuse bridge concepts that have proven productive
- Avoid regenerating hypotheses killed in prior sessions

It also consults `knowledge/meta-insights.md` (if it exists) to:
- Prioritize strategies and bridge types with higher survival rates
- Avoid patterns that consistently produce killed hypotheses
- Calibrate selection with quantitative metrics accumulated by the Session Analyst

---

## The Critic: 9 attack vectors

The Critic is genuinely adversarial. Its objective is to destroy weak hypotheses — killing 50–70% is normal and healthy.

1. **Novelty Kill** — WebSearch to verify whether the connection is already published
2. **Mechanism Kill** — Physical/chemical/biological plausibility: energy scales, time constants, concentrations
3. **Logic Kill** — Correlation passed off as causation, analogy confused with structural relationship, post-hoc reasoning
4. **Falsifiability Kill** — If it cannot be proven false → KILL
5. **Triviality Kill** — Would a PhD student in each field say "obviously"?
6. **Counter-Evidence Search** — Mandatory WebSearch for contradictions and failures of the proposed mechanism
7. **Groundedness Attack** — For every factual claim: is it from the literature (grounded)? from parametric knowledge (verify with web search)? pure speculation (flag)? If >50% of claims are unverifiable → significant downgrade
8. **Hallucination-as-Novelty Check** — For hypotheses with high novelty: "Does it appear new because it is genuinely unexplored, or because it is wrong in non-obvious ways?" Verifies via web search that the bridge mechanism exists independently of the hypothesis. If the novelty depends entirely on an unverifiable factual claim → the "novelty" is likely an artifact of incorrect parametric knowledge → KILL or severe downgrade
9. **Claim-Level Fact Verification** — Web search EVERY individual [GROUNDED] claim. Verifies citation specificity (author+year+journal), directionality, compartment, protein properties. Citation hallucination or fabricated protein property = automatic KILL. This attack vector addresses the most critical failure mode that emerged in early sessions: fabricated mechanistic claims that sound plausible and specific

### Minimum adversarial standard and META-CRITIQUE

A 0% kill rate is a red flag. If the Critic passes every hypothesis, it must re-examine them and ask "Am I being too generous?". A healthy kill rate is 30–50%; below 15% indicates insufficient adversarial pressure.

The system includes a full META-CRITIQUE: after all attacks, the Critic (1) calibrates its own kill rate, (2) for each SURVIVES writes the strongest reason it should have been killed, (3) verifies that it ran web search for every hypothesis. Additionally, when a mechanism is too vague, the Critic writes **critic_questions** in the state JSON, which the Orchestrator forwards to the Generator in cycle 2 — indirect bidirectional feedback.

Attack vector #8 addresses a documented risk from Si & Hashimoto (2025, "The Ideation-Execution Gap", arXiv:2506.20803): AI-generated ideas show sharp overall quality degradation after experimental testing (from 5.4 to 3.4 out of 10, vs. 4.6 to 4.0 for human ideas). Hypotheses can appear new only because they are wrong. The hallucination-as-novelty check complements Groundedness scoring (which measures overall evidential support) with a targeted check on the inverse relationship between novelty and correctness.

---

## The Ranker: 6 dimensions

| Dimension | Weight | Description |
|---|---|---|
| **Novelty** | 20% | Is the connection unexplored? (requires web search to verify) |
| **Mechanistic Specificity** | 20% | How concrete is the proposed mechanism? |
| **Cross-field Distance** | 10% | How far apart are the connected fields? |
| **Testability** | 20% | Verifiable with existing methods/data? |
| **Impact: Paradigm** | 5% | If true, how much does it change understanding? |
| **Impact: Translational** | 5% | If validated, how directly does it suggest a real-world application? |
| **Groundedness** | 20% | Are the hypothesis components supported by retrievable evidence? |

Composite = weighted average. The weights of the 6 dimensions are **canonical and immutable** — bolded in the agent definition to prevent drift between cycles.

### Cross-domain creativity bonus

After the weighted composite calculation, a **+0.5 bonus** is applied to the composite score for hypotheses that cross 2+ disciplinary boundaries (e.g., materials science → neuroscience, topology → developmental biology, information theory → genetics). The bonus compensates for the systematic penalization from bio-centric infrastructure: non-biomedical hypotheses receive structurally lower scores on Testability and Groundedness because PubMed/KEGG/STRING are bio-specific, not because the hypotheses are weaker. Individual dimension weights remain immutable; the bonus operates on the final composite.

### Impact-aware prioritization

Impact is decomposed into two sub-dimensions (total weight unchanged at 10%):
- **Paradigm impact (5%)**: How much does it change understanding if true? (opens a new field = 10)
- **Translational impact (5%)**: How directly does it suggest a real-world application? (drug target/diagnostic = 10, purely academic = 1)

Impact enters the pipeline as a **parallel signal**, never as a substitute for quality:
1. **Scout**: `impact_potential` field (1–10) per target, with check in TARGET QUALITY CHECK (at least 1 target ≥ 6)
2. **Target Evaluator**: 5th informational axis (not in composite), used as tiebreaker by the Orchestrator
3. **Orchestrator**: impact tiebreaker in Phase 0c (among candidates with equal disjointness) and Phase 0d (within the DISJOINT pool)
4. **Ranker**: Impact decomposed into paradigm + translational (scoring table with 2 sub-rows)
5. **Quality Gate**: informational annotation (application pathway, applied domain, validation horizon) — does NOT influence PASS/FAIL
6. **Session Analyst**: new impact metrics category, tracks impact-quality correlation across sessions

**Impact Potential Score (IPS)**: composite score calculated by the Orchestrator after EES:
- `IPS = scout_impact_potential × 0.4 + (convergence_signal_count / 3 × 10) × 0.6`
- Convergence signals = clinical trials + grants + patents found by the Convergence Scanner
- If the Convergence Scanner did not run: `IPS = scout_impact_potential` (fallback)
- Reported in ingest.json and session summary alongside QG composite and EES

**Disjointness-impact tension resolved**: high-impact domains (cancer, antibiotics) are often PARTIALLY_EXPLORED. Impact operates **only within the DISJOINT pool** as a tiebreaker — the disjointness hard constraint (87% vs 30% pass rate) stays intact.

### Mandatory scoring format

The Ranker MUST produce a per-dimension table for **every** hypothesis with justifications of at least 2 sentences per dimension. Thin output (lacking detailed individual scoring) is blocked by `ranker-stop-gate.py`, which enforces a minimum of 3KB for `ranked-cycle{N}.md`.

### Diversity check

After ranking, the Ranker examines the top-5 hypotheses. For each pair it evaluates: do they share the same bridge mechanism? (redundant) Do they connect the same subfields? (convergent) Do they make the same type of prediction? (monotonous) If 3+ of the top-5 are conceptually similar, the highest-ranked stays and the next dissimilar hypothesis is promoted. This mitigates the diversity saturation problem documented by Si et al. (2024, "Can LLMs Generate Novel Research Ideas?", ICLR 2025; [arXiv:2409.04109](https://arxiv.org/abs/2409.04109)). The diversity constraint also operates in the Evolver — double-layer protection.

### Elo tournament sanity check

After the linear ranking, the Ranker compares every pair of top-6 hypotheses (15 comparisons): "Which of these two would a researcher want to test first, and why?" The Elo ranking is compared against the linear ranking. Inspired by Google AI Co-Scientist, which uses Elo tournament ranking for better correlation with expert evaluations.

This is not an override: the linear ranking remains the primary output. Discrepancies are diagnostic signals — they indicate implicit dimensions captured by direct comparison but missed by the 6-dimension weighted average.

---

## Domain optimization: life sciences as primary domain

### Why life sciences

MAGELLAN is structurally optimized for cross-disciplinary discovery in the life sciences. This is not an arbitrary choice — three factors converge:

1. **Structural fragmentation** — The life sciences are the domain with the highest density of latent "missing links." Sub-disciplines like the microbiome, chronobiology, epigenetics, immunology, and neuroscience operate with largely disjoint literatures despite shared molecular mechanisms. This is exactly the terrain of Swanson's Undiscovered Public Knowledge.

2. **Available retrieval infrastructure** — PubMed (38M+ articles with structured abstracts), KEGG (metabolic and signaling pathways), STRING (protein interactions) provide structured grounding and programmatic queries. No comparable equivalent exists for theoretical physics or pure mathematics (arXiv lacks a semantic query API; INSPIRE-HEP and MathSciNet are not integrated as MCP servers).

3. **Rapid falsifiability** — Cross-disciplinary biomedical hypotheses are testable with wet-lab experiments or computational analyses on existing datasets (GEO, TCGA, UK Biobank). Hypotheses in theoretical physics or mathematics often require years of formal development before they can be evaluated.

### The three structural biases

The pipeline exhibits three non-independent biases that favor the life sciences:

| Level | Bias | Impact |
|---|---|---|
| **Retrieval** | PubMed, KEGG, STRING are all bio-specific. No equivalent MCP server for arXiv, INSPIRE-HEP, MathSciNet | Non-bio hypotheses have weaker literature context → lower Groundedness |
| **Scoring** | Testability (20%) + Groundedness (20%) + Mechanistic Specificity (20%) = **60% of weight** favors experimental sciences with structured databases | Physics/pure math hypotheses receive structurally lower scores on 3 of 6 dimensions |
| **Format** | Hypothesis template, few-shot examples (Generator, Critic, Ranker, Evolver) use molecular/pathway language | The Generator tends to formulate hypotheses in terms of biological mechanisms even when the target is cross-domain |

These biases are not defects to correct — they are natural consequences of the available infrastructure and the fact that the life sciences are the domain with the greatest latent discovery opportunity. The Ranker's 6-dimension weights remain **canonical and immutable**, but a cross-domain bonus of +0.5 partially compensates for the infrastructural bias on hypotheses that cross 2+ disciplinary boundaries (see "Cross-domain creativity bonus" above).

### Score interpretation guide

Non-bio hypothesis scores are **not directly comparable** with bio scores:

- A theoretical physics hypothesis with composite score 5.5 may be qualitatively equivalent to a biomedical hypothesis with score 7.0
- The gap is primarily in Testability (lack of public datasets for rapid validation), Groundedness (no MCP server for structured retrieval), and Mechanistic Specificity (formal vs. molecular mechanisms)
- Novelty, Cross-field Distance, and Impact (decomposed into Paradigm + Translational) are relatively domain-agnostic

Cross-domain hypotheses with a bio component (e.g., "topological defects in active matter ↔ stem cell niche organization") partially benefit from the retrieval infrastructure and receive intermediate scores.

### Future roadmap for multi-domain extension

Supporting other domains at comparable quality would require:

- **arXiv API / Semantic Scholar for physics** — MCP server for structured queries on physics and mathematics preprints
- **Simulation validation** — For theoretical physics, "testability" could include numerical simulations as an experimental proxy
- **Materials databases** — Materials Project, AFLOW for materials science hypotheses
- **Domain-adaptive weights** — Domain-specific scoring profiles (e.g., reduce Testability weight for mathematics, increase Formal Rigor)
- **Multi-domain few-shot** — Examples in the Generator/Critic/Ranker covering diverse hypothesis styles

These extensions are not currently planned. The architecture would support them without structural changes to the pipeline.

---

## Structured Relationship Map (on-the-fly KG)

Before generating hypotheses, the Generator builds an **on-the-fly parametric Knowledge Graph** for each field:
1. Lists 5–10 key relationships (X activates Y, W inhibits X, Y is analogous to V...)
2. Searches for **shared nodes** between the two fields (same molecule/structure/concept)
3. Searches for **analogous relationships** (A→B in Field A mirrors P→Q in Field C)
4. Searches for **inverse relationships** and **missing links** (a relationship in one field predicts an untested relationship in the other)

This leverages the KG concept without external KG infrastructure: the LLM IS the knowledge graph reasoner — you just need to ask it explicitly in the prompt.

---

## State management: structured JSON

The system runs on a dual track:

- **`results/{session-id}/`** — All per-session outputs: markdown (*.md) and structured data (*.json) in the same directory
- **`state/session.json`** — Slim coordination index (~3KB): phase, cycle, status, target, counters
- **`state/dispatch-log.json`** — Dispatch log with timestamps

```json
{
  "session_id": "2026-03-14-abc123",
  "mode": "scout|targeted|open|problem",
  "phase": 0,
  "cycle": 1,
  "status": "running|success|partial|degraded|failed",
  "status_reason": "...",
  "scout_targets": [...],
  "selected_target": {...},
  "literature_context": {...},
  "disjointness_status": "DISJOINT|PARTIALLY EXPLORED|WELL-EXPLORED",
  "papers_retrieved": ["results/papers/zhang2025-atg5.md", "..."],
  "hypotheses": {
    "cycle1": { "raw": [...], "critiqued": [...], "ranked": [...], "evolved": [...] },
    "cycle2": { ... }
  },
  "final": [...],
  "diversity_scores": [...],
  "metadata": {
    "start_time": "...", "model": "opus-4.6",
    "total_hypotheses_generated": 0, "kill_rate": 0,
    "fallback_used": false, "literature_unavailable": false,
    "generation_degraded": false, "web_search_failures": 0,
    "retries_needed": 0,
    "cycle_decision": null,
    "evolver_skipped": false,
    "literature_reinforcement": false
  },
  "progress": {
    "phases_completed": [{"phase": "scout", "outcome": "3 targets", "timestamp": "..."}],
    "current_phase": "generation"
  },
  "health": {
    "scout_targets_found": 3, "hypotheses_generated": 12,
    "survived_critique": 5, "passed_quality_gate": 2,
    "fallback_used": false, "retries_needed": 0,
    "web_search_failures": 0
  }
}
```

State is split into a **slim index** (`state/session.json`, ~3KB) and **per-session files** (`results/{session-id}/*.json` + `results/{session-id}/*.md`). Markdown and JSON colocate in the same per-session directory. Agents receive the data they need via dispatch prompts from the Orchestrator — they never read state files directly. This prevents state bloat and reduces agent context consumption.

Key fields:
- **`status`** / **`status_reason`**: Explicit outcome classification with justification. Eliminates silently empty outputs
- **`disjointness_status`**: Disjunction verification result from the Literature Scout. Informs the Generator about the genuine novelty of the connection
- **`papers_retrieved`**: Full-text papers retrieved, saved in `results/papers/`. The Generator reads them for mechanism-level reasoning
- **`progress`**: Timeline of completed phases with outcome and timestamp. Queryable via `/status` during execution
- **`health`**: Aggregated counters for rapid diagnostics
- **Extended `metadata`**: Tracks fallbacks, degradation, WebSearch failures, adaptive decisions (`cycle_decision`, `evolver_skipped`, `literature_reinforcement`)

### Timestamp protocol

For every phase transition, the Orchestrator executes `date -u +%Y-%m-%dT%H:%M:%SZ` via Bash before and after dispatch. Timestamps are never written from memory — always from the `date` command. This guarantees that timestamps in `progress.phases_completed` are real and verifiable.

### Kill rate

Exact formula:
- `killed` = count of "KILLED" verdicts across ALL critiqued arrays (cycle 1 + cycle 2)
- `total` = total raw hypotheses generated across all cycles
- `kill_rate = killed / total * 100`
- `attrition_rate = (total - len(final)) / total * 100`

Both values are reported in the session summary and validated by `orchestrator-stop-gate.py`.

### Dispatch log

Every Agent tool invocation is automatically logged by the `verify-dispatch.py` hook in `state/dispatch-log.json`. At session end, the orchestrator-stop-gate verifies that all required agents (scout, literature-scout, generator, critic, ranker, evolver, quality-gate) were invoked.

---

## Robustness: guard logic, hooks, session health

The pipeline must operate without human supervision. To prevent silent degradation (the pipeline blindly proceeds through every phase without checking output), robustness operates on three levels.

### 1. Guard logic in the Orchestrator

Conditional blocks after every phase that verify output. The flow is always: **verify → retry → fallback → abort**.

- **Post-Scout**: If 0 targets → retry with lower threshold → fallback to 3 hardcoded parametric targets → set `fallback_used = true`
- **Post-Generation**: If < 3 hypotheses → blocking hook forces re-execution → retry with all techniques → degrade gracefully
- **Post-Critique**: If 0 survivors → regenerate with different mechanisms and more conservative claims → re-critique → if it fails twice: session FAILED with explicit cause

### 2. Blocking hooks

Per-agent SubagentStop hooks that block (exit code 2) when output is insufficient:

- `scout-stop-gate.py`: blocks if 0 targets
- `target-evaluator-stop-gate.py`: blocks if ALL target scores < 3
- `generator-stop-gate.py`: blocks if < 3 hypotheses
- `literature-scout-stop-gate.py`: degrades to warning if MCP/web unavailable; blocks only if main output file is missing
- `ranker-stop-gate.py`: blocks if `ranked-cycle{N}.md` < 3KB (prevents thin output without detailed scoring)
- `computational-validator-stop-gate.py`: warn-only (never blocks — absence of data is not evidence of absence)
- `critic-stop-hook.py`: warn-only (the Critic can legitimately kill everything)
- `session-analyst-stop-gate.py`: warn-only (verifies that meta-insights.md was created)
- `orchestrator-stop-gate.py`: Stop hook that prevents premature pipeline termination + validates kill rate + verifies dispatch log (required agents are conditional on mode)

Additional hooks:
- `verify-dispatch.py`: PostToolUse hook on Agent tool — logs every dispatch to `state/dispatch-log.json`. The orchestrator-stop-gate verifies that all required agents were invoked
- `PostToolUseFailure`: Tracks WebSearch/WebFetch failures. After 3+ failures, the Scout switches to parametric-only mode
- `PreCompact`: Backs up state before context compaction
- `PostCompact`: Restores from backup if state is corrupted after compaction

### 3. Deliverables verification gate (v5.20)

Before writing the session summary, the Orchestrator runs a file-existence check on all required artifact pairs (JSON + markdown) in `results/{session-id}/`. If a markdown report is missing but its JSON counterpart exists, the Orchestrator re-dispatches the original agent to write the markdown. The markdown is the primary deliverable (detailed mechanisms, evidence, analysis); the JSON is thin metadata for pipeline routing. Re-dispatch, not fabrication, ensures the rich content comes from the specialized agent.

The Guard Protocol (applied after every agent dispatch) now includes artifact verification: both the phase JSON and corresponding markdown must exist. Required markdown per phase: `scout-targets.md`, `target-evaluation.md`, `raw-hypotheses-cycle{N}.md`, `critiqued-cycle{N}.md`, `ranked-cycle{N}.md`, `quality-gate.md`, `cross-model-consensus.md`.

Cross-model validation receives special handling: if the agent returns `manual_export_only`, the Orchestrator checks whether actual validation files (`validation-gpt.md`, `validation-gemini.md`) exist before marking the phase complete. If absent, `phases_completed` records `cross_model_export_only` instead of `cross_model_validation`.

`phase: "complete"` cannot be set until the verification gate passes. This was introduced after session S018, where 5 markdown reports were missing, cross-model validation was marked complete despite not finishing, and the upload script failed with a 400 due to missing files.

### 4. Session health classification

Every session terminates with an explicit status:

- **SUCCESS**: ≥2 hypotheses passed the Quality Gate with Groundedness ≥5
- **PARTIAL**: 1 hypothesis passed, or all have low Groundedness
- **DEGRADED**: Pipeline completed, 0 pass the Quality Gate (cards presented with warning)
- **FAILED**: Pipeline non-completable (0 targets, all killed, agent error)

The status is the first line of `session-summary.md`. For FAILED sessions: no hypothesis cards, only cause and suggested action.

**Data flow for final.json**: The quality-gate agent writes `quality-gate.json` with verdicts, composites, and `summary.session_status`. The Orchestrator then CREATES `final.json` by reading `quality-gate.json` from disk — never from its own context memory. This prevents corruption from context compression in long sessions (bug discovered in S015: Orchestrator reported 4 CONDITIONAL_PASS when the QG had 2 PASS + 4 CONDITIONAL_PASS). After enrichment, the Orchestrator verifies that verdicts and composites in final.json match quality-gate.json.

---

## Prompt engineering principles

Agent prompts follow 2026 best practices for frontier models. Choices are empirically motivated by official guides from Anthropic, OpenAI, and Google.

### Structure and separation

- **XML tags** (`<goal>`, `<constraints>`, `<strategies>`, `<reflection>`, `<output_format>`): Separate semantic sections unambiguously. Anthropic: "XML tags help Claude parse complex prompts unambiguously."
- **Role sentences**: A single opening sentence defining the agent's role. Focuses behavior without overhead.
- **Data-top / Task-bottom dispatch**: The Orchestrator structures dispatch prompts with context at the top and instructions at the bottom. Anthropic: "Put longform data at the top... Queries at the end can improve response quality by up to 30%."

### Language calibration

- **Reduced MUST/CRITICAL/MANDATORY density**: Opus 4.6 uses adaptive thinking — emphatic instructions cause overthinking and token waste. Normal-tone instructions produce better results. Exception: the Orchestrator's functional guardrails (anti-inlining) remain unchanged.
- **Positive framing**: Instructions framed as actions to take rather than prohibitions. "Continue autonomously between phases" instead of "Do NOT stop to ask questions."
- **WHY explanations on constraints**: Explaining the reason behind a constraint lets the model generalize correctly to edge cases. Example: "bridge concepts required — the Generator uses bridge concepts as seeds, so vague bridges produce vague hypotheses."

### Content enrichment

- **Few-shot examples**: Generator (2 examples: strong + weak), Critic (1 complete attack), Ranker (1 scoring table), Evolver (1 evolutionary operation). Both Anthropic ("3-5 examples dramatically improve accuracy") and Google ("Prompts without few-shot examples are likely less effective") recommend this. Synthetic, domain-neutral examples to avoid biasing future sessions.
- **Additional reflection loops**: RETRIEVAL QUALITY CHECK for the Literature Scout (verifies MCP completeness, paper count, gap analysis specificity) and EVOLUTION QUALITY CHECK for the Evolver (verifies genuine improvement, bridge duplication, crossover coherence).

### Model-specific tuning

- **Opus 4.6**: General instructions rather than prescriptive steps ("general instructions often produce better reasoning than prescriptive plans"). Anti-overengineering: "Select 3 targets and move on" (Scout), "Generate all 6-8 before refining" (Generator). No "Think very hard" — adaptive thinking decides autonomously.
- **Sonnet 4.6**: Explicit step sequences in the Ranker (Sonnet benefits more from scaffolding). Structured examples as format anchors.

### Prompts for external models

- **GPT-5.4** (`prompts/validation-prompt-gpt.md`): Output contract (mandatory sections per hypothesis), completeness checklist, empty-result recovery, explicit citation grounding, Plan→Retrieve→Synthesize research flow.
- **Gemini 3.1 Pro** (`prompts/validation-prompt-gemini.md`): Behavioral constraints up front, 1 complete few-shot example, context-first (hypothesis cards at top, task at bottom), strict grounding ("If you cannot write the formal mapping, do not claim one exists").

---

## Positioning in the state of the art (March 2026)

### Comparable systems

| System | Architecture | Key Innovation | Status |
|---------|-------------|-------------------|--------|
| **Google AI Co-Scientist** | 6 agents on Gemini 2.0, Elo tournament ranking | 3 experimentally validated discoveries (KIRA6/AML, hepatic fibrosis, cf-PICIs) | DOE partnership, 17 National Labs |
| **SciAgents** (MIT) | Ontologist + Scientists + Critic on KG (33K+ nodes) | Cross-disciplinary via graph path sampling | Open source |
| **Kosmos** (FutureHouse) | World model + specialized agents | 12h execution, 42K lines of code, 1500 papers | Open source |
| **AI Scientist v2** (Sakana) | Ideation + Tree Search + Paper Gen | AI paper accepted at ICLR 2025 workshop (withdrawn per pre-registered protocol); methodology published in Nature (March 2026) | Open source |
| **POPPER** (Huang et al., Stanford/Harvard, ICML 2025; [arXiv:2502.09858](https://arxiv.org/abs/2502.09858)) | Falsification-based with Type-I error control | Comparable to human scientists at 10x speed | Open source |
| **Virtual Lab** (Nature 2025) | PI agent + scientist agents | 92 nanobodies designed, 2 with improved binding | Published |
| **Aletheia** (DeepMind) | Generator-Verifier-Reviser on Gemini Deep Think | 4 Erdős problems solved, but 68.5% errors on 200 evaluable responses (from 700 attempted) | Internal |

### How MAGELLAN differentiates itself

**Unique differentiators**:
- **Autonomous target selection** (Scout): Nearly all other systems require human-defined research objectives. MAGELLAN is among the very few that autonomously decides *what to explore*
- **Formal Groundedness scoring** (20%): Not present as an explicit dimension in other systems
- **Hallucination-as-novelty check**: Explicitly addresses the documented risk from Si et al. (2025) that AI-generated novelty collapses after experimental testing
- **Dual-level diversity constraint**: In both the Ranker and the Evolver, mitigating the saturation documented by Si et al. (2024, "Can LLMs Generate Novel Research Ideas?", ICLR 2025; [arXiv:2409.04109](https://arxiv.org/abs/2409.04109))
- **Hook-based autonomy hardening**: Deterministic quality gates via SubagentStop hooks

**Known gaps relative to the state of the art**:
- **No persistent Knowledge Graph**: SciAgents demonstrates that KG path sampling across 33K+ nodes finds connections that parametric+web search alone misses. The Generator's Structured Relationship Map is a proto-KG built on the fly, but it is neither persistent nor queryable
- **Elo as diagnostic, not primary ranking**: Google AI Co-Scientist uses Elo tournament as its primary ranking method, with superior correlation to expert evaluations. MAGELLAN uses it as a diagnostic sanity check (15 pairwise comparisons among the top-6), but the primary ranking remains the 6-dimension linear composite
- **No in silico scientific simulation**: Virtual Lab and MARS run wet-lab simulations (molecular dynamics, protein folding). MAGELLAN validates computationally through API queries (KEGG, STRING, HPA, GWAS Catalog, ChEMBL, UniProt, PDB) and back-of-envelope calculations, but does not run actual scientific simulations

### Key empirical evidence

- **FrontierScience Benchmark** (OpenAI, Dec 2025): 52-point gap between structured tasks (77%) and open research (25%) — validates the need for multi-agent architectures on open-ended tasks
- **MOOSE-Chem** (Yang et al., ICLR 2025; [arXiv:2410.07076](https://arxiv.org/abs/2410.07076)): LLMs encode "latent scientific knowledge associations not yet recognized by humans" — direct validation of MAGELLAN's UPK thesis
- **TruthHypo** (Xiong et al., IJCAI 2025; [arXiv:2505.14599](https://arxiv.org/abs/2505.14599)): LLMs struggle with truthful hypothesis generation without grounding support — validates the parametric+retrieval paradigm
- **Ideation-Execution Gap** (Si & Hashimoto, 2025; [arXiv:2506.20803](https://arxiv.org/abs/2506.20803)): AI-generated ideas show sharp overall quality degradation after experimental testing (5.4→3.4); human ideas decline less (4.6→4.0). Note: the original Si et al. ICLR 2025 study found LLM ideas score *higher* on novelty during blind review (5.6 vs 4.8); it is the execution follow-up that reveals the gap

### Discoveries validated by similar AI systems

- **Google AI Co-Scientist + Gemini 2.0**: Vorinostat for hepatic fibrosis (lab-validated, published in *Advanced Science*). Bacterial gene transfer mechanism (published in *Cell*, confirmed after 10 years of human research)
- **GPT-5 + Ginkgo Bioworks**: 36,000 compositions for cell-free protein synthesis, 150,000 data points, 40% cost reduction. GPT-5 proposed novel reagents that anticipated published research inaccessible to the model
- **Aletheia (DeepMind)**: 4 open Erdős problems solved autonomously, 6/10 FirstProof challenge problems
- **FutureHouse Kosmos**: 79.4% overall accuracy, but only 57.9% on novel synthesis/interpretation claims. Caution: "often goes down rabbit holes"

The evidence shows that:
1. Multi-agent architecture is the differentiator — single LLMs fail where multi-agent succeeds
2. External validation is essential — no validated system operates without retrieval
3. The best quality comes with human-in-the-loop problem framing — which makes MAGELLAN's full autonomy a more ambitious bet

---

## Multi-model strategy

### Internal models (MAGELLAN pipeline)

| Agent | Model | Rationale |
|---|---|---|
| Scout, Target Evaluator, Generator, Critic, Quality Gate, Holdout Evaluator, Orchestrator | Claude Opus 4.6 | Deep reasoning, cross-disciplinary creativity, adversarial evaluation |
| Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator, Convergence Scanner, Dataset Evidence Miner | Claude Sonnet 4.6 | Structured, search-intensive tasks; ~30% cost reduction |

### External models (automatic cross-model validation)

| Phase | Model | API | Rationale |
|---|---|---|---|
| Empirical validation | GPT-5.4 Pro | OpenAI Responses API, `reasoning.effort: "high"`, `web_search_preview` (high), `code_interpreter` | OpenAI's most factual model (33% fewer errors vs 5.2), novelty verification grounded via web search, arithmetic verification via code, citation checking, experimental design |
| Structural analysis | Gemini 3.1 Pro | Google GenAI SDK, `thinkingLevel: HIGH`, `codeExecution`, `googleSearch` | ARC-AGI-2 leader, formal structures, mathematical mappings with computational verification, quantitative predictions, literature grounding |

Cross-model validation is **automatic**: the Cross-Model Validator generates the prompts, calls both APIs in parallel via `scripts/validate-crossmodel.mjs` with active tools (GPT: web search + code interpreter; Gemini: code execution + Google Search grounding), and produces a consensus report. GPT verifies novelty against current literature via web search and checks arithmetic via code interpreter. Gemini verifies formal mappings computationally via code execution. Requires `OPENAI_API_KEY` and/or `GEMINI_API_KEY`. If absent, generates only export files for manual validation (`/export gpt|gemini`).

### Reference benchmarks (March 2026)
- **Claude Opus 4.6** (Feb 2026): GPQA Diamond 91.3%, ARC-AGI-2 68.8%, HLE 53.1% with tools. Time horizon METR: 14h30m. Context: 200K (1M beta). Source: [Anthropic announcement](https://www.anthropic.com/news/claude-opus-4-6), [System Card](https://www.anthropic.com/claude-opus-4-6-system-card)
- **GPT-5.4 / 5.4 Pro** (March 5, 2026): ARC-AGI-2 73.3% (standard), 83.3% (Pro). SWE-bench ~80%. Context: up to 1M tokens. 33% fewer false claims vs GPT-5.2. Source: [OpenAI announcement](https://openai.com/index/introducing-gpt-5-4/)
- **Gemini 3.1 Pro** (Feb 2026): GPQA Diamond 94.3%, ARC-AGI-2 77.1%. Deep Think for mathematical structures. Source: [Google announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)

---

## Usage modes

| Command | Mode | Description |
|---|---|---|
| `/discover` | **Scout Mode (primary)** | The Scout autonomously identifies targets — zero human input |
| `/discover [A] × [C]` | Targeted | For focused exploration when testing a specific area |
| `/discover [topic]` | Open | Exploration from a single domain |
| `/discover solve: [problem]` | Problem-driven | Seeks cross-domain insight for a specific problem |
| `/discover --context "..."` | Context-enriched | Injects domain expertise into the Scout and Generator |
| `/discover --papers DOI,...` | Paper-seeded | Provides seed papers to the Literature Scout |
| `/discover --interactive` | Interactive | Pauses after the Scout for target approval |
| `/connect <key>` | Contributor | Links the CLI to a web profile for discovery attribution |
| `/validate [hypothesis]` | Deep Validation | In-depth post-discovery verification |
| `/evolve` | Evolution | Another evolutionary cycle on current hypotheses |
| `/export [gpt\|gemini\|both]` | Export | Formats for cross-model validation |
| `/status` | Status | Pipeline progress during execution |
| `/validate-holdout` | Holdout Validation | Rediscovery check against known post-cutoff discoveries |

### Philosophy of autonomy

**`/discover` with no arguments is the primary mode.** The entire project exists to answer the question: "Can an agentic AI system autonomously find real scientific connections?"

This differentiates MAGELLAN from Google AI Co-Scientist (which operates with scientist-in-the-loop) and from FutureHouse Kosmos (which receives human-defined research objectives). MAGELLAN is more ambitious: the Scout must autonomously decide *what is interesting* — a capability that Demis Hassabis believes is still 5–10 years away for AI (Lex Fridman Podcast #475, July 2025: "in the next maybe five to ten years we'll have systems capable of not only solving an important problem in science but coming up with it in the first place").

The targeted/open/problem modes exist as alternatives for testing and debugging, not as the primary use case.

### Modes for domain scientists

The `--context`, `--papers`, and `--interactive` flags are designed for scientists with domain expertise who want to **direct** discovery:

- `--context "I study ferroptosis in hepatocytes"` — The Scout uses this expertise to inform strategic target selection, without restricting itself exclusively to the indicated domain
- `--papers 10.1038/s41586-024-xxxxx` — The Literature Scout retrieves these papers first and uses them as seeds for literature exploration
- `--interactive` — After the Scout produces targets and the Target Evaluator evaluates them, the pipeline pauses and presents the results. The scientist can approve, select specific targets, or reject and redirect

This model preserves system autonomy (the Scout explores freely) while adding the ability for the expert to **guide** without **controlling**. The value of serendipity remains: the Scout might find connections the scientist would never have sought, even starting from their own domain.

### Contributor connection and attribution

The `/connect <mgln_key>` command links the CLI to the user's profile on the [MAGELLAN website](https://magellan-discover.ai). Every subsequent `/discover` session embeds the contributor key in its results. When results are published to the website, the session is automatically attributed to the contributor.

This creates a **contributor-owned discovery** model: each user spends their own Claude tokens to generate discoveries, and those discoveries are publicly theirs — with a profile, statistics, and leaderboard position.

### Discovery licensing

The software is under the **Apache License 2.0** (with a mandatory NOTICE file for attribution). Outputs (scientific hypotheses) follow **dual-track licensing** based on mode:

- **Autonomous discoveries** (pure `/discover`, no flags): **CC0 1.0** (public domain). No human creative input in target selection → copyright on AI-generated content is uncertain in most jurisdictions. CC0 is the honest choice. Voluntary citation requested, based on scientific attribution norms.

- **Guided discoveries** (`/discover A × B`, `--context`, `--papers`, `--interactive`): **CC-BY 4.0**. The user provides creative direction (field selection, domain context, paper curation, target approval), strengthening the copyright claim. Attribution is mandatory: the contributor as first author, MAGELLAN as tool.

The license is determined automatically at session initialization and tracked in `session.json` → `ingest.json` → website API payload. See `DISCOVERY_LICENSE.md` for full details.

### What makes full autonomy possible (March 2026)

1. **Scout with 10 strategies**: It does not choose randomly — it has structured heuristics (including structural isomorphism and serendipity) to identify where unlinked knowledge is most likely hiding
2. **Parallel Literature Scout**: Real-time verification that the Scout's targets are not already explored, providing literature context to enrich generation
3. **Opus 4.6 time horizon 14h30m (METR)**: Sustained autonomy at this level is a new capability — no pre-2026 model could operate coherently over these durations
4. **MCP servers**: Structured retrieval independent of generic web search, reducing fragility
5. **GPT-5.4 as external validator**: 33% fewer factual errors compared to GPT-5.2, with Deep Research for exhaustive literature grounding. Reduces the risk of Claude validating its own hallucinations
6. **Auto Mode (March 12, 2026)**: Eliminates permission interruptions, allowing the pipeline to flow without intervention
7. **JSON-based state management**: Survives context compaction, maintaining coherence over 30–60 minute runs

---

## Failure modes and mitigations

| Failure mode | Probability | Mitigation |
|---|---|---|
| Scout gravitates toward popular topics (not genuinely underexplored) | High | Strategies 7 (Swanson ABC) and 8 (Contradiction Mining) force non-obvious exploration. Literature Scout verifies targets are not already published. Discovery-log prevents re-exploration |
| Hallucination cascade (errors accumulate across agents) | Medium | Critic with mandatory web search. Groundedness scoring. Hallucination-as-novelty check. Cross-model validation with GPT-5.4 |
| Illusory novelty (appears new because it is wrong) | Medium | Critic attack vector #8. Si & Hashimoto (2025): AI overall quality drops from 5.4 to 3.4 after testing. Cross-model triangulation reduces the risk |
| Hypothesis convergence | Medium | Diversity check in the Ranker + diversity constraint in the Evolver — double layer |
| Context drift on long runs | Medium-low | State in JSON, not in conversational context. Each agent re-reads state. PreCompact/PostCompact hooks for backup/restore |
| "Trivial" hypotheses disguised as novel | Medium | Triviality Kill in the Critic. Web search novelty check. Cross-model validation |
| Rabbit holes (exploring dead ends) | Medium | Adaptive cycles: 1–3 cycles based on quality. Early complete prevents over-processing. Orchestrator has explicit instructions to proceed |
| Scout produces 0 targets | Medium | Post-Scout guard: retry with lower threshold → fallback to 3 hardcoded parametric targets |
| Generator produces < 3 hypotheses | Medium-low | Blocking SubagentStop hook (exit 2) forces re-execution. Post-Generation guard: retry with all techniques → degrade gracefully |
| Critic kills all hypotheses | Medium | Post-Critique guard: regenerate with different mechanisms and more conservative claims → re-critique. If it fails twice: session FAILED |
| Pipeline terminates prematurely | Medium-low | Stop hook blocks termination if phase ≠ "complete"/"failed". PostCompact restores state and instructs continuation |
| WebSearch/WebFetch unavailable | Low | PostToolUseFailure hook tracks failures. MCP servers as alternative channel. Scout switches to parametric-only mode after 3+ failures |
| Silently empty output | **Eliminated** | Session Health Classification: every session terminates with SUCCESS/PARTIAL/DEGRADED/FAILED. The status is the first line of session-summary.md |
| Orchestrator executes phases inline (agent bypass) | **Eliminated** | WebSearch/WebFetch removed from Orchestrator, maxTurns=200 (circuit breaker only; sub-agents have no turn limit — stop hooks validate output), anti-inlining directive, dispatch log with post-session verification |
| Thin ranked output (no detailed scoring) | **Eliminated** | `ranker-stop-gate.py` blocks output < 3KB, mandatory per-hypothesis table format |
| Literature Scout fails to save papers | **Mitigated** | `literature-scout-stop-gate.py` degrades to warning if MCP/web unavailable; blocks only if main output file is missing |
| Plan mode blocks autonomous pipeline | **Eliminated** | `/discover` calls ExitPlanMode automatically before launching the Orchestrator |
| Invalid hook schema causes silent errors | **Eliminated** | All hooks updated to current Claude Code schema (`"approve"/"block"` not `"allow"`, stdin for PostToolUse, `"verdict"` field for kill counting) |
| Orchestrator stops before Quality Gate | **Mitigated** | maxTurns=200 (circuit breaker), sub-agents have no turn limit, Context Efficiency Protocol. Stop hook (`orchestrator-stop-gate.py`) blocks premature termination. State Contract documents exact terminal values (`status: "success"`, `phase: "complete"`). Output quality is validated by stop hooks, not by turn count |
| Files from different sessions overwrite each other | **Eliminated** | Each session writes to `results/{session-id}/` |


---

## How to evaluate results

Given that the user has no domain expertise, the evaluation workflow is:

1. **MAGELLAN produces hypotheses** → `results/{session-id}/session-summary.md`
2. **Cross-model validation** → `/export gpt` and `/export gemini` → paste into GPT-5.4 Pro and Gemini Deep Think
3. **Triangulation**: If at least 2 of 3 models assign high confidence and novelty, the hypothesis is a candidate
4. **Expert review**: Candidate hypotheses are presented to domain experts (professors, researchers) for qualitative evaluation. This is the ground truth
5. **Iteration**: Expert feedback informs subsequent sessions

The goal is not for every hypothesis to be correct — it is for the system to produce a non-zero rate of genuinely novel and scientifically valid hypotheses, measured through expert review.

---

## Empirical validation

### The validation vs. effectiveness conflict

There is a fundamental tension: formally validating that MAGELLAN works would require "blinding" the system (no web search, parametric knowledge only), but maximum effectiveness requires giving it every tool. The solution: completely separate the two objectives.

### Track 1: Production pipeline enrichment

Two new post-Quality-Gate agents, NON-BLOCKING, that consult sources never used by the pipeline:

**Convergence Scanner**: Searches for independent convergence signals on ClinicalTrials.gov (active trials), NIH Reporter (funded grants), and patents. Also finds partial sub-mechanism confirmations using different queries than the Quality Gate. CONSTRAINT: must read `quality-gate.md` to avoid counting papers already found as "new evidence."

**Dataset Evidence Miner**: Verifies specific molecular claims via `scripts/query-biodata.py` against 5+ bioinformatics APIs: Human Protein Atlas (tissue expression), GWAS Catalog (genetic associations), ChEMBL (compound-target), UniProt (protein function), PDB/AlphaFold (structure). DISTINCTION from Computational Validator: CV operates on bridge concepts pre-generation; DEM operates on claims post-generation. Additionally, the DEM now produces "Suggested Computational Follow-Ups" -- specific, actionable database queries a researcher could execute to further validate hypotheses without wet-lab work (e.g., "query TCGA survival data stratified by CALD1 expression").

**Empirical Evidence Score (EES)**: A parallel score alongside the composite. `EES = dataset_score × 0.55 + convergence_score × 0.45`. It does not replace the composite — it measures a different axis (empirical evidence vs. reasoning quality).

### Track 2: Holdout Validation Framework

**The retrodiction paradox**: Quality Gate and Critic search the web with no temporal filter. If a post-cutoff paper confirms the mechanism, the QG would find it and kill the hypothesis as "not novel" — the opposite of the desired outcome. Pure retrodiction within the pipeline is problematic.

**Solution: Holdout Validation with post-hoc contamination check**:
1. Curate cross-disciplinary discoveries published after May 2025 (Claude's cutoff)
2. Give MAGELLAN only `[Field A] × [Field C]` in targeted mode
3. The pipeline runs normally (no handicap)
4. Afterward, the Holdout Evaluator checks:
   - **Contamination**: was the "answer" paper found by any agent? (grep DOI/PMID/title)
   - **Mechanism similarity**: how similar are MAGELLAN's hypotheses to the known mechanism?
5. Verdicts: GENUINE_REDISCOVERY (uncontaminated + strong match), PARTIAL_REDISCOVERY, ADJACENT_DISCOVERY, CONTAMINATED, MISSED

This is more rigorous than blinding because it preserves the pipeline's exact behavior (you are testing the REAL system), objectively measures contamination, and a GENUINE_REDISCOVERY is unassailable as proof.

### Overlap analysis (design decision)

| Source | Used by pipeline? | Used by Convergence Scanner? | Used by DEM? |
|-------|----------------------|-------------------------------|----------------|
| Web (Google) | Yes (Critic, QG, Scout, Lit) | Only for patent/grant search | No |
| PubMed MCP | Yes (Literature Scout) | Yes (partial confirmations) | No |
| STRING/KEGG | Yes (Comp. Validator, pre-gen) | No | Only NEW claims |
| ClinicalTrials.gov | **No** | **Yes** | No |
| NIH Reporter | **No** | **Yes** | No |
| Patents (Google) | **No** | **Yes** | No |
| HPA | **No** | No | **Yes** |
| GWAS Catalog | **No** | No | **Yes** |
| ChEMBL | **No** | No | **Yes** |
| UniProt | **No** | No | **Yes** |
| PDB/AlphaFold | **No** | No | **Yes** |

---

## Pipeline evolution

For the complete history of the pipeline's evolution — with motivations, evidence from session post-mortems, and estimated impact of every change — see `docs/CHANGELOG.md`.
