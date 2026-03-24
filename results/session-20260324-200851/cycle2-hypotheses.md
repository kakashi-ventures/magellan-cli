# Cycle 2 Hypotheses — Session session-20260324-200851
## Target: Cryo-EM heterogeneity analysis x OMV cargo sorting
## Building on Cycle 1 evolved hypotheses E1-E4, plus fresh approaches
## Addressing Critic Questions from Cycle 1

---

### Critic Questions Addressed:
1. Continuous vs discrete heterogeneity framework -> C2-H1 addresses with mixture modeling
2. Alternative cargo sorting mechanisms -> C2-H3 (fresh) explores periplasmic chaperone connection
3. Minimum particle count for subtomogram averaging -> C2-H2 addresses quantitatively
4. Orthogonal validation -> Multiple hypotheses include cryo-CLEM, proteomics, genetics

---

## C2-H1: Gaussian Mixture Model Analysis of Cryo-EM OMV Populations Distinguishes Biogenesis Pathways in P. aeruginosa (builds on E3)

**Mechanism**: Instead of forcing discrete RELION 3D classes, apply Gaussian Mixture Model (GMM) analysis to cryo-EM-derived OMV descriptors (diameter, surface roughness, radial density profile, circularity) to test whether OMV populations are best described as discrete modes or a continuum. Use BIC model selection to determine the optimal number of components. If discrete (K>=3, delta-BIC > 10 vs K-1): assign pathway labels by cross-referencing proteomics of SEC-fractionated OMVs. If continuous: report the principal axes of variation and their biological correlates.

**Specific prediction**: BIC-optimal GMM with K>=3 components. Components separable by diameter (component means differ by >30 nm) AND protein-to-lipid ratio (measured by orthogonal MALDI-MS). The smallest component (50-80 nm) is enriched for OprF and depleted of flagellin; the largest (150-250 nm) shows the inverse.

**Bridge**: GMM/BIC model selection is standard in machine learning and has been applied to cryo-EM heterogeneity (RELION) but NEVER to whole-vesicle population analysis. [GROUNDED: RELION uses expectation-maximization which is equivalent to GMM classification]

**Counter-evidence**: OMV heterogeneity may be CONTINUOUS without discrete modes, in which case K=1 or K=2 will have optimal BIC. This would be an important negative result — it would mean cargo sorting occurs at the single-vesicle level, not through distinct biogenesis pathways.

**Test protocol**: (1) Purify P. aeruginosa OMVs by SEC. (2) Cryo-EM: >50,000 particle images. (3) Measure per-particle: diameter, circularity, radial density profile (5 features). (4) Fit GMM with K=1..6, compute BIC. (5) If K>=3: fractionate by SEC, proteomics per fraction, assign pathway labels. (6) Validate: delta-ompA mutant should lose one component (the ompA-tethered budding pathway).

**Confidence**: 7/10
**Groundedness**: 7/10
**Novelty**: 9/10

---

## C2-H2: Power Analysis for Subtomogram Averaging of OMV Budding Intermediates Sets Feasibility Boundary (builds on E1)

**Mechanism**: Before undertaking the expensive cryo-ET campaign proposed in E1, perform a power analysis using existing subtomogram averaging benchmarks. The minimum number of subtomograms needed for a given resolution follows N_min ~ (d/r)^3 * SNR^-2, where d = particle diameter, r = target resolution, SNR = contrast-to-noise ratio. For OMV budding sites (d ~ 50 nm, target r = 3 nm, estimated SNR ~ 0.1 for unstained biological specimens), calculate N_min and compare against achievable yield from stress-induced OMV budding.

**Specific prediction**: N_min for 3 nm resolution of OMV budding sites = 200-500 subtomograms (based on analogous calculations for T4SS at similar size). From sub-MIC gentamicin-stressed P. aeruginosa, ~1-3 budding events per cell in 200 nm thick lamella. To collect 500 subtomograms requires 200-500 cell tomograms. At 20 min per tilt series, this requires 70-170 hours of microscope time. This is FEASIBLE (2-4 weeks on a dedicated microscope) but expensive. If Tol-Pal complex is present at scission sites, the protein density provides additional contrast that reduces N_min by ~2x.

**Bridge**: Power analysis for subtomogram averaging is routine in the cryo-ET field but has NEVER been applied to OMV budding sites. [GROUNDED: Resolution scaling with N established — Schur et al. 2016 Nature, HIV-1 capsid subtomogram averaging]

**Counter-evidence**: The estimated SNR for budding sites may be lower than assumed if no conserved protein structure exists (the null result). In that case, even 1000 subtomograms would produce featureless average, which is itself informative.

**Test protocol**: (1) Compute theoretical N_min from resolution-N relationship. (2) Collect pilot dataset: 20 tilt series of stressed PAO1. (3) Count budding events per tomogram. (4) Extrapolate total required data collection. (5) If feasible: proceed with full dataset. If infeasible: pivot to membrane-only analysis (curvature without protein architecture).

**Confidence**: 8/10
**Groundedness**: 9/10
**Novelty**: 7/10

---

## C2-H3: Periplasmic Chaperone DegP/Skp Co-localization with OMV Cargo Proteins Resolved by Cryo-ET Difference Mapping (FRESH)

**Mechanism**: A completely different approach to cargo sorting: instead of analyzing the membrane directly, investigate whether periplasmic chaperones (DegP, Skp, SurA) co-localize with specific cargo proteins inside OMVs. DegP is a periplasmic protease/chaperone that is one of the most abundant OMV cargo proteins (Schwechheimer & Kuehn 2015). Apply cryo-ET difference mapping: compare tomographic density of wild-type OMVs vs delta-degP mutant OMVs to identify DegP-dependent density features in the periplasmic space and OMV lumen. This tests whether DegP acts as a cargo chaperone that escorts specific proteins into OMVs during budding.

**Specific prediction**: Cryo-ET difference map (WT minus delta-degP) shows localized density loss in the periplasmic face of the outer membrane at budding sites, corresponding to DegP's known hexameric cage structure (~12 nm). The same difference map shows reduced luminal density in OMVs from delta-degP, corresponding to DegP-chaperoned cargo proteins.

**Bridge**: Difference mapping in cryo-ET (comparing WT and mutant tomographic averages) has been used for molecular machine characterization (flagellar components) but NEVER for periplasmic chaperone localization in OMV context. [GROUNDED: DegP presence in OMVs — established. Difference cryo-ET — established for molecular machines]

**Counter-evidence**: delta-degP has pleiotropic effects on the cell envelope (DegP is essential for outer membrane protein quality control). Density differences may reflect global envelope perturbation rather than specific cargo chaperoning. Control: compare with delta-surA (different chaperone, different client proteins) to show specificity.

**Test protocol**: (1) Generate delta-degP and delta-surA mutants in PAO1. (2) Cryo-ET of WT, delta-degP, delta-surA cells. (3) Subtomogram averaging of budding sites and intact OMVs per strain. (4) Compute difference maps: WT - delta-degP, WT - delta-surA. (5) If DegP-dependent density found: dock DegP hexamer structure into difference density. (6) Proteomics of OMVs from each strain to validate DegP-dependent cargo set.

**Confidence**: 6/10
**Groundedness**: 7/10
**Novelty**: 9/10

---

## C2-H4: Machine Learning-Guided Template Matching Identifies OMV Cargo Proteins In Situ Without Labels (FRESH)

**Mechanism**: The fundamental challenge for cryo-ET of OMVs is protein identification without labels. Recent advances in template matching with deep learning (DeePiCt, TomoTwin, TARDIS) can identify proteins in situ by matching to known structures from the PDB. Apply these tools to cryo-ET of P. aeruginosa OMVs: for each OMV in a tomogram, generate a "cargo manifest" by template matching against the P. aeruginosa structural proteome. The hypothesis predicts that template matching will identify specific OMPs and periplasmic proteins with sufficient confidence to distinguish cargo-enriched from cargo-depleted OMV subpopulations.

**Specific prediction**: Template matching with DeePiCt or TomoTwin against P. aeruginosa OMP structures (OprF, OprD, OprH, OprG — structures available in PDB) identifies >=2 OMPs per OMV with cross-correlation score > 0.5 (above noise). Classification of OMVs by their OMP composition reveals at least 2 distinct OMV subtypes differing in their OMP ratios.

**Bridge**: ML-guided template matching in cryo-ET is cutting-edge (2023-2025) and has been applied to cellular tomograms for ribosome identification and membrane protein mapping. Application to OMV cargo identification is COMPLETELY NOVEL. [GROUNDED: DeePiCt — de Teresa et al. 2023 Nat Methods; TomoTwin — Rice et al. 2023 Nat Methods]

**Counter-evidence**: Template matching resolution in tomograms (~20-30 A) may be insufficient to distinguish between similar-sized OMPs (OprF vs OprD, both ~8-barrel with similar dimensions). False positive rates in crowded membrane environments may be high. The P. aeruginosa structural proteome in PDB may be incomplete, limiting the reference library.

**Test protocol**: (1) Cryo-ET of PAO1 OMVs (in situ on bacterial surface + isolated). (2) Run DeePiCt/TomoTwin template matching against PDB structures of PAO1 OMPs. (3) Score per-OMV OMP composition. (4) Cluster OMVs by OMP composition. (5) Validate: compare ML-predicted cargo with proteomics of nanoFACS-sorted OMV fractions. (6) Knockout test: oprD deletion should remove one OMP from ML predictions without affecting other OMP identifications.

**Confidence**: 5/10
**Groundedness**: 7/10
**Novelty**: 10/10

---

## C2-H5: Time-Resolved Cryo-EM of OMV Biogenesis Using Rapid Mixing and Vitrification Captures Cargo Loading Intermediates (FRESH)

**Mechanism**: Existing cryo-EM of OMVs captures only the final product. To observe cargo sorting IN ACTION, use time-resolved cryo-EM: rapid mixing of bacterial cultures with a stress trigger (sub-MIC gentamicin or EDTA) followed by plunge-vitrification at defined time points (10s, 30s, 60s, 120s, 300s after stress). This captures the temporal sequence of OMV biogenesis — from initial membrane perturbation through cargo accumulation to scission. The hypothesis predicts an ordered sequence: (1) membrane curvature initiation at OmpA-depleted zones (<30s), (2) cargo protein accumulation at budding site (30-60s), (3) neck constriction (60-120s), (4) scission and release (>120s).

**Specific prediction**: Time-resolved cryo-EM at 5 timepoints after EDTA stress (which chelates divalent cations stabilizing LPS, triggering rapid OMV release) shows a monotonic increase in budding intermediates per cell: <1 at 10s, 2-5 at 30s, 5-10 at 60s, then decrease as OMVs release (3-5 at 120s, <2 at 300s). Early intermediates (10-30s) show membrane curvature without cargo enrichment; later intermediates (60-120s) show both curvature and cargo accumulation.

**Bridge**: Time-resolved cryo-EM (trapping reaction intermediates by rapid vitrification at defined times) has been used for protein conformational dynamics (Kaledhonkar et al. 2019 Nature, mixing-spraying approach) but NEVER for membrane biogenesis processes. [GROUNDED: Time-resolved cryo-EM methodology — Kaledhonkar et al. 2019]

**Counter-evidence**: The time resolution of plunge-vitrification (~10 ms blotting + 10 ms vitrification) may miss rapid intermediates. EDTA stress may cause non-physiological OMV production that doesn't reflect normal biogenesis. The temporal sequence may not be ordered (stochastic budding at different stages simultaneously in a population).

**Test protocol**: (1) Use microfluidic mixing-spraying device (Kaledhonkar design) adapted for bacterial cells. (2) Mix PAO1 with 1 mM EDTA. (3) Spray onto cryo-EM grids at t = 10, 30, 60, 120, 300 s. (4) Image by cryo-ET. (5) Classify budding intermediates by morphological stage. (6) Plot stage distribution vs time. (7) Quantify cargo density at budding sites per timepoint. (8) Compare with unstressed control (spontaneous budding rate, stage distribution).

**Confidence**: 5/10
**Groundedness**: 7/10
**Novelty**: 10/10

---

## SELF-CRITIQUE (Cycle 2)

### Improvements over Cycle 1:
- Added statistical framework (GMM/BIC) to address discrete vs continuous question (critic Q1)
- Added periplasmic chaperone mechanism (critic Q2 — alternative sorting mechanism)
- Added power analysis for feasibility (critic Q3)
- Added orthogonal validation strategies throughout (critic Q4)
- Fresh hypotheses (C2-H3, C2-H4, C2-H5) use completely different analytical approaches

### Remaining concerns:
- All hypotheses still require cryo-EM/cryo-ET infrastructure — this is inherent to the target
- C2-H4 (ML template matching) depends on cutting-edge tools that may not be fully validated
- C2-H5 (time-resolved) is technically very ambitious — mixing-spraying for bacteria is untested
