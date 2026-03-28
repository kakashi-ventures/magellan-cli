# Session Analysis: 2026-03-28-scout-014 (S018)

**Target**: Non-equilibrium statistical mechanics (Mpemba effect spectral theory) × Neurodegenerative protein biochemistry (amyloid aggregation selectivity)
**Strategy**: anomaly_hunting (exploration slot — 0 prior primary sessions)
**Disjointness**: DISJOINT (score 0.95, confirmed by PubMed 0 cross-field papers)
**Date**: 2026-03-28

---

## Pipeline Metrics

| Metric | Value |
|---|---|
| Total hypotheses generated | 15 (7 cycle 1, 8 cycle 2) |
| Killed in critique | 3 (20% kill rate) |
| Survived critique | 12 |
| Entered Quality Gate | 3 |
| QG PASS | 0 |
| QG CONDITIONAL_PASS | 3 |
| QG FAIL | 0 |
| Mean QG composite | 6.97 |
| Evolver (cycle 2) | SKIPPED (top-3 >= 6.5) |
| Session health | **PARTIAL** |

---

## This Session's Patterns

### The single-molecule / multi-molecule amyloid gap: session's defining architectural challenge

Every hypothesis in this session attempted to bridge single-molecule MSM properties (Mpemba index, spectral gap, eigenmode branching) to multi-molecule amyloid aggregation kinetics (nucleation, fibril growth). This is structurally difficult because:
- Real amyloid proliferation is dominated by **secondary nucleation** (Cohen et al. 2012 PNAS 109:9761), a multi-molecule surface-templated process invisible to monomer conformational dynamics.
- MSMs describe intramolecular conformational transitions; nucleation lag time is determined by intermolecular collision rates.

**All 3 QG survivors received CONDITIONAL_PASS partly because they did not fully resolve this gap.** C2-H4 (cycle 2 raw) was the only hypothesis to attempt a direct quantitative bridge (k_n <= C × pi_competent × gamma), but it was not sent to QG (ranked 4th, NOT_RECOMMENDED_FOR_EVOLUTION). This gap is the session's single biggest open problem.

**Lesson**: For physics × amyloid bridges, the single-molecule → multi-molecule translation requires an explicit mechanistic step. The most defensible framing is an **upper bound on a rate constant** (C2-H4 approach) rather than a direct kinetic prediction. Future sessions on this target should prioritize this bridging step.

### Citation hallucination persists and shifts form

Cycle 1 had 5 citation errors (3 misattributions: Rosenman year/venue, Robustelli paper type, Eschmann journal). The Evolver corrected these in cycle 2. But cycle 2 introduced a new error: **Avanzini et al. 2026 PRX 16:011065** — the journal and year are correct (PRX, 2026), but "Avanzini" is fabricated. The actual authors are Summer, Moroder, Bettmann, Turkeshi, Marvian, and Goold. This is a new failure mode: **partial hallucination** where the venue is grounded but the author attribution is confabulated.

This is the 4th session (after S004, S013, S017) showing systematic citation attribution errors. The pattern now spans: fabricated citations (S004), wrong journal (S013), wrong main conclusion (S014), and now correct venue / wrong first author (S018). Each round of correction shifts the hallucination to a new axis.

**New Generator rule needed (Rule 38)**: When citing papers from preprint or newly-published sources (arXiv, recent PRX), verify the FIRST AUTHOR NAME independently. The venue and year may be remembered correctly while the author is confabulated. Check the full author list, not just the journal.

### Non-normal dynamics: mechanism impossible by construction

H3 (cycle 1) was the most instructive kill: it proposed Henrici non-normality measure for standard protein MSMs, but standard MSM construction **enforces detailed balance → symmetric transition matrix → normal matrix → delta(Q) = 0 by construction**. The very tool being applied eliminates the phenomenon being studied. This is a new kill class: **mechanism impossible by mathematical construction of the tool**.

The Evolver correctly diagnosed this in E4-H3: non-normality becomes accessible when detailed balance is **genuinely broken** (Hsp70 ATPase cycling creates irreversible directed transitions). This is the productive rescue: specify the non-equilibrium cellular condition that breaks detailed balance, then the non-symmetrized MSM estimator (dtram/MBAR) reveals the non-normality.

**New Generator rule needed (Rule 39)**: Before proposing a mathematical property (non-normality, non-positive-definiteness, non-stationarity) that requires violating a symmetry, verify that the mathematical tool being used does NOT impose that symmetry by construction. Detailed-balance enforcement in standard MSMs is one confirmed instance; similar constraints exist in equilibrium statistical mechanics, reversible chemical kinetics, and symmetric tensor analysis.

### Evolver pivot: PrP → insulin/beta-2-microglobulin

H7 (prion strain selection) was killed in cycle 1 (critiqued as KILLED: PrP MSM infeasible, cellular cofactors dominate, 80°C denatures PrP). The Evolver correctly pivoted to **insulin at pH 2** and **beta-2-microglobulin at pH 2.5** — systems with existing trajectory data, tractable MSM construction, and experimentally accessible misfolding. The cycle 2 evolved version (C2-H3, Insulin fibril polymorph) earned CONDITIONAL_PASS (QG composite 7.0) with 0 citation errors.

This is a textbook evolution: system pivot from infeasible to tractable, preserving the core mechanism (eigenmode branching → polymorph selection) while switching to a compatible model system.

---

## Strategy Performance: anomaly_hunting (First Primary Session)

| Metric | Value |
|---|---|
| Prior primary sessions | 0 (exploration slot) |
| Targets evaluated | 1 |
| Target disjointness | 0.95 (DISJOINT confirmed) |
| Hypotheses generated | 15 |
| Kill rate | 20% |
| QG survivors (COND) | 3 |
| QG survivors (PASS) | 0 |
| Avg QG composite | 6.97 |
| Session health | PARTIAL |

**First data point for anomaly_hunting.** The strategy delivers on novelty: zero pre-existing literature bridging Mpemba physics with protein amyloid (0 PubMed, 0 Semantic Scholar cross-field hits confirmed). However, PARTIAL health (no outright PASS) limits the strategy's debut performance.

**Comparison baseline**: S009 (Swanson_ABC_bridging debut) also achieved 0 PASS, 3 COND in its first primary session. Both untested strategies produced CONDITIONAL_PASS ceilings on debut. anomaly_hunting scored higher mean composite (6.97 vs 5.87 for Swanson_ABC).

**Assessment**: anomaly_hunting is VIABLE but requires a second primary session for reliable performance estimation. The strategy's defining feature — identifying underexplored anomalies where established formalisms from Field A have never been applied to Field C — produced exactly the expected result: high novelty, zero prior art, theoretically coherent bridge. The PARTIAL health reflects the bridging difficulty (single-molecule → multi-molecule amyloid gap), not a strategy failure.

---

## Creativity Assessment (QG-Passing Hypotheses)

| Hypothesis | Disciplinary Distance (0-3) | Abstraction Level (1-3) | Novelty Type (1-4) |
|---|---|---|---|
| C2-H2: Bimodal eigenspectrum via Zwanzig-Kramers bridge | 2.5 | 2 | 3 |
| C2-H3: Fibril polymorph selection via eigenmode branching (insulin) | 2.5 | 2 | 3 |
| C2-H1: A* state = Protein Mpemba overlap coefficient (resource-theoretic) | 3.0 | 3 | 4 |

**Session averages**: Distance **2.7 / 3.0**, Abstraction **2.3 / 3.0**, Novelty Type **3.3 / 4.0**

This is the **highest creativity session in the pipeline** for disciplinary distance:
- C2-H1 crosses 3 disciplinary boundaries (statistical physics × quantum information theory × protein biochemistry) — matching S017's record (3.0)
- C2-H2 crosses condensed matter physics (Zwanzig roughness) + Markov spectral mathematics + protein biophysics + amyloid biochemistry
- C2-H3 crosses non-equilibrium stat mech (Mpemba) + soft matter/materials science + protein biophysics

The session ties S017 (EVT × Proteome Thermal Stability) as the highest-distance autonomous session in pipeline history.

---

## Kill Pattern Analysis (This Session)

| Kill | Root Cause | Severity |
|---|---|---|
| C2-H6 (IU1 mechanism backwards) | Mechanism fabrication / logical inversion | Known class |
| C2-H7 (3-6 order timescale mismatch) | Kinetic incompatibility | Known class (S016 kill 10) |
| C2-H8 (10^9 bound gap) | Quantitative impossibility | Known class |
| H3 (cycle 1, not counted in rate) | Mechanism impossible by mathematical construction | **NEW KILL CLASS** |
| H7 (cycle 1, not counted in rate) | System computationally infeasible | Known class |

**New kill class confirmed**: "Mechanism impossible by mathematical construction of the tool." Standard MSMs enforce detailed balance → normal matrices → Henrici delta = 0. Any hypothesis requiring non-normality in standard protein MSMs fails immediately. The pre-check: verify the proposed mathematical property is not eliminated by the symmetry constraints of the standard tool.

---

## New Insights from This Session

1. **anomaly_hunting produces high novelty, PARTIAL health on debut**: Strategy finds genuinely unexplored territory (0 cross-field papers), but the bridging difficulty between single-molecule spectral theory and multi-molecule aggregation kinetics constrains QG performance to CONDITIONAL_PASS ceiling. Second primary session needed.

2. **Mpemba × amyloid is a viable long-run target**: Three CONDITIONAL_PASS hypotheses, high creativity, zero prior literature. The bridge is architecturally sound (both use Markov chain formalism). The remaining weakness (monomer → aggregation kinetics translation) is addressable with the KCV framework (C2-H4 approach). This target should re-enter the deferred queue as a "bridge revision" candidate.

3. **New kill type: mechanism impossible by mathematical construction**: Standard MSM tools eliminate non-normality by detailed-balance enforcement. This kill class will recur whenever a hypothesis requires a property (non-normality, irreversibility, asymmetry) that the standard mathematical tool eliminates by design. Add to pre-generation checklist.

4. **Partial citation hallucination (correct venue, wrong first author)**: A new failure mode. Venue and year are remembered but first author is confabulated. Requires explicit author-verification step for recently published/preprint sources.

5. **Evolver system pivot is the critical evolution operation**: When the original system is computationally infeasible (PrP MSM), pivot to a tractable model system preserving the core mechanism. Insulin at pH 2 is a model amyloid system with existing trajectory data — a productive substrate for eigenmode branching hypotheses.

6. **anomaly_hunting exploration slot data**: This session provides the first performance data for anomaly_hunting. Add to strategy rotation with PARTIAL-health flag. Recommend a second primary session pairing anomaly_hunting with a target where the single-molecule → multi-molecule translation gap is explicit in the literature.
