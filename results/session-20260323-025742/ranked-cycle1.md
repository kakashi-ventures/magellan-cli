# Ranking — Cycle 1
## Target: Cartilage Biphasic Theory x Biofilm Matrix Mechanics
## Session 011 | Date: 2026-03-23

---

## Scoring Dimensions (weight)

| Dimension | Weight | Description |
|---|---|---|
| Novelty | 15% | How new is this connection? |
| Mechanistic Specificity | 20% | Are specific molecules, equations, parameters named? |
| Testability | 20% | Is there a clear experimental protocol with predicted outcomes? |
| Groundedness | 20% | How well-supported are the factual claims? |
| Impact if True | 10% | Would this change practice or understanding? |
| Cross-domain Creativity | 15% | How distant are the fields? How surprising is the bridge? |

---

## Per-Hypothesis Scoring

### H1.2: Aggregate Modulus H_a Predicts Debridement Better Than G'/G''

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 9 | H_a never measured in biofilm. Drained vs undrained distinction never applied. |
| Mechanistic Specificity | 8 | Specific equation (H_a = Es(1-nu)/((1+nu)(1-2nu))), specific protocol, specific prediction (H_a << G') |
| Testability | 8 | Clear confined compression protocol. Falsifiable: if H_a ~ G', hypothesis fails. Debridement correlation testable. |
| Groundedness | 7 | Biphasic theory well-validated [GROUNDED]. Biofilm G' values published [GROUNDED]. Specific H_a prediction is PARAMETRIC. |
| Impact if True | 8 | Would replace G'/G'' as standard biofilm mechanical characterization. Clinical implications for debridement protocols. |
| Cross-domain Creativity | 9 | Cartilage biomechanics → biofilm microbiology. Two discipline boundaries. +0.5 bonus. |
| **Composite** | **8.25** | |

### H1.1: FCD Predicts Donnan-Mediated Cationic Antibiotic Partitioning

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 8 | FCD never measured in biofilm. Donnan partitioning for antibiotics novel. Partially explored: tobramycin-alginate binding studied. |
| Mechanistic Specificity | 8 | Specific equations (Donnan factor, partition coefficient), specific antibiotics named, specific ionic strength predictions. |
| Testability | 8 | Clear protocol: measure FCD, predict partitioning, verify. ICP-MS feasible. |
| Groundedness | 7 | Triphasic theory well-validated [GROUNDED]. Alginate chemistry known [GROUNDED]. Specific biofilm FCD is PARAMETRIC. |
| Impact if True | 6 | Limited impact at physiological ionic strength. Relevant mainly for airway/mucosal environments. |
| Cross-domain Creativity | 9 | Cartilage biophysics → biofilm pharmacology. +0.5 bonus. |
| **Composite** | **7.55** | |

### H1.8: Net FCD Transitions During Maturation with Ionic Sensitivity Reversal

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 9 | No paper predicts or measures FCD changes during biofilm maturation. Charge reversal concept is new. |
| Mechanistic Specificity | 7 | Based on documented Pel→alginate shift. Specific FCD transition predicted. Therapeutic window timing less specific. |
| Testability | 7 | Daily FCD measurement by tracer ion equilibrium. Falsifiable: if FCD doesn't transition, hypothesis fails. |
| Groundedness | 6 | Pel→alginate shift documented for CF [GROUNDED]. Net FCD zero-crossing is thermodynamically necessary [PARAMETRIC]. Therapeutic utility SPECULATIVE. |
| Impact if True | 8 | If charge reversal window is real and exploitable, major clinical implications for CF biofilm treatment timing. |
| Cross-domain Creativity | 8 | Adds temporal dimension from developmental cartilage biology to biofilm maturation. |
| **Composite** | **7.40** | |

### H1.3: Opposite Donnan Swelling for Pel vs Alginate (corrected: Ca2+ differential)

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 6 | Ca2+-alginate binding known. Pel-alginate differential response is modest extension. |
| Mechanistic Specificity | 7 | Specific EPS types named, specific mutations (pelA, pslBCD knockouts), CaCl2 concentration specified. |
| Testability | 8 | Flow cell confocal with deletion mutants. Clear predicted outcomes. |
| Groundedness | 5 | Core Donnan mechanism had sign error. Ca2+ effect better explained by existing chemistry. |
| Impact if True | 6 | Incremental advance in understanding Ca2+-biofilm interactions. |
| Cross-domain Creativity | 7 | Lower creativity score due to sign error undermining the theoretical bridge. |
| **Composite** | **6.40** | |

### H1.6: Streaming Potential Reveals Spatial FCD Heterogeneity

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 8 | Streaming potential never applied to biofilm. Spatial FCD map of biofilm doesn't exist. |
| Mechanistic Specificity | 7 | Specific technique (streaming potential), specific measurement setup, microelectrode array design. |
| Testability | 5 | Technically very challenging. Biological noise concern. May require dead biofilm (alters FCD?). |
| Groundedness | 6 | Streaming potential well-validated for cartilage [GROUNDED]. Biofilm adaptation feasibility uncertain [PARAMETRIC]. |
| Impact if True | 7 | First spatial FCD map of any biofilm. Novel measurement technique for field. |
| Cross-domain Creativity | 8 | Electrokinetic measurement transfer across fields. |
| **Composite** | **6.70** | |

### H1.4: Biphasic Creep Time Constant Predicts Convective Penetration

| Dimension | Score | Justification |
|---|---|---|
| Novelty | 7 | Poroelastic transport in biofilm not proposed. |
| Mechanistic Specificity | 6 | Equation given but parameters span 4 orders of magnitude. Derived, not standalone. |
| Testability | 5 | Requires H1.2 measurements first. Distinguishing poroelastic from convective mixing is difficult. |
| Groundedness | 5 | Core physics valid [GROUNDED]. Biofilm parameters highly uncertain [PARAMETRIC]. |
| Impact if True | 6 | Would add poroelastic term to biofilm transport models. |
| Cross-domain Creativity | 7 | Transport physics transfer. |
| **Composite** | **5.95** | |

---

## Final Rankings

| Rank | ID | Title | Composite | Key Strength |
|---|---|---|---|---|
| 1 | H1.2 | Aggregate modulus H_a from confined compression | **8.25** | Foundational measurement, replaces G'/G'' paradigm |
| 2 | H1.1 | FCD-Donnan antibiotic partitioning | **7.55** | Quantitative framework, novel FCD measurement |
| 3 | H1.8 | FCD maturation transition | **7.40** | Novel temporal dimension, thermodynamic necessity |
| 4 | H1.6 | Streaming potential spatial FCD mapping | **6.70** | Novel technique transfer, high-impact measurement |
| 5 | H1.3 | Pel vs alginate differential swelling | **6.40** | Testable with deletion mutants, but lower novelty |
| 6 | H1.4 | Creep time constant transport prediction | **5.95** | Derived prediction, high parameter uncertainty |

### Diversity Check
- Bridge types represented: biphasic mechanics (H1.2), triphasic Donnan (H1.1), temporal charge evolution (H1.8), electrokinetic measurement (H1.6), charge heterogeneity (H1.3), poroelastic transport (H1.4)
- 6 distinct bridge types across 6 surviving hypotheses — PASS (no convergence)
- No two hypotheses share the same core prediction

### Elo Tournament Sanity Check (top 4 pairwise)
- H1.2 vs H1.1: H1.2 wins (more foundational, higher impact)
- H1.2 vs H1.8: H1.2 wins (better grounded, more testable)
- H1.2 vs H1.6: H1.2 wins (more feasible, clearer predictions)
- H1.1 vs H1.8: H1.1 wins marginally (more specific predictions)
- H1.1 vs H1.6: H1.1 wins (more testable, lower technical risk)
- H1.8 vs H1.6: H1.8 wins (higher impact, lower technical barrier)

Elo ranking: H1.2 > H1.1 > H1.8 > H1.6 — **CONSISTENT with composite ranking**
