# Ranking — Cycle 2
## Session: 2026-03-21-scout-008
## Survivors: 4 of 4 (100% survival rate)

---

## Scoring Dimensions (weighted)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Testability | 20% | Feasibility and clarity of test protocol |
| Groundedness | 20% | Claims verifiable in existing literature |
| Mechanistic Specificity | 20% | How specific and detailed is the mechanism |
| Novelty | 15% | Genuinely new connection |
| Cross-disciplinary Insight | 15% | Reveals something neither field alone would see |
| Potential Impact | 10% | Significance if confirmed |

---

## Per-Hypothesis Scoring

| Dimension (weight) | E1.1 | E1.4 | E1.3 | E1.2 |
|---|---|---|---|---|
| Testability (20%) | 9 | 8 | 6 | 6 |
| Groundedness (20%) | 8 | 8 | 6 | 6 |
| Mech. Specificity (20%) | 9 | 8 | 5 | 5 |
| Novelty (15%) | 8 | 9 | 8 | 7 |
| Cross-disc. depth (15%) | 9 | 8 | 8 | 6 |
| Impact (10%) | 8 | 8 | 7 | 5 |
| **Weighted composite** | **8.55** | **8.15** | **6.45** | **5.80** |

## Final Ranking

| Rank | Hypothesis | Composite | Critic Verdict | Δ from parent |
|---|---|---|---|---|
| **1** | **E1.1** Pourbaix-Quantified Fe-S Displacement | **8.55** | PASS | +0.65 (from H1.4 7.90) |
| **2** | **E1.4** FDX1 Kinetic Gate + Elesclomol | **8.15** | PASS | +1.00 (from H1.2 7.15) |
| **3** | **E1.3** Evolutionary Cu-Driven Co-Selection | **6.45** | CONDITIONAL_PASS | +2.20 (from H1.7 4.25) |
| 4 | E1.2 CuS Oligomer Buffering | 5.80 | CONDITIONAL_PASS | +0.00 (from H1.3 5.80) |

## Top-3 Composite Average: 7.72

## Adaptive Cycle Check

| Criterion | Value | Threshold | Decision |
|---|---|---|---|
| Top-3 average | 7.72 | ≥ 6.5 for cycle 2 completion | **PROCEED TO QUALITY GATE** |
| Evolver skip eligible | Yes | Top-3 ≥ 6.5 | Evolver skipped (cycle 2 terminal) |

**Decision: PROCEED TO QUALITY GATE** — Top-3 average (7.72) exceeds cycle 2 threshold (6.5). No further evolution cycles needed.

## Diversity Check

**PASS** — Top-3 span three distinct bridge types:
1. **E1.1**: Thermodynamic displacement embedded in Eh-pH speciation space (bioinorganic + geochemistry)
2. **E1.4**: Kinetic gatekeeper with elesclomol speciation and predict-then-measure protocol (enzymology + geochemistry)
3. **E1.3**: Evolutionary co-selection driven by Cu-Fe displacement chemistry (genomics + geochemistry)

No convergence — though E1.1 and E1.4 share Pourbaix framework, their core mechanisms differ (displacement thermodynamics vs kinetic gating). Different experimental approaches (ferrozine/XANES vs mutant library/ITC vs phylogenomics/ancestral reconstruction).

## Elo Tournament Sanity Check

| Matchup | Winner | Reason |
|---|---|---|
| E1.1 vs E1.4 | E1.1 | CIA/LIAS test is more decisive than mutant library |
| E1.1 vs E1.3 | E1.1 | Established biology vs evolutionary speculation |
| E1.1 vs E1.2 | E1.1 | Clear groundedness advantage |
| E1.4 vs E1.3 | E1.4 | Quantitative predictions + verified claims |
| E1.4 vs E1.2 | E1.4 | Eliminated all confounds vs new chicken-and-egg |
| E1.3 vs E1.2 | E1.3 | Tractable genomics vs transient oligomers |

**Elo ranking: E1.1 > E1.4 > E1.3 > E1.2**
**Concordance: PERFECT** — matches linear composite.

## Improvement Summary

Evolution improved the hypothesis set substantially:
- **E1.1** (8.55): Best-in-session. Crossover of two top-3 hypotheses created genuinely synergistic model.
- **E1.4** (8.15): All three cycle 1 confounds eliminated. Elesclomol speciation is a real mechanistic addition.
- **E1.3** (6.45): Largest improvement (+2.20). Tractable genomics replaces infeasible protocells.
- **E1.2** (5.80): No improvement. Chicken-and-egg problem is a new weakness introduced by the mutation.

Session 008 top-3 average improved from 6.95 (cycle 1) to 7.72 (cycle 2): **+0.77 points**.
