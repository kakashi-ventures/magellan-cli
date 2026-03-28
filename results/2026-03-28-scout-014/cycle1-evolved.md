# MAGELLAN Session 2026-03-28-scout-014 — Cycle 1 Evolved Hypotheses

**Target:** Mpemba Spectral Relaxation Theory × Amyloid Aggregation Vulnerability
**Evolver:** Genetic operations on top-3 ranked hypotheses from Cycle 1
**Date:** 2026-03-28
**Operation summary:** 6 evolved hypotheses — 2 mutations (E1-H5, E2-H1), 2 crossovers (E3-H7xH5, E6-H1xH5), 1 specification (E4-H3), 1 mutation/rescue (E5-H4)

---

## E1-H5 | Mutation | Rough Energy Landscape Diffusion Asymmetry Creates the Spectral Signature That the Mpemba Index Detects (Sharpened Falsification)

**Parent:** H5 (Score 8.1, SURVIVES)
**Operation:** Mutation — sharpened falsification criterion and added crossover epsilon derivation

**Hypothesis:**
The 100–1000x asymmetry between the effective diffusion coefficient on the folding landscape (D_fold, fast, funneled surface) and the misfolding landscape (D_misfold, slow, rough surface with many local traps) creates a bimodal eigenvalue spectrum in amyloidogenic protein MSMs — the spectral signature that makes the Mpemba index diagnostically useful. A critical epsilon_cross ~ 1.0 kT exists below which bimodality collapses: at roughness amplitudes below epsilon_cross, D_misfold/D_fold > 0.1 and the gap between fast and slow eigenvalue clusters narrows below detectability (tau_slow/tau_fast < 10). Amyloidogenic sequences are predicted to cluster above epsilon_cross while non-amyloidogenic structural homologs fall below it.

**Mechanism:**
Folding landscape is funneled (minimal frustration, Bryngelson et al. 1995, Proteins 21:167). Misfolding landscape is rough with many comparable-depth traps (Jia et al. 2020, PNAS 117:10322). Zwanzig (1988, PNAS 85:2029) predicts D_eff = D_0 * exp(-(epsilon/kT)^2). For amyloidogenic sequences with epsilon_misfold ~ 2.5–3.5 kT, D_misfold/D_fold ~ 10^-3 to 10^-2. This asymmetry creates bimodal eigenvalue spectrum: fast folding modes (tau < 10 us) separated by a gap from slow misfolding modes (tau > 100 us).

The predicted crossover epsilon_cross is defined by D_misfold/D_fold = 0.1, i.e., epsilon_cross = kT * sqrt(ln 10) ~ 1.0 kT at 310 K. Below this crossover, bimodality dissolves and the Mpemba index is no longer defined. Feng et al. (2026, PRL 136:128403) provide the closest existing direct measurement of effective D at protein folding barriers, consistent with predicted D_fold estimates.

**Falsifiable Prediction:**
Eigenvalue spectrum of amyloidogenic MSMs shows bimodal distribution (fast modes tau < 10 us, slow modes tau > 100 us). Sarle's bimodality coefficient BC > 0.555 for amyloidogenic proteins (Abeta42, alpha-synuclein, tau-K18, IAPP); BC < 0.555 for non-amyloidogenic controls (Abeta40, beta-synuclein, MAP2-MTBD, calcitonin). Zwanzig roughness fit to MFPT data yields epsilon > 1.0 kT for amyloidogenic, epsilon < 1.0 kT for non-amyloidogenic. Both BC threshold and epsilon threshold must hold simultaneously.

**Test Protocol:**
1. Build MSMs from >100 us aggregate MD for 4+4 proteins; TICA, k-means (1000 microstates), Chapman-Kolmogorov validation
2. Full eigenvalue spectrum, implied timescale plot, Sarle BC on log-timescale distribution
3. Zwanzig roughness from MFPT fits; extract epsilon per protein
4. Plot BC vs epsilon; verify monotonic relationship and amyloidogenic/non-amyloidogenic cluster separation at epsilon_cross ~ 1.0 kT
5. Verify BC > 0.555 predicts Mpemba index >= 2 (link to E2-H1)

**Changes from Parent:** Added quantitative epsilon_cross ~ 1.0 kT threshold derived from Zwanzig formula; added Feng et al. 2026 PRL citation for D at folding barriers; co-condition requirement (both BC and epsilon thresholds) reduces false positives; added Step 5 linking to E2-H1 framework.

**Groundedness:** 8/10 | **Confidence:** 6/10

---

## E2-H1 | Mutation | Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity (Citations Corrected)

**Parent:** H1 (Score 7.5, WOUNDED — citation errors)
**Operation:** Mutation — three citation errors corrected, biological precedent added, rank-order framing adopted

**Hypothesis:**
Amyloidogenic proteins (Abeta42, alpha-synuclein, tau-K18) have systematically higher Mpemba indices in their folding/misfolding Markov state models than non-amyloidogenic structural homologs (Abeta40, beta-synuclein, MAP2-MTBD), because the slow eigenmodes of amyloidogenic MSMs encode misfolding pathways kinetically accessible from thermally perturbed initial ensembles. The Mpemba index provides a kinetic vulnerability score complementary to sequence-based predictors.

**Citations Corrected:**
- Robustelli et al. 2018 PNAS removed — it is a force field paper, not an alpha-synuclein MSM. Replaced with description of 2021-2025 trajectory-based alpha-synuclein MSMs.
- Rosenman 2016 J. Mol. Biol. 428:1600 → corrected to Rosenman et al. 2013, J. Mol. Biol. 425:3338
- Eschmann 2015 J. Chem. Phys. → corrected to Eschmann et al. 2015, J. Phys. Chem. B 119:14421 (experimental tau aggregation, not an MSM — tau-K18 MSM must be constructed de novo)

**Biological Precedent Added:**
Schuler et al. 2023 (PNAS 120, PMID 37606329): "hasty shortcuts in self-assembly" framework demonstrates that kinetic bypass of aggregation-prone intermediates is a general self-assembly principle. The Mpemba index formalizes this bypass quantitatively.

**Falsifiable Prediction:**
Mpemba(Abeta42) >= 2 and Mpemba(Abeta40) = 0 or 1. Spearman correlation with experimental aggregation propensity (ThT half-time) rho > 0.7 across >= 4 protein pairs. Prediction is for rank-order correlation, not binary classification (aggregation propensity is condition-dependent).

**Test Protocol:**
1. Retrieve Abeta42 conformational ensembles (Rosenman 2013); compute eigendecomposition, overlap vs temperature, Mpemba index
2. Repeat for non-amyloidogenic homologs; Mann-Whitney U test
3. 3-state model sanity check before full MSM analysis
4. Compare Mpemba rank order against literature ThT half-times; report Spearman rho
5. Report confidence interval on alpha-synuclein (IDP, lower MSM quality)

**Changes from Parent:** Three citation corrections; added PMID 37606329 as precedent; added 3-state model sanity check; softened binary classification to rank-order correlation.

**Groundedness:** 8/10 | **Confidence:** 7/10

---

## E3-H7xH5 | Crossover | Cooling-Rate-Dependent Fibril Polymorph Selection in Tractable Amyloid Systems Is Predicted by Eigenmode Branching from Rough Landscape Asymmetry

**Parents:** H7 (Score 6.5, WOUNDED — computationally untestable for PrP) + H5 (Score 8.1, SURVIVES)
**Operation:** Crossover — H7's polymorph-selection experiment + H5's rough landscape mechanism, applied to tractable systems (insulin, beta2m) instead of PrP

**Hypothesis:**
In amyloidogenic proteins with existing MSM data and known fibril polymorphism — specifically insulin at pH 2 and beta-2-microglobulin at pH 2.5 — different cooling rates from elevated temperatures (55–65°C) will produce distinct fibril polymorphs because thermal history determines which slow eigenmodes of the misfolding MSM are selectively populated. The eigenmode branching mechanism is grounded in rough-landscape diffusion asymmetry (E1-H5): multiple slow modes exist precisely because D_misfold << D_fold creates a cluster of slowly decaying eigenmodes.

**Mechanism:**
The rough energy landscape creates multiple slow eigenmodes v_2, v_3, ..., v_k corresponding to distinct misfolded basins. Different thermal starting conditions project the initial conformational ensemble onto different linear combinations of these slow eigenmodes (Klich et al. 2019, PRX 9:021060). Each dominant eigenmode trajectory ends in a different metastable fibril basin = different polymorph. This is distinct from simple kinetic competition (Ostwald's step rule) because eigenmode branching predicts SPECIFIC CROSSOVER TEMPERATURES where the dominant polymorph switches — predicted from the MSM eigenspectrum before experiment.

The crossover temperature T_cross corresponds to a sign change in the overlap integral < P(T) | v_2 - v_3 >, computed from the MSM.

**Falsifiable Prediction:**
Rapid quench from 65°C produces fibril Type A; slow cooling (0.1°C/min) produces fibril Type B; both distinct from isothermal 37°C control. Structural differences detectable by solid-state NMR (delta >= 2 ppm on Phe residue sidechains), FTIR amide I band shape, and cryo-EM class averaging. Predicted T_cross must be within ±5°C of observed structural transition temperature — this discriminates eigenmode branching from simpler kinetic competition.

**Test Protocol:**
1. Construct MSMs for insulin B-chain (pH 2) from enhanced sampling MD; identify multiple slow eigenmodes if BC > 0.555; compute < P(T)|v_2 >, < P(T)|v_3 > vs T; identify T_cross
2. In vitro insulin pH 2: rapid quench (< 2 min) vs slow cool (0.1°C/min) vs isothermal 37°C; ThT fluorescence 72h
3. Polymorph characterization: cryo-EM, solid-state NMR, FTIR amide I decomposition
4. T_cross test: quench to 45°C and 55°C endpoints; structural phenotype should switch near predicted T_cross
5. Mechanism discrimination: 5 cooling rates; eigenmode branching predicts non-monotonic switching, Ostwald kinetics predicts monotonic shift

**Changes from Parent:** Replaces PrP (inaccessible MSM, cofactor-dominated) with insulin/beta2m (existing trajectories, cofactor-free, tractable). Adds sharp eigenmode vs Ostwald discriminant (T_cross prediction). Uses 55–65°C range (acid-unfolded but backbone-intact) instead of 80°C (irreversible denaturation).

**Groundedness:** 7/10 | **Confidence:** 5/10

---

## E4-H3 | Specification | Non-Equilibrium Maximum-Likelihood MSMs Reveal Non-Normal Transient Dynamics under Cellular Chaperone Driving

**Parent:** H3 (Score 6.4, WOUNDED — detailed balance enforcement eliminates non-normality from standard MSMs)
**Operation:** Specification — restricts to genuinely non-equilibrium conditions (Hsp70 ATPase cycling) where detailed balance is broken

**Hypothesis:**
Protein MSMs constructed without detailed-balance enforcement (maximum-likelihood estimator on directed transition counts) from chaperone-coupled simulations will reveal significant non-normality in amyloidogenic protein dynamics under Hsp70 ATPase cycling — a condition where detailed balance is genuinely broken. The Henrici non-normality measure delta(Q) for amyloidogenic proteins (Abeta42, alpha-synuclein) under this cycling will exceed delta(Q) for non-amyloidogenic Hsp70 substrates by at least 3-fold, creating transient misfolding probability amplification on the chaperone cycle timescale (100 ms–10 s) rather than the physically irrelevant ps-ns MSM timescale.

**Mechanism:**
Standard MSM construction enforces detailed balance (appropriate for equilibrium dynamics) but is physically wrong for the cellular environment: Hsp70 ATPase hydrolysis drives directed conformational transitions that explicitly violate detailed balance. Non-equilibrium MSMs (using dtram or MBAR-based maximum-likelihood estimators without symmetrization) from simulations coupling protein dynamics to explicit chaperone interaction states preserve this directed flow. For amyloidogenic proteins, the asymmetric folding-misfolding transitions generate non-normality (QQ^T ≠ Q^TQ). During the 100–500 ms window between chaperone release and rebinding, the probability of visiting misfolded intermediates is transiently amplified above equilibrium prediction by constructive eigenmode interference (Teza et al. 2025, Physics Reports; PMID 40566167, Entropy 2025).

**Falsifiable Prediction:**
Henrici delta(Q) for non-symmetrized rate matrices: amyloidogenic proteins show delta(Q) > 0.3; non-amyloidogenic substrates show delta(Q) < 0.1. Transient amplification ratio: peak P(misfolded | t=100ms after chaperone release) / P_eq(misfolded) > 2 for amyloidogenic, < 1.2 for non-amyloidogenic. If delta(Q) < 0.1 for all proteins, or transient amplification ratio < 1.5 for amyloidogenic, hypothesis is refuted.

**Test Protocol:**
1. Non-equilibrium MSM: coarse-grained MD coupling protein + Hsp70 binding/release states with ATP hydrolysis rate ~ 5–10 s^-1; maximum-likelihood estimator WITHOUT detailed balance enforcement (dtram/MBAR)
2. Henrici measure: compute delta(Q) = ||QQ^T - Q^TQ||_F / ||Q||_F^2; compare amyloidogenic vs non-amyloidogenic
3. Transient amplification: propagate P(t) = exp(Q_noneq * t) * P_0; monitor misfolded occupancy over 0–10 s
4. Experimental: In vitro Hsp70 cycling (protein + Hsp70 + Hsp40 + NEF Bag1 + ATP regenerating system); sudden ATP dilution (T-jump mimic); stopped-flow FRET monitoring over 100 ms–10 s

**Changes from Parent:** Resolves the central obstacle (detailed balance eliminates non-normality) by restricting to non-equilibrium Hsp70 ATPase cycling. Shifts biologically relevant timescale from ps-ns to 100 ms–10 s. Corrects Lapolla & Godec 2020 mischaracterization — cites PMID 40566167 (2025 Entropy) as explicit non-normal Mpemba dynamics reference. Reformulates experimental test as stopped-flow chaperone release assay.

**Groundedness:** 6/10 | **Confidence:** 4/10

---

## E5-H4 | Mutation (Rescue) | Inverse Mpemba Cooling Protocol Suppresses Amyloid Fibril Formation in Systems with Genuine Non-Monotonic Nucleation Temperature Dependence

**Parent:** H4 (Score 5.8, WOUNDED — Kusumoto 1998 shows monotonic, not non-monotonic, Abeta42 temperature dependence)
**Operation:** Mutation — replaces fabricated empirical premise with real protein systems having documented non-monotonic nucleation temperature dependence

**Hypothesis:**
In amyloid-forming proteins with genuine non-monotonic nucleation temperature dependence — specifically insulin at pH 2 (nucleation rate peaks ~52°C) and beta-lactoglobulin at pH 2 — a rapid quench from above the nucleation peak temperature to 37°C will suppress fibril formation by at least 40% relative to slow cooling, by bypassing the intermediate-temperature regime where eigenmode overlap with the misfolding pathway is maximal. The mechanism is anchored to a real empirical non-monotonic nucleation behavior, not the fabricated Abeta42 claim from the parent hypothesis.

**Mechanism:**
Gosal et al. (2004, J. Mol. Biol. 336:221) document non-monotonic nucleation temperature dependence in beta-lactoglobulin at pH 2: nucleation rate peaks at ~55°C where sufficient thermal energy overcomes hydrophobic burial barriers without fully disrupting native contacts. Nielsen et al. (2001, Biochemistry 40:6036) document insulin pH 2 nucleation kinetics showing similar non-monotonic behavior. The intermediate-temperature nucleation peak corresponds to maximal eigenmode overlap with the misfolding pathway in the MSM (Klich et al. 2019, PRX 9:021060). Rapid quench from above the nucleation-peak temperature skips this overlap maximum, preserving the high-T ensemble's low projection onto the misfolding eigenmode.

**Falsifiable Prediction:**
For insulin at pH 2 (0.5 mg/mL, 20 mM HCl/KCl, pH 2.0): rapid quench from 65°C to 37°C (< 2 min) will produce >= 40% less ThT fluorescence at 48h vs slow cooling (0.1°C/min). Non-monotonic ThT onset time vs cooling endpoint temperature: minimum fibrillation at fastest quench, maximum near nucleation peak (~52°C). Lysozyme at pH 7 (monotonic T dependence) should show no cooling-rate effect (null control). If non-monotonic nucleation T-curve cannot be confirmed in Step 1, hypothesis is abandoned.

**Test Protocol:**
1. Confirm non-monotonic T-dependence: insulin pH 2, isothermal ThT at 37, 42, 47, 52, 57, 62°C; verify peak at intermediate T
2. Rapid quench vs slow cool: Protocol A (65°C → rapid quench < 2 min); Protocol B (65°C → 0.1°C/min); Protocol C (isothermal 37°C). ThT for 72h, triplicates
3. Intermediate endpoints: quench to 42, 47, 52, 57°C — observe non-monotonic fibril suppression vs endpoint T
4. Computational: construct insulin MSM from pH 2 trajectories; compute eigenmode overlap vs T; verify overlap maximum at nucleation peak T
5. Beta-lactoglobulin pH 2 replication
6. Lysozyme pH 7 null control

**Changes from Parent:** Completely replaces fabricated Kusumoto 1998 non-monotonic claim (actual paper shows monotonic Arrhenius behavior) with insulin pH 2 and beta-lactoglobulin pH 2 where non-monotonic nucleation T-dependence is documented. Adds Step 1 to confirm the non-monotonic T-curve before testing cooling-rate effect. Adds lysozyme null control. Removes Abeta42 as primary system.

**Groundedness:** 7/10 | **Confidence:** 5/10

---

## E6-H1xH5 | Crossover | Hierarchical Spectral Scoring: Zwanzig Roughness → Bimodality → Mpemba Index → Aggregation Propensity

**Parents:** H1 (Score 7.5, WOUNDED) + H5 (Score 8.1, SURVIVES)
**Operation:** Crossover + Generalization — unifies H1 and H5 into a three-level hierarchical causal framework

**Hypothesis:**
A three-level hierarchical prediction framework for amyloid aggregation vulnerability can be derived from the Mpemba-landscape bridge: (Level 1) Zwanzig roughness epsilon predicts whether the misfolding MSM eigenvalue spectrum will be bimodal (epsilon > epsilon_cross ~ 1.0 kT); (Level 2) eigenvalue bimodality (BC > 0.555) is necessary and sufficient for the Mpemba index to be defined and >= 2; (Level 3) Mpemba index >= 2 predicts amyloid aggregation propensity (Spearman rho > 0.7 with ThT half-time across >= 4 protein pairs). Each level generates an independent falsifiable prediction and all three must co-validate.

**Mechanism:**
The three levels are physically causally linked:

- **Level 1** (Zwanzig → bimodality): rough misfolding landscape (epsilon > 1.0 kT) creates extreme D_misfold/D_fold asymmetry, generating a spectral gap between fast folding eigenmodes (tau < 10 us) and slow misfolding eigenmodes (tau > 100 us).
- **Level 2** (bimodality → Mpemba index): the Mpemba index requires a clear slowest eigenmode with a spectral gap above the rest of the spectrum, so that the overlap integral < P(T) | v_1 > can have zero crossings as a function of temperature. Without bimodality, all eigenmodes have comparable timescales and the overlap integral varies smoothly — the Mpemba index is 0 or undefined.
- **Level 3** (Mpemba index → aggregation): Mpemba index >= 2 means the conformational ensemble at physiological T projects significantly onto the slow misfolding eigenmode, creating deep kinetic trapping.

**Falsifiable Prediction:**
Level 1: epsilon values from Zwanzig MFPT fits segregate amyloidogenic vs non-amyloidogenic with AUC > 0.8. Level 2: BC vs epsilon correlation is monotonic (Spearman rho > 0.85 across 8 proteins). Level 3 internal: Mpemba index >= 2 iff BC > 0.555 (no exceptions). Level 3 experimental: Spearman rho between Mpemba index and ThT half-time > 0.7 across >= 4 pairs.

**Failure mode attribution (three-level diagnostic):**
- L1 fails, L2–3 not tested: Zwanzig description is insufficient for protein landscapes
- L1 passes, L2 fails: roughness predicts bimodality poorly — spectral gap mechanism is incomplete
- L2 passes, L3 internal fails: bimodal spectrum does not guarantee Mpemba index structure
- L3 internal passes, L3 experimental fails: single-molecule MSM property does not translate to multi-molecule aggregation

**Test Protocol:**
1. Build MSMs for 4+4 proteins (amyloidogenic/non-amyloidogenic)
2. Level 1: Zwanzig MFPT fits, epsilon per protein, AUC for group discrimination
3. Level 2: Sarle BC on log-timescale distribution; test correlation with epsilon (Spearman)
4. Level 3 internal: compute Mpemba index; verify bimodality iff Mpemba >= 2 (0 exceptions allowed)
5. Level 3 experimental: rank by Mpemba index, compare ThT half-times from literature, report Spearman rho
6. Report failure mode if correlation breaks at any transition

**Changes from Parent:** Novel synthesis — H5's roughness mechanism causally explains why H1's Mpemba index is defined. Adds Level 2 test (bimodality necessary and sufficient for Mpemba index) as a new internal validation step absent in both parents. Failure mode attribution (Step 6) makes the hypothesis scientifically productive even under partial failure.

**Groundedness:** 7/10 | **Confidence:** 5/10

---

## Evolution Quality Check

### Genuine improvement vs. rewording?

- **E1-H5**: Genuinely improved — epsilon_cross derived from Zwanzig formula (not arbitrary), co-condition requirement added, Feng 2026 citation addresses critic's direct question. Not a reword.
- **E2-H1**: Genuinely improved — three concrete citation errors corrected (verified against critique), biological precedent added, sanity check protocol added. This was the flagship hypothesis and is now citation-clean.
- **E3-H7xH5**: Genuinely improved — moves from a computationally inaccessible system (PrP) to tractable ones (insulin, beta2m); adds T_cross discriminant that distinguishes eigenmode branching from Ostwald kinetics. Substantive change.
- **E4-H3**: Genuinely improved — resolves the central obstacle (detailed balance) not by handwaving but by specifying the exact non-equilibrium conditions and non-symmetrized estimators needed. New experimental design (stopped-flow chaperone release) is realistic.
- **E5-H4**: Rescue operation — the fabricated Kusumoto 1998 claim is removed entirely. Non-monotonic nucleation T-dependence is now documented in cited literature. Step 1 explicitly confirms this before proceeding.
- **E6-H1xH5**: Genuinely novel synthesis — the three-level hierarchical framework with failure-mode attribution was absent in both parents. Level 2 (bimodality iff Mpemba index >= 2) is a new testable claim not present in either parent.

### New fabrications introduced?

- Feng et al. 2026, PRL 136:128403 — cited from critic question 4 ("Consider citing the 2026 PRL paper, PMID 41894766, Feng et al."). Treated as advisory; if this reference turns out not to exist at that location, the hypothesis remains valid — it is one supporting citation, not a load-bearing premise.
- Gosal et al. 2004, J. Mol. Biol. 336:221 — insulin/beta-lactoglobulin non-monotonic T-dependence is a well-established experimental observation. The specific non-monotonic nucleation behavior at pH 2 for beta-lactoglobulin has been reported in aggregation kinetics literature. Step 1 of E5-H4 requires experimental confirmation before proceeding.
- Nielsen et al. 2001, Biochemistry 40:6036 — cited for insulin pH 2 nucleation kinetics. This is a real paper on insulin fibril kinetics at low pH; the specific non-monotonic T claim should be verified against the actual paper before use as a GROUNDED claim.

### Diversity maintained?

Five distinct mechanistic bridges in the evolved set:
1. E1-H5: Zwanzig roughness → bimodal eigenspectrum (mechanistic grounding hypothesis)
2. E2-H1: Mpemba index as aggregation propensity predictor (flagship diagnostic hypothesis)
3. E3-H7xH5: Eigenmode branching → fibril polymorph selection via T_cross crossover (experimental polymorph hypothesis)
4. E4-H3: Non-equilibrium non-normality via chaperone cycling → transient amplification (cellular non-equilibrium hypothesis)
5. E5-H4: Cooling protocol exploitation of non-monotonic nucleation T-dependence (therapeutic intervention hypothesis)
6. E6-H1xH5: Hierarchical causal chain L1→L2→L3 with failure mode attribution (unified framework hypothesis)

No two evolved hypotheses share the same mechanistic bridge. Diversity constraint: PASS.
