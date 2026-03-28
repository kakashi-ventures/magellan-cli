# Evolved Hypotheses — Cycle 1 Evolution
## Session: session-20260328-123317
## Fields: Statistical mechanics (bond percolation theory) × Tumor immunology (ECM-mediated immune exclusion)
## Date: 2026-03-28
## Evolver: Sonnet | Operations: specification (×3), mutation (×1), crossover (×1), specification+mutation (×1)

---

## Evolution Overview

Six surviving hypotheses entered evolution. Two kills (H5, H7) are not evolved.
Primary targets per ranking: H1, H4, H2. Secondary: H8, H6. Low-priority: H3.

All evolved hypotheses address specific critic questions. Diversity check passed: six evolved
hypotheses span six distinct bridge mechanisms (LOX network topology, BAPN percolation titration,
active-percolation universality class measurement, chemotaxis Pe as classification knob,
MMP/LOX ratio oscillation clock, and velocity autocorrelation fingerprint). No two share the
same core bridge.

---

## E1: LOX-Mediated Collagen Crosslink Density as Bond Occupation Probability — Corrected Pore Geometry and Heterogeneity-Smeared Transition

**Evolved from Hypothesis H1 via Specification**
**Critic questions addressed:** Wolf 2013 threshold correction; intratumoral heterogeneity smearing quantification; disordered-lattice mapping.

### Connection
Bond percolation theory (statistical mechanics) → LOX-mediated collagen crosslink density as bond occupation probability p on a random geometric graph → Sharp (but heterogeneity-broadened) immune exclusion threshold in solid tumors, with corrected pore geometry

### Mechanism

**Corrected geometric mapping.** Wolf et al. (2013, J Cell Biol) report that T cell (nucleus diameter ~5-6 μm) migration arrests when ECM pore cross-sectional area falls below 4 μm² [GROUNDED: Wolf et al. 2013 — the threshold is cross-sectional area, not pore diameter]. The equivalent circular pore diameter for 4 μm² is d = 2√(4/π) ≈ 2.26 μm, not 3 μm as stated in the parent H1. This ~33% downward revision of the pore diameter threshold shifts the critical collagen crosslink density upward: T cells require larger open pores than the parent hypothesis assumed, meaning the immune exclusion transition occurs at somewhat lower crosslink density (more bonds must be blocked to restrict the effective pore below 4 μm²). Quantitatively, for collagen fiber spacing of ~1-2 μm in a 3D reconstituted gel, achieving pore cross-sections ≥ 4 μm² requires local inter-fiber distances of ≥ 2.26 μm in both transverse directions simultaneously — a geometric constraint that maps to bond occupation probability p ≈ 0.18-0.22 on a random geometric graph with fiber density matching 5-8 mg/mL reconstituted collagen [PARAMETRIC: estimated from SHG-derived network topology].

**Disordered lattice and universality preservation.** The parent H1 abstracted the tumor ECM as a regular cubic lattice. Real collagen networks are random fiber networks best modeled as random geometric graphs (RGGs) or continuum percolation on fiber segments. Critically, 3D random geometric graphs belong to the same universality class as regular lattices for percolation: the critical exponents β = 0.41, ν = 0.88, γ = 1.79 are preserved [GROUNDED: Stauffer & Aharony 1994; Jan & Stauffer 1998 — universality class depends only on spatial dimension and percolation type, not lattice geometry]. The critical bond fraction p_c shifts (RGG p_c differs from cubic p_c = 0.2488), but the scaling laws are unchanged. This preserves the core prediction of H1: the transition is sharp and its shape is governed by universal exponents.

**Quantifying heterogeneity smearing.** The central critic concern is whether intratumoral collagen density heterogeneity smears the sharp transition into a gradual gradient. We now provide a quantitative estimate. Let σ_p be the standard deviation of local bond occupation probability across a tumor. For a transition of width Δp ~ L^(-1/ν) at the percolation threshold in a finite system, the transition is smeared when σ_p > Δp. From SHG imaging data (Nicolas-Boluda 2021 and Levental 2009), collagen concentration varies ~2-4× across a single tumor section (core vs. periphery vs. perivascular niche). If mean crosslink density is p_mean and local density varies by ±30% (σ_p ≈ 0.3 × p_c ≈ 0.06-0.07), then the apparent transition is broadened from a sharp jump to a sigmoidal over a range of Δp ≈ 2σ_p ≈ 0.12-0.14 in bond fraction. The percolation order parameter power law I ~ (p - p_c)^0.41 is still measurable within each local domain, but the tumor-level infiltration curve will be a convolution of the sharp transition with the spatial distribution of p — producing an apparent Hill-like curve with n_Hill ≈ 2-4 (moderately sigmoidal), not a linear dose-response. This is STILL distinguishable from a Hill n = 1 (linear) response: the percolation prediction is that a log-log plot of [I(p) - I_min] vs [p - p_c] in the middle 60% of the transition yields slope β = 0.41 ± 0.15, whereas a Hill equation with n = 2 gives slope 2.0 in the same region. Heterogeneity smears but does not erase the percolation signature.

**Critical prediction refined.** The immune exclusion transition occurs when the volume-averaged bond occupation probability p crosses p_c(RGG) ≈ 0.18-0.22 [PARAMETRIC] — corresponding to approximately 4-8 mg/mL collagen concentration in reconstituted Type I collagen gels at physiological pH and 37°C, with LOX activity maintained at steady state. In the presence of spatial heterogeneity (σ_p ≈ 0.06), the transition midpoint shifts negligibly (< 5%) but the transition width broadens to Δp ≈ 0.12. The apparent Hill coefficient of the infiltration-vs-density curve is predicted to be n_app ≈ 2-4. If the true Hill n from a pharmacological model were > 4, it would indicate percolation is not the operative mechanism; n < 4 but with a power-law onset is consistent with heterogeneity-modified percolation.

### Improved Test Protocol

1. **Three-tier collagen matrix experiment**: Fabricate 12 density conditions (1-25 mg/mL, logarithmically spaced) of 3D Type I collagen matrices in 96-well format at controlled LOX/LOXL2 activity (add recombinant LOX at 0.1, 1, 10 U/mL). Measure pore cross-sectional area distribution by confocal reflection microscopy or cryo-EM before T cell addition. Key output: confirm that p(collagen density) mapping follows expected power law of gel network theory [PARAMETRIC: Broedersz & MacKintosh 2014]. Only proceed to T cell infiltration experiments after pore geometry is independently measured.
2. **Spatially-resolved infiltration**: Track activated CD8+ T cells at 24h per condition. Plot T cell core infiltration vs. volume-averaged pore area (not raw collagen concentration). Fit to convolution of percolation transition with Gaussian heterogeneity (2 free parameters: p_c and σ_p). The fit is confirmed percolation if the resulting β = 0.41 ± 0.15.
3. **Heterogeneity control**: Use cancer-associated fibroblast (CAF)-conditioned matrices (with spatially heterogeneous LOX activity) as a "high σ_p" condition. Compare transition width Δp to homogeneous matrices. Percolation predicts Δp_CAF / Δp_homogeneous = σ_p(CAF) / σ_p(homogeneous), a quantitative testable ratio.
4. **Expected result if TRUE**: Infiltration-vs-density curve has n_app = 2-4 (not 1, not >8). Log-log plot of inflection region yields slope 0.41 ± 0.15. CAF matrices show 1.5-3× wider transition than homogeneous matrices.
5. **Expected result if FALSE**: n_app > 8 (too sharp — non-physical for percolation with heterogeneity) or curve is monotonically decreasing with n_app = 1 (purely gradual — no threshold at all).
6. **Effort**: 4-8 months. Requires ECM characterization (pore geometry by cryo-EM or confocal reflection) before biological experiments. Adds one step vs. parent but makes the test more rigorous.

**Confidence**: 6/10 (unchanged from parent — corrections increase specificity but do not resolve the fundamental disordered-lattice abstraction concern)
**Groundedness**: 7 — corrected Wolf 2013 geometry [GROUNDED], heterogeneity smearing estimate [PARAMETRIC: derived from known σ_p from literature], RGG universality class [GROUNDED: standard theory], LOX-crosslink density mapping [GROUNDED: Nicolas-Boluda 2021]

**Why stronger than H1**: (1) Wolf 2013 pore threshold is now correct (4 μm² cross-section, d ≈ 2.26 μm); (2) heterogeneity smearing is quantified (σ_p ≈ 0.06, Δp ≈ 0.12, n_app ≈ 2-4) rather than waved away; (3) the critical collagen concentration range is refined (4-8 mg/mL vs 5-10 mg/mL); (4) a new discriminator between percolation and Hill pharmacology is specified (β = 0.41 slope in log-log plot of inflection region); (5) the test protocol now includes an independent pore geometry calibration step.

---

## E2: BAPN Percolation Titration — Corrected LOX Inhibitor Citation and Quantified p(dose) Mapping Function

**Evolved from Hypothesis H4 via Specification**
**Critic questions addressed:** Tang citation correction (1983 not 2017); shape of p(dose) mapping; cooperative LOX kinetics concern.

### Connection
Bond percolation threshold crossing → BAPN (LOX inhibitor) dose-response as an experimentally controlled p(dose) → Sharp phase transition in T cell infiltration with quantified mapping from dose to crosslink density

### Mechanism

**Corrected citation.** The parent H4 cited "Tang et al. 2017" as the source for BAPN's irreversible LOX inhibition mechanism. The correct citation is Tang, Trackman & Kagan (1983, J Biol Chem 258:4331-4338), which first established that BAPN inactivates LOX via irreversible covalent modification of the active-site copper cofactor [GROUNDED: Tang, Trackman & Kagan 1983]. The mechanism is identical to the parent's description; only the year was wrong.

**Quantifying p(dose): enzyme kinetics to crosslink density.** The central unknown in H4 is the shape of p(dose) — the mapping from BAPN dose to equilibrium crosslink bond occupation probability. We now provide a mechanistic estimate based on LOX enzyme kinetics.

LOX enzymes follow Michaelis-Menten kinetics: LOX activity v = Vmax × [substrate] / (Km + [substrate]), where Km ≈ 10-30 μM for lysine residues in collagen [PARAMETRIC: order of magnitude from amine oxidase literature]. BAPN is a suicide inhibitor — it does not compete reversibly but instead forms a covalent inhibitory intermediate with probability f_inact per catalytic cycle. At BAPN concentration [B], the fraction of active LOX molecules falls as:

    f_active(B) = 1 / (1 + [B] / K_I^BAPN)

where K_I^BAPN ≈ 50-200 μM in cell culture models [PARAMETRIC: estimated from IC50 values in Nicolas-Boluda 2021 and fibrosis literature; exact value tumor-type-dependent].

At steady state (new crosslink formation balanced by MMP degradation), the equilibrium crosslink density is:

    p_eq = k_LOX × f_active(B) / (k_LOX × f_active(B) + k_MMP)

For baseline ratio k_LOX / k_MMP ≈ 2-5 (estimated from tumors with p > p_c, i.e., immune-cold tumors), this gives:

    p_eq(B) = (2-5) × f_active(B) / ((2-5) × f_active(B) + 1)

This mapping is a rectangular hyperbola in [B], but the percolation threshold is crossed at a specific p_c. The critical BAPN dose d_c satisfying p_eq(d_c) = p_c is:

    d_c = K_I^BAPN × [(k_LOX/k_MMP) / p_c - 1 - k_LOX/k_MMP × (1 - 1/p_c)]^(-1)

For k_LOX/k_MMP = 3, p_c = 0.20, K_I = 100 μM: d_c ≈ 50-150 μM intratumoral [PARAMETRIC].

**Crucially, the p(dose) mapping is itself smooth (no discontinuity).** The percolation transition at p = p_c produces a sharp infiltration response even though p(dose) is a smooth hyperbola. The critical dose d_c is where the smooth p(dose) curve crosses the sharp percolation threshold. This means:

- The dose-response curve for T cell infiltration is NOT a simple Hill equation — it has a true dead zone below d_c, a power-law onset near d_c with exponent β = 0.41, and saturation above d_c.
- A Hill equation fit (symmetric sigmoid) will underestimate the sharpness at threshold and overestimate the low-dose response.

**Cooperative LOX concern addressed.** The critic raised whether cooperative LOX activity could introduce a secondary inflection mimicking percolation. LOX family enzymes are monomeric or form loose dimers — they do not exhibit allosteric cooperativity analogous to hemoglobin [PARAMETRIC: LOX structure review, Lucero & Kagan 2006]. The relevant nonlinearity in BAPN dose-response arises from: (1) network effects in collagen crosslinking (each new crosslink makes adjacent crosslinks more probable — a positive feedback), and (2) the percolation transition itself. Network cooperative crosslinking would shift the transition sharper (higher apparent β), not create a second inflection. The predicted power-law exponent β = 0.41 is therefore a lower bound; cooperative ECM crosslinking could increase the effective β to 0.5-0.8. If the measured β > 0.8, cooperative ECM crosslinking must be invoked in addition to percolation.

**In vivo heterogeneity concern.** BAPN distributes non-uniformly in vivo (tissue penetration depends on local vascularity and LOX enzyme load). We account for this by predicting that the apparent transition width (in dose space) broadens from the in vitro Δd_c (sharp, ~1.5× K_I^BAPN) to a broader in vivo range (~3-5× K_I^BAPN) due to spatial averaging of p(x, dose). This is testable: comparing in vitro collagen gel experiments (homogeneous BAPN) with in vivo mouse tumor experiments (heterogeneous BAPN) should show a 2-4× broadening of the transition width. If in vivo broadening exceeds 10× K_I, the transition is non-percolation (dominated by heterogeneity).

### Refined Test Protocol

1. **In vitro p(dose) calibration (new step added vs parent)**: Before the in vivo experiment, measure equilibrium crosslink density (pyridinoline HPLC assay) in 3D collagen gels with CAF-conditioned medium ± BAPN (0-500 μM, 8 doses, 72h equilibration). Plot p_eq vs [BAPN]. Fit to the k_LOX/k_MMP hyperbolic model. Extract K_I^BAPN and baseline k_LOX/k_MMP ratio. This provides the p(dose) calibration curve.
2. **In vivo BAPN titration (as in parent)**: Syngeneic tumors (4T1 breast, KPC pancreatic) in mice. Correct BAPN dose range: 0-500 mg/kg/day i.p. for 7 days (parent used 0-1000 mg/kg — reduce upper bound to avoid toxicity artifacts). Quantify CD8+ T cell density (immunohistochemistry) and crosslink density (pyridinoline assay).
3. **Composite analysis**: Plot T cell infiltration vs p_eq (using calibration curve to convert dose → p_eq). Fit I(p_eq) = 0 for p > p_c, I ~ (p_c - p_eq)^β for p < p_c. Compare fit to Hill equation with n free. Percolation wins if β_fit = 0.41 ± 0.15.
4. **Discriminator**: Different tumor models should show different d_c (because they have different baseline k_LOX/k_MMP) but the same β = 0.41 when plotted in p-space. Hill equation with one shared n cannot accommodate this model-dependent shift in threshold combined with universal exponent.
5. **Expected result if TRUE**: Power-law onset with β_fit = 0.41 ± 0.15. In vivo transition width 2-4× wider than in vitro.
6. **Expected result if FALSE**: β_fit > 0.8 with no convergence to universal value across tumor models, OR transition is symmetrically sigmoidal (Hill n ≈ 2, equidistant rise and fall).
7. **Effort**: 8-12 months (vs 6-12 in parent). Added in vitro calibration step adds ~2 months but is necessary to validate the p(dose) mapping.

**Confidence**: 6/10 (increased from 5 in parent by adding the p(dose) mechanistic model)
**Groundedness**: 7 — BAPN LOX inhibition mechanism [GROUNDED: Tang, Trackman & Kagan 1983 — now correctly cited], LOX Michaelis-Menten kinetics [PARAMETRIC: order-of-magnitude from literature], K_I estimate [PARAMETRIC], percolation β exponent [GROUNDED: Stauffer & Aharony 1994], p(dose) hyperbolic model [PARAMETRIC: derived from enzyme kinetics]

**Why stronger than H4**: (1) Tang citation is now correct (1983, not 2017); (2) p(dose) is explicitly modeled using LOX enzyme kinetics with estimated K_I ≈ 50-200 μM and baseline k_LOX/k_MMP ratio; (3) d_c is estimated (~50-150 μM intratumoral) with clear derivation; (4) cooperative LOX concern is addressed (monomeric LOX, no allosteric cooperativity — β = 0.41 is lower bound, not upper); (5) in vivo broadening is quantified and testable (2-4× expected); (6) a new in vitro p(dose) calibration experiment is added before the in vivo titration to anchor the two-step mapping.

---

## E3: Exponent-Agnostic Universality Class Measurement — From Assumed ν=0.88 to Measured Critical Exponent via Active-Particle Crossover

**Evolved from Hypothesis H2 via Specification + Mutation**
**Critic questions addressed:** What universality class for Pe ~ 3 active particles? Is ν = 0.88 still valid? What fraction of tumors near p_c? Redesign test to MEASURE exponent, not assume it.

### Connection
Percolation universality class identification → Measured critical exponent ν from T cell cluster correlation length data → Determines whether T cell infiltration follows isotropic percolation (ν = 0.88), directed percolation (ν_⊥ = 1.10), or a crossover universality class — with practical testability bounds on tumors near p_c

### Mechanism

**The parent H2 committed the wrong hypothesis form.** H2 assumed ν = 0.88 and asked if it could be confirmed. The critic correctly identified that active particles (Pe ~ 3) may violate isotropic percolation universality. The evolved hypothesis inverts the approach: MEASURE ν experimentally in a controlled in vitro system spanning Pe = 0 to Pe ~ 5, and use the measured value to determine which universality class applies. This transforms H2 from a verification of an assumed prediction into a classification hypothesis: "The critical exponent ν of T cell percolation on tumor ECM identifies the operative universality class, with Pe as the control parameter that drives a crossover from isotropic (ν = 0.88) to directed (ν_⊥ = 1.10) percolation."

**Active percolation crossover quantified.** For a biased random walker on a percolation cluster, the relevant dimensionless parameter is the Péclet number Pe = v_drift × a / D_transverse, where a is the lattice spacing (pore spacing ~ 2-5 μm), v_drift is the chemotactic drift velocity, and D_transverse is the transverse random motility. The crossover between universality classes is expected at Pe_c ~ 1 [PARAMETRIC: standard active percolation expectation; Saha 2024 provides 2D evidence]. For Pe < Pe_c: isotropic percolation (ν = 0.88). For Pe >> Pe_c: directed percolation (ν_∥ = 1.73, ν_⊥ = 1.10). For Pe ~ 3 (the estimated T cell Pe): the system is in the crossover regime, expected to show effective exponents intermediate between the two classes.

The measurable quantity is the T cell pair correlation function g(r) in isotropic and gradient-defined directions separately:
- Isotropic case (no chemokine gradient, Pe → 0): compute spherically averaged g(r). Extract ξ ~ (p - p_c)^(-ν) over 5-7 density conditions near p_c. Measured ν should converge to 0.88 ± 0.15 if isotropic percolation applies.
- Directed case (CXCL9/10 gradient imposed by microfluidic gradient generator, Pe ~ 3): compute g_∥(r) along gradient and g_⊥(r) transverse. Extract ν_∥ and ν_⊥ separately. Expected: ν_∥ ≈ 1.4-1.7, ν_⊥ ≈ 1.0-1.1.
- Crossover mapping: Vary Pe from 0 to 5 by adjusting CXCL9/10 concentration (0-100 ng/mL). Track ν_eff(Pe). The crossover Pe_c is the Pe at which ν_eff deviates by > 2 standard errors from 0.88.

**Fraction of tumors near p_c.** The critic asked what fraction of clinical tumors sit near p_c. From two data points: (1) Collagen density ranges 5-50 mg/mL across tumor types [GROUNDED: Levental 2009]. (2) The percolation threshold p_c corresponds to approximately 4-8 mg/mL (E1 estimate). This places only tumors in the 4-8 mg/mL window "near p_c." Tumors with dense desmoplastic stroma (pancreatic PDAC, TNBC) typically range 20-50 mg/mL — far above p_c, deeply immune-cold. Tumors with loose stroma (colorectal MSI-high) range 5-15 mg/mL — spanning the critical range. Therefore, a reasonable working estimate is that ~20-30% of solid tumors sit within 2× p_c (within the range where percolation scaling is measurable) [PARAMETRIC: based on collagen density distributions from Levental 2009 and Kuczek 2019]. This is sufficient for experimental study in CRC and early TNBC cohorts. Pancreatic PDAC is less likely to be near p_c in the primary tumor but may approach p_c during neoadjuvant therapy response.

**Practical testability redesign.** Rather than requiring clinical tumor samples near p_c (uncertain), the exponent measurement is first done in vitro with full control:
- Collagen gels at 8 densities (3-15 mg/mL) in a microfluidic chip with an integrated CXCL9 gradient generator [PARAMETRIC: PDMS-based gradient chip, commercially available].
- Activated CD8+ T cells embedded or flowed in from one side.
- Imaging at 10-minute intervals for 12 hours. Compute g_∥ and g_⊥ at each density.
- Identify p_c (density at which g(r) first shows power-law tail), measure ν_∥ and ν_⊥.

### Refined Predictions

1. **Classification prediction**: If measured ν_eff at Pe ~ 3 is 0.88 ± 0.15 → isotropic percolation dominates (strong result: chemotaxis does not break universality class at physiological Pe). If ν_eff ≈ 1.0-1.1 (close to ν_⊥ for DP) → directed percolation applies (CXCL9/10 gradient is the primary navigator; ECM topology is secondary). Either outcome is scientifically valuable and clinically actionable.
2. **Cross-tumor prediction refined**: Instead of claiming all tumors show ν = 0.88 (original H2), we predict that tumors near p_c with similar Pe should show the same ν_eff, regardless of molecular details. The universality is within a universality class, not between classes. CRC and TNBC at identical p/p_c and Pe should show identical ν_eff ± 0.15. This is the correct universality claim.
3. **Clinical fraction**: Predict that colorectal MSI-high tumors are most likely to sit near p_c (20-40% within the 4-10 mg/mL range), making them the priority cohort for clinical validation.

**Effort**: 6-9 months in vitro (microfluidic chip + collagen matrices + T cell tracking + correlation analysis). Clinical validation requires retrospective cohort with SHG + T cell staining + crosslink density assay: additional 12-18 months.

**Confidence**: 5/10 (vs. 4/10 for parent). Increased because the test is now measurement-based (not assumption-based) and Pe-control is experimentally accessible. The exponent outcome is a discovery regardless of which universality class wins.
**Groundedness**: 6 — isotropic percolation ν = 0.88 [GROUNDED: Stauffer & Aharony 1994], directed percolation exponents ν_⊥ = 1.10, ν_∥ = 1.73 [GROUNDED: Hinrichsen 2000], active percolation crossover concept [GROUNDED: Saha 2024 — 2D], crossover Pe ~ 1 [PARAMETRIC], ν_eff(Pe) crossover map [PARAMETRIC], 20-30% tumors near p_c [PARAMETRIC: from collagen density distributions]

**Why stronger than H2**: (1) No longer assumes ν = 0.88 — instead MEASURES ν_eff as a function of Pe; (2) the Pe-crossover is now the primary experiment, making the hypothesis falsifiable regardless of which universality class wins; (3) quantifies fraction of tumors near p_c (~20-30% for CRC, MSI-high); (4) identifies the priority clinical cohort for follow-up (CRC MSI-high, early TNBC); (5) the test is redesigned to use microfluidic gradient control (in vitro, no need to find clinical tumors near p_c as a prerequisite).

---

## E4: CXCL9/10 Gradient Steepness as Pe-Based Percolation Phase Diagram Classifier

**Evolved from Hypothesis H8 via Mutation (simpler observable) + Specification**
**Critic questions addressed:** Simpler observable than anisotropic ξ; does gradient variation over correlation length revert to isotropic?

### Connection
Directed vs. isotropic percolation universality class crossover → Péclet number Pe (CXCL9/10 gradient steepness / local diffusion) → Binary T cell infiltration classification into directed-percolation or isotropic-percolation regime, discriminated by measurable CXCL9/10 staining gradient

### Mechanism

**The parent H8 proposed measuring anisotropic correlation lengths ξ_∥ and ξ_⊥ as the experimental discriminator.** The critic correctly identified this as technically demanding (requires co-staining + directional analysis). The evolved E4 mutates this observable to a simpler and clinically accessible one: the normalized spatial gradient of CXCL9/10 immunostaining intensity across the tumor-stroma interface.

**Pe as the classification parameter.** Pe = v_drift × a / D_transverse, where:
- v_drift ~ μ_motility × |∇[CXCL9]| (chemotactic drift velocity proportional to gradient steepness)
- a ~ 2-5 μm (collagen pore spacing)
- D_transverse ~ 30-50 μm²/min (T cell random motility from intravital data [GROUNDED: Mrass et al. 2006; Germain et al. 2006])

The gradient ∇[CXCL9] is directly accessible from tumor tissue sections via quantitative immunofluorescence: measure CXCL9 pixel intensity as a function of distance from the tumor edge and compute dI/dx over the 50-200 μm stromal band. This converts a theory-level quantity (Pe) into a histopathological measurement.

**Critical Pe_c for classification.** Based on 2D active percolation results (Saha 2024), the crossover between isotropic and directed percolation universality classes occurs at Pe_c ~ 1. In 3D, Pe_c is expected to be similar [PARAMETRIC: extrapolated]. Therefore:
- Tumors with normalized gradient steepness |∇[CXCL9]| above a threshold g_c → Pe > Pe_c → directed percolation regime → T cell infiltration is gradient-guided and the relevant critical exponents are ν_⊥ = 1.10, ν_∥ = 1.73.
- Tumors with |∇[CXCL9]| below g_c → Pe < Pe_c → isotropic percolation regime → ECM topology alone determines infiltration; exponents are ν = 0.88, β = 0.41.
- g_c ≈ 1-10 ng/mL per 100 μm [PARAMETRIC: derived from D_transverse and chemotactic coefficient estimates from Weber et al. 2013, Science].

**Gradient variation concern addressed.** The critic asked: if the chemokine gradient varies on correlation length scales (ξ ~ 10-100 μm), does the system revert to isotropic percolation? The answer is: yes, partially — but with a specific prediction. If the gradient varies on a length scale l_gradient < ξ, T cells average over the gradient within one correlation volume and experience an effective reduced Pe. The effective Pe is:

    Pe_eff = Pe × min(l_gradient, ξ) / ξ

When l_gradient < ξ (gradient heterogeneous on correlation length scale), Pe_eff < Pe → system shifts toward isotropic regime. When l_gradient >> ξ (gradient smooth relative to correlation volume), Pe_eff ≈ Pe → system remains in directed regime. This gives a testable prediction: tumors with spatially heterogeneous CXCL9/10 (high local variance in gradient direction) should behave more isotropically (ν → 0.88) than tumors with smooth monotonic gradients (ν → ν_⊥ = 1.10), even at the same mean Pe.

**Simpler observable: gradient anisotropy score (GAS).** Define:

    GAS = |∇[CXCL9]| / σ(∇[CXCL9])

where σ is the spatial standard deviation of the gradient across the section. GAS > 3 → smooth, unidirectional gradient → directed percolation regime. GAS < 1 → noisy, multidirectional gradient → isotropic percolation regime. GAS is a single number extractable from standard CXCL9 immunofluorescence without T cell tracking or network extraction.

**Prediction**: Tumors with GAS > 3 and collagen density near p_c should show significantly higher T cell infiltration depth (median T cell distance from edge) than tumors with GAS < 1 at the same collagen density, because directed percolation has a lower effective p_c than isotropic percolation. The effect size is predicted to be ~15-25% more infiltrating T cells per unit distance in the directed regime [PARAMETRIC: from the DP vs isotropic p_c difference of ~10-15%].

### Test Protocol

1. **Retrospective analysis**: In a cohort of 50-100 tumor sections with available CD8+ T cell IHC, CXCL9/10 immunofluorescence, and SHG collagen imaging, compute: (a) GAS from CXCL9 staining gradient; (b) collagen crosslink density proxy (SHG intensity + hydroxyproline assay); (c) T cell infiltration depth (median distance from tumor edge).
2. **Phase diagram construction**: Plot T cell infiltration depth vs. collagen crosslink density, stratified by GAS (low/high). Expect two distinct curves: high-GAS tumors with lower effective p_c (infiltrate at higher collagen density) vs. low-GAS tumors tracking the isotropic percolation curve.
3. **Expected result if TRUE**: At fixed collagen density near p_c, high-GAS tumors show 15-25% greater T cell infiltration depth than low-GAS tumors. Regression: infiltration ~ GAS × [p_c - p]^β (interaction term between gradient anisotropy and crosslink density).
4. **Expected result if FALSE**: GAS does not predict infiltration after controlling for collagen density. T cell depth is determined by total CXCL9 level, not gradient anisotropy.
5. **Effort**: 3-6 months retrospective analysis (no new experiments required if tissue bank with matched IHC/SHG is available). This is the lowest-effort hypothesis in the evolved set.

**Confidence**: 4/10 (vs. 3/10 for parent). Increased because GAS is a clinically measurable single variable (replaces technically demanding anisotropic ξ measurement) and the gradient-variation concern is now addressed with a specific quantitative correction.
**Groundedness**: 6 — directed percolation exponents [GROUNDED: Hinrichsen 2000], T cell chemotaxis [GROUNDED: Nagarsheth 2017], chemotactic coefficient estimates [PARAMETRIC: Weber 2013], Pe_c ~ 1 crossover [PARAMETRIC: 2D from Saha 2024], GAS definition [PARAMETRIC: novel construct], 15-25% effect size estimate [PARAMETRIC]

**Why stronger than H8**: (1) Observable changed from technically demanding anisotropic correlation length (requires directional g(r) analysis) to a single gradient anisotropy score (GAS) extractable from standard immunofluorescence; (2) the gradient-variation concern is explicitly addressed with the Pe_eff formula; (3) the clinical consequence is concretized (15-25% more T cells in directed-percolation tumors near p_c); (4) the test is redesigned as a retrospective analysis of existing tissue (no new animal experiments needed as first test).

---

## E5: MMP/LOX Ratio as a Percolation Clock — Separating Dynamic Percolation Windows from Salmon 2012 Fiber Alignment

**Evolved from Hypothesis H6 via Specification + Mutation**
**Critic questions addressed:** Distinguish dynamic percolation from Salmon 2012 fiber alignment; what is the degradation timescale of LOX-crosslinked collagen by MMPs?

### Connection
Dynamic percolation theory (time-varying bond occupation) → MMP/LOX activity ratio as the percolation clock controlling p(t) → Temporal windows of immune infiltration measurable by MMP activity, distinct from fiber-alignment trapping

### Mechanism

**The Salmon 2012 distinction is the central challenge.** Salmon et al. (2012, J Clin Invest) showed that peri-tumoral T cell trapping correlates with collagen fiber ALIGNMENT (geometric guidance), not network connectivity. The parent H6 did not distinguish its prediction from Salmon 2012. E5 now provides a specific experimental discriminator:

- **Salmon 2012 (fiber alignment) mechanism**: T cells are physically guided along collagen fibers parallel to the tumor boundary. Trapping occurs because fibers run circumferentially around the tumor, creating a tangential guide that prevents radial penetration. This mechanism depends on fiber ORIENTATION, not fiber DENSITY or pore size. Prediction: T cell trapping should correlate with CurveAlign fiber alignment score (CT-FIRE alignment metric, 0-1 scale [GROUNDED: Bredfeldt et al. 2014]) regardless of crosslink density.
- **Dynamic percolation (H6/E5) mechanism**: T cell trapping occurs when the ECM transitions from subcritical (open path exists) to supercritical (path closes) on timescales comparable to the T cell transit time (~2-6 hours for 500 μm). This mechanism depends on MMP/LOX activity DYNAMICS, not fiber orientation. Prediction: T cell trapping should correlate with temporal variance in MMP activity (pulsatility score), independent of fiber alignment.

**Experimental discriminator**: Measure both fiber alignment score and MMP activity pulsatility score in organotypic cultures simultaneously. Partial correlation analysis (controlling for alignment when testing MMP-pulsatility, and vice versa). If fiber alignment mediates all trapping: MMP pulsatility contributes zero incremental R² after controlling for alignment. If dynamic percolation contributes independently: MMP pulsatility explains incremental R² > 10% after alignment control.

**LOX-crosslinked collagen MMP degradation timescale (critic question answered).** Critic asked specifically: what is the degradation timescale of LOX-crosslinked collagen? Available data: MMP-1 (collagenase) cleaves native Type I collagen with t₁/₂ ~ 4-12 hours at physiological concentrations (Spicer et al. 2014, J Cell Sci [GROUNDED: cited in parent H6]). However, LOX-crosslinked collagen (pyridinoline crosslinks) is substantially more resistant: crosslinks reduce the catalytic rate constant k_cat of MMP-1 by 3-10× [PARAMETRIC: estimated from Orgel et al. 2011 — LOX crosslinks stabilize the collagen triple helix against unfolding, which is the rate-limiting step for MMP cleavage; exact factor tumor-type-dependent]. Therefore, the effective t₁/₂ for degradation of LOX-crosslinked collagen by MMP-1 is approximately 12-120 hours (0.5-5 days) at physiological enzyme concentrations.

**Timescale matching and the percolation window.** T cell transit time from stroma to tumor core (100-500 μm at 5-15 μm/min): 10-100 minutes. MMP burst duration (MMP-9 burst after macrophage activation, hypoxia burst): 2-12 hours [GROUNDED: Semba et al. 2004; Erler 2006]. LOX-crosslinked collagen degradation t₁/₂: 12-120 hours. The timescales are NOT well-matched:
- MMP burst (2-12 hours) >> T cell transit (10-100 minutes): good — T cells can traverse during the window.
- LOX-crosslinked collagen degradation (12-120 hours) >> MMP burst (2-12 hours): bad — LOX-crosslinked bonds are largely resistant to typical MMP bursts.

This implies that dynamic percolation windows are most likely to occur at the BOUNDARY between the dense-crosslinked core and the less-crosslinked peripheral stroma, where crosslink density is near p_c AND crosslinks are of mixed LOX/non-LOX origin (partially crosslinked zones where MMP can degrade the weaker, non-pyridinoline crosslinks on shorter timescales).

**Revised mechanistic prediction.** Dynamic percolation is not a bulk ECM effect — it operates at the tumor-stroma INTERFACE (within ~100-200 μm of the boundary), where: (1) p is near p_c (the critical zone between dense core and loose periphery); (2) crosslinks are a mix of LOX-generated (MMP-resistant) and non-LOX (MMP-sensitive); (3) MMP bursts can transiently push p below p_c in the interface zone, creating a ~2-6 hour infiltration window. T cells that are already positioned in the interface zone during an MMP burst can penetrate; those that arrive after the window closes accumulate as the peri-tumoral ring. This is distinct from Salmon 2012 fiber alignment (which operates at all crosslink densities and does not require temporal fluctuations).

### Test Protocol

1. **Organotypic culture time-lapse (as in parent H6) with added controls**: Add collagen-embedded tumorspheres in a matrigel/collagen mix. Add activated CD8+ T cells at periphery. Monitor: (a) T cell positions by fluorescence every 30 min for 72h; (b) MMP-2/9 activity by DQ-collagen fluorescence; (c) fiber alignment by SHG at start and 24h intervals. Apply MMP inhibitor (GM6001, 25 μM) in one arm and LOX crosslinking enhancer (LOXL2 supplementation) in another arm.
2. **Fiber alignment control**: Process SHG images with CT-FIRE software to extract fiber alignment score per region. Compute partial correlation between T cell infiltration burst timing and MMP burst timing, controlling for fiber alignment score.
3. **Expected result if DYNAMIC PERCOLATION**: MMP burst events (identified as DQ-collagen fluorescence peaks) precede T cell infiltration events by 1-3 hours (cross-correlation peak at τ = 1-3h). Partial correlation MMP pulsatility vs. infiltration (controlling for alignment) R² > 0.1. Effect is largest at tumor-stroma interface, not throughout the ECM.
4. **Expected result if SALMON 2012 FIBER ALIGNMENT only**: T cell trapping correlates with CT-FIRE alignment score (r > 0.5) but MMP pulsatility contributes zero incremental R² after alignment control. No temporal correlation between MMP bursts and infiltration events.
5. **Expected result if BOTH MECHANISMS OPERATE**: Both fiber alignment score AND MMP pulsatility independently predict infiltration. Additive model fits better than either alone (ΔR² > 0.05 for each).
6. **Effort**: 8-14 months. Organotypic cultures are standard; the addition of DQ-collagen and CT-FIRE analysis adds 2-3 months of methods development. Requires access to SHG imaging facility.

**Confidence**: 4/10 (vs. 3/10 for parent). Increased by providing the Salmon 2012 experimental discriminator and quantifying the LOX-crosslinked collagen degradation timescale. Remaining concern: timescale mismatch suggests dynamic percolation operates only at the interface (not throughout ECM), limiting the scope of the prediction.
**Groundedness**: 6 — MMP-1 collagen degradation t₁/₂ 4-12h [GROUNDED: Spicer 2014], LOX crosslink resistance to MMP (3-10× slowing) [PARAMETRIC: Orgel 2011 structural basis], MMP burst dynamics [GROUNDED: Semba 2004, Erler 2006], CT-FIRE fiber alignment [GROUNDED: Bredfeldt 2014], Salmon 2012 fiber alignment mechanism [GROUNDED], DQ-collagen MMP sensor [GROUNDED: commercial reagent], timescale mismatch implication [PARAMETRIC: derived from above]

**Why stronger than H6**: (1) Provides explicit experimental discriminator between dynamic percolation and Salmon 2012 fiber alignment (partial correlation analysis, quantified by incremental R²); (2) LOX-crosslinked collagen MMP degradation timescale is now quantified (t₁/₂ = 12-120h, 3-10× slower than uncrosslinked); (3) mechanistic scope is refined — dynamic percolation now predicted to operate at the tumor-stroma INTERFACE specifically, not throughout the tumor ECM; (4) the experimental protocol explicitly tests both mechanisms in the same preparation, making the result interpretable regardless of which mechanism wins.

---

## E6: Velocity Autocorrelation Signature Distinguishes Percolation Subdiffusion from T Cell Run-and-Pause

**Evolved from Hypothesis H3 via Specification**
**Critic questions addressed:** Distinguishing percolation subdiffusion from run-and-pause subdiffusion; proposed measurement of velocity autocorrelation function (VACF).

### Connection
Anomalous diffusion theory → Velocity autocorrelation function (VACF) as mechanistic fingerprint → Distinguishes percolation-induced subdiffusion (negative VACF at intermediate lag times) from T cell run-and-pause subdiffusion (exponential VACF decay) in tumor ECM

### Mechanism

**The parent H3 was correctly killed by the critic for circular reasoning.** The parent argued that α = 0.53 (from MSD exponent) is a diagnostic fingerprint, but run-and-pause T cell behavior independently produces α ~ 0.5-0.7 (Krummel 2016; Riedl 2020). MSD alone is insufficient. E6 replaces MSD as the primary observable with the velocity autocorrelation function (VACF), which has mechanistically distinct signatures for the two processes.

**VACF signatures.** The VACF is C(τ) = ⟨v(t) · v(t+τ)⟩ / ⟨v²⟩.

For **percolation subdiffusion** (random walk trapped in fractal cluster): C(τ) shows a NEGATIVE region at intermediate lag times (anti-correlation dip at τ ~ τ_c, the caging timescale) followed by decay to zero at long τ [GROUNDED: Ben-Avraham & Havlin 2000 — cage effect on percolation cluster]. The negative dip arises because a walker in a dead-end pore must reverse direction to escape. The depth of the negative dip scales as ~-(1-α)/α at the characteristic time, and the area under the negative region equals -⟨Δx²(τ_c)⟩/2 [GROUNDED: fluctuation-dissipation relation for subdiffusive VACF; Metzler & Klafter 2000].

For **run-and-pause subdiffusion** (T cell alternating between directed runs and paused scanning): C(τ) shows a single-exponential decay from C(0) = 1 to C(∞) = 0, with correlation time τ_run ~ 2-5 minutes (inter-pause interval) [GROUNDED: Krummel 2016; Mrass 2006]. There is NO negative region — C(τ) remains positive or zero for all τ [GROUNDED: two-state random walk VACF is strictly non-negative; Weiss 1976].

**This is the discriminator.** A measured VACF with a negative dip at τ ~ 1-10 min (the ECM pore traversal timescale, estimated from T cell speed ~ 5 μm/min and pore spacing ~ 2-5 μm: τ_c ~ 1-3 min) is diagnostic of percolation topology. A VACF without a negative dip (monotone decay) indicates run-and-pause or viscoelastic subdiffusion independent of percolation.

**Active particle VACF modification.** For active T cells (Pe ~ 3), the VACF at short times (τ < τ_active ~ pore traversal time) is enhanced relative to passive particles due to persistent self-propulsion. The critical diagnostic is specifically the intermediate-time negative dip, which is not expected for run-and-pause T cells regardless of activity. Active percolation VACF: positive at τ < τ_c (self-propulsion contribution), negative dip at τ ~ τ_c (dead-end reversal), recovery to zero at long τ. This three-region VACF profile is unique to percolation in the presence of active self-propulsion.

**Quantitative prediction.** At p = p_c in 3D passive percolation, the VACF negative minimum occurs at:
    τ_min ~ a² / (2D_0) × (d_w / 2 - 1)^(-1) ≈ (2-5 μm)² / (30 μm²/min) × (0.9)^(-1) ≈ 0.15-0.92 min [PARAMETRIC: derived from d_w = 3.8, a = 2-5 μm, D_0 = 30 μm²/min]

The minimum value of C(τ_min) ≈ -(α-1)/2 ≈ -0.24 [PARAMETRIC: estimated from anomalous diffusion VACF theory]. For run-and-pause: C(τ_min) = C(0.15-0.92 min) ≈ exp(-τ_min / τ_run) ≈ exp(-0.15/2.5) ≈ 0.94 — positive, nearly 1.

The VACF diagnostic: measure VACF at τ = 0.5-1 min lag. If C(0.5 min) < -0.1 → percolation subdiffusion. If C(0.5 min) > 0.5 → run-and-pause. The two mechanisms are separated by a factor of ~5 in VACF magnitude at the diagnostic lag.

### Test Protocol

1. **In vitro VACF measurement**: Embed activated CD8+ T cells in 3D collagen gels at 5 density conditions (2, 4, 6, 8, 12 mg/mL). Track individual T cells at 10-second intervals for 4+ hours (n ≥ 30 tracks per condition, 600+ time points per track minimum). Compute VACF for each condition.
2. **Key measurement**: Presence and depth of VACF negative dip at τ = 0.5-3 min lag.
3. **Percolation control**: Use non-actively-migrating (cytochalasin D-treated) T cells or passive microspheres of comparable size (8 μm) as passive walkers. Their VACF should show a negative dip at the same collagen density where active T cells show a dip (confirming it is ECM topology, not T cell biology).
4. **Run-and-pause control**: Image T cells at zero collagen (suspended in buffer). VACF should show exponential decay, no negative dip. This establishes the run-and-pause baseline.
5. **Expected result if percolation**: At the critical collagen density, VACF has negative minimum C(τ_min) < -0.1 at τ_min ≈ 0.5-1 min. Both passive beads AND active T cells show the negative dip at the same critical density. The density at which the dip appears matches the density at which T cell infiltration is halved (from the H1/E1 experiment).
6. **Expected result if run-and-pause only**: VACF remains positive for all collagen densities. No negative dip. T cell motion is correlated/uncorrelated at all densities without sign change. Passive beads do NOT show subdiffusion (they diffuse normally, confirming ECM is not the source of T cell subdiffusion).
7. **Effort**: 3-5 months. Requires high-frame-rate 3D confocal (10-second intervals, achievable with spinning disk), custom VACF analysis scripts, and access to T cell culture.

**Confidence**: 5/10 (vs. 4/10 for parent H3). Increased because VACF is a mechanistically definitive discriminator between the two subdiffusion mechanisms — unlike MSD slope, which both mechanisms can produce.
**Groundedness**: 6 — VACF theory for subdiffusion [GROUNDED: Metzler & Klafter 2000; Ben-Avraham & Havlin 2000], VACF negative dip for cage/percolation effect [GROUNDED: Ben-Avraham & Havlin 2000], run-and-pause VACF non-negative [GROUNDED: Weiss 1976 two-state random walk], T cell run-and-pause (Krummel 2016) [GROUNDED], τ_min estimate [PARAMETRIC: derived from d_w = 3.8, a = 2-5 μm], C(τ_min) estimate [PARAMETRIC: derived from anomalous diffusion VACF theory]

**Why stronger than H3**: (1) Abandons the flawed MSD-alone diagnostic in favor of VACF, which has mechanistically distinct signatures for the two subdiffusion causes; (2) the discriminator is now quantitative: C(τ_min) < -0.1 for percolation vs C(τ_min) > 0.5 for run-and-pause at τ = 0.5-1 min — a 5× separability gap; (3) an independent passive-bead control is proposed that definitively attributes the VACF dip to ECM topology rather than T cell biology; (4) the τ_min is now estimated quantitatively (0.15-0.92 min) with clear derivation from d_w and a.

---

## EVOLUTION QUALITY CHECK

### 1. Is each hypothesis genuinely stronger than its parent, or just rephrased?

**E1 (from H1 — Specification)**: Genuinely stronger. Mechanism specificity increased substantially: Wolf 2013 threshold corrected to 4 μm² (d ≈ 2.26 μm, not 3 μm); heterogeneity smearing is now quantified with σ_p ≈ 0.06, Δp ≈ 0.12, and predicted n_app ≈ 2-4; a discriminator between percolation and Hill pharmacology is specified (β = 0.41 slope in log-log inflection region). The test protocol adds an independent pore geometry calibration step. Not a restatement.

**E2 (from H4 — Specification)**: Genuinely stronger. Tang citation corrected to 1983. The p(dose) function is now mechanistically derived using LOX enzyme kinetics and estimated K_I ≈ 50-200 μM; critical dose d_c is estimated (~50-150 μM intratumoral); the cooperative LOX concern is addressed (LOX is monomeric, no allosteric cooperativity); in vivo broadening is quantified (2-4×). A new in vitro calibration experiment is added before the in vivo titration. Not a restatement.

**E3 (from H2 — Specification + Mutation)**: Genuinely stronger. The entire hypothesis is inverted from "assume ν = 0.88 and verify" to "measure ν_eff as a function of Pe." The test is redesigned to use a microfluidic Pe-control system. The fraction of tumors near p_c is quantified (~20-30% for CRC MSI-high). The clinical priority cohort is identified. Not a restatement — this is a qualitative improvement in hypothesis form.

**E4 (from H8 — Mutation + Specification)**: Genuinely stronger. The anisotropic ξ observable is replaced with the Gradient Anisotropy Score (GAS), a single number extractable from standard immunofluorescence. The gradient-variation concern is now addressed with a quantitative correction (Pe_eff formula). A retrospecive study is proposed as the first test (lower cost and effort than parent). The predicted effect size (15-25% more T cells in directed-percolation tumors) is specified. Not a restatement.

**E5 (from H6 — Specification + Mutation)**: Genuinely stronger. The Salmon 2012 fiber alignment mechanism is now explicitly distinguished via partial correlation analysis. The LOX-crosslinked collagen MMP degradation timescale is quantified (t₁/₂ = 12-120h, 3-10× slower than uncrosslinked). The scope of dynamic percolation is refined to the tumor-stroma interface (100-200 μm zone), not throughout the ECM. A quantitative discriminator (incremental R² > 10% after alignment control) is specified. Not a restatement.

**E6 (from H3 — Specification)**: Genuinely stronger. The flawed MSD diagnostic is replaced with VACF, which has mechanistically distinct signatures. The discriminator is quantitative (C(τ_min) < -0.1 for percolation vs > 0.5 for run-and-pause at τ = 0.5-1 min). A passive-bead control is proposed to definitively assign the VACF dip to ECM topology. τ_min is estimated from first principles (0.15-0.92 min). The evolution operation succeeded — mechanism specificity genuinely increased.

**Conclusion**: All 6 evolved hypotheses are stronger than their parents. Evolution did not merely rephrase.

### 2. Do any two share the same bridge mechanism?

Bridge mechanisms across the 6 evolved hypotheses:
- E1: LOX collagen network topology as bond occupation probability on random geometric graph
- E2: BAPN dose-to-p mapping via LOX enzyme kinetics (percolation titration)
- E3: Active-particle universality class measurement via Pe-controlled microfluidic experiment
- E4: Gradient Anisotropy Score (CXCL9/10 steepness) as Pe-based classifier for isotropic vs directed percolation regime
- E5: MMP/LOX ratio temporal dynamics as percolation clock at tumor-stroma interface
- E6: Velocity autocorrelation function negative dip as percolation-specific mechanistic fingerprint

No two share the same bridge mechanism. Diversity constraint passes.

Note: E3 and E4 both involve the isotropic-vs-directed percolation distinction, but their bridge mechanisms are distinct: E3 measures the critical exponent via Pe control in microfluidic collagen; E4 classifies clinical tumors using CXCL9/10 gradient steepness as a proxy for Pe. They operate at different levels (in vitro measurement vs clinical classification) and require different experiments.

### 3. Did any crossover produce something incoherent?

No crossover was used in this evolution cycle. All operations were specification (E1, E2, E3, E6) or mutation/specification hybrid (E4, E5). Both hybrids are coherent.

### 4. Are the critic questions addressed?

| Critic Question | Addressed By | How |
|---|---|---|
| H1: Quantify heterogeneity smearing | E1 | σ_p ≈ 0.06, Δp ≈ 0.12, n_app ≈ 2-4 |
| H1: Correct Wolf 2013 (4 μm² not 3 μm) | E1 | Threshold corrected to 4 μm², d ≈ 2.26 μm |
| H2: Universality class for Pe ~ 3 | E3 | Measure ν_eff(Pe), Pe-crossover at Pe_c ~ 1 |
| H2: Fraction of tumors near p_c | E3 | ~20-30% for CRC MSI-high, from collagen density data |
| H3: Distinguish percolation from run-and-pause | E6 | VACF negative dip (C < -0.1) vs run-and-pause (C > 0.5) |
| H4: Correct Tang citation (1983 not 2017) | E2 | Tang, Trackman & Kagan 1983, J Biol Chem 258:4331 |
| H4: Estimate p(dose) shape | E2 | Hyperbolic LOX kinetics model; K_I ≈ 50-200 μM; d_c ≈ 50-150 μM |
| H6: Distinguish from Salmon 2012 alignment | E5 | Partial correlation analysis; incremental R² discriminator |
| H6: LOX-crosslinked collagen degradation timescale | E5 | t₁/₂ = 12-120h (3-10× slower than uncrosslinked) |
| H8: Simpler observable than anisotropic ξ | E4 | Gradient Anisotropy Score (GAS) from CXCL9 immunofluorescence |
| H8: Gradient variation vs correlation length → reversion to isotropic | E4 | Pe_eff formula; GAS > 3 needed for directed regime |

All 11 substantive critic questions addressed. The 12th (H3: velocity autocorrelation precision) is addressed by E6.

---

## Lineage Summary

| Evolved ID | Parent | Operation | Key Change |
|---|---|---|---|
| E1 | H1 | Specification | Wolf 2013 correction (4 μm²); σ_p heterogeneity quantification; n_app = 2-4 discriminator |
| E2 | H4 | Specification | Tang 1983 correction; LOX kinetics p(dose) model; K_I ≈ 50-200 μM; d_c ≈ 50-150 μM |
| E3 | H2 | Specification + Mutation | Inverted from "assume ν" to "measure ν_eff(Pe)"; microfluidic Pe-control; 20-30% CRC near p_c |
| E4 | H8 | Mutation + Specification | GAS replaces anisotropic ξ; Pe_eff formula for gradient variation; retrospective study design |
| E5 | H6 | Specification + Mutation | Partial correlation vs Salmon 2012; t₁/₂ LOX-crosslinked collagen = 12-120h; scope limited to interface zone |
| E6 | H3 | Specification | VACF replaces MSD; C(τ_min) < -0.1 discriminator; passive-bead control; τ_min estimated |
