# MAGELLAN Meta-Insights (Cumulative)
Updated: 2026-03-28 after Session 018 (2026-03-28-scout-014)
Based on 18 sessions (~2 cycles for S016, S018), ~252 hypotheses generated, ~92 passed Quality Gate (PASS+COND)

---

## Strategy Performance (all sessions)

| Strategy | Sessions (primary) | Targets produced | Hyps generated | Survived critique | Passed QG (PASS+COND) | QG pass rate | Avg QG composite |
|---|---|---|---|---|---|---|---|
| network_gap_analysis | 006, 007, 008 | 3 | 41 | 25 | 16 | 39% | 6.92 |
| **tool_repurposing** | **010, 013** | **2** | **24** | **18** | **2 PASS (S010) + 3 PASS+1 COND (S013)** | **33% (S010), 100% (S013), ~67% combined** | **S010: 6.23, S013: 8.31, combined: 7.27** |
| scale_bridging | 005 | 1 | 14 | 8 | 4 | 29% | 6.75 |
| implicit_disjoint (sessions 001-002) | 001, 002 | 2 | ~20 | ~7 | ~7 | ~35% | ~7.0 |
| recent_breakthrough_radiation | 004 | 1 | 15 | 5 | 2 | 13% | ~6.0 |
| Swanson_ABC_bridging | 009 (primary) | 1 | 10 | 10 | 0 PASS, 3 COND | 0% PASS, 30% COND | 5.87 |
| **structural_isomorphism** | **011 (primary)** | **2** | **8** | **6** | **2 PASS, 2 COND** | **25% PASS, 50% PASS+COND** | **7.28** |
| **contradiction_mining** | **012 (primary)**, 006 (secondary), 009 (secondary) | **1** | **14** | **11** | **0 PASS, 5 COND** | **0% PASS, 35.7% COND** | **6.7** |
| **converging_vocabularies** | **014, 017 (primary)** | **2** | **22** | **15** | **014: 1 PASS, 6 COND; 017: 1 PASS, 2 COND** | **S014: 87.5%; S017: 75%** | **S014: 6.81; S017: 7.87** |
| **anomaly_hunting** | **018 (primary)** | **1** | **15** | **12** | **0 PASS, 3 COND** | **S018: QG entering 3, 100% PASS+COND; 0% PASS** | **S018: 6.97** |
| evolutionary_conservation_gap | 006 (secondary) | — | — | — | — | — | — |
| dimensional_mismatch | 006 (secondary) | — | — | — | — | — | — |
| **targeted_user_specified** | **015, 016** | **— (user-set)** | **~12 (est. S015) + 7 (S016 C1) + 7 (S016 C2) = ~26** | **~12 + 5 + 5 = ~22** | **S015: 3 PASS; S016 C1: 2 PASS + 1 COND; S016 C2: 3 PASS + 2 COND** | **S015: 100% (3/3); S016 C1: 100% (3/3); S016 C2: 100% (5/5)** | **S015: ~7.5 est; S016 C1: 7.50; S016 C2: 7.10 (mean of 3 PASS + 2 COND: 7.5/7.5/7.0/6.0/5.5)** |

**Session 013 tool_repurposing Performance Update**: Second primary test produced **EXCEPTIONAL** results. 3 PASS + 1 COND from 4 entering hypotheses (75% PASS, 100% PASS+COND). Mean composite 8.31 — highest of any session. Key differentiator vs S010: source tool (cryo-EM structural biology) and target domain (bacterial biology) share the same specimen type (biological, aqueous). S010's geochemistry-to-pharmacology transfer required biological constraint verification that introduced kill risk.

**New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing achieves dramatically better results when source (Field A) and target (Field C) share the same specimen class (e.g., both biological/aqueous, both materials/solid-state). Cross-class transfers (materials to biology, chemistry to biology) require additional domain-specific constraint verification.

**Session 014 converging_vocabularies Performance**: First primary test produced **87.5% PASS+COND rate** (7/8 entering QG — highest raw PASS+COND rate of any session). 1 PASS + 6 COND, mean composite 6.81. Strategy: select field pairs where both fields independently developed the same mathematical vocabulary (stochastic thermodynamics TUR ↔ bacterial adder model CV statistics). Apply Field A's mathematical constraints directly to Field C's observables without analogical translation. The 7 survivors (highest absolute count in any session) show that vocabulary overlap enables dense hypothesis generation from a single bridge concept.

**New heuristic (S014): "Physical law as bridge > physical model as bridge"** — converging_vocabularies works best when Field A contributes an inequality or conservation law (TUR, Poincare-Hopf, Landauer bound), not merely a predictive model. Laws cannot be violated; their application to Field C produces unfalsifiable lower bounds. The biological hypothesis tests whether the system approaches or saturates the bound. This eliminates the "is the analogy valid?" kill vector present in structural_isomorphism and tool_repurposing.

**Sessions 015-016 targeted_user_specified Note**: Targeted mode (user-specified target, no Scout) is not in the 10-strategy rotation. It cannot be ranked against Scout strategies for exploration quality, but it CAN be evaluated for QG survival rate. S015 and S016 both targeted Mechanobiology x Epigenomics and both achieved 100% QG pass+cond from hypotheses entering QG in both cycles. The explanation is field-specific (ECM stiffness + H3K27ac = 1 paper = near-DISJOINT specific bridge), not a property of targeted mode in general. S016 Cycle 2 (5/5 pass+cond) was run in BLIND mode, confirming the holdout validation architecture produces high-quality output without web retrieval during generation. After two consecutive targeted sessions, the autonomous Scout MUST return to the deferred queue.

**S016 Cycle 2 Performance Detail**: 7 hypotheses generated, 29% kill rate, 5 advancing to QG. QG results: C2-H6 (7.5 PASS), E1-H3 (7.5 PASS), E1-H4 (7.0 PASS), E1-H5 (6.0 COND), C2-H7 (5.5 COND). Zero citation hallucinations. Evolver correctly skipped (top-3 composites 7.4/7.2/7.1 all ≥ 6.5). Highest-novelty hypothesis in the session (C2-H6 novelty=9) produced by `negation_exploration` technique — the first time this technique yielded a top-ranking result. First appearance of eraser-depletion mechanism in MAGELLAN history.

**Recommendation for Scout**:
1. `network_gap_analysis` remains the highest-performing measured strategy (39% QG pass rate, 3 sessions). Use as reliable baseline.
2. **`tool_repurposing` UPGRADED to high-performance strategy** (S013: 100% PASS+COND rate, avg 8.31). When source and target share specimen class, prioritize targets where the tool is mature in Field A and the measurement need is explicitly identified in Field C literature. Add to top rotation.
3. **`converging_vocabularies` NEW HIGH-POTENTIAL strategy** (S014: 87.5% PASS+COND rate, 7 survivors). Search for field pairs where BOTH fields use the same mathematical objects (same equations, same dimensionless ratios, same inequality forms). Physics x biology pairs are prime candidates. Prioritize cases where Field A has proven mathematical inequalities (bounds, conservation laws) that MUST hold for any system of Field C's type.
4. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND rate). Regular rotation. Prioritize deep mathematical isomorphism (same PDEs independently derived).
5. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND rate). Regular rotation. Produces high-quality targets (score 8.0). Framework and measurement hypotheses outperform molecule-specific hypotheses when binding affinity is weak.
6. `Swanson_ABC_bridging` — first data confounded by PARTIALLY_EXPLORED. Re-test with verified DISJOINT target. Add B-term-in-Field-C literature check before disjointness assignment.
7. `recent_breakthrough_radiation` has lowest QG pass rate (13%) — use only when technique is genuinely new and biological target needs measurement tools.
8. **New heuristic (S011): "Measurement transfer > model transfer"** — hypotheses introducing new measurements into Field C outperform those transferring predictive models. Measurements are independently verifiable; models require parameter data first.
9. **New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing works best within the life sciences. Cross-domain transfers (materials/geochemistry to biology) require extra domain compatibility verification.
10. **New heuristic (S014): "Physical law as bridge > physical model as bridge"** — inequalities and conservation laws are stronger bridges than predictive models. For converging_vocabularies, identify the mathematical law in Field A (TUR inequality, Poincare-Hopf theorem, Landauer bound) and check if Field C systems must satisfy it.
**New heuristic (S017): "Universality theorem as bridge = strongest converging_vocabularies configuration"** — FTG theorem guarantees GEV convergence regardless of underlying distribution shape. This creates unfalsifiable-direction predictions (the Tm distribution MUST have a GEV tail) while leaving the shape parameter (xi) as the testable biological variable. The same architecture made TUR work in S014. When using converging_vocabularies, search for universality theorems in Field A (CLT, FTG, ergodicity, conservation laws) that apply to Field C data by mathematical necessity. Template: [universality theorem] guarantees [form] → [Field C parameter] is the testable biological/physical variable.
**New heuristic (S017): "Statistics x life sciences is a high-distance, high-yield pairing"** — S017 is the first session applying formal mathematical statistics at theorem level (not just regression) to biology. Disciplinary distance 3.0 (maximum). Formal statistics (EVT, extreme value theory, stochastic processes, information theory, topological data analysis) are largely underexplored bridges to life science domains. Scout should systematically consider adding one statistics-as-Field-A target per 3 autonomous sessions.

**Session 018 anomaly_hunting Performance (First Primary Session) — FINAL**: anomaly_hunting debut produced **1 PASS, 5 COND, 2 FAIL** from 8 evaluated at QG (mean composite 6.97, QG PASS+COND rate 75%). 15 hypotheses generated, 20% kill rate in critique. Session health PARTIAL. Target: Mpemba spectral relaxation theory × amyloid aggregation selectivity (disjointness 0.95). Zero pre-existing literature bridge confirmed. **PARTIAL health reflects the single-molecule MSM → multi-molecule amyloid kinetics gap**, not a strategy failure. MSMs describe intramolecular conformational transitions; real amyloid proliferation is dominated by secondary nucleation (multi-molecule surface-templated, Cohen 2013) — invisible to monomer eigenspectra. Evolver pivot from PrP (infeasible) to insulin (tractable) produced the sole PASS (C2-H7, 7.5). The 2 FAILs were citation fabrication (Avanzini confabulation persisting across cycles) and anatomy error (T217 outside K18 fragment). Comparison: best strategy debut by QG mean composite (6.97 vs 6.81 for converging_vocabularies S014, 5.87 for Swanson_ABC S009). Second primary session needed for reliable performance ranking.

**New heuristic (S018): "anomaly_hunting targets need explicit single→multi-molecule translation"** — anomaly_hunting's core mechanism is importing a formalism from a physics anomaly (Mpemba effect spectral theory) into biology. When the physics formalism operates at single-molecule level and the biology operates at population level (amyloid nucleation, gene expression), provide a quantitative bridge (upper bound on rate constant, flux inequality) as the explicit monomer-to-population translation. Without this, all hypotheses share a structural weakness that caps them at CONDITIONAL_PASS. Template: "By [single-molecule property X], the rate constant k satisfies k ≤ C × [MSM spectral quantity]. This bound is tight when [physical condition]; loose when [multi-molecule process dominates]."

**New heuristic (S018): "System feasibility pivot is the highest-value Evolver operation for Mpemba-class targets"** — When anomaly physics is applied to a computationally infeasible model system (PrP MSM requiring alpha→beta transition, IDP MSM requiring 500us trajectories), the highest-value Evolver operation is system replacement (PrP → insulin), not mechanism refinement. Insulin at pH 2 shares the key mechanistic property (fibril polymorphism, multiple conformational basins) while having existing trajectory data and tractable MSM construction timelines. Rescue template: "Replace [infeasible system] with [tractable system] sharing [key property]. Justify shared property: both exhibit [mechanism X]."

**New heuristic (S018): "For physics anomaly bridges, prefer anomalies that operate at population scale"** — The monomer-to-population translation burden is the dominant structural weakness for all Mpemba × aggregation hypotheses. For future anomaly_hunting sessions, prefer physics anomalies that natively operate at population/ensemble scale: stochastic resonance (population-level noise enhancement), noise-induced phase transitions (ensemble behavior), self-organized criticality (collective dynamics). These avoid the single→multi-molecule gap. Alternatively, pair the Mpemba formalism with biology that natively operates at the monomer level: enzyme kinetics (single-turnover), single-cell gene expression bursting, receptor-ligand binding kinetics.

---

## Disjointness vs Outcome (all sessions)

| Disjointness | Sessions | Targets selected | Hyps survived | QG passed (PASS only) | QG CONDITIONAL | QG pass + cond rate | PASS rate |
|---|---|---|---|---|---|---|---|
| DISJOINT | 001, 002, 004, 005, 006, 007, 008, 010, 013, **014**, **017**, **018** | **13** | ~89 | ~49 PASS or COND | majority are PASS | ~85% combined | ~33-38% PASS |
| PARTIALLY_EXPLORED (traditional) | 009 | 1 | 10 | 0 PASS | 3 COND | 30% COND only | 0% PASS |
| **PARTIALLY_EXPLORED (newly opened — < 6 months since landmark)** | **015, 016** | **2** | **~17 (C1) + 5 (S016 C2) = ~22** | **3 PASS (S015) + 2 PASS (S016 C1) + 3 PASS (S016 C2)** | **0 (S015) + 1 (S016 C1) + 2 COND (S016 C2)** | **100% (all three batches entering QG)** | **S015: 100%; S016 C1: 100%; S016 C2: 100%** |

**Session 013 confirms DISJOINT advantage**: DISJOINT target (score 9) with tool_repurposing produced 3 PASS + 1 COND — the best single-session PASS count in pipeline history.

**Session 014 confirms DISJOINT advantage**: DISJOINT target (score 8.5, confidence 0.96) with converging_vocabularies produced 1 PASS + 6 COND — highest absolute survivor count in pipeline history (7). PubMed verification: 0 papers bridging TUR and adder model.

**Sessions 015-016: PARTIALLY_EXPLORED (newly opened) rivals DISJOINT**: S015 (3 PASS from 3 entering QG) and S016 (2 PASS + 1 COND from 3 entering QG) both achieved 100% QG pass+cond rate. The key variable is NOT field-level overlap but BRIDGE-LEVEL novelty. ECM stiffness + H3K27ac genome-wide = 1 PubMed paper — this is effectively a DISJOINT bridge embedded in a PARTIALLY_EXPLORED field pair.

**Critical nuance (S015-S016)**: PARTIALLY_EXPLORED does NOT equal PARTIALLY_QUALITY when the specific bridge is unstudied. The correct analysis is two-level: (1) Are the fields broadly overlapping? (2) Is the SPECIFIC BRIDGE (particular measurement, particular mechanism) unstudied? If (1) is YES but (2) is NO, treat the target as functionally DISJOINT for hypothesis generation.

**Recommendation for Scout**:
- DISJOINT preference is **STRONGLY CONFIRMED** across 11 sessions. Never select a PARTIALLY_EXPLORED target when DISJOINT alternatives exist.
- **NEW (S015-S016)**: PARTIALLY_EXPLORED is acceptable when: (a) a landmark paper defined the field < 6 months ago (NEWLY_OPENED), OR (b) the specific bridge query (Field A entity + Field C measurement) returns <= 2 PubMed papers. When either condition holds, classify as NEWLY_OPENED_PARTIALLY_EXPLORED and proceed.
- S013's DISJOINT score of 9 and S014's 0.96 confidence both produced exceptional results. Continue building DISJOINT deferred target queue.
- The Literature Scout's explicit disjointness verification step is critical — PubMed zero-hit confirmation is the strongest signal.

---

## Bridge Type Performance (all sessions)

| Bridge Type | Sessions | Used | QG Passed | QG Score Range | Notes |
|---|---|---|---|---|---|
| Published unmeasured variable (gap paper) | 007 | 1 | 1 PASS | 8/10 | Highest quality — gap explicitly stated. Pre-grounded. |
| Thermodynamic displacement (Ksp/Irving-Williams) | 008 | 1 | 1 PASS | 8.1/10 | 29-order Ksp driving force. Quantitative irrefutable. |
| Mathematical topology constraints | 002 | 3 | 3 | ~8/10 | Poincare-Hopf gives necessary predictions. |
| **Computational/analytical tool transfer (life sciences) (NEW — S013)** | **013** | **4** | **3 PASS, 1 COND** | **8.15-8.55** | **GMM, power analysis, difference mapping, ML template matching. Highest avg score of any bridge type.** |
| **Physical law constraint (TUR inequality) (NEW — S014)** | **014** | **7** | **1 PASS, 6 COND** | **5.2-8.3** | **TUR inequality as hard CV lower bound. Cannot be violated. Best hypothesis (C2-H5): 7.90 composite. Full PASS+COND rate 100% for this bridge type.** |
| **Nuclear architecture spatial selectivity filter (LAD compartmentalization) (NEW — S016)** | **016** | **1** | **1 PASS** | **8.5/10** | **Three-tier lamin A/C-mediated LAD filter: cLAD (permanent barrier), fLAD (stiffness-modulated), non-LAD (accessible). OR >= 4.0 prediction vs H3K4me1 null model. CRISPR tethering causal test. Spatial genomic architecture as mechanosensing filter.** |
| **Sequential enzymatic temporal gate (NEW — S015/016)** | **015, 016** | **2** | **2 PASS** | **7.5-7.8/10** | **Two-phase model where temporal GAP between enzyme arrivals is the falsifiable prediction. Biochemically forced by enzymatic epistasis (demethylation precedes acetylation because H3K27me3/H3K27ac are mutually exclusive). Avg QG score ~7.6.** |
| **Kinetically gated epigenetic memory via BRD4 scaffolding (NEW — S016)** | **016** | **1** | **1 COND** | **6.5/10** | **BRD4 scaffold retains EP300 at super-enhancers post-YAP exit. dBET6 vs JQ1 differential as discriminating prediction. Kinetic rate model (k_write vs k_erase). Retention framing more defensible than de novo recruitment.** |
| Multi-pathway convergence on single HAT hub (EP300) | 015 | 5 | 3 PASS | 7.50-7.85 | Hub identified by STRING. Five parallel mechanosensory pathways to EP300 = five non-redundant hypotheses. |
| Geochemical tool transfer | 010 | 3 | 1 PASS, 2 FAIL | 6.23 avg | TST rate law, PHREEQC modeling. Requires biological constraint verification. |
| Indirect enzymatic cascade (multi-step) | 001, 006 | 8+ | 6+ | 7-8.5/10 | ~100% survival. More named molecules = more falsifiable. |
| Vibronic/phonon coupling | 004 | 3 | 2 | ~7.5/10 | Established physics in new protein system. |
| Quantitative thermodynamic framework (Pourbaix) | 005, 008 | 2 | 2 | 6-7.3/10 | Powerful but kinetics can override. |
| Tool transfer (PHREEQC, Pourbaix) | 005 | 1 | 1 | 7/10 | High novelty, must check biological constraints. |
| Quantitative scavenging budget | 006 | 1 | 1 | 7.5/10 | Inter-compartment signal feasibility. |
| ER-mito Ca2+ signaling at MAMs (CISD2) | 007 | 1 | 1 COND | 7/10 | Triple intersection: longevity x circadian x Fe-S. |
| Published gap extension | 009 | 3 | 0 PASS, 3 COND | 5.3-6.5/10 | Prior paper bridges B-term; hypothesis extends to stress context. |
| **Eraser depletion (HDAC3-NCoR depletion by stiffness) (NEW — S016 C2)** | **016** | **1** | **1 PASS** | **7.5/10** | **Paradigm inversion: ECM stiffness depletes an eraser (HDAC3-NCoR) rather than activating a writer. Novelty score 9 — highest in session. A-485 vs RGFP966 dissection is the key experiment. HDAC1/2 compensation is addressable concern. First MAGELLAN hypothesis to propose mechanoepigenetic regulation via eraser depletion.** |
| **Killed bridge types** | | | | | |
| Fabricated polymer interaction claims (S010) | 010 | 1 | 0 | 0 | HPMCAS-LLPS claims contradicted by NMR evidence. |
| Activation volume misapplication (S010) | 010 | 1 | 0 | 0 | Pressure kinetics invalidated by polymer matrix effects. |
| Direct electric/electromagnetic field effects | 001, 004 | 8 | 0 | 0 | Energy scale mismatch always fatal. |
| Quantum entanglement/information storage | 004 | 3 | 0 | 0 | Decoherence in biology is fatal. |
| **Mechanism fabrication: wrong compartment/topology (NEW — S013)** | **013** | **2** | **0** | **0** | **T6SS fires inward; OMVs bud outward. Topology mismatch = instant kill. OmpA gating model had zero literature support.** |
| **Equipment mismatch with specimen type (NEW — S013)** | **013** | **1** | **0** | **0** | **Microfluidic mixing-spray device designed for purified proteins incompatible with whole bacteria.** |
| **Spatial gradient (diffusion physics mismatch) (NEW — S014)** | **014** | **2** | **0** | **0** | **DnaA D~3 um2/s equilibrates across 2 um cell in <1s. Pe~0.002. Gradient physically impossible without active confinement.** |
| **Direct force on chromatin (NEW — S016)** | **016** | **2** | **0** | **0** | **Force per contact 100-1000x below LAD detachment threshold (C1-H2). Per-nucleosome force 13,000x below unwrapping threshold, below thermal noise (C1-H7). Same root cause as S001/S004 direct field kills. Pre-check: (total force) / (molecular contacts) vs physical threshold MANDATORY.** |

**New Bridge Type: Computational/Analytical Tool Transfer within Life Sciences (Session 013)**:
- **Performance**: 3 PASS, 1 COND from 4 hypotheses (highest bridge type performance yet recorded)
- **What works**: Statistical methods (GMM/BIC), power analysis frameworks, differential image analysis, ML-based in situ identification. All have established precedent in adjacent biological domains.
- **What fails**: Tools applied to specimens outside their validated range (protein size limits for cryoDRGN), tools misapplied to wrong compartments/topology
- **Guideline**: For computational/analytical tool transfers: verify tool's validated specimen range (size, sample type) before proposing application. Benchmark on similar specimens in original domain.

**New Bridge Type: Physical Law Constraint (Session 014)**:
- **Performance**: 1 PASS, 6 COND from 7 hypotheses (100% PASS+COND rate). Best hypothesis: C2-H5 at 7.90 composite (PASS).
- **What works**: Using a mathematical inequality (TUR: CV^2 >= 2/(Sigma*tau)) as a hard lower bound on biological observables. The bound cannot be violated; the hypothesis tests whether the system operates near or far from the bound. Parameters are all independently measurable. The direction of the result is FORCED by the math — unaffected by parameter uncertainty ranges.
- **What fails within this type**: Spatial gradient extensions of TUR (DnaA pole-biased firing) killed by diffusion physics (Pe~0.002). The mathematical constraint was valid but the proposed mechanism for achieving a gradient was physically impossible.
- **Guideline**: For physical law bridges: (1) State the exact inequality with parameters. (2) Compute the bound numerically with independently verified parameters. (3) Check whether the bound's direction is robust to +-order-of-magnitude parameter variation. (4) Propose experiments that test whether the biological system approaches the bound (not whether the bound holds — it always does).
- **Relationship to mathematical topology bridges (S002)**: Poincare-Hopf theorem and TUR inequality are both physical law bridges. Both produce necessary predictions. Both survive adversarial critique. Physical law bridges are a robust bridge category.

**New Bridge Type: Nuclear Architecture Spatial Selectivity Filter (Session 016)**:
- **Performance**: 1 PASS from 1 hypothesis (H4-v2, 8.5/10 — session high). Rescued a rank-4 parent through full mechanism pivot.
- **What works**: Using LAD tier classification (cLAD/fLAD/non-LAD) as a mechanistically grounded stiffness-readout filter. Three-tier model naturally produces distinct per-tier predictions. CRISPR tethering provides causal test. Null model (OR >= 4.0 vs H3K4me1 baseline) provides quantitative falsification threshold. Lamin A/C upregulation by stiffness is well-grounded (Swift 2013, Xu 2023, Mandal 2025).
- **Guideline**: When proposing ECM stiffness to genome topology bridges, use LAD compartmentalization as the filter architecture. cLADs are constitutively in nuclear periphery (not mechanosensitive); fLADs near constitutive enhancers (productive target); non-LAD regions (highest basal accessibility). Always include a proper null model (OR vs H3K4me1 baseline, not absolute percentages).

**New Bridge Type: Sequential Enzymatic Temporal Gate (Sessions 015-016)**:
- **Performance**: 2 PASS from 2 hypotheses across related sessions. Avg QG score ~7.6.
- **What works**: Two enzymes operating at distinct timescales on the same chromatin modification create a testable temporal gap. The gap (8-14h between non-bivalent and bivalent enhancer activation peaks) is a precision kinetic prediction uniquely associated with the sequential model. The sequential model is biochemically FORCED by enzymatic epistasis (demethylation must precede acetylation because H3K27me3/H3K27ac are mutually exclusive).
- **Guideline**: Whenever the Critic flags that two mechanistic components operate at different timescales, immediately consider "sequential two-phase model where the temporal gap is the prediction" as the primary evolution operation. Paralog disambiguation experiment (siKDM6A vs siKDM6B) elevates testability.

**New Bridge Type: Eraser Depletion as Mechanoepigenetic Mechanism (Session 016, Cycle 2)**:
- **Performance**: 1 PASS from 1 hypothesis (C2-H6, 7.5/10, novelty score 9 — highest novelty in the session).
- **What it is**: The dominant paradigm in mechanobiology assumes ECM stiffness ACTIVATES writers (EP300 HAT activity, SETD2 H3K36 methylation) to deposit activating marks. C2-H6 inverts this: ECM stiffness depletes an eraser (HDAC3-NCoR complex) from mechanosensitive enhancers, allowing H3K27ac to accumulate passively. Mechanistic route: stiffness -> YAP/ROCK1 -> HDAC3 nuclear export or NCoR complex destabilization -> reduced local deacetylase activity -> H3K27ac accumulation at YAP-bound enhancers.
- **Why it's underexplored**: Mechanobiology literature overwhelmingly frames regulation as "stiffness turns ON writer X." Eraser depletion produces the same H3K27ac output but is mechanistically distinct. Literature gap: essentially no papers examine stiffness effects on HDAC3-NCoR localization at enhancers (Fu 2024 is context-specific to chondrocyte senescence via Parkin, not enhancer regulation).
- **Key discriminating experiment**: A-485 (EP300 HAT inhibitor) vs RGFP966 (HDAC3 inhibitor). If eraser-depletion model is correct: RGFP966 on soft ECM should phenocopy stiff ECM H3K27ac pattern. A-485 on stiff ECM should NOT fully block H3K27ac gain if depletion is the primary mechanism.
- **Guideline**: When exploring chromatin regulation under external stimuli (ECM stiffness, shear stress, osmotic pressure, temperature), explicitly consider eraser depletion as a parallel hypothesis to writer activation. The two produce identical ChIP-seq output but opposite pharmacological predictions. Generator should generate ONE eraser-depletion hypothesis per mechano-epigenomics session.
- **Production technique**: `negation_exploration` — the Generator was prompted to invert the dominant-paradigm assumption. This is the first time this technique produced the highest-novelty hypothesis in a session (see Generator Technique Insights below).

**Recommendation for Generator**:
- **Use (highest QG scores)**: Published unmeasured variables. Thermodynamic displacement via Ksp. Mathematical necessity arguments (topology). Indirect multi-step enzymatic cascades. **Computational/analytical tool transfer within life sciences (NEW — S013, avg 8.31 composite).** **Physical law constraint bridges (NEW — S014, 100% PASS+COND rate).** **Nuclear architecture spatial filter using LAD tiers (NEW — S016, 8.5/10).** **Sequential enzymatic temporal gate when Critic identifies kinetic mismatch (NEW — S015-016, avg 7.6).** **Eraser depletion as alternative to writer activation (NEW — S016 C2, novelty 9, 7.5/10).**
- **Use with enhanced verification**: Geochemical tool transfer — verify biological constraints, polymer/matrix effects, sign of feedback mechanisms. BRD4-scaffolded retention — verify direct protein interaction domain before claiming mechanistic specificity.
- **Avoid (unconditional kills)**: Direct field effects. Fabricated polymer interactions without literature grounding. Mechanism fabrication (wrong compartment/topology). Equipment application outside validated specimen type. **Spatial gradient mechanisms without Pe > 1 or active confinement (NEW — S014).** **Direct force on molecular-scale chromatin targets (NEW — S016): force per contact is always below threshold; use biochemical relay instead.**
- **New verification rule (S013)**: For tool transfer bridges, verify: (a) specimen type compatibility, (b) tool's validated size/complexity range, (c) correct cellular compartment and topology, (d) named proteins/enzymes are confirmed for the specific model organism used.
- **New verification rule (S014)**: For spatial gradient hypotheses, compute Peclet number Pe = v*L/D. If Pe << 1, the gradient cannot persist passively. Must cite active confinement mechanism or the hypothesis is physically impossible.
- **New verification rule (S016)**: For mechanobiology hypotheses proposing direct force on chromatin components, compute per-element force = (total force) / (number of molecular contacts) and compare to the physical threshold. If per-element force is below 10x threshold, redesign to use biochemical amplification (YAP nuclear translocation, MRTF-A import, Ca2+/CaM cascade). Direct force-on-chromatin without this calculation = pre-kill vulnerability.

---

## Kill Pattern Distribution (all sessions, updated)

| Kill Reason | Estimated count | Approx % | Sessions |
|---|---|---|---|
| Energy scale mismatch (thermal overwhelm, too weak) | 14 | 16% | 001, 004 dominant |
| Substrate/condition mismatch | 8 | 9% | 005 dominant |
| Quantitative impossibility (Km saturation, concentration gap, threshold mismatch) | 9 | 10% | 005, 007, 008 |
| **Quantitative impossibility — diffusion physics (Pe << 1, spatial gradient impossible) (NEW — S014)** | **2** | **2%** | **014 (C2-H4, E-H4)** |
| **Quantitative impossibility — force below physical threshold (NEW — S016)** | **2** | **2%** | **016 (C1-H2: LAD detachment threshold 100-1000x; C1-H7: nucleosome unwrapping threshold 13,000x, below thermal noise)** |
| Classical explanation sufficiency | 6 | 7% | 001, 002, 004 |
| **Mechanism fabrication: wrong compartment or topology (includes S014)** | **8** | **9%** | **001 (indirect), 013 (T6SS, OmpA), 014 (V. cholerae RctB compound)** |
| Fabricated interaction claims (S010) | 2 | 2% | 010 |
| Mechanism fabrication (no known receptor/enzyme/pathway) | 5 | 6% | 002, 006 |
| Mechanism wrong (correct mechanism exists, wrong one cited) | 2 | 2% | 014 (H5 ppGpp), prior |
| Thermodynamic impossibility (wrong redox, wrong pH) | 4 | 5% | 007, 005 |
| Citation hallucination / unverifiable reference | 3 | 3% | 004 |
| **Citation misuse (real paper, wrong conclusion attributed) (NEW — S014)** | **1** | **1%** | **014 (H6: Campos 2014 adder cited as sizer)** |
| Mathematical invalidity | 3 | 3% | 002 |
| **Logic kill: internal contradiction (NEW — S014)** | **1** | **1%** | **014 (C2-H3: near-zero WT memory vs claimed explanation of substantial memory)** |
| Scope overreach / universal claim | 3 | 3% | 002 |
| Novelty failure (well-studied in adjacent domain) | 2 | 2% | 008 |
| **Conceptual flaw — YAP-TEAD tissue-specificity error (NEW — S016)** | **1** | **1%** | **016 (C1-H6: YAP-TEAD targets are shared proliferation enhancers, not tissue-specific; lineage TFs required)** |
| Autocatalytic sign error (S010) | 1 | 1% | 010 |
| Binding affinity too weak (Ka) (S012) | 3 | 3% | 012 |
| Vocabulary re-description | 2 | 2% | 002, 005 |
| **Equipment mismatch with specimen type (NEW — S013)** | **1** | **1%** | **013 (C2-H5 microfluidic device)** |
| ROS species mismatch | 1 | 1% | 009 |
| **Time-scale mismatch: fast upstream trigger vs slow downstream effector (NEW — S016 C2)** | **1** | **1%** | **016 C2 (C2-H4: PIEZO1 ~30ms vs calcineurin minutes; 10,000-100,000x incompatibility)** |
| **Low groundedness + multi-step unverified chain (NEW — S016 C2)** | **1** | **1%** | **016 C2 (C2-H5: groundedness 33% + 3 unverified sequential steps; hallucination-as-novelty)** |
| **Mechanism impossible by mathematical construction (NEW — S018, K14)** | **1** | **<1%** | **018 C1 (H3: standard MSM detailed balance enforcement → symmetric transition matrix → normal matrix → Henrici delta(Q)=0; non-normality structurally impossible in equilibrium MSMs)** |
| **Partial citation hallucination — correct venue/year, fabricated first author (NEW — S018, K15)** | **1** | **<1%** | **018 QG (C2-H1-resource: 'Avanzini et al. 2026 PRX 16:011065' — journal PRX and year 2026 correct; first author 'Avanzini' fabricated; actual: Summer, Moroder, Bettmann, Turkeshi, Marvian, Goold)** |
| **Anatomy error: proposed residue outside fragment range (NEW — S018)** | **1** | **<1%** | **018 QG (C2-H6: T217 at position 217 is outside K18 fragment residues 244-372; core mechanistic claim structurally impossible)** |
| **System computationally infeasible (S018 confirmation — PrP MSM)** | **+1** | | **018 C1 (H7: PrP^C→Sc alpha→beta transition far beyond MD capabilities; cofactors absent; 80C denatures PrP before strain selection window)** |

**New Kill Patterns (Session 013)**:
1. **Wrong cellular topology/compartment**: T6SS fires inward through inner membrane; OMVs bud outward from outer membrane. Compartment topology mismatch is a rapid kill — verify the directionality of molecular machines before proposing cargo transfer between cellular structures.
2. **Equipment mismatch with specimen type**: Time-resolved cryo-EM microfluidic device validated for purified proteins is incompatible with whole bacterial cells. Technique transfer requires specimen-technique compatibility check, not just theoretical feasibility check.
3. **cryoDRGN minimum particle size**: Tool has a validated lower limit (~100 kDa). OmpA at 35 kDa was 3x below this limit. For tool transfer hypotheses, verify the tool's quantitative range limits.

**New Kill Patterns (Session 014)**:
4. **Spatial gradient physically impossible (diffusion physics / Peclet number)**: For any passive spatial gradient hypothesis in a cell, compute Pe = v*L/D. DnaA: D~3 um2/s, L=2 um -> Pe~0.002. Gradient homogenizes in <1s; cell cycle operates on minutes. Gradient cannot exist without active maintenance mechanism. Pe check is now a REQUIRED pre-verification step.
5. **Citation misuse (real paper, opposite conclusion)**: Campos 2014 proves E. coli-like ADDER for Caulobacter, cited as evidence of a SIZER. The paper exists and the biology is real — but the conclusion cited is the opposite of the paper's actual finding. Check that paper's MAIN CONCLUSION matches the claimed content, not just that the paper exists.
6. **Logic kill: internal quantitative contradiction**: C2-H3 predicted near-zero WT memory (f=0.007 per-generation correlation) while claiming to explain Susman 2025's "substantial nonlinear memory" in WT E. coli. These are irreconcilable without addressing the quantitative gap. When a hypothesis both quantifies and claims to explain an empirical observation, verify the quantitative consistency.
7. **Computational phase error propagation**: Computational Validator's N_eff=20 events was misinterpreted as 20 DnaA boxes (actual: 11). The ambiguous upstream estimate contaminated 3 downstream hypotheses simultaneously. Computational Validator must explicitly distinguish physical binding site count, events per cycle, and TUR parameter N_eff with separate literature citations for each.

**New Kill Patterns (Session 016, Cycle 2)**:
10. **Time-scale mismatch (kinetic incompatibility) — confirmed dominant kill vector**: C2-H4 killed because PIEZO1 inactivation (~30 ms) is 10,000-100,000x too fast for calcineurin (requires minutes of sustained Ca2+ for full activation). Same root cause as S001/S004 energy scale kills and S016-C1 force-below-threshold kills: a quantitative physical/biochemical incompatibility that is detectable before generation. Pattern is now confirmed across 3 session families: energy scale (S001, S004), force below threshold (S016 C1), kinetic time-scale mismatch (S016 C2). Generator MUST perform a time-scale compatibility check before pairing a fast upstream trigger (ion channel gating, receptor internalization) with a slow downstream effector (phosphatase activation, transcription factor translocation). Minimum check: does the upstream event persist long enough to saturate or significantly activate the downstream effector? If upstream τ << downstream τ by > 100x on STATIC substrates, the mechanism is kinetically impossible.
11. **Groundedness below 50% + multi-step unverified chain = pre-kill vulnerability**: C2-H5 (viscoelastic filter) killed with groundedness 33% AND three sequential unverified mechanism steps. This combination — low grounding combined with mechanistic dependency chain (each step must be true for hypothesis to hold) — represents a fatal structural flaw. A three-step unverified chain where each step has 50% individual confidence gives compound confidence of 12.5%. Generator rule: when < 50% of mechanism claims are grounded, the hypothesis should not be submitted. Force at least one anchor (named protein, published interaction, measured timescale) at each step before proposing multi-step cascades.

**New Kill Patterns (Session 018 — Mpemba Spectral Theory x Amyloid Aggregation)**:
14. **Mechanism impossible by mathematical construction**: H3 (cycle 1) proposed Henrici non-normality measure (delta(Q) > 0) for standard protein MSMs. FATAL: Standard MSM tools (PyEMMA, MSMBuilder) enforce detailed balance, which symmetrizes the transition matrix (Q → (Q+Q^T)/2), making it a normal matrix by construction — Henrici delta(Q) = 0 always. The very tool being used eliminates the property being measured. This extends S013's "compartment topology mismatch" kill: here the constraint is not spatial topology but MATHEMATICAL SYMMETRY imposed by the tool. **Pre-generation checklist item**: Before proposing a mathematical property that requires breaking a symmetry (non-normality, irreversibility, non-stationarity), verify the standard tool does NOT impose that symmetry by construction. Rescue path: specify the non-equilibrium condition that genuinely breaks detailed balance (Hsp70 ATPase cycling, irreversible aggregation sinks) and use non-symmetrized estimators (dtram, MBAR).
15. **Partial citation hallucination (correct venue, fabricated first author)**: C2-H1 cited "Avanzini et al. 2026, PRX 16:011065" — the journal (PRX), year (2026), and volume are correct, but "Avanzini" is the wrong first author. The actual paper is Summer, Moroder, Bettmann, Turkeshi, Marvian, and Goold (2026 PRX). The LLM correctly recalled the publication venue and date but confabulated the first author. This is a new sub-type of citation hallucination distinct from: fabricated paper (S004), wrong journal (S013), wrong year (S001/S013), wrong main conclusion (S014). **Pattern**: For recently published papers (< 6 months), verify the first author name explicitly via search — do not rely on parametric recall of author attribution. Venue and year are remembered more reliably than author names.
16. **System computationally infeasible (PrP MSM)** (S018, not a new pattern but confirmed): H7 proposed a prion strain selection model requiring a PrP misfolding MSM. FATAL: PrP^C → PrP^Sc involves a massive alpha-helix → beta-sheet conformational change of ~50 kDa, far beyond current MD capabilities (~100-200 us); additionally, PrP strain selection depends on cellular cofactors (lipids, RNA, polyanions) absent from simplified models. **Rescue**: Evolver correctly pivoted to insulin at pH 2 and beta-2-microglobulin at pH 2.5 — systems with existing trajectory data and tractable MSM construction. When a model system is computationally infeasible, pivot to the closest tractable model system that shares the key mechanistic property (fibril polymorphism) but has existing simulation data.

**New Kill Patterns (Session 017 — EVT x Proteome Thermal Stability)**:
12. **Data-type requirement mismatch for mathematical bridge concepts**: Extremal index (H6) requires sequential/temporal data with defined clustering order; applying it to cross-sectional Tm data sorted by value creates tautological clustering. Non-stationary GEV with trend (H4) requires smoothly-ordered observations; drug concentration series (3-5 points) is grossly insufficient. When transferring a mathematical concept, verify that Field C's available data has the STRUCTURAL FORM required by the concept definition. This is distinct from quantitative checks (sample size, effect size). Add as a pre-generation step alongside specimen compatibility and Peclet checks.
13. **IDP model misspecification by population heterogeneity (new QG-level kill)**: Censored GEV (H3) survived critique but failed QG because IDPs in the censored population have NO defined cooperative unfolding transition — Tm is undefined, not merely below the measurement window. This is a new failure mode: a parametric model that is mathematically valid for one subpopulation (folded proteins with defined Tm) is catastrophically misspecified for a qualitatively different subpopulation (IDPs). For any hypothesis applying a parametric model to proteome-wide data, verify that ALL subpopulations satisfy the model's foundational assumptions. IDPs are now a confirmed recurrent assumption-violation risk in proteomics: 30-50% of eukaryotic proteome; enriched in the low-Tm tail; lack cooperative unfolding; behave qualitatively differently from folded proteins.

**New Kill Patterns (Session 016, Cycle 1)**:
8. **Force per element below physical threshold — force-on-chromatin class**: Two hypotheses killed by the same mechanism. C1-H2: per-LAD tether force 100-1000x below biochemical LAD detachment threshold (H3K9me2 removal requires enzymatic demethylase, not mechanical force; Sun 2020 PMID 32270037 confirms). C1-H7: per-nucleosome force 13,000x below nucleosome unwrapping threshold (~50 pN), well below thermal noise (~4.1 pN). Root cause: ECM stiffness forces divide across thousands-to-millions of molecular contacts; per-molecule force is always below threshold. Pre-check: (total force) / (molecular contacts) vs physical threshold. All surviving mechanobiology hypotheses used biochemical amplification (YAP translocation, Ca2+/CaM, actomyosin -> MRTF). This kill pattern is the mechanobiology-domain equivalent of the S001/S004 energy scale mismatch pattern.
9. **YAP-TEAD tissue-specificity error — biology specificity class**: Hypothesis C1-H6 claimed YAP-TEAD drives tissue-specific enhancer programs. YAP-TEAD targets are shared proliferation/survival enhancers (CTGF, CYR61, AMOTL1) expressed across all stiff-matrix cell types. Tissue identity requires lineage-specific TFs (MYOD, RUNX2, PPARgamma) co-binding at tissue-restricted loci. YAP-TEAD produces QUANTITATIVELY GRADED activation of the SAME enhancer program, not QUALITATIVELY DIFFERENT programs. The morphogen analogy fails because morphogens produce qualitatively different cell fates at different concentrations; YAP produces more or less of the same target gene set. Generator rule: never claim YAP-TEAD is "tissue-specific" without citing a co-binding lineage TF.

**Recommendation for Generator**:
0. **Force-per-contact check (NEW — S016, MANDATORY for mechanobiology)**: For any hypothesis proposing that cytoskeletal/nuclear mechanical force acts directly on chromatin: compute F_per_contact = F_total (cite source) / N_contacts (cite or estimate). Required thresholds: chromatin loop deformation ~1 pN; nucleosome outer-wrap unwrapping ~2 pN; inner-wrap ~5-8 pN. If F_per_contact < threshold, the direct force mechanism is physically impossible. LINC complex typical F_total = 10-100 pN. At N_contacts = 100,000+, F_per_contact = 0.001-0.001 pN — too weak by 3-4 orders of magnitude. Signaling cascades (YAP nuclear translocation, ROCK1 activation) can work at these force levels; direct physical chromatin unwrapping cannot.
1. **Compartment/topology pre-check (NEW — S013)**: Before proposing cargo transfer between compartments or organelles, verify the topology and directionality of the proposed molecular machine. Inner membrane vs outer membrane, inward-firing vs outward-budding, periplasmic vs cytoplasmic — these distinctions are binary kill factors.
2. **Specimen-technique compatibility check (NEW — S013)**: For technique transfer, verify the source technique's validated specimen type (purified proteins, cell lysates, whole cells, tissue). Mismatch = feasibility kill even if the theoretical principle is sound.
3. **Tool quantitative range check (NEW — S013)**: For tool transfer, retrieve the tool's validated operating range (particle size for cryo-EM methods, affinity range for binding assays, concentration range for spectroscopy). Proposing application outside this range = technical impossibility.
4. **Species-specific protein confirmation (NEW — S013)**: Named proteins in bridge mechanism must be confirmed for the specific model organism in Field C. P. aeruginosa uses MucD, not DegP (E. coli), as the primary HtrA-family periplasmic chaperone. Genus-level assumption of protein conservation is unreliable.
5. **Peclet number check for spatial gradient hypotheses (NEW — S014)**: Before proposing any spatial concentration gradient in a cell, compute Pe = v*L/D. If Pe << 1 (passive diffusion dominates), the gradient washes out faster than the biological process operates. Cite the active confinement mechanism explicitly or abandon the spatial gradient.
6. **Citation conclusion verification (NEW — S014)**: When citing a paper for a specific result, verify the paper's MAIN CONCLUSION — not just its existence. Papers are sometimes cited for the opposite of their conclusion. Cross-check: does the paper's abstract conclusion match the claim being grounded?
7. **Independent verification of Computational Validator counting parameters (NEW — S014)**: When Computational Validator provides N_eff or copy number recommendations, independently verify from primary literature: (a) the physical binding site count, (b) events per cycle, (c) regulatory context (RIDA, DARS, datA). Upstream parameter errors cascade into multiple hypotheses.
7b. **Data-structural form check for mathematical bridge concepts (NEW — S017, MANDATORY)**: Before proposing a mathematical method as a bridge, verify that Field C's available data has the structural form required by the method definition. Check: (a) sequential/temporal vs cross-sectional; (b) ordered vs unordered; (c) sufficient observation density for trend fitting. Cross-sectional proteome Tm data lacks time-ordering required for extremal index and lacks sufficient points for non-stationary GEV. Pre-generation checklist: [what data structure does this method require?] vs [what structure does Field C data actually have?]
7c. **IDP subpopulation check for proteome-wide parametric models (NEW — S017)**: For any parametric model applied to proteome-wide data, ask: "Do IDPs (30-50% of eukaryotic proteome) satisfy this model's foundational assumptions?" IDPs lack defined Tm, cooperative unfolding, stable hydrophobic core. Any model assuming "all proteins have a defined Tm" is structurally misspecified for IDPs. State IDP exclusion criteria explicitly and estimate the excluded fraction.
8. **YAP-TEAD tissue-specificity error (NEW — S016)**: Never claim YAP-TEAD drives tissue-specific enhancers without specifying the co-binding lineage-restricted TF (MYOD, RUNX2, PPARgamma, SOX2, CDX2). YAP-TEAD alone activates CTGF/CYR61/AMOTL1 — shared proliferation enhancers across ALL stiff-matrix cell types.
9. **MRTF-SRF mandatory consideration for mechano-epigenomics (NEW — S016)**: When generating hypotheses for ECM mechanics x chromatin/epigenomics, include at least one MRTF-SRF hypothesis. Route: RhoA -> ROCK -> actin polymerization -> MRTF-A released from G-actin -> SRF -> CArG-box enhancers. Targets non-overlapping from TEAD. Do NOT generate more than 3 YAP-centric hypotheses in a 7-hypothesis cycle for this domain.
10. **Citation verification for very recent papers (NEW — S018, MANDATORY)**: For any paper published or preprinted in the past 6 months (2025-2026), verify the FIRST AUTHOR NAME explicitly via web search before citing. State: "First author: [NAME], verified via search for [query]." Journal, year, and volume are recalled reliably; first author attribution for recent papers is systematically hallucination-prone. The Avanzini confabulation (S018, C2-H1) is the clearest documented case: journal (PRX), year (2026), and volume (16) were all correct; only the first author was wrong. Do not cite without this verification.
11. **Symmetry constraint pre-check (NEW — S018, MANDATORY)**: Before proposing any mathematical property that requires breaking a symmetry constraint imposed by the standard tool, verify that the tool does NOT enforce that symmetry. Key confirmed case: standard protein MSMs (PyEMMA, MSMBuilder, deeptime) enforce detailed balance (reversibility), which symmetrizes the transition rate matrix Q → (Q+Q^T)/2, making it a normal matrix by construction — Henrici non-normality delta(Q) = 0 always. Proposing non-normal dynamics in standard reversible MSMs is structurally impossible. Rescue: specify the physical non-equilibrium condition that genuinely breaks detailed balance (Hsp70 ATPase cycling, irreversible aggregation sink states) and use non-symmetrized estimators (dtram, MBAR, TRAM). Symmetry pre-check is now mandatory for all mathematical-property bridge proposals.
12. **Protein fragment residue position check (NEW — S018)**: For any hypothesis specifying that a post-translational modification at residue X modulates a protein fragment simulation spanning residues A-B, verify that X is in the range [A, B] before generation. C2-H6 (S018) claimed T217 phosphorylation perturbs the K18 fragment (residues 244-372) — T217 is at position 217, OUTSIDE the fragment. This is a trivial arithmetic check that prevents an automatic FAIL.

---

## Session Performance History

| Session | Target | Hyps gen | Kill rate | QG pass+cond | QG PASS | QG mean | Evolver | Status |
|---|---|---|---|---|---|---|---|---|
| 001 | Bioelectric x Condensates | ~8 | ~50% | 4 | 4 | ~7.5 | — | SUCCESS |
| 002 | Active matter x Stem cells | ~12 | ~75% | 3 | 3 | ~7.0 | — | SUCCESS |
| 003 | (targeted, early session) | — | — | — | — | — | — | — |
| 004 | THz spectroscopy x Quantum coherence | 15 | 67% | 2 | 2 | ~6.5 | — | SUCCESS |
| 005 | Ferroptosis x Serpentinization | 14 | 50% | 4 | 4 | ~7.0 | — | SUCCESS |
| 006 | Ferroptosis x Quorum sensing | 14 | ~36% | 6 | 6 | ~7.2 | — | SUCCESS |
| 007 | Fe-S biogenesis x Circadian clock | 15 | 17% | 5 | 1 + 4 COND | ~6.6 | — | SUCCESS |
| 008 | Cuproptosis x Vent Cu-S Geochemistry | 12 | 17% | 5 | 1 + 4 COND | ~6.8 | — | SUCCESS |
| 009 | Plant melatonin x Coral bleaching | 10 | 0% | 3 COND | 0 | 5.87 | run | PARTIAL |
| 010 | Volcanic glass x ASD dissolution | 13 | 42.9% | 1 PASS | 1 | 6.23 | run | SUCCESS |
| 011 | Cartilage biphasic x Biofilm mechanics | 8 | 50% | 2 PASS, 2 COND | 2 | 7.28 | run | SUCCESS |
| 012 | Mn speciation x Deinococcus Mn-OP | 14 | 21.4% | 0 PASS, 5 COND | 0 | 7.1 | run | SUCCESS |
| 013 | Cryo-EM heterogeneity x OMV cargo sorting | 11 | 27.3% | 3 PASS, 1 COND | 3 | 8.31 | SKIPPED | SUCCESS |
| **014** | **TUR x Bacterial adder model** | **15** | **33%** | **1 PASS, 6 COND** | **1** | **6.81** | **run** | **SUCCESS** |
| **015** | **Mechanobiology x Epigenomics (targeted, NEWLY_OPENED)** | **~12 est.** | **0%** | **3 PASS** | **3** | **~7.5 est.** | **run** | **SUCCESS** |
| **016** | **Mechanobiology x Epigenomics (targeted, blind mode, 2 cycles)** | **7 (C1) + 7 (C2) = 14** | **C1: 28.6%, C2: 28.6%** | **C1: 2 PASS, 1 COND; C2: 3 PASS, 2 COND** | **C1: 2, C2: 3** | **C1: 7.50; C2: 7.10** | **C1: run; C2: SKIPPED** | **SUCCESS** |
| **017** | **EVT x Proteome Thermal Stability (2026-03-27-scout-013)** | **7** | **28.6%** | **1 PASS, 2 COND** | **1** | **7.87** | **SKIPPED** | **SUCCESS** |
| **018** | **Mpemba Spectral Theory x Amyloid Aggregation (2026-03-28-scout-014)** | **15** | **20%** | **1 PASS, 5 COND** | **1** | **6.97** | **C1: run; C2: SKIPPED** | **PARTIAL** |

**Session 013 Analysis**:
- **Best QG PASS count ever**: 3 PASS verdicts from 4 entering hypotheses. S013 achieved 75% outright PASS rate.
- **Highest mean composite**: 8.31 — surpassing S001 (~7.5) which previously held the record.
- **Zero fabricated claims found**: Quality Gate reported 0 citation hallucinations, 0 fabricated claims, 0 mechanism errors (only 1 citation error in journal name, 1 unverifiable formula in C2-H2). Lowest error rate in pipeline history.
- **Evolver correctly skipped**: Cycle 2 top-3 composite >= 6.5 triggered skip condition.
- **Kill rate**: 27.3% (healthy range).

**Session 014 Analysis**:
- **Highest PASS+COND absolute count ever**: 7 survivors from 8 entering QG (87.5% PASS+COND rate). Previous records: S013 (4 survivors), S006 (6 survivors). First session to exceed 6 survivors at QG.
- **First primary test of converging_vocabularies**: Strategy debut produced dense hypothesis generation — one core mathematical bridge (TUR) yielded 7 distinct survivors covering 6 different sub-hypotheses of the same framework. This is the highest hypothesis diversity from a single bridge concept.
- **Mean composite 6.81**: Below S013 (8.31) but above S010 (6.23) and S009 (5.87). The lower composite relative to S013 reflects more CONDITIONAL verdicts (6 vs 1) — conditions are addressable (extrinsic noise, cooperative binding, broken primary experiment). These are quality COND, not intractable COND.
- **Citation error rate**: 2 minor citation errors (journal/page), 1 unverifiable citation, 0 hallucinations. Clean session.
- **Kill rate**: 33% (5/15 in critique — healthy range). One additional QG FAIL (E-H4) for total 6 kills.
- **Evolver ran**: Cycle 2 was necessary; cycle 1 top-3 composite did not meet skip threshold.

**Session 015 Analysis**:
- **Best PARTIALLY_EXPLORED result**: 3 PASS from 3 entering QG. Zero kills in critique (kill rate 0%). Newly-opened subfield (Cosgrove 2025 Science < 6 months prior).
- **Multi-pathway convergence on single hub (EP300)**: 5 complementary hypotheses from one hub protein. Strategy for dense hypothesis generation in targeted sessions: identify hub protein with high STRING scores to both Field A and Field C proteins, then generate hypotheses for each upstream pathway to the hub.
- **NEWLY_OPENED_PARTIALLY_EXPLORED**: S015 introduced this subcategory. Confirmed by S016.

**Session 016 Analysis (Cycle 1)**:
- **Mean composite 7.50**: Above pipeline average. Best hypothesis H4-v2 at 8.5/10 — highest score this session and competitive with best-ever scores.
- **100% QG pass+cond rate**: 2 PASS + 1 COND from 3 evolved hypotheses entering QG.
- **Force-on-chromatin kill pattern confirmed (3rd session family)**: Both kills (C1-H2, C1-H7) share identical root cause — per-element force below physical threshold by 100x-13,000x. Three session families now confirm direct force-on-molecular-target is always quantitatively fatal: S001 (electric fields), S004 (THz photons), S016 (ECM forces on nucleosomes/LADs).
- **YAP-centrism bias documented**: 5/7 cycle 1 hypotheses used YAP-EP300. MRTF-SRF absent from cycle 1. Systematic generator bias for this target domain identified and added to Generator screening rules (Rules 35-37).
- **Evolution rescued rank-4 parent**: H4-v2 (8.5/10, PASS) descended from a Ranker rank-4 hypothesis via full mechanism pivot. Lowest-ranked parent produced highest QG score. Evolver should consider mechanism replacement, not only refinement.
- **Blind mode validated**: Zero citation hallucinations across 18 post-verified citations. Blind generative phase + post-blind QG web verification is a viable pipeline architecture.
- **Kill rate**: 28.6% (healthy range).
- **Domain saturation warning**: S015 + S016 are consecutive sessions in the same domain. A third mechano-epigenomics session risks novelty degradation.

**Session 016 Analysis (Cycle 2)**:
- **5/5 QG pass+cond (100%)**: C2-H6 (7.5 PASS), E1-H3 (7.5 PASS), E1-H4 (7.0 PASS), E1-H5 (6.0 COND), C2-H7 (5.5 COND). Zero citation hallucinations across all 5 evaluated.
- **Evolver correctly skipped**: Top-3 composites 7.4/7.2/7.1 all ≥ 6.5 threshold. Adaptive cycle rule triggered correctly — consistent with S013 skip.
- **negation_exploration produced highest-novelty hypothesis in session**: C2-H6 (eraser depletion, novelty 9) was the first hypothesis in MAGELLAN history to propose mechanoepigenetic regulation via eraser depletion rather than writer activation. Produced by paradigm-inversion technique.
- **Time-scale mismatch confirmed as dominant kill vector**: C2-H4 (PIEZO1 → calcineurin, 30ms vs minutes) killed for the same root cause as S001/S004/S016-C1 force/energy kills — quantitative physical incompatibility that is detectable pre-generation. Three kill families now share this root: energy scale, force-per-contact, kinetic time-scale.
- **Kill rate**: 28.6% (C2-H4, C2-H5) — exactly matching cycle 1 rate.
- **Cycle 1 evolved hypotheses outperformed cycle 2 raw**: E1-H3 and E1-H4 (both PASS, 7.5/7.0) from cycle 1 evolution performed at least as well as best cycle 2 raw (C2-H6 7.5). Evolution quality is equivalent to fresh generation when source hypotheses are structurally sound.
- **Combined session totals (S016 C1+C2)**: 14 hypotheses generated, 10 survived critique (71.4% survival), 8 entering QG (after diversity pruning), 5 PASS + 3 COND (100% QG pass+cond across all batches).

**Session 017 Analysis (2026-03-27-scout-013)**:
- **EVT x Proteome Thermal Stability**: First session pairing formal mathematical statistics (extreme value theory) with proteomics. Domain type "statistics x life sciences" is entirely new to the pipeline.
- **Highest disciplinary distance ever**: Avg 3.0/3.0 for QG-passing hypotheses. Statistics → biostatistics → biology crosses three disciplinary boundaries. Previous pipeline avg ~2.2.
- **Mean composite 7.87 (QG-passing)**: Highest mean composite for passing hypotheses ever recorded, surpassing S013 (8.31 overall) on a per-survivor basis.
- **converging_vocabularies + FTG universality theorem**: Second confirmation that converging_vocabularies works best when Field A contributes a mathematical theorem (TUR in S014, FTG in S017) rather than a fitting procedure. The theorem creates guaranteed predictions about form; parameters become the testable biology.
- **Kill rate 28.6%**: Healthy range. Both kills were data-type mismatch errors (extremal index requires temporal/sequential data; non-stationary GEV requires dense ordered observations — neither applies to cross-sectional Tm data).
- **IDP model misspecification (new QG-level kill)**: H3 passed critique but failed QG for model misspecification by population heterogeneity. IDPs (30-50% eukaryotic proteome) lack defined Tm — censored GEV models a non-existent quantity. This is a new failure mode: mathematically correct method applied to a heterogeneous population where assumptions hold for one subpopulation but are violated for another.
- **Systematic citation attribution error (3rd session)**: S007, S013 (cryo-EM), S017 — all show review-paper substitution for primary source. Generator pattern confirmed across multiple domains.
- **Evolver correctly skipped**: Top-3 composites (8.45, 8.15, 7.05) all ≥ 7.0 early-complete threshold.

**Trend analysis (S013-S018)**:
- **Pipeline quality trajectory**: S013 (8.31) -> S014 (6.81) -> S015 (~7.5 est.) -> S016 (7.50) -> S017 (7.87) -> S018 (6.97). S018 dip vs S017 reflects PARTIAL health and the single-molecule to multi-molecule bridging difficulty inherent to Mpemba spectral formalism applied to amyloid aggregation (secondary nucleation is a multi-molecule process invisible to monomer MSMs). S018 produced 1 PASS + 5 COND — not COND-only. anomaly_hunting debut is the best strategy debut in pipeline history by QG mean composite (6.97 vs 6.81 for converging_vocabularies debut in S014, 5.87 for Swanson_ABC debut in S009).
- **Survivor count trend**: S013 (4 QG entering) -> S014 (7) -> S015 (3) -> S016 (3+5 across 2 cycles) -> S017 (3) -> S018 (6 from 8 entering). S018 has the second-highest QG entry count (8) after S014 (8). 15-hypothesis generation now standard for 2-cycle sessions.
- **Strategy rotation**: S013 (tool_repurposing) -> S014 (converging_vocabularies) -> S015-S016 (targeted) -> S017 (converging_vocabularies) -> S018 (anomaly_hunting). Strategy diversification healthy; anomaly_hunting exploration slot fulfilled.
- **DISJOINT maintained**: S018 target had disjointness 0.95 (PubMed: 0 cross-field papers). 12 consecutive DISJOINT sessions (S006-S018 excluding S015-S016 targeted).
- **anomaly_hunting first data**: PARTIAL health, 1 PASS + 5 COND, 6.97 mean composite. Single session insufficient for reliable ranking — needs second primary session. Provisional: above Swanson_ABC and network_gap_analysis, below converging_vocabularies and tool_repurposing.

**Session 018 Analysis (2026-03-28-scout-014) — FINAL**:
- **anomaly_hunting exploration slot fulfilled**: First primary session confirms the strategy finds genuinely unexplored territory (0 PubMed/Semantic Scholar cross-field papers, disjointness 0.95). Zero prior art on Mpemba × protein biology across 6 independent web searches.
- **QG results: 1 PASS + 5 COND + 2 FAIL from 8 evaluated** (8 entering, 6 passing = 75% PASS+COND). Mean composite 6.97. QG evaluated cycle 1 evolved + cycle 2 combined. Best hypothesis: C2-H7 (Cooling-Rate Fibril Polymorph Selection in Insulin, 7.5, PASS). FAILs: C2-H1-resource (Avanzini fabricated citation + wrong math formula) and C2-H6 (T217 outside K18 fragment + Wesseling misattributed).
- **PARTIAL health driven by structural constraint, not strategy failure**: PARTIAL classification reflects the absence of full PASS verdicts from the initial cycle 1 generation. The monomer→population bridging gap (amyloid nucleation is dominated by secondary nucleation, a multi-molecule surface-templated process invisible to monomer MSMs) is the structural reason all cycle 1 hypotheses were CONDITIONAL. The Evolver pivot from PrP to insulin broke through this constraint and produced the session's only PASS.
- **Evolver pivot (PrP → insulin) was the decisive operation**: C2-H7 (PASS, 7.5) traces through the H7 lineage, which was KILLED in cycle 1 critique (PrP misfolding MSM computationally infeasible, 80C denaturates PrP). Evolver replaced the system with insulin at pH 2 — tractable, well-characterized, existing trajectory data. System replacement was higher value than mechanism refinement.
- **Highest novelty-type average in pipeline history (3.3/4.0)**: Surpasses S017 (3.0). C2-H4 (novelty 9) and C2-H1-resource (novelty paradigm-shift 4/4, though killed by citation). anomaly_hunting reliably produces high-creativity output.
- **Two new kill patterns confirmed**: (K14) Mechanism impossible by mathematical construction — standard MSM detailed balance enforcement makes non-normality (Henrici delta(Q)) identically zero; standard tools eliminate the property being measured. (K15) Partial citation hallucination — correct venue/year, fabricated first author. 'Avanzini et al. 2026 PRX' — journal and year correct; first author name is confabulated. Persistent across both cycles despite Critic flag.
- **Kill rate 20%** (3 kills from 15 hypotheses — lower than average 28%). Critic correctly identified both kills in cycle 1 (H3: non-normality impossible; H7: PrP infeasible). QG killed 2 additional (C2-H1-resource, C2-H6) — both citation or anatomy errors.
- **Evolver correctly ran in cycle 1, skipped in cycle 2**: Cycle 1 ran (top-3 below 7.0 threshold). Cycle 2 skipped — top-3 composites from QG (8.43, 8.28, 7.81) all ≥ 6.5 skip threshold. Third consecutive skip after S013 and S017.
- **Generator-level persistent error identified**: Avanzini confabulation persisted from cycle 1 through cycle 2 despite explicit Critic flag. This is a new failure mode — parametric recall of venue/year is reliable, but author attribution for very recent papers is unreliable, and self-critique cannot catch what parametric memory has confabulated. Requires mandatory search verification rule for 2025-2026 citations (Rule 38).

---

## Creativity Metrics (v5.8)

### Per-Session Creativity

| Session | Avg Disciplinary Distance (0-3) | Avg Abstraction Level (1-3) | Avg Novelty Type (1-4) | Strategy |
|---|---|---|---|---|
| 001 | 2.5 | 2.0 | 2.5 | implicit_disjoint |
| 002 | 2.5 | 2.5 | 3.0 | implicit_disjoint |
| 004 | 2.0 | 2.0 | 2.0 | recent_breakthrough_radiation |
| 005 | 2.0 | 1.5 | 2.0 | scale_bridging |
| 006 | 2.5 | 1.5 | 2.5 | network_gap_analysis |
| 007 | 2.0 | 1.5 | 2.0 | network_gap_analysis |
| 008 | 2.0 | 1.5 | 2.0 | network_gap_analysis |
| 009 | 2.5 | 2.0 | 2.5 | Swanson_ABC_bridging |
| 010 | 2.5 | 1.5 | 2.0 | tool_repurposing |
| 011 | 2.5 | 2.5 | 3.0 | structural_isomorphism |
| 012 | 2.5 | 2.0 | 2.5 | contradiction_mining |
| 013 | 1.5 | 1.5 | 2.0 | tool_repurposing |
| **014** | **2.0** | **1.7** | **2.6** | **converging_vocabularies** |
| **015** | **2.6** | **2.0** | **2.5** | **targeted (newly opened, mechano x epigenomics)** |
| **016** | **2.0** | **1.7** | **2.3** | **targeted (blind, newly opened, mechano x epigenomics)** |
| **017** | **3.0** | **2.3** | **3.0** | **converging_vocabularies (EVT x Proteome Thermal Stability)** |
| **018** | **2.7** | **2.3** | **3.3** | **anomaly_hunting (Mpemba Spectral Theory x Amyloid Aggregation)** |

### Cross-Session Creativity Trend
- Disciplinary Distance trend: **HIGH AND STABLE**. Pipeline avg now 2.3+. S013 dip (1.5) -> S014 (2.0) -> S015 (2.6) -> S016 (2.0) -> S017 (3.0) -> S018 (2.7). S017 and S018 are tied-highest sessions in pipeline history. Physics × biology pairings (S014, S018) and statistics × biology pairings (S017) both achieve 2.7-3.0 distance. No corrective action needed.
- Abstraction Level trend: **stable at 1.7-2.3**. S018 (2.3) reflects the mathematical framing of Mpemba spectral theory and resource-theoretic Mpemba (C2-H1, abstraction 3). S016 (1.7) was the molecular-enzymatic floor.
- Novelty Type trend: **INCREASING**. S014 (2.6) -> S015 (2.5) -> S016 (2.3) -> S017 (3.0) -> S018 (3.3). S018 is the highest novelty-type average in pipeline history, reflecting new frameworks (3) and one paradigm-shift hypothesis (4: A* state = Protein Mpemba overlap coefficient).
- Strategies with primary data: **9 / 11** (network_gap_analysis, tool_repurposing, scale_bridging, recent_breakthrough_radiation, Swanson_ABC_bridging, structural_isomorphism, contradiction_mining, converging_vocabularies, **anomaly_hunting**). Untested: evolutionary_conservation_gap, dimensional_mismatch, **serendipity**.

**Creativity Assessment**: Pipeline creativity is at an all-time high on novelty type (3.3 avg in S018) and distance (2.7, tied-highest with S017). The autonomous Scout is selecting genuinely novel targets. anomaly_hunting and converging_vocabularies are both producing high-creativity output. The remaining untested strategy (serendipity) should be explored in the next 2-3 sessions.

**Recommendation**: S018 maintained pipeline at high disciplinary distance (2.7). anomaly_hunting exploration slot fulfilled. Next session should explore **serendipity** (untested) or use **converging_vocabularies** with a new formal mathematics field (Topological Data Analysis, Information Theory, Stochastic Processes). Three consecutive sessions below 2.0 distance = corrective action trigger. Current position: S016 (2.0) -> S017 (3.0) -> S018 (2.7) — no corrective action needed.

---

## Generator Technique Performance (NEW — S016 Cycle 2)

### negation_exploration: First Confirmed Top-Result Technique

**Technique**: The Generator is asked to invert the dominant-paradigm assumption in the target field. For mechano-epigenomics: "The field assumes stiffness activates writers. What if stiffness depletes erasers instead?"

**S016 Cycle 2 result**: `negation_exploration` produced C2-H6 (HDAC3-NCoR eraser depletion), which scored:
- Composite ranking: 7.4 (rank 1 in cycle 2)
- QG verdict: PASS (7.5/10)
- Novelty score: 9 — **highest novelty in the entire session (both cycles)**
- First appearance of eraser-depletion mechanism in MAGELLAN history

**Previous technique performance (cycle 2 context)**:
- `negation_exploration`: C2-H6 PASS 7.5 (novelty 9)
- `gap_targeted_generation + facet_recombination`: C2-H7 COND 5.5
- `facet_recombination + multi_level_abstraction` (E1-H3, cycle 1 evolved): PASS 7.5
- `bisociation + scale_bridging`: C2-H1 — 5.8 (did not advance)
- `scale_bridging + analogy_transfer`: C2-H3 — 6.1 (did not advance)
- `counterfactual_probing + negation`: C2-H5 — KILL (groundedness 33%)

**Key insight**: `negation_exploration` (paradigm inversion without negation of ground truth) outperformed `counterfactual_probing + negation` (which kills hypotheses by violating established evidence). The distinction is:
- **negation_exploration**: "What if the mechanism is the opposite?" — inverts the ASSUMED direction, not a confirmed fact. C2-H6 inverts writer-activation to eraser-depletion; both are physically plausible, but only one has been studied.
- **counterfactual_probing**: "What if an established fact were false?" — more likely to produce low-groundedness hypotheses (C2-H5 had groundedness 33%).

**Recommendation for Generator**: In any domain where the literature is dominated by one mechanistic direction (writer activation, receptor upregulation, kinase activation), generate at least ONE hypothesis that inverts the direction to the complementary mechanism (eraser depletion, receptor downregulation, phosphatase activation). Paradigm inversions that remain physically plausible produce the highest novelty scores in the Ranker (novelty is scored relative to existing literature, and the eraser/phosphatase/receptor-depletion direction is systematically understudied).

---

## Systematic Generator Bias Patterns (NEW — S015-S016)

### YAP-EP300 Over-Reliance in Mechanobiology x Epigenomics Sessions

**Evidence**: S015: EP300 appeared as hub in 5/5 structured hypotheses. S016: YAP-EP300 axis in 5/7 cycle 1 hypotheses (71%). In both sessions, MRTF-SRF was absent from the first generation cycle and had to be introduced by the Critic.

**Why this is a problem**: YAP-TEAD drives shared proliferation/survival enhancers (CTGF, CYR61, AMOTL1) — the same enhancer set across ALL stiff-matrix cell types. MRTF-SRF drives CArG-box enhancers (SMA, SM22, TAGLN) — a completely non-overlapping enhancer population. The two pathways respond to the SAME mechanical signal (ECM stiffness/actin tension) but produce DIFFERENT genomic outputs. Generating 5-7 YAP-centric hypotheses misses half the mechanosensory epigenomic landscape.

**Generator rules for mechano-epigenomics targets**:
- Generate AT LEAST ONE MRTF-SRF hypothesis in the first cycle.
- Generate AT LEAST ONE PIEZO1-Ca2+ pathway hypothesis (verify via Ca2+/CaM-CAMKII route only; PIEZO1-DOT1L direct interaction does NOT exist per STRING).
- Do NOT generate more than 3 YAP-centric hypotheses in a 7-hypothesis generation cycle.

### Underexplored Mechanosensory Pathways in This Domain

1. **MRTF-SRF pathway**: RhoA -> actin polymerization -> MRTF-A nuclear import -> SRF -> CArG-box enhancers. Targets non-overlapping from TEAD enhancers. Stiffness-specific MRTF-SRF enhancers = essentially unmeasured. Tsaryk 2022 (PMID 35314737) characterized shear stress MRTF-SRF enhancers; stiffness vs shear stress distinction is open.

2. **PIEZO1-Ca2+-CAMKII-EP300 cascade**: PIEZO1 -> Ca2+ influx -> calmodulin -> CAMKII -> EP300-Ser1834 phosphorylation -> increased HAT activity. Operates on faster timescale than YAP (<15 min vs 30-60 min). PIEZO1-DOT1L direct interaction does NOT exist (STRING: NOT FOUND); must route through Ca2+/CaM cascade.

3. **Hi-C under ECM stiffness**: Zero papers report Hi-C, HiChIP, or chromosome conformation capture under ECM stiffness gradient. Confirmed measurement gap. Highest novelty for loop/TAD topology hypotheses.

4. **HDAC2-Lamin A/C locus**: LMNA-HDAC2 STRING 0.690; LMNA-HDAC3 STRING 0.187. Lamin-associated deacetylase hypothesis must use HDAC2, not HDAC3.

**Recommendation for Generator and Scout**: For any future mechanobiology x epigenomics session, MRTF-SRF should be the first alternative mechanosensor considered. The strongest untested hypothesis: "ECM stiffness simultaneously activates independent MRTF-SRF (CArG-box) and YAP-TEAD (TEAD-motif) enhancer programs; do the two programs converge on shared target genes or produce distinct transcriptomes at TAD resolution?"

---

## Cross-Model Validation Patterns (Sessions 4-13)

### Session 013 New Insights

**Arithmetic verification is cross-model validation's unique contribution**:
- GPT-5.4 explicitly computed (50nm/3nm)^3 * (0.1)^-2 approximately 4.6x10^5 and identified the 4-orders-of-magnitude discrepancy in C2-H2's N_min formula. Quality Gate had flagged the formula as "unverifiable" but did not attempt the calculation. This is a distinct added value: external models run calculations that internal pipeline models decline to execute on unverifiable formulas.
- **New protocol**: When Quality Gate marks a formula as "unverifiable," cross-model validation should explicitly compute the formula and flag order-of-magnitude discrepancies.

**Species-level correction pattern**:
- S012: Gemini caught Irving-Williams dose-response inversion (mathematical)
- S013: Gemini caught MucD vs DegP species-specificity error (biological)
- S013: GPT caught OprF directionality prediction error (mechanistic)
- Pattern: Gemini catches formal/structural errors; GPT catches empirical/biological errors. Both are needed.

**Cross-hypothesis synthesis (S013 new)**:
- Gemini generated a novel mutual-information test between H1 (GMM clusters) and H4 (per-OMV cargo manifests): if both true, MI(cluster label, cargo composition) should approach the entropy of cluster assignments. This is a new experimental prediction not in any of the four original hypotheses.
- **Protocol recommendation**: Ask Gemini explicitly for cross-hypothesis logical dependencies and mutual information in each session. This generates experimental sequencing recommendations that improve resource allocation.

**Recommendation for Cross-Model Validator**:
1. Continue dual-axis evaluation (GPT empirical, Gemini structural) — confirmed productive by S013 catches.
2. When QG marks a formula "unverifiable," pass to GPT for explicit numerical computation.
3. Ask Gemini for cross-hypothesis logical dependencies — this systematically generates novel experimental sequencing.
4. Flag species-specific protein name claims for targeted GPT verification (genus assumption is unreliable).

---

## Productive Bridge Concept Patterns (updated)

1. **Published unmeasured variable bridges** (S007): When literature explicitly identifies gaps, build hypotheses around them. Highest QG scores.
2. **Thermodynamic displacement via equilibrium constants** (S008): 29-order Ksp differences provide irrefutable driving forces.
3. **Mathematical topology constraints** (S002): Poincare-Hopf theorem gives necessary predictions.
4. **Geochemical tool transfer** (S010): TST rate law, PHREEQC modeling transfer at reaction-transport level, but require independent biological constraint verification. Use as discovery heuristic, not mechanistic proof.
5. **Indirect enzymatic cascades** (S001, S006): Multi-step pathways through well-characterized intermediaries survive at ~100%.
6. **Computational/analytical tool transfer within life sciences** (S013): GMM population analysis, power analysis frameworks, differential image analysis, ML-based in situ proteomics. When source and target share specimen class (biological/aqueous), this bridge type achieves the highest composite scores in pipeline history. Requires: specimen-technique compatibility, tool range verification, species-specific protein confirmation.
7. **Physical law constraint as bridge concept** (S014): Apply a mathematical inequality (TUR, Poincare-Hopf, Landauer bound) that MUST hold for any system in Field C. The constraint cannot be violated; the hypothesis tests whether the biological system approaches or saturates the bound. This is stronger than (3) Mathematical topology constraints because it applies to dynamical systems (not just geometric arrangements) and uses directly measurable biological observables (CV, precision, noise). First demonstrated: TUR inequality bounding bacterial cell size homeostasis CV, yielding 1 PASS + 6 COND from 7 hypotheses (100% pass+cond rate for this bridge type). Key requirement: all parameters in the inequality must be independently measurable in Field C.
8. **Multi-pathway convergence on single hub protein** (S015): Use computational validation (STRING) to find a single protein with high confidence scores to BOTH Field A proteins AND Field C proteins. Then generate hypotheses exploring different upstream pathways to the hub. Produces 4-5 complementary non-redundant hypotheses from a single bridge protein. S015 demonstration: EP300 (STRING to YAP1 0.692, CAMKII 0.908, MRTFA 0.710). Five pathways -> five non-redundant hypotheses, three QG PASS.
9. **Nuclear architecture spatial selectivity filter / LAD compartmentalization** (S016 — NEW): Use LAD tier classification (cLAD/fLAD/non-LAD) as a mechanistically grounded genomic selectivity filter. Three-tier model naturally produces distinct per-tier predictions. CRISPR tethering provides causal test. Highest single-hypothesis score in S016 (8.5/10). Key: cLADs are constitutively in nuclear periphery (not mechanosensitive); fLADs near constitutive enhancers (productive target); non-LAD regions (highest basal accessibility). Lamin A/C upregulation by stiffness is well-grounded.
10. **Sequential enzymatic temporal gate** (S015-016 — NEW): Convert a Critic-identified kinetic mismatch (enzyme A arrives N hours before enzyme B) from a vulnerability into the central prediction (N-hour gap IS the testable claim). Two-phase model is biochemically forced by enzymatic epistasis (demethylation must precede acetylation because H3K27me3/H3K27ac are mutually exclusive). Each phase is independently measurable. Two related sessions, two QG PASS outcomes. Avg score ~7.6. Pattern: whenever the Critic identifies a kinetic mismatch, immediately generate the two-phase model as the primary evolution candidate.

11. **Markov spectral formalism imported from non-equilibrium physics (S018 — NEW, first primary session)**: Import a spectral formalism developed for physics anomalies (Mpemba effect: eigenmode overlap and relaxation, Klich et al. 2019 PRX) into a biology domain that independently uses the same mathematical object (protein MSMs). Bridge works because BOTH fields use discrete-time Markov chains: Mpemba theory characterizes eigenmode overlap a_k(T) = <P_Boltzmann(T)|v_k>; protein MSMs characterize misfolding pathways as slowest eigenmodes. Three working bridge variants:
   - (a) Mpemba index as aggregation propensity classifier (single-molecule MSM diagnostic)
   - (b) Zwanzig roughness asymmetry → bimodal eigenspectrum as physical basis for why amyloidogenic proteins have exploitable eigenstructure
   - (c) Eigenmode branching from thermal initial conditions → fibril polymorph selection (insulin model system)
   - **Performance**: 3 CONDITIONAL_PASS (0 outright PASS). PARTIAL health. Key weakness: all three require bridging from single-molecule eigenspectrum to multi-molecule aggregation kinetics. Addresses a genuinely unresolved biology question (why ~30 proteins form pathological amyloids out of thousands of amyloidogenic candidates). **Guideline**: For MSM spectral formalism bridges, always include an explicit upper-bound translation (k_n ≤ C × pi_competent × gamma) from single-molecule MSM properties to population-level rate constants. Without this step, CONDITIONAL_PASS is the ceiling.

**New Bridge Concept: Measurement Gap + Mature Tool (S013 synthesis)**:
The highest-performing S013 hypotheses all follow the same template: "Field A has a mature tool X that has NEVER been applied to measurement problem Y in Field C, despite Field C explicitly identifying Y as its top priority." This is stronger than pure tool repurposing because it combines (a) the tool's proven track record in adjacent problems, (b) the target field's explicit need statement, and (c) zero prior art at the intersection.
- Scout should search for "what does Field C say is its #1 unsolved measurement problem?" and then match that to tools from Field A.
- Generator should lead with the measurement gap statement before proposing the tool transfer.

---

## Domain-Specific Patterns

### Mechanobiology x Epigenomics (S015-S016)
1. **YAP-centrism anti-pattern**: YAP-TEAD is the most-cited mechanosensor but targets a SHARED (non-tissue-specific) TEAD enhancer set. At least 4 parallel mechanosensitive programs exist with distinct enhancer targets: MRTF-SRF (CArG-box, actin cytoskeleton genes), PIEZO1-Ca2+-CaMKII (Ca2+/CaM signaling), integrin-FAK direct nuclear signaling, LINC-lamin nuclear mechanics. Generator must enumerate >= 2 parallel programs per hypothesis.
2. **MRTF-SRF is the most neglected parallel program**: CArG-box (CC[AT]6GG) enhancers targeted by MRTF-SRF are activated by RhoA-F-actin within 2-6h of stiffening — FASTER than KDM6B-dependent bivalent activation. This creates a rapid-first-responder pattern (MRTF -> actin cytoskeleton genes in 2-6h) vs delayed-cell-fate program (YAP-EP300 -> SNAI1/RUNX2 in 12-24h). Both programs are mechanosensitive; neither subsumes the other.
3. **LAD spatial filter as productive bridge**: Lamin A/C upregulation by stiffness (Swift 2013, Xu 2023, Mandal 2025) creates differential accessibility across the LAD/non-LAD compartment. Stiffness-responsive enhancers predicted to concentrate in non-LAD regions. cLAD (H3K9me3) vs fLAD (H3K27me3) distinction creates testable stratified predictions.
4. **Bivalent enhancers as cell-fate gatekeepers**: ECM stiffness can resolve bivalent (H3K4me1+ H3K27me3+) developmental enhancers via KDM6B/UTX demethylation. This explains why stiff substrates drive differentiation while soft substrates maintain stemness. Generator should explicitly target bivalent enhancer maps for mechanobiology hypotheses in stem cells.
5. **No Hi-C under ECM stiffness** (confirmed gap): Zero papers report Hi-C, HiChIP, or chromosome conformation capture under ECM stiffness gradient. Highest novelty opportunity for loop/TAD topology hypotheses.
6. **PIEZO1-DOT1L direct interaction does NOT exist**: STRING score NOT FOUND. Any PIEZO1 -> chromatin route must use: PIEZO1 -> Ca2+ influx -> calmodulin -> CAMKII -> EP300-Ser1834 phosphorylation. Do NOT claim direct PIEZO1-DOT1L interaction.
7. **LMNA-HDAC2 preferred over LMNA-HDAC3**: STRING scores: LMNA-HDAC2 = 0.690; LMNA-HDAC3 = 0.187. All lamin-associated deacetylase hypotheses should use HDAC2.

---

## Unexplored High-Quality Targets (Scout deferred queue)

| Target pair | Identified in | Strategy | Scout score | Disjointness | Priority | Notes |
|---|---|---|---|---|---|---|
| ~~Mn neurotoxicity x Deinococcus Mn-antioxidant biology~~ | ~~009~~ | ~~contradiction_mining~~ | ~~7.7~~ | ~~DISJOINT~~ | ~~COMPLETED S012~~ | ~~5 CONDITIONAL_PASS. contradiction_mining validated.~~ |
| ~~Cryo-EM heterogeneity x OMV cargo sorting~~ | ~~013~~ | ~~tool_repurposing~~ | ~~8.5~~ | ~~DISJOINT~~ | ~~COMPLETED S013~~ | ~~3 PASS + 1 COND. Best single-session PASS count.~~ |
| ~~TUR x Bacterial adder model~~ | ~~014~~ | ~~converging_vocabularies~~ | ~~8.5~~ | ~~DISJOINT~~ | ~~COMPLETED S014~~ | ~~1 PASS + 6 COND. Highest survivor count (7). converging_vocabularies debut.~~ |
| **Percolation threshold x T cell infiltration in solid tumors** | **014** | **anomaly_hunting (2nd primary session)** | **8** | **DISJOINT (est.)** | **HIGH** | **Statistical physics (bond percolation, LOX collagen crosslinking as p) x tumor immunology (ECM-mediated immune exclusion). Finite-size scaling predictions for T cell MSD. Genuinely DISJOINT — no percolation-immunology papers found. Scout confidence 8, web verified. anomaly_hunting exploration slot was used for S018 (Mpemba x Amyloid); Percolation is the 2nd primary session for this strategy.** |
| FLIM-FRET biosensors x Bacterial persisters | 013 | network_gap_analysis | 8.0 | DISJOINT (est.) | **HIGH** | PubMed "FLIM persister" = 0 results. Explicit measurement gap. Scout score 8.0. Same-class tool transfer (life sciences). |
| **Acoustic filter-bank theory x Plant bioacoustics** | **014** | **serendipity** | **7** | **DISJOINT (est.)** | **HIGH** | **Acoustic engineering (matched-filter detection, parallel filter-bank) x plant bioacoustics (ultrasonic emission detection via MSL channels). Trichome resonance as acoustic pre-filter. Highly creative (distance~2.5). serendipity strategy untested — exploration value.** |
| CNT x Ferroptosis LIP dynamics | 012 | scale_bridging | — | DISJOINT | HIGH | Classical nucleation theory for ferritin-encaged ferrihydrite -> ferroptosis LIP overflow. Zero cross-field papers. Third Ferroptosis session — domain saturation risk. |
| Granular jamming x Chromatin compaction | 012, 014 | structural_isomorphism | — | DISJOINT | HIGH | Liu-Nagel phase diagram. Target Evaluator S014 gave MODIFY (4.75): replace with polymer glass transition framework, not granular matter. Needs modification before use. |
| Patch-clamp x Plant turgor sensing | 013 | tool_repurposing | 7.5 | DISJOINT (est.) | HIGH | Turgor sensing is "dark matter" of plant physiology. MSL/OSCA channels uncharacterized at turgor-relevant pressures. Tool transfer within life sciences. |
| Turing patterns x Tumor mutational burden heterogeneity | 012 | dimensional_mismatch | — | PARTIALLY_EXPLORED | MEDIUM | Core Turing-in-cancer exists (2025); specific TMB spatial application novel. |
| Optogenetics (LAPD) x Biofilm dispersal | 013 | Swanson_ABC_bridging | 7.0 | PARTIALLY_EXPLORED (risk) | MEDIUM | B-term (LAPD) already exists; therapeutic application may be partially explored. Needs literature check first. |
| AFM-SMFS x IDP condensate cohesive energy | 013 | scale_bridging | 7.5 | PARTIALLY_EXPLORED (risk) | MEDIUM | AFM nanoindentation of condensates exists; SMFS pulling from condensates may not. Needs verification. |
| EIS x Gut microbiome metabolic state | 013 | evolutionary_conservation_gap | 7.0 | DISJOINT (est.) | MEDIUM | Real-time functional monitoring gap. Same-class tool transfer (electrochemistry in both fields). |
| Circadian x Neurodegeneration | 001 | contradiction_mining | — | DISJOINT | MEDIUM | Cross-session circadian oscillation -> condensate aging. |
| Piezoelectric collagen x HSC fate decisions | 006 | contradiction_mining + dimensional_mismatch | 7/10 | DISJOINT | LOW | CRITICAL energy-scale pre-check needed. |

**Recommendation for Scout**: **Three equally strong next primary targets (S015-S016 were targeted mode — deferred queue unchanged):**
1. **Percolation x T cell infiltration (T1 from S014)**: Scout score 8, DISJOINT, anomaly_hunting strategy (untested — exploration slot value), statistical physics x tumor immunology (disciplinary distance ~2.5). This is the highest unexplored creativity target in the queue.
2. **FLIM-FRET x Bacterial persisters (T3 from S013)**: Scout score 8.0, DISJOINT, network_gap_analysis strategy (39% historical pass rate), same-class tool transfer within life sciences. Most reliable expected performance.
3. **Acoustic filter-bank x Plant bioacoustics (T2 from S014)**: Scout score 7, DISJOINT, serendipity strategy (untested — exploration slot value). Engineering x plant biology bridge.
- All three would achieve disciplinary distance >= 2.5 in the next session. After two consecutive targeted sessions (S015-S016), the autonomous Scout MUST select the next target from the deferred queue.
- Prioritize based on strategy rotation: if exploration slot needed -> Percolation (anomaly_hunting) or Acoustic filter-bank (serendipity); if high reliability needed -> FLIM-FRET (network_gap_analysis).

---

## Domain Productivity Assessment (updated)

### Confirmed High-Productivity Domains
**Geochemistry x Pharmaceutical Sciences** (S010): 33% QG pass rate. Tool_repurposing with cross-class transfer. Requires enhanced biological constraint verification.

**Metal-dependent cell death x Geochemistry** (S005, S008): 29-42% QG pass rate. Quantitative thermodynamic frameworks provide irrefutable predictions.

**Infection biology x Shared metabolites** (S006): 43% QG pass rate. Molecular infrastructure enables groundedness verification.

**Extremophile biology x Mammalian neurotoxicology** (S012): 35.7% PASS+COND rate with contradiction_mining. Framework and measurement hypotheses outperform molecule-specific hypotheses when binding affinity is weak.

**Structural biology x Microbiology (same-class tool transfer)** (S013): **75% PASS rate, 100% PASS+COND rate, avg 8.31 composite** — highest productivity of any session. Electron microscopy methodology transfers cleanly into bacterial biology because both share biological/aqueous specimens. Measurement gaps in microbiology are numerous and well-documented. Highly recommended pairing for tool_repurposing.

**Mechanobiology x Epigenomics (newly opened field)** (S015, S016): **100% QG pass+cond rate from evolved hypotheses in BOTH sessions** (3 PASS from S015; 2 PASS + 1 COND from S016). Confirmed productive due to a specific measurement gap (ECM stiffness + H3K27ac genome-wide = 1 PubMed paper). Caution: domain saturation after S015-S016. A third consecutive session requires confirmation of a new specific bridge gap (MRTF-SRF enhancers under stiffness, Hi-C under stiffness, TET-mediated CpG demethylation under stiffness).

### Caution Domains (confirmed)
**Photosynthetic symbiont stress biology** (S009): 0 PASS verdicts due to database infrastructure limitations. Viable for testing but expect CONDITIONAL_PASS ceiling.

**Cross-class tool transfer** (S010 partial caution): Geochemistry tools applied to pharmaceutical biology require extensive biological constraint verification. Not a block, but expect lower PASS rate (33% vs 75% for same-class transfer).

**Mechano-epigenomics after S015-S016**: Two consecutive sessions in same domain. A third session should only proceed with a new specific bridge gap identified.

---

## Critical Screening Rules (for Generator — updated)

Rules 1-19: [Prior rules maintained — see S010/S011/S012 versions]

20. **Tool transfer biological constraint pre-check** (S010): When applying mathematical frameworks from Field A to Field C, independently verify: all claimed molecular interactions have literature support in Field C, structural compatibility (polymer vs crystalline, matrix effects), sign of feedback mechanisms, domain-specific physics constraints.

21. **Cross-model validation integration** (S010): When structural analysis diverges from empirical plausibility by >3 points: check for autocatalytic/feedback sign errors, verify claimed interactions are not fabricated, distinguish mathematical utility from mechanistic derivation.

22. **Geochemical tool application guidelines** (S010): Use TST, PHREEQC, saturation index as mathematical structure, not mechanistic proof. Verify polymer/biological matrix effects. Present geochemical analogy as discovery heuristic, not mechanistic foundation.

23. **Front-load binding affinity checks** (S012): When bridge involves molecular complexation, retrieve Ka/Kd data BEFORE generating molecule-specific hypotheses. If Ka < 10^3 M-1, pivot to framework and measurement hypotheses.

24. **Weak-binding pivot heuristic** (S012): When quantitative binding data shows weak affinity, generate framework hypotheses and measurement transfer hypotheses rather than therapeutic or direct mechanism transfer hypotheses.

25. **Compartment topology pre-check (NEW — S013)**: Before proposing cargo transfer between cellular compartments, verify the directionality of the molecular machine and the topology of the membrane boundaries. Inner membrane vs outer membrane, inward-firing vs outward-budding, periplasmic vs cytoplasmic — these are binary kill factors. Explicitly state "Machine X fires in direction Y" and "Target compartment Z is located at position W relative to machine X."

26. **Specimen-technique compatibility check (NEW — S013)**: For technique transfer hypotheses, verify the source technique's validated specimen type (purified proteins, cell lysates, intact cells, tissue). Proposing application to a fundamentally different specimen form (e.g., whole bacteria with a purified-protein microfluidic device) = feasibility kill even if the theoretical principle is sound.

27. **Tool quantitative range check (NEW — S013)**: Retrieve the tool's validated operating range before proposing application: particle size limits for cryo-EM methods, affinity range for binding assays, concentration range for spectroscopy, resolution limits for structural methods. Specific confirmed limits: cryoDRGN validated minimum ~100 kDa (do not apply to proteins < 80 kDa). Application outside validated range = technical impossibility.

28. **Species-specific protein name confirmation (NEW — S013)**: Do NOT assume proteins/enzymes are conserved at the species level based on genus. Verify that the named protein exists and has the proposed function in the SPECIFIC model organism used in Field C. Critical example: DegP (E. coli) vs MucD (P. aeruginosa) — same HtrA-family function, different gene names. Use UniProt or organism-specific databases to confirm.

29. **Peclet number check for spatial gradient hypotheses (NEW — S014)**: Before proposing any spatial concentration gradient within a cell, compute the Peclet number: Pe = v*L/D, where v is the advection velocity, L is the cell length, D is the diffusion coefficient. For passive protein diffusion in E. coli (D~1-5 um2/s, L=2 um), Pe~0.001-0.004. Gradient equilibrates in ~0.3-4 seconds. If the biological process operates on minutes timescale and Pe << 1, the gradient is physically impossible unless an active confinement mechanism is present. Cite the confinement mechanism explicitly (cytoskeletal scaffold, reaction-diffusion coupling, membrane corraling).

30. **Independent verification of Computational Validator counting parameters (NEW — S014)**: When the Computational Validator recommends an N_eff or copy number estimate, do NOT use it without cross-checking against primary literature. Distinguish explicitly: (a) physical binding site count [cite paper, e.g., "11 DnaA boxes — McGarry 2004, Fuller 1984"], (b) events per cell cycle [state assumptions], (c) TUR parameter N_eff in the formula [state mathematical context]. Ambiguity between these propagates errors to multiple downstream hypotheses simultaneously. Upstream errors are the highest-leverage kill risk in the pipeline.

31. **Citation conclusion verification (NEW — S014)**: Verify a cited paper's MAIN CONCLUSION, not just its existence. Papers can be cited for the opposite of their actual finding (e.g., Campos 2014 proves adder mechanism but can be misread as demonstrating sizer). When grounding a claim with a citation, state the paper's key finding explicitly ("Campos 2014 shows Caulobacter uses an ADDER mechanism: constant size extension per generation, slope alpha=0 in birth-size vs added-size plot"). If the stated finding does not appear in the abstract, re-read.

32. **Internal quantitative consistency check (NEW — S014)**: If a hypothesis makes both a quantitative mechanistic prediction (f=0.007 correlation per generation) AND claims to explain an empirical observation (Susman 2025 "substantial nonlinear memory"), verify that the quantitative prediction is consistent with the empirical claim's magnitude. If they are irreconcilable without additional assumptions, the hypothesis has a logical kill vulnerability.

33. **Cell-type specificity for chromatin mark hypotheses (NEW — S015)**: When proposing histone marks (H3K27me3, H3K4me1, H3K27ac) at specific genomic loci, verify that the proposed mark state is consistent with the cell type's differentiation state. Terminally differentiated cells (lung fibroblasts) typically lack Polycomb-repressed (H3K27me3) bivalent enhancers — these are features of stem/progenitor cells. Before generating a hypothesis requiring H3K27me3 at a genomic locus in a differentiated cell, check: (a) Is there evidence for H3K27me3 at this class of loci in this specific cell type? (b) Does chromatin accessibility data (ATAC-seq) contradict the silenced assumption? If ATAC-accessible, H3K27me3-silenced is implausible.

34. **Force per element pre-check for mechanobiology (NEW — S016, MANDATORY)**: For any hypothesis proposing direct force action on a chromatin component (nucleosome, LAD tether, TAD boundary), compute: per-element force = (total ECM-transmitted force) / (number of molecular contacts). Compare to: nucleosome unwrapping threshold ~50 pN; LAD biochemical detachment requires enzymatic H3K9me2 removal (not force-driven; Sun 2020 PMID 32270037 confirms). If per-element force is below 10x the threshold, the hypothesis REQUIRES a biochemical relay (YAP nuclear translocation, Ca2+/CaM cascade, MRTF-A import, actomyosin tension -> signal cascade). Never propose direct force-on-nucleosome or direct force-on-LAD without this calculation. LINC complex total force ~10-100 pN; distributed across 100,000+ contacts = 0.001 pN per contact, always below threshold.

35. **YAP-TEAD tissue-specificity error (NEW — S016)**: Do NOT claim YAP-TEAD drives tissue-specific enhancers without specifying the co-binding lineage-restricted TF. YAP-TEAD targets CTGF, CYR61, AMOTL1 — shared proliferation/survival enhancers present across ALL stiff-matrix cell types. Tissue identity requires: MYOD (muscle), RUNX2 (bone), PPARgamma (fat), SOX2 (neural), CDX2 (intestine). YAP-TEAD produces QUANTITATIVELY GRADED activation of the SAME program, not QUALITATIVELY DIFFERENT programs. The morphogen analogy fails: morphogens produce qualitatively different cell fates at different concentrations; YAP activates more or less of the same target gene set.

36. **MRTF-SRF mandatory consideration for mechanobiology x epigenomics (NEW — S016)**: When generating hypotheses for any ECM mechanics x chromatin/epigenomics target, include at least one MRTF-SRF hypothesis. Route: RhoA -> ROCK -> actin polymerization -> G-actin sequestration decreases -> MRTF-A (MAL) released from G-actin -> MRTF-A translocates to nucleus -> binds SRF -> activates CArG-box enhancers. Targets non-overlapping from YAP-TEAD. CArG-box enhancers are the distinguishing genomic feature. Shear stress vs stiffness specificity for MRTF-SRF is an open question (Tsaryk 2022 data on shear stress; stiffness-MRTF-SRF is essentially unmeasured).

37. **BRD4 as scaffold/retention factor vs recruiter (NEW — S016)**: When proposing BRD4-EP300 interactions, default to "BRD4 scaffolds and retains active EP300 at super-enhancers" rather than "BRD4 recruits EP300 de novo." Retention is: (a) consistent with BRD4's known mitotic bookmarking role, (b) consistent with BRD4 as a reader of H4K16ac at active enhancers, (c) produces a discriminating prediction (dBET6 displaces BRD4 scaffold -> EP300 leaves; JQ1 blocks BD reading -> EP300 stays). De novo recruitment claims require evidence for a specific BRD4-CTD/EP300 direct interaction that has not been confirmed. BRD4-CTD's known confirmed partner is P-TEFb, not EP300.

38. **First-author verification for recently published papers (NEW — S018)**: When citing papers published within the past 6 months or available only as preprints, verify the FIRST AUTHOR NAME independently via a search. The journal and year may be correctly recalled from parametric memory while the author attribution is confabulated (as in S018: Avanzini PRX was actually Summer et al. PRX). State explicitly: "First author [NAME] verified via [search query]." Do NOT cite a recent paper without explicit first-author confirmation. This check is a distinct step from venue verification.

39. **Mathematical symmetry pre-check (NEW — S018, MANDATORY for spectral/matrix methods)**: Before proposing a mathematical property that requires breaking a symmetry (non-normality, irreversibility, non-stationarity, non-positive-definiteness), verify that the standard tool for the domain does NOT impose that symmetry by construction. Confirmed instances: (1) Standard protein MSMs enforce detailed balance via MLE symmetrization → normal matrices → Henrici delta(Q) = 0 always. Non-normality in protein dynamics requires non-equilibrium conditions + non-symmetrized estimators (dtram, MBAR). (2) Equilibrium statistical mechanics enforces time-reversal symmetry. (3) Standard Gaussian process regression enforces positive-definite kernels. If the standard tool imposes the symmetry you need to break, specify the non-equilibrium condition that genuinely breaks it AND the non-standard estimator that preserves the asymmetry. Without both, the hypothesis is mathematically impossible.

40. **Single-molecule → multi-molecule translation for anomaly_hunting targets (NEW — S018)**: When anomaly_hunting imports a physics formalism operating at single-molecule level into a biology that operates at population level (amyloid nucleation, gene expression, cell division), provide an explicit quantitative bridging argument. The most defensible form is an UPPER BOUND on a population-level rate constant: k_population ≤ C × [single-molecule MSM quantity]. This bound is tight when single-molecule dynamics are rate-limiting; loose when multi-molecule processes (secondary nucleation, collision kinetics) dominate. Hypotheses without this translation are structurally capped at CONDITIONAL_PASS. Template: "By [single-molecule MSM property X], the primary nucleation rate satisfies k_n ≤ C × pi_competent × gamma (from spectral gap and competent basin population). This bound is tight at low [monomer] (primary nucleation dominant); loose at high [monomer] (secondary nucleation dominant, Cohen et al. 2012)."

---

## Recommendations Summary (updated after Session 018)

**For Scout**:
1. `network_gap_analysis` remains highest-performing (39% QG pass rate). Use as reliable baseline.
2. **`tool_repurposing` HIGH-PERFORMANCE** (S013: 75% PASS rate, avg 8.31). When source and target share specimen class (life sciences), prioritize. New heuristic: search for "what is Field C's #1 unsolved measurement problem?" and match to mature tools from Field A with no prior art at the intersection.
3. **`converging_vocabularies` NEW HIGH-POTENTIAL** (S014: 87.5% PASS+COND rate, 7 survivors — highest absolute count ever). Search for field pairs where BOTH fields use the same mathematical objects (equations, inequalities, dimensionless ratios) to describe different phenomena. Physics x biology pairs are prime candidates. Prioritize cases where Field A has proven mathematical inequalities that MUST hold for any system of Field C's type. Lead with the inequality, not the mechanism.
4. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND). Regular rotation. Prioritize deep mathematical isomorphism.
5. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND). Regular rotation. Produces high-quality targets (score 8.0).
6. ABSOLUTE RULE: Prioritize DISJOINT targets. 11 consecutive DISJOINT sessions (S004-S014) confirm the advantage is real and large. Never select PARTIALLY_EXPLORED when DISJOINT alternatives exist.
7. **PARTIALLY_EXPLORED exception (NEW — S015-S016)**: PARTIALLY_EXPLORED is acceptable when (a) landmark paper defined the field < 6 months ago (NEWLY_OPENED), OR (b) the specific bridge query returns <= 2 PubMed papers. Both conditions met for mechano-epigenomics. Classification: NEWLY_OPENED_PARTIALLY_EXPLORED — treat as DISJOINT for mechanism-level hypotheses.
8. **Next priority targets (updated after S018)**:
   - **FLIM-FRET x Bacterial persisters (S013 T3, network_gap_analysis, score 8.0, DISJOINT)**: Highest reliability target (network_gap_analysis has 39% historical pass rate). Same-class tool transfer within life sciences. Scout score 8.0. Best expected performance given strategy reliability.
   - **Acoustic filter-bank x Plant bioacoustics (S014 T2, serendipity, score 7, DISJOINT)**: serendipity strategy is the last untested primary strategy. Exploration slot value. Disciplinary distance ~2.5 (engineering × plant biology).
   - **Percolation x T cell infiltration (S014 T1, anomaly_hunting, score 8, DISJOINT)**: anomaly_hunting exploration slot was fulfilled in S018. Percolation × T cell is now a primary target for a second anomaly_hunting session to build strategy performance data. Statistical physics × tumor immunology (disciplinary distance ~2.5).
   - **Mpemba × amyloid (S018 bridge revision)**: Target can be re-entered with specific brief: "translate single-molecule Mpemba eigenmode predictions to population-level nucleation rate bounds via KCV framework." If explored again, goal is to convert C2-H2 and C2-H3 COND to PASS by resolving the monomer-aggregation gap.
9. Continue building DISJOINT deferred queue. **serendipity is now the only completely untested primary strategy** — prioritize for next exploration slot.
10. **Creativity health**: Current position S016 (2.0) -> S017 (3.0) -> S018 (2.7). Pipeline is at high creativity. No corrective action needed. Novelty type trend is INCREASING (S018: 3.3 — pipeline high). Next session should maintain distance 2.5+ via serendipity (est. 2.5) or converging_vocabularies with new formal mathematics field (TDA, information theory).

**For Generator**:
1. Lead with quantitative thermodynamic bridges, mathematical necessity arguments (inequalities/bounds), or measurement gap + mature tool bridges (highest QG scores).
2. **Measurement gap template (NEW — S013)**: Lead with "Field C has identified X as its top measurement priority. No paper applies tool Y from Field A to X. This is the bridge."
3. **Physical law constraint template (NEW — S014)**: Lead with "By [Law], [observable] >= [bound]. Therefore [biological system] cannot achieve precision better than [threshold]. The novel question: does [biological system] operate near or far from this bound, and which molecular machinery determines efficiency?"
4. **Sequential temporal gate template (NEW — S015-016)**: When the Critic identifies a kinetic mismatch (enzyme A arrives N hours before enzyme B), immediately generate: "Phase 1 (0-Nh): [enzyme A] acts on accessible targets. Phase 2 (N+8-24h): [enzyme B] acts on Phase 1 products. The N-hour gap is the central prediction (measurable by KS test or ChIP-seq time series). Epistatic constraint: [biochemical reason why Phase 2 requires Phase 1]."
5. **Mechanobiology force pre-check (MANDATORY — S016)**: Before ANY hypothesis proposing direct force on chromatin, compute per-element force vs physical threshold. If below 10x threshold, use biochemical relay instead.
6. **MRTF-SRF mandatory in mechano-epigenomics (NEW — S016)**: Include at least one MRTF-SRF hypothesis in any mechanobiology x epigenomics generation cycle.
7. **BRD4 as retention scaffold not recruiter (NEW — S016)**: Frame BRD4 as maintaining active EP300 at super-enhancers (retention), not recruiting EP300 de novo. Discriminating prediction: dBET6 -> EP300 leaves; JQ1 -> EP300 stays.
8. Tool transfer bridges within life sciences: verify specimen compatibility, tool range, species-specific protein names, compartment topology.
9. **Peclet number check for spatial gradients (NEW — S014)**: Before any spatial gradient mechanism, compute Pe = v*L/D. If Pe << 1 without active confinement, abandon the gradient.
10. **Independent verification of counting parameters (NEW — S014)**: Cross-check Computational Validator N_eff against primary literature before use. Distinguish binding site count, events per cycle, and TUR parameter N_eff explicitly.
11. **Citation conclusion verification (NEW — S014)**: State the cited paper's key finding explicitly and verify it matches the claim being grounded.
12. Continue indirect enzymatic cascade emphasis (~100% survival rate).
13. **Front-load Ka/Kd checks** (S012): If bridge involves molecular complexation, retrieve binding affinity data first. If weak, pivot to framework hypotheses.
14. **Mathematical symmetry pre-check (MANDATORY — S018)**: Before proposing any mathematical property requiring symmetry-breaking, verify the standard tool does NOT enforce that symmetry by construction. Key case: standard protein MSMs enforce detailed balance → normal matrices. Non-normality requires either (a) non-equilibrium driving (Hsp70 ATPase cycling) + non-symmetrized estimators, or (b) irreversible aggregation sink states + absorbing-state Markov chain. See Generator Rule 39.
15. **Single-molecule → multi-molecule translation (MANDATORY for physics × biology bridges — S018)**: For any physics formalism applied to a biological process dominated by multi-molecule kinetics (amyloid nucleation, receptor clustering, enzyme turnover), provide an upper bound on the relevant rate constant via the single-molecule MSM property. Template: k_population ≤ C × [MSM spectral quantity]. Without this translation, CONDITIONAL_PASS is the ceiling. See Generator Rule 40.
16. **First-author verification for recent papers (NEW — S018)**: State "First author [NAME] verified via [search]" for any paper published within 6 months. Venue/year is reliably recalled; first author is hallucination-prone. See Generator Rule 38.

**For Computational Validator**:
1. **Explicit parameter labeling (NEW — S014)**: For any counting or copy number recommendation, state THREE distinct values with citations: (a) physical binding site count [cite primary paper], (b) events per cell cycle [state assumptions explicitly], (c) TUR or noise parameter N_eff [state mathematical formula context]. Conflation of these three causes multi-hypothesis error propagation in the Generator.
2. Include Peclet number check as standard verification for any spatial gradient mechanism in bridge concepts. State Pe explicitly and whether it supports or kills the gradient.
3. Verify quantitative range compatibility for any tool transfer hypothesis — size limits, affinity range, concentration range.
4. **Force per element check for mechanobiology (NEW — S016)**: For any mechanobiology bridge proposing direct force on chromatin, compute: per-element force = total ECM-transmitted force / number of molecular contacts, and compare to nucleosome unwrapping (~50 pN) and LAD detachment (enzymatic, not force-driven). If per-element force is below 10x threshold, redirect Generator to biochemical relay pathways.
5. **STRING interaction verification for mechanobiology (NEW — S016)**: Confirm key STRING scores: YAP1-EP300 (0.692), YAP1-BRD4 (0.691), LMNA-CTCF (0.654), LMNA-HDAC2 (0.690 — use HDAC2 not HDAC3; LMNA-HDAC3 = 0.187). PIEZO1-DOT1L = NOT FOUND; route must use PIEZO1 -> Ca2+/CaM -> CAMKII -> EP300.

**For Quality Gate**:
1. Enhanced scrutiny for tool transfer hypotheses — verify specimen-technique compatibility and tool quantitative range.
2. Integration of cross-model consensus findings before final verdicts.
3. **Order-of-magnitude spot-checks on numerical claims** (S013): When a formula is flagged as "unverifiable," compute order-of-magnitude estimate to detect 2+ order discrepancies.
4. **Citation conclusion verification (NEW — S014)**: Check that cited papers' MAIN CONCLUSIONS match the claims they ground, not just that the papers exist.
5. Flag species-specific protein claims for targeted verification.
6. For spatial gradient hypotheses: verify that Pe > 1 or that a confinement mechanism is cited.
7. **Hypothesis-specific QG searches find papers field-level searches miss (NEW — S015)**: When Literature Scout reports a paper as not found, try QG-stage searches with hypothesis-specific terms (protein name + context + year). S015 example: "endogenous YAP condensates actin tension fibroblast" found iScience 2024 PMID 38784009 that field-level "YAP BRD4 condensates mechanobiology" missed.
8. **Force per element check for mechanobiology (NEW — S016)**: For any mechanobiology hypothesis claiming direct force on chromatin components without a biochemical relay, require the Generator to provide the per-element force calculation. Missing calculation = CONDITIONAL_PASS until provided.

---

## Session 015 Updates (2026-03-25-targeted-002)

**Target**: Mechanobiology (ECM mechanics) x Epigenomics (enhancer regulation) [TARGETED mode]
**Disjointness**: PARTIALLY_EXPLORED — but NEWLY_OPENED (Cosgrove 2025 Science defined the field ~3 months prior)
**Performance**: 0 kills, 3/5 QG PASS (60% — highest PARTIALLY_EXPLORED result), 2 productive evolutions

### New PARTIALLY_EXPLORED subcategory: NEWLY_OPENED

S015 updates the PARTIALLY_EXPLORED row in the Disjointness table, confirmed by S016:

| Disjointness | Sessions | QG pass+cond rate | Notes |
|---|---|---|---|
| DISJOINT | S001-S014 | ~87% | Strongly preferred |
| PARTIALLY_EXPLORED (traditional — multiple prior papers) | S009 | 30% COND only | Avoid |
| **PARTIALLY_EXPLORED (newly opened — < 6 months since landmark)** | **S015, S016** | **100% in both sessions (from evolved hypotheses entering QG)** | **Viable — treat as DISJOINT for specific mechanism gaps** |

**S015-S016 heuristic**: When a recent (< 6 months) landmark paper defines a new subfield, the PARTIALLY_EXPLORED status reflects "newly opened" rather than "saturated." The specific mechanistic gaps the landmark paper leaves open are effectively DISJOINT. When Literature Scout identifies such a defining paper, classify as NEWLY_OPENED_PARTIALLY_EXPLORED and proceed — do not downgrade.

### New Bridge Type: Multi-Pathway Convergence on Single Hub Protein

Added to Bridge Type Performance table:

| Bridge Type | Session | QG Pass+Cond | Score Range | Notes |
|---|---|---|---|---|
| Multi-pathway convergence on single HAT hub | S015 | 3 PASS + 2 evolved | 7.50-7.85 | EP300 receives mechanosensory signals from Piezo1 (Ca2+, <15 min), YAP (nuclear, 30-60 min), MRTF-A (actin, 30-60 min) via distinct routes. Hub identified by STRING: EP300-BRD4 0.988, EP300-CAMK2A 0.908, EP300-MRTFA 0.710. Naturally produces non-redundant hypotheses exploring different hub inputs. |

**Hub protein architecture principle**: Use computational validation to find a single protein (high STRING scores to BOTH Field A proteins AND Field C proteins). Then generate hypotheses exploring different upstream pathways to the hub. This maximizes hypothesis density while preventing redundancy. Five complementary hypotheses from one hub (EP300) is the S015 demonstration case.

### New Screening Rule 33

33. **Cell-type specificity for chromatin mark hypotheses (NEW — S015)**: When proposing histone marks (H3K27me3, H3K4me1, H3K27ac) at specific genomic loci, verify that the proposed mark state is consistent with the cell type's differentiation state. Terminally differentiated cells (lung fibroblasts) typically lack Polycomb-repressed (H3K27me3) bivalent enhancers — these are features of stem/progenitor cells. Before generating a hypothesis requiring H3K27me3 at a genomic locus in a differentiated cell, check: (a) Is there evidence for H3K27me3 at this class of loci in this specific cell type? (b) Does chromatin accessibility data (ATAC-seq) contradict the silenced assumption? If ATAC-accessible, H3K27me3-silenced is implausible.

### Updated Creativity Metrics Table

| S015 | 2.6 | 2.0 (concrete mechanism-specific) | 2.5 (gap-filling adjacent to landmark) | targeted (NEWLY_OPENED) |
| S016 | 2.0 | 1.7 (molecular-entity level) | 2.3 (new mechanistic application) | targeted (blind, NEWLY_OPENED) |

### Recommendation Updates for Next Session (post-S016)

**Scout target queue status unchanged** — S015 and S016 were both targeted mode (user-specified). Deferred queue recommendation from S014 remains:
1. **Percolation x T cell infiltration** (anomaly_hunting, score 8, DISJOINT)
2. **FLIM-FRET x Bacterial persisters** (network_gap_analysis, score 8.0, DISJOINT)
3. **Acoustic filter-bank x Plant bioacoustics** (serendipity, score 7, DISJOINT)

**After two consecutive targeted sessions (S015-S016), the autonomous Scout MUST use the deferred queue for the next autonomous session.**

**Creativity health**: S016 disciplinary distance 2.0 (at pipeline average 2.2). Next autonomous session should achieve 2.5+. No corrective action yet, but the trend S014 (2.0) -> S015 (2.6) -> S016 (2.0) shows alternation — next session should be high.

**For Literature Scout (updated)**:
- When a recently published (< 6 months) landmark paper defines a new subfield, identify the specific mechanism gaps it leaves open. These are the most generative targets even under PARTIALLY_EXPLORED classification.
- Actively report numerical anomalies from landmark papers (percentages, unexpected trends). S015 example: "86.2% looping-independent connections" directly generated 2 of the 5 hypotheses (H5, H5e).
- Use hypothesis-specific search terms during verification (protein + context + year), not just field-level terms. This surfaces papers that field-level searches miss.

**For Cross-Model Validator**:
1. Continue dual-axis evaluation (GPT empirical, Gemini structural) — consistently catching distinct error types.
2. **Explicit arithmetic computation** (S013): When QG marks a formula as "unverifiable," compute the formula explicitly.
3. **Cross-hypothesis dependency synthesis** (S013): Ask Gemini for logical dependencies between hypotheses — generates experimental sequencing recommendations.
4. Flag species-specific protein name claims for targeted GPT verification.
5. For TUR-based hypotheses: compute whether stated TUR efficiency ratios (e.g., FtsZ/DnaA ~1840x) are arithmetic correct. GPT caught a 4-order-of-magnitude arithmetic error in S013.
6. Continue flagging divergences >3 points for sign error and fabricated claim investigation.
