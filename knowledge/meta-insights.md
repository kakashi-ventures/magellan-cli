# MAGELLAN Meta-Insights (Cumulative)
Updated: 2026-03-24 after Session 013 (session-20260324-200851)
Based on 13 sessions, ~189 hypotheses generated, ~65 passed Quality Gate (PASS+COND)

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
| evolutionary_conservation_gap | 006 (secondary) | — | — | — | — | — | — |
| dimensional_mismatch | 006 (secondary) | — | — | — | — | — | — |

**Session 013 tool_repurposing Performance Update**: Second primary test produced **EXCEPTIONAL** results. 3 PASS + 1 COND from 4 entering hypotheses (75% PASS, 100% PASS+COND). Mean composite 8.31 — highest of any session. Key differentiator vs S010: source tool (cryo-EM structural biology) and target domain (bacterial biology) share the same specimen type (biological, aqueous). S010's geochemistry-to-pharmacology transfer required biological constraint verification that introduced kill risk.

**New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing achieves dramatically better results when source (Field A) and target (Field C) share the same specimen class (e.g., both biological/aqueous, both materials/solid-state). Cross-class transfers (materials to biology, chemistry to biology) require additional domain-specific constraint verification.

**Recommendation for Scout**:
1. `network_gap_analysis` remains the highest-performing measured strategy (39% QG pass rate, 3 sessions). Use as reliable baseline.
2. **`tool_repurposing` UPGRADED to high-performance strategy** (S013: 100% PASS+COND rate, avg 8.31). When source and target share specimen class, prioritize targets where the tool is mature in Field A and the measurement need is explicitly identified in Field C literature. Add to top rotation.
3. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND rate). Regular rotation. Prioritize deep mathematical isomorphism (same PDEs independently derived).
4. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND rate). Regular rotation. Produces high-quality targets (score 8.0). Framework and measurement hypotheses outperform molecule-specific hypotheses when binding affinity is weak.
5. `Swanson_ABC_bridging` — first data confounded by PARTIALLY_EXPLORED. Re-test with verified DISJOINT target. Add B-term-in-Field-C literature check before disjointness assignment.
6. `recent_breakthrough_radiation` has lowest QG pass rate (13%) — use only when technique is genuinely new and biological target needs measurement tools.
7. **New heuristic (S011): "Measurement transfer > model transfer"** — hypotheses introducing new measurements into Field C outperform those transferring predictive models. Measurements are independently verifiable; models require parameter data first.
8. **New heuristic (S013): "Same-class tool transfer > cross-class tool transfer"** — tool_repurposing works best within the life sciences. Cross-domain transfers (materials/geochemistry to biology) require extra domain compatibility verification.

---

## Disjointness vs Outcome (all sessions)

| Disjointness | Sessions | Targets selected | Hyps survived | QG passed (PASS only) | QG CONDITIONAL | QG pass + cond rate | PASS rate |
|---|---|---|---|---|---|---|---|
| DISJOINT | 001, 002, 004, 005, 006, 007, 008, 010, **013** | **10** | ~57 | ~42 PASS or COND | majority are PASS | ~86% combined | ~37-40% PASS |
| PARTIALLY_EXPLORED | 009 | 1 | 10 | 0 PASS | 3 COND | 30% COND only | 0% PASS |

**Session 013 confirms DISJOINT advantage**: DISJOINT target (score 9) with tool_repurposing produced 3 PASS + 1 COND — the best single-session PASS count in pipeline history.

**Recommendation for Scout**:
- DISJOINT preference is **STRONGLY CONFIRMED** across 10 sessions. Never select a PARTIALLY_EXPLORED target when DISJOINT alternatives exist.
- S013's DISJOINT score of 9 (from Literature Scout verification: 3 DISJOINT, 2 PARTIALLY_EXPLORED, 1 WELL_EXPLORED) produced optimal results. Continue building DISJOINT deferred target queue.
- The Literature Scout's explicit disjointness verification step is critical — Scout's pre-estimate matched the outcome in S013.

---

## Bridge Type Performance (all sessions)

| Bridge Type | Sessions | Used | QG Passed | QG Score Range | Notes |
|---|---|---|---|---|---|
| Published unmeasured variable (gap paper) | 007 | 1 | 1 PASS | 8/10 | Highest quality — gap explicitly stated. Pre-grounded. |
| Thermodynamic displacement (Ksp/Irving-Williams) | 008 | 1 | 1 PASS | 8.1/10 | 29-order Ksp driving force. Quantitative irrefutable. |
| Mathematical topology constraints | 002 | 3 | 3 | ~8/10 | Poincare-Hopf gives necessary predictions. |
| **Computational/analytical tool transfer (life sciences) (NEW — S013)** | **013** | **4** | **3 PASS, 1 COND** | **8.15-8.55** | **GMM, power analysis, difference mapping, ML template matching. Highest avg score of any bridge type.** |
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

**New Bridge Type: Computational/Analytical Tool Transfer within Life Sciences (Session 013)**:
- **Performance**: 3 PASS, 1 COND from 4 hypotheses (highest bridge type performance yet recorded)
- **What works**: Statistical methods (GMM/BIC), power analysis frameworks, differential image analysis, ML-based in situ identification. All have established precedent in adjacent biological domains.
- **What fails**: Tools applied to specimens outside their validated range (protein size limits for cryoDRGN), tools misapplied to wrong compartments/topology
- **Guideline**: For computational/analytical tool transfers: verify tool's validated specimen range (size, sample type) before proposing application. Benchmark on similar specimens in original domain.

**Recommendation for Generator**:
- **Use (highest QG scores)**: Published unmeasured variables. Thermodynamic displacement via Ksp. Mathematical necessity arguments (topology). Indirect multi-step enzymatic cascades. **Computational/analytical tool transfer within life sciences (NEW — S013, avg 8.31 composite).**
- **Use with enhanced verification**: Geochemical tool transfer — verify biological constraints, polymer/matrix effects, sign of feedback mechanisms.
- **Avoid (unconditional kills)**: Direct field effects. Fabricated polymer interactions without literature grounding. Mechanism fabrication (wrong compartment/topology). Equipment application outside validated specimen type.
- **New verification rule (S013)**: For tool transfer bridges, verify: (a) specimen type compatibility, (b) tool's validated size/complexity range, (c) correct cellular compartment and topology, (d) named proteins/enzymes are confirmed for the specific model organism used.

---

## Kill Pattern Distribution (all sessions, updated)

| Kill Reason | Estimated count | Approx % | Sessions |
|---|---|---|---|
| Energy scale mismatch (thermal overwhelm, too weak) | 14 | 18% | 001, 004 dominant |
| Substrate/condition mismatch | 8 | 10% | 005 dominant |
| Quantitative impossibility (Km saturation, concentration gap, threshold mismatch) | 9 | 12% | 005, 007, 008 |
| Classical explanation sufficiency | 6 | 8% | 001, 002, 004 |
| **Mechanism fabrication: wrong compartment or topology (NEW — S013)** | **7** | **9%** | **001 (indirect), 013 (T6SS topology, OmpA function)** |
| Fabricated interaction claims (S010) | 2 | 3% | 010 |
| Mechanism fabrication (no known receptor/enzyme/pathway) | 5 | 6% | 002, 006 |
| Thermodynamic impossibility (wrong redox, wrong pH) | 4 | 5% | 007, 005 |
| Citation hallucination / unverifiable reference | 3 | 4% | 004 |
| Mathematical invalidity | 3 | 4% | 002 |
| Scope overreach / universal claim | 3 | 4% | 002 |
| Novelty failure (well-studied in adjacent domain) | 2 | 3% | 008 |
| Autocatalytic sign error (S010) | 1 | 1% | 010 |
| Binding affinity too weak (Ka) (S012) | 3 | 4% | 012 |
| Vocabulary re-description | 2 | 3% | 002, 005 |
| **Equipment mismatch with specimen type (NEW — S013)** | **1** | **1%** | **013 (C2-H5 microfluidic device)** |
| ROS species mismatch | 1 | 1% | 009 |

**New Kill Patterns (Session 013)**:
1. **Wrong cellular topology/compartment**: T6SS fires inward through inner membrane; OMVs bud outward from outer membrane. Compartment topology mismatch is a rapid kill — verify the directionality of molecular machines before proposing cargo transfer between cellular structures.
2. **Equipment mismatch with specimen type**: Time-resolved cryo-EM microfluidic device validated for purified proteins is incompatible with whole bacterial cells. Technique transfer requires specimen-technique compatibility check, not just theoretical feasibility check.
3. **cryoDRGN minimum particle size**: Tool has a validated lower limit (~100 kDa). OmpA at 35 kDa was 3x below this limit. For tool transfer hypotheses, verify the tool's quantitative range limits.

**Recommendation for Generator**:
1. **Compartment/topology pre-check (NEW — S013)**: Before proposing cargo transfer between compartments or organelles, verify the topology and directionality of the proposed molecular machine. Inner membrane vs outer membrane, inward-firing vs outward-budding, periplasmic vs cytoplasmic — these distinctions are binary kill factors.
2. **Specimen-technique compatibility check (NEW — S013)**: For technique transfer, verify the source technique's validated specimen type (purified proteins, cell lysates, whole cells, tissue). Mismatch = feasibility kill even if the theoretical principle is sound.
3. **Tool quantitative range check (NEW — S013)**: For tool transfer, retrieve the tool's validated operating range (particle size for cryo-EM methods, affinity range for binding assays, concentration range for spectroscopy). Proposing application outside this range = technical impossibility.
4. **Species-specific protein confirmation (NEW — S013)**: Named proteins in bridge mechanism must be confirmed for the specific model organism in Field C. P. aeruginosa uses MucD, not DegP (E. coli), as the primary HtrA-family periplasmic chaperone. Genus-level assumption of protein conservation is unreliable.

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
| **013** | **Cryo-EM heterogeneity x OMV cargo sorting** | **11** | **27.3%** | **3 PASS, 1 COND** | **3** | **8.31** | **SKIPPED** | **SUCCESS** |

**Session 013 Analysis**:
- **Best QG PASS count ever**: 3 PASS verdicts from 4 entering hypotheses. Previous record was S001, S006 at 4+ but with many CONDITIONAL. S013 achieved 75% outright PASS rate.
- **Highest mean composite**: 8.31 — surpassing S001 (~7.5) which previously held the record. This reflects well-grounded, technically specific hypotheses where all 4 claims were verified.
- **Zero fabricated claims found**: Quality Gate reported 0 citation hallucinations, 0 fabricated claims, 0 mechanism errors (only 1 citation error in journal name, 1 unverifiable formula in C2-H2). This is the lowest error rate in pipeline history.
- **Evolver correctly skipped**: Cycle 2 top-3 composite >= 6.5 triggered skip condition. Given the high baseline quality, evolution was unnecessary.
- **Kill rate**: 27.3% (healthy range, two structurally sound kills in C1, one feasibility kill in C2).

**Trend analysis**:
- **Pipeline quality improving**: S011 (7.28) → S012 (7.1) → S013 (8.31). The increasing trend in PASS rate and composite scores after S009's PARTIALLY_EXPLORED anomaly suggests the pipeline is learning to select better targets.
- **DISJOINT + same-class tool transfer**: The combination of a high-disjointness target (score 9) and a tool transfer where source and target share specimen class produced the best session outcome to date.
- **Cross-model validation maturing**: S013 cross-model validation caught arithmetic error (GPT), species correction (Gemini), and produced a novel cross-hypothesis synthesis (H1-H4 duality). The value of cross-model validation is accelerating.

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
| **013** | **1.5** | **1.5** | **2.0** | **tool_repurposing** |

### Cross-Session Creativity Trend
- Disciplinary Distance trend: **S013 is the first session to drop to 1.5 (below baseline)**. All prior sessions averaged 2.0-2.5. This reflects tool_repurposing applied within-life-sciences (1-2 disciplinary boundaries vs the 2-3 boundaries characteristic of geochemistry↔biology or physics↔biology bridges).
- Abstraction Level trend: **stable at 1.5-2.5**. S013 (1.5) is on the lower end, consistent with tool transfer hypotheses that operate at the molecular/measurement level rather than formal frameworks.
- Novelty Type trend: **stable at 2.0-2.5**. S013 (2.0) is Novelty Type 2 (new application of known method to new domain). This is appropriate and high-value for tool_repurposing sessions.
- Strategies with primary data: **7 / 10** (network_gap_analysis, tool_repurposing, scale_bridging, recent_breakthrough_radiation, Swanson_ABC_bridging, structural_isomorphism, contradiction_mining).

**Creativity Assessment**: S013's lower disciplinary distance (1.5 vs pipeline avg 2.2) is a FEATURE of the tool_repurposing strategy when applied within the life sciences, not a sign of pipeline degradation. The appropriate concern would be if multiple CONSECUTIVE sessions showed declining creativity. Since S012 (structural_isomorphism/contradiction_mining) scored 2.5/2.0/2.5, the pipeline is alternating between high-creativity conceptual sessions and high-quality technique transfer sessions. This diversity is healthy.

**Recommendation**: Maintain strategy rotation between: (a) high-creativity strategies (structural_isomorphism, contradiction_mining, Swanson_ABC_bridging — avg distance 2.5) and (b) high-quality tool transfer strategies (tool_repurposing, network_gap_analysis — avg distance 1.5-2.0). If three consecutive sessions show distance < 2.0, flag for corrective action. Current position (S013 after S012 high-creativity) is expected pattern, not degradation.

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
6. **Computational/analytical tool transfer within life sciences** (S013 — NEW): GMM population analysis, power analysis frameworks, differential image analysis, ML-based in situ proteomics. When source and target share specimen class (biological/aqueous), this bridge type achieves the highest composite scores in pipeline history. Requires: specimen-technique compatibility, tool range verification, species-specific protein confirmation.

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
| CNT x Ferroptosis LIP dynamics | 012 | scale_bridging | — | DISJOINT | **HIGH** | Classical nucleation theory for ferritin-encaged ferrihydrite → ferroptosis LIP overflow. Zero cross-field papers. |
| Granular jamming x Chromatin compaction | 012 | structural_isomorphism | — | DISJOINT | **HIGH** | Liu-Nagel phase diagram, Edwards entropy. Zero cross-field papers. |
| **FLIM-FRET biosensors x Bacterial persisters** | **013** | **network_gap_analysis** | **8.0** | **DISJOINT (est.)** | **HIGH** | **PubMed "FLIM persister" = 0 results. Explicit measurement gap. Scout score 8.0. Same-class tool transfer (life sciences).** |
| **Patch-clamp x Plant turgor sensing** | **013** | **tool_repurposing** | **7.5** | **DISJOINT (est.)** | **HIGH** | **Turgor sensing is "dark matter" of plant physiology. MSL/OSCA channels uncharacterized at turgor-relevant pressures. Tool transfer within life sciences.** |
| Turing patterns x Tumor mutational burden heterogeneity | 012 | dimensional_mismatch | — | PARTIALLY_EXPLORED | MEDIUM | Core Turing-in-cancer exists (2025); specific TMB spatial application novel. |
| Optogenetics (LAPD) x Biofilm dispersal | 013 | Swanson_ABC_bridging | 7.0 | PARTIALLY_EXPLORED (risk) | MEDIUM | B-term (LAPD) already exists; therapeutic application may be partially explored. Needs literature check first. |
| AFM-SMFS x IDP condensate cohesive energy | 013 | scale_bridging | 7.5 | PARTIALLY_EXPLORED (risk) | MEDIUM | AFM nanoindentation of condensates exists; SMFS pulling from condensates may not. Needs verification. |
| EIS x Gut microbiome metabolic state | 013 | evolutionary_conservation_gap | 7.0 | DISJOINT (est.) | MEDIUM | Real-time functional monitoring gap. Same-class tool transfer (electrochemistry in both fields). |
| Circadian x Neurodegeneration | 001 | contradiction_mining | — | DISJOINT | MEDIUM | Cross-session circadian oscillation → condensate aging. |
| Piezoelectric collagen x HSC fate decisions | 006 | contradiction_mining + dimensional_mismatch | 7/10 | DISJOINT | LOW | CRITICAL energy-scale pre-check needed. |

**Recommendation for Scout**: **Prioritize FLIM-FRET x Bacterial persisters (T3 from S013) or CNT x Ferroptosis LIP (T3 from S012) as next primary targets.**
- FLIM-FRET x Persisters: Scout score 8.0, DISJOINT, network_gap_analysis strategy (39% historical pass rate), same-class tool transfer within life sciences (highest-performing S013 bridge type), PubMed gap verified.
- CNT x Ferroptosis LIP: DISJOINT with zero cross-field papers, scale_bridging strategy (29% pass rate), tests physical → biological tool transfer.

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

---

## Recommendations Summary (updated after Session 013)

**For Scout**:
1. `network_gap_analysis` remains highest-performing (39% QG pass rate). Use as reliable baseline.
2. **`tool_repurposing` UPGRADED** (S013: 75% PASS rate, avg 8.31). When source and target share specimen class (life sciences), prioritize this strategy. New heuristic: search for "what is Field C's #1 unsolved measurement problem?" and match to mature tools from Field A with no prior art at the intersection.
3. `structural_isomorphism` VALIDATED (S011, 50% PASS+COND). Regular rotation. Prioritize deep mathematical isomorphism.
4. `contradiction_mining` VALIDATED (S012, 35.7% PASS+COND). Regular rotation. Produces high-quality targets (score 8.0).
5. ABSOLUTE RULE: Prioritize DISJOINT targets. S013 confirms DISJOINT + same-class tool transfer = optimal combination.
6. **Next priority targets**: FLIM-FRET x Bacterial persisters (S013 deferred, network_gap_analysis, score 8.0, DISJOINT) and CNT x Ferroptosis LIP (S012 deferred, scale_bridging, DISJOINT).
7. Continue building DISJOINT deferred queue.
8. **Creativity health**: Alternate between high-creativity sessions (structural_isomorphism, contradiction_mining) and high-quality tool transfer sessions (tool_repurposing, network_gap_analysis). Three consecutive sessions with avg disciplinary distance < 2.0 = flag for corrective action.

**For Generator**:
1. Lead with quantitative thermodynamic bridges or measurement gap + mature tool bridges (highest QG scores).
2. **Measurement gap template (NEW — S013)**: Lead with "Field C has identified X as its top measurement priority. No paper applies tool Y from Field A to X. This is the bridge." This framing anchors every claim in an explicit literature need.
3. Tool transfer bridges within life sciences: verify specimen compatibility, tool range, species-specific protein names, compartment topology.
4. Cross-class tool transfer (geochemistry/materials → biology): use mathematical structure as heuristic, verify biological constraints independently.
5. Continue indirect enzymatic cascade emphasis (~100% survival rate).
6. **Front-load Ka/Kd checks** (S012): When bridge involves molecular complexation, retrieve binding affinity data before hypothesis generation. If weak, pivot to framework and measurement hypotheses.
7. **Species-specific protein confirmation** (S013): Named proteins must be confirmed for specific model organism. Use UniProt species filter.
8. **Compartment topology verification** (S013): State machine directionality and compartment position explicitly. Topology mismatch = instant kill.

**For Quality Gate**:
1. Enhanced scrutiny for tool transfer hypotheses — verify specimen-technique compatibility and tool quantitative range.
2. Integration of cross-model consensus findings before final verdicts.
3. **Attempt order-of-magnitude spot-checks on numerical claims** (NEW — S013): When a formula is flagged as "unverifiable," compute an order-of-magnitude estimate to detect 2+ orders of magnitude discrepancies. Do not require exact derivation — just flag if the stated numerical result is grossly inconsistent with the formula structure.
4. Flag species-specific protein claims for targeted verification (genus-level assumption unreliable).

**For Cross-Model Validator**:
1. Continue dual-axis evaluation (GPT empirical, Gemini structural) — consistently catching distinct error types.
2. **Explicit arithmetic computation** (NEW — S013): When QG marks a formula as "unverifiable," compute the formula explicitly and report whether the stated numerical result is consistent.
3. **Cross-hypothesis dependency synthesis** (NEW — S013): Ask Gemini explicitly for logical dependencies between hypotheses (if H_i is true, what does it imply for H_j?). Report as experimental sequencing recommendation.
4. Flag species-specific protein name claims for GPT verification.
5. Continue flagging divergences >3 points for sign error and fabricated claim investigation.
