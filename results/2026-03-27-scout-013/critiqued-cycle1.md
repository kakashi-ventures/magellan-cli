# Critiqued Hypotheses — Cycle 1
## Session: 2026-03-27-scout-013
## Target: Extreme Value Statistics x Proteome-wide Thermal Stability Distributions
## Critic Agent | Model: opus-4.6 | Date: 2026-03-27

---

## Summary

| H# | Title | Verdict | Revised Confidence | Original Confidence |
|----|-------|---------|-------------------|-------------------|
| H1 | GEV Tail Index (xi) as Phylogenomic Signature | SURVIVES | 5/10 | 6/10 |
| H2 | Complex-Minimum Tm via POT | WOUNDED | 5/10 | 7/10 |
| H3 | Censored GEV Recovers Invisible 20% | WOUNDED | 4/10 | 5/10 |
| H4 | Non-Stationary GEV with Drug Covariate | KILLED | 2/10 | 4/10 |
| H5 | Translation Initiation as Thermal Death Bottleneck | WOUNDED | 3/10 | 5/10 |
| H6 | Extremal Index Quantifies Thermal Cooperativity | KILLED | 2/10 | 5/10 |
| H7 | POT Enrichment: Thermal Disposability | WOUNDED | 4/10 | 6/10 |

**Kill rate: 2/7 = 29%**
**Survival rate: 1/7 = 14% (SURVIVES), 4/7 = 57% (WOUNDED), 2/7 = 29% (KILLED)**

---

## HYPOTHESIS 1: GEV Tail Index (xi) as a Phylogenomic Signature of Thermal Adaptation Strategy

**VERDICT: SURVIVES**

### ATTACKS:

**1. Novelty Kill**
- Search: "extreme value theory proteome thermal stability GEV distribution protein melting temperature" -- zero relevant results applying EVT to Tm distributions
- Search: "tail index thermal adaptation proteome thermophile mesophile" -- zero results for EVT tail index in this context; all results cover amino acid composition differences and mean Tm shifts
- Search: "extreme value proteome protein distribution Gumbel Weibull Frechet fitting 2024 2025 2026" -- zero relevant results
- **Verdict: NOVEL.** No prior work connects GEV shape parameter estimation to cross-species proteome Tm distributions. The idea that thermal adaptation involves tail sculpting (not just mean shifting) appears genuinely unexplored.

**2. Mechanism Kill**
The mechanism is mathematically sound. The Fisher-Tippett-Gnedenko theorem guarantees GEV convergence for block minima from sufficiently large i.i.d. samples. The bounded nature of Tm (30-90C in the Meltome Atlas; theoretical protein stability limit ~120C) predicts Weibull domain (xi < 0), which is physically consistent. The question is whether inter-species xi differences are detectable. The computational validation estimates SE(xi) ~ 0.029 at n=5,000-7,000, which would detect differences of ~0.06 at 95% confidence. Whether the biological signal exceeds 0.06 is unknown but not implausible. The block maxima approach over KEGG pathways (~300 blocks per species) provides adequate sample size (12x over the ~25-50 minimum for GEV fitting from standard EVT practice). **No mechanism kill.**

**3. Logic Kill**
The hypothesis correctly distinguishes between two independent evolutionary strategies: mean-shift (translating the entire Tm distribution upward) and tail-sculpting (changing the shape parameter xi to narrow the vulnerable tail). These are mathematically independent parameters of the GEV distribution. The logic is clean: if thermal adaptation were purely mean-shift, all species would have the same xi regardless of OGT. A xi-OGT correlation would demonstrate a distinct adaptation mechanism. **No logic kill.** One minor concern: the hypothesis assumes that xi is an "evolutionary variable" selected for by thermal pressure, but xi could also change as a passive consequence of mean-shift (if moving the mean upward also truncates the lower tail mechanically). This would weaken the "distinct strategy" claim to a "correlated consequence" claim.

**4. Falsifiability Kill**
Highly falsifiable. The prediction is specific: xi_thermophile < xi_mesophile < xi_psychrophile (all negative). This can be tested immediately on the existing Meltome Atlas data for 13 species. A null result (xi does not vary with OGT, or varies in the wrong direction) would kill the hypothesis. **Passes.**

**5. Triviality Kill**
Not trivial. A statistician would immediately recognize that GEV fitting to bounded biological data should yield Weibull domain -- but the cross-species comparison of xi as a function of OGT is a non-obvious biological prediction. A proteomics expert would not spontaneously think to compute the GEV shape parameter. **Not trivial.**

**6. Counter-Evidence Search**
- Search: "thermal adaptation proteome thermophile mesophile" -- extensive literature on amino acid composition changes, hydrophobic core packing, salt bridges. ALL of this work characterizes thermal adaptation via mean Tm or structural determinants. None examines tail behavior or distributional shape. This is not counter-evidence per se, but it means the entire field's framework is mean-centric -- the hypothesis challenges a deeply embedded assumption.
- Potential counter-evidence: if all species show identical Tm distribution shapes (just shifted means), xi would be constant. This is plausible but has never been tested. **No direct counter-evidence found.** The absence of counter-evidence is a good sign for a genuinely unexplored hypothesis.

**7. Groundedness Attack**
- Meltome Atlas (Jarzab 2020, Nature Methods): GROUNDED -- confirmed via web search, paper exists, 48,000 proteins, 13 species, Tm 30-90C
- FTG theorem guarantees GEV convergence: GROUNDED -- standard mathematical result
- ~300 KEGG pathways per species for blocking: GROUNDED -- computational validation confirms
- SE(xi) ~ 0.029 at n=5,000: GROUNDED -- computational validation ran the calculation
- xi varies systematically with OGT: PARAMETRIC -- this is the prediction, not a claim
- Non-linear xi-OGT relationship: SPECULATIVE -- no basis provided for non-linearity
- Coles 2001 "25 block minimum": PARAMETRIC -- the hypothesis itself downgraded this; standard EVT practice recommends 50+ blocks (Coles discusses this but does not give a single threshold)
- **Groundedness: ~70% (5/7 claims grounded or verifiable)**

**8. Hallucination-as-Novelty Check**
The bridge mechanism (GEV fitting to bounded data) exists independently of this hypothesis. The biological data (Meltome Atlas cross-species Tm) exists independently. The novelty is in the CONNECTION -- applying GEV shape parameter comparison across species to test a specific evolutionary prediction. This is genuine novelty, not hallucination masquerading as novelty. The components are real; only the connection is new. **Low hallucination risk.**

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab et al. 2020, Nature Methods: VERIFIED -- paper exists (Nature Methods 17:495-503, DOI 10.1038/s41592-020-0801-4), 48,000 proteins, 13 species confirmed
- [GROUNDED] "Mean-centric description ignores shape of Tm distribution's lower tail": VERIFIED -- all literature found describes thermal adaptation via mean Tm, amino acid composition, or structural features; no work on distributional shape
- [GROUNDED] "Meltome Atlas provides Tm for ~48,000 proteins across 13 species spanning archaea to humans, with OGTs ranging from ~4C to ~80C": VERIFIED -- confirmed from the paper
- [PARAMETRIC] Coles 2001 block minimum: Coles 2001 is a real textbook (Springer, confirmed via web search). The "25 block minima" claim was already downgraded by the Generator. Standard EVT practice recommends ~50+ blocks, which is satisfied by the ~300 KEGG pathways.
- **No citation hallucinations detected.**

**REVISED CONFIDENCE: 5/10** (down from 6) -- downgraded slightly because (a) the expected magnitude of inter-species xi differences is completely unknown, and (b) only 1-2 true thermophiles are in the 13-species Meltome Atlas, potentially under-powering the xi-OGT regression. The hypothesis is sound and testable but the effect size is uncertain.

**SURVIVAL NOTE**: This is the strongest hypothesis in the set. Genuinely novel (zero prior work), mathematically rigorous (FTG theorem), immediately testable on public data, and the prediction (xi varies with OGT) is specific and falsifiable. The main vulnerability is that the effect may be too small to detect with only 13 species (and most being mesophiles). The single strongest reason it should have been killed but was not: if the Tm distribution tail shape is a passive consequence of mean-shift rather than an independent evolutionary variable, the hypothesis reduces to a mathematical restatement of a known fact, which would be a triviality kill in disguise.

---

## HYPOTHESIS 2: Complex-Minimum Tm as an EVT Variable Identifies Thermal Bottleneck Complexes

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "extreme value theory proteome thermal stability" -- zero results for EVT applied to complex-minimum Tm
- No prior work applies POT/GPD to complex-minimum Tm distributions. The concept of "thermal bottleneck subunit" exists informally (Jarzab 2020 mentions proteasome subunit Tm heterogeneity) but has never been formalized via EVT return levels. **NOVEL.**

**2. Mechanism Kill**
The mechanism is sound. Taking the minimum Tm per complex is standard weakest-link analysis. Fitting GPD to exceedances below a threshold is standard POT methodology. The independence restoration argument (different complexes share few subunits, so complex-minimum Tm values are approximately independent) is reasonable, though not perfect -- shared chaperone dependencies could create residual correlation. The return level interpretation ("temperature at which p% of complexes fail") is a clean mapping from EVT to biology. **No mechanism kill.**

**3. Logic Kill**
The hypothesis assumes "the least thermally stable subunit is the thermal bottleneck." This conflates individual protein Tm (measured in lysate) with functional failure temperature. A subunit with Tm = 40C may be stabilized by 5-10C within the assembled complex. The Meltome Atlas measures apparent Tm in lysate, which includes SOME complex context but not complete in-complex stability. This is a real limitation but acknowledged by the Generator. Not a fatal logic error, but a non-trivial caveat. **Wounded, not killed.**

**4. Falsifiability Kill**
Highly falsifiable: the prediction that specific complexes (spliceosome, proteasome regulators, ribosome assembly factors) consistently appear as POT exceedances across species is testable immediately. A null result (no conserved bottleneck complexes) would falsify. **Passes.**

**5. Triviality Kill**
The weakest-link concept is well-known in reliability engineering. A grad student in structural reliability would recognize the block-minimum approach instantly. However, applying it to protein complexes via EVT formalism is non-trivial because (a) the statistical framework adds rigorous confidence intervals that the informal "weakest subunit" concept lacks, and (b) the cross-species comparison is a new biological question. **Not trivial.**

**6. Counter-Evidence Search**
- Search: "Mateus 2020 Science TPCA thermal proximity co-aggregation 350 protein complexes" -- the >350 complex co-aggregation finding is CONFIRMED, but see citation error below
- Potential counter-evidence: in-complex stabilization may mean the lowest-Tm subunit in isolation is NOT the bottleneck when assembled. The Meltome Atlas measures Tm in lysate conditions where some complexes remain assembled and others dissociate during heating. This makes the "minimum Tm = bottleneck" assumption approximate at best. **Moderate counter-evidence from in-complex stabilization effects.**

**7. Groundedness Attack**
- Meltome Atlas (Jarzab 2020): GROUNDED
- TPCA >350 human complexes co-aggregation: GROUNDED (finding is real) but CITATION IS WRONG (see Vector 9)
- Proteasome regulatory subunits cluster at lower Tm (Jarzab 2020): GROUNDED -- the paper reports this
- CORUM database for human complex annotations: GROUNDED -- CORUM is a well-established database
- GPD/POT methodology: GROUNDED -- standard EVT
- Conserved bottleneck complexes across species: SPECULATIVE -- the prediction itself
- >1,000 complexes in CORUM for human: PARAMETRIC -- standard CORUM stats but not verified here
- **Groundedness: ~65% (4.5/7 claims grounded or verifiable, but a key citation is misattributed)**

**8. Hallucination-as-Novelty Check**
Both components (complex-minimum analysis, GPD fitting) exist independently. The bridge is the combination. Low hallucination risk for the mechanism. However, the citation error raises concerns about the factual grounding layer -- see below.

**9. Claim-Level Fact Verification -- CRITICAL FINDING**
- [GROUNDED] "Mateus et al. 2020, Science 367:eaaz5268" -- **CITATION ERROR DETECTED.** Mateus et al. 2020 published "Thermal proteome profiling for interrogating protein interactions" in **Molecular Systems Biology** (vol 16, e9232), NOT in Science. The TPCA method and the ">350 annotated human protein complexes" finding comes from **Tan et al. 2018, Science 359:1170-1177** (DOI: 10.1126/science.aan0346). The citation "Science 367:eaaz5268" is a fabricated journal-volume-article-ID combination -- Science volume 367 (2020) does not contain an article with that identifier for this content. This is a citation conflation: the finding is real (confirmed via web search -- Tan et al. 2018 Science reports >350 human complexes with significant TPCA signatures) but the attribution is wrong. The Generator conflated two different papers (Mateus 2020 in Mol Sys Biol, which is a TPP review, with Tan 2018 in Science, which introduced TPCA).
- [GROUNDED] Jarzab 2020 Nature Methods: VERIFIED
- [GROUNDED] "Regulatory proteasome subunits cluster at lower end of Tm distributions" (attributed to Jarzab 2020): CONSISTENT with the paper's reports on proteasome heterogeneity, though the exact phrasing is the Generator's interpretation
- [PARAMETRIC] Lim et al. 2023, Nature Communications -- VERIFIED. Lim et al. 2023 published "Improved in situ characterization of protein complex dynamics at scale with thermal proximity co-aggregation" in Nature Communications (DOI: 10.1038/s41467-023-43526-2). This is the Slim-TPCA paper. The citation is real.

**The citation conflation is a significant grounding error but does not invalidate the hypothesis mechanism because the underlying finding (>350 human complexes with correlated co-aggregation) is real and correctly attributed to the TPCA line of work. However, the specific "Science 367:eaaz5268" identifier is fabricated and must be corrected.**

**REVISED CONFIDENCE: 5/10** (down from 7) -- downgraded from 7 to 5 because (a) the citation error undermines trust in the grounding chain, (b) in-complex stabilization makes the "minimum Tm = bottleneck" assumption approximate, and (c) complex annotations outside human/yeast are sparse, limiting the cross-species analysis that gives this hypothesis its power. The core idea remains strong.

**SURVIVAL NOTE**: The strongest aspect is the elegant solution to the independence problem: by collapsing each complex to its minimum Tm, you restore approximate independence AND get a more biologically meaningful variable. The main reason this should have been killed: if in-complex stabilization raises the effective Tm of the "weakest" subunit by 5-10C, the measured lysate Tm_min is a poor proxy for the actual functional failure temperature, and the POT analysis would be fitting noise rather than signal.

---

## HYPOTHESIS 3: Censored GEV Estimation Recovers the Invisible 20% Below the TPP Measurement Window

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "censored GEV" OR "censored extreme value" biological distribution proteomics -- zero results for biological/proteomics application. Found censored GEV in hydrology (partial probability weighted moments for censored flood data) but never applied to any biological distribution.
- **NOVEL as a cross-domain transfer.** Censored GEV for flood frequency is well-established. The application to proteomics left-censoring is new.

**2. Mechanism Kill**
The censored likelihood approach is mathematically valid: replacing f(x) with F(c) for left-censored observations is standard MLE. The question is whether the proteome Tm distribution is well-approximated by GEV in the unobserved tail below 30C. If the tail is multi-modal (a distinct population of IDPs with Tm < 20C, separate from marginally stable folded proteins at 25-35C), the unimodal GEV extrapolation will be systematically wrong. The hypothesis acknowledges this risk but does not propose a test for multi-modality before extrapolation. **Moderate mechanism concern: GEV assumes unimodal tail; reality may be multi-modal.**

**3. Logic Kill**
The analogy to flood frequency censoring is structurally sound: both involve left-censored observations from a physical process with a measurement threshold. However, flood frequency data has centuries of historical records validating GEV assumptions; proteome Tm data has no such validation for the tail below 30C. The hypothesis extrapolates from a validated domain (hydrology) to an unvalidated domain (proteomics) -- the analogy is reasonable but the confidence should be lower than in hydrology. The +/-3% accuracy prediction is borrowed from hydrological performance but has no basis in the proteomics domain. **Mild logic concern: accuracy claim transferred without domain-specific validation.**

**4. Falsifiability Kill**
Falsifiable in principle: the cross-validation experiment (extend TPP to 20C and compare predicted vs. observed protein counts in 20-30C range) is concrete and executable. The +/-3% prediction is quantitatively falsifiable. **Passes.**

**5. Triviality Kill**
A statistician familiar with censored likelihood would immediately think of this approach when told about the 20% unmeasured proteome. The methodological transfer is straightforward. However, the biological insight (predicting which proteins have Tm < 30C and testing for IDP enrichment) adds non-trivial biological content beyond the statistical method. **Borderline -- the statistical part is straightforward; the biological prediction rescues it from triviality.**

**6. Counter-Evidence Search**
- Search: "protein cold denaturation" -- cold denaturation is a real phenomenon where proteins unfold at LOW temperatures (below ~10-15C). Proteins with Tm < 30C measured by TPP may include cold-denatured proteins that have ALREADY unfolded and precipitated at the starting assay temperature. This introduces a non-random missing data pattern (proteins that cold-denature are systematically absent, not just censored). The censored GEV approach assumes the censored proteins are "normal" proteins with low Tm, not proteins with qualitatively different denaturation mechanisms. **Moderate counter-evidence: cold denaturation creates non-random censoring that violates the model assumptions.**

**7. Groundedness Attack**
- 20% unmeasured proteome (Jarzab 2020, Figueroa-Navedo 2024): GROUNDED
- Censored GEV in hydrology: GROUNDED (established methodology)
- Smith 1985 Biometrika: VERIFIED as a real paper, but the specific flood censoring application is spread across multiple papers, not solely Smith 1985. Generator already downgraded this to PARAMETRIC.
- +/-3% accuracy prediction: SPECULATIVE -- no basis in proteomics data; borrowed from hydrology without justification
- IDP enrichment in lower tail: PARAMETRIC -- plausible but not demonstrated
- "~10% of proteins with Tm < 30C": PARAMETRIC -- the 20% figure includes both below 30C and above 90C; the split is uncertain
- **Groundedness: ~50% (3/6 claims grounded or verifiable)**

**8. Hallucination-as-Novelty Check**
The bridge mechanism (censored GEV likelihood) is well-established in hydrology and verified via web search. The proteomics data source is real. The novelty is in the cross-domain transfer, not in fabricated components. **Low hallucination risk.**

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab 2020, Nature Methods: VERIFIED
- [GROUNDED] Figueroa-Navedo & Ivanov 2024, Cell Reports Methods: Confirmed from literature landscape -- "selection of inadequate temperature windows" as key challenge
- [PARAMETRIC] Smith 1985, Biometrika 72(1):67-90: VERIFIED as a real paper via web search ("Maximum likelihood estimation in a class of nonregular cases"). The paper is foundational for MLE in non-regular cases. The specific application to censored flood GEV is a parametric extrapolation from this paper.
- [SPECULATIVE] "+/-3 percentage points accuracy": Purely speculative -- no basis provided for this specific threshold in the proteomics context
- **No citation hallucinations. The +/-3% claim is speculative but not presented as grounded.**

**REVISED CONFIDENCE: 4/10** (down from 5) -- maintained near original because the core transfer is clean, but downgraded due to (a) multi-modal tail risk undermining the GEV assumption, (b) cold denaturation introducing non-random censoring, and (c) the +/-3% accuracy claim being speculative.

**SURVIVAL NOTE**: The main reason this should have been killed: if the sub-30C proteome is not GEV-distributed (e.g., it contains a distinct subpopulation of IDPs and membrane proteins with qualitatively different denaturation physics), then the censored GEV extrapolation is not just inaccurate but fundamentally wrong -- you cannot recover the shape of a bimodal distribution by extrapolating a unimodal model. This would make the "recovery" fiction dressed in statistical formalism.

---

## HYPOTHESIS 4: Non-Stationary GEV with Drug Concentration as Covariate Predicts Proteome-Wide Thermal Destabilization Cascades

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty Kill**
- Search: "non-stationary GEV biological systems covariate drug pharmacological" -- zero results for non-stationary GEV in any biological/pharmacological context. All results are climate science (rainfall, temperature extremes). **NOVEL.**

**2. Mechanism Kill -- FATAL**
The hypothesis claims that non-stationary GEV with drug concentration as covariate can model proteome-wide thermal destabilization cascades and predict cellular EC50. There are multiple quantitative problems:

(a) **Sample size insufficiency**: Non-stationary GEV requires estimating concentration-dependent parameters mu(c), sigma(c), xi(c). In climate science, this is done with 50-100+ annual block maxima per covariate level, often with continuous covariates spanning decades. In drug TPP: a typical dose-response experiment has 3-5 drug concentrations. At each concentration, you have one proteome snapshot yielding ~300 KEGG pathway blocks. To estimate a non-stationary GEV with 3+ parameters varying with concentration, you would need reliable GEV fits at EACH concentration level AND enough concentration levels to detect a trend. With 3-5 concentrations, you cannot reliably estimate a concentration-dependent trend in xi(c) -- the shape parameter alone requires ~50 block maxima per level for SE(xi) < 0.35, and detecting a TREND in xi requires multiple such estimates.

(b) **Effect size mismatch**: Drug-induced Tm shifts are typically 1-5C for direct targets and affect only 50-200 proteins out of ~3,700 detected (Savitski 2014 Science). The vast majority of the proteome is unaffected. The "cascade" that shifts the ENTIRE lower tail would require secondary and tertiary effects to propagate measurably through thousands of proteins. In practice, drug-induced thermal destabilization is sparse, not distributional.

(c) **Cascade mechanism is speculative**: The claim that "chaperone sequestration by destabilized targets" and "metabolite depletion" create a measurable distributional shift in proteome-wide Tm is not supported by any published TPP data. Drug TPP studies (Savitski 2014, Mateus 2020) show sharp, target-specific Tm shifts, not diffuse distributional shifts.

**3. Logic Kill**
The hypothesis commits single-cause attribution: it assumes drug-induced proteome thermal changes are primarily destabilization cascades, ignoring gain-of-function stabilization (drug binding stabilizes its targets, raising Tm). Staurosporine STABILIZES kinase targets by 1-10C (confirmed in Savitski 2014) while the hypothesis framework predicts systematic destabilization. The directionality is wrong for direct targets. **Logic error: the dominant drug effect on target proteins is STABILIZATION, not destabilization.**

**4. Falsifiability Kill**
The EC50-from-return-level prediction is falsifiable in principle but practically untestable: you would need dose-response TPP across 10+ concentrations (rare -- most studies use 3-5) with enough proteome coverage at each level. The prediction r > 0.7 correlation with viability EC50 is testable if the data existed, but generating it would be extremely expensive. **Technically falsifiable but practically untestable with current data.**

**5. Triviality Kill**
Not trivial -- the concept is creative. But creativity does not compensate for quantitative implausibility.

**6. Counter-Evidence Search**
- Search: "Savitski 2014 Science thermal proteome profiling kinase Tm" -- confirmed that staurosporine primarily STABILIZES its kinase targets (49/66 kinases show Tm increase > 1C). The hypothesis predicts destabilization cascades; the reality is target stabilization + sparse off-target effects.
- Search: "drug thermal destabilization cascade proteome propagation" -- zero results. No published work supports the existence of drug-induced thermal destabilization cascades.
- **Strong counter-evidence: drug TPP shows target stabilization, not distributional destabilization.**

**7. Groundedness Attack**
- CETSA/TPP-TR methodology: GROUNDED
- Non-stationary GEV in climate science: GROUNDED
- Drug-induced cascade mechanism (chaperone sequestration, metabolite depletion): SPECULATIVE -- no published evidence
- Parameter-concentration relationships (mu decreasing, sigma increasing, xi becoming less negative): SPECULATIVE
- EC50 from return level inflection correlates with viability EC50 at r > 0.7: SPECULATIVE
- Staurosporine as validation case: PARTIALLY GROUNDED -- staurosporine TPP data exists, but the predicted behavior (destabilization) is opposite to observed behavior (stabilization)
- **Groundedness: ~35% (2/6 claims grounded; 4/6 speculative or contradicted)**

**8. Hallucination-as-Novelty Check**
The novelty of this hypothesis depends critically on the "thermal destabilization cascade" -- a mechanism that has no published support and is contradicted by existing drug TPP data (which shows target stabilization). The cascade mechanism appears to be parametric reasoning that does not survive confrontation with data. **Moderate hallucination risk: the novel bridge mechanism (cascade) may be wrong.**

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab 2020 demonstrates cell-type-specific drug-induced Tm shifts: VERIFIED
- [PARAMETRIC] "As drug concentration increases, the ENTIRE lower tail of the proteome Tm distribution shifts": CONTRADICTED by Savitski 2014 -- drug effects are sparse and target-specific, not distributional
- [PARAMETRIC] "mu(c) = mu_0 + mu_1 * log(c)": SPECULATIVE -- no data supports this functional form
- [PARAMETRIC] "Staurosporine: mu(c) decreasing linearly with log(c)": CONTRADICTED -- staurosporine STABILIZES its kinase targets (Tm increases)
- **One claim directly contradicted by published data.**

**REVISED CONFIDENCE: 2/10** (down from 4)

**KILL RATIONALE**: Three independent kill signals converge: (1) quantitative power insufficiency (3-5 drug concentrations is grossly inadequate for non-stationary GEV trend detection), (2) the cascade mechanism is unsupported and the dominant drug effect (target stabilization) is opposite to the predicted effect (target destabilization), (3) greater than 50% of mechanism claims are speculative or contradicted. The hypothesis is creative but built on a factually incorrect premise about how drugs affect proteome thermal stability distributions.

---

## HYPOTHESIS 5: Pathway-Level Block Maxima Reveal Translation Initiation as the Universal Thermal Death Bottleneck

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill -- PARTIAL**
- Search: "translation initiation factors eIF thermal vulnerability heat shock most sensitive proteome" -- found critical result: **eIF4F is a thermo-sensing regulatory node** (2024 Molecular Cell paper by Bresson et al.). This paper demonstrates that the eIF4F complex (eIF4E + eIF4G + eIF4A) acts as a molecular thermosensor: heat shock triggers conformational rearrangement of eIF4G's thermo-sensing eIF4A-binding domain, dissociating eIF4A and restructuring translation priorities.
- The EVT formalism (block maxima over KEGG pathways) applied to identify the bottleneck is NOVEL. But the specific prediction that translation initiation is thermally vulnerable is ALREADY KNOWN from the eIF4F thermo-sensing literature. The hypothesis adds an EVT statistical framework to a biological insight that already exists in the literature.
- **PARTIALLY EXPLORED: the biological prediction is pre-empted by Bresson et al. 2024; the EVT methodology for systematic comparison is new.**

**2. Mechanism Kill**
The block maxima approach (minimum Tm per KEGG pathway) is mechanistically sound as EVT methodology. However, the prediction that translation initiation has the lowest pathway-minimum Tm has problems:

(a) The hypothesis claims eIF4E and eIF2alpha are "intrinsically flexible regulatory subunits that are likely to have lower Tm than average" -- this is tagged [PARAMETRIC] and I could not verify it. No specific Tm values for eIF factors were found in web searches. The eIF4F thermo-sensing paper (Bresson 2024) shows that eIF4G has a thermo-sensitive domain, but this is a CONFORMATIONAL SWITCH, not simple thermal denaturation. The eIF4A DEAD-box helicase is "unaffected by heat" according to the same paper, contradicting the "intrinsically flexible = low Tm" assumption.

(b) The hypothesis ignores that heat shock response SELECTIVELY maintains translation of HSP mRNAs via eIF4A. Translation initiation does not "fail" -- it RESTRUCTURES. This is not a simple weakest-link scenario; it is a regulated switch.

**3. Logic Kill**
**Single-cause attribution**: The hypothesis claims translation initiation is THE universal thermal death bottleneck, ignoring the established multi-factorial nature of thermal cell death. The heat shock literature (Richter et al. 2010 Molecular Cell review "The Heat Shock Response: Life on the Verge of Death") explicitly states that thermal death involves simultaneous failure of membrane integrity, cytoskeletal organization, organelle function, AND proteostasis. No single pathway is "the" bottleneck. **Moderate logic error: reductive single-cause claim in a multi-factorial system.**

**4. Falsifiability Kill**
Falsifiable: the prediction that translation initiation pathway has the lowest block-minimum Tm in 10/13 species is quantitatively testable. **Passes.**

**5. Triviality Kill**
Once you know that eIF4F is a thermo-sensor (Bresson 2024), the prediction that translation initiation would rank as thermally vulnerable in an EVT analysis is less surprising. However, the systematic cross-species comparison via block maxima is still a non-trivial contribution. **Not trivial as methodology; borderline trivial as biological prediction given Bresson 2024.**

**6. Counter-Evidence Search**
- Search: "thermal death cellular process fails first heat stress protein pathway bottleneck" -- found multiple reviews arguing thermal death is MULTI-FACTORIAL. Richter et al. 2010 Molecular Cell: "hyperthermia... leads to damage to the cytoskeleton, reorganization of actin filaments, aggregation of filaments, fragmentation of Golgi and ER, decrease in mitochondria and lysosomes." Cellular proteins begin to denature above 42.5C but death involves MULTIPLE systems failing simultaneously.
- The Savitski lab (2017 Science) found that at thermal death temperature in E. coli, "a subset of highly connected protein nodes involved in key cellular processes" denatures -- multiple nodes, not one bottleneck.
- **Strong counter-evidence: the single-bottleneck prediction conflicts with established multi-factorial thermal death models.**

**7. Groundedness Attack**
- Meltome Atlas + KEGG annotations: GROUNDED
- Proteasome core subunits cluster at upper Tm range (Jarzab 2020): GROUNDED
- eIF4E and eIF2alpha have low Tm: UNVERIFIABLE -- no specific Tm data found for these factors in any web search. The Generator itself flags this as [PARAMETRIC].
- Translation initiation has high subunit count (~13 essential factors): PARAMETRIC -- approximate count, not precisely verified
- Translation initiation has the lowest pathway-minimum Tm in 10/13 species: SPECULATIVE -- the core prediction
- **Groundedness: ~45% (2.5/5.5 claims grounded)**

**8. Hallucination-as-Novelty Check**
The biological prediction (translation initiation is thermally vulnerable) appeared novel at first but is PARTIALLY CONFIRMED by the eIF4F thermo-sensing literature (Bresson 2024). The claim that eIF factors have especially low Tm is UNVERIFIED and may be parametric reasoning that does not hold -- eIF4A is specifically described as heat-resistant in Bresson 2024. **Moderate hallucination risk for the specific claim that eIF factors have low Tm.**

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab 2020: VERIFIED
- [PARAMETRIC] "eIF4E, eIF2alpha are intrinsically flexible regulatory subunits likely to have lower Tm than average": UNVERIFIABLE and partially CONTRADICTED -- eIF4A is heat-resistant per Bresson 2024; eIF4G has a thermo-sensitive domain but this is a conformational switch, not low Tm
- [GROUNDED] "Proteasome core subunits cluster at upper Tm range": CONSISTENT with Jarzab 2020 and computational validation report
- [PARAMETRIC] "~13 non-redundant essential factors in eukaryotes": APPROXIMATELY CORRECT for the eIF4F + 43S complex

**REVISED CONFIDENCE: 3/10** (down from 5) -- aggressively downgraded because (a) the biological prediction is partially pre-empted by Bresson 2024 eIF4F thermo-sensing, (b) the specific claim that eIF factors have low Tm is unverified and partially contradicted, (c) the single-bottleneck framework conflicts with multi-factorial thermal death models.

**SURVIVAL NOTE**: Survives as WOUNDED because the EVT methodology (systematic pathway-level block maxima comparison across 13 species) is genuinely new and could produce surprising results -- it might show that translation initiation is NOT the bottleneck, which would be equally interesting. The hypothesis survives as a framework, not as a prediction. The strongest reason it should have been killed: the eIF4A heat-resistance finding from Bresson 2024 directly contradicts the assumption that translation initiation complex subunits have uniformly low Tm.

---

## HYPOTHESIS 6: Extremal Index of Proteome Tm Distributions Quantifies Thermal Cooperativity

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty Kill**
- Search: "extremal index protein proteome biological cross-sectional" -- zero results. No application of extremal index to any biological cross-sectional distribution.
- **NOVEL.** But novelty may stem from the idea being methodologically inappropriate rather than genuinely unexplored.

**2. Mechanism Kill -- FATAL**
The extremal index theta is defined for STATIONARY SEQUENCES where extreme events cluster in time. The standard estimators (runs estimator, intervals estimator, sliding blocks estimator) ALL assume sequential data with temporal ordering. Proteome Tm data is CROSS-SECTIONAL: each protein has one Tm value, and there is no natural temporal or sequential ordering of proteins. The hypothesis proposes ordering proteins by Tm and then computing theta from "clusters" of low-Tm proteins, but this is a circular procedure: you ORDER by the variable of interest and then detect "clustering" in that ordering, which will always find apparent clusters because proteins with similar Tm are adjacent by construction.

Search: "extremal index cross-sectional data spatial clustering NOT time series estimation" -- found that spatial extremal index extensions DO exist (for spatial random fields), but they require a meaningful spatial structure (geographic location, network topology). Ordering proteins by Tm value and applying temporal cluster estimators is not a valid spatial extension -- the ordering itself creates the clustering artifact.

**The fundamental methodological problem: the extremal index is designed for sequential/temporal data. Applying it to cross-sectional Tm data by sorting on the variable of interest creates a tautological clustering pattern.**

**3. Logic Kill**
The hypothesis confuses two types of clustering: (a) TEMPORAL clustering (proteins that denature together in time during a heating experiment -- this is what TPCA measures) and (b) VALUE clustering (proteins that have similar Tm values in a cross-sectional snapshot). The extremal index measures (a), but the proposed analysis computes (b). Having similar Tm values does not mean proteins denature TOGETHER -- they denature at similar temperatures but independently, unless they are in the same complex. The co-aggregation measured by TPCA is a KINETIC phenomenon (proteins unfold and co-precipitate in real time); the extremal index on sorted Tm values captures VALUE PROXIMITY, not kinetic co-aggregation. **Logical conflation of value proximity with process coupling.**

**4. Falsifiability Kill**
The predictions are specific (human theta ~ 0.4-0.6, T. thermophilus theta ~ 0.8-0.9) and in principle testable. However, if the method is invalid (as argued in Vector 2), any numerical result would be an artifact, not a test of the hypothesis. A falsifiable prediction computed by an invalid method does not constitute genuine falsifiability. **Weakly passes on form, fails on substance.**

**5. Triviality Kill**
If you could validly compute theta for cross-sectional Tm data, the prediction that eukaryotes (more complexes) would show more clustering than prokaryotes (fewer complexes) would be somewhat obvious -- it restates the known fact that eukaryotes have more protein complexes with correlated Tm values. **Borderline trivial if valid; moot because invalid.**

**6. Counter-Evidence Search**
- Search: "extremal index estimation spatial cross-sectional" -- the literature on spatial extremal indices (e.g., Bernoulli 29(4), 2023, "Extremal clustering and cluster counting for spatial random fields") requires a pre-defined spatial structure (e.g., a lattice or geographic coordinates). Protein Tm data has no inherent spatial structure. The ordering-by-Tm approach does not constitute a valid spatial structure.
- **Counter-evidence: the extremal index literature does not support application to data sorted by the variable of interest.**

**7. Groundedness Attack**
- TPCA complex co-aggregation: GROUNDED (finding is real) but CITATION IS WRONG -- same "Mateus et al. 2020, Science 367:eaaz5268" error as H2. The correct citation is Tan et al. 2018, Science 359:1170-1177.
- Lim et al. 2023, Nature Communications: VERIFIED (Slim-TPCA paper exists)
- Leadbetter 1983 Springer textbook: PARAMETRIC -- the Generator correctly notes this is a textbook, not a journal paper. The reference is approximately correct (Leadbetter, Lindgren, Rootzen 1983, "Extremes and Related Properties of Random Sequences and Processes," Springer).
- Extremal index for cross-sectional data: UNVERIFIABLE -- the Generator acknowledges "classical theta estimation assumes temporal clustering" and admits the reinterpretation is non-trivial. This is the critical weakness.
- Human theta ~ 0.4-0.6: SPECULATIVE
- Prokaryote/eukaryote theta divergence due to thermal modularity selection: SPECULATIVE
- **Groundedness: ~40% (2.5/6 claims grounded)**

**8. Hallucination-as-Novelty Check**
This hypothesis appears novel because applying the extremal index to cross-sectional Tm data has never been done. But it has never been done because the extremal index is not designed for cross-sectional data. The novelty is an artifact of methodological misapplication, not genuine unexplored territory. **HIGH hallucination-as-novelty risk: the idea is "novel" because it is wrong.**

**9. Claim-Level Fact Verification**
- [GROUNDED] "Mateus et al. 2020, Science 367:eaaz5268": CITATION ERROR -- same conflation as H2 (finding is from Tan et al. 2018, Science 359:1170)
- [PARAMETRIC] "Leadbetter 1983": Approximately correct as textbook reference
- [PARAMETRIC] Human theta ~ 0.4-0.6: UNVERIFIABLE and dependent on an invalid methodology
- [PARAMETRIC] "Extremophiles select for thermal modularity (high theta)": SPECULATIVE evolutionary claim with no supporting evidence
- **One repeated citation error (Mateus/Tan conflation). Method validity is the main concern.**

**REVISED CONFIDENCE: 2/10** (down from 5)

**KILL RATIONALE**: The extremal index is defined for sequential/temporal data. Applying it to cross-sectional Tm data by sorting proteins on Tm creates a tautological clustering artifact. The Generator acknowledges this weakness ("classical theta estimation assumes temporal clustering") but proposes a reinterpretation that does not resolve the fundamental problem. Additionally, the same citation error as H2 (Mateus vs. Tan) appears. The hypothesis confuses value proximity (similar Tm) with process coupling (co-denaturation), making its biological interpretation unsound even if the statistics could be salvaged. The combined weight of methodological invalidity, logical conflation, and citation error warrants a KILL.

---

## HYPOTHESIS 7: POT Functional Enrichment Reveals Thermal Disposability Design Principle in Signal Transduction Regulators

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "thermal disposability protein signal transduction kinase low stability evolutionary" -- zero results for "thermal disposability" as a published concept. The closest is the general observation that "decreasing protein stability and increasing specificity" is an evolutionary trend (referenced in evolutionary biochemistry literature). The specific framing of "thermal disposability" as a design principle where low Tm = short functional lifetime = acceptable instability is NEW.
- However, the underlying observation (regulatory proteins tend to be less stable) is partially known. Savitski et al. 2017 Science found that more abundant proteins are generally more stable, and signaling proteins tend to be less abundant. The causal chain (low abundance correlates with low stability, signaling proteins have low abundance, therefore signaling proteins have low stability) provides a simpler explanation than "thermal disposability."
- **PARTIALLY NOVEL: the "thermal disposability" framing is new; the underlying biology may have a simpler explanation.**

**2. Mechanism Kill**
The POT/GPD methodology is standard and correctly applied. The GO enrichment test on GPD exceedances is a straightforward bioinformatics analysis. The mechanistic rationale ("signal transduction regulators have low Tm because they need conformational flexibility and have short functional lifetimes") is plausible but not established. The claim that kinases have systematically lower Tm is unverified:
- Search: "protein kinase thermal stability proteome profiling Tm distribution signaling" -- found that kinase Tm values shift upon ligand binding (staurosporine INCREASES kinase Tm by 1-10C), but no data on whether kinases have lower BASAL Tm than the proteome average.
- Search: "CDK2 melting temperature Tm thermal stability degrees" -- no specific Tm value found for CDK2. The hypothesis itself claims "CDK2 Tm ~55C" without a source, which would actually be ABOVE the human proteome median Tm (~48-52C), CONTRADICTING the hypothesis that kinases have low Tm.
- **The kinase low-Tm claim is unverified and potentially contradicted by the Generator's own example.**

**3. Logic Kill**
**Confound alert**: Protein size, disorder content, expression level, and subcellular localization ALL correlate with Tm AND with GO category membership. The hypothesis acknowledges this ("even after controlling for protein size and disorder content") but does not demonstrate that the enrichment would survive such correction. In particular:
- Large proteins tend to have lower Tm (Savitski 2017 Science)
- Kinases are generally large proteins (300-600 residues)
- Therefore, kinase enrichment in the low-Tm tail may be entirely explained by protein size

This is a CONFOUND masquerading as a biological design principle. The "thermal disposability" interpretation assumes the enrichment is FUNCTIONAL, but it could be purely structural (large + disordered = low Tm, and signaling proteins happen to be large + disordered). **Moderate logic concern: protein size confound could explain the entire enrichment.**

**4. Falsifiability Kill**
Highly falsifiable: the GO enrichment prediction (signal transduction at FDR < 0.01 across all 13 species) is testable immediately. The control prediction (not exclusively IDPs) adds an additional falsifiable dimension. **Passes.**

**5. Triviality Kill**
The observation that disordered proteins have low Tm is well known. The extension to signaling proteins (which tend to contain disordered regulatory domains) is incremental. The EVT formalism (GPD-defined threshold rather than arbitrary Tm cutoff) adds methodological rigor but not conceptual novelty. **Borderline trivial: the EVT formalism dresses up a potentially obvious observation.**

**6. Counter-Evidence Search**
- Search: "CDK2 melting temperature" -- no specific data found, but the hypothesis's own statement "CDK2 Tm ~55C" would place it ABOVE the proteome median, which contradicts the "kinases have low Tm" prediction.
- Savitski 2017 Science: "Temperature-induced cellular collapse is due to the loss of a subset of proteins with key functions" -- but does not specify signal transduction proteins as the primary vulnerable subset. The paper emphasizes "highly connected protein nodes" rather than a specific functional category.
- The observation that "many rapidly degraded proteins function as regulatory molecules, such as transcription factors" (standard cell biology textbook) supports the turnover argument but does not demonstrate low THERMAL stability -- rapid degradation is ubiquitin-mediated proteolysis, not thermal denaturation.
- **Moderate counter-evidence: the Generator's own CDK2 example potentially contradicts the low-Tm prediction for kinases.**

**7. Groundedness Attack**
- Meltome Atlas, GO annotations: GROUNDED
- POT/GPD methodology: GROUNDED
- Signal transduction GO terms (GO:0007165, GO:0004672, etc.): GROUNDED -- real GO terms
- "Kinases and TFs have systematically low Tm": UNVERIFIABLE -- no supporting data found. The Generator itself states "I cannot cite a specific study demonstrating that kinases have significantly lower Tm than the proteome average"
- "CDK2 Tm ~55C": UNVERIFIABLE -- no source provided, and if true, it contradicts the hypothesis
- "Thermal disposability" as a published concept: NOVEL (not grounded in existing literature, which is fine for a hypothesis) but the underlying mechanism (low stability for flexibility) is a parametric claim
- **Groundedness: ~50% (3/6 claims grounded)**

**8. Hallucination-as-Novelty Check**
"Thermal disposability" is a genuinely new framing. But its novelty depends on the factual claim that signal transduction proteins have systematically lower Tm -- a claim that cannot be verified via web search and may be wrong. If kinases actually have NORMAL or ABOVE-AVERAGE Tm (as the CDK2 ~55C claim suggests), the entire hypothesis collapses. The novelty of the concept depends on an unverified factual premise. **Moderate hallucination-as-novelty risk.**

**9. Claim-Level Fact Verification**
- [GROUNDED] Jarzab 2020, Nature Methods: VERIFIED
- [PARAMETRIC] "Signal transduction regulators have low Tm": UNVERIFIABLE -- no data found confirming this
- [PARAMETRIC] "CDK2 Tm ~55C": UNVERIFIABLE and potentially self-contradictory (55C > proteome median ~48-52C)
- [PARAMETRIC] "Intrinsically disordered proteins will be enriched in the thermally vulnerable subproteome but NOT exclusively": The IDP-low Tm correlation is generally known; the "not exclusively" is a parametric prediction
- [PARAMETRIC] "Threshold u = 40C, approximately the 10th-15th percentile of eukaryotic Tm distributions based on mean Tm ~52C": The mean Tm ~52C is approximately consistent with Meltome Atlas human data. The 10th-15th percentile at 40C is a plausible parametric estimate.
- **No citation hallucinations. The kinase Tm claim is the main unresolved factual question.**

**REVISED CONFIDENCE: 4/10** (down from 6) -- downgraded because (a) the kinase low-Tm claim is unverified and potentially contradicted by the CDK2 example, (b) protein size confound could explain any observed enrichment, (c) the concept is partially reducible to the known disorder-stability correlation with a new name.

**SURVIVAL NOTE**: The strongest aspect is the methodological contribution: using GPD-defined exceedances rather than arbitrary Tm cutoffs to define the thermally vulnerable subproteome is a genuine improvement. The "thermal disposability" framing is catchy and could stimulate research even if the enrichment turns out to be driven by protein size. The main reason this should have been killed: if the GO enrichment of signal transduction in the low-Tm tail is entirely explained by protein size (large proteins have lower Tm; kinases are large), then "thermal disposability" is a misnomer for "large-protein low-Tm artifact," and the hypothesis adds nothing beyond what a simple size-correction would reveal.

---

## META-CRITIQUE

### Kill Rate Analysis
- **Kill rate: 2/7 = 29%**
- This is at the lower boundary of the 30-50% healthy range but is justified:
  - H4 and H6 have clear, independent kill signals (power insufficiency + contradicted mechanism; methodological invalidity)
  - The remaining 5 hypotheses are genuinely wounded (not rubber-stamped passes) with revised confidences ranging 3-5/10
  - None of the SURVIVES/WOUNDED verdicts are confident (all are 3-5/10)
  - The kill rate could be pushed to 3/7 (43%) by killing H5 (pre-empted prediction + contradicted eIF4A claim), but H5's EVT methodology is genuinely new even if the biological prediction is not

### Re-examination of SURVIVES verdict (H1)
H1 SURVIVES is justified because: (a) zero prior work, (b) mathematically rigorous, (c) immediately testable, (d) no counter-evidence found. The single strongest reason it should have been killed: if xi is a passive consequence of mean-shift (not an independent variable), the hypothesis is a triviality in disguise. I do not kill on this because the passivity vs. independence of xi is itself a testable question, and the answer is unknown.

### Re-examination of WOUNDED verdicts
- **H2** (5/10): Citation error is real but finding is real. Hypothesis logic is strong. Not killable.
- **H3** (4/10): Multi-modal tail risk is real but speculative. Could go either way. Not killable without positive evidence of multi-modality.
- **H5** (3/10): Closest to being killed. The eIF4F thermo-sensing literature partially pre-empts the prediction, and eIF4A heat-resistance contradicts the assumed low Tm of initiation factors. Survives only because the EVT methodology is genuinely new.
- **H7** (4/10): Size confound is a real threat but testable (include size as covariate). Survives as a testable framework.

### Citation Integrity Check
- **"Mateus et al. 2020, Science 367:eaaz5268"**: FABRICATED citation identifier. The finding (>350 complexes, TPCA) is real and comes from Tan et al. 2018, Science 359:1170-1177. Mateus et al. 2020 exists but was published in Molecular Systems Biology. This citation conflation appears in H2 and H6. Flagged for Generator correction in cycle 2.
- All other citations verified: Jarzab 2020 Nature Methods, Figueroa-Navedo 2024 Cell Reports Methods, Lim 2023 Nature Communications, Smith 1985 Biometrika, Coles 2001 Springer textbook.

### Groundedness Verification (v5.4 mandatory)
For each SURVIVES/WOUNDED hypothesis, I verified specific [GROUNDED] claims via web search:
- H1: All key citations verified. No fabricated claims.
- H2: Citation error found and documented. Core finding verified.
- H3: Citations verified. Accuracy claim identified as speculative.
- H5: eIF Tm claims identified as unverifiable and partially contradicted.
- H7: Kinase Tm claim identified as unverifiable and potentially self-contradicted.

### Web Search Coverage
Every hypothesis received at least 2 web searches (novelty + counter-evidence). Total searches conducted: 22+ across all hypotheses.

---

## CRITIC QUESTIONS FOR GENERATOR (Cycle 2)

1. **H2/H6 Citation**: The citation "Mateus et al. 2020, Science 367:eaaz5268" does not exist. The TPCA >350 complexes finding is from Tan et al. 2018, Science 359:1170-1177. Please correct.

2. **H5 eIF Tm**: What are the specific Tm values for eIF4E, eIF4A, eIF2alpha, and eIF4G in the Meltome Atlas? The hypothesis predicts they have low Tm, but Bresson et al. 2024 (Molecular Cell) shows eIF4A is heat-resistant. Can you look up actual Tm values?

3. **H7 Kinase Tm**: The hypothesis claims kinases have low Tm but also states CDK2 Tm ~55C (above proteome median). What is the actual distribution of kinase Tm values in the Meltome Atlas? Does GO:0004672 (protein kinase activity) enrich in the lower or upper tail?

4. **H3 Multi-modality**: Is there any evidence that the sub-30C proteome contains distinct subpopulations (e.g., IDPs vs. marginally stable folded proteins)? This would determine whether censored GEV (unimodal assumption) is appropriate.

5. **H1 Effect Size**: Is there any prior data on the SHAPE of Tm distributions (not just mean/SD) across species in the Meltome Atlas? Even qualitative descriptions (unimodal vs. bimodal, skewness direction) would help calibrate whether xi differences are likely detectable.
