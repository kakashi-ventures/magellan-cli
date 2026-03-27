# Cycle 1 Ranking — Extreme Value Statistics × Proteome Thermal Stability

**Session**: 2026-03-27-scout-013
**Cycle**: 1
**Ranker model**: claude-sonnet-4-6
**Hypotheses ranked**: 5 (of 7; 2 killed by Critic)

---

## Per-Hypothesis Scoring Tables

---

### H2: Complex-Minimum Tm Identifies Thermal Bottleneck Complexes Invisible to Mean-Tm Analysis

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 8 | Critic's web search found zero results for return level estimation applied to protein complex thermal failure. The bottleneck-principle applied as an EVT return-level problem is genuinely unexplored territory in both proteomics and EVT literatures. |
| Mechanistic Specificity | 20% | 9 | Multi-level abstraction with molecular (complex-minimum Tm bottleneck), systemic (process failure fraction), and mathematical (return level formula with μ, σ, ξ and profile-likelihood CIs) layers. Names specific assays (puromycin incorporation, Seahorse respirometry), specific complexes (ribosomal subcomplexes, mitochondrial respiratory chain), specific threshold (1% return level), and a ±2°C prediction window. Strongest mechanistic statement in the batch. |
| Cross-field Distance | 10% | 7 | Structural hydrology (flood return levels) → molecular cell biology (protein complex thermal failure). The formal analogy "flood blocks" = "protein complexes" and "return period" = "fraction of process capacity lost" bridges communities that never interact. |
| Testability | 20% | 9 | All data exists (Meltome Atlas, TPCA complex annotations). EVT fitting is standard (R: evd/extRemes). Validation assays (puromycin, Seahorse) are workhorse methods available in any cell biology lab. The ±2°C prediction window is specific and pre-registered. A PhD student with R and cell culture could execute this in 2–3 months. |
| Impact: Paradigm | 5% | 7 | Provides the first quantitative framework for predicting cellular process failure temperatures from static proteomics data. Elevates TPP from "protein stability catalogue" to "predictive thermal physiology." Would change how thermal stress and fever research designs experiments. |
| Impact: Translational | 5% | 6 | Predicting which cellular processes fail first during fever, heat stroke, or therapeutic hyperthermia has direct biomedical relevance. Ribosome failure temperatures tie to heat shock response thresholds; mitochondrial failure ties to ischemia-reperfusion. More translational than others in this batch. |
| Groundedness | 20% | 7 | Critic revised to 7. ~75% grounded: TPCA data (Tan 2018, confirmed, soft attribution error only); Meltome Atlas (Jarzab 2020, confirmed); EVT return level methodology (Coles 2001, confirmed). Deduction: soft TPCA misattribution (Mateus 2020 vs. Tan 2018); chaperone buffering (HSP70/HSP90 STRING scores ≥0.93 confirmed) is a real concern that inflates uncertainty on the ±2°C window. |
| **Composite (pre-bonus)** | | **7.95** | 0.20×8 + 0.20×9 + 0.10×7 + 0.20×9 + 0.05×7 + 0.05×6 + 0.20×7 |
| **Cross-domain bonus** | | **+0.5** | Applied: EVT/structural hydrology (mathematics) → molecular cell biology (life sciences) spans 2+ disciplinary boundaries. |
| **Composite (final)** | | **8.45** | |

---

### H1: GEV Tail Index (xi) as Phylogenomic Signature of Thermal Adaptation Strategy

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 8 | Critic confirmed: zero results for GEV shape parameter applied to proteome Tm distributions. The "domain-of-attraction" vocabulary from EVT has never been applied to classify organisms by thermal adaptation strategy. Genuinely unexplored at the intersection of EVT and comparative proteomics. |
| Mechanistic Specificity | 20% | 7 | Names specific EVT parameter (ξ), specific dataset (Meltome Atlas, PRIDE PXD011929, 13 species), specific prediction (negative ξ-OGT correlation), and a computational estimate of detection power (SE(ξ) ≈ 0.016, detectable difference 0.033 vs. expected thermophile-mesophile gap 0.3–0.5). Deduction: the tail-truncation vs. distribution-shift distinction for different adaptation strategies is PARAMETRIC and lacks direct molecular grounding of the ξ→strategy inference. |
| Cross-field Distance | 10% | 7 | EVT/mathematical statistics → evolutionary proteomics / comparative genomics. These communities share almost no overlap. The converging vocabularies (EVT "domain of attraction" ↔ proteomics "thermal adaptation strategy") is the kind of structural isomorphism that makes for high cross-field impact. |
| Testability | 20% | 8 | Existing Meltome Atlas data (PRIDE PXD011929) requires only EVT fitting — no new experiments. Standard R packages (evd, extRemes) handle GEV MLE with profile-likelihood CIs. Phylogenetically independent contrasts for n=13 are feasible. The n=13 limitation is a real power constraint but the expected ξ difference (0.3–0.5) is large relative to SE(ξ) ≈ 0.016 — the test is powered. A single computational analysis, 1–2 months. |
| Impact: Paradigm | 5% | 6 | Would reframe thermal adaptation research from mean-Tm-shifts to distribution-shape signatures. Creates a new classification tool for organisms' thermotolerance strategies. Moderate — extends existing framework rather than overturning it. |
| Impact: Translational | 5% | 3 | Primarily a characterization and classification tool. No immediate biomedical application. Phylogenomic signature of adaptation is interesting scientifically but lacks near-term translational pathway. |
| Groundedness | 20% | 8 | Critic maintained at 8 (revised). ~80% grounded: FTG theorem (Fisher & Tippett 1928, Gnedenko 1943 — confirmed); Meltome Atlas (Jarzab 2020 — confirmed); thermophile amino acid adaptations (confirmed, well-reviewed). Hallucination risk LOW. Deduction: the specific ξ values predicted for thermophiles vs. psychrophiles are PARAMETRIC; phylogenetic confounding with n=13 is a real methodological limitation. |
| **Composite (pre-bonus)** | | **7.35** | 0.20×8 + 0.20×7 + 0.10×7 + 0.20×8 + 0.05×6 + 0.05×3 + 0.20×8 |
| **Cross-domain bonus** | | **+0.5** | Applied: EVT/mathematical statistics → evolutionary proteomics spans 2+ disciplinary boundaries. |
| **Composite (final)** | | **7.85** | |

---

### H3: Censored GEV Recovers the Invisible 20% Below TPP Window

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 8 | Critic confirmed: zero results for censored EVT applied to TPP data. The application of hydrological censored GEV methods to the TPP detection-limit problem is a genuine gap — Figueroa-Navedo & Ivanov 2024 (Cell Reports Methods) explicitly flag the 20% unmeasured problem as unresolved. Novel method application to a recognized problem. |
| Mechanistic Specificity | 20% | 7 | Specifies censoring points (left at 30°C, right at 90°C), censored MLE procedure, specific predictions (Δμ > 1°C, Δσ > 0.5°C, ±3°C validation window for extended-range TPP), and posterior predictive distributions for individual censored proteins. Deduction: the IDP fundamental flaw (IDPs lack cooperative unfolding → no defined Tm) is unaddressed, and IDPs likely constitute a substantial fraction of the <30°C set — this is a SPECIFICATION error, not just noise. |
| Cross-field Distance | 10% | 7 | Hydrological statistics (rain gauge censoring, flood censored MLE) → proteomics measurement bias. Same cross-domain as other EVT hypotheses. The censoring analogy is structurally coherent, which is why the IDP flaw is so damaging — the analogy breaks where it matters most. |
| Testability | 20% | 4 | The Critic identified a critical model misspecification: IDPs (30–50% of eukaryotic proteomes, and likely overrepresented among proteins with Tm < 30°C) lack cooperative unfolding transitions, meaning Tm is undefined for them. Censored GEV models P(Tm ≤ 30°C) but this quantity is undefined for IDPs. The extended-range TPP validation would work for non-IDP proteins but cannot distinguish model failure from IDP biology. Testability is substantially limited by this fundamental mismatch between model assumptions and data-generating process. |
| Impact: Paradigm | 5% | 5 | Addresses a recognized problem (Figueroa-Navedo 2024 explicitly raises it). If the IDP issue were resolved, would fix a systematic bias in all thermal proteomics. As currently formulated, the bias correction is incomplete and potentially misleading. |
| Impact: Translational | 5% | 3 | Corrected proteome thermal maps are interesting but no immediate therapeutic application. IDP enrichment finding is a side-effect, not the target application. |
| Groundedness | 20% | 5 | Critic revised to 5. ~60% grounded: Stedinger et al. 1993 censored EVT (confirmed); Jarzab 2020 20% unmeasured (confirmed); Figueroa-Navedo 2024 (confirmed). Deduction: IDP issue unaddressed — ~30–50% of the censored population may not satisfy model assumptions; this is not a minor confounder but a structural failure of the model for a large fraction of its target population. |
| **Composite (pre-bonus)** | | **5.90** | 0.20×8 + 0.20×7 + 0.10×7 + 0.20×4 + 0.05×5 + 0.05×3 + 0.20×5 |
| **Cross-domain bonus** | | **+0.5** | Applied: hydrological statistics → proteomics spans 2+ disciplinary boundaries. |
| **Composite (final)** | | **6.40** | |

---

### H7: POT Functional Enrichment Reveals Thermal Disposability in Signal Transduction

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 5 | PARTIALLY_EXPLORED per Critic. Leuenberger et al. 2017 (Science, PMID 28232526) already performed GO enrichment on the thermally least stable proteins, finding enrichment for cofactor and DNA-binding proteins. The GPD threshold selection (replacing percentile cutoff with MRL-plot principled threshold) is a genuine methodological contribution, but the biological finding is incremental over established prior art. Score reflects this mixed picture. |
| Mechanistic Specificity | 20% | 6 | Specifies GPD methodology, MRL-plot threshold selection, enrichment ratios (≥2.0 for disorder, ≥1.5 for STRING degree), specific GO terms ("signal transduction," "transcription regulation"), FDR<0.01. However, "thermal disposability as a design principle" is post-hoc interpretation of an enrichment pattern; CDK2 Tm unverified; disorder/size/expression confounders not addressed in the hypothesis design. |
| Cross-field Distance | 10% | 7 | EVT/extreme value statistics → protein biochemistry / cell biology. Same cross-domain as others. |
| Testability | 20% | 7 | FDR<0.01 across 13 species is specific and testable with existing Meltome Atlas data plus IUPred disorder scores (freely available). STRING PPI degree query is standard. A replication of Leuenberger 2017 with better threshold methodology is well within a PhD student's scope. Deduction: prior art means the main result is likely confirmatory rather than discovery. |
| Impact: Paradigm | 5% | 4 | Leuenberger 2017 (Science) already showed enrichment. GPD threshold provides methodological rigor but does not change the conceptual landscape. "Thermal disposability" as an evolutionary design principle is speculative and likely incorrect (low Tm reflects disorder for binding flexibility, not adaptive disposability). |
| Impact: Translational | 5% | 3 | Identifying thermally unstable signal transduction proteins has limited direct biomedical application without identifying specific therapeutic targets or mechanisms. |
| Groundedness | 20% | 5 | Critic revised to 5. ~55% grounded: GPD methodology (Coles 2001, confirmed); Leuenberger 2017 prior art (confirmed); GO terms (confirmed). Deduction: "thermal disposability" interpretation is PARAMETRIC and potentially overclaimed; CDK2 Tm is UNVERIFIED; enrichment vs. protein size / disorder fraction / expression level confounders are unaddressed. |
| **Composite (pre-bonus)** | | **5.65** | 0.20×5 + 0.20×6 + 0.10×7 + 0.20×7 + 0.05×4 + 0.05×3 + 0.20×5 |
| **Cross-domain bonus** | | **+0.5** | Applied: EVT → cell biology/proteomics spans 2+ disciplinary boundaries. |
| **Composite (final)** | | **6.15** | |

---

### H5: Pathway-Level Block Maxima = Translation Initiation as Universal Thermal Death Bottleneck

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 5 | PARTIALLY_EXPLORED per Critic. The EVT formalization (block maxima per KEGG pathway) is novel. However, the predicted biological outcome — translation initiation as the rate-limiting thermally sensitive process — is ALREADY ESTABLISHED from heat stress biology (eIF2α phosphorylation, eIF4F disassembly, integrated stress response). A hypothesis that is likely to rediscover established biology via a new method scores lower on novelty than one predicting genuinely unknown biology. |
| Mechanistic Specificity | 20% | 6 | Specifies KEGG pathway groupings, block maxima EVT methodology, 13-species comparison, and translation initiation as the specific prediction. However, the biological prediction is expected rather than surprising, and KEGG annotation incompleteness in non-model species weakens the analysis in exactly the organisms where the finding would be most informative. |
| Cross-field Distance | 10% | 7 | EVT → heat stress biology / cell biology. Same cross-domain distance as other hypotheses in this session. |
| Testability | 20% | 6 | The EVT formalization is testable with existing Meltome Atlas + KEGG data. However, the Membrane Sensor Hypothesis (Vigh et al. 2007 PNAS) — that membrane lipid phase transitions trigger thermal death BEFORE protein denaturation at physiological temperatures — means the test may be measuring the wrong bottleneck. If membranes fail first, TPP-based EVT predicts the wrong cellular death mechanism, limiting the experimental validation to a narrow temperature window where protein denaturation dominates. |
| Impact: Paradigm | 5% | 4 | Low impact because translation heat sensitivity is established knowledge. The EVT formalization adds methodological rigor but does not change the conceptual picture. The Membrane Sensor Hypothesis undermines the framing that protein-Tm-based analyses can identify the primary thermal death mechanism. |
| Impact: Translational | 5% | 3 | Confirming known biology with a new statistical framework has limited translational value. No novel therapeutic angle beyond existing heat shock response literature. |
| Groundedness | 20% | 5 | Critic revised to 5. ~65% grounded: block maxima EVT (Coles 2001, confirmed); KEGG pathway groupings (partially confirmed, incompleteness noted); translation initiation heat sensitivity (confirmed — and this is the prior art problem). Deduction: Membrane Sensor Hypothesis (Vigh 2007, confirmed) provides active counter-evidence that the protein-Tm framework misses the primary death mechanism; KEGG incomplete for non-model species. |
| **Composite (pre-bonus)** | | **5.45** | 0.20×5 + 0.20×6 + 0.10×7 + 0.20×6 + 0.05×4 + 0.05×3 + 0.20×5 |
| **Cross-domain bonus** | | **+0.5** | Applied: EVT → heat stress biology/cell biology spans 2+ disciplinary boundaries. |
| **Composite (final)** | | **5.95** | |

---

## Final Ranking Table

| Rank | ID | Title (abbreviated) | Novelty | Mech. Spec. | Cross-field | Testability | Impact: Par. | Impact: Trans. | Groundedness | Pre-bonus | Bonus | **Final** | Verdict |
|------|----|---------------------|---------|-------------|-------------|-------------|--------------|----------------|--------------|-----------|-------|-----------|---------|
| 1 | H2 | Complex-Minimum Tm Return Levels | 8 | 9 | 7 | 9 | 7 | 6 | 7 | 7.95 | +0.5 | **8.45** | SURVIVES |
| 2 | H1 | GEV Tail Index Phylogenomic Signature | 8 | 7 | 7 | 8 | 6 | 3 | 8 | 7.35 | +0.5 | **7.85** | SURVIVES |
| 3 | H3 | Censored GEV — Invisible 20% | 8 | 7 | 7 | 4 | 5 | 3 | 5 | 5.90 | +0.5 | **6.40** | WOUNDED |
| 4 | H7 | POT Functional Enrichment | 5 | 6 | 7 | 7 | 4 | 3 | 5 | 5.65 | +0.5 | **6.15** | WOUNDED |
| 5 | H5 | Pathway Block Maxima / Translation | 5 | 6 | 7 | 6 | 4 | 3 | 5 | 5.45 | +0.5 | **5.95** | WOUNDED |

*All hypotheses received the cross-domain creativity bonus (+0.5) because every hypothesis in this session bridges EVT/mathematical statistics to life sciences (proteomics/cell biology), spanning 2+ disciplinary boundaries.*

---

## Diversity Check

**Question**: Do any 3+ of the top 5 share the same bridge mechanism, connect the same subfields, or make the same type of prediction?

**Assessment**:

| Pair | Mechanism overlap? | Prediction type overlap? | Verdict |
|------|--------------------|--------------------------|---------|
| H2 + H1 | Both use GEV fitting to Tm distributions, but H2 applies return levels to complex-minimum Tm (failure prediction); H1 applies tail index to species-level comparison (classification) | H2 predicts specific temperatures; H1 predicts statistical signatures | **Distinct** |
| H2 + H3 | Both use GEV; H2 on complex-minimum data; H3 on censored single-protein data | H2 predicts process failure temps; H3 corrects measurement bias | **Distinct** |
| H2 + H7 | H2 uses return levels on complexes; H7 uses GPD on individual proteins | H2 predicts cellular failure; H7 enrichment analysis | **Distinct** |
| H2 + H5 | H2 return levels on complexes; H5 block maxima on pathways | H2 predicts specific temperatures; H5 identifies bottleneck pathways | **Similar method layer** but different biological question |
| H1 + H3 | Both fit GEV to Tm; H1 for tail index across species; H3 for correcting censoring within species | H1 cross-species; H3 within-species — different biological questions | **Distinct** |
| H5 + H7 | Both apply EVT to identify biologically important proteins; H5 block maxima on pathways; H7 GPD on individual proteins | Both look for "what is thermally sensitive and biologically important?" | **Convergent in spirit** |

**Conclusion**: H5 and H7 share the spirit of "use EVT to identify which biology is thermally most vulnerable," but they use different EVT methods (block maxima vs. GPD/POT) and make different predictions (pathway bottlenecks vs. protein-type enrichment). No 3+ hypotheses are sufficiently convergent to trigger a diversity adjustment.

**Decision**: No reordering required. Ranking stands as computed.

---

## Elo Tournament Sanity Check

All 5 surviving hypotheses included (10 pairwise comparisons).

**Question per pair**: Which hypothesis would a domain researcher want to test FIRST, and why?

| Pair | Winner | Rationale |
|------|--------|-----------|
| H2 vs H1 | **H2** | H2 has a concrete experimental endpoint (Seahorse respirometry at predicted temperature) that gives an unambiguous binary result. H1 requires n=13 phylogenetic analysis with confounding concerns that make interpretation harder even with positive results. |
| H2 vs H3 | **H2** | H2's methodology is sound; H3 has a fundamental model misspecification (IDPs with undefined Tm in the censored set). Testing H2 first gives clean results; H3 needs IDP pre-filtering before the core test is valid. |
| H2 vs H5 | **H2** | H2 predicts something unknown (which cellular process fails at which temperature with ±2°C precision); H5 is expected to confirm that translation initiation is thermally sensitive — a fact already in the heat stress literature. |
| H2 vs H7 | **H2** | H2 has higher discovery potential; H7 is largely a methodological refinement of Leuenberger 2017 using GPD threshold vs. percentile cutoff. A researcher would prioritize the genuinely novel framework. |
| H1 vs H3 | **H1** | H1 is methodologically clean (FTG theorem guarantees convergence; GEV fitting to existing data); H3 requires the IDP issue to be resolved before the core censored GEV analysis is interpretable. |
| H1 vs H5 | **H1** | H1 predicts a genuinely novel biological signal (phylogenomic signature in tail index); H5 is likely to rediscover known heat stress biology via a new formalism. Higher expected discovery yield from H1. |
| H1 vs H7 | **H1** | H1 opens a new line of inquiry (EVT domain-of-attraction as taxonomic classification); H7 adds rigor to existing TPP analysis. H1 has higher asymmetric upside. |
| H3 vs H5 | **H3** | Despite the IDP flaw, H3 addresses a recognized measurement gap (Figueroa-Navedo 2024) and could be salvaged with IDP pre-filtering. H5 is confirmatory of known biology in a domain where the bottleneck may not even be protein stability (Vigh 2007 membrane hypothesis). |
| H3 vs H7 | **H3** | H3 corrects a specific, quantified measurement bias (~20% of proteome unmeasured) with potential to change all downstream thermal proteomics analyses. H7 refines a threshold method on a population Leuenberger 2017 already characterized. |
| H5 vs H7 | **H7** | H7's GPD threshold provides a genuinely principled statistical improvement over arbitrary percentile cuts, even with prior art on the biological conclusion. H5's biological conclusion is more thoroughly anticipated and the Membrane Sensor Hypothesis undermines its framing. |

**Win tallies**:
| Hypothesis | Wins | Losses | Win Rate |
|------------|------|--------|----------|
| H2 | 4 | 0 | 4/4 = 100% |
| H1 | 3 | 1 | 3/4 = 75% |
| H3 | 2 | 2 | 2/4 = 50% |
| H7 | 1 | 3 | 1/4 = 25% |
| H5 | 0 | 4 | 0/4 = 0% |

**Elo ranking**: H2 > H1 > H3 > H7 > H5

**Verdict**: **Elo confirms linear ranking.** The win-rate ranking exactly matches the composite score ranking. The pairwise tournament validates the linear scoring on both axes: (a) the top-2 separation (H2's concrete experimental endpoint vs. H1's pure computational analysis) maps to the Testability + Impact scoring gap; (b) the bottom-2 separation (H7 over H5) is confirmed by the reasoning that prior-art inhibition is worse for H5 (actively undermined by the Membrane Sensor Hypothesis) than for H7 (partial methodological novelty preserved).

**No divergence to flag.**

---

## Evolution Selection

**Top 4 selected for evolution** (all scoring ≥6.15; top 5 scoring ≥5.95 but H5 is marginal):

| Priority | ID | Final Score | Reason for inclusion |
|----------|----|-------------|----------------------|
| 1 | **H2** | 8.45 | Strongest in all dimensions; concrete experimental validation path; genuinely novel framework |
| 2 | **H1** | 7.85 | Computationally executable with existing data; novel phylogenomic classification signal; high groundedness |
| 3 | **H3** | 6.40 | Novel method application to recognized gap; evolution should address the IDP misspecification flaw directly (e.g., IDP pre-filtering + separate censored GPD for non-IDP proteins) |
| 4 | **H7** | 6.15 | Methodological improvement over Leuenberger 2017; evolution should deconfound from disorder/size/expression and propose a test that distinguishes GPD-threshold from percentile results |

**H5 (5.95) is NOT selected for evolution**: The Membrane Sensor Hypothesis (Vigh 2007) provides active counter-evidence that protein-Tm-based EVT misses the primary thermal death mechanism. Evolving H5 would require reframing the hypothesis around what EVT can uniquely contribute BEYOND confirming known heat stress biology — which may be possible but is not the highest-value use of evolution effort relative to the other four.

**Evolution notes for the Evolver**:
- H2: Consider extending the framework to include non-equilibrium kinetic corrections (heating rate dependence); explore whether chaperone STRING scores predict ±2°C offset magnitude
- H1: Phylogenetically independent contrasts are critical; consider whether the two ξ-prediction regimes (tail truncation vs. distribution shift) can be distinguished with existing OGT metadata
- H3: IDP pre-filtering is the central challenge — propose a modified hypothesis that applies censored GEV only to proteins with AlphaFold pLDDT > 70 (structured) and a separate analysis for IDPs
- H7: Must deconfound from Leuenberger 2017 — propose a test that specifically isolates the GPD threshold effect from a percentile-based benchmark; address size/disorder confounders explicitly
