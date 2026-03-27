# Critique — Cycle 1
## Session: 2026-03-27-scout-013
## Target: Extreme Value Statistics x Proteome-wide Thermal Stability Distributions
## Critic: Opus 4.6
## Date: 2026-03-27

---

## Summary

| ID | Title | Verdict | Revised Confidence | Key Attack |
|----|-------|---------|-------------------|------------|
| H1 | GEV Tail Index as Phylogenomic Signature | SURVIVES | 5/10 | Unknown effect size; few thermophile species |
| H2 | Complex-Minimum Tm Identifies Bottleneck Complexes | WOUNDED | 5/10 | TPCA citation error (Tan 2018, not Mateus 2020); CORUM mammalian-only |
| H3 | Censored GEV Recovers Invisible 20% | WOUNDED | 4/10 | IDP multimodality violates GEV assumptions; accuracy claim overoptimistic |
| H4 | Non-Stationary GEV with Drug Covariate | KILLED | 2/10 | Fatally under-powered: 3-5 concentrations insufficient for covariate GEV estimation |
| H5 | Pathway-Level Block Maxima: Translation Initiation Bottleneck | WOUNDED | 4/10 | eIF4F already identified as thermo-sensing node (Mol Cell 2024); Leuenberger 2017 pre-existing |
| H6 | Extremal Index Quantifies Thermal Cooperativity | KILLED | 1/10 | Fundamental methodological error: extremal index requires time series, not cross-sectional data |
| H7 | POT Functional Enrichment: Thermal Disposability | WOUNDED | 4/10 | Partially scooped by Leuenberger 2017 GO enrichment; CDK2 Tm claim incorrect |

**Kill rate: 2/7 = 29%**

---

## H1: GEV Tail Index (xi) as a Phylogenomic Signature of Thermal Adaptation Strategy

### VERDICT: SURVIVES
### Revised Confidence: 5/10 (down from 6)

### ATTACKS:

**1. Novelty Kill**
- Search: "extreme value theory GEV proteome thermal stability Tm distribution" -- Zero relevant results. Confirmed NOVEL.
- Search: "GEV tail index thermal adaptation thermophile mesophile proteome" -- Results on amino acid composition-based thermal adaptation but zero on GEV/EVT approaches. Confirmed NOVEL.
- No published work applies GEV shape parameter analysis to proteome Tm distributions. BLAST/Karlin-Altschul uses Gumbel for alignment scores, which is entirely distinct. Novelty holds.

**2. Mechanism Kill**
- The FTG theorem does guarantee convergence of block maxima/minima to GEV for distributions satisfying regularity conditions. For bounded distributions (Tm has a finite lower endpoint), the Weibull domain (xi < 0) is expected. PLAUSIBLE.
- CONCERN: Using KEGG pathways as "blocks" for block maxima is statistically questionable. Block maxima analysis requires blocks of roughly equal size from a random process. KEGG pathways range from <10 to >500 genes. Unequal block sizes introduce bias into GEV parameter estimation. The hypothesis should use random partitions of fixed size (e.g., 50 proteins per block) rather than functionally-defined pathways.
- CONCERN: The SE(xi) ~ 0.016 estimate is credible for ~3,700 proteins, but the BIOLOGICAL effect size (how much xi differs between thermophiles and psychrophiles) is entirely unknown. If xi differences are <0.05, they may be within estimation noise even with perfect block structure.

**3. Logic Kill**
- The logic chain is sound: if thermal adaptation involves tail sculpting rather than just mean shifting, xi should differ across species. No fallacy detected.
- Minor: the hypothesis assumes xi variation is caused by thermal adaptation. Alternative explanation: xi differences could reflect proteome size, composition, or phylogenetic distance rather than thermal adaptation specifically. The xi-OGT regression could be confounded by other species-level variables.

**4. Falsifiability Kill**
- PASSES. The prediction (xi_thermophile < xi_mesophile < xi_psychrophile) is quantitatively testable with existing Meltome Atlas data. GEV fitting is computationally straightforward. The non-linear xi-OGT prediction is also falsifiable.

**5. Triviality Kill**
- Not trivial. EVT specialists do not think about proteome data; proteomics researchers do not use GEV shape parameters. The connection requires genuine cross-disciplinary insight.

**6. Counter-Evidence Search**
- Search: "thermal death protein denaturation first to fail bottleneck organism heat tolerance proteome" -- Found Leuenberger et al. 2017 (Science), which showed that thermal cellular collapse is caused by loss of a subset of key proteins (the "first to fail" phenomenon). This is ADJACENT but does not use EVT framework or GEV tail analysis. Leuenberger used a different approach (limited proteolysis + MS) and did not characterize the tail shape statistically.
- No direct counter-evidence against GEV tail index comparison across species.

**7. Groundedness Attack**
- Meltome Atlas (Jarzab 2020): GROUNDED, VERIFIED via web search.
- FTG theorem, GEV fitting: GROUNDED in mathematical literature.
- 13 species spanning archaea to humans: VERIFIED. Species list includes Oleispira antarctica (psychrophile, ~4C), Thermus thermophilus and Pyrococcus torridus (thermophiles). But only 2-3 thermophiles out of 13 -- limited statistical power for OGT regression.
- SE(xi) ~ 0.016: PLAUSIBLE (sqrt(1/n) approximation).
- "25 block minima for stable estimation" (attributed to Coles 2001): Correctly tagged PARAMETRIC. Common heuristic but not a formal threshold.
- xi prediction (xi_thermophile < xi_mesophile < xi_psychrophile): PARAMETRIC. Reasonable but untested.
- Grounded/Verifiable: ~65%. ACCEPTABLE.

**8. Hallucination-as-Novelty Check**
- Both components (GEV shape parameter estimation and Meltome Atlas Tm distributions) exist independently and are verified. The novelty is in the connection, not in fabricated components. Low hallucination risk.

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab et al. 2020, Nature Methods -- VERIFIED. 48,000 proteins, 13 species, Tm 30-90C.
- [GROUNDED] "Current literature characterizes thermal adaptation exclusively by shifts in mean Tm" -- VERIFIED. The thermal adaptation literature focuses on amino acid composition and mean Tm; no EVT tail analysis exists.
- [PARAMETRIC] Coles 2001 "25 block minimum" -- Correctly tagged PARAMETRIC. No specific page or threshold verifiable.
- [PARAMETRIC] xi-OGT non-linear relationship -- PURE PREDICTION, correctly tagged.

**SURVIVAL NOTE**: This is the strongest hypothesis in the set. The mathematical framework is sound, the data exists, the prediction is specific and testable, and no prior work connects GEV tail analysis to proteome Tm distributions. The main vulnerability is that xi differences between species may be too small to detect, and the OGT regression has very few data points (13 species, only 2-3 at extreme temperatures). Downgraded from 6 to 5 because of the unknown effect size and the potential confounding of xi by proteome composition rather than thermal adaptation per se.

---

## H2: Complex-Minimum Tm Identifies Thermal Bottleneck Complexes Invisible to Mean-Tm Analysis

### VERDICT: WOUNDED
### Revised Confidence: 5/10 (down from 7)

### ATTACKS:

**1. Novelty Kill**
- Search: "peaks over threshold GPD protein thermal stability proteomics" -- Zero relevant EVT results. The GPMelt paper (Gaussian process) appeared but is entirely distinct from POT/GPD. NOVEL.
- The concept of "weakest subunit determines complex vulnerability" is implicit in the structural reliability literature but has never been formalized using EVT return levels for protein complexes. Novelty holds.

**2. Mechanism Kill**
- The POT/GPD approach to complex-minimum Tm is statistically sound in principle. Fitting GPD to exceedances below a threshold is well-established methodology.
- CONCERN: The "independence restoration" argument is the strongest part of this hypothesis. Taking min-Tm per complex does reduce within-complex correlation. However, complexes sharing subunits (multi-complex proteins) reintroduce dependence. Need to verify how many proteins belong to multiple complexes.
- CONCERN: CORUM is mammalian-only (human 64%, mouse 16%, rat 12%). For the 13 Meltome Atlas species, CORUM covers only human and mouse well. For E. coli, S. cerevisiae, T. thermophilus, etc., CORUM provides NO annotations. The cross-species analysis claimed in the hypothesis is severely limited by annotation coverage. This is a significant practical limitation not adequately acknowledged.

**3. Logic Kill**
- The "minimum Tm subunit = bottleneck" logic assumes all subunits in a complex are essential and that the lowest-Tm subunit is the first to denature in vivo. The hypothesis itself acknowledges this may be wrong for dispensable subunits or cooperatively stabilized complexes. No hard logical fallacy, but the assumption is strong.

**4. Falsifiability Kill**
- PASSES. The prediction that specific complexes (spliceosome, proteasome regulatory, ribosome assembly) appear as POT exceedances across species is testable -- but only for species with complex annotations (human, mouse).

**5. Triviality Kill**
- Not trivial. The connection between EVT return levels and complex thermal vulnerability is genuinely cross-disciplinary.

**6. Counter-Evidence Search**
- Search: "CORUM database protein complex annotations non-human species yeast coverage" -- CORUM is explicitly mammalian. No coverage for most Meltome Atlas species. This severely limits the claimed "cross-species" analysis.
- Search: "proteasome subunit thermal stability Tm thermostable proteome Meltome" -- Confirmed that proteasome core subunits have high Tm, regulatory subunits have low Tm (Jarzab 2020; also Arabidopsis TPP data). This SUPPORTS the hypothesis's claim about proteasome Tm heterogeneity.

**7. Groundedness Attack**
- Meltome Atlas (Jarzab 2020): GROUNDED, VERIFIED.
- **"Mateus et al. 2020, Science" for TPCA with >350 complexes**: CITATION ATTRIBUTION ERROR. The TPCA paper with >350 human protein complexes showing correlated Tm is **Tan et al. 2018, Science 359:1170-1177** (authors: Tan CSH, Go KD, Bisteau X, et al.). Mateus et al. 2020 was published in **Molecular Systems Biology** (not Science) and is a review/methods paper about TPP for protein interactions, NOT the original TPCA report. The factual claim about >350 complexes is correct; the attribution to "Mateus 2020, Science" is wrong in both author and journal. This is not a fabricated finding but is an incorrectly attributed citation.
- Proteasome subunit Tm heterogeneity (Jarzab 2020): VERIFIED. Core subunits at upper Tm range, regulatory at lower.
- CORUM complex annotations: VERIFIED to exist for human/mouse. NOT available for most Meltome Atlas species.
- GPD/POT methodology: GROUNDED in statistical literature.
- Grounded/Verifiable: ~55% (reduced due to citation error and limited cross-species annotation).

**8. Hallucination-as-Novelty Check**
- The bridge mechanism (POT/GPD on complex-minimum Tm) uses real statistical tools and real biological data. The citation error is an attribution mistake, not a hallucinated mechanism. Low hallucination risk for the mechanism itself.

**9. Claim-Level Fact Verification**
- [GROUNDED] "Mateus et al. 2020, Science" for TPCA: **INCORRECT ATTRIBUTION**. Correct paper: Tan et al. 2018, Science 359:1170-1177. The claim about >350 complexes is factually correct but attributed to the wrong paper/author/journal. This is a citation hallucination (wrong author + wrong journal), though the underlying fact is real.
- [GROUNDED] "Jarzab 2020 reports regulatory proteasome subunits cluster at lower end of Tm distributions": VERIFIED consistent with the published data.
- [PARAMETRIC] "Conserved bottleneck complexes across species": Untestable for most species due to CORUM being mammalian-only.

**SURVIVAL NOTE**: The hypothesis has a strong biological rationale and the independence restoration argument is genuinely clever. However, the TPCA citation is incorrectly attributed (Tan 2018, not Mateus 2020), and the cross-species analysis is impractical because CORUM covers only mammals. Downgraded from 7 to 5. The hypothesis should be reframed for human/mouse-specific analysis and the citation corrected.

---

## H3: Censored GEV Recovers the Invisible 20% Below TPP Window

### VERDICT: WOUNDED
### Revised Confidence: 4/10 (down from 5)

### ATTACKS:

**1. Novelty Kill**
- Search: "censored GEV likelihood flood frequency left-censored data hydrology Smith 1985" -- Confirmed that censored GEV is well-established in hydrology. Multiple papers on censored flood frequency analysis. NO application to proteomics found. The methodological transfer is NOVEL.

**2. Mechanism Kill**
- Censored GEV maximum likelihood estimation is a mature technique in hydrology. The mathematical transfer to left-censored Tm data (proteins with Tm < 30C are known to exist but Tm is unknown) is correct in principle.
- CRITICAL CONCERN: The GEV is appropriate for distributions that satisfy domain-of-attraction conditions. Tm distributions may be MULTIMODAL in the lower tail: (a) a population of marginally stable folded proteins with Tm 25-35C, and (b) a separate population of intrinsically disordered proteins (IDPs) with no defined Tm or very low Tm. IDPs often lack a cooperative unfolding transition, meaning they do not have a well-defined Tm at all (Leuenberger 2017 showed ~50% of predicted IDPs do show two-state unfolding, but ~50% do not). If the sub-30C population is a mixture of folded low-Tm proteins and IDPs without defined Tm, the GEV assumption is violated and extrapolation will fail.
- CRITICAL CONCERN: The +/-3% accuracy prediction is almost certainly overoptimistic. In hydrology, censored GEV accuracy depends on: (a) censoring fraction (here ~10-20%, which is high), (b) distance from observed data to extrapolation target, and (c) whether the distribution is truly GEV in the tail. Hydrological estimates for 5-15% accuracy are for single return-period extrapolation from well-behaved data with centuries of records. Proteome data has much less tail information. A more realistic prediction would be +/-10-20%.

**3. Logic Kill**
- The analogy between flood censoring (events below a measurement threshold) and TPP censoring (proteins melting below the temperature window) is structurally correct. No logical fallacy.

**4. Falsifiability Kill**
- PASSES with qualification. The cross-validation experiment (extend TPP to 20C and compare predicted vs. observed protein count) is technically feasible and would provide a clear test. However, the hypothesis does not acknowledge that extending TPP to 20C would itself be a substantial experimental effort, not a trivial validation.

**5. Triviality Kill**
- Not trivial. Hydrologists would not think of proteomics; proteomics researchers do not use censored GEV.

**6. Counter-Evidence Search**
- Search: "intrinsically disordered proteins thermal stability Tm low melting temperature proteome" -- Confirmed that IDPs "struggle with" thermal shift assays because they lack cooperative unfolding. Leuenberger 2017 found ~50% of predicted IDPs show two-state denaturation in cells. This means the sub-30C population is a mixture of defined-Tm and undefined-Tm proteins, complicating any distributional assumption.
- This is moderate counter-evidence: the lower tail is likely NOT well-described by a single GEV distribution.

**7. Groundedness Attack**
- 20% unmeasured proteome: GROUNDED (Jarzab 2020, Figueroa-Navedo 2024). VERIFIED.
- Censored GEV in hydrology: GROUNDED. VERIFIED via web search (multiple papers on censored flood frequency GEV).
- Smith 1985 Biometrika: VERIFIED to exist. The specific flood application is correctly tagged PARAMETRIC.
- +/-3% accuracy: PARAMETRIC and likely OVEROPTIMISTIC.
- IDP enrichment in lower tail: PARAMETRIC but supported by indirect evidence (IDPs generally have lower thermal stability).
- Grounded/Verifiable: ~50%. Below ideal.

**8. Hallucination-as-Novelty Check**
- The bridge mechanism (censored GEV) exists independently. The biological problem (left-censored Tm data) is real. The novelty is in the connection, not fabricated. But the QUALITY of the extrapolation may be poor due to IDP multimodality, making the "useful" novelty questionable.

**9. Claim-Level Fact Verification**
- [GROUNDED] "20% of proteome has Tm outside 30-90C": VERIFIED from Jarzab 2020 and Figueroa-Navedo 2024.
- [PARAMETRIC] "Smith 1985 censored flood application": Smith 1985 Biometrika paper exists; flood application distributed across hydrology literature. Correctly tagged.
- [PARAMETRIC] "+/-3% accuracy prediction": OVEROPTIMISTIC. Hydrological analogy suggests 5-15% for favorable conditions; with 10-20% censoring fraction and possible multimodality, 10-20% is more realistic.

**SURVIVAL NOTE**: The methodological transfer is clean and novel. The biological problem (invisible sub-30C proteome) is real and important. However, the accuracy claim is overoptimistic, and the multimodal nature of the sub-30C population (folded low-Tm proteins + IDPs without defined Tm) may violate the GEV assumption, making the extrapolation unreliable. Downgraded from 5 to 4.

---

## H4: Non-Stationary GEV with Drug Covariate Predicts Destabilization Cascades

### VERDICT: KILLED
### Revised Confidence: 2/10 (down from 4)

### ATTACKS:

**1. Novelty Kill**
- Search: "non-stationary GEV drug concentration CETSA thermal proteome profiling covariate" -- Zero relevant results. NOVEL.
- Confirmed: no published work applies non-stationary GEV to drug-treated TPP data.

**2. Mechanism Kill -- FATAL**
- **Statistical under-powering**: Non-stationary GEV models in climate science estimate location/scale/shape as functions of covariates using LONG time series (typically thousands of annual maxima across decades). Drug-concentration series in TPP typically have 3-5 concentrations (sometimes up to 8-10 in high-throughput CETSA). Estimating GEV(mu(c), sigma(c), xi(c)) with mu(c) = mu_0 + mu_1*log(c) requires estimating AT LEAST 5 parameters from a handful of proteome-level distributions. With only 3-5 concentration points, the model is either over-parameterized or requires fixing xi, which defeats the purpose.
- **Effect size**: Staurosporine (a broad kinase inhibitor) shifts Tm of ~49-72 kinases by >1C. Out of ~3,700 detected proteins, this is 1-2% of the proteome. The proteome-wide Tm DISTRIBUTION may change negligibly. The "cascade" mechanism posits that secondary effects (chaperone depletion, cofactor redistribution) amplify the signal, but this cascade is SPECULATIVE -- no evidence that drug-induced Tm shifts propagate beyond direct targets in a cascade-like manner.
- **EC50 prediction from return level**: The claim that the return-level inflection point predicts cellular EC50 (r > 0.7) is unsupported speculation. Drug toxicity mechanisms include membrane disruption, DNA damage, metabolic poisoning, and immune mechanisms -- many of which have no connection to proteome-wide Tm distribution shifts.

**3. Logic Kill**
- The hypothesis conflates two different things: (a) drug-induced Tm shifts of specific targets (a protein-level phenomenon affecting 1-2% of the proteome) and (b) proteome-wide distributional shifts (requiring the tail behavior of the entire distribution to change detectably). The jump from specific target effects to distributional-level detection is a logical gap.

**4. Falsifiability Kill**
- Technically falsifiable (run non-stationary GEV on dose-response TPP data and check predictions). PASSES.

**5. Triviality Kill**
- Not trivial -- the conceptual transfer is creative. But creativity does not compensate for fatal statistical constraints.

**6. Counter-Evidence Search**
- Search: "staurosporine thermal proteome profiling Tm shift kinase number affected proteins" -- Confirmed: staurosporine stabilizes 49-72 kinases by >1C (out of ~7,000 detected). Most effects are modest (1-5C range). This confirms the effect is too small and too sparse to shift the proteome-wide distribution detectably.
- Search: "thermal destabilization cascade drug treatment proteome-wide off-target CETSA" -- Found that proteome-wide CETSA detects off-targets but no evidence for a "cascade" amplification mechanism. Destabilization effects are protein-specific, not cascade-propagating.

**7. Groundedness Attack**
- CETSA/TPP-TR methodology: GROUNDED.
- Non-stationary GEV in climate science: GROUNDED.
- Cascade mechanism: SPECULATIVE. No evidence for proteome-wide thermal destabilization cascading from direct targets.
- mu(c) = mu_0 + mu_1*log(c): PARAMETRIC. Standard in climate GEV but never tested for drug effects.
- EC50 from return level (r > 0.7): SPECULATIVE. No basis for this quantitative prediction.
- Grounded/Verifiable: ~30%. Too low.

**8. Hallucination-as-Novelty Check**
- The novelty depends on the cascade mechanism, which appears to be speculative rather than grounded. The bridge mechanism (non-stationary GEV) is real but misapplied to a context where the data constraints (3-5 concentrations) make it unworkable.

**9. Claim-Level Fact Verification**
- [GROUNDED] Drug-induced Tm shifts measured by CETSA: VERIFIED.
- [PARAMETRIC] "Cascade" through chaperone sequestration and cofactor depletion: UNVERIFIED. No published evidence for this mechanism.
- [PARAMETRIC] EC50 from return level inflection (r > 0.7): UNVERIFIED. Pure speculation.
- [PARAMETRIC] sigma(c) increases with c: UNVERIFIED. Would require demonstrating that drug treatment broadens the Tm distribution, which has not been shown.

**KILL RATIONALE**: Fatal under-powering (3-5 concentrations insufficient for covariate GEV), negligible proteome-wide effect (1-2% of proteins affected), speculative cascade mechanism with no supporting evidence, and quantitative predictions (r > 0.7 for EC50) that are pure invention. The hypothesis is creative but statistically and biologically unworkable.

---

## H5: Pathway-Level Block Maxima Reveal Translation Initiation as Universal Thermal Death Bottleneck

### VERDICT: WOUNDED
### Revised Confidence: 4/10 (down from 5)

### ATTACKS:

**1. Novelty Kill -- PARTIAL**
- Search: "eIF4F thermo-sensing translational heat shock thermal vulnerability bottleneck 2024" -- Found: **eIF4F is a thermo-sensing regulatory node in the translational heat shock response** (Molecular Cell, 2024). This paper demonstrates that the eIF4F complex (eIF4G + eIF4E + eIF4A) disassembles upon heat shock, functioning as a thermal sensor that switches translation from housekeeping to stress mRNAs. This means the concept of translation initiation as thermally vulnerable is ALREADY KNOWN, though not framed using EVT.
- The EVT application (block maxima over KEGG pathways with GEV return levels) is novel. But the biological conclusion (translation initiation is a thermal bottleneck) would not be "discovering" something new -- it would be confirming an existing observation with a different statistical tool. Downgraded from NOVEL to PARTIALLY EXPLORED for the biological claim.

**2. Mechanism Kill**
- KEGG pathways as "blocks": Same concern as H1. KEGG pathways vary enormously in size and are functionally defined, not statistically defined. Block maxima analysis requires blocks of comparable size drawn from a random process. Using pathways as blocks means the "block minimum" is heavily influenced by pathway size (larger pathways have more chances to contain a low-Tm protein by random sampling). Size correction is needed but not proposed.
- Translation initiation prediction: The claim that translation initiation has the lowest pathway-minimum Tm in 10/13 species is specific but may fail because (a) KEGG annotation completeness varies wildly across species, (b) the eIF factors may not have unusually low Tm in lysate TPP data (they could be stabilized by mRNA or partner interactions in vivo), and (c) the prediction ignores metabolic pathways with cofactor-dependent enzymes that might also be thermally vulnerable.

**3. Logic Kill**
- The hypothesis assumes that pathway-minimum Tm identifies the "thermal death bottleneck." This conflates thermal vulnerability of individual proteins with pathway failure. A pathway can tolerate loss of one low-Tm protein if that protein is redundant or dispensable. The block minimum overestimates pathway vulnerability when low-Tm members are non-essential.

**4. Falsifiability Kill**
- PASSES. The prediction (translation initiation has lowest block-minimum Tm in 10/13 species) is quantitatively testable.

**5. Triviality Kill**
- The eIF4F thermo-sensing paper (2024) already showed that translation initiation is thermally sensitive. Using EVT block maxima to re-derive this known result would be confirmatory, not discovery. Approaches triviality for the biological conclusion (though the EVT methodology is novel).

**6. Counter-Evidence Search**
- The Leuenberger 2017 paper found that ~80 proteins collapse near the species-specific optimum temperature, and these include proteins "essential for protein, nucleic acid, and fatty acid biosynthesis and nucleotide and cofactor binding." Translation was not singled out as THE bottleneck; rather, multiple essential processes fail near-simultaneously. This suggests the "universal bottleneck" claim may be too strong.
- The eIF4F paper (2024) found that translation initiation is regulated by thermal sensing (eIF4G conformational change), suggesting evolution has specifically ADAPTED translation initiation to sense temperature, rather than it being a passive vulnerability. This reinterpretation weakens the "bottleneck = failure" framing.

**7. Groundedness Attack**
- Meltome Atlas + KEGG: GROUNDED.
- Proteasome core subunits at upper Tm range: GROUNDED (Jarzab 2020).
- "eIF4E, eIF2alpha likely to have lower Tm" -- PARAMETRIC. The eIF4F paper (2024) shows eIF4G is thermo-sensitive, but specific Tm values for eIF4E and eIF2alpha from Meltome data are not cited. The claim in the hypothesis about "eIF factors having low Tm" is a reasonable inference but unverified.
- Translation initiation as bottleneck in 10/13 species: PARAMETRIC. Strong prediction, untested.
- Grounded/Verifiable: ~45%.

**8. Hallucination-as-Novelty Check**
- The eIF4F thermo-sensing paper (2024) means the biological claim is not genuinely novel -- the thermal sensitivity of translation initiation is known. The EVT framing is novel, but if it merely re-derives a known result, the "novelty" is methodological rather than biological.

**9. Claim-Level Fact Verification**
- [GROUNDED] Proteasome core subunits at upper Tm range: VERIFIED.
- [PARAMETRIC] "eIF4E, eIF2alpha likely have lower Tm than average": NOT VERIFIED from any specific data source. The eIF4F paper shows conformational sensitivity, but this is about functional inactivation (complex disassembly), not necessarily a low Tm in TPP measurements.
- [PARAMETRIC] Translation initiation lowest block-minimum in 10/13 species: UNTESTED PREDICTION. Reasonable but not grounded.

**SURVIVAL NOTE**: The EVT methodology is novel, but the biological conclusion (translation initiation is thermally vulnerable) is partially known from the eIF4F thermo-sensing paper (2024). The prediction is specific enough to test, but the block maxima approach needs size correction for varying pathway sizes. Downgraded from 5 to 4 due to partial novelty kill and methodological concerns.

---

## H6: Extremal Index Quantifies Thermal Cooperativity -- Eukaryotes vs. Prokaryotes

### VERDICT: KILLED
### Revised Confidence: 1/10 (down from 5)

### ATTACKS:

**1. Novelty Kill**
- Search: "extremal index cross-sectional data static distribution NOT time series" -- All literature confirms the extremal index is defined for STATIONARY SEQUENCES (temporal processes), not cross-sectional data. Zero applications of extremal index to non-temporal distributions found. This is "novel" because it may be WRONG, not because it is unexplored.

**2. Mechanism Kill -- FATAL**
- **The extremal index theta is defined for stationary time series.** Leadbetter's definition (from the 1983 textbook correctly cited as PARAMETRIC) requires a stationary sequence X_1, X_2, ..., X_n where theta quantifies the tendency of exceedances above a high threshold to cluster in TIME. The runs estimator, intervals estimator, and all standard theta estimation methods assume an ordered temporal sequence with serial dependence.
- Proteome Tm data is a CROSS-SECTION: each protein has one Tm value. There is no natural ordering. If you sort proteins by Tm (as the hypothesis suggests), you create an artificial ordering that has no temporal or causal meaning. "Clusters" in Tm space (proteins with similar Tm) arise from trivially different reasons than temporal clusters of extremes. Two proteins can have similar Tm by chance, by shared physicochemical properties, or by being in the same complex. The extremal index cannot distinguish these.
- **The hypothesis acknowledges this problem in "Why this might be wrong" section 1** but proceeds to build the entire mechanism on the assumption that the adaptation will work. The acknowledgment is honest but the methodological problem is FATAL, not just a caveat.
- ALTERNATIVE: Spatial extremal indices exist for spatial processes (e.g., extreme rainfall over a geographic grid), but these require spatial coordinates and a meaningful spatial distance metric. Proteins do not have natural spatial coordinates (protein-protein interaction network distance could serve, but this would be a different analysis entirely).

**3. Logic Kill**
- The hypothesis confuses two types of clustering: (a) TEMPORAL clustering of extreme events (what theta measures) and (b) DISTRIBUTIONAL concentration of values near certain Tm ranges (what proteome Tm data shows). These are fundamentally different statistical phenomena. Applying theta to cross-sectional data is a category error.

**4. Falsifiability Kill**
- The hypothesis is technically falsifiable (compute theta and compare), but the computation itself is MEANINGLESS because theta is not defined for cross-sectional data. A falsifiable prediction based on a misapplied statistic does not constitute genuine falsifiability.

**5. Triviality Kill**
- An EVT specialist would immediately recognize that the extremal index cannot be applied to cross-sectional data. This is a fundamental misunderstanding of the statistical tool, not a creative application.

**6. Counter-Evidence Search**
- Multiple references confirm that "the extremal index is a measure of the degree of local dependence in the extremes of a stationary process" (emphasis on "stationary process"). The R packages exdex and extRemes implement theta estimation exclusively for time-ordered data.
- No published work applies extremal index to cross-sectional distributions, which is evidence that the EVT community considers it inapplicable.

**7. Groundedness Attack**
- TPCA complex co-aggregation: GROUNDED. But cited as "Mateus et al. 2020, Science" -- same attribution error as H2. Correct reference: Tan et al. 2018, Science.
- Lim et al. 2023, Nature Communications: VERIFIED. Improved TPCA.
- Extremal index concept: GROUNDED in the literature but for time series.
- Human theta ~ 0.4-0.6: SPECULATIVE and based on a misapplication.
- T. thermophilus theta ~ 0.8-0.9: SPECULATIVE and based on a misapplication.
- Grounded/Verifiable for correct application: ~20%. Fatally low.

**8. Hallucination-as-Novelty Check**
- This is the classic hallucination-as-novelty pattern: the hypothesis seems novel because it applies a real statistical concept (extremal index) to a new domain (proteome Tm). But the "novelty" arises from MISAPPLICATION -- the tool is designed for a fundamentally different data type. The EVT community has not made this connection because it is statistically invalid, not because they lacked the insight.

**9. Claim-Level Fact Verification**
- [GROUNDED] "Mateus et al. 2020, Science" for TPCA: SAME CITATION ERROR AS H2. Correct: Tan et al. 2018, Science.
- [PARAMETRIC] "Theta can be estimated from cross-sectional Tm data": NOT VERIFIED. All theta estimation methods require time-ordered data. This claim is factually incorrect.
- [PARAMETRIC] "Human theta ~ 0.4-0.6": Based on a misapplication of theta. Not meaningful.

**KILL RATIONALE**: Fundamental methodological error. The extremal index is defined for stationary time series and cannot be meaningfully applied to cross-sectional proteome Tm data. Sorting proteins by Tm to create an artificial sequence does not produce a valid input for theta estimation. The TPCA citation error (Tan 2018, not Mateus 2020) is a secondary issue. The biological question (quantifying thermal cooperativity) is interesting but the proposed tool is wrong for this data type.

---

## H7: POT Functional Enrichment Reveals Thermal Disposability in Signal Transduction

### VERDICT: WOUNDED
### Revised Confidence: 4/10 (down from 6)

### ATTACKS:

**1. Novelty Kill -- PARTIAL**
- Search: "Leuenberger 2017 Science thermal stability GO enrichment unstable proteins cofactor DNA-binding kinase" -- Confirmed: **Leuenberger et al. 2017 (Science)** already performed GO enrichment analysis on proteins stratified by thermal stability. Key finding: unstable proteins enriched for "cofactor and DNA-binding proteins"; stable proteins enriched for "ribosomal, RNA-binding, and protein biosynthesis processes."
- This PARTIALLY SCOOPS H7. The specific GO categories differ slightly (Leuenberger found "cofactor and DNA-binding" enrichment; H7 predicts "signal transduction GO:0007165 and transcription factor GO:0003700"), but the general approach of functionally annotating the thermally vulnerable tail of the proteome has been done.
- H7's novelty claim is that it uses POT/GPD to rigorously define the "thermally vulnerable subproteome" (rather than arbitrary percentile cutoffs), and predicts specific GO terms (signal transduction, not just DNA-binding). This is an INCREMENTAL improvement, not a fully novel insight.

**2. Mechanism Kill**
- POT/GPD fitting to the lower tail is statistically sound. The threshold selection (u = 40C) is reasonable.
- CONCERN: The "thermal disposability" interpretation (evolution tolerates low Tm in short-lived signaling proteins) is an attractive narrative but difficult to distinguish from simpler explanations: (a) signaling proteins tend to be larger (more domains), and larger proteins have slightly lower Tm on average; (b) signaling proteins have more disordered regions, and disorder correlates with lower Tm; (c) signaling proteins are less abundant, and less abundant proteins are less thermostable (Leuenberger 2017 showed abundance-stability correlation).
- The hypothesis acknowledges these confounders ("after controlling for protein size and disorder content") but does not propose how to disentangle "thermal disposability" from these known correlations.

**3. Logic Kill**
- The observation that signaling proteins have low Tm, even if confirmed, does not establish that this is an evolved "design principle" of thermal disposability. This would be post-hoc reasoning: observing a pattern and then inventing an adaptive explanation. A null model (low Tm results from disorder + size + abundance confounders) would need to be explicitly ruled out before claiming an evolutionary design principle.

**4. Falsifiability Kill**
- The GO enrichment prediction (signal transduction FDR < 0.01 across all 13 species) is falsifiable.
- The "not exclusively IDPs" control prediction adds falsifiable nuance. PASSES.

**5. Triviality Kill**
- PARTIAL. Given that Leuenberger 2017 already showed GO enrichment of thermally unstable proteins, repeating this with POT/GPD instead of percentile cutoffs is an incremental methodological improvement, not a discovery. A proteomics grad student who read Leuenberger 2017 would consider the GO enrichment of the lower tail "already known."
- The specific POT/GPD framing and the "thermal disposability" interpretation are novel, but the core finding would not be surprising.

**6. Counter-Evidence Search**
- Search: "protein thermal stability GO enrichment signal transduction kinase lower tail vulnerable" -- Found that Leuenberger 2017 already identified functional enrichment in thermally unstable proteins. Also found that "the correlation between detected kinase substrate motifs and thermal stability values was not significant," suggesting kinases do not have systematically altered Tm.
- CDK2 Tm: The hypothesis claims "CDK2 Tm ~55C" as an example of a stable kinase. Web search found CDK2 Tm ~51C (wild-type, by DSF). The claim is quantitatively incorrect by ~4C. This is not a fatal error but demonstrates imprecise parametric knowledge. (Note: CDK2 Tm can vary with measurement conditions, but ~55C appears to be overestimated.)

**7. Groundedness Attack**
- Meltome Atlas + GO annotations: GROUNDED.
- POT/GPD methodology: GROUNDED.
- "Signal transduction enriched at FDR < 0.01": PARAMETRIC prediction. Consistent with Leuenberger 2017 but not yet tested with POT/GPD.
- "Thermal disposability" concept: SPECULATIVE. Attractive narrative without a way to distinguish from confounders.
- "CDK2 Tm ~55C": INCORRECT. Actual value ~51C.
- "Kinases and TFs have systematically low Tm": PARTIALLY SUPPORTED. DNA-binding proteins have lower Tm (Leuenberger 2017), but kinases specifically show variable Tm with no systematic pattern.
- Grounded/Verifiable: ~50%.

**8. Hallucination-as-Novelty Check**
- The GO enrichment approach is not novel (Leuenberger 2017). The POT/GPD framing is novel but the core finding is expected to replicate existing results. The "thermal disposability" interpretation is a speculative narrative. The CDK2 Tm claim is incorrect. Risk of parametric knowledge error: MODERATE.

**9. Claim-Level Fact Verification**
- [GROUNDED] Meltome Atlas data: VERIFIED.
- [PARAMETRIC] "CDK2 Tm ~55C": INCORRECT. Actual ~51C (by DSF). Error of ~4C.
- [PARAMETRIC] "Signal transduction (GO:0007165) and TF (GO:0003700) enriched at FDR < 0.01": UNTESTED but consistent with prior GO enrichment work.
- [PARAMETRIC] "Not exclusively IDPs": Supported by Leuenberger 2017 (50% of predicted IDPs show two-state unfolding in cells).

**SURVIVAL NOTE**: The hypothesis is partially scooped by Leuenberger 2017, who already performed GO enrichment on thermally stratified proteins. The incremental contribution (POT/GPD threshold definition vs. arbitrary cutoffs) is real but modest. The "thermal disposability" interpretation is speculative and may not survive confounder correction. CDK2 Tm claim is incorrect. Downgraded from 6 to 4.

---

## META-CRITIQUE

### Kill Rate Assessment
- **Kill rate: 2/7 = 29%**. Within healthy range (target 30-50%).
- H4 killed for fatal statistical under-powering (3-5 concentrations for covariate GEV).
- H6 killed for fundamental methodological misapplication (extremal index for cross-sectional data).
- Both kills are based on evidence of methodological impossibility, not absence of evidence.

### Strongest Reasons Each SURVIVOR Should Have Been Killed

- **H1 (SURVIVES)**: The OGT regression has only 13 data points with 2-3 thermophiles, making the non-linear xi-OGT claim statistically unpowerable. This approaches "hypothesis that cannot be adequately tested with available data."
- **H2 (WOUNDED)**: The citation attribution error (Tan 2018, not Mateus 2020) is technically a citation hallucination under the v5.4 standard. I WOUNDED rather than KILLED because the underlying fact (>350 complexes) is correct; only the attribution is wrong. A stricter interpretation would KILL.
- **H3 (WOUNDED)**: The IDP multimodality problem may make GEV fitting fundamentally inappropriate for the sub-30C population, in which case the entire hypothesis framework collapses.
- **H5 (WOUNDED)**: The eIF4F thermo-sensing paper (2024) means the biological conclusion is already known. The EVT framing is methodologically novel but scientifically redundant.
- **H7 (WOUNDED)**: Leuenberger 2017 already performed functional enrichment of thermally stratified proteins. H7's contribution is incremental at best.

### Web Search Coverage Check
- H1: 3 searches (novelty + counter-evidence + claim verification). COMPLETE.
- H2: 3 searches (novelty + TPCA citation + CORUM coverage). COMPLETE.
- H3: 2 searches (novelty + IDP Tm). COMPLETE.
- H4: 3 searches (novelty + staurosporine effects + cascade evidence). COMPLETE.
- H5: 3 searches (novelty + eIF4F paper + thermal death bottleneck). COMPLETE.
- H6: 2 searches (novelty + extremal index definition). COMPLETE.
- H7: 3 searches (novelty + Leuenberger GO enrichment + CDK2 Tm). COMPLETE.

### Claim-Level Verification Check (v5.4)
- All [GROUNDED] citations verified via web search.
- TPCA citation error identified (Tan 2018, not Mateus 2020) -- present in H2 and H6.
- CDK2 Tm error identified (~51C, not ~55C) -- present in H7.
- No other citation hallucinations detected.

---

## Critic Questions for Generator (Cycle 2)

1. **H1**: What is the expected MAGNITUDE of xi differences between thermophile and mesophile proteomes? If the effect is <0.05, is the analysis adequately powered given the SE(xi) ~ 0.016? Can you provide a power calculation?

2. **H2**: Please correct the TPCA citation from "Mateus et al. 2020, Science" to "Tan et al. 2018, Science 359:1170-1177." Also: given that CORUM covers only mammals, how can the cross-species analysis be performed for the non-mammalian species in the Meltome Atlas (E. coli, S. cerevisiae, T. thermophilus, etc.)?

3. **H3**: How does the hypothesis handle the multimodal nature of the sub-30C population? If ~50% of proteins below 30C are IDPs without a well-defined Tm (Leuenberger 2017), does this violate the GEV domain-of-attraction assumption? Revise the accuracy prediction from +/-3% to something more realistic.

4. **H5**: Given that eIF4F has already been identified as a "thermo-sensing regulatory node" (Molecular Cell 2024), how does the EVT analysis add value beyond confirming a known result? Does the block maxima approach correct for unequal KEGG pathway sizes?

5. **H7**: How does this hypothesis differ from Leuenberger et al. 2017 (Science), which already performed GO enrichment on thermally stratified proteins and found enrichment for "cofactor and DNA-binding proteins"? What specific new insight does POT/GPD provide beyond replacing arbitrary percentile cutoffs? Please correct CDK2 Tm from ~55C to ~51C.

6. **General (H1, H5)**: KEGG pathways used as "blocks" for block maxima analysis vary enormously in size. How do you correct for this? Larger pathways are more likely to contain extreme-Tm proteins simply by having more members. Do you propose a size-correction method or random partitioning instead?
