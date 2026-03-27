# Final Hypotheses — Session 2026-03-27-scout-013

Passing hypotheses after Quality Gate (PASS + CONDITIONAL_PASS).
Contains full tagged text ([GROUNDED] / [PARAMETRIC]) for claim-level verification.

---

## C1-H1: GEV Tail Index (xi) as Phylogenomic Signature of Thermal Adaptation Strategy

**QG Verdict**: PASS (composite 8.45)

**Connection**: Extreme value statistics → GEV shape parameter ξ fitted to proteome Tm distributions → Evolutionary thermal adaptation strategy classification

**Mechanism**:

The shape parameter ξ of the Generalized Extreme Value distribution fitted to proteome melting temperature data encodes evolutionary information about how an organism handles thermal vulnerability. The Fisher-Tippett-Gnedenko theorem guarantees that block extremes of the Tm distribution converge to one of exactly three families, classified solely by ξ [GROUNDED: Fisher & Tippett 1928, Proc. Cambridge Phil. Soc. 24, 180-190; Gnedenko 1943, Annals of Mathematics 44, 423-453].

Two distinct evolutionary strategies predict separable ξ signatures. **Strategy 1 — tail truncation** (thermophilic adaptation): organisms that evolved under sustained high temperatures eliminated the most vulnerable proteins through amino acid substitutions that raise the stability floor (increased hydrophobic core packing, salt bridge networks, disulfide bonds). This compresses the lower tail of the Tm distribution, producing more negative ξ (deeper into the Weibull domain) [PARAMETRIC]. **Strategy 2 — distribution shift** (psychrophilic adaptation): organisms adapted to cold shifted the ENTIRE Tm distribution leftward to maintain conformational flexibility at low temperatures, without specifically truncating the vulnerable tail. This produces ξ closer to zero (approaching Gumbel domain) because the relative tail shape is preserved even as the location parameter shifts [PARAMETRIC].

**Falsifiable prediction**: Fit GEV to the proteome Tm distributions of each of the 13 species in the Meltome Atlas (PRIDE PXD011929) [GROUNDED: Jarzab et al. 2020, Nature Methods, PMID 32284610]. Estimate ξ per species using maximum likelihood. Plot ξ against optimal growth temperature (OGT). Prediction: ξ correlates negatively with OGT (thermophiles more negative, psychrophiles less negative). SE(ξ) = 0.016 per species [PARAMETRIC estimate from computational validation], expected thermophile-mesophile ξ difference of 0.3-0.5 [PARAMETRIC].

**Confidence**: 5/10 (revised from 6/10 by Critic)

**Groundedness**: MEDIUM — GEV fitting methodology [GROUNDED: Coles 2001, "An Introduction to Statistical Modeling of Extreme Values," Springer]. Meltome Atlas data [GROUNDED: Jarzab et al. 2020, Nature Methods, 48,000 proteins across 13 species, PMID 32284610]. Thermophile amino acid adaptations [GROUNDED: well-documented in structural biology literature; IVYWREL amino acid set correlates with OGT r=0.93]. The specific ξ-OGT correlation and tail-truncation vs. distribution-shift distinction are [PARAMETRIC].

**Key organisms**: Thermus thermophilus (OGT ~65°C), Homo sapiens (OGT ~37°C), psychrophilic bacteria in Meltome Atlas

---

## C1-H2: Complex-Minimum Tm Return Levels Predict Process-Specific Thermal Failure Temperatures

**QG Verdict**: CONDITIONAL_PASS (composite 8.15)
**Conditions**: (1) Correct TPCA attribution to Tan et al. 2018 (not Mateus 2020 MSB); (2) Quantify chaperone buffering correction

**Connection**: Extreme value statistics → Return level estimation on complex-level thermal bottleneck Tm → Prediction of pathway-specific thermal failure points

**Mechanism (multi-level abstraction)**:

**Molecular level**: Each multi-protein complex has a thermal bottleneck — the subunit with the lowest Tm. TPCA data confirms intra-complex Tm correlation r = 0.75-0.83 and documents 350+ human protein complexes with coordinated melting behavior [GROUNDED: Tan et al. 2018, Science 359:1170-1177, PMID 29439025; Lim et al. 2023, Nature Communications, PMID 38001062]. For each complex, the minimum Tm among essential subunits defines the complex's thermal vulnerability.

**Systemic level**: The process fails when a critical fraction of its complexes lose function. This is a return level problem: the p-return level R_p = μ + (σ/ξ)[(−log(1−p))^{−ξ} − 1] [GROUNDED: standard EVT, Coles 2001, Springer] extrapolates from the observed Tm distribution to predict temperatures that cause arbitrary levels of process degradation.

**Formal/mathematical level**: Return level R_p maps a probability (fraction of complexes failing) to a temperature. Profile likelihood provides confidence intervals on R_p. Mathematically identical to flood return level estimation [GROUNDED: standard practice since Gumbel 1958], but applied to protein complexes.

**Falsifiable prediction**: For human cells: (1) compute minimum Tm per complex for all ribosomal subcomplexes using Meltome Atlas data; (2) fit GEV to this distribution; (3) estimate the 1% return level. Prediction: this temperature matches the experimentally measured temperature at which translation rate drops below 90% of baseline (measurable by puromycin incorporation). Apply same to mitochondrial respiratory chain complexes (10% OCR drop, Seahorse respirometry). Agreement within ±2°C validates; systematic underestimation indicates chaperone buffering. Jarzab 2020 confirms "near-normal respiration at 46°C" [GROUNDED: Jarzab et al. 2020, Nature Methods].

**Confidence**: 5/10 (revised from 7/10 by Critic)

**Groundedness**: MEDIUM-HIGH — Return level estimation [GROUNDED: Coles 2001]. TPCA co-aggregation data [GROUNDED: Tan et al. 2018, Science; Lim et al. 2023, Nature Communications]. Meltome Atlas protein-level Tm [GROUNDED: Jarzab et al. 2020]. The specific ±2°C prediction and puromycin/Seahorse assay mapping are [PARAMETRIC].

**Key chaperones**: HSP70, HSP90 (STRING interaction scores 0.939-0.999) [GROUNDED: STRING database]
**Key complexes**: Ribosomal subcomplexes, mitochondrial respiratory chain complexes (I, III, IV, V)
**Key processes**: Translation (puromycin incorporation assay), oxidative phosphorylation (Seahorse respirometry)

---

## C1-H7: GPD Scale Parameter Predicts Evolutionary Rate in the Thermally Vulnerable Subproteome

**QG Verdict**: CONDITIONAL_PASS (composite 7.00)
**Conditions**: (1) Correct Drummond 2005 citation (PNAS 102:14338, not Cell); (2) Distinguish novel (sigma-dN/dS) from prior art (GO enrichment per Leuenberger 2017); (3) Control for expression level and interaction degree confounders

**Connection**: Extreme value statistics → GPD scale parameter σ of lower-tail Tm exceedances → Evolutionary constraint (dN/dS) on thermally vulnerable proteins

**Mechanism**:

The Generalized Pareto Distribution fitted to lower-tail exceedances (proteins with Tm below a POT threshold) has scale parameter σ quantifying SPREAD of the vulnerable subset. A SMALL σ means all vulnerable proteins have similar Tm — imposing strong purifying selection (any amino acid substitution that lowers Tm risks pushing below the functional threshold). A LARGE σ means vulnerable proteins span a wide Tm range — creating a tolerance gradient where some mutations are permissible [PARAMETRIC].

**Falsifiable prediction**: (1) Fit GPD to lower 5th percentile Tm exceedances for each of 13 Meltome Atlas species. (2) For each species, identify genes encoding GPD exceedance proteins. (3) Compute pairwise dN/dS for orthologous tail-protein genes between species using reciprocal best BLAST + PAML codeml [GROUNDED: Yang 2007, "PAML 4: Phylogenetic Analysis by Maximum Likelihood," Mol. Biol. Evol. 24:1586-1591, PMID 17483113]. (4) Test whether σ negatively correlates with mean dN/dS across species, controlling for proteome size and OGT.

**Prior art note**: GO functional enrichment of thermally unstable proteins (percentile-based) has prior art from Leuenberger et al. 2017, Science, PMID 28232526. The novel contribution is (a) GPD-principled threshold selection and (b) the sigma-dN/dS evolutionary rate correlation.

**Confidence**: 4/10 (revised from 5/10 by Critic)

**Groundedness**: MEDIUM — GPD methodology [GROUNDED: Coles 2001]. dN/dS estimation [GROUNDED: PAML, Yang 2007, MBE PMID 17483113]. Expression-level confounders in evolutionary rate [GROUNDED: Drummond et al. 2005, PNAS 102:14338, PMID 16176987]. The specific σ-dN/dS correlation prediction is [PARAMETRIC].

**Key datasets**: Meltome Atlas PRIDE PXD011929, OrthoFinder/reciprocal BLAST for orthologs, PAML codeml
**Key method**: Mean residual life plot for GPD threshold selection [GROUNDED: Coles 2001]
**Key confounders to control**: expression level (PAX database), protein-protein interaction degree (STRING), essentiality
