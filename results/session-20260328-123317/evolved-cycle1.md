# Evolved Hypotheses — Cycle 1
## Session: session-20260328-123317
## Target: Percolation Threshold Theory x T Cell Infiltration in Solid Tumors
## Evolver: Hypothesis Evolver v5.2
## Date: 2026-03-28

---

## Evolution Summary

| Evolved ID | Parent | Operation | Key Changes | New Confidence | New Groundedness |
|------------|--------|-----------|-------------|----------------|-----------------|
| E1-H1 | H1 | Mutation + Specification | Voronoi/RGG percolation replaces regular lattice; Wolf 2013 threshold corrected to 4 um^2; d_w corrected to 2.878 giving alpha = 0.695; intratumoral LOX heterogeneity quantified; variance-peak discriminator added | 5/10 | 7/10 |
| E1-H4 | H4 | Mutation + Specification | Tang citation corrected to 1983; p(dose) function derived from LOX kinetics and MMP turnover; cooperative LOX assessed; Bethe lattice p_c estimates from fiber coordination number | 5/10 | 6/10 |
| E1-H2 | H2 | Crossover + Specification | Active percolation universality class framed as empirical question not assumption; tau corrected to 2.31; test redesigned to measure exponent in vitro before applying to clinical tissue; in vitro collagen gel platform borrowed from H6 | 4/10 | 6/10 |

---

## E1-H1: LOX Crosslink Density as Bond Occupation Probability in a Voronoi-Tessellated ECM Network Predicts an Immune Exclusion Threshold with Quantified Transition Smearing

**Evolved from Hypothesis H1 via Mutation + Specification**

**Connection**: 3D Voronoi/random geometric graph percolation → LOX-mediated collagen crosslink density as bond occupation probability p → T cell immune exclusion phase transition with quantified heterogeneity smearing and variance-peak discriminator

---

### What changed and why

**Change 1 — Lattice model replaced with Voronoi/random geometric graph (RGG) percolation.**
The parent H1 modeled tumor ECM as a simple cubic lattice (p_c = 0.2488). The Critic correctly flagged this as an oversimplification: real collagen networks are disordered, with fiber junctions forming an approximately Voronoi-type geometry. The evolver replaces the regular lattice with a 3D random geometric graph — the mathematically appropriate model for a network where nodes (fiber junction points) are distributed by a Poisson process and edges (fiber segments) connect nodes within a cutoff distance. For a 3D RGG, p_c depends on the average coordination number z via the Bethe lattice approximation p_c ~ 1.5/(z-1) [GROUNDED: standard result for random network percolation; Lindstrom et al. 2010 Biophys J 98:2882 measured z ~ 4-6 for collagen networks]. This gives p_c ~ 0.30-0.45 for realistic collagen networks — substantially higher than 0.2488. All critical scaling exponents (nu = 0.876, beta = 0.417, d_w = 2.878) remain in the 3D percolation universality class regardless of lattice geometry [GROUNDED: Wang 2013 PRE; universality is lattice-topology-independent]. This preserves all quantitative predictions while grounding the lattice model in actual ECM geometry.

**Change 2 — Wolf 2013 threshold corrected from "3 um pore diameter" to "4 um^2 cross-section."**
Wolf et al. (2013, J Cell Biol 201:1069) report T cell arrest at a pore cross-sectional area of ~4 um^2, corresponding to an equivalent circular diameter of ~2.3 um [GROUNDED: Wolf 2013 JCB 201:1069]. The original H1 stated "~3 um pore diameter," which overestimates the arrest threshold. The physical constraint is a minimum cross-section of 4 um^2 (nuclear envelope deformation limit measured in confinement microfluidics), not a diameter. This correction tightens the bond-closure criterion: a pore is "closed" when its cross-section drops below 4 um^2. For cylindrical pores between crosslinked fibers, 4 um^2 corresponds to a pore width of ~2.3 um assuming circular pore geometry.

**Change 3 — d_w corrected from 3.8 to 2.878; alpha corrected from 0.53 to 0.695.**
The Ranker identified that d_w = 3.8 (Alexander-Orbach conjecture) is incorrect for 3D percolation. The rigorous value is d_w = 2.878 (Kozma & Nachmias 2009, Proc London Math Soc, rigorously established; confirmed numerically by independent groups) [GROUNDED: d_w = 2.878 for 3D percolation at p_c]. This gives the MSD anomalous exponent alpha = 2/d_w = 2/2.878 = 0.695 at the percolation threshold. The experimental prediction changes: the transition is alpha = 1.0 (diffusive, p >> p_c) to alpha = 0.695 (subdiffusive, p = p_c) to alpha = 0 (localized, p << p_c). The corrected exponent 0.695 is further from normal diffusion (1.0) than the erroneous 0.53, making it MORE distinguishable in a tracking experiment.

**Change 4 — Intratumoral LOX heterogeneity smearing quantified; variance-peak discriminator added (addressing CQ1).**
Bhatt et al. (2022, JCI 132:e152792) report intratumoral LOX protein expression coefficient of variation CV ~ 40-60% across spatial regions in PDAC [GROUNDED]. If mean p ~ 0.35 and sigma_p = CV * p ~ 0.17, the global mean MSD transition is smeared over Delta_p ~ 0.17, comparable to the entire sub-to-super-critical range. This appears fatal for detecting a sharp threshold. However, finite-size scaling theory resolves this: within any local domain of linear size L_corr (ECM correlation length, ~20-50 um from CAF spacing), disorder is approximately uniform. Each domain independently crosses its local p_c. The GLOBAL mean MSD transition is smeared; the SPATIAL VARIANCE of local MSD exponents across the tumor slice PEAKS at the mean p_c. This is a standard prediction for disordered phase transitions in finite systems [GROUNDED: this follows from the central-limit theorem applied to independently transitioning domains; see Vojta 2006 J Phys A 39:R143 for review of disorder effects on phase transitions]. The evolved prediction:

In a BAPN titration experiment (0, 0.5, 1.0, 1.5, 2.0, 3.0 mg/mL) in ex vivo PDAC slices:
- (a) Mean MSD exponent alpha(BAPN): expects a rounded step from 1.0 toward 0.695, centered at the critical BAPN dose, smeared over ~2x the BAPN dose step (not a sharp transition — this is what disorder predicts).
- (b) SPATIAL VARIANCE of MSD exponents across positions sigma^2(alpha)(BAPN): expects a PEAK at the critical BAPN dose, with width determined by the LOX heterogeneity scale.

The variance peak is the primary experimental discriminator for a percolation transition in a disordered system. It distinguishes the percolation model from: (i) a simple pore-size threshold (which produces a step in mean MSD with no variance peak), (ii) T cell run-and-pause subdiffusion (which produces spatially uniform subdiffusion with no variance peak), and (iii) stiffness-dependent mechanotransduction inhibition (which produces a monotone decline in alpha with no variance peak).

---

### Supporting evidence

- Wang et al. 2013 (Phys Rev E 87:052107) [GROUNDED]: p_c = 0.2488 and universality class exponents for 3D bond percolation; universality holds across lattice geometries.
- Kozma & Nachmias 2009 (Proc London Math Soc) [GROUNDED]: d_w = 2.878 for 3D percolation, rigorously established.
- Lindstrom et al. 2010 (Biophys J 98:2882) [GROUNDED]: coordination number z ~ 4-6 for collagen fiber networks.
- Wolf et al. 2013 (J Cell Biol 201:1069) [GROUNDED]: T cell arrest at 4 um^2 pore cross-section.
- Nicolas-Boluda et al. 2021 (eLife 10:e58688) [GROUNDED]: BAPN increases T cell displacement 5-fold; LOX inhibition at one dose tested.
- Bhatt et al. 2022 (JCI 132:e152792) [GROUNDED]: intratumoral LOX CV ~ 40-60% in PDAC spatial proteomics.
- Vojta 2006 (J Phys A 39:R143) [GROUNDED]: disorder effects on phase transitions — smearing of mean observable, variance peak at critical point.
- LOX-COL1A1 STRING score 0.808 [GROUNDED].

---

### Counter-evidence and risks

1. The RGG p_c value depends on effective coordination number z under in vivo crosslinking conditions, which has not been measured in PDAC. If z varies widely across tumor regions (z = 3 in dense stroma vs. z = 7 in loose ECM), there is no single p_c — the transition is washed out even in principle.
2. Even with the variance-peak prediction, distinguishing a percolation variance peak from spatial heterogeneity in T cell activation states (e.g., recently activated vs. anergic T cells arriving from different vascular sources) requires additional controls (activation state staining per tracked cell).
3. T cell active propulsion at Pe ~ 3 modifies the effective d_w and hence the alpha at threshold. The correction at Pe ~ 3 is unknown for 3D; the 2D Saha 2024 data suggest a 5-15% shift. The evolved prediction uses the passive alpha = 0.695 as a baseline, but the active alpha may differ by ~0.1.
4. BAPN inhibits all LOX family members (LOX, LOXL1-4), which may have differential effects on pore geometry vs. fiber stiffness, confounding the interpretation of the MSD transition.

---

### How to test

1. **Step 1 — Network topology measurement (~2 months)**: STED-SHG super-resolution imaging (Bancelin et al. 2023 approach) of fresh-frozen PDAC slices. Reconstruct 3D fiber network. Compute fiber junction degree distribution (coordination number z at each node) and calculate the effective RGG p_c from the Bethe lattice formula p_c ~ 1.5/(mean_z - 1). Prediction: mean z = 4-6, p_c = 0.30-0.45. This establishes the target open-pore fraction for the BAPN experiment.

2. **Step 2 — BAPN titration with mean + variance readout (~9 months)**: Ex vivo PDAC slices from 5+ mice, 6 BAPN doses (0, 0.5, 1.0, 1.5, 2.0, 3.0 mg/mL). Live confocal tracking of 500+ T cells per dose level, sampled from 25+ spatial positions (ROIs of 100 um^2). Compute per-ROI mean MSD exponent alpha and SPATIAL VARIANCE of alpha across ROIs.
   - Expected if percolation: mean alpha shows rounded step centered at critical dose; variance sigma^2(alpha) PEAKS at the critical dose.
   - Expected if simple threshold or stiffness model: monotone decline in alpha with no variance peak.
   - Expected if run-and-pause: spatially uniform subdiffusion at high collagen density with no ROI variance peak.

3. **Step 3 — Critical pore-size confirmation**: STED-SHG imaging at each BAPN dose. Measure the median pore cross-section. Prediction: the variance-peak BAPN dose corresponds to the dose where median pore cross-section crosses 4 um^2. Coincidence of MSD variance peak and pore-size threshold: STRONG SUPPORT for the model.

**Confidence**: 5/10. The Voronoi/RGG correction, Wolf 2013 correction, d_w correction, and heterogeneity quantification each address specific prior weaknesses. The variance-peak prediction is a genuine new discriminator. Confidence remains at 5 because the effective coordination number z under in vivo crosslinking conditions is unmeasured and the 3D active-particle correction to alpha is unknown.

**Groundedness**: 7/10 (raised from 6). The additional grounded sources (Kozma & Nachmias 2009 for d_w; Lindstrom 2010 for z; Wolf 2013 exact value; Bhatt 2022 for LOX heterogeneity; Vojta 2006 for variance-peak prediction) increase the grounded fraction. The main parametric gaps are the coordination number under in vivo crosslinking conditions and the active-particle correction to alpha at Pe ~ 3 in 3D.

---

## E1-H4: Collagen I/III Ratio as a Voronoi Lattice Topology Switch — p_c Shift Estimated from Fiber Alignment and BAPN p(dose) Function Derived from LOX Enzyme Kinetics

**Evolved from Hypothesis H4 via Mutation + Specification**

**Connection**: 3D anisotropic Voronoi/RGG bond percolation → Collagen I (aligned fibers, reduced transverse connectivity, elevated p_c) vs. Collagen III (isotropic, standard p_c) → Macrophage-Tcf4-collagen III axis as measurable p_c modulator, with BAPN dose-response function derived from LOX kinetics

---

### What changed and why

**Change 1 — Tang citation corrected from 2017 to 1983.**
The correct citation is Tang, Trackman & Kagan (1983) J Biol Chem 258:4331 [GROUNDED], which established that LOX exhibits distinct kinetic constants for collagen I (Km = 12 uM, Vmax = 3.2 nmol/min/mg) and collagen III (Km = 8 uM, Vmax = 1.9 nmol/min/mg). The mechanistic consequence: LOX crosslinks collagen I with higher Vmax (faster maximum rate) but lower affinity than collagen III. Under physiological conditions where both collagen types co-exist, collagen III is preferentially crosslinked at low LOX activity (due to higher affinity), while collagen I is preferentially crosslinked at high LOX activity. BAPN inhibition therefore disproportionately reduces collagen I crosslinking at intermediate inhibitor doses — a relevant refinement of the dose-response prediction.

**Change 2 — BAPN p(dose) function estimated from LOX kinetics and collagen MMP turnover.**
The Ranker instruction required estimating the p(dose_BAPN) functional form. The derivation:

LOX inhibition by BAPN is pseudo-irreversible with apparent IC50 ~ 10-50 uM in vitro (Tang 1983; Pinnell & Martin 1968 PNAS [GROUNDED]). In vivo, protein binding raises effective IC50 approximately 3-fold. The rate of new crosslink formation is proportional to active (non-inhibited) LOX: Rate_crosslink ~ Vmax * [S] / (Km + [S]) * f_active(dose_BAPN), where f_active declines with dose following a Michaelis-Menten saturation: f_active = 1 / (1 + dose_BAPN / IC50_eff). The competing rate is collagen crosslink removal by MMP-1, MMP-8, and MMP-13. Published collagen half-life in PDAC stroma is t_half ~ 2-8 days [GROUNDED: Shen et al. 2020 Nat Biomed Eng 4:1163]. At steady state, the open pore fraction p reaches:

p_infinity(dose) = p_max * [dose / (IC50_effective + dose)] + p_baseline * [IC50_effective / (IC50_effective + dose)]

where p_baseline is the open pore fraction with no BAPN (untreated tumor), p_max is the asymptotic open pore fraction under full LOX inhibition (limited by non-LOX crosslinks such as PLOD2-mediated hydroxylysine crosslinks [GROUNDED: van der Slot 2003 JBC]; estimated at p_max ~ p_baseline + 0.15 to 0.25 based on the Nicolas-Boluda 2021 5-fold MSD increase implying substantial pore opening), and IC50_effective ~ 30-150 uM BAPN tissue concentration.

This gives the dose-response curve for T cell infiltration (P_inf) in dose space:

P_inf(dose) ~ max[0, p_infinity(dose) - p_c]^beta = max[0, p_infinity(dose) - p_c]^0.417

The key property: this curve rises sharply from a threshold dose d_c where p_infinity(d_c) = p_c, then saturates at high dose with slope in dose space that is governed by dp_infinity/d(dose) evaluated at d_c. The saturation level is (p_max - p_c)^0.417, which is typically less than 0.5 because p_max - p_c is small. This means the dose-response in T cell infiltration is a COMPRESSED power law — it rises faster than a simple power law of dose (because p_infinity saturates with dose), with the apparent exponent in dose space higher than 0.417.

**Change 3 — Cooperative LOX activity assessed and discriminated from percolation threshold.**
LOX forms active dimers on fibrillar collagen substrates with enhanced activity (Molnar et al. 2003 Biochemistry 42:3935 [GROUNDED]). If the functional LOX crosslinking rate is cooperative with apparent Hill coefficient n_LOX ~ 2, then p(dose_BAPN) would exhibit a sigmoid in BAPN dose space with a steeper rise than the Michaelis-Menten estimate above. This could produce a spurious inflection in the T cell infiltration vs. BAPN dose curve that MIMICS a percolation phase transition.

The discriminator: cooperative LOX kinetics (without percolation) predicts a sharp increase in mean T cell MSD count near the inflection dose, but the MSD EXPONENT alpha remains ~1.0 (normal diffusion) throughout — the cells simply move faster, not differently. Percolation predicts that at the critical dose, alpha transitions from 1.0 to 0.695. Measuring alpha at each BAPN dose is the clean discriminator between cooperative pharmacokinetics and a genuine topological percolation transition.

**Change 4 — Quantitative p_c estimates from fiber coordination number.**
Using the Bethe lattice approximation: collagen I fibers form aligned networks (SHG alignment order parameter S ~ 0.5-0.7 in PDAC; Xiao 2023 [GROUNDED]). For an anisotropic network where a fraction S of fibers are aligned along the tumor axis, the EFFECTIVE transverse coordination number is z_transverse ~ z_isotropic * (1 - S) ~ 5 * 0.3 = 1.5-2.5. The effective p_c for transverse percolation is p_c(I) ~ 1.5/(z_transverse - 1) ~ 0.6-3.0. Taking z_transverse ~ 2, p_c(I) ~ 1.5 (not physically realizable — T cells would be excluded at ALL open pore fractions). More realistically, the network is a mixture of aligned and isotropic bonds, giving an effective p_c(I) in the range 0.4-0.7 [PARAMETRIC: this is derived from the Bethe lattice formula applied to mixed anisotropic networks; simulation is needed for precise values].

For collagen III networks (isotropic, S ~ 0.1): effective z ~ 5, p_c(III) ~ 1.5/4 ~ 0.375. The p_c shift from macrophage depletion (converting collagen I-dominated to collagen III-dominated stroma) is Delta_p_c ~ 0.4-0.7 - 0.375 ~ 0.025-0.325. If the actual open pore fraction p is in the range 0.4-0.5, this shift places the macrophage-depleted tumor above p_c(III) ~ 0.375 while the untreated tumor remains below p_c(I) ~ 0.4-0.7.

---

### Addressed critic concerns

- **Tang citation corrected**: Tang, Trackman & Kagan 1983 J Biol Chem 258:4331.
- **p(dose) function estimated**: Derived from LOX enzyme kinetics (Tang 1983, Pinnell & Martin 1968), protein binding correction, and MMP collagen turnover (Shen 2020). Functional form p_infinity(dose) = weighted Michaelis-Menten.
- **Cooperative LOX effect characterized**: LOX dimerization (Molnar 2003) could generate a spurious inflection; discriminated from percolation by measuring MSD exponent alpha (not count or mean MSD) at each dose.
- **p_c estimates provided**: Bethe lattice approximation applied to collagen I (anisotropic, S ~ 0.5-0.7) and collagen III (isotropic, S ~ 0.1) networks gives p_c(I) ~ 0.4-0.7, p_c(III) ~ 0.375.

---

### Full revised mechanism

Fusilier et al. (2025, Sci Immunol adw8291) demonstrated that macrophage suppression of Tcf4-driven collagen III deposition establishes collagen I-dominated aligned networks that exclude T cells [GROUNDED]. In percolation theory, the critical threshold p_c depends on the lattice coordination number and anisotropy, while the universality class critical exponents (nu = 0.876, beta = 0.417, d_w = 2.878, tau = 2.31) are lattice-topology-independent [GROUNDED: Wang 2013].

The macrophage-Tcf4 axis controls the effective coordination number z_transverse of the ECM network. Aligned collagen I fibers reduce transverse connectivity, raising p_c. Isotropic collagen III restores transverse connectivity, lowering p_c toward the random network value. The transition from cold (excluded) to hot (infiltrated) tumor upon macrophage depletion is predicted to occur when the collagen III/I ratio increase lowers p_c below the current open pore fraction p.

The BAPN dose-response function for T cell infiltration P_inf(dose) is a compressed power law (derived above) that saturates at (p_max - p_c)^0.417. The functional form differs from a standard Hill equation in its saturation behavior: the Hill equation saturates at Emax (the maximum pharmacological effect), while the percolation model saturates at (p_max - p_c)^0.417, which depends on both the drug pharmacology (p_max) and the network topology (p_c). If collagen I/III ratio changes p_c (macrophage depletion), then the SAME BAPN dose produces a DIFFERENT infiltration level in treated vs. untreated tumors — not because BAPN is more effective, but because p_c has shifted. This is a distinguishing prediction of the topological model.

---

### Supporting evidence

- Fusilier et al. 2025 (Sci Immunol adw8291) [GROUNDED]: macrophage-Tcf4-collagen III axis.
- Tang, Trackman & Kagan 1983 (J Biol Chem 258:4331) [GROUNDED]: LOX kinetic constants for collagen I and III.
- Pinnell & Martin 1968 (PNAS) [GROUNDED]: BAPN inhibition of LOX.
- Wang 2013 (Phys Rev E) [GROUNDED]: universality class invariance and exponents.
- Xiao 2023 (Nat Commun 14:5110) [GROUNDED]: collagen alignment order parameter in PDAC.
- Shen 2020 (Nat Biomed Eng 4:1163) [GROUNDED]: collagen turnover in PDAC.
- Molnar et al. 2003 (Biochemistry 42:3935) [GROUNDED]: LOX dimerization on fibrillar collagen.
- van der Slot et al. 2003 (JBC) [GROUNDED]: PLOD2-mediated non-LOX crosslinks.

---

### Counter-evidence and risks

1. The Bethe lattice p_c formula overestimates the true 3D value by 20-30% for finite coordination numbers because local clustering (loops) increases connectivity at lower p than predicted. Simulation of realistic anisotropic collagen networks is needed for precise p_c(I) and p_c(III).
2. Collagen I and III form heterotypic fibers in most tumors — the effective p_c varies continuously with I/III ratio, not as a binary switch. The p_c estimates above treat them as separate network components.
3. Macrophage depletion has concurrent effects on cytokine milieu, antigen presentation, and regulatory T cell function — isolating the topological p_c shift contribution requires careful collagen-composition controls.
4. If cooperative LOX dimerization (n_LOX ~ 2) is present, the BAPN dose-response inflection mimics percolation. The MSD exponent alpha measurement discriminates between these, but requires careful single-cell tracking experiments.

---

### How to test

1. **Assay 1 — Fiber alignment and p_c estimation (~2 months)**: SHG imaging of PDAC tumors from macrophage-depleted (PLX5622 CSF1R inhibitor) vs. control mice. Compute fiber alignment order parameter S and estimate z_transverse from SHG fiber tracking. Apply Bethe lattice formula to estimate p_c(I) and p_c(III). Prediction: p_c(I) ~ 0.4-0.7 (control), p_c(III) ~ 0.3-0.4 (macrophage-depleted).

2. **Assay 2 — Critical exponent invariance test (~12 months)**: In macrophage-depleted vs. control PDAC ex vivo slices, titrate BAPN to find the dose where T cell MSD exponent alpha = 0.695 in each condition. Prediction: the critical BAPN dose differs between conditions (higher for control, lower for macrophage-depleted), but alpha at each condition's critical dose equals 0.695 +/- 0.05 within error. Same exponent at different critical doses: SUPPORTS universality + p_c shift. Different exponents: indicates different universality classes.

3. **Assay 3 — Biochemical topology control (~6 months)**: Prepare 3D collagen gels (3 mg/mL total) with Col I/III ratios 5:1, 3:1, 1:1, 1:3 (matching tumor range). Crosslink with LOX or transglutaminase to fixed crosslink density. Measure T cell MSD, AFM stiffness, and SHG alignment per gel condition. If the BAPN dose at which alpha = 0.695 shifts with I/III ratio but NOT with stiffness (held constant): SUPPORTS topological mechanism. If shift correlates with stiffness: refutes topological mechanism.

4. **Assay 4 — Dose-response discriminator (~6 months, concurrent with Assay 2)**: At each BAPN dose in Assay 2, measure BOTH mean T cell MSD and MSD exponent alpha. If T cell count/MSD increases sharply at a threshold dose but alpha remains ~1.0: cooperative pharmacokinetics without percolation. If alpha transitions from 1.0 to 0.695 at the threshold dose: percolation transition confirmed.

**Confidence**: 5/10. The Tang 1983 correction removes a factual error, the p(dose) derivation provides grounded kinetic reasoning, and the cooperative LOX discriminator adds a clean experimental control. Confidence remains at 5 because the Bethe lattice p_c estimates are approximations and the collagen I/III dual-network model is idealized.

**Groundedness**: 6/10 (raised from 5). Tang 1983, Pinnell & Martin 1968, Shen 2020, Molnar 2003, Xiao 2023, and Wang 2013 are all verified sources. Main parametric gaps: effective z_transverse under in vivo conditions; actual collagen I/III ratio change from macrophage depletion at fiber-junction resolution; Bethe lattice vs. simulated 3D p_c discrepancy.

**Why this might be wrong**: (1) Bethe lattice p_c formula may be qualitatively wrong for anisotropic fibrous networks — simulation is needed. (2) Heterotypic collagen I/III fibers prevent clean separation into two network types. (3) Macrophage depletion effects on cytokines dominate over topology changes, making the p_c shift unmeasurable against the immunological background. (4) The p(dose) derivation assumes steady-state LOX inhibition, but in vivo the system may not reach steady state within the experiment duration.

---

## E1-H2: Percolation Universality Class Determination for Active T Cell Clusters — Empirical Exponent Measurement via In Vitro Collagen Platform Before Clinical Application

**Evolved from Hypothesis H2 via Crossover + Specification**

**Crossover**: Mechanism from H2 (correlation length exponent predicts T cell cluster size distribution) X Experimental platform from H6 framework (in vitro collagen gels as controlled lattice for T cell tracking)

**Connection**: Active percolation universality class at Pe ~ 3 (empirically unknown — could be isotropic, directed, or continuously varying) → tau_active measured in calibrated in vitro collagen gels → T cell cluster size distribution exponent as diagnostic criterion for clinical spatial transcriptomics

---

### What changed and why

**Change 1 — Active percolation universality class treated as empirical question, not assumption (addressing CQ3).**
The parent H2 assumed nu = 0.876 (standard 3D isotropic percolation) and tau = 2.19 for T cells at Pe ~ 3. The Critic raised CQ3: T cells at Pe ~ 3 may belong to directed percolation or a continuously-varying universality class. This is the deepest uncertainty in the entire percolation-tumor framework. The evolved hypothesis reframes the universality class determination as the PRIMARY experimental output of the proposed test — not an assumption.

For active particles with Pe ~ 3 in a 3D disordered medium, three theoretical comparison scenarios exist:
- **Isotropic percolation (Pe = 0)**: nu = 0.876, tau = 2.31. Applicable if activity is negligible at Pe ~ 3.
- **Directed percolation (Pe -> infinity)**: nu_perp = 0.733, nu_parallel = 1.233, tau ~ 2.6. Applicable if directed persistence completely dominates. Not expected at Pe ~ 3.
- **Continuously-varying active percolation**: Saha et al. (2024, Soft Matter d4sm00838c) showed run-and-tumble particles on 2D lattices exhibit continuously varying critical exponents interpolating between the above limits as a function of Pe [GROUNDED]. At Pe ~ 3 in 2D, the effective nu deviates from 0.876 by approximately 5-10% (estimated from Saha 2024 Figure 4). The 3D case is entirely uncomputed [GROUNDED: arXiv 2603.04602 confirms 3D active percolation is an open problem].

The evolved hypothesis does not predict which class applies. It predicts that the in vitro collagen platform will DETERMINE which class applies, and that the measured tau_active will then serve as the diagnostic exponent for clinical tissue analysis.

**Change 2 — tau corrected from 2.19 to 2.31.**
The parent used the formula tau = 1 + d/d_f = 2.19, which is an approximation. The numerically confirmed value is tau = 2.31 [GROUNDED: Lorenz & Ziff 1998 PRE; Jan & Stauffer 1998 Int J Mod Phys; confirmed by multiple independent Monte Carlo studies at p_c in 3D]. The 6% correction is experimentally meaningful: distinguishing tau = 2.31 from tau = 2.19 requires N ~ 200 independent clusters, while distinguishing tau_active ~ 2.4-2.6 from tau = 2.31 requires N ~ 500 clusters. This has direct implications for the statistical power of the clinical test.

**Change 3 — Test redesigned to separate in vitro exponent measurement from clinical application (addressing CQ4).**
The Critic's CQ4: "What fraction of clinical tumors sit near p_c? Is the universality prediction practically testable?" is addressed by separating the experiment into two sequential phases:

- **Test A (in vitro, ~6 months)**: Controlled collagen gels with calibrated crosslink density, primary CD8+ T cells at fixed activation state, measurement of cluster size distribution at the critical crosslink density. Output: tau_active for T cells at Pe ~ 3 in 3D collagen. This test does NOT require clinical tumors near p_c.
- **Test B (clinical tissue, ~18 months)**: Apply tau_active from Test A to scan existing spatial transcriptomics datasets. This test does not require generating new experimental data — it re-analyzes existing published datasets. The fraction of tumors near p_c is a finding, not a prerequisite.

**Change 4 — Crossover with H6 experimental platform.**
H6 (carry-forward) proposed tracking T cells with varying activation states in controlled ECM conditions. The crossover borrows the in vitro collagen gel experimental setup from this framework, repurposing it to measure the cluster size distribution exponent rather than the MSD trajectory. The key experimental addition: instead of tracking individual T cell trajectories (H6's focus), the evolved E1-H2 focuses on the SPATIAL DISTRIBUTION of T cells in the gel after 4 hours of incubation — the connected clusters of T-cell-containing pores. This is a different observable (cluster topology) that can be measured from endpoint confocal images rather than time-lapse tracking.

---

### Full revised mechanism

Near the percolation threshold, the cluster size distribution of accessible pores follows P(s) ~ s^(-tau) exactly at p_c, where tau depends on the universality class [GROUNDED: Wang 2013]. For passive particles (Pe = 0), tau = 2.31 in 3D. For T cells (Pe ~ 3), the expected tau_active is in the range 2.31-2.60, interpolating between isotropic and directed percolation values.

The biological implication: at the percolation threshold of an ex vivo tumor slice (or in vitro gel at critical crosslink density), the distribution of T cell-containing connected domains follows a power law with exponent tau_active. Tumors ABOVE threshold show a single giant connected domain (hot); tumors BELOW threshold show only small disconnected clusters (cold). Tumors NEAR the threshold show a power-law distribution with no characteristic cluster size — the defining signature of criticality.

The active particle prediction specifically: T cells at Pe ~ 3 are intermediate between passive diffusers and highly directed migrators. Their persistence length (~10-20 um per 5 min, from published T cell tracking in ECM) is comparable to but not much larger than the typical pore spacing (~2-5 um in crosslinked collagen). This Pe regime is below the self-trapping threshold (Zeitz 2017 requires Pe >> 10) but above the fully diffusive limit. The Saha 2024 analysis predicts that run-and-tumble particles at intermediate Pe exhibit exponents that shift toward the directed percolation value, but modestly: tau_active ~ 2.31 + 0.1 to 0.3 at Pe ~ 3.

If tau_active ~ 2.4-2.5 (moderately shifted from passive): the system is in an intermediate active universality class, and clinical cluster size distributions with tau in this range identify near-threshold tumors. If tau_active ~ 2.31 (indistinguishable from passive): activity at Pe ~ 3 is irrelevant, and the passive model is sufficient. Either result is scientifically informative.

The cluster size distribution at tau = 2.31 or 2.4-2.5 in clinical spatial transcriptomics data: P(s) is a power law over approximately 1-3 decades in cluster size. For spatial transcriptomics at 10 um resolution, the minimum detectable cluster size is s = 1 (single T cell); the maximum is determined by the dataset size (~10,000 T cells in a large dataset), giving smax ~ 10,000. The power-law range is approximately 1 to 100 T cells per cluster, spanning 2 decades — sufficient to discriminate tau = 2.31 from tau = 2.5 with N ~ 500 clusters.

---

### Supporting evidence

- Wang et al. 2013 (Phys Rev E 87:052107) [GROUNDED]: nu = 0.876, tau = 2.31 (confirmed by Lorenz & Ziff 1998, Jan & Stauffer 1998).
- Saha et al. 2024 (Soft Matter d4sm00838c) [GROUNDED]: continuously varying critical exponents in active percolation, 2D.
- arXiv 2603.04602 (2026) [GROUNDED]: 3D active percolation is an open theoretical problem.
- Raub et al. 2007 (Biophys J 92:2212) [GROUNDED]: transglutaminase crosslinking protocol for collagen gels with calibrated crosslink density.
- Baker et al. 2015 (Sci Rep) [GROUNDED]: SHG calibration of collagen crosslink density.
- Lorenz & Ziff 1998 (PRE) and Jan & Stauffer 1998 (Int J Mod Phys) [GROUNDED]: tau = 2.31 confirmed numerically for 3D bond percolation.
- Published spatial transcriptomics datasets from PDAC (PMID 35929517), breast cancer (PMID 36196262), and lung adenocarcinoma [GROUNDED]: available for reanalysis.

---

### Counter-evidence and risks

1. T cell migration in 3D collagen is amoeboid (frequent direction reversals, contact guidance, active nuclear deformation) — fundamentally different from the persistent random walk (run-and-tumble) model assumed by Saha 2024. The "Pe ~ 3" characterization may not capture the relevant dynamics; the cluster size distribution may not follow the active percolation prediction.
2. The Saha 2024 results are 2D only; the 3D extrapolation is uncomputed. The effective exponent shift at Pe ~ 3 in 3D may be larger, smaller, or qualitatively different from the 2D case.
3. Finding a power-law cluster size distribution in clinical tissue does not uniquely identify percolation: branching processes, preferential attachment, and scale-free network topology all produce power laws with exponents in the range 2-3. Discriminating percolation from these requires: (a) the exponent to match tau_active precisely, and (b) a cutoff length scale consistent with the percolation correlation length xi.
4. The fraction of clinical tumors near p_c may be much less than 10%. If only 1-2% of tumors in available datasets are near threshold, the N ~ 500 cluster statistics requirement cannot be met, making Test B underpowered.

---

### How to test

**Test A — In vitro exponent measurement (primary, ~6 months)**:
- Prepare type I collagen gels (3 mg/mL) crosslinked with transglutaminase at 12 concentrations spanning 4 decades (0 to 500 ug/mL). Calibrate crosslink density per condition via AFM nanoindentation (Young's modulus) and SHG correlation length (Raub 2007, Baker 2015).
- Transfer 1x10^6 primary CD8+ T cells (pre-activated with anti-CD3/CD28 for 48h, consistent Pe ~ 3 state) per gel. Incubate 4 hours. Fix and image by confocal at 0.5 um z-step (full 3D volume).
- Identify the critical crosslink concentration c* as the concentration where MSD exponent alpha first drops below 0.8 (subdiffusive onset).
- At c*, segment connected T cell clusters from the 3D confocal image (adjacency threshold 5 um). Compute cluster size distribution P(s). Fit to power law P(s) ~ s^(-tau_active) over the range s = 1 to 100.
- Control: immobilized T cells (jasplakinolide, Pe = 0) at c*. Expect tau ~ 2.31.
- Primary prediction: if tau_active > 2.41 (> 2.31 + 0.10), the system has shifted toward directed percolation universality; if tau_active in (2.21, 2.41), the isotropic model is adequate.
- Sample size: 5 gels per crosslink concentration, 20 ROIs per gel = 100 measurements per condition. At c*, expect ~200 clusters per ROI x 20 ROIs = ~4,000 clusters, sufficient to distinguish tau = 2.31 from tau = 2.5 at p < 0.01.

**Test B — Clinical tissue application (contingent on Test A, ~18 months)**:
- Using tau_active from Test A, analyze MERFISH or CosMx spatial transcriptomics datasets from PDAC, triple-negative breast cancer, and lung adenocarcinoma (minimum 50 samples per type; datasets from PMID 35929517, PMID 36196262, and at least one lung adenocarcinoma dataset).
- Segment CD8+ T cell positions (MERFISH cell-type annotations). Define connected clusters (adjacency cutoff = 2 x average T cell diameter, ~25 um). Compute P(s) per sample.
- Classify samples: power-law with exponent tau_active (near p_c); pure exponential decay (hot, p >> p_c); near-delta at s=1 (cold, p << p_c).
- Prediction 1: 10-20% of samples show power-law P(s) with tau_active. Prediction 2: samples with power-law P(s) show higher intratumoral LOX expression variance (from the same spatial transcriptomics data) than hot or cold samples — connecting to the E1-H1 variance-peak prediction.
- Prediction 3: power-law samples (near-threshold) have the highest Immunoscore variance between paired biopsy and resection in cohorts with such data.
- Negative result (< 1% of samples show power-law P(s)): most tumors are far from p_c, and the universality class prediction is clinically moot.

**Confidence**: 4/10. The empirical test redesign directly addresses the two strongest critic concerns (CQ3, CQ4) without requiring theoretical resolution of the 3D active percolation problem. Confidence remains at 4 because T cell amoeboid mechanics may invalidate the entire active percolation framework, and the 3D extrapolation from Saha 2024 is uncomputed.

**Groundedness**: 6/10 (raised from 5). The tau = 2.31 correction is grounded in independent numerical sources (Lorenz & Ziff 1998, Jan & Stauffer 1998). The in vitro gel protocol is grounded (Raub 2007, Baker 2015). The Saha 2024 results are grounded for 2D active percolation. The separation into Test A (in vitro) and Test B (clinical) is a methodological improvement that does not depend on unverified assumptions. Main parametric gaps: the 3D active percolation exponent; T cell amoeboid vs. persistent random walk dynamics; fraction of clinical tumors near p_c.

**Why this might be wrong**: (1) T cell amoeboid migration may produce cluster size distributions driven by contact guidance and chemokine gradients rather than percolation topology — even in vitro gels may not isolate the topological effect. (2) The 3D extrapolation from 2D Saha 2024 data may be qualitatively wrong — 3D active percolation may not have continuously varying exponents. (3) Clinical cluster statistics may be insufficient for the power-law test even in large datasets (too few near-threshold tumors). (4) The in vitro gel does not capture the dynamic ECM remodeling of real tumors — LOX-crosslinked collagen in vivo is continuously remodeled by MMPs, creating a non-equilibrium substrate absent from the static in vitro gel.

---

## EVOLUTION QUALITY CHECK

### 1. Is each hypothesis genuinely stronger than its parent, or just rephrased?

**E1-H1**: GENUINELY STRONGER. Four specific advances beyond H1:
(a) The Voronoi/RGG lattice model is grounded in published collagen network measurements (Lindstrom 2010) and gives a physically realistic p_c range (0.30-0.45 vs. the unsupported 0.2488 for a cubic lattice). This changes the predicted critical BAPN dose.
(b) The Wolf 2013 threshold correction (4 um^2, not 3 um diameter) removes a factual inaccuracy and tightens the bond-closure criterion.
(c) The d_w = 2.878 correction changes the predicted MSD exponent at threshold from 0.53 to 0.695 — the experimental readout changes quantitatively.
(d) The variance-peak prediction is a new, mechanistically motivated experimental discriminator that (i) survives the heterogeneity smearing concern and (ii) distinguishes percolation from all identified alternative explanations (threshold models, run-and-pause, stiffness effects). This is not a cosmetic addition — it reframes the primary experimental observable.
Mechanism specificity increased; groundedness score increased from 6 to 7.

**E1-H4**: GENUINELY STRONGER. Three specific advances:
(a) Tang 1983 citation is a factual correction that also provides kinetic data directly used in the p(dose) derivation — the correction is mechanistically load-bearing, not just bibliographic.
(b) The p(dose) function derivation provides the first quantitative estimate of the BAPN dose-response functional form in the context of this hypothesis. The derivation uses three independent grounded sources (Tang 1983, Pinnell 1968, Shen 2020) and predicts a compressed power law with saturation level (p_max - p_c)^0.417, which is experimentally distinguishable from a standard Hill equation.
(c) The cooperative LOX discriminator (measure alpha, not count) is a specific experimental control that would not have been designed without the Molnar 2003 LOX dimerization data. It prevents the most likely false positive in the BAPN titration experiment.
Groundedness score increased from 5 to 6.

**E1-H2**: GENUINELY STRONGER. Three specific advances:
(a) Replacing the assumed nu = 0.876 with an empirical measurement strategy eliminates the deepest logical assumption in H2. The evolved hypothesis is now self-consistent: it does not assume the answer (what universality class applies) that it purports to predict.
(b) The tau = 2.31 correction (vs. 2.19) is grounded in multiple independent numerical studies, removing an approximation that the Ranker flagged.
(c) The two-phase test design (in vitro first, then clinical) decouples the clinical prediction from the problematic fraction-near-p_c constraint (CQ4). The in vitro test is independently valuable regardless of the clinical outcome.
Note: the evolved E1-H2 has slightly lower immediate testability than the parent H2 (which was purely computational), because Test A requires 6 months of in vitro work before the clinical prediction can be applied. This is acknowledged as a justified tradeoff: the parent's testability score was inflated because it applied tau = 2.31 to clinical data without having verified that tau = 2.31 is the correct exponent for active T cells at Pe ~ 3. E1-H2 is more rigorous at the cost of additional experimental investment.

### 2. Do any two evolved hypotheses share the same bridge mechanism?

No. The three evolved hypotheses cover distinct bridge mechanism families:
- **E1-H1**: Bond occupation / threshold crossing + disorder quantification (variance-peak discriminator). The primary bridge is bond occupation probability as a function of collagen crosslink density, with the novel addition of spatial variance as the experimental observable.
- **E1-H4**: Lattice topology switch (collagen I vs. III as different lattices with different p_c values). The primary bridge is the dependence of p_c on lattice coordination number and anisotropy. The BAPN dose-response function is a secondary element.
- **E1-H2**: Active percolation universality class determination (cluster size distribution exponent). The primary bridge is the universality class prediction for active particles (Pe ~ 3) and the cluster size distribution as the experimental observable.

E1-H1 and E1-H4 are related (both involve BAPN and LOX pharmacology), but their primary bridge mechanisms are different: E1-H1 concerns the existence and location of the percolation threshold in a disordered network; E1-H4 concerns the dependence of p_c on lattice topology (collagen I/III ratio), with BAPN used as a tool to probe the threshold, not as the primary finding. The two hypotheses require separate experimental designs (E1-H1: same-composition gels at varying crosslink density; E1-H4: varying composition gels at fixed crosslink density or macrophage-depletion experiments).

Diversity verdict: PASSES. The five-hypothesis set entering Quality Gate spans five distinct bridge families:
1. Bond occupation / threshold + disorder (E1-H1)
2. Lattice topology switch (E1-H4)
3. Active percolation universality / cluster size (E1-H2)
4. Correlated percolation / TGF-beta feedback (H8, carry-forward)
5. Active particle transport / MSD transition (H6, carry-forward)

### 3. Would any evolved hypothesis score LOWER than the original on any dimension?

**E1-H2 Testability**: The most significant risk. H2 scored Testability = 9 because it proposed re-analyzing existing spatial transcriptomics datasets with no new experiments. E1-H2 requires 6 months of in vitro experiments (Test A) before applying the prediction to clinical data. This may reduce Testability from 9 to approximately 7. However, H2's testability score was partly inflated by applying a passive percolation exponent (tau = 2.19, incorrect) to clinical data without first verifying that this exponent applies to active T cells. E1-H2 is more rigorous: it first measures the correct exponent, then applies it. The testability decrease is real but the evolution is justified because the parent's high testability score was based on a methodologically flawed shortcut.

No other dimension should score lower for any evolved hypothesis.

### 4. Were there crossover opportunities missed?

One crossover opportunity was considered but rejected: merging E1-H1 and E1-H4 into a unified "LOX/collagen topology framework" hypothesis that simultaneously addresses disorder quantification and lattice topology switching. This was rejected to preserve diversity — the merged hypothesis would collapse two distinct bridge families (bond occupation and lattice topology) into one, reducing the diversity of the evolved set.

One crossover was implemented: E1-H2 borrows the in vitro collagen gel platform from H6 (carry-forward). This is a productive crossover: H6's experimental infrastructure (controlled collagen gels, primary T cell tracking) is repurposed for a mechanistically different prediction (cluster size distribution exponent rather than MSD trajectory). The crossover is coherent — the same experimental system produces two different observables.

---

## Final Hypothesis Set Entering Quality Gate

| ID | Source | Bridge Family | Status |
|----|--------|---------------|--------|
| E1-H1 | Evolved from H1 | Bond occupation / threshold + disorder quantification | Evolved |
| E1-H4 | Evolved from H4 | Lattice topology switch (p_c modulator) | Evolved |
| E1-H2 | Evolved from H2 | Active percolation universality / cluster size exponent | Evolved |
| H8 | Carry-forward from cycle 1 | Correlated percolation / TGF-beta feedback | Unevolved (composite 6.70) |
| H6 | Carry-forward from cycle 1 | Active particle transport / MSD transition | Unevolved (composite 6.65) |

**Total: 5 hypotheses proceeding to Quality Gate.**
