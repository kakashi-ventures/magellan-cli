# Ranked Hypotheses — Cycle 1
## Session: 2026-03-27-scout-013
## Target: Extreme Value Statistics x Proteome-wide Thermal Stability Distributions
## Ranker Agent | Model: sonnet-4.6 | Date: 2026-03-27

---

## Scoring Methodology

- **6 fixed dimensions** with canonical weights (Novelty 20%, Mechanistic Specificity 20%, Cross-field Distance 10%, Testability 20%, Impact Paradigm 5%, Impact Translational 5%, Groundedness 20%)
- **Cross-domain bonus**: All 5 surviving hypotheses bridge extreme value statistics / reliability engineering (mathematics) → proteomics / evolutionary biology (life sciences), spanning 2+ disciplinary boundaries. +0.5 applied to all composites after weighted average.
- **Input**: Critic-reviewed hypotheses with web-searched novelty verdicts, claim-level groundedness assessments, and revised confidence scores.

---

## Per-Hypothesis Scoring Tables

### Hypothesis H1: GEV Tail Index (xi) as Phylogenomic Signature of Thermal Adaptation Strategy

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic's web searches across 3 targeted queries returned zero results connecting GEV shape parameter estimation to cross-species proteome Tm distributions. The tail-sculpting vs. mean-shift framing is genuinely new to the field. This is the strongest novelty signal in the set: even the closest adjacent work (thermal adaptation by amino acid composition) does not examine distributional shape. |
| Mechanistic Specificity | 20% | 8 | Names the specific theorem (FTG), the specific data source (Meltome Atlas, 13 species, accession PXD011929), the specific operation (block minima over ~300 KEGG pathways), the specific parameter (xi), the specific prediction direction (xi_thermophile < xi_mesophile < xi_psychrophile), and provides quantified statistical power (SE(xi) ~ 0.029 at n=5,000-7,000). One gap: the expected magnitude of inter-species xi differences is entirely unknown, which prevents a pre-registered effect size estimate. |
| Cross-field Distance | 10% | 8 | GEV shape parameter analysis originates in mathematical statistics / actuarial / climate engineering. Phylogenomic thermal adaptation is a sub-field of evolutionary proteomics. These communities use different mathematical vocabularies, publish in different journals (Journal of Applied Statistics vs. Molecular Biology and Evolution), and share almost no methodological overlap. |
| Testability | 20% | 9 | Fully executable on public data (Meltome Atlas, PRIDE PXD011929) with standard GEV fitting packages (R `extRemes`, Python `pyextremes`). No wet-lab work required for initial test. A PhD student with R skills could complete the analysis in 4-6 weeks. The null result (xi constant across OGT levels) is as informative as a positive result. The only constraint is the small number of true thermophiles (1-2 of 13 species), but this is a power concern, not a feasibility concern. |
| Impact: Paradigm | 5% | 7 | If confirmed, this reframes 50 years of thermal adaptation research from a mean-centric to a distributional-shape paradigm. It would open a new subfield (EVT-based proteome evolution) and provide a universal classifier for thermal adaptation strategy applicable to any species with proteome Tm data. The main reason this is not a 9-10: it could be a methodological observation that does not change biological understanding of the mechanisms of thermal adaptation. |
| Impact: Translational | 5% | 4 | Translational impact is indirect. Knowing that thermophiles sculpt their lower tail could inspire protein engineering approaches that eliminate thermal outliers rather than uniformly raising stability. No direct drug target or diagnostic follows from the hypothesis as stated. Some relevance to industrial enzyme design and synthetic biology. |
| Groundedness | 20% | 7 | Critic assessed ~70% of claims as grounded or verifiable. Confirmed: Jarzab 2020 Nature Methods (DOI verified), FTG theorem (standard mathematics), ~300 KEGG pathways per species (computational validation), SE(xi) ~ 0.029 (computational validation). Speculative: non-linear xi-OGT relationship (no basis provided). Parametric: Coles 2001 "25 block minimum" (standard EVT practice recommends 50+, satisfied by 300 pathways regardless). No citation hallucinations detected. |
| **Composite** | | **7.95** | Weighted average before bonus. |
| **Cross-domain bonus** | | **+0.5** | Statistics → evolutionary proteomics: 2+ disciplinary boundaries confirmed. |
| **Final Composite** | | **8.45** | |

---

### Hypothesis H2: Complex-Minimum Tm via POT Identifies Thermal Bottleneck Complexes

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed zero prior work applying POT/GPD to complex-minimum Tm distributions. The informal "weakest subunit" concept exists in the TPCA literature (Jarzab 2020 mentions proteasome subunit Tm heterogeneity) but has never been formalized via EVT return levels. The cross-species conservation prediction (same bottleneck complexes appearing across organisms) is a specifically novel biological question. |
| Mechanistic Specificity | 20% | 8 | Mechanism is layered and concrete: names the EVT method (GPD/POT, threshold u=45C), the biological aggregation (complex-minimum Tm = Tm_min per complex), the statistical output (return levels with CIs), the independence restoration argument (inter-complex independence once one value per complex), the specific predicted complexes (spliceosome, proteasome regulators, ribosome assembly factors), and the validation database (CORUM). The in-complex stabilization caveat is clearly articulated as a known limitation. |
| Cross-field Distance | 10% | 8 | Structural reliability engineering (weakest-link analysis, first-failure statistics) applied to protein complex network biology. These communities share almost no overlap; the bridge via POT/return-levels is the specific contribution. |
| Testability | 20% | 9 | Immediately executable on Meltome Atlas + CORUM (human) + KEGG (yeast, E. coli). The prediction about conserved bottleneck complexes is directly falsifiable by running GPD fits on existing data. Cross-species scope is limited for non-human organisms (sparse complex annotations), but human + yeast analysis alone constitutes a strong test. Standard bioinformatics pipeline, no new techniques required. |
| Impact: Paradigm | 5% | 7 | Introduces return-level language into cell biology ("the temperature at which p% of essential complexes begin to fail"). This is a significant conceptual advance: it converts the informal question "which complex is the thermal bottleneck?" into a statistically rigorous, quantitative answer with confidence intervals. Could change how researchers design heat stress experiments. |
| Impact: Translational | 5% | 6 | Identifying the thermally critical bottleneck complexes has direct applications: (a) engineering thermostable cell lines for bioproduction, (b) predicting which complexes to stabilize pharmacologically during fever or hyperthermia cancer treatment, (c) understanding why certain organisms are heat-sensitive. More tractable translational pathway than H1. |
| Groundedness | 20% | 6 | ~65% grounded per Critic. Confirmed: Jarzab 2020 (Meltome Atlas), Lim 2023 Nature Communications (Slim-TPCA), CORUM database, proteasome regulatory subunits at lower Tm (Jarzab 2020), GPD/POT methodology. Critical issue: the citation "Mateus et al. 2020, Science 367:eaaz5268" is a fabricated journal-volume-article-ID combination — the finding (>350 human complexes with significant TPCA signatures) is real and comes from Tan et al. 2018, Science 359:1170-1177. This is a citation conflation, not a factual fabrication, but it penalizes groundedness. |
| **Composite** | | **7.65** | Weighted average before bonus. |
| **Cross-domain bonus** | | **+0.5** | Reliability engineering → protein complex cell biology: 2+ disciplinary boundaries confirmed. |
| **Final Composite** | | **8.15** | |

---

### Hypothesis H3: Censored GEV Recovers the Invisible 20% Below the TPP Measurement Window

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed zero prior work applying censored GEV to any biological distribution. Censored GEV for flood frequency is well-established in hydrology; the proteomics application is a genuine first. The cross-domain transfer from hydrology to proteomics is the specific novelty. The 20% unmeasured proteome problem is documented, but the statistical solution proposed here is completely new. |
| Mechanistic Specificity | 20% | 6 | Specifies the censored likelihood approach (replacing f(x) with F(c) for censored observations at c=30C), names the data source (Meltome Atlas), outlines the cross-validation (extend TPP to 20C), and makes a quantitative accuracy claim (+/-3%). However, the +/-3% claim is directly borrowed from hydrological performance with no domain-specific justification, and the hypothesis does not propose how to test whether the GEV assumption holds below 30C before extrapolating. The mechanism for WHY the sub-30C tail should be GEV-distributed is assumed rather than argued. |
| Cross-field Distance | 10% | 9 | Flood frequency hydrology → proteomics. These fields share essentially no practitioners, no shared journals, and no shared vocabulary. The mapping from "floods below a gauging threshold" to "proteins below the TPP measurement window" is a structural isomorphism across completely distinct domains. This is the highest cross-field distance in the set. |
| Testability | 20% | 7 | The computational fitting of censored GEV to existing Meltome Atlas data is immediately executable (standard software, existing data). However, the definitive test — extending TPP temperature range downward to 20C to validate predictions — requires experimental work that is technically feasible but non-trivial (cold denaturation artifacts, non-standard TPP protocol). A partial test using existing data alone would be less rigorous. Score reflects this two-stage testability. |
| Impact: Paradigm | 5% | 5 | Primarily a methodological contribution: provides a statistical tool to characterize the unobserved 20% of the proteome. Extends the existing EVT-proteomics framework but does not fundamentally reshape understanding. Impact depends heavily on whether the invisible 20% turns out to contain biologically important proteins (IDPs, key regulators) that change interpretations of thermal vulnerability. |
| Impact: Translational | 5% | 4 | Knowing which proteins have Tm < 30C could guide drug target selection (avoid thermally unstable targets) and improve TPP experimental design. The translational pathway is indirect and depends on the recovered proteins being of pharmaceutical relevance. |
| Groundedness | 20% | 5 | ~50% grounded per Critic. Confirmed: Jarzab 2020 (20% unmeasured proteome), Figueroa-Navedo & Ivanov 2024 Cell Reports Methods (left-censoring as key challenge), Smith 1985 Biometrika (foundational MLE paper, verified as real), censored GEV methodology in hydrology. Speculative/Unverified: +/-3% accuracy prediction (no basis in proteomics domain), cold denaturation creating non-random censoring (real counter-evidence), multi-modal tail risk undermining GEV assumption (real mechanism concern). Two substantive model-assumption risks lower this score. |
| **Composite** | | **6.55** | Weighted average before bonus. |
| **Cross-domain bonus** | | **+0.5** | Hydrology/flood frequency → proteomics: 2+ disciplinary boundaries confirmed. Among the most distant bridges in this session. |
| **Final Composite** | | **7.05** | |

---

### Hypothesis H5: Pathway-Level Block Maxima Reveal Translation Initiation as Universal Thermal Death Bottleneck

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 5 | Dual novelty status: the EVT methodology (pathway-level block minima ranking across 13 species) is genuinely novel — Critic found zero prior work. However, the core biological prediction (translation initiation is thermally vulnerable) is substantially pre-empted by Bresson et al. 2024 Molecular Cell (eIF4F as thermo-sensing regulatory node). The EVT formalism adds rigor to a partially known conclusion rather than generating a fully new biological insight. Score reflects this mixed status. |
| Mechanistic Specificity | 20% | 5 | Names specific pathway (KEGG hsa03013), specific complex (eIF4F: eIF4E + eIF4G + eIF4A, plus 43S), specific prediction (lowest pathway-minimum Tm in 10/13 species at >95% CI), and secondary prediction (lowest inter-species variance in translation initiation). However, the core mechanistic claim — that eIF factors have intrinsically low Tm — is explicitly flagged as parametric, unverifiable, and partially contradicted (eIF4A is heat-resistant per Bresson 2024). This undermines the mechanistic grounding substantially. |
| Cross-field Distance | 10% | 8 | Structural reliability analysis / EVT → molecular cell biology of translation. These communities are distant; the application of block-maxima methodology to identify the thermal death bottleneck pathway is a cross-field contribution. |
| Testability | 20% | 8 | Fully executable on existing data: Meltome Atlas + KEGG pathway annotations. Pathway-level block minima and GEV fitting are standard operations. The prediction (translation initiation has the lowest block-minimum Tm) is directly falsifiable. A negative result (some other pathway ranks lowest) would be equally publishable and informative. |
| Impact: Paradigm | 5% | 6 | If confirmed, provides the first data-driven, statistically rigorous answer to the longstanding question of which cellular process fails first under thermal stress. Even if translation initiation is not the bottleneck, the EVT framework for unbiased pathway-level thermal vulnerability ranking would be a lasting methodological contribution. Partially discounted because Bresson 2024 reduces the surprise of finding translation as the answer. |
| Impact: Translational | 5% | 5 | Identifying the universal thermal death bottleneck pathway is directly relevant to: fever management, hyperthermia cancer treatment, cell line heat tolerance engineering for bioproduction, and understanding heat stroke pathophysiology. The translation initiation prediction, if confirmed, could point to eIF factor stabilization as a therapeutic strategy. |
| Groundedness | 20% | 4 | ~45% grounded per Critic. Confirmed: Jarzab 2020 Meltome Atlas, KEGG annotations, proteasome core subunits at upper Tm range (Jarzab 2020), multi-factorial thermal death counter-evidence (Richter 2010 Mol Cell). Unverified/Contradicted: eIF4E, eIF2alpha low-Tm claim (not found in web search), eIF4A specifically described as heat-resistant (Bresson 2024), ~13 non-redundant eIF factors (approximately correct). One core mechanistic premise is contradicted by published data. |
| **Composite** | | **5.75** | Weighted average before bonus. |
| **Cross-domain bonus** | | **+0.5** | EVT / engineering reliability → cell biology / translation biology: 2+ disciplinary boundaries confirmed. |
| **Final Composite** | | **6.25** | |

---

### Hypothesis H7: POT Functional Enrichment Reveals Thermal Disposability Design Principle

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | "Thermal disposability" as an evolutionary design principle is a genuinely new framing. Critic confirmed zero prior work framing low Tm as an adaptive feature in signal transduction regulators. However, the underlying observation (regulatory/signaling proteins tend to be less stable) is partially known from the protein turnover and conformational flexibility literature. The novelty is in the EVT-based definition of the threshold and the cross-species universality prediction. |
| Mechanistic Specificity | 20% | 6 | Names specific GO terms (GO:0007165, GO:0004672, GO:0004871, GO:0003700), specific threshold (u=40C, 10th-15th percentile), specific statistical test (hypergeometric, FDR < 0.01), and specific control prediction (enrichment not driven exclusively by IDPs). However, the kinase Tm claim is explicitly unverified, and the CDK2 ~55C example cited by the Generator would, if accurate, CONTRADICT the hypothesis (55C > proteome median of ~48-52C). This internal inconsistency penalizes the score. |
| Cross-field Distance | 10% | 8 | Statistical reliability analysis (GPD/POT tail characterization) → evolutionary functional genomics. These are distant fields; the use of EVT-defined exceedances as a biologically principled threshold (instead of arbitrary cutoffs) is the bridge contribution. |
| Testability | 20% | 8 | GO enrichment on GPD exceedances is a fully standard bioinformatics pipeline. Immediately executable on Meltome Atlas with standard tools (R bioconductor, GO enrichment packages). The size-correction control (include protein length as covariate) is also straightforward. Cross-species consistency prediction (enrichment holds in all 13 species) is a strong falsifiability test. One limitation: low-Tm proteins may be systematically underrepresented in the Meltome Atlas. |
| Impact: Paradigm | 5% | 5 | If the enrichment holds after size correction, "thermal disposability" would establish a new category of proteins defined by functional ephemeralness. This extends the existing stability-function framework but is unlikely to open a new field. Impact is contingent on the enrichment not being explainable by the known size/disorder confound. |
| Impact: Translational | 5% | 5 | "Thermally disposable" proteins could be preferential targets for thermal therapies (hyperthermia selectively kills cells by disrupting signaling regulators), or alternatively, stabilizing these proteins could enhance therapeutic protein production. The translational pathway is real but indirect. |
| Groundedness | 20% | 5 | ~50% grounded per Critic. Confirmed: Jarzab 2020 Meltome Atlas, GO annotation databases, GPD/POT methodology, mean Tm ~52C in humans (consistent with Meltome Atlas), Savitski 2017 Science (abundant proteins more stable). Unverified: kinase systematic low-Tm claim (no data found; CDK2 ~55C example is potentially self-contradictory), "thermal disposability" as a published concept (novel, not grounded). The size confound is a real threat to the biological interpretation. |
| **Composite** | | **6.50** | Weighted average before bonus. |
| **Cross-domain bonus** | | **+0.5** | EVT / reliability engineering → evolutionary functional genomics: 2+ disciplinary boundaries confirmed. |
| **Final Composite** | | **7.00** | |

---

## Final Ranking Table

| Rank | H# | Title | Novelty | Mech. Spec. | Cross-field | Testability | Impact Par. | Impact Trans. | Groundedness | Weighted Avg | +Bonus | **Final** |
|------|-----|-------|---------|------------|-------------|-------------|------------|--------------|-------------|-------------|--------|-----------|
| 1 | H1 | GEV Tail Index as Phylogenomic Signature | 9 | 8 | 8 | 9 | 7 | 4 | 7 | 7.95 | +0.5 | **8.45** |
| 2 | H2 | Complex-Minimum Tm via POT | 8 | 8 | 8 | 9 | 7 | 6 | 6 | 7.65 | +0.5 | **8.15** |
| 3 | H3 | Censored GEV Recovers Invisible 20% | 8 | 6 | 9 | 7 | 5 | 4 | 5 | 6.55 | +0.5 | **7.05** |
| 4 | H7 | POT Enrichment: Thermal Disposability | 7 | 6 | 8 | 8 | 5 | 5 | 5 | 6.50 | +0.5 | **7.00** |
| 5 | H5 | Translation Initiation as Thermal Death Bottleneck | 5 | 5 | 8 | 8 | 6 | 5 | 4 | 5.75 | +0.5 | **6.25** |

---

## Diversity Check

**Top 5 evaluated** (all 5 survive, since only 5 remain after 2 kills):

**Pair-by-pair conceptual similarity assessment:**

| Pair | Bridge Mechanism Same? | Subfields Same? | Prediction Type Same? | Similarity Verdict |
|------|----------------------|----------------|----------------------|-------------------|
| H1 vs H2 | No: H1 uses GEV block-minima for phylogenomics; H2 uses POT for complex-level bottleneck detection | No: H1 is evolutionary proteomics; H2 is cell biology / complex networks | No: H1 = cross-species xi distribution; H2 = return-level identification of specific complexes | DISTINCT |
| H1 vs H3 | No: H1 fits full GEV across species; H3 applies censored likelihood to recover unobservable data | No: H1 = evolutionary; H3 = methodological/measurement | No: H1 = phylogenetic signal; H3 = proteome coverage recovery | DISTINCT |
| H1 vs H7 | Partial: both fit GEV-family models to Tm distributions; H7 uses POT/GPD; H1 uses block-minima GEV | No: H1 = evolutionary; H7 = functional enrichment / evolutionary design | No: H1 = species-level comparison; H7 = protein functional category enrichment | SOMEWHAT SIMILAR (share GEV-family fitting to Tm data) |
| H1 vs H5 | No: H1 compares xi across species; H5 ranks KEGG pathways by block-minimum Tm | Partial: both use 13-species Meltome Atlas, both work at pathway/species level | No: H1 = phylogenetic xi pattern; H5 = universal pathway ranking | SOMEWHAT SIMILAR (both use KEGG pathway blocks on Meltome Atlas) |
| H2 vs H3 | No: H2 uses POT on complex Tm_min; H3 uses censored GEV for left-censored tail | No: H2 = cell biology / complex stability; H3 = methodology / proteome coverage | No: H2 = identify bottleneck complexes; H3 = recover unobserved proteins | DISTINCT |
| H2 vs H7 | Partial: both use POT/GPD framework, both identify biologically meaningful subsets | Partial: both work at the protein-population level using GPD exceedances | Partial: both predict functional enrichment of exceedance proteins | SIMILAR (shared POT/GPD mechanism; different biological question) |
| H2 vs H5 | No: H2 = complex-level POT for bottleneck identification; H5 = pathway-level block maxima for bottleneck identification | Partial: both identify thermal bottleneck cellular components | No: H2 = specific bottleneck complexes via return levels; H5 = single pathway via block-minima GEV | SOMEWHAT SIMILAR (both identify thermal bottleneck entities) |
| H3 vs H7 | No: H3 = censored likelihood; H7 = POT/GPD enrichment | No: H3 = proteome coverage recovery; H7 = functional enrichment | No | DISTINCT |
| H3 vs H5 | No | No | No | DISTINCT |
| H7 vs H5 | Partial: both use lower-tail analysis of Tm to make a functional claim | Partial: both work at the protein-function level | Partial: both predict that specific functional categories are enriched in the thermally vulnerable subproteome | SOMEWHAT SIMILAR |

**Convergence assessment:**
- H2 and H7 share the POT/GPD bridge mechanism and both identify functional subsets of the proteome using exceedance-based definitions. This is the most similar pair.
- No cluster of 3+ hypotheses shares the same bridge mechanism, subfields, AND prediction type simultaneously.
- H1, H3, and H5 are all conceptually distinct from each other and from H2/H7.
- The set of 5 covers: (a) phylogenomic tail-shape comparison [H1], (b) complex-level bottleneck identification via return levels [H2], (c) measurement recovery for unobserved tail [H3], (d) functional enrichment of the extreme lower tail [H7], (e) pathway ranking for universal bottleneck identification [H5]. These are 5 distinct scientific questions asked with related but not identical statistical tools.

**Diversity check verdict: NO ADJUSTMENT NEEDED.** Although H2 and H7 share the POT/GPD mechanism, they ask fundamentally different biological questions (which specific complexes fail vs. which functional categories are overrepresented in the vulnerable tail). No 3+ cluster of conceptually identical hypotheses exists. The ranking stands as computed.

---

## Elo Tournament Sanity Check

**15 pairwise comparisons on top 5 (all hypotheses included since only 5 survive):**

**1. H1 vs H2**: A domain researcher would want to test H2 first. H2 is immediately executable with existing Meltome Atlas + CORUM data, produces a directly interpretable biological output (specific bottleneck complexes), and has a cleaner mechanistic prediction. H1 requires interpreting xi differences that may be below detection threshold given only 1-2 thermophiles. **Winner: H2**

**2. H1 vs H3**: H1 first. H3's core cross-validation requires extending TPP to 20C (technically non-standard), while H1 is a pure computational analysis on existing data. H1 also has a more surprising biological implication (tail sculpting as a distinct evolutionary strategy). **Winner: H1**

**3. H1 vs H5**: H1 first. H5's central biological prediction is partially pre-empted by Bresson 2024 (eIF4F thermo-sensing already known), and the mechanistic premise (eIF factors have low Tm) is partially contradicted. H1 makes a prediction about which no prior work exists, making a positive result more impactful. **Winner: H1**

**4. H1 vs H7**: H1 first. H7 faces a potential total confound from protein size (kinases are large; large proteins have lower Tm). If that confound explains the enrichment, H7 produces a trivial result. H1 has no equivalent fatal confound identified. **Winner: H1**

**5. H2 vs H3**: H2 first. H2 is more immediately executable (CORUM + Meltome Atlas vs. needing to extend TPP to 20C for validation). H2's independence-restoration argument is elegant and the return-level output is directly interpretable. H3's key prediction depends on an accuracy threshold (+/-3%) with no proteomics-specific basis. **Winner: H2**

**6. H2 vs H5**: H2 first. H5's prediction is partly pre-empted and has an internally contradicted mechanistic premise (eIF4A heat-resistance). H2's mechanism is sounder and its cross-species bottleneck prediction is more novel. **Winner: H2**

**7. H2 vs H7**: H2 first. Both use POT/GPD, but H2's independence-restoration argument and return-level interpretation are more rigorous. H7 faces the size confound that could fully explain results without invoking "thermal disposability." H2 produces a more biologically interpretable output (specific named bottleneck complexes). **Winner: H2**

**8. H3 vs H5**: H3 first. H3 offers a genuine methodological contribution (censored GEV for left-censored proteomics) with no pre-emption in the literature. H5's central prediction was anticipated by Bresson 2024. H3's cross-domain transfer from hydrology is more novel even if execution is harder. **Winner: H3**

**9. H3 vs H7**: H3 first. The censored GEV approach addresses a real documented problem (20% unmeasured proteome) with a principled statistical solution. H7 risks being a size-confound artifact. H3's result, whether positive or negative, teaches us something about the distribution of the unobserved proteome. **Winner: H3**

**10. H5 vs H7**: H7 first. While both have grounding issues, H7's functional enrichment prediction is directly testable with a simple bioinformatics pipeline and a negative result (enrichment disappears after size correction) would cleanly answer the design-principle question. H5's specific bottleneck prediction is more likely to be wrong (eIF4A heat-resistance, multi-factorial thermal death). **Winner: H7**

**Tally (wins out of 4 comparisons each):**

| H# | Wins | Losses | Win Rate |
|----|------|--------|----------|
| H1 | 3 (vs H3, H5, H7) | 1 (vs H2) | 3/4 = 75% |
| H2 | 4 (vs H1, H3, H5, H7) | 0 | 4/4 = 100% |
| H3 | 2 (vs H5, H7) | 2 (vs H1, H2) | 2/4 = 50% |
| H7 | 1 (vs H5) | 3 (vs H1, H2, H3) | 1/4 = 25% |
| H5 | 0 | 4 | 0/4 = 0% |

**Elo ranking (by win rate):** H2 > H1 > H3 > H7 > H5

**Linear composite ranking:** H1 (8.45) > H2 (8.15) > H3 (7.05) > H7 (7.00) > H5 (6.25)

**Comparison:**
- Top 3 are identical in both rankings: H1, H2, H3 (order reverses for #1 vs #2).
- H7 and H5 maintain the same relative order.
- Minor divergence: Elo places H2 above H1 while the linear ranking places H1 above H2.

**Divergence analysis — H2 over H1 in Elo:**
The pairwise preference for H2 over H1 reflects an implicit dimension the linear scoring partly captures but underweights: **near-term executability and output interpretability**. H2 produces named bottleneck complexes (a result directly usable by a cell biologist), while H1 produces a cross-species xi comparison whose biological significance depends on the unknown effect size. In the linear scoring, both receive 9/10 on Testability, but H2's richer output interpretability is not fully captured by the Testability dimension alone. This is a useful diagnostic: if the Orchestrator needs to prioritize for a time-constrained lab collaboration, H2 may be the pragmatic first choice despite H1's marginally higher composite.

**Verdict: Elo CONFIRMS linear ranking at the top-3 level (same three hypotheses selected).** The H1/H2 swap at positions 1-2 is a diagnostic signal about output interpretability, not an override.

---

## Evolution Selection (Post-Diversity-Check)

**Selected for Quality Gate: H1, H2, H3, H7**

Rationale:
- **H1** (8.45): Strongest overall composite. Highest novelty. Zero prior work. Immediately testable. Core prediction mathematically rigorous. Selected.
- **H2** (8.15): Second-highest composite and winner of Elo tournament. Clean independence-restoration argument. Specific biological predictions. Cross-species validation path. Selected.
- **H3** (7.05): Third highest. Addresses a documented unmet need (20% unmeasured proteome). Cross-domain transfer from hydrology has strong novelty. Partially held back by multi-modal tail risk and +/-3% speculative claim; these are addressable by the Evolver (add unimodality test, replace +/-3% with a calibration curve). Selected.
- **H7** (7.00): Fourth highest. Testability is strong (standard bioinformatics pipeline). "Thermal disposability" framing is catchy and stimulating. The size-confound issue is addressable (include protein length as a covariate in enrichment test — this is a standard correction). The CDK2 internal contradiction needs to be resolved. Selected.

**Not selected:**
- **H5** (6.25): Partially pre-empted by Bresson 2024. Core mechanistic premise (eIF factors have low Tm) is partially contradicted by published data. Single-bottleneck framework conflicts with multi-factorial thermal death models. Lowest composite and zero Elo wins. The EVT framework is useful but the biological prediction is the weakest in the set. Excluded from Quality Gate in this cycle; may re-enter if Evolver is run.

**Final selection: H1, H2, H3, H7 — 4 hypotheses advance to Quality Gate.**

---

*Ranker Agent — Session 2026-03-27-scout-013 — Cycle 1 — 2026-03-27*
