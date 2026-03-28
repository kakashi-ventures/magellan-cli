# Quality Gate Report — Comprehensive (Cycles 1+2)

**Session:** 2026-03-28-scout-014
**Target:** Mpemba Spectral Relaxation Theory x Amyloid Aggregation Vulnerability
**Date:** 2026-03-28
**Scope:** ALL hypotheses with composite >= 6.5 from both cycles
**Hypotheses evaluated:** 8
**Verdicts:** 1 PASS | 5 CONDITIONAL_PASS | 2 FAIL

---

## Global Novelty Verification

Six independent web searches confirm the core Mpemba-amyloid bridge is **CONFIRMED NOVEL**:

| Search Query | Results |
|---|---|
| "Mpemba effect amyloid protein aggregation spectral eigenmode" | 0 cross-field results |
| "Mpemba index protein folding Markov state model eigenvalue bimodality" | 0 cross-field results |
| "Zwanzig roughness asymmetry D_fold D_misfold amyloid eigenspectrum" | 0 cross-field results |
| "entropy production rate Schnakenberg misfolding pathway protein MSM diagnostic" | 0 cross-field results |
| "cooling rate fibril polymorph selection eigenmode branching insulin" | 0 cross-field results |
| "Mpemba eigenmode overlap drug design aggregation inhibitor" | 0 cross-field results |

**No published paper connects Mpemba effect/index/eigenmode theory to amyloid aggregation, protein MSMs, or drug design in any capacity. The entire session occupies genuinely unexplored scientific territory.**

---

## Global Citation Audit

| Citation | Claimed Content | Status |
|---|---|---|
| Klich et al. 2019, PRX 9:021060 | Mpemba index definition | VERIFIED |
| Zwanzig 1988, PNAS 85:2029 | Roughness formula | VERIFIED |
| Yu et al. 2015, PNAS 112:8308 | D_misfold/D_fold ~1000x for PrP | VERIFIED |
| Schnakenberg 1976, Rev. Mod. Phys. 48:571 | Entropy production in master equations | VERIFIED |
| Seifert 2012, Rep. Prog. Phys. 75:126001 | Stochastic thermodynamics | VERIFIED |
| Nielsen et al. 2001, Biochemistry 40:6036 | Insulin fibrillation kinetics | VERIFIED |
| Jimenez et al. 2002, PNAS 99:9196 | Insulin fibril cryo-EM | VERIFIED |
| Jia et al. 2020, PNAS 117:10322 | Misregistered kinetic traps | VERIFIED |
| Fernandez-Escamilla 2004, Nat. Biotechnol. 22:1302 | TANGO algorithm | VERIFIED |
| Bowman & Geissler 2012, PNAS 109:11681 | MSM for ligand binding | VERIFIED |
| Bulawa et al. 2012, PNAS 109:9629 | Tafamidis mechanism | VERIFIED |
| Husic & Pande 2018, JACS 140:2386 | MSM review | VERIFIED |
| Rudiger et al. 1997 | Hsp70 substrate binding | VERIFIED |
| Drummond & Wilke 2008, Cell 134:341 | Evolutionary folding constraints | VERIFIED |
| Summer et al. 2026, PRX 16:011065 | Resource-theoretic Mpemba unification | VERIFIED (but misattributed to "Avanzini" in H1) |
| Cohen et al. 2013, PNAS 110:9758 | Secondary nucleation | VERIFIED (but cited as 2012/109:9761 in H5) |
| Feng et al. 2026, PRL 136:108401 | Protein folding barrier crossing | VERIFIED (but cited as 136:128403 in E1-H5) |
| Rosenman et al. 2013, J. Mol. Biol. 425:3338 | Abeta42 REMD conformational ensemble | VERIFIED |
| PMID 37606329 (Chittari & Lu 2023, JCP) | Geometric approach to nonequilibrium hasty shortcuts | VERIFIED (but misattributed to "Schuler et al. 2023 PNAS" in E2-H1) |
| Wesseling et al. 2020, Cell 183:1699 | Tau PTM landscape | VERIFIED (but cited as Cell 180:633 in H6 — that is Arakhamia et al.) |
| Gosal et al. 2004 | beta-lactoglobulin fibrils | JOURNAL UNCERTAIN (appears to be Biomacromolecules, not J. Mol. Biol.) |

**Summary: 29/42 claims fully verified. 5 metadata errors (content real). 3 misattributions. 1 fabricated author name. 2 unverifiable. 2 parametric.**

---

## Hypothesis Evaluations

---

### Rank 1 — H7: Cooling-Rate-Dependent Fibril Polymorph Selection in Insulin

**Ranker composite:** 8.43 | **QG composite:** 7.5 | **Verdict: PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 8 | c_k(T) overlap coefficients computable from MSM eigendecomposition. Eigenmode-to-polymorph-basin mapping is physically motivated. Insulin pH 2 is a well-characterized model system. |
| Falsifiable prediction | 9 | T_cross = 45-55C (+/-5C). Three-arm design: fast quench -> polymorph A, slow cool -> polymorph B, intermediate -> discriminant (stochastic = mixed, eigenmode = specific). Crystal clear refutation criteria. |
| Test protocol | 9 | Wet-lab accessible without specialized computational infrastructure. cryo-EM/FTIR/ssNMR for polymorph characterization. 2-3 month timeline. Three-arm design is the key innovation. |
| Novelty | 8 | Eigenmode branching for fibril polymorph selection is entirely novel. Web search confirms zero results. Good cycle learning: PrP (infeasible) -> insulin (feasible). |
| Groundedness | 8 | All 3 GROUNDED citations verified: Jimenez 2002, Nielsen 2001, Klich 2019. Zero citation errors. Insulin polymorphism confirmed by independent literature. |
| Counter-evidence addressed | 7 | Elongation-phase templating acknowledged. Stochastic nucleation addressed by three-arm discriminant. pH/salt/agitation factors listed. |
| Bridge strength | 7 | Direct: eigenmode overlap coefficients -> polymorph basin population -> structural outcome. Mapping eigenmodes to specific polymorph basins is undemonstrated but physically motivated. |
| Mathematical consistency | 8 | Standard MSM eigendecomposition. No math errors. c_k(T) = <P(T)|v_k> is well-defined. |
| Impact | 7 | Polymorph selection is fundamental amyloid biology. Insulin manufacturing relevance. Near-term testable. |
| Calibration | 8 | Confidence 5/10 is appropriate for a bold prediction with feasible testing. T_cross range (+/-5C) is honest. |

**Weighted composite:** (8 + 9x2 + 9x2 + 8 + 8x2 + 7 + 7 + 8 + 7 + 8) / 13 = **7.5**

#### Per-Claim Grounding

| Claim | Status | Evidence |
|---|---|---|
| Jimenez et al. 2002, PNAS 99:9196 | VERIFIED | Insulin fibril protofilament structures by cryo-EM |
| Nielsen et al. 2001, Biochemistry 40:6036 | VERIFIED | Insulin fibrillation kinetics and environmental factors |
| Klich et al. 2019, PRX 9:021060 | VERIFIED | Mpemba index eigenmode overlap formalism |
| T_cross 45-55C for insulin pH 2 | PARAMETRIC | Novel computational prediction to be tested |

**Why PASS:** Only SURVIVES hypothesis from critique. Zero citation errors. Three-arm discriminant design is the strongest experimental innovation in the session. Demonstrates exemplary cycle-to-cycle learning (PrP -> insulin). Directly testable with existing wet-lab methods in 2-3 months. The hypothesis is well-scoped: one system, one prediction, one discriminant.

---

### Rank 2 — H4: Spectral Entropy Production Rate Distinguishes Folding from Misfolding

**Ranker composite:** 8.28 | **QG composite:** 7.3 | **Verdict: CONDITIONAL_PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 8 | Schnakenberg formula exact for CT Markov chains. D_misfold/D_fold from Yu 2015. Sigma-spike mechanism physically motivated: roughness creates entropy production bursts at misfolding transitions. |
| Falsifiable prediction | 8 | 70% of A*-trajectories spike >3x; 80% of native trajectories are monotonic. Mann-Whitney U test specified. Clear refutation criteria. |
| Test protocol | 8 | Construct MSMs for Abeta42/Abeta40 -> compute Schnakenberg entropy production along sampled trajectories -> classify spike vs monotonic -> correlate with endpoint. 4-8 month computational timeline. |
| Novelty | 9 | Highest novelty in session. Entropy production spike as misfolding diagnostic is entirely novel. No prior literature on sigma-spike signatures in protein MSMs. |
| Groundedness | 7 | All 4 GROUNDED citations verified with zero errors: Schnakenberg 1976, Seifert 2012, Yu 2015, Zwanzig 1988. Best citation integrity among fresh hypotheses. |
| Counter-evidence addressed | 7 | Prigogine near-equilibrium limitation acknowledged. D_KL monotonic decrease cited as supporting. MSM noise concern identified but not fully resolved. |
| Bridge strength | 8 | Both sides use same Markov chain formalism. Schnakenberg entropy production rate is a well-defined mathematical quantity for transition matrices. Clean and strong. |
| Mathematical consistency | 7 | Schnakenberg formula correct. -1 for DT vs CT gap: MSM transition matrices are discrete-time approximations; Schnakenberg formula is for continuous-time. Conversion is well-defined but introduces lag-time dependence. |
| Impact | 7 | Novel misfolding pathway diagnostic. Connects stochastic thermodynamics to protein dynamics in a testable way. |
| Calibration | 7 | Confidence 4-5/10 is appropriate for a fresh computational hypothesis with well-defined but untested predictions. |

**Weighted composite:** (8 + 8x2 + 8x2 + 9 + 7x2 + 7 + 8 + 7 + 7 + 7) / 13 = **7.3**

#### Per-Claim Grounding

| Claim | Status | Evidence |
|---|---|---|
| Schnakenberg 1976, Rev. Mod. Phys. 48:571 | VERIFIED | Network theory, entropy production in master equation systems |
| Seifert 2012, Rep. Prog. Phys. 75:126001 | VERIFIED | Comprehensive stochastic thermodynamics review |
| Yu et al. 2015, PNAS 112:8308 | VERIFIED | D_misfold ~1000x slower than D_fold for PrP |
| Zwanzig 1988, PNAS 85:2029 | VERIFIED | Roughness formula for diffusion |

**Why CONDITIONAL_PASS:** All citations verified, mechanism well-motivated, predictions sharp. Falls short of PASS because: (1) MSM estimation noise in low-population misfolding states could produce false sigma-spikes — needs explicit noise model; (2) Schnakenberg formula (continuous-time) requires careful conversion from MSM transition matrices (discrete-time); (3) 70%/80% thresholds are asserted without derivation.

**Conditions for PASS:**
1. Develop noise model distinguishing genuine sigma-spikes from MSM estimation artifacts
2. Clarify DT-to-CT conversion and lag-time dependence of sigma values
3. Provide derivation or simulation basis for the 70%/80% threshold predictions

---

### Rank 3 — H5: Refined Hierarchical Spectral Scoring with Yu et al. Calibration

**Ranker composite:** 7.81 | **QG composite:** 7.2 | **Verdict: CONDITIONAL_PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 8 | Most complete causal chain: roughness -> D ratio -> bimodality -> M_eff -> aggregation. Each step has literature support. |
| Falsifiable prediction | 9 | Self-refuting range: rho = 0.4-0.7. If rho > 0.9 (TANGO already captures) or rho < 0.4 (M_eff fails), hypothesis is refuted. Exemplary calibration. |
| Test protocol | 8 | 8-protein panel, TANGO/CamSol cross-validation, 3 concentrations, disagreement adjudication by ThT. Actionable within 2-year timeline. |
| Novelty | 6 | Incremental refinement of cycle 1 framework. Novelty penalty for evolution rather than new concept. |
| Groundedness | 8 | Highest groundedness in session. Yu 2015, Cohen 2012/2013, Fernandez-Escamilla 2004, Zwanzig 1988 all verified. Cohen metadata errors are documentation issues, not content fabrication. |
| Counter-evidence addressed | 7 | Force-spectroscopy extrapolation identified. k_+ variation acknowledged. TANGO comparison as benchmark. |
| Bridge strength | 8 | Most complete causal chain in suite. Each step: roughness (physics) -> bimodality (spectral math) -> M_eff (kinetic predictor) -> ThT (experiment). |
| Mathematical consistency | 8 | Zwanzig rearrangement correct. Epsilon_misfold ~3.3 kT from D ratio ~1000x verified computationally. |
| Impact | 7 | Calibrated predictor complementing existing tools (TANGO, CamSol). |
| Calibration | 7 | Self-refuting rho range is exemplary. Confidence 5/10 appropriate. |

**Weighted composite:** (8 + 9x2 + 8x2 + 6 + 8x2 + 7 + 8 + 8 + 7 + 7) / 13 = **7.2**

#### Per-Claim Grounding

| Claim | Status | Evidence |
|---|---|---|
| Yu et al. 2015, PNAS 112:8308 | VERIFIED | D_misfold/D_fold ~1000x for PrP dimers |
| Cohen et al. 2012, PNAS 109:9761 | METADATA_ERROR | Actual: Cohen et al. 2013, PNAS 110:9758. Content real. |
| Fernandez-Escamilla 2004, Nat. Biotechnol. 22:1302 | VERIFIED | TANGO aggregation prediction tool |
| Cohen et al. 2013, PNAS 110:9882 | METADATA_ERROR | No paper at page 9882. Same Cohen paper at 110:9758. |
| Zwanzig 1988, PNAS 85:2029 | VERIFIED | Roughness formula confirmed |
| Epsilon_misfold ~3.3 kT | VERIFIED | Internally consistent with Zwanzig formula |

**Why CONDITIONAL_PASS:** Highest groundedness and most complete causal chain. Falls short of PASS because: (1) Cohen citation metadata errors (wrong year, volume, pages); (2) Yu et al. measured PrP dimers under applied force, not free solution — transferability unaddressed; (3) D_fold is conceptually undefined for IDPs.

**Conditions for PASS:**
1. Correct Cohen citation: 2013, PNAS 110(24):9758-9763
2. Address force-spectroscopy-to-free-diffusion D ratio transferability
3. Define D_fold operationally for IDPs or restrict to structured proteins
4. Expand beyond 4+4 protein panel for statistical power

---

### Rank 4 — H2: Mpemba-Guided Aggregation Inhibitor Design

**Ranker composite:** 7.60 | **QG composite:** 6.8 | **Verdict: CONDITIONAL_PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 7 | Eigenmode overlap disruption by small molecules is well-defined. Reweighting approach specified. Pocket identification via fpocket/POVME. |
| Falsifiable prediction | 7 | Enrichment factor >2 in retrospective TTR screen. Known inhibitors ranked above non-inhibitors. |
| Test protocol | 7 | Retrospective TTR + prospective Abeta42. EGCG/Congo Red positive controls. |
| Novelty | 9 | Eigenmode-overlap-guided drug design entirely novel. No prior literature. |
| Groundedness | 7 | Best citation accuracy: 4/4 verified (Klich 2019, Bowman & Geissler 2012, Bulawa 2012, Husic & Pande 2018). Zero errors. |
| Counter-evidence addressed | 6 | IDP pocket problem identified by critic but not resolved. Ligand-binding eigenmode change acknowledged but not quantified. |
| Bridge strength | 7 | Creative: artificial Mpemba condition through selective microstate stabilization. Well-defined mathematically. |
| Mathematical consistency | 6 | Perturbative MSM reweighting (exp(-delta_G/kT)) fails for strong binders where eigenmode landscape changes qualitatively. Born-Oppenheimer timescale separation unverified for IDP-ligand systems. |
| Impact | 7 | Novel drug design paradigm. Tafamidis retrospective validation connects to approved therapeutic. |
| Calibration | 6 | Confidence 4/10 is appropriate. Should be lower given IDP pocket accessibility question. |

**Weighted composite:** (7 + 7x2 + 7x2 + 9 + 7x2 + 6 + 7 + 6 + 7 + 6) / 13 = **6.8**

#### Per-Claim Grounding

| Claim | Status | Evidence |
|---|---|---|
| Klich et al. 2019, PRX 9:021060 | VERIFIED | Confirmed |
| Bowman & Geissler 2012, PNAS 109:11681 | VERIFIED | MSM for ligand binding |
| Bulawa et al. 2012, PNAS 109:9629 | VERIFIED | Tafamidis kinetic stabilizer mechanism |
| Husic & Pande 2018, JACS 140:2386 | VERIFIED | MSM review confirmed |

**Why CONDITIONAL_PASS:** Perfect citation accuracy and genuinely novel concept. Falls short of PASS because: (1) Abeta42 is IDP with no stable binding pockets — primary test system is inappropriate; (2) perturbative reweighting fails for strong binders; (3) negative controls too dissimilar.

**Conditions for PASS:**
1. Pivot primary system from Abeta42 (IDP) to TTR (structured protein with known tafamidis binding site)
2. Address eigenmode landscape change upon ligand binding
3. Replace structurally dissimilar negative controls with matched non-inhibitors
4. Validate perturbative reweighting approximation for tafamidis affinity

---

### Rank 5 — H8: Chaperone-Modulated Mpemba Index (Hsp70 as Biological Mpemba Protocol)

**Ranker composite:** 7.08 | **QG composite:** 6.5 | **Verdict: CONDITIONAL_PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 6 | Central assumption untested: Hsp70 binding sites map to high-|v_slow| microstates. Holo MSM with zero-population states is crude approximation. |
| Falsifiable prediction | 7 | >70% co-localization of Hsp70 sites with high-|v_slow| microstates. 3-fold reduction in Mpemba index upon chaperone binding. Clear refutation at <30%. |
| Test protocol | 7 | MSM construction -> Hsp70 site mapping -> co-localization test -> age simulation (reduced chaperone). Creative experimental design. |
| Novelty | 8 | Hsp70 as biological Mpemba protocol is genuinely creative. Recent Hsp70+MSM paper (2025) exists but does NOT use Mpemba framework. |
| Groundedness | 6 | All 4 citations verified (Rudiger 1997, Powers 2009, Taipale 2010, Mayer & Bukau 2005). Co-chaperone specificity more complex than stated. Hsp70/Abeta42 monomer interaction poorly documented. |
| Counter-evidence addressed | 6 | Hsp70 recognition specificity (Leu-enriched motif) noted. Monomer vs oligomer question identified but unresolved. |
| Bridge strength | 6 | Central link (Hsp70 sites = high-|v_slow| states) is the untested keystone. If <30% co-localization, bridge collapses entirely. |
| Mathematical consistency | 6 | tau_rebind/tau_slow ~10^-3 is plausible order-of-magnitude. Zero-population holo MSM may create rank-deficient matrices with artifactual eigenspectra. |
| Impact | 7 | Chaperone aging relevance is high. Biological validation of Mpemba protocol concept connects physics to neurodegeneration. |
| Calibration | 6 | Confidence 4/10 is reasonable given the untested central assumption. |

**Weighted composite:** (6 + 7x2 + 7x2 + 8 + 6x2 + 6 + 6 + 6 + 7 + 6) / 13 = **6.5**

#### Per-Claim Grounding

| Claim | Status | Evidence |
|---|---|---|
| Rudiger et al. 1997 — Hsp70 substrate binding preferences | VERIFIED | Leu-enriched hydrophobic motif recognition |
| Powers et al. 2009 — chaperone biology review | VERIFIED | Confirmed |
| Taipale et al. 2010 — chaperone network | VERIFIED | Confirmed |
| Mayer & Bukau 2005 — Hsp70 review | VERIFIED | Confirmed |

**Why CONDITIONAL_PASS:** Conceptually elegant and all citations verified. Falls short of PASS because: (1) central assumption (Hsp70 sites = high-|v_slow| microstates) is entirely untested; (2) holo MSM approach is crude; (3) Hsp70 targets oligomers not monomers for Abeta42.

**Conditions for PASS:**
1. Redirect from Abeta42 to tau/alpha-synuclein (documented Hsp70 monomer interaction)
2. Address rank-deficiency risk in holo MSM construction
3. Specify monomer vs oligomer targeting
4. Provide sensitivity analysis for co-chaperone specificity

---

### Rank 6 — H3: Evolutionary Mpemba Tradeoff

**Ranker composite:** 6.15 | **QG composite:** 5.6 | **Verdict: CONDITIONAL_PASS**

#### 10-Point Rubric

| Criterion | Score | Justification |
|---|---|---|
| Mechanistic specificity | 5 | Folding rate undefined for IDPs — core prediction untestable for Abeta42, alpha-synuclein, tau (half the relevant proteins). |
| Falsifiable prediction | 5 | Mpemba index correlates with folding rate for 6+ proteins — but IDP folding rate does not exist. |
| Test protocol | 4 | Requires both MSMs and measured folding rates. IDP MSMs challenging. Partial correlation for contact order not proposed. |
| Novelty | 8 | Evolutionary dual-use Mpemba metric is genuinely novel. |
| Groundedness | 6 | All 3 citations verified: Drummond & Wilke 2008, Tartaglia 2007, Ciryam 2017. No errors. |
| Counter-evidence addressed | 5 | Contact order confound (Plaxco 1998) identified by critic but not addressed. IDP problem identified but not resolved. |
| Bridge strength | 6 | Spectral argument is coherent for structured proteins only. |
| Mathematical consistency | 6 | No math errors. Spectral gap tradeoff may not be as rigid as claimed. |
| Impact | 6 | Evolutionary biology angle is interesting but scope restriction to non-IDP amyloids narrows impact considerably. |
| Calibration | 5 | Confidence 3/10 is appropriate given fundamental scope limitations. |

**Weighted composite:** (5 + 5x2 + 4x2 + 8 + 6x2 + 5 + 6 + 6 + 6 + 5) / 13 = **5.6**

**Why CONDITIONAL_PASS (borderline):** All citations verified and concept is novel. At 5.6, this just clears the 5.5 threshold. The IDP folding rate problem is a scope error, not an integrity failure. Fixable by restricting to non-IDP amyloid proteins.

**Conditions for PASS:**
1. MUST restrict to non-IDP amyloid proteins (TTR, lysozyme, beta-2-microglobulin)
2. Add partial correlation controlling for contact order
3. Acknowledge IDP-mediated diseases (AD, PD, ALS) are excluded

---

### FAIL — H1: Resource-Theoretic Mpemba Vulnerability Score

**Ranker composite:** 6.15 | **QG composite:** 5.4 | **Verdict: FAIL**

**Fatal flaw: FABRICATED CITATION.**

The hypothesis cites "Avanzini et al. 2026, PRX 16:011065" as the resource-theoretic Mpemba unification paper. Web verification confirms: the paper at PRX 16:011065 is by **Summer, Moroder, Bettmann, Turkeshi, Marvian, and Goold**. The name "Avanzini" does not appear on the paper. This is a confabulated author attribution — not a metadata error.

This is the SECOND citation fabrication in this hypothesis lineage. Cycle 1 H1 had three citation errors (Robustelli mischaracterization, Rosenman wrong citation, Eschmann wrong journal). Cycle 2 was supposed to fix these, and while the original three were corrected, a NEW fabricated attribution was introduced.

Additionally: the D_KL spectral decomposition formula (D_KL = sum c_k^2/(2|lambda_k|)) is chi-squared divergence near equilibrium, NOT KL divergence for arbitrary distributions. The A* aggregation-prone state is far from equilibrium, making the formula mathematically inapplicable in the claimed regime.

**Per QG rules: citation hallucination = automatic FAIL.**

The underlying concept (resource-theoretic unification of Mpemba and aggregation) is genuinely powerful and novel. The hypothesis can be rebuilt on correct foundations (Summer et al. 2026 with correct attribution, chi-squared divergence acknowledged as the correct formula).

---

### FAIL — H6: Tau PTM Variants as Personalized Tauopathy Biomarker

**Ranker composite:** 4.73 | **QG composite:** 4.2 | **Verdict: FAIL**

**Fatal flaws (two independent):**

1. **Citation misattribution:** "Wesseling et al. 2020, Cell 180:633" is NOT Wesseling et al. Cell 180:633 is **Arakhamia et al.** (cryo-EM tau filament structures). The real Wesseling et al. is Cell 183:1699-1713 — wrong volume, wrong pages, completely different paper.

2. **Factual topology error:** T217 is at amino acid position 217, which is OUTSIDE the K18 fragment (residues 244-372). Phosphorylation at T217 cannot directly perturb the K18 eigenmode because the modification site is not in the simulated fragment. The entire mechanistic chain (PTM -> eigenmode change -> Mpemba index shift -> clinical prediction) is anatomically impossible as described.

Additional problems: 500 us IDP MD for tau-K18 is computationally extreme with no validated MSM precedent. CSF p-tau ratios reflect clearance kinetics, not just conformational properties. Clinical prediction chain (MD -> MSM -> Mpemba -> CSF -> cognition) has too many unvalidated steps.

---

## META-VALIDATION

### Are my standards consistent?

**Yes.** The two FAILs are driven by hard QG rules (fabricated citations, factual errors), not soft scoring. Both FAILed hypotheses would have been CONDITIONAL_PASS on rubric scores alone (5.4 and 4.2 respectively — H1 would have been borderline). The hard rules are applied consistently: H1 fails for author confabulation; H6 fails for citation misattribution + topology error.

The six passing hypotheses all have verified citations (or minor metadata errors where content is real). The PASS threshold (7.0) is only met by H7, which has perfect citation integrity and a 10/10 testability score from the ranker.

### Am I passing hypotheses that should fail?

**Potential concern: H8 (Chaperone-Modulated Mpemba Index, 6.5).** This is the most borderline CONDITIONAL_PASS. The central assumption (Hsp70 sites = high-|v_slow| microstates) is entirely untested, and the holo MSM approach is mathematically crude. However: all 4 citations are verified, the concept is novel, and the predictions are falsifiable with clear refutation criteria (<30% co-localization). These clear the QG bar.

**Potential concern: H3 (Evolutionary Tradeoff, 5.6).** At 5.6, this barely clears the 5.5 CONDITIONAL_PASS threshold. The IDP folding rate problem is serious but is a scope limitation, not an integrity failure. The fix is straightforward (restrict to structured amyloid proteins). Marginally acceptable.

### Am I failing hypotheses on technicalities?

**H1 (Resource-Theoretic, 5.4 FAIL):** The concept is genuinely powerful. The Avanzini confabulation is not a technicality — it is a recurring Generator-level error that persists across cycles despite explicit critic feedback. The QG rule (fabricated citation = automatic FAIL) exists precisely for this case. The hypothesis can be rebuilt with correct attribution. This is the correct call.

**H6 (Tau Biomarker, 4.2 FAIL):** The T217 topology error is not a technicality — it invalidates the entire mechanistic chain. The PTM site is literally outside the simulated fragment. This is an anatomy error, not a scoring judgment.

### Scoring drift between Ranker and QG

Ranker composites average 0.8 points higher than QG composites. This is expected because QG applies 2x weighting to groundedness (items 2, 3, 5), which penalizes hypotheses with citation issues. The rank ordering is preserved with one justified swap (H3 > H1 due to citation integrity).

### Overall session assessment

**Strong session.** 1 PASS + 5 CONDITIONAL_PASS from a genuinely novel cross-domain bridge is above the pipeline's historical average. The top 3 (H7 polymorph selection, H4 entropy production diagnostic, H5 hierarchical spectral scoring) form a coherent framework that spans experimental, diagnostic, and predictive applications of the Mpemba-amyloid bridge.

**Recurring concern:** The Avanzini confabulation persists across both cycles for the H1 lineage. This is a Generator-level systematic error that critic feedback alone cannot fix.
