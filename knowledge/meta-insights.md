# MAGELLAN Meta-Insights (Cumulative)
Updated: 2026-03-22 after Session 009
Based on 9 sessions, ~129 hypotheses generated, ~46 passed Quality Gate

---

## Strategy Performance (all sessions)

| Strategy | Sessions | Targets produced | Hyps generated | Survived critique | Passed QG | QG pass rate | Avg QG composite |
|---|---|---|---|---|---|---|---|
| network_gap_analysis | 006, 007, 008 | 3 | 41 | 25 | 16 | 39% | 6.92 |
| scale_bridging | 005 | 1 | 14 | 8 | 4 | 29% | 6.75 |
| recent_breakthrough_radiation | 004 | 1 | 15 | 5 | 2 | 13% | ~6.0 |
| implicit_disjoint (sessions 001-002) | 001, 002 | 2 | ~20 | ~7 | ~7 | ~35% | ~7.0 |
| Swanson_ABC_bridging | 009 (primary) | 1 | 10 | 10 | 0 PASS, 3 COND | 0% PASS, 30% COND | 5.87 |
| contradiction_mining | 006 (secondary), 009 (secondary) | — | — | — | — | — | — |
| tool_repurposing | 009 (secondary, not selected) | — | — | — | — | — | — |
| evolutionary_conservation_gap | 006 (secondary) | — | — | — | — | — | — |
| dimensional_mismatch | 006 (secondary) | — | — | — | — | — | — |

**IMPORTANT CAVEAT on Session 009 Swanson_ABC_bridging**: The session selected a PARTIALLY_EXPLORED target (Roopin 2013 directly bridges melatonin to Symbiodinium). S009's poor QG performance may reflect disjointness quality, not strategy quality. Swanson_ABC_bridging should be re-tested with a verified DISJOINT target before final ranking.

**Recommendation for Scout**:
1. `network_gap_analysis` remains the highest-performing measured strategy (39% QG pass rate, 3 sessions). Use as the reliable baseline when no strong alternative target exists.
2. `Swanson_ABC_bridging` — first-time data is confounded by PARTIALLY_EXPLORED disjointness. DO NOT downrank based on Session 009 alone. Re-test with a DISJOINT target. When using Swanson_ABC_bridging, add mandatory B-term-in-Field-C PubMed check before assigning disjointness.
3. `tool_repurposing` — no primary data yet. T3 from Session 009 (volcanic glass x pharmaceutical ASD dissolution, scout score 8.3, DISJOINT) is the highest-priority un-tested strategy/target pair in the pipeline. **Make this the primary target in the next session.**
4. `contradiction_mining` — no primary data yet. T1 from Session 009 (Mn speciation paradox, scout score 7.7, DISJOINT) is the secondary priority.
5. `recent_breakthrough_radiation` has the lowest QG pass rate (13%) — use only when the technique is genuinely new (< 2 years) and the biological target is in acute need of measurement tools.

---

## Disjointness vs Outcome (all sessions)

| Disjointness | Sessions | Targets selected | Hyps survived | QG passed (PASS only) | QG CONDITIONAL | QG pass + cond rate | PASS rate |
|---|---|---|---|---|---|---|---|
| DISJOINT | 001, 002, 004, 005, 006, 007, 008 | 8 | ~44 | ~37 PASS or COND | most are PASS | ~84% combined | ~33-43% PASS |
| PARTIALLY_EXPLORED | 009 | 1 | 10 | 0 PASS | 3 COND | 30% COND only | 0% PASS |

**Session 009 first data point for PARTIALLY_EXPLORED**: The selected target (melatonin x coral bleaching) was reclassified from DISJOINT (Scout) to PARTIALLY_EXPLORED (Literature Scout) when Roopin 2013 was discovered. Result: 0 PASS verdicts, mean QG score 5.87 (lowest since S004), no full PASS in any hypothesis. The Ranker-to-QG delta was 1.85 points — the largest in pipeline history — reflecting inflated testability/novelty scores paired with low groundedness.

**Recommendation for Scout**:
- DISJOINT preference is strongly confirmed across 8 prior sessions AND the first PARTIALLY_EXPLORED session (S009) produced the weakest QG outcomes of any recent session.
- **Never select a PARTIALLY_EXPLORED target when DISJOINT alternatives of comparable quality exist in the same session.** In S009, both T1 (7.7, DISJOINT) and T3 (8.3, DISJOINT) were available but T2 (8.0, PARTIALLY_EXPLORED after literature check) was selected. This was an error.
- When Swanson_ABC_bridging is the strategy, add a mandatory step: query "B-term AND Field C" in PubMed/Semantic Scholar. If any papers appear, the target is PARTIALLY_EXPLORED regardless of Field A <-> Field C co-citation counts. Downrank accordingly.

---

## Bridge Type Performance (all sessions)

| Bridge Type | Sessions | Used | QG Passed | QG Score Range | Notes |
|---|---|---|---|---|---|
| Published unmeasured variable (gap paper) | 007 | 1 | 1 PASS | 8/10 | Highest quality — gap explicitly stated. Nadimpalli 2024 → IRP1 → H2.1. Pre-grounded. |
| Thermodynamic displacement (Ksp/Irving-Williams) | 008 | 1 | 1 PASS | 8.1/10 | 29-order Ksp driving force. CIA/LIAS differential rescue. Cross-model HIGH PRIORITY. |
| Mathematical topology constraints | 002 | 3 | 3 | ~8/10 | Poincare-Hopf gives necessary predictions. Cannot be dismissed. |
| Vibronic/phonon coupling | 004 | 3 | 2 | ~7.5/10 | Established physics in new protein system. |
| Quantitative thermodynamic framework (Pourbaix) | 005, 008 | 2 | 2 | 6-7.3/10 | Powerful but kinetics can override. |
| Indirect enzymatic cascade (multi-step) | 001, 006 | 8+ | 6+ | 7-8.5/10 | ~100% survival. More named molecules = more falsifiable. |
| Tool transfer (PHREEQC, Pourbaix) | 005 | 1 | 1 | 7/10 | High novelty, must check biological constraints. |
| Quantitative scavenging budget | 006 | 1 | 1 | 7.5/10 | Inter-compartment signal feasibility. |
| ER-mito Ca2+ signaling at MAMs (CISD2) | 007 | 1 | 1 COND | 7/10 | Triple intersection: longevity x circadian x Fe-S. |
| Cytoplasmic maturation pathway gate | 007 | 1 | 1 COND | 7/10 | ~20 proteins coordinately affected. |
| Substrate supply bottleneck (frataxin/FTMT) | 007 | 1 | 1 COND | 6/10 | Tissue-specificity argument novel. |
| Electrochemical potential matching (Pourbaix/Eh-pH) | 008 | 1 | 1 COND | 7.3/10 | FDX1 E0' at Cu boundary. Needs bypass experiment. |
| Ligand homology (molecular fossil) | 008 | 1 | 1 COND | 5.4/10 | Dithiolane ring-strain DFT testable. |
| Phase formation (nanoparticle concentration) | 008 | 2 | partial | 5.2/10 | One survived as sink; one killed (CuS-Fenton not novel). |
| Evolutionary co-selection (genomic signatures) | 008 | 1 | 1 COND | 5.2/10 | Weakly motivated causal geochemistry. |
| **Published gap extension (NEW — S009)** | **009** | **3** | **0 PASS, 3 COND** | **5.3-6.5/10** | **Prior paper bridges B-term to Field C in normal conditions; hypothesis extends to new stress context.** |
| Diel temporal dynamics | 009 | 1 | 1 COND | 5.8/10 | Nocturnal peak mechanism. SNAT/AANAT bioinformatic angle novel, ecological prediction not. |
| Chemical cascade multiplication | 009 | 1 | 1 COND | 5.3/10 | AFMK/AMK cascade in dinoflagellates. Weak due to wrong ROS species (OH vs 1O2). |
| pH/ion microdomains as molecular effectors | 001 | 4 | 4 | 7.5-8.5/10 | pH and Ca2+ couple broadly across biological scales. |
| Tissue expression pattern → vulnerability map | 006 | 1 | 1 COND | 7/10 | Incremental extension — passes QG but low impact. |
| Electrophilic lipid modifier of receptor (covalent) | 006 | 1 | 1 COND | 7/10 | 4-HNE→LasR Michael addition. |
| Radical regioselectivity contrast | 005 | 1 | 1 | 7/10 | Textbook chemistry both sides. |
| Conservation gap with time lag | 007 | 1 | 1 COND | 6/10 | 14-year Drosophila→mammalian follow-up gap. |
| **Killed bridge types** | | | | | |
| Enzyme saturation (Km-gated, Km << [S]) | 007 | 1 | 0 | 0 | FDXR Km=0.7µM vs NADPH ~50-100µM. Cannot gate. |
| Non-transcriptional redox timer (Prx→H2O2) | 007 | 1 | 0 | 0 | H2O2 2-3 orders below activation threshold. |
| Direct electric/electromagnetic field effects | 001, 004 | 8 | 0 | 0 | Energy scale mismatch always fatal. |
| Quantum entanglement/information storage | 004 | 3 | 0 | 0 | Decoherence in biology is fatal. |
| Fröhlich condensates | 004 | 2 | 0 | 0 | Thermodynamically impossible at 300K. |
| Abiotic PUFA synthesis (FTT route) | 005 | 2 | 0 | 0 | Fischer-Tropsch doesn't make PUFAs. |
| Homogeneous Fenton at wrong pH | 005 | 2 | 0 | 0 | Serpentinization pH 10 ≠ cell pH 7.2. |
| Vocabulary re-description | 002, 005 | 2 | 0 | 0 | No predictive power added. |
| Chemical identity prediction (spectroscopic counter-evidence) | 008 | 1 | 0 | 0 | CuL killed by Cobine JBC 2006 NMR. |
| Novelty failure (adjacent domain) | 008 | 1 | 0 | 0 | CuS-Fenton extensively studied in env. chemistry. |
| Oscillator/limit cycle (Bendixson violation) | 008 | 1 | 0 | 0 | Gemini formal proof rejected H1.3. |
| Novel bacterial receptor (no known family) | 006 | 1 | 0 | 0 | No bacterial phospholipid sensing receptor. |
| Species numbering error (cross-organism annotation) | 007 | 1 | 0 | 0 | E. coli IscS Cys328 ≠ human NFS1. |

**Recommendation for Generator**:
- **Use (highest QG scores)**: Published unmeasured variable (8/10 PASS). Thermodynamic displacement via Ksp (8.1/10 PASS). Indirect multi-step enzymatic cascades (~100% survival). Mathematical necessity arguments (topology). Quantitative scavenging budgets and mass-balance frameworks.
- **Use with caution**: Published gap extension (NEW — 5.3-6.5 COND). Viable but requires verifying that the extension to new conditions is mechanistically justified, not just analogical. Best used when the gap paper makes the extension explicit.
- **Avoid (unconditional kills)**: Direct field effects. Quantum entanglement. Novel receptor with no known family. pH conditions incompatible with target organism. Vocabulary re-description. Cross-species protein annotation errors. Benzene-criterion violations (Bendixson for limit cycles). Chemical identity predictions without checking spectroscopic data.
- **New (Session 009)**: In photosynthetic organisms under thermal or light stress, ¹O₂ is the dominant ROS (not OH). Any cascade mechanism proposing ROS scavenging in chloroplasts must use ¹O₂-specific rate constants (k ≈ 10⁷ M⁻¹s⁻¹ vs 10¹⁰ for OH — a 500x difference). Using OH rate constants in a ¹O₂-dominated context is a direct QG failure mode.

---

## Kill Pattern Distribution (all sessions, cumulative)

| Kill Reason | Estimated count | Approx % | Sessions |
|---|---|---|---|
| Energy scale mismatch (thermal overwhelm, too weak) | 14 | 20% | 001, 004 dominant |
| Substrate/condition mismatch | 8 | 11% | 005 dominant |
| Quantitative impossibility (Km saturation, concentration gap, threshold mismatch) | 9 | 13% | 005, 007, 008 |
| Classical explanation sufficiency | 6 | 9% | 001, 002, 004 |
| Mechanism fabrication (no known receptor/enzyme/pathway) | 5 | 7% | 002, 006 |
| Thermodynamic impossibility (wrong redox, wrong pH) | 4 | 6% | 007, 005 |
| Citation hallucination / unverifiable reference | 3 | 4% | 004 |
| Mathematical invalidity | 3 | 4% | 002 |
| Scope overreach / universal claim | 3 | 4% | 002 |
| Novelty failure (well-studied in adjacent domain) | 2 | 3% | 008 (CuS-Fenton in env. chemistry) |
| Vocabulary re-description | 2 | 3% | 002, 005 |
| Spectroscopic counter-evidence | 1 | 1% | 008 (CuL identity, Cobine NMR) |
| Partial novelty reduction (prior work partially covers) | 1 | 1% | 006 |
| Species numbering error | 1 | 1% | 007 |
| Pathway direction error | 1 | 1% | 007 |
| Dependency cascade | 1 | 1% | 007 |
| Oscillator model mathematically impossible | 1 | 1% | 008 (Bendixson criterion) |
| **ROS species mismatch (photosynthetic context) — NEW S009** | **1** | **1%** | **009 (H2: OH kinetics used, 1O2 dominates)** |

Note: Session 009 kill rate was 0% at critique but QG downgraded all 3 for groundedness failures — these are soft kills (QG CONDITIONAL_PASS) rather than explicit critique kills. The ROS species mismatch is counted here as the primary QG failure mode for H2.

**Recommendation for Generator**:
1. **Thermal energy pre-screen**: For quantum or physical mechanisms, compute kT (26 meV at 300K) vs proposed effect BEFORE writing. 20% of all kills trace to this.
2. **Substrate compatibility check**: Verify conditions in Field A exist in Field C (pH, temperature, substrates).
3. **Receptor existence check (NEW S6)**: Verify receptor family exists for proposed ligand class.
4. **Quantitative scavenging budget (NEW S6)**: For inter-compartment signaling, compute mass-balance.
5. **Back-of-envelope self-consistency**: All calculations must be internally consistent. 40x errors have slipped through.
6. **Classical alternative check**: Before proposing exotic mechanisms, verify classical biochemistry cannot explain.
7. **Citation journal verification**: Verify journal name, not just author/year.
8. **Scope limitation**: Restrict claims to specific systems where assumptions hold.
9. **Km pre-verification (NEW S7)**: If Km << [S], enzyme is saturated; substrate oscillation cannot gate rate.
10. **Redox midpoint verification (NEW S7)**: Verify specific protein isoform redox potential, not homolog.
11. **Species annotation verification (NEW S7)**: Verify residue numbering matches target organism.
12. **Decorative framing gate (NEW S8)**: If cross-field connection is ornamental, cut the hypothesis.
13. **Novelty pre-check in adjacent domains (NEW S8)**: Check environmental chemistry, materials science.
14. **Spectroscopic data pre-check (NEW S8)**: Check published NMR/EXAFS before proposing molecular identity.
15. **Oscillator/limit cycle pre-check (NEW S8)**: Verify Bendixson/Dulac criteria before dynamic models.
16. **ROS species identity in photosynthetic organisms (NEW S9)**: In chloroplasts under thermal/light stress, ¹O₂ dominates (k ≈ 10⁷ M⁻¹s⁻¹). Using OH rate constants (k ≈ 10¹⁰) overstates scavenging by ~500x. Specify the ROS species and use its correct rate constant.
17. **Propagate Critic corrections before QG (NEW S9)**: If Critic flags a numerical error in a specific hypothesis, the hypothesis must be explicitly revised before passing to QG. Do not leave Critic corrections as caveats in the critique document.

---

## Session Performance History

| Session | Target | Hyps gen | Kill rate | QG pass+cond | QG PASS | QG mean | Ranker-QG delta | Status |
|---|---|---|---|---|---|---|---|---|
| 001 | Bioelectric x Condensates | ~8 | ~50% | 4 | 4 | ~7.5 | ~0.3 | SUCCESS |
| 002 | Active matter x Stem cells | ~12 | ~75% | 3 | 3 | ~7.0 | ~0.4 | SUCCESS |
| 003 | (targeted, early session) | — | — | — | — | — | — | — |
| 004 | THz spectroscopy x Quantum coherence | 15 | 67% | 2 | 2 | ~6.5 | ~0.5 | SUCCESS |
| 005 | Ferroptosis x Serpentinization | 14 | 50% | 4 | 4 | ~7.0 | ~0.4 | SUCCESS |
| 006 | Ferroptosis x Quorum sensing | 14 | ~36% | 6 | 6 | ~7.2 | ~0.3 | SUCCESS |
| 007 | Fe-S biogenesis x Circadian clock | 15 | 17% | 5 | 1 + 4 COND | ~6.6 | ~0.6 | SUCCESS |
| 008 | Cuproptosis x Vent Cu-S Geochemistry | 12 | 17% | 5 | 1 + 4 COND | ~6.8 | ~0.2 | SUCCESS |
| 009 | Plant melatonin x Coral bleaching | 10 | **0%** | 3 COND | **0** | **5.87** | **1.85** | PARTIAL |

**Trend analysis**:
- Kill rate trend: 50-75% (S001-002) → 17% (S007-008) → **0% (S009)**. The 0% rate in S009 is an anomaly driven by domain characteristics (no KEGG/STRING Symbiodiniaceae data = no structural kill information available), not by improving hypothesis quality. The pipeline should target a kill rate of 15-25% as the healthy operating range.
- QG mean trend: Sessions 006-008 sustained 6.6-7.2. Session 009 drops to 5.87 — lowest since S004. This is a domain-specific dip (PARTIALLY_EXPLORED target, low infrastructure coverage) rather than pipeline degradation.
- Ranker-QG delta: S008 was the minimum (0.2 — the Ranker and QG were most aligned). S009 is the maximum (1.85 — largest misalignment). When computational validation yields INCONCLUSIVE organism data, the Ranker consistently over-scores testability relative to QG.
- PASS verdicts: S007-S008 each had 1 full PASS. S009 had 0. DISJOINT + quantitative thermodynamic bridges have produced the only full PASS verdicts. PARTIALLY_EXPLORED + analogical bridges produce CONDITIONAL_PASS at best.

**Pipeline health**: The pipeline is **not degrading** — the S009 performance drop is fully explained by (a) PARTIALLY_EXPLORED target selection and (b) domain infrastructure limitations. The S009 Scout actually generated three strong targets (T1: 7.7 DISJOINT, T2: 8.0 PARTIALLY_EXPLORED, T3: 8.3 DISJOINT) — the selection of T2 over T1/T3 is the root cause of weaker outcomes. The pipeline generated correct Scout targets but made the wrong selection choice. Correcting the selection rule (prioritize DISJOINT absolutely when alternatives exist) will restore S006-S008 performance levels.

---

## Cross-Model Validation Patterns (Sessions 4–8, updated)

(No new cross-model validation data for Session 009 — analysis pending.)

### GPT vs Gemini Divergence (prior sessions)
- **Gemini** consistently scores mathematical/structural correctness highly (8-10/10)
- **GPT** consistently scores biological plausibility and practical utility (2-6/10)
- **Divergence is largest** when math is sound but biology is domain-irrelevant
- **Divergence is smallest** when both chemistry AND biology are well-grounded
- **New (S8)**: Gemini can provide formal mathematical proofs that kill hypotheses (Bendixson criterion). Unique strength — leverage for dynamic model hypotheses.

**Recommendation for Quality Gate**: When cross-model scores diverge by > 4 points, prioritize GPT score for biological plausibility; investigate Gemini score for structural/mathematical validity.

---

## Productive Bridge Concept Patterns (cumulative)

1. **Published unmeasured variable bridges** (S007): When recent literature explicitly identifies gaps ("X remains unmeasured"), building hypotheses around these gaps produces pre-grounded, high-scoring results. Nadimpalli 2024 → IRP1 → H2.1 PASS is the exemplar.
2. **Indirect enzymatic cascades** (S001, S006): Multi-step pathways through well-characterized intermediaries survive at ~100%. The more named molecules in the chain, the more falsifiable.
3. **pH/ion microdomains** (S001): pH and Ca2+ are promiscuous regulators; they couple broadly across biological scales.
4. **Mathematical topology constraints** (S002): Poincare-Hopf theorem gives mathematically necessary predictions.
5. **Vibronic coupling in structured protein scaffolds** (S004): Established physics; novelty comes from new protein system.
6. **Shared mineral chemistry** (S005): Iron/copper minerals bridge geochemistry and biology through identical chemical species.
7. **Tool transfer** (S005): Applying geochemistry tools (PHREEQC, Pourbaix) to biology. High novelty, must check biological constraints.
8. **Quantitative scavenging budget** (S006): Computing whether a reactive intermediate can physically traverse an extracellular space. Applicable to any inter-compartment signaling hypothesis.
9. **Deferred DISJOINT targets** (S006): Scout queue of validated-but-unexplored targets pays dividends. Session 002 flagged ferroptosis x QS; Session 006 delivered the pipeline's best results to date.
10. **Thermodynamic displacement via equilibrium constants** (S008): When two metals compete for the same coordination site, the ratio of formation/solubility constants provides a quantitative, irrefutable driving force (29-order Ksp difference → H1.4 PASS 8.1/10).
11. **Pourbaix/Eh-pH framework transfer** (S008): Geochemists have 50+ years of copper speciation data. Applying to intracellular compartments is absolutely novel (zero publications found).
12. **Published gap extension** (S009 — new, lower tier): A prior paper establishes B-term in Field C under NORMAL conditions; hypothesis extends to a NEW stress/context. Produces CONDITIONAL_PASS (5.3-6.5) but not full PASS. Use when stronger bridge types are unavailable but ensure the extension is mechanistically justified, not merely analogical.

---

## Domain Productivity Assessment (updated)

### Confirmed High-Productivity Domains

**Infection biology** (S006): 43% QG pass rate, first 10/10 scores. Both fields have defined molecular players with published kinetics. Shared metabolic intermediaries (GSH, iron, lipid aldehydes). Standard assay systems (P. aeruginosa QS, GPX4 KO cell lines).

**Metal-dependent cell death x Geochemistry** (S005, S008): 29-42% QG pass rate. Quantitative thermodynamic frameworks (Ksp, Pourbaix, speciation) provide irrefutable numerical predictions. Well-characterized molecular targets. Geochemistry precision (50+ years Cu-S data) transfers to biology.

**Fe-S cluster biology** (S007): 33% QG pass rate. Rich molecular infrastructure (NFS1, ISCU2, FDX2, frataxin). Published quantitative gaps (Nadimpalli 2024). High testability. Active field validation.

### New Caution Domain (Session 009)

**Photosynthetic symbiont stress biology (Symbiodiniaceae)**: 0 PASS verdicts, mean QG 5.87. Key limitation: Symbiodiniaceae are ABSENT from KEGG, STRING, and most proteomics databases. Melatonin x coral bleaching is a genuine gap but the biochemical infrastructure for claim verification is insufficient. Hypotheses in this domain are testable (bioinformatics on PRJNA723630, culture experiments) but not groundable from existing databases. The pipeline's groundedness scoring (20% weight) penalizes this domain systematically.

**Recommendation for Scout**: Photosynthetic symbiont biology pairs are viable targets but expect CONDITIONAL_PASS at best with current database infrastructure. If selecting such a target, ensure the hypothesis testing plan uses available datasets explicitly (PRJNA723630 for Symbiodiniaceae, direct culture experiments) rather than relying on database-verifiable claims.

---

## Unexplored High-Quality Targets (Scout deferred queue)

| Target pair | Identified in | Strategy | Scout score | Disjointness | Priority | Notes |
|---|---|---|---|---|---|---|
| Volcanic glass dissolution kinetics x Pharmaceutical ASD dissolution | 009 | tool_repurposing | **8.3** | DISJOINT | **HIGHEST** | TST rate law / PHREEQC / passivation layer — zero pharma citations confirmed. Highest unselected Scout score in pipeline history. |
| Mn neurotoxicity x Deinococcus Mn-antioxidant biology | 009 | contradiction_mining | 7.7 | DISJOINT | HIGH | Free Mn2+ (toxic) vs complexed Mn-OP (protective). DP1 synthetic decapeptide characterized (PNAS 2024). Genuine speciation paradox. |
| Circadian x Neurodegeneration | 001 | contradiction_mining | — | DISJOINT | MEDIUM | Cross-session circadian oscillation → condensate aging |
| Acoustic mechanotransduction x Tumor immune microenvironment | 001 | — | — | PARTIALLY_EXPLORED | MEDIUM-LOW | Piezo1 differential expression |
| Cristae remodeling x Synaptic plasticity | 002 | — | — | PARTIALLY_EXPLORED | MEDIUM-LOW | MICU1 gating threshold |
| Mitochondrial hormesis x Cellular aging hallmarks | 004 | contradiction_mining | — | PARTIALLY_EXPLORED | MEDIUM | ROS threshold switching |
| Piezoelectric collagen x HSC fate decisions | 006 | contradiction_mining + dimensional_mismatch | 7/10 | DISJOINT | MEDIUM | CRITICAL energy-scale pre-check needed before selection |
| BEV x Exosome immunomodulation | 006 | evolutionary_conservation_gap | 7/10 | DISJOINT | MEDIUM | Needs more specific bridge concepts |
| Coral calcification x Vascular calcification | 008 | implicit_disjoint | — | DISJOINT | MEDIUM | Biomineralization bridge; not evaluated |

**Recommendation for Scout**: **Prioritize T3 from Session 009 (volcanic glass x pharmaceutical ASD dissolution) as the primary target for the next session.** It has the highest Scout score of any unselected target in the pipeline history (8.3), is confirmed DISJOINT, uses an untested strategy (tool_repurposing), and has a clean quantitative bridge (TST rate law, saturation index, passivation layer kinetics). Mn speciation paradox (T1 from S009) is the secondary priority.

---

## Critical Screening Rules (for Generator — cumulative)

1. **Thermal energy pre-screen**: For quantum/physical mechanisms, compute kT (26 meV @ 300K) BEFORE proceeding. 20% of all kills trace to this failure.

2. **Substrate/condition compatibility**: Verify conditions in Field A actually exist in Field C. Serpentinization pH ≠ cytoplasmic pH. Check BEFORE writing.

3. **Receptor existence check (NEW S6)**: Before proposing a sensing/receptor mechanism, verify a receptor family for the ligand class exists in the target organism.

4. **Quantitative scavenging budget (NEW S6)**: For inter-compartment signaling involving reactive small molecules, compute the mass-balance: how much intermediate survives scavenging?

5. **Biological effect-size comparison**: Compare proposed mechanism's effect size to known dominant regulators. If GPX4/ACSL4 dominate by 100-fold, a 3-fold speciation effect is biologically minor.

6. **Geochemical/field specificity**: When claiming connection to a specific geochemical setting, ensure bridge concepts are diagnostic for that setting, not generic.

7. **Citation verification**: Every [GROUNDED] claim must have a verifiable citation. Verify journal names, not just author/year.

8. **Classical alternative check**: Before proposing exotic mechanisms, verify classical biochemistry cannot explain the observation.

9. **Scope limitation**: Avoid universal claims. Restrict to specific systems where assumptions hold.

10. **Back-of-envelope self-consistency**: Self-critique calculations must match stated log K values and concentrations. Numerical inconsistencies (~40x errors) have slipped through before.

11. **Incremental extension check (NEW S6)**: Hypotheses of the form "X expression level determines susceptibility to known mechanism Y" consistently score as incremental (7/10 at QG). Apply higher novelty threshold.

12. **Published gap exploitation (NEW S7)**: Search for recent reviews that explicitly identify "unmeasured variables" or "open questions" — these produce the highest-quality bridge concepts.

13. **Species annotation verification (NEW S7)**: Always verify protein residue numbering matches target organism. Cross-species errors (E. coli → human) are an emerging failure mode.

14. **Enzyme kinetics pre-check (NEW S7)**: Before proposing enzyme-gated mechanisms, verify Km vs [substrate]. If Km << [S], enzyme is saturated and substrate oscillation cannot gate rate.

15. **Decorative framing gate (NEW S8)**: If Generator self-critique identifies the cross-field connection as ornamental rather than mechanistically necessary, do NOT include the hypothesis.

16. **Novelty pre-check in adjacent domains (NEW S8)**: Before proposing a reaction as novel, check whether it is well-studied in an adjacent domain (e.g., environmental chemistry, materials science).

17. **Spectroscopic data pre-check (NEW S8)**: Before proposing molecular identity or structural predictions, check for existing spectroscopic data (NMR, EXAFS, X-ray) that could immediately contradict it.

18. **Oscillator/limit cycle pre-check (NEW S8)**: Before proposing oscillatory mechanisms, verify Bendixson/Dulac criteria. If Jacobian trace is negative, no limit cycle exists.

19. **ROS species identity in photosynthetic organisms (NEW S9)**: In chloroplasts under thermal or high-light stress, ¹O₂ is the dominant ROS (k_scavenging ≈ 10⁷ M⁻¹s⁻¹). Using OH kinetics (k ≈ 10¹⁰) overstates scavenging capacity by ~500x. Always specify the ROS species and use species-correct rate constants. OH dominates in dark Fenton chemistry; ¹O₂ dominates in illuminated photosynthetic systems.

20. **Propagate Critic corrections before QG (NEW S9)**: If Critic flags a specific numerical error (concentration, rate constant, species identity) in a hypothesis, that correction MUST be incorporated into the revised hypothesis text. Do not leave corrections as caveats in the critique log. QG will find the uncorrected text and penalize it.

---

## Recommendations Summary (updated after Session 009)

**For Scout**:
1. `network_gap_analysis` remains highest-performing (39% QG pass rate, 3 sessions). Use as reliable baseline.
2. `tool_repurposing` has zero primary data but T3 from S009 (volcanic glass x pharma ASD, 8.3 score, DISJOINT) is the pipeline's highest-priority un-tested strategy/target pair. **Make it Session 010's primary target.**
3. `contradiction_mining` has zero primary data. T1 from S009 (Mn speciation paradox, 7.7, DISJOINT) is secondary priority.
4. `Swanson_ABC_bridging` — first data confounded by PARTIALLY_EXPLORED. Re-test with verified DISJOINT target. Add B-term-in-Field-C literature check before disjointness assignment.
5. **ABSOLUTE RULE**: When DISJOINT targets are available at comparable quality, NEVER select a PARTIALLY_EXPLORED target. S009 demonstrates that PARTIALLY_EXPLORED selection degrades QG outcomes even when Scout scores are high.
6. Maintain DISJOINT deferred target queue. Two new entries from S009: T1 (7.7) and T3 (8.3, highest priority).
7. Metal-dependent cell death x geochemistry and infection biology x shared metabolites remain confirmed high-productivity domains.
8. Photosynthetic symbiont biology (Symbiodiniaceae) domains are viable but expect CONDITIONAL_PASS ceiling due to database infrastructure gaps.

**For Generator**:
1. Lead with quantitative thermodynamic bridges (Ksp ratios, Pourbaix, equilibrium constants) — highest QG scores (8.1/10 PASS).
2. Exploit published gap papers — when literature identifies specific unmeasured variables, build hypotheses around them. The highest-quality bridge type.
3. Hard gate on "decorative" framing — if self-critique flags cross-field connection as ornamental, cut the hypothesis.
4. Check spectroscopic data before proposing molecular identity predictions.
5. Check novelty in adjacent domains (environmental chemistry, materials science) before claiming biological novelty.
6. Verify species-specific protein data — don't use E. coli numbering for human proteins.
7. Enzyme kinetics pre-check — verify Km vs [substrate] before proposing rate-gating mechanisms.
8. Oscillator/limit cycle pre-check — verify Bendixson criteria before proposing dynamic models.
9. In photosynthetic organisms under thermal/light stress: identify dominant ROS species (¹O₂), use species-correct rate constants. OH kinetics in a ¹O₂-dominated system = QG failure.
10. Propagate every Critic numerical correction into revised hypothesis text before QG. No exceptions.
11. Indirect enzymatic cascades with named molecules maintain ~100% critique survival rate.

**For Quality Gate**:
1. Pipeline returned to CONDITIONAL_PASS-only in S009. This is a domain/disjointness artifact, not a quality degradation.
2. When computational validation shows INCONCLUSIVE for target organism KEGG/STRING, apply heightened per-claim scrutiny — groundedness claims cannot be database-verified.
3. Ranker-QG delta > 1.0 should trigger additional cross-model validation scrutiny. S009 had the largest delta (1.85) and the weakest QG outcomes.
4. CONDITIONAL_PASS hypotheses should receive explicit "resolve before publication" annotations for each specific weakness.

**For Ranker**:
1. When computational validation returns INCONCLUSIVE for the target organism in KEGG/STRING, reduce groundedness dimension score by 1.5 points across all hypotheses before computing weighted composite. This prevents testability/novelty inflation from masking infrastructure gaps — the root cause of the 1.85-point Ranker-QG delta in S009.
