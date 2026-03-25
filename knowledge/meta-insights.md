# MAGELLAN Meta-Insights (Cumulative)
Updated: 2026-03-25 after Session 014 (session-20260325-000727)
Based on 14 sessions, ~204 hypotheses generated, ~72 passed Quality Gate (PASS+COND)

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
| **converging_vocabularies** | **014 (primary)** | **1** | **15** | **10** | **1 PASS, 6 COND** | **87.5% PASS+COND at QG** | **6.81** |
| evolutionary_conservation_gap | 006 (secondary) | — | — | — | — | — | — |
| dimensional_mismatch | 006 (secondary) | — | — | — | — | — | — |

**Session 013 tool_repurposing Performance Update**: Second primary test produced **EXCEPTIONAL** results. 3 PASS + 1 COND from 4 entering hypotheses (75% PASS, 100% PASS+COND). Mean composite 8.31 — highest of any session. Key differentiator vs S010: source tool (cryo-EM structural biology) and target domain (bacterial biology) share the same specimen type (biological, aqueous). S010's geochemistry-to-pharmacology transfer required biological constraint verification that introduced kill risk.

**New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing achieves dramatically better results when source (Field A) and target (Field C) share the same specimen class (e.g., both biological/aqueous, both materials/solid-state). Cross-class transfers (materials to biology, chemistry to biology) require additional domain-specific constraint verification.

**Session 014 converging_vocabularies Performance**: First primary test produced **87.5% PASS+COND rate** (7/8 entering QG — highest raw PASS+COND rate of any session). 1 PASS + 6 COND, mean composite 6.81. Strategy: select field pairs where both fields independently developed the same mathematical vocabulary (stochastic thermodynamics TUR ↔ bacterial adder model CV statistics). Apply Field A's mathematical constraints directly to Field C's observables without analogical translation. The 7 survivors (highest absolute count in any session) show that vocabulary overlap enables dense hypothesis generation from a single bridge concept.

**New heuristic (S014): "Physical law as bridge > physical model as bridge"** — converging_vocabularies works best when Field A contributes an inequality or conservation law (TUR, Poincaré-Hopf, Landauer bound), not merely a predictive model. Laws cannot be violated; their application to Field C produces unfalsifiable lower bounds. The biological hypothesis tests whether the system approaches or saturates the bound. This eliminates the "is the analogy valid?" kill vector present in structural_isomorphism and tool_repurposing.

**Recommendation for Scout**:
1. `network_gap_analysis` remains the highest-performing measured strategy (39% QG pass rate, 3 sessions). Use as reliable baseline.
2. **`tool_repurposing` UPGRADED to high-performance strategy** (S013: 100% PASS+COND rate, avg 8.31). When source and target share specimen class, prioritize targets where the tool is mature in Field A and the measurement need is explicitly identified in Field C literature. Add to top rotation.
3. **`converging_vocabularies` NEW HIGH-POTENTIAL strategy** (S014: 87.5% PASS+COND rate, 7 survivors — highest absolute count). Search for field pairs where BOTH fields use the same mathematical objects (same equations, same dimensionless ratios, same inequality forms). Physics×biology pairs are prime candidates. Prioritize cases where Field A has proven mathematical inequalities (bounds, conservation laws) that MUST hold for any system of Field C's type.
4. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND rate). Regular rotation. Prioritize deep mathematical isomorphism (same PDEs independently derived).
5. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND rate). Regular rotation. Produces high-quality targets (score 8.0). Framework and measurement hypotheses outperform molecule-specific hypotheses when binding affinity is weak.
6. `Swanson_ABC_bridging` — first data confounded by PARTIALLY_EXPLORED. Re-test with verified DISJOINT target. Add B-term-in-Field-C literature check before disjointness assignment.
7. `recent_breakthrough_radiation` has lowest QG pass rate (13%) — use only when technique is genuinely new and biological target needs measurement tools.
8. **New heuristic (S011): "Measurement transfer > model transfer"** — hypotheses introducing new measurements into Field C outperform those transferring predictive models. Measurements are independently verifiable; models require parameter data first.
9. **New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing works best within the life sciences. Cross-domain transfers (materials/geochemistry to biology) require extra domain compatibility verification.
10. **New heuristic (S014): "Physical law as bridge > physical model as bridge"** — inequalities and conservation laws are stronger bridges than predictive models. For converging_vocabularies, identify the mathematical law in Field A (TUR inequality, Poincaré-Hopf theorem, Landauer bound) and check if Field C systems must satisfy it.

---

## Disjointness vs Outcome (all sessions)

| Disjointness | Sessions | Targets selected | Hyps survived | QG passed (PASS only) | QG CONDITIONAL | QG pass + cond rate | PASS rate |
|---|---|---|---|---|---|---|---|
| DISJOINT | 001, 002, 004, 005, 006, 007, 008, 010, 013, **014** | **11** | ~67 | ~43 PASS or COND | majority are PASS | ~87% combined | ~35-40% PASS |
| PARTIALLY_EXPLORED | 009 | 1 | 10 | 0 PASS | 3 COND | 30% COND only | 0% PASS |

**Session 013 confirms DISJOINT advantage**: DISJOINT target (score 9) with tool_repurposing produced 3 PASS + 1 COND — the best single-session PASS count in pipeline history.

**Session 014 confirms DISJOINT advantage**: DISJOINT target (score 8.5, confidence 0.96) with converging_vocabularies produced 1 PASS + 6 COND — highest absolute survivor count in pipeline history (7). PubMed verification: 0 papers bridging TUR and adder model.

**Recommendation for Scout**:
- DISJOINT preference is **STRONGLY CONFIRMED** across 11 sessions. Never select a PARTIALLY_EXPLORED target when DISJOINT alternatives exist.
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
| Geochemical tool transfer | 010 | 3 | 1 PASS, 2 FAIL | 6.23 avg | TST rate law, PHREEQC modeling. Requires biological constraint verification. |
| Indirect enzymatic cascade (multi-step) | 001, 006 | 8+ | 6+ | 7-8.5/10 | ~100% survival. More named molecules = more falsifiable. |
| Vibronic/phonon coupling | 004 | 3 | 2 | ~7.5/10 | Established physics in new protein system. |
| Quantitative thermodynamic framework (Pourbaix) | 005, 008 | 2 | 2 | 6-7.3/10 | Powerful but kinetics can override. |
| Tool transfer (PHREEQC, Pourbaix) | 005 | 1 | 1 | 7/10 | High novelty, must check biological constraints. |
| Quantitative scavenging budget | 006 | 1 | 1 | 7.5/10 | Inter-compartment signal feasibility. |
| ER-mito Ca2+ signaling at MAMs (CISD2) | 007 | 1 | 1 COND | 7/10 | Triple intersection: longevity x circadian x Fe-S. |
| Published gap extension | 009 | 3 | 0 PASS, 3 COND | 5.3-6.5/10 | Prior paper bridges B-term; hypothesis extends to stress context. |
| **Killed bridge types** | | | | | |
| Fabricated polymer interaction claims (S010) | 010 | 1 | 0 | 0 | HPMCAS-LLPS claims contradicted by NMR evidence. |
| Activation volume misapplication (S010) | 010 | 1 | 0 | 0 | Pressure kinetics invalidated by polymer matrix effects. |
| Direct electric/electromagnetic field effects | 001, 004 | 8 | 0 | 0 | Energy scale mismatch always fatal. |
| Quantum entanglement/information storage | 004 | 3 | 0 | 0 | Decoherence in biology is fatal. |
| **Mechanism fabrication: wrong compartment/topology (NEW — S013)** | **013** | **2** | **0** | **0** | **T6SS fires inward; OMVs bud outward. Topology mismatch = instant kill. OmpA gating model had zero literature support.** |
| **Equipment mismatch with specimen type (NEW — S013)** | **013** | **1** | **0** | **0** | **Microfluidic mixing-spray device designed for purified proteins incompatible with whole bacteria.** |
| **Spatial gradient (diffusion physics mismatch) (NEW — S014)** | **014** | **2** | **0** | **0** | **DnaA D~3 μm²/s equilibrates across 2 μm cell in <1s. Pe~0.002. Gradient physically impossible without active confinement.** |

**New Bridge Type: Computational/Analytical Tool Transfer within Life Sciences (Session 013)**:
- **Performance**: 3 PASS, 1 COND from 4 hypotheses (highest bridge type performance yet recorded)
- **What works**: Statistical methods (GMM/BIC), power analysis frameworks, differential image analysis, ML-based in situ identification. All have established precedent in adjacent biological domains.
- **What fails**: Tools applied to specimens outside their validated range (protein size limits for cryoDRGN), tools misapplied to wrong compartments/topology
- **Guideline**: For computational/analytical tool transfers: verify tool's validated specimen range (size, sample type) before proposing application. Benchmark on similar specimens in original domain.

**New Bridge Type: Physical Law Constraint (Session 014)**:
- **Performance**: 1 PASS, 6 COND from 7 hypotheses (100% PASS+COND rate). Best hypothesis: C2-H5 at 7.90 composite (PASS).
- **What works**: Using a mathematical inequality (TUR: CV² ≥ 2/(Σ·τ)) as a hard lower bound on biological observables. The bound cannot be violated; the hypothesis tests whether the system operates near or far from the bound. Parameters are all independently measurable. The direction of the result is FORCED by the math — unaffected by parameter uncertainty ranges.
- **What fails within this type**: Spatial gradient extensions of TUR (DnaA pole-biased firing) killed by diffusion physics (Pe~0.002). The mathematical constraint was valid but the proposed mechanism for achieving a gradient was physically impossible.
- **Guideline**: For physical law bridges: (1) State the exact inequality with parameters. (2) Compute the bound numerically with independently verified parameters. (3) Check whether the bound's direction is robust to ±order-of-magnitude parameter variation. (4) Propose experiments that test whether the biological system approaches the bound (not whether the bound holds — it always does).
- **Relationship to mathematical topology bridges (S002)**: Poincaré-Hopf theorem and TUR inequality are both physical law bridges. Both produce necessary predictions. Both survive adversarial critique. Physical law bridges are a robust bridge category.

**Recommendation for Generator**:
- **Use (highest QG scores)**: Published unmeasured variables. Thermodynamic displacement via Ksp. Mathematical necessity arguments (topology). Indirect multi-step enzymatic cascades. **Computational/analytical tool transfer within life sciences (NEW — S013, avg 8.31 composite).** **Physical law constraint bridges (NEW — S014, 100% PASS+COND rate).**
- **Use with enhanced verification**: Geochemical tool transfer — verify biological constraints, polymer/matrix effects, sign of feedback mechanisms.
- **Avoid (unconditional kills)**: Direct field effects. Fabricated polymer interactions without literature grounding. Mechanism fabrication (wrong compartment/topology). Equipment application outside validated specimen type. **Spatial gradient mechanisms without Pe > 1 or active confinement (NEW — S014).**
- **New verification rule (S013)**: For tool transfer bridges, verify: (a) specimen type compatibility, (b) tool's validated size/complexity range, (c) correct cellular compartment and topology, (d) named proteins/enzymes are confirmed for the specific model organism used.
- **New verification rule (S014)**: For spatial gradient hypotheses, compute Péclet number Pe = v·L/D. If Pe << 1, the gradient cannot persist passively. Must cite active confinement mechanism or the hypothesis is physically impossible.

---

## Kill Pattern Distribution (all sessions, updated)

| Kill Reason | Estimated count | Approx % | Sessions |
|---|---|---|---|
| Energy scale mismatch (thermal overwhelm, too weak) | 14 | 16% | 001, 004 dominant |
| Substrate/condition mismatch | 8 | 9% | 005 dominant |
| Quantitative impossibility (Km saturation, concentration gap, threshold mismatch) | 9 | 10% | 005, 007, 008 |
| **Quantitative impossibility — diffusion physics (Pe << 1, spatial gradient impossible) (NEW — S014)** | **2** | **2%** | **014 (C2-H4, E-H4)** |
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
| Autocatalytic sign error (S010) | 1 | 1% | 010 |
| Binding affinity too weak (Ka) (S012) | 3 | 3% | 012 |
| Vocabulary re-description | 2 | 2% | 002, 005 |
| **Equipment mismatch with specimen type (NEW — S013)** | **1** | **1%** | **013 (C2-H5 microfluidic device)** |
| ROS species mismatch | 1 | 1% | 009 |

**New Kill Patterns (Session 013)**:
1. **Wrong cellular topology/compartment**: T6SS fires inward through inner membrane; OMVs bud outward from outer membrane. Compartment topology mismatch is a rapid kill — verify the directionality of molecular machines before proposing cargo transfer between cellular structures.
2. **Equipment mismatch with specimen type**: Time-resolved cryo-EM microfluidic device validated for purified proteins is incompatible with whole bacterial cells. Technique transfer requires specimen-technique compatibility check, not just theoretical feasibility check.
3. **cryoDRGN minimum particle size**: Tool has a validated lower limit (~100 kDa). OmpA at 35 kDa was 3x below this limit. For tool transfer hypotheses, verify the tool's quantitative range limits.

**New Kill Patterns (Session 014)**:
4. **Spatial gradient physically impossible (diffusion physics / Péclet number)**: For any passive spatial gradient hypothesis in a cell, compute Pe = v·L/D. DnaA: D~3 μm²/s, L=2 μm → Pe~0.002. Gradient homogenizes in <1s; cell cycle operates on minutes. Gradient cannot exist without active maintenance mechanism. Pe check is now a REQUIRED pre-verification step.
5. **Citation misuse (real paper, opposite conclusion)**: Campos 2014 proves E. coli-like ADDER for Caulobacter, cited as evidence of a SIZER. The paper exists and the biology is real — but the conclusion cited is the opposite of the paper's actual finding. Check that paper's MAIN CONCLUSION matches the claimed content, not just that the paper exists.
6. **Logic kill: internal quantitative contradiction**: C2-H3 predicted near-zero WT memory (f=0.007 per-generation correlation) while claiming to explain Susman 2025's "substantial nonlinear memory" in WT E. coli. These are irreconcilable without addressing the quantitative gap. When a hypothesis both quantifies and claims to explain an empirical observation, verify the quantitative consistency.
7. **Computational phase error propagation**: Computational Validator's N_eff=20 events was misinterpreted as 20 DnaA boxes (actual: 11). The ambiguous upstream estimate contaminated 3 downstream hypotheses simultaneously. Computational Validator must explicitly distinguish physical binding site count, events per cycle, and TUR parameter N_eff with separate literature citations for each.

**Recommendation for Generator**:
1. **Compartment/topology pre-check (NEW — S013)**: Before proposing cargo transfer between compartments or organelles, verify the topology and directionality of the proposed molecular machine. Inner membrane vs outer membrane, inward-firing vs outward-budding, periplasmic vs cytoplasmic — these distinctions are binary kill factors.
2. **Specimen-technique compatibility check (NEW — S013)**: For technique transfer, verify the source technique's validated specimen type (purified proteins, cell lysates, whole cells, tissue). Mismatch = feasibility kill even if the theoretical principle is sound.
3. **Tool quantitative range check (NEW — S013)**: For tool transfer, retrieve the tool's validated operating range (particle size for cryo-EM methods, affinity range for binding assays, concentration range for spectroscopy). Proposing application outside this range = technical impossibility.
4. **Species-specific protein confirmation (NEW — S013)**: Named proteins in bridge mechanism must be confirmed for the specific model organism in Field C. P. aeruginosa uses MucD, not DegP (E. coli), as the primary HtrA-family periplasmic chaperone. Genus-level assumption of protein conservation is unreliable.
5. **Péclet number check for spatial gradient hypotheses (NEW — S014)**: Before proposing any spatial concentration gradient in a cell, compute Pe = v·L/D. If Pe << 1 (passive diffusion dominates), the gradient washes out faster than the biological process operates. Cite the active confinement mechanism explicitly or abandon the spatial gradient.
6. **Citation conclusion verification (NEW — S014)**: When citing a paper for a specific result, verify the paper's MAIN CONCLUSION — not just its existence. Papers are sometimes cited for the opposite of their conclusion. Cross-check: does the paper's abstract conclusion match the claim being grounded?
7. **Independent verification of Computational Validator counting parameters (NEW — S014)**: When Computational Validator provides N_eff or copy number recommendations, independently verify from primary literature: (a) the physical binding site count, (b) events per cycle, (c) regulatory context (RIDA, DARS, datA). Upstream parameter errors cascade into multiple hypotheses.

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

**Trend analysis (S011-S014)**:
- **Pipeline quality trajectory**: S011 (7.28) → S012 (7.1) → S013 (8.31) → S014 (6.81). The S014 dip from S013 reflects strategy switch (tool_repurposing → converging_vocabularies) rather than degradation. S013's 8.31 composite was exceptional by any standard.
- **Survivor count trend**: S011 (4) → S012 (5) → S013 (4) → S014 (7). The survivor count increasing to 7 in S014 shows the pipeline is producing more valid hypotheses per session, even if mean composite is slightly lower.
- **DISJOINT performance**: S014 continues 100% DISJOINT target selection (11 DISJOINT out of 11 primary selections since S009 course-correction). DISJOINT constraint working as designed.
- **Strategy rotation**: S012 (contradiction_mining) → S013 (tool_repurposing) → S014 (converging_vocabularies). Strategy diversification is healthy and introducing new bridge types each session.

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

### Cross-Session Creativity Trend
- Disciplinary Distance trend: **RESTORED after S013 dip**. S013 (1.5 — within-life-sciences tool_repurposing) → S014 (2.0 — physics×biology converging_vocabularies). Pipeline avg remains 2.2. No consecutive decline.
- Abstraction Level trend: **stable at 1.5-2.5**. S014 (1.7) is moderate — TUR applied at molecular-kinetic level with some formal framework comparisons (C2-H6 dual bound, C2-H1 multi-current portfolio). Consistent with physics×biology bridges using specific molecular entities.
- Novelty Type trend: **improved from S013**. S013 (2.0 — new application of known method) → S014 (2.6 — between "new application" and "new framework connecting fields"). TUR applied to adder biology is genuinely new framework connection.
- Strategies with primary data: **8 / 11** (network_gap_analysis, tool_repurposing, scale_bridging, recent_breakthrough_radiation, Swanson_ABC_bridging, structural_isomorphism, contradiction_mining, **converging_vocabularies**). 3 untested: evolutionary_conservation_gap, dimensional_mismatch, anomaly_hunting.

**Creativity Assessment**: S014's disciplinary distance (2.0) confirms the healthy S012→S013→S014 alternation pattern: S012 (2.5, high creativity) → S013 (1.5, high-quality tool transfer) → S014 (2.0, physics×biology framework). The pipeline is NOT in a creativity decline. converging_vocabularies for physics×biology pairs consistently produces distance 2.0 (physics ↔ biology) and novelty type 2.5-3.0 (new framework connecting fields). This is above the pipeline's tool_repurposing baseline and below the structural_isomorphism/contradiction_mining ceiling.

**Recommendation**: Maintain strategy rotation. Three consecutive sessions below 2.0 distance = corrective action trigger. Current position: S013 (1.5) → S014 (2.0) → next session should be 2.0-2.5. Priority candidates for next session from deferred queue: Percolation × T cell infiltration (anomaly_hunting, est. distance 2.5), FLIM-FRET × bacterial persisters (network_gap_analysis, distance 2.0), or Acoustic filter-bank × plant bioacoustics (serendipity, distance 2.5). All three would restore or maintain creativity above current level.

---

## Cross-Model Validation Patterns (Sessions 4–13)

### Session 013 New Insights

**Arithmetic verification is cross-model validation's unique contribution**:
- GPT-5.4 explicitly computed (50nm/3nm)^3 * (0.1)^-2 ≈ 4.6×10^5 and identified the 4-orders-of-magnitude discrepancy in C2-H2's N_min formula. Quality Gate had flagged the formula as "unverifiable" but did not attempt the calculation. This is a distinct added value: external models run calculations that internal pipeline models decline to execute on unverifiable formulas.
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
7. **Physical law constraint as bridge concept** (S014 — NEW): Apply a mathematical inequality (TUR, Poincaré-Hopf, Landauer bound) that MUST hold for any system in Field C. The constraint cannot be violated; the hypothesis tests whether the biological system approaches or saturates the bound. This is stronger than (3) Mathematical topology constraints because it applies to dynamical systems (not just geometric arrangements) and uses directly measurable biological observables (CV, precision, noise). First demonstrated: TUR inequality bounding bacterial cell size homeostasis CV, yielding 1 PASS + 6 COND from 7 hypotheses (100% pass+cond rate for this bridge type). Key requirement: all parameters in the inequality must be independently measurable in Field C.

**New Bridge Concept: Measurement Gap + Mature Tool (S013 synthesis)**:
The highest-performing S013 hypotheses all follow the same template: "Field A has a mature tool X that has NEVER been applied to measurement problem Y in Field C, despite Field C explicitly identifying Y as its top priority." This is stronger than pure tool repurposing because it combines (a) the tool's proven track record in adjacent problems, (b) the target field's explicit need statement, and (c) zero prior art at the intersection.
- Scout should search for "what does Field C say is its #1 unsolved measurement problem?" and then match that to tools from Field A.
- Generator should lead with the measurement gap statement before proposing the tool transfer.

---

## Unexplored High-Quality Targets (Scout deferred queue)

| Target pair | Identified in | Strategy | Scout score | Disjointness | Priority | Notes |
|---|---|---|---|---|---|---|
| ~~Mn neurotoxicity x Deinococcus Mn-antioxidant biology~~ | ~~009~~ | ~~contradiction_mining~~ | ~~7.7~~ | ~~DISJOINT~~ | ~~COMPLETED S012~~ | ~~5 CONDITIONAL_PASS. contradiction_mining validated.~~ |
| ~~Cryo-EM heterogeneity x OMV cargo sorting~~ | ~~013~~ | ~~tool_repurposing~~ | ~~8.5~~ | ~~DISJOINT~~ | ~~COMPLETED S013~~ | ~~3 PASS + 1 COND. Best single-session PASS count.~~ |
| ~~TUR x Bacterial adder model~~ | ~~014~~ | ~~converging_vocabularies~~ | ~~8.5~~ | ~~DISJOINT~~ | ~~COMPLETED S014~~ | ~~1 PASS + 6 COND. Highest survivor count (7). converging_vocabularies debut.~~ |
| **Percolation threshold x T cell infiltration in solid tumors** | **014** | **anomaly_hunting** | **8** | **DISJOINT (est.)** | **HIGH** | **Statistical physics (bond percolation, LOX collagen crosslinking as p) × tumor immunology (ECM-mediated immune exclusion). Finite-size scaling predictions for T cell MSD. Genuinely DISJOINT — no percolation-immunology papers found. Scout confidence 8, web verified.** |
| FLIM-FRET biosensors x Bacterial persisters | 013 | network_gap_analysis | 8.0 | DISJOINT (est.) | **HIGH** | PubMed "FLIM persister" = 0 results. Explicit measurement gap. Scout score 8.0. Same-class tool transfer (life sciences). |
| **Acoustic filter-bank theory x Plant bioacoustics** | **014** | **serendipity** | **7** | **DISJOINT (est.)** | **HIGH** | **Acoustic engineering (matched-filter detection, parallel filter-bank) × plant bioacoustics (ultrasonic emission detection via MSL channels). Trichome resonance as acoustic pre-filter. Highly creative (distance~2.5). serendipity strategy untested — exploration value.** |
| CNT x Ferroptosis LIP dynamics | 012 | scale_bridging | — | DISJOINT | HIGH | Classical nucleation theory for ferritin-encaged ferrihydrite → ferroptosis LIP overflow. Zero cross-field papers. Third Ferroptosis session — domain saturation risk. |
| Granular jamming x Chromatin compaction | 012, 014 | structural_isomorphism | — | DISJOINT | HIGH | Liu-Nagel phase diagram. Target Evaluator S014 gave MODIFY (4.75): replace with polymer glass transition framework, not granular matter. Needs modification before use. |
| Patch-clamp x Plant turgor sensing | 013 | tool_repurposing | 7.5 | DISJOINT (est.) | HIGH | Turgor sensing is "dark matter" of plant physiology. MSL/OSCA channels uncharacterized at turgor-relevant pressures. Tool transfer within life sciences. |
| Turing patterns x Tumor mutational burden heterogeneity | 012 | dimensional_mismatch | — | PARTIALLY_EXPLORED | MEDIUM | Core Turing-in-cancer exists (2025); specific TMB spatial application novel. |
| Optogenetics (LAPD) x Biofilm dispersal | 013 | Swanson_ABC_bridging | 7.0 | PARTIALLY_EXPLORED (risk) | MEDIUM | B-term (LAPD) already exists; therapeutic application may be partially explored. Needs literature check first. |
| AFM-SMFS x IDP condensate cohesive energy | 013 | scale_bridging | 7.5 | PARTIALLY_EXPLORED (risk) | MEDIUM | AFM nanoindentation of condensates exists; SMFS pulling from condensates may not. Needs verification. |
| EIS x Gut microbiome metabolic state | 013 | evolutionary_conservation_gap | 7.0 | DISJOINT (est.) | MEDIUM | Real-time functional monitoring gap. Same-class tool transfer (electrochemistry in both fields). |
| Circadian x Neurodegeneration | 001 | contradiction_mining | — | DISJOINT | MEDIUM | Cross-session circadian oscillation → condensate aging. |
| Piezoelectric collagen x HSC fate decisions | 006 | contradiction_mining + dimensional_mismatch | 7/10 | DISJOINT | LOW | CRITICAL energy-scale pre-check needed. |

**Recommendation for Scout**: **Three equally strong next primary targets:**
1. **Percolation × T cell infiltration (T1 from S014)**: Scout score 8, DISJOINT, anomaly_hunting strategy (untested — exploration slot value), statistical physics × tumor immunology (disciplinary distance ~2.5). This is the highest unexplored creativity target in the queue.
2. **FLIM-FRET × Bacterial persisters (T3 from S013)**: Scout score 8.0, DISJOINT, network_gap_analysis strategy (39% historical pass rate), same-class tool transfer within life sciences. Most reliable expected performance.
3. **Acoustic filter-bank × Plant bioacoustics (T2 from S014)**: Scout score 7, DISJOINT, serendipity strategy (untested — exploration slot value). Engineering × plant biology bridge. Would test two new strategies (anomaly_hunting, serendipity) in one session if selected.
- All three would maintain disciplinary distance ≥ 2.0 in the next session. Prioritize based on strategy rotation: if network_gap_analysis not used recently → FLIM-FRET; if exploration slot needed → Percolation or Acoustic filter-bank.

---

## Domain Productivity Assessment (updated)

### Confirmed High-Productivity Domains
**Geochemistry x Pharmaceutical Sciences** (S010): 33% QG pass rate. Tool_repurposing with cross-class transfer. Requires enhanced biological constraint verification.

**Metal-dependent cell death x Geochemistry** (S005, S008): 29-42% QG pass rate. Quantitative thermodynamic frameworks provide irrefutable predictions.

**Infection biology x Shared metabolites** (S006): 43% QG pass rate. Molecular infrastructure enables groundedness verification.

**Extremophile biology x Mammalian neurotoxicology** (S012): 35.7% PASS+COND rate with contradiction_mining. Framework and measurement hypotheses outperform molecule-specific hypotheses when binding affinity is weak.

**Structural biology x Microbiology (same-class tool transfer)** (S013 — NEW): **75% PASS rate, 100% PASS+COND rate, avg 8.31 composite** — highest productivity of any session. Electron microscopy methodology transfers cleanly into bacterial biology because both share biological/aqueous specimens. Measurement gaps in microbiology are numerous and well-documented. Highly recommended pairing for tool_repurposing.

### Caution Domains (confirmed)
**Photosynthetic symbiont stress biology** (S009): 0 PASS verdicts due to database infrastructure limitations. Viable for testing but expect CONDITIONAL_PASS ceiling.

**Cross-class tool transfer** (S010 partial caution): Geochemistry tools applied to pharmaceutical biology require extensive biological constraint verification. Not a block, but expect lower PASS rate (33% vs 75% for same-class transfer).

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

29. **Péclet number check for spatial gradient hypotheses (NEW — S014)**: Before proposing any spatial concentration gradient within a cell, compute the Péclet number: Pe = v·L/D, where v is the advection velocity, L is the cell length, D is the diffusion coefficient. For passive protein diffusion in E. coli (D~1-5 μm²/s, L=2 μm), Pe~0.001-0.004. Gradient equilibrates in ~0.3-4 seconds. If the biological process operates on minutes timescale and Pe << 1, the gradient is physically impossible unless an active confinement mechanism is present. Cite the confinement mechanism explicitly (cytoskeletal scaffold, reaction-diffusion coupling, membrane corraling).

30. **Independent verification of Computational Validator counting parameters (NEW — S014)**: When the Computational Validator recommends an N_eff or copy number estimate, do NOT use it without cross-checking against primary literature. Distinguish explicitly: (a) physical binding site count [cite paper, e.g., "11 DnaA boxes — McGarry 2004, Fuller 1984"], (b) events per cell cycle [state assumptions], (c) TUR parameter N_eff in the formula [state mathematical context]. Ambiguity between these propagates errors to multiple downstream hypotheses simultaneously. Upstream errors are the highest-leverage kill risk in the pipeline.

31. **Citation conclusion verification (NEW — S014)**: Verify a cited paper's MAIN CONCLUSION, not just its existence. Papers can be cited for the opposite of their actual finding (e.g., Campos 2014 proves adder mechanism but can be misread as demonstrating sizer). When grounding a claim with a citation, state the paper's key finding explicitly ("Campos 2014 shows Caulobacter uses an ADDER mechanism: constant size extension per generation, slope α=0 in birth-size vs added-size plot"). If the stated finding does not appear in the abstract, re-read.

32. **Internal quantitative consistency check (NEW — S014)**: If a hypothesis makes both a quantitative mechanistic prediction (f=0.007 correlation per generation) AND claims to explain an empirical observation (Susman 2025 "substantial nonlinear memory"), verify that the quantitative prediction is consistent with the empirical claim's magnitude. If they are irreconcilable without additional assumptions, the hypothesis has a logical kill vulnerability.

---

## Recommendations Summary (updated after Session 014)

**For Scout**:
1. `network_gap_analysis` remains highest-performing (39% QG pass rate). Use as reliable baseline.
2. **`tool_repurposing` HIGH-PERFORMANCE** (S013: 75% PASS rate, avg 8.31). When source and target share specimen class (life sciences), prioritize. New heuristic: search for "what is Field C's #1 unsolved measurement problem?" and match to mature tools from Field A with no prior art at the intersection.
3. **`converging_vocabularies` NEW HIGH-POTENTIAL** (S014: 87.5% PASS+COND rate, 7 survivors — highest absolute count ever). Search for field pairs where BOTH fields use the same mathematical objects (equations, inequalities, dimensionless ratios) to describe different phenomena. Physics×biology pairs are prime candidates. Prioritize cases where Field A has proven mathematical inequalities that MUST hold for any system of Field C's type. Lead with the inequality, not the mechanism.
4. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND). Regular rotation. Prioritize deep mathematical isomorphism.
5. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND). Regular rotation. Produces high-quality targets (score 8.0).
6. ABSOLUTE RULE: Prioritize DISJOINT targets. 11 consecutive DISJOINT sessions (S004-S014) confirm the advantage is real and large. Never select PARTIALLY_EXPLORED when DISJOINT alternatives exist.
7. **Next priority targets (updated)**: Percolation × T cell infiltration (S014 T1, anomaly_hunting, score 8, DISJOINT), FLIM-FRET × Bacterial persisters (S013 T3, network_gap_analysis, score 8.0, DISJOINT), Acoustic filter-bank × Plant bioacoustics (S014 T2, serendipity, score 7, DISJOINT).
8. Continue building DISJOINT deferred queue. Test anomaly_hunting and serendipity strategies — both untested with primary data.
9. **Creativity health**: Alternate between high-creativity strategies (structural_isomorphism, contradiction_mining, converging_vocabularies — avg distance 2.0-2.5) and high-quality tool transfer strategies (tool_repurposing, network_gap_analysis — avg distance 1.5-2.0). Three consecutive sessions below 2.0 = corrective action.

**For Generator**:
1. Lead with quantitative thermodynamic bridges, mathematical necessity arguments (inequalities/bounds), or measurement gap + mature tool bridges (highest QG scores).
2. **Measurement gap template (NEW — S013)**: Lead with "Field C has identified X as its top measurement priority. No paper applies tool Y from Field A to X. This is the bridge."
3. **Physical law constraint template (NEW — S014)**: Lead with "By [Law], [observable] ≥ [bound]. Therefore [biological system] cannot achieve precision better than [threshold]. The novel question: does [biological system] operate near or far from this bound, and which molecular machinery determines efficiency?"
4. Tool transfer bridges within life sciences: verify specimen compatibility, tool range, species-specific protein names, compartment topology.
5. **Péclet number check for spatial gradients (NEW — S014)**: Before any spatial gradient mechanism, compute Pe = v·L/D. If Pe << 1 without active confinement, abandon the gradient.
6. **Independent verification of counting parameters (NEW — S014)**: Cross-check Computational Validator N_eff against primary literature before use. Distinguish binding site count, events per cycle, and TUR parameter N_eff explicitly.
7. **Citation conclusion verification (NEW — S014)**: State the cited paper's key finding explicitly and verify it matches the claim being grounded.
8. Continue indirect enzymatic cascade emphasis (~100% survival rate).
9. **Front-load Ka/Kd checks** (S012): If bridge involves molecular complexation, retrieve binding affinity data first. If weak, pivot to framework hypotheses.

**For Computational Validator**:
1. **Explicit parameter labeling (NEW — S014)**: For any counting or copy number recommendation, state THREE distinct values with citations: (a) physical binding site count [cite primary paper], (b) events per cell cycle [state assumptions explicitly], (c) TUR or noise parameter N_eff [state mathematical formula context]. Conflation of these three causes multi-hypothesis error propagation in the Generator.
2. Include Péclet number check as standard verification for any spatial gradient mechanism in bridge concepts. State Pe explicitly and whether it supports or kills the gradient.
3. Verify quantitative range compatibility for any tool transfer hypothesis — size limits, affinity range, concentration range.

**For Quality Gate**:
1. Enhanced scrutiny for tool transfer hypotheses — verify specimen-technique compatibility and tool quantitative range.
2. Integration of cross-model consensus findings before final verdicts.
3. **Order-of-magnitude spot-checks on numerical claims** (S013): When a formula is flagged as "unverifiable," compute order-of-magnitude estimate to detect 2+ order discrepancies.
4. **Citation conclusion verification (NEW — S014)**: Check that cited papers' MAIN CONCLUSIONS match the claims they ground, not just that the papers exist.
5. Flag species-specific protein claims for targeted verification.
6. For spatial gradient hypotheses: verify that Pe > 1 or that a confinement mechanism is cited.

**For Cross-Model Validator**:
1. Continue dual-axis evaluation (GPT empirical, Gemini structural) — consistently catching distinct error types.
2. **Explicit arithmetic computation** (S013): When QG marks a formula as "unverifiable," compute the formula explicitly.
3. **Cross-hypothesis dependency synthesis** (S013): Ask Gemini for logical dependencies between hypotheses — generates experimental sequencing recommendations.
4. Flag species-specific protein name claims for targeted GPT verification.
5. For TUR-based hypotheses: compute whether stated TUR efficiency ratios (e.g., FtsZ/DnaA ~1840×) are arithmetic correct. GPT caught a 4-order-of-magnitude arithmetic error in S013.
6. Continue flagging divergences >3 points for sign error and fabricated claim investigation.
