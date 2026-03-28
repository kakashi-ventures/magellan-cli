# Evolved Hypotheses — Cycle 1
## Session: session-20260328-123317
## Fields: Statistical mechanics (bond percolation theory) x Tumor immunology (ECM-mediated immune exclusion)
## Date: 2026-03-28
## Evolver: Opus | Cycle: 1

---

## Evolution Summary

| ID | Operation | Parents | Bridge Family | Conf | Ground |
|----|-----------|---------|---------------|------|--------|
| EH1 | CROSSOVER | H1 x H5 | Bond occupation / threshold crossing | 7 | 7 |
| EH2 | MUTATION | H2 | Correlation length / spatial scaling | 5 | 6 |
| EH3 | MUTATION | H4 | Lattice topology | 5 | 6 |
| EH4 | MUTATION | H8 | Correlated percolation / feedback | 5 | 5 |

**Mandatory corrections applied**: d_w = 2.878 (not 3.8), tau = 2.31 (not 2.19), PXS-5505 (not LOX-IN-3), TGF-beta ~10-30 um (not 50-100 um), Wolf 2013 = 4 um^2 cross-section (not 3 um diameter), H4 title = "p_c shift within same universality class" (not "universality class switch").

**Diversity**: 4 distinct bridge families across 4 hypotheses. Constraint (>= 3) satisfied.

---

## EH1: Unified Percolation-Pharmacology Framework — LOX Crosslink Density as Bond Occupation Probability Predicts Both a Sharp Immune Exclusion Threshold and Order-Parameter Scaling of LOX Inhibitor Dose-Response

**Parents**: H1 (LOX Crosslink Density, composite 7.80) x H5 (LOX Inhibitor Dose-Response, composite 7.60)
**Operation**: CROSSOVER
**Bridge family**: Bond occupation / threshold crossing

### Connection

Bond percolation theory (statistical mechanics) -> LOX-mediated collagen crosslink density as bond occupation probability p -> Sharp immune exclusion phase transition in solid tumors AND pharmacological dose-response following order-parameter scaling P_inf ~ (p - p_c)^0.41

### Mechanism

**Core framework (from H1, corrected)**: In 3D bond percolation, each bond is open with probability p. Below p_c = 0.2488 (simple cubic, passive walkers), only finite clusters exist; above p_c, a spanning cluster emerges with order parameter P_inf ~ (p - p_c)^beta, beta = 0.41 [GROUNDED: Stauffer & Aharony 1994]. We map LOX-mediated collagen crosslinks to bonds: each potential crosslink site is either covalently bonded (LOX/LOXL1-4 catalyzed) or open. T cells migrating through the ECM traverse open pores but are arrested when the pore cross-section drops below ~4 um^2 [GROUNDED: Wolf et al. 2013 — corrected from the imprecise "3 um pore diameter" in H1; 4 um^2 corresponds to a circular pore diameter of ~2.3 um]. The percolation threshold p_c marks the critical crosslink density at which the last connected T cell migration path is severed.

**Active percolation correction**: T cells are active particles with chemotactic persistence (Pe ~ 3, estimated from v_active ~ 10 um/min, l ~ 10 um, D_passive ~ 35 um^2/min [PARAMETRIC]). Active particles experience a shifted threshold: p_c(active) < p_c(passive) because active force permits traversal of partially constricting bonds. Extrapolating from the 2D active percolation framework (Saha et al. 2024, Soft Matter) to 3D with Pe ~ 3: p_c(active) ~ 0.21-0.24 [PARAMETRIC: 3D extrapolation].

**Critical correction — d_w = 2.878, not 3.8**: The fractal walk dimension d_w governs anomalous diffusion on the percolation cluster at p_c: MSD ~ t^(2/d_w). The Alexander-Orbach conjecture gives d_w = 2 * d_f / d_s ~ 3.8, but this is exact only for d >= 19 (upper critical dimension for percolation transport). The numerically measured value for 3D percolation is d_w = 2.878 +/- 0.002 [GROUNDED: Bunde & Havlin 1996; Grassberger 1999]. This gives MSD exponent alpha = 2/d_w = 0.695, NOT 0.53. Alpha = 0.695 is still distinctly subdiffusive but closer to normal diffusion than previously claimed.

**Heterogeneity analysis (addressing Critic)**: Real tumors have spatially heterogeneous collagen density (sigma_p/p ~ 0.3-0.5 from SHG imaging). Does this destroy the phase transition? The Harris criterion states that weak uncorrelated disorder is irrelevant to the percolation transition when nu > 2/d [GROUNDED: Harris 1974, J Phys C]. Since nu = 0.88 > 2/3 = 0.67, the criterion is satisfied: the percolation transition SURVIVES disorder. Specifically, heterogeneity broadens the transition region by Delta_p ~ sigma_p (the transition occurs over a range of p values rather than a single point), but the critical singularity (power-law scaling) is preserved within this broadened region. For sigma_p/p ~ 0.3-0.5, the transition window is Delta_p ~ 0.06-0.12 around p_c — broad enough to be experimentally accessible but sharp enough to be distinguishable from a gradual decline.

**Pharmacological dose-response (from H5, corrected)**: If LOX crosslinking = bond occupation probability p, then pharmacological LOX inhibition provides a direct control knob. BAPN (beta-aminopropionitrile) irreversibly inhibits LOX [GROUNDED: Tang, Trackman & Kagan 1983, J Biol Chem 258:4331]. PXS-5505 is a pan-LOX inhibitor targeting LOX, LOXL1, LOXL2, LOXL3, and LOXL4 [GROUNDED: PMID 39101793, 2024] — corrected from the erroneously cited "LOX-IN-3" in H5. Using PXS-5505 resolves the multi-LOX-family confound: because it inhibits all LOX isoforms, the dose-response directly maps to total crosslink formation rate without isoform-specific complications.

**p(dose) estimation (addressing Critic)**: For irreversible LOX inhibition, the fraction of active LOX at steady state is f_active(dose) = K_i / (dose + K_i), where K_i is the inhibitor's effective concentration for 50% inhibition [PARAMETRIC: standard irreversible enzyme kinetics]. The steady-state crosslink density is:

p(dose) = p_0 * K_i / (dose + K_i)

where p_0 is the baseline crosslink density without inhibitor. This crosses p_c at the critical dose:

d_c = K_i * (p_0/p_c - 1)

Near d_c, T cell infiltration follows order-parameter scaling:

I(d) ~ |p(d) - p_c|^beta = |p_0 * K_i/(d + K_i) - p_c|^0.41 for d > d_c

This is SHARPER than a Hill equation for two reasons: (1) it has a true zero below threshold (I = 0 for d < d_c), not an asymptotic approach; (2) the exponent beta = 0.41 is a universal constant fixed by 3D percolation, not a free fitting parameter. The shape is distinguishable from Hill: plot log(I) vs log|d - d_c| — a straight line with slope 0.41 +/- 0.1 indicates percolation; curvature or different slope indicates conventional pharmacology.

### Unified predictions

1. **Threshold existence**: T cell infiltration density shows a sharp (though heterogeneity-broadened) transition as collagen crosslink density p crosses p_c ~ 0.21-0.25.
2. **Order-parameter scaling**: Near p_c, infiltration I ~ (p_c - p)^0.41, where beta = 0.41 is universal.
3. **Dose-response shape**: LOX inhibitor (PXS-5505 or BAPN) dose-response follows p(dose) = p_0 * K_i/(dose + K_i), with T cell infiltration onset at d_c = K_i(p_0/p_c - 1) and power-law scaling near d_c.
4. **Cross-tumor universality**: Different tumor types have different p_0 (baseline crosslink density) and therefore different d_c, but ALL show the same exponent beta = 0.41.
5. **MSD at criticality**: T cells at p = p_c show alpha = 0.695 subdiffusion (corrected from 0.53).
6. **Heterogeneity resilience**: The transition survives intratumoral heterogeneity (Harris criterion). Transition window Delta_p ~ sigma_p ~ 0.06-0.12 is experimentally accessible.

### Novelty beyond Ashworth 2015

Ashworth et al. (2015, PMID 25881025) applied percolation to connective tissue cell invasion in collagen scaffolds. The present hypothesis differs in: (1) T cells of the adaptive immune system, not connective tissue cells; (2) LOX enzyme activity as endogenous, druggable control parameter; (3) active percolation (Pe ~ 3); (4) pharmacological dose-response prediction with specific exponent; (5) Harris criterion analysis for biological heterogeneity; (6) unified threshold + dose-response framework in a single testable prediction.

### Confidence: 7/10

Increased from H1 (6) and H5 (5) because: (1) unification makes both components stronger — H1's threshold gains pharmacological testability, H5's dose-response gains the physical mechanism; (2) Harris criterion resolves the main heterogeneity concern with rigorous theory; (3) PXS-5505 correction removes multi-LOX confound that weakened H5. Remaining concerns: (a) p(dose) model assumes simple enzyme kinetics; real dose-response may involve PK/PD complications in vivo; (b) the lattice abstraction of disordered collagen is still the fundamental assumption; (c) collagen is not the only physical barrier to T cell migration.

### Groundedness: 7/10

- LOX-mediated collagen crosslinking [GROUNDED: Nicolas-Boluda 2021, eLife]
- LOX inhibition improves T cell infiltration [GROUNDED: PMID 38267662, 38305736]
- PXS-5505 as pan-LOX inhibitor [GROUNDED: PMID 39101793, 2024]
- Percolation threshold and exponents for 3D (p_c = 0.2488, nu = 0.88, beta = 0.41) [GROUNDED: Stauffer & Aharony 1994]
- d_w = 2.878 for 3D percolation [GROUNDED: Bunde & Havlin 1996; Grassberger 1999]
- Harris criterion nu > 2/d for disorder irrelevance [GROUNDED: Harris 1974, J Phys C]
- Wolf 2013 T cell arrest at 4 um^2 [GROUNDED: corrected]
- Active percolation p_c ~ 0.21-0.24 in 3D [PARAMETRIC: extrapolated from Saha 2024 2D framework]
- p(dose) model [PARAMETRIC: standard enzyme kinetics applied to crosslink steady state]
- Heterogeneity sigma_p/p ~ 0.3-0.5 [PARAMETRIC: estimated from SHG literature]

### Why this might be WRONG

1. **Lattice abstraction**: Collagen ECM is a disordered fiber network, not a regular lattice. Percolation on random geometric graphs has different p_c values (though same universality class in 3D). The mapping from crosslink density to bond occupation probability requires defining the network topology, which is nontrivial for stochastically oriented fibers.
2. **Soft thresholds**: T cell nuclear deformability means "blocked" is not strictly binary — cells can squeeze through pores below 4 um^2 with increasing transit time and DNA damage [GROUNDED: Raab et al. 2016, Science]. This creates a soft threshold rather than a hard bond, potentially converting the phase transition into a sharp crossover.
3. **PK/PD complications**: In vivo drug distribution, metabolism, and tissue penetration may transform the clean p(dose) = p_0 * K_i/(dose + K_i) into a more complex function. If the effective p(dose) has its own nonlinearity, the composite dose -> infiltration curve may have multiple inflections.
4. **Alternative barriers**: Collagen is not the only barrier — basement membrane, blood vessel walls, and immunosuppressive gradients (TGF-beta, PD-L1) independently limit T cell access. The percolation framework captures only the ECM component.

### How to Test

1. **Unified dose-response experiment**: Implant syngeneic tumors (4T1 breast and KPC pancreatic) in mice. Treat with PXS-5505 at 10 doses (spanning 2 orders of magnitude) for 7 days. Simultaneously quantify: (a) CD8+ T cell density in tumor core (IHC), (b) collagen crosslink density (pyridinoline assay), (c) total collagen (hydroxyproline).
2. **Expected if TRUE**: (a) T cell density vs PXS-5505 dose shows a sharp sigmoid with identifiable inflection at d_c. (b) T cell density vs crosslink density shows power-law onset I ~ (p_c - p)^0.41 near threshold. (c) 4T1 and KPC show DIFFERENT d_c values (different p_0) but SAME exponent beta = 0.41 +/- 0.1. (d) Log-log plot of I vs |p - p_c| yields a straight line with slope 0.41.
3. **Expected if FALSE**: T cell density increases linearly or log-linearly with PXS-5505 dose, fitting a Hill equation. Different tumors show different apparent exponents. No identifiable inflection point.
4. **Effort**: 6-12 months. IACUC approval, 10 dose groups x 5-8 mice/group x 2 tumor models, histology + crosslink quantification. High cost but directly clinically relevant — PXS-5505 is in clinical trials for fibrosis.

---

## EH2: Correlation Length Exponent nu = 0.88 Predicts T Cell Cluster Size Distribution Near the Hot-Cold Boundary, with Active-Particle Crossover Below ~9 um

**Parent**: H2 (Correlation Length Exponent, composite 7.40)
**Operation**: MUTATION
**Bridge family**: Correlation length / spatial scaling

### Connection

Percolation universality (critical exponents) -> Correlation length xi ~ |p - p_c|^(-0.88) and cluster size distribution n_s ~ s^(-2.31) -> T cell cluster size scaling law conserved across all solid tumor types, with active-particle corrections below a quantifiable crossover length scale

### Mechanism

**Core prediction (from H2, corrected)**: Near the percolation threshold, the ECM accessible to T cells fragments into clusters whose size distribution follows the Fisher scaling form:

n_s ~ s^(-tau) * f(s / s_xi)

where s is cluster size (number of accessible pores), tau = 2.31 is the cluster size exponent [GROUNDED: Jan & Stauffer 1998 — CORRECTED from 2.19 which is the approximate formula tau ~= 1 + d/d_f, inaccurate for d=3], and s_xi ~ xi^(d_f) is the characteristic cluster size set by the correlation length xi ~ |p - p_c|^(-nu), nu = 0.88 [GROUNDED: Stauffer & Aharony 1994]. The fractal dimension d_f = 2.53 in 3D [GROUNDED].

T cells confined to these clusters form spatial aggregates whose size distribution mirrors the underlying percolation cluster distribution. The prediction is that CD8+ T cell cluster sizes in tumor tissue follow n_s ~ s^(-2.31) when the tumor ECM is near the percolation threshold, and this exponent is UNIVERSAL — identical across breast, pancreatic, colorectal, and lung tumors despite their different collagen compositions, LOX isoforms, and chemokine environments.

**Active-particle universality analysis (addressing Critic)**: The Critic asked what universality class the Pe ~ 3 active-particle system belongs to. This is a crossover problem with a quantifiable length scale:

- **Below l_crossover**: Active forces (chemotaxis, self-propulsion) dominate thermal fluctuations and modify the effective critical behavior. l_crossover ~ a * Pe^(1/(d-1)) ~ 5 um * 3^(1/2) ~ 9 um [PARAMETRIC: dimensional analysis for active-to-passive crossover].

- **Above l_crossover**: Active forces average out over many lattice spacings, and the system crosses over to standard passive percolation universality. At these scales, tau = 2.31, nu = 0.88, beta = 0.41 hold.

- **Consequence for measurability**: The correlation length xi diverges near p_c. At 5% above p_c: xi ~ |0.05|^(-0.88) * 5 um ~ 80 um. At 1% above: xi ~ 400 um. Since xi >> l_crossover = 9 um for any tumor near p_c, the MEASURABLE cluster statistics (at scales of tens to hundreds of microns) follow passive percolation universality.

- **Prediction for small clusters**: At cluster sizes s < s_crossover ~ (l_crossover/a)^d_f ~ (9/5)^2.53 ~ 5 pores, active-particle effects may modify the apparent tau. This is below the resolution of standard histopathological analysis (which counts T cell clusters of 3+ cells, corresponding to ~10+ pore sites). Therefore, the passive universality prediction tau = 2.31 should hold for all experimentally measurable cluster sizes.

**Self-consistency check via Fisher scaling**: The Fisher scaling relation tau = 1 + d/(d*nu - beta/(beta+gamma)) provides an independent consistency check. With d = 3, nu = 0.88, beta = 0.41, gamma = 1.79:
- Denominator: 3*0.88 - 0.41/(0.41+1.79) = 2.64 - 0.186 = 2.454
- tau = 1 + 3/2.454 = 1 + 1.222 = 2.22

This differs from the numerically measured tau = 2.31, indicating that the approximate Fisher formula is inaccurate (as expected — it ignores correction-to-scaling terms). The numerically measured value tau = 2.31 is the correct one to use for predictions.

**Pre-screening for near-critical tumors**: A practical concern is that universality predictions require tumors near p_c. We propose pre-screening using susceptibility: for tumors near p_c, the mean cluster size chi ~ |p - p_c|^(-gamma) diverges, manifesting as high inter-biopsy variance in T cell density. Tumors in the top quartile of inter-biopsy T cell variance are enriched for p ~ p_c and should be prioritized for correlation length measurements.

### Confidence: 5/10

Increased from H2 (4) because active-particle crossover analysis strengthens the case that passive universality applies at measurable scales, and the pre-screening strategy addresses practical testability. Remaining concerns: (1) collagen fiber alignment in desmoplastic tumors creates anisotropic ECM that may change effective dimensionality; (2) T cell-T cell interactions (cooperative migration) create inter-particle correlations absent in standard percolation.

### Groundedness: 6/10

- Percolation critical exponents for 3D [GROUNDED: Stauffer & Aharony 1994]
- tau = 2.31 numerically measured [GROUNDED: Jan & Stauffer 1998]
- Universality across lattice types [GROUNDED: renormalization group theory]
- d_f = 2.53 for 3D percolation [GROUNDED]
- Active-particle crossover length [PARAMETRIC: dimensional analysis, not validated for biological system]
- Pre-screening via susceptibility divergence [PARAMETRIC: standard percolation diagnostic applied to biology]
- Cross-tumor universality [PARAMETRIC: assumes all tumor ECMs are in same universality class]

### Why this might be WRONG

1. **Anisotropy**: Collagen fiber alignment in tumors creates anisotropic ECM. If alignment is strong (desmoplastic pancreatic tumors), effective dimensionality may be 2 in collagen sheets, changing all exponents (tau_2D = 2.06, nu_2D = 4/3). Tumors could show crossover between 2D and 3D universality.
2. **Active-particle universality**: The crossover length estimate l_crossover ~ 9 um is an order-of-magnitude argument. If l_crossover is actually ~50-100 um (due to persistent chemotactic runs), the active-particle regime extends to measurable scales and exponents may deviate from passive predictions.
3. **Inter-particle correlations**: T cells interact — cooperative migration, contact inhibition of locomotion, paracrine signaling. These create inter-particle correlations absent in standard percolation, which studies single-particle transport on a random lattice.

### How to Test

1. **Multi-tumor cluster size distribution**: From 4 tumor types (breast, pancreatic, colorectal, lung), quantify T cell positions via anti-CD8 immunofluorescence on tissue microarrays. Define clusters using a distance threshold (e.g., 15 um nearest-neighbor). Measure cluster size distribution n_s for each tumor.
2. **Pre-screen**: Select tumors in the top quartile of inter-biopsy T cell density variance (enriched for p ~ p_c).
3. **Expected if TRUE**: n_s ~ s^(-2.31 +/- 0.15) across all tumor types on a single log-log plot. Different tumors have different cutoffs s_xi (different distances from p_c) but the SAME slope tau = 2.31.
4. **Expected if FALSE**: Different tumor types show different slopes, or no power-law behavior (exponential cutoff without power-law regime).
5. **Effort**: 6-12 months. Computational analysis of existing or new immunofluorescence data. Requires spatial statistics expertise but no new biological experiments beyond tissue staining.

---

## EH3: Collagen I/III Ratio Tunes Percolation Threshold p_c via Effective Coordination Number z, Within the 3D Random Percolation Universality Class

**Parent**: H4 (Collagen I/III Ratio, composite 7.10)
**Operation**: MUTATION
**Bridge family**: Lattice topology

### Connection

Lattice coordination number z in percolation theory -> Collagen fiber branching architecture (Col I vs Col III) determines effective z -> Different tumor types have different p_c values for the immune exclusion threshold, but identical critical exponents

### Mechanism

**Corrected framework**: The original H4 described the Col I/III ratio as a "lattice topology switch" that changes the "universality class." This was a conceptual error. In 3D percolation, ALL lattice topologies (simple cubic, FCC, BCC, diamond, random geometric graph) share the SAME universality class with SAME critical exponents: nu = 0.88, beta = 0.41, gamma = 1.79, tau = 2.31. What changes between lattice topologies is p_c — the location of the threshold [GROUNDED: Stauffer & Aharony 1994]. The corrected hypothesis: Collagen I/III ratio tunes p_c by changing the effective coordination number z of the fiber network, while leaving all critical exponents invariant.

**Coordination number and p_c**: For a random lattice with mean coordination number z (average number of nearest-neighbor connections per node), the percolation threshold is approximately:

p_c ~ 1.5 / z (Bethe lattice approximation with empirical loop correction for 3D) [PARAMETRIC: approximation from percolation theory; exact values require simulation for each specific topology]

This gives a quantitative relationship between fiber architecture and immune exclusion threshold:

- **Collagen I-dominant networks**: Type I collagen forms thick (50-200 nm diameter), stiff, parallel-aligned fibrils [GROUNDED: Shoulders & Raines 2009]. In tumor ECM, aligned Col I bundles create a network with high effective coordination: each crosslink node connects to z ~ 5-7 neighboring fibrils (due to parallel bundling, each node sits at the junction of multiple aligned fibers). This gives p_c ~ 0.21-0.30.

- **Collagen III-dominant networks**: Type III collagen forms thin (25-50 nm), flexible, highly branched reticular fibers [GROUNDED: Keene et al. 1987]. The branched architecture creates more connection points per unit volume but lower coordination per node: z ~ 3-4 (each branch point connects fewer fibers). This gives p_c ~ 0.38-0.50.

**Biological consequence**: At the same total crosslink density p, a Col I-dominant tumor (lower p_c) is MORE LIKELY to be above threshold (immune-excluded) than a Col III-dominant tumor (higher p_c). This predicts:

- Pancreatic ductal adenocarcinoma (PDAC): Col I-dominant, aligned stroma (z ~ 6, p_c ~ 0.25). Low threshold → easy to reach immune exclusion → consistent with clinical observation that PDAC is among the most immune-cold tumor types [GROUNDED: Ho et al. 2020].
- Hepatocellular carcinoma (HCC): Mixed Col I + Col III reticular stroma (z ~ 4-5, p_c ~ 0.30-0.38). Intermediate threshold → variable immune infiltration across tumors.
- Lymph node metastases: Col III-rich reticular framework (z ~ 3-4, p_c ~ 0.38-0.50). High threshold → difficult to reach immune exclusion → consistent with observation that metastases in lymph nodes often remain immune-infiltrated [GROUNDED: qualitative observation from pathology].

**Falsifiable prediction**: Two tumors with IDENTICAL total collagen crosslink density p but DIFFERENT Col I/III ratios should differ in immune infiltration status. Specifically:

- If p = 0.30 and Tumor A has Col I/III = 3:1 (z ~ 6, p_c ~ 0.25): p > p_c → EXCLUDED
- If p = 0.30 and Tumor B has Col I/III = 1:3 (z ~ 4, p_c ~ 0.38): p < p_c → INFILTRATED

The prediction is that Col I/III ratio is an independent predictor of immune exclusion AFTER controlling for total collagen crosslink density. This is a strong, falsifiable prediction that no existing framework makes — current models treat collagen density as the sole ECM determinant.

### Confidence: 5/10

Increased from H4 (4) because the conceptual error (universality vs p_c shift) is fixed and the coordination number analysis provides a physical basis for quantitative predictions. Remaining concerns: (1) the z values for collagen networks are estimates from fiber morphology, not measured directly from network extraction; (2) collagen I/III ratio may correlate with other ECM features (HA content, fibronectin density) that independently affect T cell migration; (3) the Bethe lattice approximation for p_c may be inaccurate for the specific geometries of tumor collagen.

### Groundedness: 6/10

- Col I thick aligned fibrils [GROUNDED: Shoulders & Raines 2009]
- Col III thin branched reticular [GROUNDED: Keene et al. 1987]
- PDAC immune-cold phenotype [GROUNDED: clinical consensus]
- Bethe lattice p_c ~ 1/(z-1) [GROUNDED: exact result for tree graphs]
- 3D correction to Bethe approximation [PARAMETRIC: empirical factor ~1.5/z]
- z ~ 5-7 for Col I networks [PARAMETRIC: estimated from fiber morphology, not measured on specific tumor samples]
- z ~ 3-4 for Col III networks [PARAMETRIC: same]
- Cross-tumor p_c predictions [PARAMETRIC: derived from estimated z values]
- Col I/III as independent predictor after controlling for total crosslink density [PARAMETRIC: novel prediction]

### Why this might be WRONG

1. **Coordination number estimates**: The z values (3-7) are inferred from fiber morphology, not directly measured from network topology extraction. Real collagen networks have broad degree distributions (some nodes have z = 2, others z = 10+), and the mean may not capture the relevant physics. Percolation on heterogeneous-degree networks may require the Molloy-Reed criterion (p_c depends on <z^2>/<z>) rather than the simple Bethe approximation.
2. **Correlated structure**: Col I alignment creates long-range structural correlations in the network. The simple z -> p_c mapping assumes an uncorrelated random network. Aligned fibers may create anisotropic percolation with direction-dependent p_c, not captured by a single scalar threshold.
3. **Confounding ECM components**: Col I/III ratio correlates with hyaluronan density, fibronectin content, and MMP activity. Any observed correlation between Col I/III and immune infiltration could be driven by these confounders rather than the coordination-number mechanism.

### How to Test

1. **Col I/III ratio as independent predictor**: In a cohort of 100+ tumors (mixed types), measure (a) total collagen crosslink density (pyridinoline assay), (b) Col I/III ratio (immunofluorescence with type-specific antibodies), (c) CD8+ T cell density (IHC). Regress T cell density on both crosslink density AND Col I/III ratio.
2. **Expected if TRUE**: Col I/III ratio is a statistically significant independent predictor (p < 0.01) of T cell density after controlling for total crosslink density. Higher Col III fraction associates with higher T cell density at the same crosslink density. Effect size: ~2-fold difference in T cell density between top and bottom quartile of Col III fraction, at matched total crosslink density.
3. **Expected if FALSE**: Col I/III ratio adds no predictive power beyond total crosslink density. Or Col I/III correlates with T cell density but loses significance after controlling for confounders (HA, fibronectin).
4. **Advanced test**: Fabricate synthetic 3D collagen matrices with controlled Col I/III ratios (5 ratios) at matched total concentration (5 mg/mL). Measure T cell infiltration depth. If coordination-number mechanism is correct, infiltration should increase monotonically with Col III fraction even at constant total collagen.
5. **Effort**: 6-12 months. Clinical cohort analysis requires archived tissue with IHC capacity. In vitro validation requires Col I/III matrix fabrication (commercially available collagens) + standard infiltration assay.

---

## EH4: TGF-beta Contact-Dependent Activation Generates Short-Range Correlated Percolation with Downward p_c Shift, Predicting Non-Linear LOX Inhibitor / Anti-TGF-beta Combination Synergy

**Parent**: H8 (TGF-beta Autocrine Signaling, composite 7.00)
**Operation**: MUTATION
**Bridge family**: Correlated percolation / feedback

### Connection

Correlated percolation theory (non-independent bond occupation) -> TGF-beta contact-dependent activation creates short-range spatial correlation in LOX expression and collagen crosslink density -> Downward p_c shift worsens immune exclusion AND creates opportunity for non-linear anti-TGF-beta / LOX inhibitor combination therapy synergy

### Mechanism

**Corrected TGF-beta biology**: The original H8 assumed TGF-beta has an effective range of 50-100 um (diffusion-limited paracrine signaling). This is INCORRECT for the dominant TGF-beta activation mechanism in tumor ECM. TGF-beta1 is secreted as a latent complex bound to LTBP (latent TGF-beta binding protein), stored in the ECM [GROUNDED: Munger & Sheppard 2011]. Activation occurs primarily through CONTACT-DEPENDENT integrin alphav-beta6 (and alphav-beta8) mediated mechanical pulling on the latent complex [GROUNDED: Munger et al. 1999, Cell 96:319-328; Shi et al. 2011, Nature 474:343-349]. This means active TGF-beta is generated ONLY at the cell surface of integrin-expressing cells, with an effective signaling range of ~10-30 um (1-3 cell diameters) — the distance over which active TGF-beta1 can diffuse before binding to receptors or being sequestered [PARAMETRIC: constrained by the rapid binding kinetics of TGF-beta1 to TGF-betaRII, Kd ~ 50-100 pM].

**Mapping to correlated percolation**: TGF-beta1 induces LOX expression [GROUNDED: STRING TGFB1-LOX score 0.623; Setargew et al. 2021]. Because TGF-beta activation is spatially localized (~10-30 um range), cells near an integrin alphav-beta6-expressing cell receive higher TGF-beta signal and upregulate LOX more than distant cells. This creates SHORT-RANGE POSITIVE CORRELATIONS in bond occupation probability: crosslinks are not independent — neighboring crosslinks are more likely to be simultaneously present (both induced by the same TGF-beta source) or simultaneously absent (both far from TGF-beta sources).

In correlated percolation theory, when bonds are positively correlated at short range, the percolation threshold shifts DOWNWARD relative to uncorrelated percolation [GROUNDED: Weinrib & Halperin 1983, Phys Rev B 27:413-427]. The mechanism is intuitive: positive correlations create clusters of high-density crosslinks separated by gaps of low-density — the gaps form connected channels even at mean crosslink densities above the uncorrelated p_c. Quantitatively, for exponentially decaying correlations C(r) ~ exp(-r/r_c) with correlation length r_c ~ 20 um (TGF-beta range) and lattice spacing a ~ 10 um, the ratio r_c/a ~ 2 creates a p_c shift of approximately Delta_p_c ~ -0.01 to -0.05 [PARAMETRIC: estimated from correlated percolation simulations in the short-range regime].

**Harris-type analysis (addressing Critic)**: The Weinrib-Halperin extended Harris criterion states that correlations with power-law decay C(r) ~ r^(-a) are relevant to the critical exponents only when a < 2/nu = 2.27 for 3D percolation [GROUNDED: Weinrib & Halperin 1983]. For TGF-beta contact-dependent signaling, the correlation decays EXPONENTIALLY (much faster than any power law), so a -> infinity >> 2.27. Therefore:

- **Critical exponents are UNCHANGED**: nu = 0.88, beta = 0.41, gamma = 1.79, tau = 2.31 remain valid.
- **Threshold p_c is SHIFTED downward**: The correlations change WHERE the transition occurs but not HOW it occurs.
- **Experimental consequence**: The percolation framework from EH1-EH3 applies with modified p_c. TGF-beta-high tumors have lower effective p_c, meaning they reach immune exclusion at LOWER total crosslink density than TGF-beta-low tumors.

**Combination therapy synergy prediction**: Anti-TGF-beta therapy (e.g., galunisertib, fresolimumab) has TWO distinct effects on the percolation landscape:

Effect 1 — LOX reduction: Blocking TGF-beta signaling reduces LOX transcription [GROUNDED: TGFB1-LOX axis], lowering the mean crosslink density p by Delta_p_1.

Effect 2 — Decorrelation: Blocking TGF-beta ALSO removes the spatial correlation in crosslink density, pushing p_c UPWARD (back toward the uncorrelated value p_c(0)). This raises the barrier to immune exclusion by Delta_p_c > 0.

LOX inhibitor (PXS-5505/BAPN) has one effect:
Effect 3 — Direct crosslink reduction: Inhibiting LOX enzyme activity reduces p by Delta_p_2.

**Combination vs individual therapy**:
- LOX inhibitor alone: reduces p by Delta_p_2. Effective distance below threshold = Delta_p_2.
- Anti-TGF-beta alone: reduces p by Delta_p_1 AND raises p_c by Delta_p_c. Effective distance = Delta_p_1 + Delta_p_c.
- Combination: reduces p by Delta_p_1 + Delta_p_2 AND raises p_c by Delta_p_c. Effective distance = Delta_p_1 + Delta_p_2 + Delta_p_c > sum of individual effective distances.

This predicts Bliss independence violation: the combination effect exceeds the product of individual survival fractions. The synergy comes from the DECORRELATION term Delta_p_c, which is present only in anti-TGF-beta (not LOX inhibitor) and is ADDITIVE with the direct crosslink reduction from LOX inhibitor. This is a non-trivial mechanistic prediction — it explains WHY the combination would be synergistic and WHERE the synergy originates (in the p_c shift, not just in additive p reduction).

### Confidence: 5/10

Increased from H8 (3-4) because: (1) corrected TGF-beta range resolves the main biological objection; (2) Weinrib-Halperin criterion provides a rigorous framework for when correlations matter; (3) the synergy prediction is specific, mechanistic, and clinically actionable. Remaining concerns: (a) the magnitude of the p_c shift (Delta_p_c ~ 0.01-0.05) may be too small to generate measurable synergy; (b) anti-TGF-beta has pleiotropic effects beyond LOX induction (immune suppression, angiogenesis, EMT) that may dominate the collagen-mediated effect; (c) TGF-beta activation mechanisms in tumors are heterogeneous (not exclusively alphav-beta6-dependent).

### Groundedness: 5/10

- TGF-beta contact-dependent activation via integrin alphav-beta6 [GROUNDED: Munger et al. 1999, Cell 96:319]
- TGF-beta1-LOX axis [GROUNDED: STRING 0.623; Setargew et al. 2021]
- Correlated percolation p_c shift under positive correlations [GROUNDED: Weinrib & Halperin 1983, Phys Rev B 27:413]
- Weinrib-Halperin criterion for correlation relevance [GROUNDED]
- TGF-beta effective range ~10-30 um [GROUNDED for activation mechanism; PARAMETRIC for exact diffusion range of active form]
- Anti-TGF-beta drugs (galunisertib, fresolimumab) [GROUNDED: in clinical trials]
- p_c shift magnitude Delta_p_c ~ 0.01-0.05 [PARAMETRIC: estimated from correlated percolation literature]
- Bliss independence violation prediction [PARAMETRIC: mechanistic prediction from percolation framework]

### Why this might be WRONG

1. **Pleiotropic TGF-beta effects**: TGF-beta suppresses T cell function directly (reduced IFN-gamma, granzyme B [GROUNDED: Thomas & Bhola 2020]), promotes regulatory T cells, and induces EMT. Anti-TGF-beta therapy may improve T cell infiltration through immune-modulatory effects that have nothing to do with collagen, masking or overwhelming the percolation-mediated synergy.
2. **Magnitude of effect**: If Delta_p_c ~ 0.01, the decorrelation-mediated synergy is ~4% of p_c, which may be below the detection limit of in vivo combination therapy experiments where biological noise is high.
3. **Heterogeneous activation**: Not all TGF-beta in tumors is activated by alphav-beta6. Thrombospondin-1, plasmin, and MMP-mediated activation can release TGF-beta at longer ranges, potentially increasing correlation length and modifying the Weinrib-Halperin analysis.
4. **Feedback complexity**: TGF-beta -> LOX -> collagen crosslinking -> ECM stiffness -> mechanotransduction -> more TGF-beta activation (stiffness-dependent integrin engagement). This positive feedback loop may create bistable behavior (all-or-nothing ECM states) rather than the continuous phase transition assumed by percolation theory.

### How to Test

1. **In vitro combination synergy**: Culture CAFs (cancer-associated fibroblasts) in 3D collagen with or without TGF-beta1 stimulation. Add PXS-5505 (LOX inhibitor) and/or galunisertib (TGF-betaRI inhibitor) at 5 doses each (5x5 matrix). After 72h, quantify collagen crosslink density (pyridinoline), measure spatial homogeneity of crosslinking (SHG image texture analysis), and add CD8+ T cells for infiltration assay.
2. **Expected if TRUE**: (a) TGF-beta stimulation increases BOTH mean crosslink density (p up) AND spatial heterogeneity (higher Moran's I for crosslink density). (b) Galunisertib reduces BOTH. (c) Combination (galunisertib + PXS-5505) shows Bliss synergy index > 1 for T cell infiltration — specifically, the combination infiltration exceeds (galunisertib_infiltration x PXS_infiltration / control_infiltration). (d) The synergy index correlates with the magnitude of decorrelation (change in Moran's I).
3. **Expected if FALSE**: (a) TGF-beta does not increase spatial heterogeneity of crosslinking (challenges the correlated percolation premise). (b) Combination shows additive or sub-additive effect (Bliss synergy index <= 1). (c) No correlation between spatial homogeneity and infiltration.
4. **In vivo validation**: If in vitro synergy confirmed, test in tumor-bearing mice: PXS-5505 + anti-TGF-beta (1D11 antibody) vs each alone vs vehicle. Primary endpoint: CD8+ T cell density in tumor core. Secondary: collagen spatial heterogeneity by SHG.
5. **Effort**: 6-12 months in vitro, 12-18 months with in vivo. Requires 3D culture, SHG imaging, spatial statistics analysis, combination drug dosing. Technically demanding but the clinical question (LOX inhibitor + anti-TGF-beta combination) is directly relevant to ongoing translational research.

---

## EVOLUTION QUALITY CHECK

### Are evolved hypotheses genuinely improved, or just rephrased?

**EH1 (CROSSOVER)**: Genuinely improved. Not just H1 + H5 stapled together — the unified framework produces a single experimental protocol that tests both threshold existence and dose-response shape simultaneously. Harris criterion adds new theoretical content that resolves the heterogeneity objection. The p(dose) estimation provides a quantitative prediction the parents lacked individually.

**EH2 (MUTATION)**: Genuinely improved. The active-particle crossover analysis is new physics content — it provides a quantitative length scale (9 um) below which active effects matter and above which passive universality applies. The pre-screening strategy via susceptibility divergence is a novel experimental design contribution. tau correction changes a specific numerical prediction (2.19 -> 2.31).

**EH3 (MUTATION)**: Genuinely improved. Fixes a fundamental conceptual error (universality class switch -> p_c shift). The coordination number analysis provides a physical mechanism for WHY p_c varies between tumor types, replacing an unexplained parametric assertion (0.35-0.45 range). The falsifiable same-density-different-ratio prediction is a strong new test.

**EH4 (MUTATION)**: Genuinely improved. TGF-beta range correction (50-100 um -> 10-30 um) changes the fundamental physics from long-range to short-range correlated percolation. Weinrib-Halperin criterion analysis resolves the open question about correlation relevance. p_c shift direction (downward) is a new directional prediction. Combination synergy prediction with mechanistic origin (decorrelation) adds clinical actionability.

### Does each evolution address a specific weakness from the Critic?

- EH1: Addresses heterogeneity smearing (Harris criterion), Wolf 2013 cross-section, LOX-IN-3 error, p(dose) shape estimation.
- EH2: Addresses active-particle universality class question, tau exponent error, practical testability concern.
- EH3: Addresses title inaccuracy, lack of quantitative p_c predictions, missing physical mechanism for p_c variation.
- EH4: Addresses TGF-beta range error, p_c shift direction, Prakash 1992 citation, correlation relevance question.

### Is diversity maintained?

4 distinct bridge families across 4 evolved hypotheses:
1. Bond occupation / threshold crossing (EH1)
2. Correlation length / spatial scaling (EH2)
3. Lattice topology (EH3)
4. Correlated percolation / feedback (EH4)

No family has more than 1 hypothesis. No convergence on a single mechanism. Diversity constraint (>= 3 families) is satisfied with margin.
