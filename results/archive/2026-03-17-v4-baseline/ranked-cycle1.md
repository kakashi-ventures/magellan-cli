# Ranked Hypotheses — Cycle 1
## Session: 2026-03-17-scout-001

## Scoring Dimensions (weights)
1. **Novelty** (25%): Is this genuinely new? Not published?
2. **Mechanism Specificity** (20%): How concrete is the proposed mechanism?
3. **Groundedness** (20%): How much is grounded in verified literature vs parametric speculation?
4. **Testability** (15%): How actionable is the proposed test?
5. **Impact** (10%): How significant if true?
6. **Confidence** (10%): Calibrated probability of being correct

---

## H3: V-ATPase-Driven Local pH Microdomains Act as Condensate Nucleation Templates
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 9 | No prior work connecting V-ATPase to condensate nucleation |
| Mechanism Specificity | 8 | Concrete: V-ATPase -> H+ gradient -> local pH drop -> pH-dependent IDP conformational change -> condensate nucleation. Specific proteins (V-ATPase subunits), specific chemistry (proton gradients) |
| Groundedness | 7 | V-ATPase function: GROUNDED. pH-dependent condensate formation: GROUNDED (Nat Chem 2025). Connection: PARAMETRIC but well-reasoned |
| Testability | 7 | Bafilomycin A1 + condensate reporters. Feasible with current tools. pH imaging near V-ATPase sites |
| Impact | 7 | Would explain how cells organize condensates spatially, a major open question |
| Confidence | 5 | Strongest mechanistic chain of all hypotheses |
| **WEIGHTED TOTAL** | **7.35** | |

---

## H4: Bidirectional Bioelectric-Condensate Feedback Creates Morphogenetic Bistability
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 9 | Bidirectional feedback framework not proposed |
| Mechanism Specificity | 6 | Feedback concept is clear; specific molecular players for both directions identified but the integration is more conceptual |
| Groundedness | 7 | Both directions independently supported: Bhatt 2024 (condensate->Vmem), Ca2+ signaling literature (Vmem->condensate) |
| Testability | 8 | Bimodal distribution prediction is highly testable with simultaneous voltage + condensate imaging |
| Impact | 8 | Would provide a new framework for understanding morphogenetic decision-making |
| Confidence | 4 | Timescale mismatch is a real concern |
| **WEIGHTED TOTAL** | **7.15** | |

---

## H7: Circadian Bioelectric Oscillations Gate Daily Condensate Renewal, Preventing Aggregation
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 8 | Circadian-condensate link emerging; bioelectric oscillation as renewal mechanism is novel |
| Mechanism Specificity | 6 | Three-step mechanism clear but each step has uncertainties |
| Groundedness | 6 | Circadian-condensate: EMERGING (Brown & Nagel 2025). Bioelectric oscillations: PARAMETRIC. Combined: SPECULATIVE |
| Testability | 8 | FRAP measurements over circadian cycle are highly feasible and specific |
| Impact | 8 | Would connect three major fields and offer therapeutic intervention timing |
| Confidence | 4 | Builds on partially explored territory but adds novel mechanism |
| **WEIGHTED TOTAL** | **6.70** | |

---

## H1: Bioelectric Voltage Patterns Spatially Organize Condensate Landscapes via Calcium-Kinase Cascades
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 9 | Core thesis of entire investigation; never proposed |
| Mechanism Specificity | 7 | Clear chain: Vmem -> VGCCs -> Ca2+ -> CaMKII -> phosphorylation -> condensate dissolution |
| Groundedness | 5 | Each step individually grounded but the full chain is PARAMETRIC. AC field suppression of LLPS creates tension |
| Testability | 6 | Depolarization/hyperpolarization + condensate imaging feasible but many confounds |
| Impact | 9 | Most transformative if true — would identify the molecular readout of the bioelectric code |
| Confidence | 4 | Specificity concern (calcium does too many things) |
| **WEIGHTED TOTAL** | **6.70** | |

---

## H5: Bioelectric Dysregulation Drives Neurodegeneration Through Aberrant Condensate Phase Transitions
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 8 | Bioelectric aging exists; condensate angle is new |
| Mechanism Specificity | 5 | Broad mechanism; many steps between V-ATPase decline and protein aggregation |
| Groundedness | 5 | V-ATPase decline: GROUNDED. Condensate aging: GROUNDED. Link: SPECULATIVE |
| Testability | 4 | Very difficult to establish causation; requires longitudinal aging studies |
| Impact | 9 | Transformative for neurodegeneration field if true |
| Confidence | 3 | Causal direction problem is serious |
| **WEIGHTED TOTAL** | **5.75** | |

---

## H2: Gap Junction-Mediated Ion Sharing Creates Tissue-Scale Condensate Coherence Domains
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 8 | Never proposed |
| Mechanism Specificity | 5 | Gap junctions share ions; but quantitative argument for condensate threshold effects is weak |
| Groundedness | 4 | Gap junction ion sharing: GROUNDED. Condensate threshold effects from shared ions: SPECULATIVE |
| Testability | 6 | Carbenoxolone + condensate imaging feasible but off-target effects |
| Impact | 7 | Would explain tissue-scale condensate coordination |
| Confidence | 3 | Quantitative plausibility uncertain |
| **WEIGHTED TOTAL** | **5.40** | |

---

## H6: Morphogenetic Memory Is Physically Stored in Self-Sustaining Condensate-Voltage Circuits
| Dimension | Score (1-10) | Justification |
|---|---|---|
| Novelty | 9 | Highly original concept |
| Mechanism Specificity | 4 | Conceptually interesting but condensate lifetime problem is unresolved |
| Groundedness | 3 | Both components independently grounded but circuit concept is HIGHLY SPECULATIVE |
| Testability | 3 | 1,6-hexanediol test confounded; no clean experimental approach identified |
| Impact | 9 | Would be transformative for understanding biological memory |
| Confidence | 2 | Too many unsupported steps |
| **WEIGHTED TOTAL** | **4.80** | |

---

## FINAL RANKING

| Rank | Hypothesis | Weighted Score | Confidence |
|---|---|---|---|
| 1 | H3 (V-ATPase pH Nucleation) | 7.35 | 5/10 |
| 2 | H4 (Bidirectional Feedback Bistability) | 7.15 | 4/10 |
| 3 | H7 (Circadian Condensate Renewal) | 6.70 | 4/10 |
| 4 | H1 (Vmem-Ca-Kinase-Condensate) | 6.70 | 4/10 |
| 5 | H5 (Bioelectric Neurodegeneration) | 5.75 | 3/10 |
| 6 | H2 (Gap Junction Coherence) | 5.40 | 3/10 |
| 7 | H6 (Morphogenetic Memory Storage) | 4.80 | 2/10 |

## Diversity Check
- H3 and H1 share the "Vmem controls condensate formation" core mechanism but through DIFFERENT bridges (pH vs calcium-kinase). Acceptable diversity.
- H4 is conceptually distinct (feedback framework, not unidirectional).
- H7 brings circadian dimension — distinct mechanism class.
- H5 applies to disease — distinct context.
- Top 5 show good conceptual diversity. No promotion needed.
