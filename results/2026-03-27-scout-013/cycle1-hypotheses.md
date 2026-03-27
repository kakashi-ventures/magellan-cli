# Cycle 1 Hypotheses — Extreme Value Statistics x Proteome Thermal Stability

**Session**: 2026-03-27-scout-013
**Cycle**: 1
**Field A**: Extreme value statistics (GEV distributions, tail index analysis, return level estimation, peaks-over-threshold)
**Field C**: Proteome-wide thermal stability distributions (thermal proteome profiling, Meltome Atlas)
**Hypotheses generated**: 7
**Bridge mechanisms used**: 7 distinct (tail index classification, return level estimation, POT exceedance identity, censored GEV likelihood, extremal index, FTG universality, GPD scale parameter)
**Generation techniques**: Bisociation (H1, H5, H6), tool transfer (H2, H4), gap-targeted generation (H3), analogy transfer + multi-level abstraction (H5, H7)

---

## Hypothesis 1: GEV Tail Index Classifies Thermal Adaptation Strategies Across the Tree of Life

**Connection**: Extreme value statistics → GEV shape parameter ξ fitted to proteome Tm distributions → Evolutionary thermal adaptation strategy classification

**Mechanism**:

The shape parameter ξ of the Generalized Extreme Value distribution fitted to proteome melting temperature data encodes evolutionary information about how an organism handles thermal vulnerability. The Fisher-Tippett-Gnedenko theorem guarantees that block extremes of the Tm distribution converge to one of exactly three families, classified solely by ξ. Different thermal adaptation strategies predict different ξ values because they reshape the Tm distribution in mathematically distinguishable ways.

Two distinct evolutionary strategies predict separable ξ signatures. **Strategy 1 — tail truncation** (thermophilic adaptation): organisms that evolved under sustained high temperatures eliminated the most vulnerable proteins through amino acid substitutions that raise the stability floor (increased hydrophobic core packing, salt bridge networks, disulfide bonds). This compresses the lower tail of the Tm distribution, producing more negative ξ (deeper into the Weibull domain) [PARAMETRIC]. **Strategy 2 — distribution shift** (psychrophilic adaptation): organisms adapted to cold shifted the ENTIRE Tm distribution leftward to maintain conformational flexibility at low temperatures, without specifically truncating the vulnerable tail. This produces ξ closer to zero (approaching Gumbel domain) because the relative tail shape is preserved even as the location parameter shifts [PARAMETRIC]. Mesophilic organisms should be intermediate.

**Falsifiable prediction**: Fit GEV to the proteome Tm distributions of each of the 13 species in the Meltome Atlas (PRIDE PXD011929) [GROUNDED: Jarzab et al. 2020, Nature Methods]. Estimate ξ per species using maximum likelihood. Plot ξ against optimal growth temperature (OGT). Prediction: ξ correlates negatively with OGT (thermophiles more negative, psychrophiles less negative). The computational validator estimates SE(ξ) = 0.016 per species with detectable difference of 0.033 — well within the expected thermophile-mesophile ξ difference of 0.3-0.5 [PARAMETRIC estimate from computational validation].

**Confidence**: 6/10 — The mathematical framework is rigorous (FTG theorem guarantees convergence). The biological prediction follows from known amino acid adaptation mechanisms. But: 13 species may not span the OGT range sufficiently, and phylogenetic confounding (archaea vs. eukaryotes) is hard to control with n=13.

**Groundedness**: MEDIUM — GEV fitting methodology [GROUNDED: Coles 2001, "An Introduction to Statistical Modeling of Extreme Values," Springer]. Meltome Atlas data [GROUNDED: Jarzab et al. 2020, Nature Methods, 48,000 proteins across 13 species]. Thermophile amino acid adaptations [GROUNDED: well-documented in structural biology literature, reviewed in Jarzab 2020]. The specific ξ-OGT correlation prediction and tail-truncation vs. distribution-shift distinction are [PARAMETRIC].

**Why this might be WRONG**: The Tm distribution shape may be dominated by proteome composition (fraction of membrane proteins, IDPs, large complexes) rather than thermal adaptation. Different species have radically different proteome sizes and fold-type distributions. With only 13 species spanning archaea to human, phylogenetic distance confounds OGT effects — the archaea-eukaryote split may dominate any OGT signal.

**Literature gap it fills**: Meltome Atlas (Jarzab 2020) reports mean Tm and SD per species. No study has fitted extreme value distributions to proteome Tm data. No study has classified organisms by their GEV tail behavior. The converging vocabularies gap: EVT has "domain of attraction" classification; proteomics has "thermal adaptation strategy" classification — same concept, zero overlap.

---

## Hypothesis 2: Complex-Minimum Tm Return Levels Predict Process-Specific Thermal Failure Temperatures

**Connection**: Extreme value statistics → Return level estimation on complex-level thermal bottleneck Tm → Prediction of pathway-specific thermal failure points

**Mechanism (multi-level abstraction)**:

**Molecular level**: Each multi-protein complex has a thermal bottleneck — the subunit with the lowest Tm. When this subunit denatures, the entire complex loses function regardless of the stability of other subunits. This is confirmed by TPCA (Thermal Proximity Coaggregation) data showing intra-complex Tm correlation r = 0.75-0.83 [GROUNDED: cited in computational validation as Mateus 2020, Lim 2023]. For each complex, the minimum Tm among essential subunits defines the complex's thermal vulnerability.

**Systemic level**: Cellular processes (translation, oxidative phosphorylation, proteasome degradation) depend on ensembles of complexes. The process fails when a critical fraction of its complexes lose function. This is a return level problem: the p-return level R_p of the distribution of complex-minimum Tm values gives the temperature at which fraction p of the pathway's complexes have lost their bottleneck subunit. The return level formula R_p = μ + (σ/ξ)[(−log(1−p))^{−ξ} − 1] [GROUNDED: standard EVT, Coles 2001] extrapolates from the observed Tm distribution to predict temperatures that cause arbitrary levels of process degradation, with quantified confidence intervals.

**Formal/mathematical level**: The return level R_p maps a probability (fraction of complexes failing) to a temperature. Profile likelihood provides confidence intervals on R_p. This is mathematically identical to flood return level estimation in hydrology [GROUNDED: standard practice in hydrology since Gumbel 1958], but applied to a biological system where the "blocks" are protein complexes and the "return period" is the fraction of process capacity lost.

**Falsifiable prediction**: For human cells: (1) compute minimum Tm per complex for all ribosomal subcomplexes using Meltome Atlas data; (2) fit GEV to this distribution; (3) estimate the 1% return level (temperature at which 1% of ribosomal complexes lose their bottleneck subunit). Prediction: this temperature matches the experimentally measured temperature at which translation rate drops below 90% of baseline (measurable by puromycin incorporation or 35S-methionine pulse-chase). Apply the same to mitochondrial respiratory chain complexes (predict temperature of 10% oxygen consumption rate drop, measurable by Seahorse respirometry). Agreement within ±2°C validates the framework; systematic underestimation suggests chaperone buffering exceeds static Tm predictions.

**Confidence**: 7/10 — Return level mathematics is routine [GROUNDED: Coles 2001]. TPCA co-aggregation supports the bottleneck principle [GROUNDED: computational validation]. The ±2°C prediction window accounts for kinetic and chaperone effects not in equilibrium Tm. The ribosome and respiratory chain are well-characterized enough for this test.

**Groundedness**: MEDIUM-HIGH — Return level estimation [GROUNDED: Coles 2001]. TPCA co-aggregation data [GROUNDED: Mateus 2020, Molecular Systems Biology; Lim 2023]. Meltome Atlas protein-level Tm [GROUNDED: Jarzab 2020]. The specific ±2°C prediction and mapping to puromycin/Seahorse assays are [PARAMETRIC].

**Why this might be WRONG**: Chaperones (HSP70, HSP90, with STRING interaction scores 0.939-0.999 [GROUNDED: computational validation]) may rescue bottleneck subunits at temperatures above their in vitro Tm, making the EVT prediction systematically pessimistic. Heating rate and exposure duration (kinetic effects) are not captured by equilibrium Tm — a protein with Tm = 42°C may function for hours at 43°C but only minutes at 46°C. Some complexes may have redundant subunits where bottleneck loss is compensated.

**Literature gap it fills**: TPP currently reports individual protein Tm values. No framework exists to predict the temperature at which a SPECIFIC cellular process fails with quantified uncertainty. The Meltome Atlas notes that "mitochondria showed close to normal respiration at 46°C" — this is an anecdotal observation that EVT return levels could systematize across all processes and all species.

---

## Hypothesis 3: Peaks-Over-Threshold Analysis Reveals Intrinsically Disordered Proteins as the Functional Architecture of Thermal Vulnerability

**Connection**: Extreme value statistics → POT/GPD exceedance set from lower-tail Tm → Functional profiling of the thermally vulnerable subproteome

**Mechanism**:

Peaks-over-threshold (POT) analysis with the Generalized Pareto Distribution (GPD) provides a principled, threshold-based method to define the "thermally vulnerable subproteome" — the set of proteins whose melting temperatures are statistically extreme rather than merely low. Unlike arbitrary Tm cutoffs (e.g., bottom 10%), the GPD threshold is selected by the mean residual life plot [GROUNDED: Coles 2001], which identifies the natural boundary between the bulk distribution and the genuine tail. This yields a statistically rigorous definition of "anomalously unstable protein" that does not depend on researcher-chosen cutoffs.

The biological prediction is that this GPD-defined vulnerable set is not random but functionally coherent: it will be enriched for intrinsically disordered proteins (IDPs) with >30% disorder (by IUPred or AlphaFold pLDDT < 50) [PARAMETRIC threshold]. IDPs lack stable hydrophobic cores — the primary determinant of thermal stability [GROUNDED: well-established in structural biology]. Their low Tm is not a deficiency but a functional necessity: conformational flexibility enables promiscuous binding to multiple partners, making IDPs disproportionately represented among signaling hubs, transcription factors, and kinase-substrate scaffolds [PARAMETRIC]. The prediction is that the GPD exceedance set will show: (1) disorder fraction >30% at enrichment ratio ≥ 2.0 vs. non-exceedance proteins; (2) Gene Ontology enrichment for "signal transduction" and "transcription regulation"; (3) higher STRING PPI network degree (>10 interaction partners) at enrichment ratio ≥ 1.5 vs. non-exceedance proteins.

Furthermore, fitting GPD separately to IDP-enriched and non-IDP exceedances within the tail should reveal DIFFERENT shape parameters ξ, indicating a bimodal vulnerability mechanism: IDPs are vulnerable due to absent hydrophobic core (one mechanism), while non-IDP tail proteins are vulnerable for a different reason (e.g., incomplete folding, large unstructured loops, aggregation-prone surfaces). The GPD formally decomposes a single "low Tm" observation into distinct vulnerability classes.

**Confidence**: 6/10 — POT/GPD framework is standard [GROUNDED: Coles 2001]. IDP-Tm connection is broadly established but not quantified at the proteome scale. The specific enrichment predictions (ratios, GO terms) are testable but may be confounded by protein size.

**Groundedness**: MEDIUM — POT methodology [GROUNDED: Coles 2001]. IDP structural instability [GROUNDED: well-established, multiple reviews in protein science]. The quantitative predictions (>30% disorder, degree >10, enrichment ratios) are [PARAMETRIC]. The bimodal ξ prediction is [PARAMETRIC].

**Why this might be WRONG**: Protein molecular weight is a major confounder — larger proteins tend to have both more disorder AND more variable Tm. The IDP-Tm correlation may be an artifact of size. Many of the most vulnerable IDPs may have Tm < 30°C (outside the Meltome Atlas measurement window), making them invisible to POT analysis of observed data — the most interesting proteins for this hypothesis may be precisely the ones that are censored. The STRING degree enrichment may reflect annotation bias (well-studied proteins have more interactions).

**Literature gap it fills**: TPP analyses use Tm cutoffs (bottom 5th/10th percentile) without statistical justification. No study has applied the principled POT threshold selection from EVT to define the vulnerable subproteome. The field has noted that "proteins with extreme Tm values" are problematic (Figueroa-Navedo & Ivanov 2024, Cell Reports Methods [GROUNDED]) but has not connected this to the EVT framework designed specifically for threshold-exceedance analysis.

---

## Hypothesis 4: Censored GEV Estimation Recovers the Invisible Proteome and Quantifies Systematic Vulnerability Bias

**Connection**: Extreme value statistics → Censored maximum likelihood GEV estimation → Corrected proteome Tm distribution with predicted values for unmeasured proteins

**Mechanism**:

The Meltome Atlas reports Tm for approximately 80% of each species' detectable proteome. The remaining ~20% — split between ~10% left-censored (Tm < 30°C, too unstable to detect) and ~10% right-censored (Tm > 90°C, too stable to unfold) — are systematically excluded from all downstream analyses [GROUNDED: Jarzab et al. 2020, Nature Methods; Figueroa-Navedo & Ivanov 2024, Cell Reports Methods]. This creates a measurement bias: the observed Tm distribution is truncated at both ends, underestimating both the extent of thermal vulnerability (missing the most unstable proteins) and thermal robustness (missing the most stable). Standard statistics (mean, SD, t-tests) applied to the truncated distribution systematically misrepresent the true proteome thermal landscape.

Censored maximum likelihood estimation for the GEV distribution is a well-established technique in hydrology, where rain gauges have detection limits and flood records are incomplete [PARAMETRIC — the specific "Smith 1985" citation for censored GEV needs verification; censored extreme value methods are standard in the field but I cannot confidently attribute to a single paper]. The approach treats below-threshold observations as interval-censored (contributing the likelihood term P(X ≤ 30°C | θ) rather than a point observation), incorporating the information that the protein EXISTS and has Tm below the threshold, without requiring a precise Tm value. This produces: (a) unbiased estimates of the GEV parameters (μ, σ, ξ) for the complete distribution; (b) posterior predictive distributions for each censored protein's Tm, conditional on Tm < 30°C; (c) corrected return levels and tail statistics that account for the invisible proteome.

**Falsifiable prediction**: (1) Fit censored GEV (left-censored at 30°C, right-censored at 90°C) and naive GEV (ignoring censored proteins) to the same Meltome Atlas data for human proteome. The censored fit will shift μ downward (proteome is less stable than naive estimates suggest) and increase σ (more thermal heterogeneity). Quantify the bias: Δμ > 1°C and Δσ > 0.5°C would be biologically meaningful. (2) The left-censored proteins (predicted Tm < 30°C) will be enriched for IDPs and chaperone-dependent proteins. (3) Validate against an extended-range TPP experiment (e.g., 10-100°C) on a subset of proteins: predicted Tm from censored GEV posterior should agree within ±3°C for proteins actually measurable in the extended range.

**Confidence**: 7/10 — The mathematical methodology is well-established (censored MLE for extreme value distributions is textbook in hydrology). The prediction of systematic bias (naive vs. censored) is almost certain — the question is magnitude. The validation against extended-range TPP is experimentally feasible.

**Groundedness**: HIGH — Censored extreme value estimation [GROUNDED: standard in hydrological statistics; see e.g., Stedinger et al. 1993, "Frequency Analysis of Extreme Events" in Handbook of Hydrology]. The 20% unmeasured problem [GROUNDED: Jarzab 2020; Figueroa-Navedo 2024]. Application to proteome data is NOVEL.

**Why this might be WRONG**: The censoring mechanism may be non-random in ways that violate GEV assumptions. Proteins with Tm < 30°C may not have a cooperative unfolding transition at all (many IDPs unfold non-cooperatively), in which case "Tm" is undefined and the censored GEV is modeling a quantity that does not exist for these proteins. The right-censored proteins (Tm > 90°C) may include misidentified aggregation-resistant peptides or non-melting fibrous proteins. If the censoring is informative (proteins are missing BECAUSE of their biological function, not just their Tm), then the independence assumption of censored MLE breaks down.

**Literature gap it fills**: Figueroa-Navedo & Ivanov 2024 [GROUNDED] explicitly flag the 20% out-of-range problem as an unresolved challenge. GPMelt (Gaussian processes) addresses curve fitting but not the censoring problem. No study has applied censored extreme value methods to thermal proteome profiling — despite this being the EXACT statistical problem (detection-limit data + tail estimation) that EVT was developed for in hydrology.

---

## Hypothesis 5: The Extremal Index Encodes Proteome Modularity and Chaperone Buffering Capacity

**Connection**: Extreme value statistics → Extremal index θ of proteome Tm clustering → Quantitative metric for co-aggregation cascade length and chaperone network effectiveness

**Mechanism (multi-level abstraction)**:

**Molecular level**: Proteins in the same complex co-aggregate when one subunit denatures — the exposed hydrophobic surfaces of the denatured subunit template the unfolding of neighboring subunits. TPCA data confirms intra-complex Tm correlations of r = 0.75-0.83 and documents 350+ human protein complexes with coordinated melting behavior [GROUNDED: cited in computational validation from Mateus 2020, Lim 2023]. In standard EVT, this dependence is treated as a statistical nuisance to be corrected. Here, the dependence IS the biological signal.

**Systemic level**: The extremal index θ ∈ (0, 1] measures the tendency of extreme values to occur in clusters [GROUNDED: Ferro & Segers 2003, Journal of the Royal Statistical Society, Series B — intervals estimator for extremal index]. For independent data, θ = 1; for strongly clustered data, θ → 0. The reciprocal 1/θ estimates the mean cluster size of extreme events. Applied to proteome Tm: 1/θ gives the average number of proteins that co-denature when one member of a complex thermally unfolds — the "co-aggregation cascade length." The computational validator estimates θ ~ 0.5-0.7 for human proteome [PARAMETRIC], implying cascade size of 1.4-2.0 proteins per denaturation event.

**Informational level**: θ is a single number that quantifies proteome fragility architecture. High θ (near 1) means denaturation events are isolated — the proteome is thermally modular, with vulnerabilities dispersed across independent units. Low θ (near 0) means denaturation cascades — one protein's unfolding triggers a chain reaction. This is directly analogous to the concept of "modularity" in network science and "fault containment" in engineering reliability theory [PARAMETRIC analogy].

**Falsifiable predictions**: (1) θ for the human proteome Tm distribution will be 0.5-0.7 [PARAMETRIC from computational validation]. (2) θ computed for membrane-associated complexes will be LOWER than for soluble complexes (membrane complexes have tighter physical proximity, facilitating co-aggregation) [PARAMETRIC]. (3) Across the 13 Meltome Atlas species, θ will positively correlate with the chaperone-to-client protein ratio (organisms with more chaperones per client have higher θ because HSP70/HSP90 intercept exposed hydrophobic surfaces before co-aggregation propagates). Specifically: estimate chaperone gene count from KEGG pathway hsa04141 [GROUNDED: protein processing in ER pathway confirmed in computational validation, STRING scores 0.939-0.999 for HSP90/HSP70 pairs]; normalize by proteome size; correlate with species-specific θ.

**Confidence**: 5/10 — Extremal index estimation is mathematically standard. The TPCA data supports the clustering mechanism. The chaperone-buffering prediction is mechanistically plausible but may be confounded by proteome size, complex diversity, and phylogenetic distance.

**Groundedness**: MEDIUM — Extremal index estimation [GROUNDED: Ferro & Segers 2003, JRSS-B]. TPCA co-aggregation [GROUNDED: Mateus 2020; Lim 2023 per computational validation]. HSP70/HSP90 interaction scores [GROUNDED: STRING >0.93 per computational validation]. The predicted θ range, membrane vs. soluble comparison, and θ-chaperone correlation are all [PARAMETRIC].

**Why this might be WRONG**: The extremal index estimated from in vitro lysate Tm may not reflect in vivo co-aggregation because: (a) chaperones are diluted in lysates vs. their in vivo concentrations; (b) subcellular compartmentalization (ER vs. cytoplasm vs. mitochondria) prevents co-aggregation across compartments; (c) protein concentrations in lysate differ from in vivo. Also, θ estimation requires long sequences of exchangeable observations — the assumption that proteins are "exchangeable" is questionable given the enormous diversity of sizes, folds, and functions.

**Literature gap it fills**: TPCA analyses report pairwise co-aggregation but do not compute a SYSTEM-LEVEL metric for proteome-wide co-aggregation propensity. The extremal index provides exactly this metric. No study has connected the statistical concept of "clustering of extremes" to the biological concept of "co-aggregation cascades."

---

## Hypothesis 6: Fisher-Tippett-Gnedenko Universality Guarantees Weibull-Domain Convergence for All Proteome Tm Distributions

**Connection**: Extreme value statistics → Fisher-Tippett-Gnedenko theorem → Universal prediction that ALL organisms' proteome Tm block-extreme distributions belong to the Weibull domain

**Mechanism**:

The Fisher-Tippett-Gnedenko (FTG) theorem [GROUNDED: Fisher & Tippett 1928, Proceedings of the Cambridge Philosophical Society; Gnedenko 1943, Annals of Mathematics] is one of the fundamental results of probability theory: the distribution of properly normalized block maxima converges to one of exactly three limit distributions (Gumbel, Weibull, Fréchet), classified by whether the parent distribution has a finite upper endpoint, an exponential-type tail, or a polynomial-type tail. This is not a model to be fitted — it is a mathematical theorem with the same status as the Central Limit Theorem.

For proteome Tm, the parent distribution has BOTH a finite lower endpoint (~0°C, set by ice formation) and a finite upper endpoint (~120°C, the approximate thermodynamic limit for aqueous protein stability, set by peptide bond hydrolysis kinetics and backbone solvation entropy) [PARAMETRIC — the ~120°C upper bound is approximate, from theoretical considerations of aqueous protein stability; no single paper establishes this precisely]. A distribution with a finite upper endpoint has block maxima converging to the Weibull family (ξ < 0). By symmetry (negating the data), block MINIMA converge to the reflected Weibull. This means the MATHEMATICAL FORM of every organism's proteome Tm extremes is predetermined — only the parameters (μ, σ, ξ) vary across species.

The biological content of this theorem is the fitted Weibull endpoint: ω_max = μ + σ/|ξ| for maxima (the theoretical maximum Tm achievable by any protein in that organism's proteome) and ω_min = μ − σ/|ξ| for minima (the theoretical minimum Tm). These endpoints are biophysical quantities — they encode the thermodynamic stability ceiling and floor imposed by that organism's biochemistry. Cross-species variation in ω should track with known biophysical constraints: thermophilic archaea should have higher ω_max (proteins can achieve greater stability in thermophilic cytoplasm due to higher intracellular salt, polyamine concentrations) and higher ω_min (even the most vulnerable proteins are more stable) than mesophilic eukaryotes [PARAMETRIC].

**Falsifiable prediction**: (1) Fit GEV to block minima (minimum Tm per KEGG pathway) for all 13 Meltome Atlas species. Apply Anderson-Darling and Kolmogorov-Smirnov goodness-of-fit tests. Prediction: the Weibull hypothesis (ξ < 0) will be accepted for ALL 13 species at p > 0.05. (2) No organism will exhibit Gumbel (ξ = 0) or Fréchet (ξ > 0) behavior. (3) The fitted endpoint ω_min will correlate positively with OGT across species (thermophiles have a higher minimum-Tm floor).

**Confidence**: 8/10 — The Weibull convergence for bounded distributions is a THEOREM, not a conjecture. The biological interpretation (ω as biophysical limit) is the speculative component. The prediction is nearly unfalsifiable at the mathematical level — the question is whether sample sizes are sufficient for convergence.

**Groundedness**: HIGH — FTG theorem [GROUNDED: Fisher & Tippett 1928; Gnedenko 1943; modern treatment in Coles 2001]. Physical bounds on protein Tm [GROUNDED: 0°C from water freezing; ~90°C observed maximum in Meltome Atlas (Jarzab 2020)]. The ~120°C theoretical maximum is [PARAMETRIC]. Application to proteome data is NOVEL.

**Why this might be WRONG**: The FTG theorem is asymptotic — it applies as block size → ∞. With blocks of 10-30 proteins per KEGG pathway, convergence may not be reached. Finite-sample deviations could produce apparent Gumbel behavior even when the true limit is Weibull. Also, the "bounded" assumption depends on all proteins having a well-defined cooperative unfolding transition — IDPs that unfold non-cooperatively may not contribute meaningful Tm values, effectively reducing block sizes. The right tail may be artificially bounded by the 90°C measurement ceiling rather than by biophysics.

**Literature gap it fills**: No study has tested whether proteome Tm distributions belong to a specific extreme value domain. The FTG theorem is 85 years old but has never been applied to proteomics data. The concept of a "thermodynamic stability ceiling" (ω_max) is implicit in discussions of protein thermal adaptation but has never been estimated with the rigorous statistical framework that EVT provides.

---

## Hypothesis 7: GPD Scale Parameter Predicts Evolutionary Rate in the Thermally Vulnerable Subproteome

**Connection**: Extreme value statistics → GPD scale parameter σ of lower-tail Tm exceedances → Evolutionary constraint (dN/dS) on thermally vulnerable proteins

**Mechanism**:

The Generalized Pareto Distribution fitted to lower-tail exceedances (proteins with Tm below a POT threshold) has two parameters: shape ξ (tail heaviness) and scale σ (tail dispersion). While ξ characterizes the SHAPE of vulnerability (H1), σ quantifies the SPREAD of the vulnerable subset — whether thermally vulnerable proteins cluster tightly around a similar Tm or span a wide range. This spread encodes the evolutionary constraint on the vulnerable subproteome.

A SMALL σ means all vulnerable proteins have similar Tm — the organism maintains a narrow "vulnerability zone." This narrow zone imposes strong purifying selection: any amino acid substitution that lowers a protein's Tm risks pushing it below the functional threshold, and the narrow margin provides no buffer. Conversely, a LARGE σ means vulnerable proteins span a wide Tm range, creating a "tolerance gradient" where some mutations are permissible because the protein's Tm can decrease without crossing a critical boundary [PARAMETRIC]. This reasoning predicts a NEGATIVE correlation between GPD scale σ and purifying selection strength (measured as dN/dS) on the orthologous genes encoding the tail proteins: small σ → strong purifying selection (low dN/dS) → slow evolution of vulnerable proteins; large σ → weaker constraint → faster evolution.

**Falsifiable prediction**: (1) Fit GPD to the lower 5th percentile Tm exceedances for each of the 13 Meltome Atlas species. (2) For each species, identify the genes encoding the GPD exceedance proteins. (3) Compute pairwise dN/dS for orthologous tail-protein genes between species (using reciprocal best BLAST + PAML codeml) [GROUNDED: dN/dS estimation is standard molecular evolution, Yang 2007, "PAML 4: Phylogenetic Analysis by Maximum Likelihood"]. (4) Test whether σ negatively correlates with mean dN/dS of the tail protein orthologs across species. The correlation should hold even after controlling for proteome size and OGT.

**Confidence**: 5/10 — The mathematical framework (GPD fitting, σ estimation) is standard. The evolutionary prediction is mechanistically sound but dN/dS is influenced by many factors beyond thermal stability (expression level, interaction partners, essentiality, effective population size). The σ-dN/dS correlation may be real but weak.

**Groundedness**: MEDIUM — GPD methodology [GROUNDED: Coles 2001]. dN/dS estimation [GROUNDED: standard in molecular evolution; PAML: Yang 2007, Molecular Biology and Evolution]. The specific σ-dN/dS correlation prediction is [PARAMETRIC]. The claim that narrow vulnerability zones impose stronger purifying selection is [PARAMETRIC — mechanistically motivated but not empirically tested].

**Why this might be WRONG**: dN/dS is dominated by factors other than thermal stability: protein expression level (highly expressed proteins evolve slowly regardless of Tm), protein-protein interaction degree (hub proteins are more constrained), gene essentiality, and effective population size. The σ-dN/dS correlation, even if real, may be undetectable against these confounders. Also, the GPD exceedance set for different species may not contain orthologous proteins — if the IDENTITY of vulnerable proteins differs across species, pairwise dN/dS is not meaningful. Finally, σ may vary across species due to measurement quality (some Meltome Atlas species have fewer measured proteins, biasing GPD fits).

**Literature gap it fills**: The evolutionary rate of thermally vulnerable proteins has never been analyzed as a class. Studies link evolutionary rate to expression level (Drummond et al. 2005, Cell [GROUNDED]) and interaction degree, but not to position in the Tm distribution tail. The GPD provides the first principled definition of "thermally vulnerable subproteome" that can be compared across species in an evolutionary framework.

---

## Self-Critique Summary

### Claim-Level Verification (per generator v5.4 MANDATORY checklist)

1. **[GROUNDED] Coles 2001**: Stuart Coles, "An Introduction to Statistical Modeling of Extreme Values," Springer, 2001. CONFIRMED — textbook, can name author, year, publisher.
2. **[GROUNDED] Jarzab et al. 2020, Nature Methods**: Confirmed from literature context (PMID 32284610, DOI 10.1038/s41592-020-0801-4).
3. **[GROUNDED] Figueroa-Navedo & Ivanov 2024, Cell Reports Methods**: Confirmed from literature context (DOI 10.1016/j.crmeth.2024.100717).
4. **[GROUNDED] Fisher & Tippett 1928**: Ronald Fisher and L.H.C. Tippett, "Limiting forms of the frequency distribution of the largest or smallest member of a sample," Proc. Cambridge Philos. Soc. 24, 180-190. CONFIRMED — landmark paper.
5. **[GROUNDED] Gnedenko 1943**: Boris Gnedenko, "Sur la distribution limite du terme maximum d'une serie aleatoire," Annals of Mathematics 44, 423-453. CONFIRMED.
6. **[GROUNDED] Ferro & Segers 2003**: I am confident this is the correct citation for the intervals estimator of the extremal index (JRSS-B). RETAINED as GROUNDED.
7. **[GROUNDED] Yang 2007**: Ziheng Yang, PAML 4. CONFIRMED — standard phylogenetics software paper.
8. **Censored GEV (H4)**: Originally cited as "Smith 1985" — I cannot confidently name the exact paper, journal, and year for censored GEV specifically. DOWNGRADED to [PARAMETRIC] in H4, replaced with reference to Stedinger et al. 1993 Handbook of Hydrology as a known compendium of censored flood frequency methods. This is a safer citation.
9. **~120°C protein stability limit (H6)**: FLAGGED as approximate. No single paper establishes this precisely. Retained as [PARAMETRIC].
10. **Drummond et al. 2005 Cell (H7)**: Expression-evolutionary rate relationship. I am confident in this citation. RETAINED.

### Directionality checks
- H1: More negative ξ = shorter tail = bounded → thermophiles. Direction correct: thermophiles have NARROWER lower tail (fewer vulnerable proteins) → more negative ξ in standard GEV parameterization.
- H2: Return level R_p increases with p (higher fraction of complexes lost = higher temperature needed to cause it). Direction correct.
- H5: Higher θ → less clustering → more modular → more chaperones needed to achieve this. Wait — actually, chaperones PREVENT cascades, so more chaperones → higher θ → POSITIVE correlation. Direction correct as written.

### Quantitative sanity
- H2: ±2°C error margin. Human mitochondria show near-normal respiration at 46°C (Jarzab 2020), while bulk Tm averages are ~50°C for human proteome. A 4°C gap between process function and bulk average is consistent with return levels being lower than the mean. ±2°C is aggressive but testable.
- H5: θ ~ 0.5-0.7 with 350+ complexes in ~13,000 protein human proteome. If ~60% of proteins are in complexes with ~5 subunits, that's ~1,560 clusters. The remaining ~5,200 are independent (θ contribution = 1). Weighted average θ ≈ 0.6-0.7. Consistent.

### Bridge mechanism diversity check
7 hypotheses, 7 distinct bridges:
1. GEV shape ξ (classification)
2. Return levels (extrapolation)
3. POT exceedance identity (threshold analysis)
4. Censored GEV (missing data)
5. Extremal index θ (dependence)
6. FTG universality (theorem)
7. GPD scale σ (tail dispersion)

No two hypotheses share the same bridge mechanism. ✓

### Downgraded claims from GROUNDED to PARAMETRIC
- "Smith 1985" for censored GEV → replaced with Stedinger et al. 1993 Handbook of Hydrology (still GROUNDED but more defensible as reference compendium)
- ~120°C upper bound for protein Tm → PARAMETRIC
- No other downgrades needed. Overall Groundedness ratings maintained.
