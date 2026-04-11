# OIDA × MAGELLAN: Epistemic Infrastructure for Autonomous Scientific Discovery

## Architecture Specification & Implementation Plan

**Authors:** Alberto Trivero, Federico Bottino, Carlo Ferrero
**Status:** Architecture Draft v0.1
**Date:** April 2026

---

## 1. Thesis

MAGELLAN's adversarial pipeline for hypothesis generation is procedurally epistemic: it already distinguishes hypotheses from evidence, applies structured criticism, and tracks convergence. But this epistemic structure lives in the pipeline's execution flow and evaporates between sessions. OIDA makes it computationally persistent.

The integration creates three capabilities absent from current MAGELLAN:

1. **Cross-session epistemic memory.** The knowledge graph accumulates across sessions. An unresolved question from Session 3 rises in priority by Session 15. A pattern detected across Sessions 7, 11, and 14 becomes a canonical insight.
2. **Inference optimization through epistemic filtering.** Agents receive KOs filtered by epistemic relevance, not raw context. Estimated 40-60% context reduction per agent while maintaining or improving output quality.
3. **Native adversarial infrastructure.** The Critic's work becomes persistent contradiction edges. The Dialectic Engine surfaces tensions before agents encounter them. The Surprise Engine routes incoherences to the agents best equipped to resolve them.

---

## 2. Knowledge Object Schema for Scientific Discovery

### 2.1 KOC Axis Specification (7-axis, immutable)

```
[Entity]-[Domain]-[Class]-[Epoch]-[Depth]-[Author]-[Variant]
```

**MAGELLAN-specific axis definitions:**

| Axis | Organizational (OIDA) | Scientific Discovery (MAGELLAN) | Example |
|---|---|---|---|
| **Entity** | Business entity | Research target (mechanism, pathway, phenomenon) | `thermal-proteome-evt` |
| **Domain** | Business domain | Scientific discipline pair | `stat-physics×proteomics` |
| **Class** | Epistemic class | Same 9 classes (unchanged) | `HYPOTHESIS` |
| **Epoch** | Calendar quarter | Session ID + generation cycle | `S22-C2` (Session 22, Cycle 2) |
| **Depth** | Organizational depth | Abstraction level: observation → mechanism → theory | `mechanism` |
| **Author** | Human author | Agent ID (Scout, Generator, Critic, etc.) | `generator-01` |
| **Variant** | Document version | Hypothesis evolution (original → evolved → validated) | `v3-evolved` |

### 2.2 Epistemic Class Mapping

| OIDA Class | MAGELLAN Artifact | Seed K | Decay | Half-life | Example |
|---|---|---|---|---|---|
| **QUESTION** | Scout targets, unresolved gaps | 0.30 | Inverse | Urgency grows | "Can percolation theory model immune exclusion?" |
| **HYPOTHESIS** | Generator output (pre-validation) | 0.30 | Exp. | ~120d | "GEV distributions characterize thermal proteome stability" |
| **OBSERVATION** | Literature findings, dataset evidence | 0.40 | Exp. | ~180d | "Meltome Atlas shows bimodal distribution in thermophiles" |
| **EVIDENCE** | Cross-model validated findings | 0.80 | Exp. | ~730d | "Cramer-Rao bound confirmed from first principles" |
| **EVALUATION** | QG assessments, Ranker scores, Critic attacks | 0.55 | Exp. | ~120d | "H-17 scores 7.2/10 testability, 4.1/10 mechanism" |
| **DECISION** | Methodological findings, validated conclusions | 1.00 | None | Inf | "Math constraints transfer better than analogies (84% vs 30%)" |
| **CONSTRAINT** | Physical laws, mathematical boundaries | 0.90 | None | Inf | "Second law constrains entropy-based protein stability" |
| **NARRATIVE** | Session meta-learning, field summaries | 0.70 | None | Inf | "Disjoint pairs produce higher survival rates" |
| **PLAN** | Research directions, experimental proposals | 0.65 | Exp. | ~90d | "Priority: validate percolation threshold prediction" |

### 2.3 Decay Calibration Rationale

- **HYPOTHESIS: 50d → 120d.** Scientific hypotheses require literature review, formal analysis, sometimes experimental work. Longer relevance window.
- **OBSERVATION: 90d → 180d.** Dataset findings from 6 months ago still relevant; market signals wouldn't be.
- **EVIDENCE: 365d → 730d.** Confirmed mathematical bounds don't decay like quarterly analyses.
- **QUESTION urgency: steeper.** Denominator /30 → /20, reaching high urgency ~33% faster.

### 2.4 Edge Vocabulary

12 edge types (10 from OIDA + 2 new):

| Type | Coeff. | Semantics |
|---|---|---|
| SUPPORTS | +1.0 | Evidence validates hypothesis |
| CONTRADICTS | -0.6 | Attack succeeds; evidence falsifies |
| BASED_ON | +0.8 | Hypothesis grounded in evidence/constraint |
| SUPERSEDES | +0.6 | Evolved hypothesis replaces earlier version |
| IMPLEMENTS | +0.7 | Experimental proposal operationalizes hypothesis |
| BLOCKS | -0.4 | Missing evidence blocks validation |
| REFINES | +0.5 | Hypothesis refinement without contradiction |
| ENABLES | +0.4 | Methodological finding enables new direction |
| PRECEDES | +0.3 | Temporal ordering |
| DERIVES_FROM | +0.5 | Logical derivation |
| **CONVERGES_WITH** | **+0.9** | **Independent derivations reach same conclusion** |
| **ANALOGOUS_TO** | **+0.3** | **Structural analogy across disciplines** |

---

## 3. Knowledge Regimes

| Regime | Description | Gravity Multiplier |
|---|---|---|
| **working** | Intra-session scratch | 0.0 |
| **event** | Session-bound findings (default for outputs) | 1.0 |
| **canonical** | Validated scientific knowledge | 1.6 |
| **tacit** | Emergent meta-patterns across >=5 sessions | 0.8 |

**Consolidation score for canonical promotion:**
```
C(KO) = 0.30 * cross_session_survival
      + 0.25 * independent_confirmation
      + 0.25 * relational_centrality
      + 0.20 * methodological_stability
```
Promotion threshold: C(KO) >= 0.70

---

## 4. Agent-to-rho Routing Table

| Agent | rho | Primary Need |
|---|---|---|
| Scout | 0.90 | High-urgency QUESTIONs, cross-domain surprises |
| Convergence Scanner | 0.90 | CONVERGES_WITH candidates, cross-session patterns |
| Session Analyst | 0.85 | Tacit patterns, methodological KOs |
| Critic | 0.80 | Surprise Engine output, contradictions |
| Evolver | 0.60 | Critic EVALUATIONs + surviving EVIDENCE |
| Generator | 0.55 | QUESTIONs + CONSTRAINTs + canonical methodology |
| Ranker | 0.45 | EVALUATION history + comparative EVIDENCE |
| Quality Gate | 0.35 | Rubric-relevant EVIDENCEs and EVALUATIONs |
| Cross-Model Validator | 0.25 | Target HYPOTHESEs + verification CONSTRAINTs |
| Dataset Evidence Miner | 0.20 | Specific claims to find evidence for/against |
| Orchestrator | 0.15 | Phase status, blocking QUESTIONs, pipeline state |

---

## 5. Dialectic Engine

Maps MAGELLAN's adversarial pipeline to persistent tension fields:

| Critic Attack Vector | Tension Field Type | Edge on Success |
|---|---|---|
| Logical consistency | Formal contradiction | CONTRADICTS (-0.6) |
| Empirical falsifiability | Testability gap | BLOCKS (-0.4) |
| Known counter-evidence | Evidence conflict | CONTRADICTS (-0.6) |
| Mechanism clarity | Explanatory gap | New QUESTION KO |
| Scope overclaim | Boundary violation | CONTRADICTS on CONSTRAINT |
| Redundancy | Novelty deficit | CONVERGES_WITH (negative) |
| Statistical validity | Methodological weakness | EVALUATION KO |
| Cross-domain transfer | Analogy breakdown | CONTRADICTS on ANALOGOUS_TO |
| Practical testability | Implementation barrier | BLOCKS (-0.4) |

---

## 6. Implementation

### File Structure

```
prompts/
  ko-schema.json              # KO and edge JSON schema
  epistemic-config.json        # Runtime configuration

scripts/epistemic/             # Python package
  __init__.py
  config.py                    # Constants and paths
  store.py                     # Graph storage (JSON-based CRUD)
  kge.py                       # KGE cycle runner
  ingest.py                    # Agent output → KO converter
  salience.py                  # Dual-salience computation
  dialectic.py                 # Tension field detection
  context.py                   # Agent context injection
  regime.py                    # Regime promotion lifecycle

scripts/
  kge-cycle.py                 # CLI: python3 scripts/kge-cycle.py [--converge]
  ingest-kos.py                # CLI: python3 scripts/ingest-kos.py <results-dir>
  inject-context.py            # CLI: python3 scripts/inject-context.py <agent-id>

knowledge/graph/               # Runtime KO graph storage
  kos.json                     # All KOs (created at runtime)
  edges.json                   # All edges (created at runtime)
```

### CLI Usage

```bash
# Ingest a session's results into the KO graph
python3 scripts/ingest-kos.py results/2026-04-08-autonomous-022

# Run a KGE cycle to update K-scores
python3 scripts/kge-cycle.py --converge --verbose

# Generate context briefing for an agent
python3 scripts/inject-context.py scout --tensions

# View tension report
python3 scripts/inject-context.py --dialectic

# Graph statistics
python3 scripts/kge-cycle.py --stats
```

---

## 7. Evaluation Framework

### Metrics

| Metric | Definition |
|---|---|
| Hypothesis Survival Rate | % passing QG — compare pre/post OIDA (baseline: 37.4%) |
| Token Efficiency | Tokens per surviving hypothesis |
| Cross-Session Convergence Rate | % with CONVERGES_WITH edges across sessions |
| QUESTION Resolution Rate | % high-urgency QUESTIONs addressed within N sessions |
| Critic Precision | % attacks targeting genuinely novel weaknesses |
| Canonical Promotion Rate | % event KOs reaching canonical per quarter |

### Falsification Conditions

- **F1:** Survival rate must improve >= 5 points (37.4% → >= 42.4%) within 20 sessions.
- **F2:** Token efficiency must improve >= 30%.
- **F3:** If static tag-and-boost matches full OIDA within 1 SE, dynamic KGE not justified.

---

## Appendix: Decision Log

| Decision | Rationale | Revisit Condition |
|---|---|---|
| HYPOTHESIS half-life: 120d | Scientific validation takes longer | If avg lifespan < 60d, reduce |
| QUESTION urgency /20 | Scientific questions compound faster | If urgency saturates too early, increase |
| Canonical gravity: 1.6 | Scientific canonical harder-won | If canonical KOs dominate unfairly, reduce |
| Consolidation threshold: 0.70 | Scientific canonicalization should be harder | If promotion rate < 5%/quarter, reduce |
| CONVERGES_WITH: +0.9 | Independent convergence near-maximal | If false convergences inflate K, reduce |
| ANALOGOUS_TO: +0.3 | Analogy suggestive, not deductive | If analogies underweighted, increase |
