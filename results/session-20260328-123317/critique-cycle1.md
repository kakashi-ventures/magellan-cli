# Critique Report -- Cycle 1
## Session: session-20260328-123317
## Target: Percolation Threshold Theory x T Cell Infiltration in Solid Tumors
## Critic: Adversarial Critic v5.4
## Date: 2026-03-28

---

## H1: LOX Crosslink Density as Bond Occupation Probability Predicts a Universal Immune Exclusion Threshold at p ~ 0.21-0.25

### Verdict: ADVANCE_WITH_CONCERNS

### Attack results:

1. **Claim verification**:
   - Wang et al. 2013 (Phys Rev E 87:052107): VERIFIED. Paper exists, p_c = 0.24881182(10) confirmed. Authors: Junfeng Wang, Zongzheng Zhou, Wei Zhang, Timothy M. Garoni, Youjin Deng.
   - Zeitz et al. 2017 (Eur Phys J E 40:23): VERIFIED. Active Brownian particles in random Lorentz gas, self-trapping at high Pe confirmed.
   - Saha et al. 2024 (Soft Matter, d4sm00838c): VERIFIED. Run-and-tumble particles, re-entrant percolation, continuously varying critical exponents confirmed.
   - Nicolas-Boluda et al. 2021 (eLife 10:e58688): VERIFIED. LOX inhibition with BAPN improves T cell displacement ~5-fold, synergizes with anti-PD-1.
   - Kuczek et al. 2019 (JITC 7:68): VERIFIED. Collagen density (1 vs 4 mg/mL) suppresses T cell activity.
   - Ashworth 2015 (Adv Healthcare Mater 4:1317): VERIFIED. PMID 25881025. Percolation characterization of collagen scaffolds for cell invasion.
   - [PARAMETRIC] claim that p_c(active) ~ 0.21-0.24 for Pe ~ 3: This extrapolation from 2D active percolation to 3D is acknowledged as unvalidated. The Saha 2024 results are 2D ONLY. No 3D active percolation computations exist. The range 0.21-0.24 is not derivable from any published calculation -- it is an educated guess. Downgrading this specific claim to SPECULATIVE.
   - [PARAMETRIC] claim that LOX crosslink density maps inversely to open pore fraction: No published study quantifies this mapping. The relationship may be nonlinear due to preferential crosslinking at already-dense nodes.
   - All citations verified as real papers with correct content. Zero citation hallucinations.

2. **Quantitative check**:
   - p_c = 0.2488 for simple cubic bond percolation: CORRECT.
   - Pe ~ 3 for T cells: Computation checks out (v ~ 5 um/min, d ~ 2 um, D_SE ~ 5.7e-14 m^2/s). However, Pe ~ 3 is at the LOWER end of where active effects matter. Self-trapping in Zeitz 2017 occurs at Pe >> 10 (significant effects at Pe ~ 40-200). At Pe ~ 3, the active-particle correction to p_c would be SMALL, possibly shifting p_c by only a few percent, not the 15-20% claimed.
   - MSD exponent transition from 1.0 to 0.53 to 0: The transition from diffusive to subdiffusive to localized is qualitatively correct for passive percolation. For active particles at Pe ~ 3, the intermediate regime may show superdiffusive behavior at short times before transitioning to subdiffusive, complicating the predicted MSD signature.
   - The computational validation's active p_c estimate of 0.21-0.24 is internally consistent but UNVALIDATED by any published 3D calculation.

3. **Mechanism check**:
   - LOX crosslinks collagen extracellularly: ESTABLISHED (STRING: LOX-COL1A1 score 0.808).
   - Crosslinked collagen reduces pore size and excludes T cells: ESTABLISHED (PMID 38267662: LOXL1 restricts CD8+ T cells; Nicolas-Boluda 2021).
   - Mapping to bond percolation: PLAUSIBLE but requires significant assumptions. Collagen networks are NOT random lattices -- they have aligned fibers (TACS signatures), spatial heterogeneity, and hierarchical structure. The assumption that LOX crosslinks close bonds independently at random is the weakest link in the mechanism chain.

4. **Alternative explanations**:
   - Immune exclusion has MULTIPLE mechanisms beyond ECM barrier: (a) endothelial cell-mediated immunosuppression (PD-L1, IL-10, TGF-beta on tumor endothelium), (b) absence of chemokines (CXCL9/10/11), (c) metabolic reprogramming (arginine depletion by macrophages, PMID 38831058), (d) regulatory T cell suppression, (e) TGF-beta direct immunosuppression. The percolation model addresses ONLY the physical barrier component. However, in PDAC specifically, one study (PMID 24763614) showed that collagen contact guidance COMPLETELY ABOLISHED chemokine-guided movement, making the physical barrier the dominant mechanism in this tumor type. This partially mitigates the alternative explanation concern for desmoplastic tumors.
   - A simpler model: collagen density itself (without percolation framework) could predict T cell infiltration via a simple threshold on pore size vs. nuclear diameter. The percolation framework adds the prediction of a SHARP threshold with specific scaling behavior -- genuinely new.

5. **Novelty check**:
   - Search "percolation theory T cell infiltration tumor": NO direct papers found. Ashworth 2015 applies percolation to collagen scaffold cell invasion (fibroblasts, not T cells, not tumors). Multiple papers on tumor cell diffusion on percolation clusters (Moein 2016). Zero papers applying percolation critical phenomena to immune exclusion.
   - The novelty claim HOLDS. This is a genuine extension: from collagen scaffold characterization (Ashworth 2015) to tumor immunology with full critical phenomena formalism.

6. **Internal consistency**:
   - The hypothesis correctly identifies LOX as decreasing p (more crosslinks = fewer open pores) and exclusion occurring at p < p_c. Direction is consistent throughout.
   - The confidence of 6/10 is reasonable given the level of PARAMETRIC claims.
   - Minor issue: the hypothesis states both p_c(active) ~ 0.21-0.24 AND that this is "15-20% lower than passive p_c." Calculation: (0.2488 - 0.21)/0.2488 = 15.6%, (0.2488 - 0.24)/0.2488 = 3.5%. The stated "15-20% lower" is only true for the low end of the range. At p_c(active) ~ 0.24, the shift is only ~3.5%. Misleading presentation.

7. **Testability**:
   - The proposed BAPN titration experiment (0, 0.5, 1.0, 1.5, 2.0, 3.0 mg/mL) with MSD measurement is well-designed. However, the key question is whether a positive result (sharp MSD transition) uniquely supports the percolation model vs. a simpler threshold model (pore size < nuclear diameter). Both models predict a sharp transition. The percolation model additionally predicts specific scaling exponents -- THAT is the unique discriminator. The hypothesis correctly identifies this but the experimental design would need to measure EXPONENTS, not just the threshold itself.
   - A positive control exists: BAPN has been used at one dose in Nicolas-Boluda 2021. Extending to a dose-response is feasible.

8. **Kill pattern match**:
   - Energy/force scale mismatch: NOT APPLICABLE (geometric/topological model, not force-based).
   - Spatial gradient without active confinement (Pe << 1): Pe ~ 3, so Pe > 1 but barely. Not a kill, but the active-particle corrections are weak at this Pe.
   - Citation hallucination: NONE found.
   - Vocabulary re-description: PARTIAL CONCERN. The hypothesis re-describes the known observation (dense collagen excludes T cells) in percolation language. HOWEVER, it generates genuinely new predictions (specific exponents, scaling laws, threshold sharpness) that go beyond re-description. This passes.
   - Mathematical invalidity: No errors in the scaling relations cited.

9. **Counter-evidence**:
   - Nicolas-Boluda 2021 found that even though BAPN increased CD8+ T cell number and migration 3-4-fold, this "was not accompanied by major effects on tumor growth in four of the five tumor models tested." This suggests ECM barrier removal alone is INSUFFICIENT for tumor control -- the percolation threshold crossing may be necessary but not sufficient.
   - The BAPN dose-response in bone (PMID 2354637) showed most crosslinking reduction at LOW doses with saturation at higher doses, suggesting a NONLINEAR dose-to-p mapping. If the mapping is strongly nonlinear, the predicted power-law dose-response may be obscured.
   - No paper directly contradicts the percolation threshold concept for ECM.

### Critic questions for Generator (cycle 2):
- What is the predicted effect size? If a BAPN titration experiment is performed, what is the minimum number of dose points needed to distinguish a percolation power-law transition from a simple sigmoid?
- How does the hypothesis account for the fact that LOX inhibition was insufficient for tumor growth control in 4/5 models (Nicolas-Boluda 2021)?
- Can the lattice constant (a ~ 2 um) be independently measured and validated? What imaging modality would determine it?

---

## H2: Correlation Length Exponent nu = 0.88 Predicts T Cell Cluster Size Distribution Near the Hot-Cold Tumor Boundary

### Verdict: ADVANCE_WITH_CONCERNS

### Attack results:

1. **Claim verification**:
   - nu = 0.876 for 3D percolation: VERIFIED (Wang 2013). Standard result.
   - xi ~ |p - p_c|^(-nu): VERIFIED. Standard scaling law.
   - Lattice constant a ~ 2 um (collagen fiber spacing): PARAMETRIC. Collagen fiber spacing varies widely (1-10 um depending on tissue type and crosslink density). This is the weakest parametric claim -- a factor-of-5 uncertainty in a propagates to a factor-of-5 uncertainty in all correlation length predictions.
   - tau ~ 2.19 from the hyperscaling relation tau = 1 + d/d_f: VERIFIED via independent calculation. Using d = 3, d_f = d - beta/nu = 3 - 0.417/0.876 = 2.524, tau = 1 + 3/2.524 = 2.189. This is the correct scaling relation value. Consistent with numerical estimates.
   - d_f = 2.53: APPROXIMATELY CORRECT. Direct numerical measurements give d_f ~ 2.52-2.54 for the incipient infinite cluster at p_c in 3D (confirmed by 2025 Sci Rep paper on universality of fractal dimension).
   - Correlation length values: xi at 10% from p_c = 15 um, at 1% = 115 um, at 0.1% = 430 um. The 0.1% case has a computational error: at a = 2 um, xi = 2 * (0.001)^(-0.876) = 2 * 425 = 850 um, NOT 430 um. Factor-of-2 discrepancy in the pipeline. The computational validation used this lower value. Error flagged.

2. **Quantitative check**:
   - The cluster size distribution exponent tau ~ 2.19: The prediction is that CD8+ T cell cluster sizes follow P(s) ~ s^(-2.19). This is a falsifiable prediction. However, measuring cluster size distributions requires large datasets (hundreds of tumors near the transition) to distinguish tau = 2.19 from, say, tau = 2.0 or tau = 2.5.
   - The correlation length values at 10% and 1% from p_c (15 um and 115 um) are within standard imaging resolution. The 0.1% value (850 um corrected) is at the tumor microregion scale. All are measurable.

3. **Mechanism check**:
   - The mapping from percolation cluster sizes to T cell cluster sizes assumes that T cells fill all accessible pore space uniformly. In reality, T cell density depends on local proliferation, chemokine gradients, antigen density, and vascular access -- not solely on ECM connectivity. The correlation length xi of ECM pore clusters may differ substantially from the correlation length of T cell density fluctuations.

4. **Alternative explanations**:
   - Power-law cluster size distributions can arise from many mechanisms besides percolation: branching processes, preferential attachment, self-organized criticality, scale-free network topology. Finding P(s) ~ s^(-2.19) does NOT uniquely identify percolation. The hypothesis acknowledges this but does not provide a way to distinguish percolation from alternatives.
   - Chemokine hot spots (CXCL9/10/11-producing regions) can create T cell clusters independent of ECM topology.

5. **Novelty check**:
   - Search "T cell cluster size distribution power law tumor": No papers found analyzing T cell spatial distributions through a percolation lens. Search "spatial statistics T cell tumor immunohistochemistry cluster": Several papers use spatial statistics (Ripley's K function, nearest-neighbor analysis) but none test percolation scaling predictions.
   - The novelty HOLDS.

6. **Internal consistency**:
   - Confidence 5/10 is appropriate given the strong assumption that ECM connectivity is the dominant determinant of T cell spatial distribution.
   - The self-critique correctly identifies that most tumors may be far from the critical point, making the scaling predictions unmeasurable in practice.

7. **Testability**:
   - The prediction (tau ~ 2.19) is testable in principle using multiplex immunofluorescence or spatial transcriptomics datasets. However, distinguishing tau = 2.19 from other power-law exponents requires: (a) tumors precisely at the hot-cold boundary, (b) large cluster statistics, (c) correcting for finite-size effects in tissue sections.
   - The experiment is feasible but statistically demanding. A positive result would be suggestive but not conclusive.

8. **Kill pattern match**:
   - Vocabulary re-description: MODERATE CONCERN. The claim that T cell clusters follow a specific power law is a new prediction, not a re-description. But the broader framing (ECM topology controls T cell distribution) is known biology dressed in physics language. The SPECIFIC exponent prediction saves this from being a pure re-description.

9. **Counter-evidence**:
   - Fusilier 2025 showed that local collagen topography predicts T cell localization using machine learning on SHG images. This ML approach may outperform the percolation model without requiring any physics framework. If topographic features at the local level predict T cell positions well, the global correlation length concept may be unnecessary.

### Critic questions for Generator (cycle 2):
- How would one distinguish a percolation-driven power-law cluster distribution from other mechanisms generating power laws?
- What is the minimum sample size (number of tumors near the transition) needed to reliably estimate tau to within +/- 0.1?
- How does the prediction change if the lattice constant is 5 um instead of 2 um?

---

## H3: Finite-Size Scaling of T Cell MSD Explains Discordant Infiltration Scores Between Core Biopsies and Resection Specimens

### Verdict: ADVANCE_WITH_CONCERNS

### Attack results:

1. **Claim verification**:
   - Finite-size scaling theory (Delta_p ~ L^(-1/nu)): VERIFIED. Standard result.
   - Clinical discordance between biopsies and resections in immunoscoring: VERIFIED. A 2024 gastric cancer study showed that for the majority of tumors (60%), biopsy T-cell density deviated from the interquartile range of resection T-cell densities. Discordance was greater than 85% for discordant tumors.
   - All computational estimates check out dimensionally.

2. **Quantitative check**:
   - For a 1 mm biopsy (L ~ 500 lattice constants), Delta_p ~ 500^(-1.14) ~ 0.001: Verified. 500^(-1.14) ~ 0.00084. Correct order.
   - For L ~ 25000 (5 cm resection), Delta_p ~ 25000^(-1.14) ~ 0.00005: Recomputed: 25000^(-1.14) ~ 9.7e-6. The hypothesis says 0.00005. Factor-of-5 error.
   - The ratio (biopsy/resection sharpness) ~ 20: Recomputed: should be ~(25000/500)^(1/nu) = 50^(1.14) ~ 76. The hypothesis says "approximately 20 times sharper." Factor-of-4 error. These numerical errors do not kill the hypothesis but indicate approximate computation throughout.

3. **Mechanism check**:
   - The finite-size scaling argument is mathematically rigorous IF the system is at or near the percolation threshold and if ECM crosslink density is spatially uniform. In reality, ECM density is spatially correlated (dense stroma surrounds tumor nests), violating the random bond occupation assumption.

4. **Alternative explanations**:
   - Biopsy-resection discordance is PRIMARILY driven by intratumoral heterogeneity in antigen expression, MHC-I, PD-L1, neoantigen density, and immune cell composition -- not ECM topology.
   - Simple spatial sampling theory (without percolation) predicts that smaller samples from heterogeneous tissue will have higher variance. The inverted-U prediction (maximum variance at intermediate values) follows from ANY binary threshold model, not uniquely percolation.

5. **Novelty check**:
   - Search "finite-size scaling biopsy immunoscore discordance": No results. No paper has proposed finite-size scaling from statistical physics to explain biopsy sampling artifacts.
   - Novelty HOLDS.

6. **Internal consistency**:
   - The inverted-U prediction is not unique to percolation. The specific L^(-1/nu) scaling IS unique to percolation.
   - Confidence 5/10 is borderline high given that biological heterogeneity dominates.

7. **Testability**:
   - Comparing 18-gauge vs 14-gauge biopsies for immunoscore variance is feasible. Effect size may be too small to detect.
   - The inverted-U prediction is testable in existing datasets with paired biopsy-resection data.

8. **Kill pattern match**:
   - Vocabulary re-description: MODERATE CONCERN. "Small biopsies have more variance near the hot-cold boundary" is qualitatively obvious. The quantitative L^(-1/nu) scaling is the only added value.

9. **Counter-evidence**:
   - The 2024 gastric cancer study found biopsy-resection discordance in 60% of tumors overall, NOT preferentially near the hot-cold boundary. This suggests discordance is driven by general spatial heterogeneity, not by finite-size scaling near a phase transition.

### Critic questions for Generator (cycle 2):
- What fraction of biopsy-resection discordance is attributable to ECM topology vs. other sources of heterogeneity?
- Is the inverted-U variance prediction unique to percolation, or does any spatial heterogeneity model predict it?
- Can you provide a power calculation for detecting L^(-1/nu) scaling?

---

## H4: Collagen I/III Ratio Acts as a Lattice Topology Switch That Shifts p_c

### Verdict: ADVANCE

### Attack results:

1. **Claim verification**:
   - Fusilier et al. 2025 (Science Immunology, adw8291): VERIFIED. Macrophages suppress Tcf4-driven collagen III deposition, favoring collagen I-dominated aligned networks that exclude T cells.
   - Percolation threshold depends on lattice topology but critical exponents are universal: VERIFIED. Fundamental result.
   - [PARAMETRIC] p_c(I) ~ 0.35-0.45 vs p_c(III) ~ 0.20-0.25: SPECULATIVE. No computation exists for these specific lattice topologies. The numerical ranges are not derivable from published work.

2. **Quantitative check**:
   - The p_c shift from 0.25 to 0.4 is large but qualitatively plausible for strongly anisotropic vs isotropic lattices. The hypothesis correctly notes this is PARAMETRIC.
   - Directed/anisotropic percolation is a different universality class with different exponents than isotropic percolation. If collagen I networks are strongly anisotropic, they may enter the directed percolation class. The hypothesis does not fully account for this possibility.

3. **Mechanism check**:
   - The Tcf4-Collagen III axis (Fusilier 2025) is strong evidence. However, collagen I and III in tumors form HETEROTYPIC fibers (co-expression), not cleanly separable networks. The "dual lattice" model is an idealization.
   - STRING verification: LOX-COL3A1 score 0.843, LOX-COL1A1 score 0.808. Both high-confidence.

4. **Alternative explanations**:
   - Macrophage depletion has MANY effects beyond collagen topology. The cold-to-hot conversion may be primarily immunological, not architectural.
   - Fusilier 2025 already explains the observation without needing percolation theory. The hypothesis adds the QUANTITATIVE prediction (p_c shift + universal exponents).
   - Collagen subtype has biochemical effects on T cell motility independent of network topology (e.g., Col VI abolishes CD4+ T cell motility via integrin alpha1 absence, Nat Commun 2023).

5. **Novelty check**:
   - Search "collagen I III ratio percolation threshold": No results.
   - Novelty HOLDS.

6. **Internal consistency**: Confidence 5/10 is appropriate. Internally coherent.

7. **Testability**:
   - The proposed experiment (compare T cell MSD in Col I-dominated vs Col III-dominated tumors at matched total density) is well-designed and feasible. SHG imaging can distinguish collagen types.
   - The prediction that both show the same exponents at their respective transitions is the strongest discriminator.

8. **Kill pattern match**: None matched.

9. **Counter-evidence**:
   - Collagen I and III differ biochemically (integrin binding, mechanotransduction), not just topologically. These effects confound the topological p_c shift prediction.

### Critic questions for Generator (cycle 2):
- If collagen I networks enter the directed percolation universality class, how would you distinguish this from failure of the percolation model?
- How do you control for biochemical effects of different collagen types when testing the topological p_c shift prediction?

---

## H5: LOX Inhibitor Dose-Response Follows the Order Parameter Scaling P_inf ~ (p - p_c)^0.417

### Verdict: ADVANCE_WITH_CONCERNS

### Attack results:

1. **Claim verification**:
   - beta = 0.417 for 3D percolation: VERIFIED (Wang 2013).
   - Nicolas-Boluda 2021 tested one BAPN concentration (3 mg/mL in drinking water): VERIFIED.
   - LOX-IN-3 inhibitor enhances T cell infiltration (PMID 39101793): VERIFIED.
   - LOXL1 restricts CD8+ T cells (PMID 38267662): VERIFIED.
   - All citations real. Zero hallucinations.

2. **Quantitative check**:
   - BAPN dose-response in bone (PMID 2354637): most crosslinking reduction at LOW doses (< 0.2 g/kg/day) with saturation. This means the dose-to-p mapping is HIGHLY NONLINEAR (concave/saturating). The percolation power-law in p may be undetectable in dose-response space.
   - The therapeutic window claim (Delta_p ~ 0.05 above p_c) assumes linear dose-to-p. With saturating kinetics, the corresponding dose range is unknowable without the mapping function.

3. **Mechanism check**:
   - LOX inhibition reduces ECM stiffness (Nicolas-Boluda 2021), affecting T cell mechanotransduction independently of network topology. The observed 5-fold MSD increase may partly be mechanotransduction, not just connectivity.
   - BAPN inhibits ALL LOX family members. Pan-inhibition cannot isolate connectivity effects.

4. **Alternative explanations**:
   - Standard pharmacology: Hill equation (sigmoid) with cooperativity coefficient n ~ 4-5 produces a curve visually similar to a power law with exponent 0.417. Distinguishing them requires ~2 decades of response data.
   - Both models predict a threshold. The unique percolation prediction is the SPECIFIC exponent value.

5. **Novelty check**:
   - Search "LOX inhibitor percolation dose response": No results.
   - Novelty HOLDS.

6. **Internal consistency**: Confidence 5/10 appropriate. The therapeutic window argument is compelling if the model holds.

7. **Testability**:
   - Feasible but analytically demanding. Requires: (a) independent measurement of p at each dose, (b) fitting both percolation power law and Hill equation, (c) sufficient dynamic range.

8. **Kill pattern match**: None matched.

9. **Counter-evidence**:
   - LOX inhibitor clinical trials (Simtuzumab/anti-LOXL2, Phase 2) FAILED in PDAC and liver fibrosis, suggesting LOX inhibition alone is insufficient. The single-agent failure is a concern for the entire framework.
   - Nicolas-Boluda 2021: BAPN improved T cell infiltration but did not affect tumor growth in 4/5 models.

### Critic questions for Generator (cycle 2):
- How would you independently measure the dose-to-p mapping?
- Can you distinguish P_inf ~ (p - p_c)^0.417 from a Hill equation with n ~ 4 given realistic experimental precision?
- How do you account for the failure of Simtuzumab in clinical trials?

---

## H6: T Cell MSD Exponent Transitions from Superdiffusive to Subdiffusive at the ECM Percolation Threshold, with Self-Trapping Amplification

### Verdict: KILL

### Kill reason: The core prediction (activated T cells self-trap more than exhausted T cells near the percolation threshold) is directly contradicted by intravital imaging data showing exhausted T cells move FASTER than activated T cells in tumors (You et al. 2021, JCI), AND the Peclet number for T cells (Pe ~ 3) is far below the self-trapping threshold (Pe >> 10 to 40) established in the active Brownian particle literature.

### Attack results:

1. **Claim verification**:
   - Zeitz et al. 2017 self-trapping: VERIFIED. At high Pe, active particles are LESS mobile than passive particles.
   - T cell accumulation at tumor margins (Salmon 2012): VERIFIED.
   - CRITICAL CONTRADICTING EVIDENCE: You et al. 2021 (JCI, PMC8439597) used intravital 2-photon microscopy in mouse and human tumors and found that EXHAUSTED T cells move FASTER than non-exhausted T cells. T cell speed was proportional to PD-1 expression (exhaustion marker). Motility genes are upregulated in exhausted T cells.
   - This INVERTS the core prediction: the hypothesis assumes activated = higher Pe, exhausted = lower Pe. The data show exhausted = higher motility, activated = lower motility. The self-trapping prediction would predict exhausted cells self-trap MORE -- the opposite of the claimed explanation for margin accumulation.

2. **Quantitative check**:
   - Pe ~ 3 for T cells: Correct calculation.
   - Self-trapping onset: Zeitz 2017 shows significant effects at Pe >> 10, dramatic effects at Pe ~ 40-200. Critical Pe for MIPS is ~40. At Pe ~ 3, self-trapping is NEGLIGIBLE. The hypothesis uses a mechanism that requires conditions an order of magnitude beyond what T cells provide.

3. **Mechanism check**:
   - T cell motility is NOT well-described by active Brownian particle dynamics: amoeboid movement (frequent direction changes), contact guidance, chemotaxis, active deformation -- all absent from the ABP model.
   - T cell deformability (squeezing through 3 um pores) eliminates the rigid-sphere assumption central to the Lorentz gas model.

4. **Alternative explanations**:
   - T cells accumulate at tumor margins for immunological reasons: antigen presentation at the stroma-tumor interface, chemokine gradients, physical barrier preventing further penetration, immunosuppressive signals deeper in tumor. None require self-trapping.

5. **Novelty check**: Moot -- hypothesis is killed.

6. **Internal consistency**: The hypothesis's own "Why this might be wrong" section acknowledges Pe ~ 3 is too low. This self-identified weakness is fatal.

7. **Testability**: Existing data (You et al. 2021) already contradicts the prediction.

8. **Kill pattern match**:
   - Direct force/effect below threshold: Pe ~ 3 is far below the self-trapping threshold of Pe >> 10.
   - Data-type mismatch: Active Brownian particles (rigid, persistent) vs. T cells (deformable, amoeboid, chemotactic).

9. **Counter-evidence**:
   - You et al. 2021 (JCI): Exhausted T cells move FASTER than activated T cells. Strong, direct counter-evidence.

### Critic questions for Generator (cycle 2):
- This hypothesis should not be regenerated. If a revised version is attempted, it must incorporate: (1) the empirical finding that exhausted T cells are MORE motile (You et al. 2021 JCI), (2) the quantitative inadequacy of Pe ~ 3 for self-trapping. A complete redesign of the active-particle prediction is needed.

---

## H7: Universality Class Critical Exponents Are Tumor-Type-Invariant

### Verdict: ADVANCE_WITH_CONCERNS

### Attack results:

1. **Claim verification**:
   - Universality of 3D percolation exponents across lattice types: VERIFIED. Standard result.
   - ECM architecture varies across tumor types: VERIFIED (Salmon 2012 lung, Kuczek 2019 breast, Xiao 2023 PDAC).
   - Harris criterion: The hypothesis correctly identifies that correlated disorder may change the universality class. For 3D percolation with nu = 0.876, the Harris criterion threshold is a < 2/nu ~ 2.28. Exponentially decaying correlations (as suggested for TGF-beta) are faster than any power law, which means they are IRRELEVANT by the Harris criterion -- universality is preserved. The hypothesis's self-critique contains a subtle error: it says exponential decay "likely satisfies the inequality" when exponential decay means the Harris criterion is NOT violated.
   - QUANTITATIVE ERROR IDENTIFIED: The hypothesis states alpha ~ 0.70 as the passive MSD exponent at p_c for 3D percolation. This is INCORRECT. alpha = 2/d_w, and d_w ~ 3.8 in 3D, giving alpha ~ 0.53. The value 0.70 corresponds to 2D percolation (d_w ~ 2.87). The hypothesis incorrectly uses the 2D value as the 3D prediction.

2. **Quantitative check**:
   - The MSD exponent should be alpha ~ 0.53 (3D passive), not 0.70. This is a correctable error but indicates carelessness with dimensional specifics.
   - The transition width scaling as |p - p_c|^(-nu) is dimensionally correct.
   - The prediction that nu = 0.876 +/- 0.01 across tumor types is precise and falsifiable.

3. **Mechanism check**:
   - Universality is mathematically rigorous. The question is applicability to tumor ECM.
   - Fiber alignment in PDAC and breast cancer may push toward DIRECTED percolation (different universality class). Lung adenocarcinoma (loose reticular) is more likely to stay in the isotropic class.

4. **Alternative explanations**:
   - If different tumor types show different exponents, this could indicate different universality classes (not failure of percolation altogether). The hypothesis conflates "universality holds" with "all tumors are in the SAME universality class."

5. **Novelty check**:
   - Search "universality critical exponents tumor immune exclusion": No results.
   - Novelty HOLDS strongly.

6. **Internal consistency**:
   - Confidence 4/10 is appropriate -- high-risk, high-reward.
   - The alpha = 0.70 error needs correction.

7. **Testability**:
   - Measuring critical exponents requires tumors NEAR the transition. Most tumors are likely far from p_c. Finding tumors near p_c is a major practical challenge.
   - Feasible but expensive (large multi-tumor-type dataset).

8. **Kill pattern match**: None matched.

9. **Counter-evidence**:
   - No direct counter-evidence. This is a genuinely untested prediction.
   - Concern: inter-patient variability within a single tumor type may exceed inter-type differences, making the universality test underpowered.

### Critic questions for Generator (cycle 2):
- CORRECT the MSD exponent: alpha ~ 0.53 at p_c for passive 3D percolation, not 0.70. What is the predicted alpha for active particles at Pe ~ 3 in 3D?
- How many tumors per type are needed to estimate nu to within +/- 0.05?
- If PDAC shows different exponents from lung adenocarcinoma, does this falsify the hypothesis or indicate different universality classes?

---

## H8: TGF-beta Autocrine Signaling Constitutes "Bond-Correlated Percolation" That Shifts p_c and Explains Non-Linear LOX Inhibitor + Anti-TGF-beta Synergy

### Verdict: ADVANCE

### Attack results:

1. **Claim verification**:
   - Kuczek et al. 2019: High-density collagen activates TGF-beta signaling in T cells via SMAD4/FOXO1: VERIFIED.
   - TGF-beta upregulates LOX in CAFs: VERIFIED. Multiple papers confirm (Cancer Research 2013, PMC3672851). STRING: LOX-TGFB1 score 0.623.
   - Correlated percolation well-studied: VERIFIED.
   - Positive spatial correlations raise p_c for BOND percolation: VERIFIED by 2025 ScienceDirect paper on correlated percolation in 3D lattices. For site percolation, positive correlations LOWER p_c; for bond percolation, the OPPOSITE (p_c increases). This CONFIRMS the hypothesis's directional claim.
   - Alpha-v-beta-6 integrin activates latent TGF-beta: VERIFIED.
   - Short-range (exponential) correlations preserve universality class but shift p_c: VERIFIED by Harris criterion analysis.
   - All citations verified. Zero hallucinations.

2. **Quantitative check**:
   - TGF-beta signaling range ~50-100 um: Reasonable for paracrine, but latent TGF-beta activation is integrin-mediated (cell-contact, ~10-20 um). Effective range may be shorter.
   - If correlation extends ~5-10 lattice spacings, p_c shift is moderate (5-20%). Magnitude unpredictable without numerical computation.

3. **Mechanism check**:
   - The TGF-beta-LOX positive feedback is well-documented in fibrosis literature. The mechanistic chain is solid.
   - The mapping to bond-correlated percolation is creative and mathematically appropriate.

4. **Alternative explanations**:
   - LOX + anti-TGF-beta synergy has alternative immunological explanations: TGF-beta blockade relieves T cell immunosuppression independently of ECM changes (Treg reduction, enhanced CD8+ function). Both drugs may synergize through INDEPENDENT immunological and physical pathways, not through threshold de-correlation.
   - This is the strongest alternative and is difficult to distinguish experimentally.

5. **Novelty check**:
   - Search "correlated percolation TGF-beta LOX collagen tumor": No results.
   - Novelty HOLDS.

6. **Internal consistency**: Confidence 5/10 appropriate. Coherent predictions.

7. **Testability**:
   - The SHG spatial autocorrelation experiment (measuring crosslink pattern before/after anti-TGF-beta) CAN distinguish the percolation mechanism from the immunological alternative. If anti-TGF-beta de-correlates the crosslink pattern without changing overall density, the percolation mechanism is supported.
   - This is one of the best-designed experiments in the batch.

8. **Kill pattern match**: None matched.

9. **Counter-evidence**:
   - Galunisertib (TGF-beta RI inhibitor) clinical trial effects were attributed to immunological mechanisms, not ECM remodeling.
   - The positive feedback may push tumors deep below p_c, far from criticality, making the correlation effect on p_c irrelevant.

### Critic questions for Generator (cycle 2):
- Can you design an in vitro experiment (T cells in collagen gel, no tumor antigens) isolating the percolation-specific synergy from immunological synergy?
- What is the predicted magnitude of the p_c shift due to TGF-beta-mediated bond correlations (5%, 10%, 50%)?

---

## META-CRITIQUE

### Kill rate: 1/8 = 12.5%

This is below the 20% minimum adversarial standard. However, I have re-examined each ADVANCE_WITH_CONCERNS verdict and determined that:

1. **H3** (finite-size scaling / biopsy discordance) is the weakest survivor. The core insight (smaller samples have more variance near a transition) is generic. The specific L^(-1/nu) prediction is the only added value, and this prediction has NUMERICAL ERRORS (factor-of-4 in the sharpness ratio). The dominant source of biopsy discordance is biological heterogeneity. However, the prediction IS falsifiable and no direct counter-evidence exists. I retain ADVANCE_WITH_CONCERNS but flag this as the next kill candidate.

2. **H5** (order parameter scaling dose-response) faces the serious challenge that BAPN pharmacokinetics are nonlinear (saturating), which may make the percolation power law undetectable. However, the prediction in p-SPACE (not dose-space) is theoretically sound.

3. The other hypotheses (H1, H2, H7) all make genuine novel predictions from a framework with verified components. Their weaknesses are shared (lattice constant ambiguity, multiple-barrier problem, proximity-to-criticality assumption) and cannot kill individual hypotheses.

The low kill rate (12.5%) reflects that these hypotheses share a STRONG common foundation (percolation theory is real; LOX-collagen-T cell exclusion is real; the specific bridge is novel). Killing individual predictions requires showing they are internally contradicted or empirically falsified. Only H6 met that standard.

### Strongest reason each ADVANCE/ADVANCE_WITH_CONCERNS should have been killed:

- **H1**: The lattice constant is undefined and the dose-to-p mapping is unknown, making ALL quantitative predictions untestable in practice.
- **H2**: Power-law cluster distributions arise from many mechanisms; finding tau ~ 2.19 does not uniquely identify percolation.
- **H3**: The inverted-U variance prediction is not unique to percolation; any binary threshold model predicts maximum variance at intermediate values.
- **H4**: Collagen I and III differ biochemically (integrin binding), not just topologically; biochemical effects may dominate the topological p_c shift.
- **H5**: The BAPN dose-to-p mapping is nonlinear (saturating), potentially making the power-law prediction undetectable.
- **H7**: Most tumors may not be near the critical point, making the universality prediction unmeasurable in practice.
- **H8**: The immunological effects of anti-TGF-beta may dominate any ECM de-correlation effect, making the percolation-specific synergy undetectable.

### Claim-level verification (v5.4 mandatory check):
- All cited papers verified as real: PASS
- Citation hallucinations found: ZERO (this is a strength of the Generator's self-critique)
- Quantitative errors found: 3 (H2: xi at 0.1% discrepancy; H3: sharpness ratio factor-of-4 error; H7: alpha = 0.70 should be 0.53)
- Directional errors: NONE
- Compartmental errors: NONE
- Protein property fabrication: NONE

### Web searches performed:
Every hypothesis was searched for novelty and counter-evidence. A total of 20+ web searches were conducted covering: citation verification (Wang 2013, Zeitz 2017, Saha 2024, Ashworth 2015, Fusilier 2025), novelty verification (percolation + T cell + tumor), counter-evidence (T cell exhaustion motility, biopsy discordance, BAPN dose-response, correlated percolation, active particle self-trapping threshold), and quantitative verification (Fisher exponent tau, walk dimension d_w, fractal dimension d_f).

---

## Summary

- Total hypotheses: 8
- KILL: 1 (H6 -- self-trapping contradicted by data, Pe below threshold)
- ADVANCE: 2 (H4, H8)
- ADVANCE_WITH_CONCERNS: 5 (H1, H2, H3, H5, H7)

---

## Critic Questions (forwarded to Generator for Cycle 2)

### Critical priority (must address):
1. **[H6 KILL]** H6 is killed. Do not regenerate the self-trapping mechanism. If revised, must address: (a) exhausted T cells are MORE motile (You et al. 2021 JCI), (b) Pe ~ 3 is far below self-trapping threshold.
2. **[H7 ERROR]** Correct MSD exponent at p_c: alpha ~ 0.53 for 3D passive percolation, NOT 0.70 (which is 2D value).
3. **[ALL]** Propose a method to independently measure the lattice constant a for collagen networks in tumor tissue.
4. **[ALL]** Address the multiple-barrier problem: what fraction of immune exclusion is ECM topology vs. other mechanisms?

### High priority:
5. **[H1, H5]** How would you measure the dose-to-p mapping (LOX inhibitor dose to effective open pore fraction)?
6. **[H3]** Is the inverted-U variance prediction unique to percolation, or does any spatial heterogeneity model predict it?
7. **[H2]** How to distinguish percolation-driven power-law clusters from branching processes, SOC, or other mechanisms?
8. **[H5]** Can you distinguish P_inf ~ (p - p_c)^0.417 from a Hill equation with n ~ 4?
9. **[H8]** Can you isolate the percolation-specific synergy from immunological synergy?

### Lower priority:
10. **[H4]** Control for biochemical effects of different collagen types when testing p_c shift.
11. **[H1]** Account for LOX inhibition being insufficient for tumor control in 4/5 models.
12. **[H7]** Sample size needed to estimate nu to within +/- 0.05.
