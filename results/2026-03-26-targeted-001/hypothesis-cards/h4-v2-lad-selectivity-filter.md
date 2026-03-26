# Hypothesis Card: Stiffness-Calibrated LAD Compartmentalization as a Genomic Selectivity Filter for TEAD Enhancer Access

**Session**: 2026-03-26-targeted-001 (Blind Mode — Holdout Validation)
**Target**: Mechanobiology (ECM mechanics) × Epigenomics (genomic enhancer regulation)
**ID**: H4-v2 | **Parent**: H4 — LAD-Embedded Enhancers as Stiffness-Resistant Mechanical Selectivity Filter
**Generation cycle**: 1 (evolved, specification + mutation operations)
**Date**: 2026-03-26

---

## One-Line Summary

ECM stiffness upregulates lamin A/C, reinforcing constitutive LAD (cLAD) anchoring and creating a three-tier spatial selectivity filter that partitions the TEAD enhancer repertoire into permanently silenced (cLAD), stiffness-modulated (fLAD), and freely accessible (non-LAD) categories — making genomic address, not motif content, the primary determinant of enhancer mechanosensitivity.

---

## Quality Gate Verdict

| Dimension | Score |
|---|---|
| Mechanistic Specificity | 2.0/2.0 |
| Novelty | 2.0/2.0 |
| Groundedness | 1.5/2.0 |
| Testability | 1.5/2.0 |
| Impact | 1.5/2.0 |
| **Total** | **8.5/10** |

**Verdict**: PASS
**Confidence**: 0.68 | **Groundedness**: 8/10
**QG mode**: Post-blind web-verified (20+ searches, 0 citation hallucinations)
**Key novelty confirmation**: No paper has stratified H3K27ac enhancer responsiveness by LAD compartment (cLAD vs fLAD vs non-LAD) under ECM stiffness. Cosgrove et al. Science 2025 (mechanoenhancers via ATAC-seq) and Pigeot et al. bioRxiv 2025 (lamin + PRC2 at bivalent genes) are partially convergent but do not address the LAD selectivity filter model.

---

## Bridge Mechanism (A → B → C)

**A** — ECM stiffness (1–25 kPa gradient): integrin-FAK-RhoA-ROCK1 → actomyosin contractility → LINC complex (emerin-SUN2-nesprin) → nuclear force transmission
**B** — Lamin A/C upregulation (6-fold across 0.1–40 kPa; Swift et al. Science 2013): stabilizes nuclear lamina, increases mean residence time of cLAD chromatin at nuclear periphery; HDAC2 proximity at lamina (LMNA-HDAC2 STRING 0.690) maintains H3K9me2/3 in cLADs
**C** — Three-tier TEAD enhancer selectivity filter set by nuclear geometry:
- **cLADs** (H3K9me3, H3K27ac-depleted): stiffness-INDEPENDENT absolute barriers; EP300 sterically/biochemically excluded by compact H3K9me3 chromatin + HDAC2 proximity
- **fLADs** (H3K27me3, developmentally regulated): stiffness-MODULATED partial barriers; increased lamin A/C on stiff ECM tightens fLAD anchoring → soft-specific peaks preferentially lost from fLADs
- **Non-LADs** (euchromatin): freely accessible to YAP-EP300-H3K27ac deposition

---

## Detailed Mechanism

**Step 1** — Stiff ECM (>5 kPa) activates ROCK1-actomyosin contractility, transmitting cytoskeletal tension through the LINC complex to the nuclear lamina. This mechanically stabilizes lamin A/C at the nuclear periphery and upregulates *LMNA* expression via SRF/MRTF and YAP. Lamin A/C levels scale 6-fold with tissue stiffness (0.1 to 40 kPa; Swift et al. Science 2013 [GROUNDED]).

**Step 2** — Elevated lamin A/C increases the mean residence time of constitutive LAD (cLAD) chromatin at the nuclear periphery. cLADs are defined as domains present at the periphery in >80% of cells across cell types (Guelen Nature 2008; Meuleman Genome Research 2013 [GROUNDED]). Within cLADs, proximity to lamina-resident HDAC2 and HP1 proteins maintains H3K9me2/3, creating a stiffness-resistant epigenetic lock.

**Step 3** — Simultaneous YAP nuclear translocation (30–60 min post-stiffening) recruits EP300, which writes H3K27ac at non-LAD euchromatic enhancers. EP300 is excluded from cLAD-embedded enhancers by: (a) H3K9me3 competing with H3K27 as acetyltransferase substrate; (b) chromatin compaction limiting nucleosome accessibility. This creates the binary selectivity filter: TEAD-motif enhancers in non-LADs gain H3K27ac; identical motif-containing enhancers in cLADs do not.

**Step 4** — The lamin A/C reinforcement amplification loop: increased lamin A/C on stiff ECM further tightens cLAD anchoring and potentially recruits additional HDAC2, widening the activation gap between cLAD and non-LAD enhancers. The filter is dose-dependent with ECM stiffness (i.e., stiffness-responsive not all-or-nothing).

**Step 5** — fLAD distinction: facultative LADs (present at the periphery in <80% of cells, H3K27me3-enriched) are stiffness-MODULATED rather than stiffness-RESISTANT. Prediction: stiffness-lost H3K27ac peaks should be enriched in fLADs (OR ≥ 2.5) vs. cLADs. The mechanism for fLAD partial barriers is lamin A/C-dependent anchoring of H3K27me3 chromatin that can be relaxed upon lamin reduction.

---

## Quantitative Predictions

1. **Enrichment test** (primary): Stiffness-gained H3K27ac peaks (10 kPa vs 1 kPa) show OR ≥ 4.0 for non-LAD localization vs. H3K4me1 baseline distribution (chi-square, p < 0.001, N ≥ 2,000 peaks). Null expectation: ~1.4x from random LAD composition (genome is ~35% LAD-covered).

2. **fLAD specificity**: Stiffness-lost H3K27ac peaks enriched in fLADs (OR ≥ 2.5) vs. cLADs among lost peaks. Tests whether the partial barrier model predicts the correct compartment.

3. **CRISPR gain-of-function** (causal): dCas9-Lamin B1 targeted to CTGF super-enhancer (non-LAD TEAD target): predicts >60% H3K27ac reduction and >50% CTGF mRNA reduction, rescued by siLMNA co-treatment.

4. **Lamin A/C knockdown** (rescue): siLMNA on stiff ECM: >2-fold H3K27ac gain at fLAD-TEAD loci; <1.3-fold at cLAD-TEAD loci (tests whether the filter is lamin A/C-dependent for fLADs but not cLADs).

---

## Experimental Protocol

**Cell model**: MSCs or HFFs on polyacrylamide hydrogels (1 kPa soft / 10–25 kPa stiff), n = 3 biological replicates per condition, 72h culture at 5,000 cells/cm² on fibronectin-coated 1,000 μm² circular micropatterns (to decouple stiffness-dependent YAP from spreading-area-dependent Hippo signaling).

**Readouts**:
- H3K27ac CUT&Tag (differential enhancer activity)
- Lamin B1 CUT&RUN (LAD mapping in same cells — avoids cell-line mismatch)
- LMNA/LMNB western blot (confirm stiffness-dependent upregulation)

**Perturbations**:
- dCas9-LaminB1 gain-of-function at CTGF super-enhancer (sgRNA pool targeting ~5 kb window)
- siLMNA knockdown + soft → stiff shift (rescue experiment)
- LMNA point mutant R386K (retains nuclear stiffness, weakens chromatin tethering — isolates LAD-anchoring from nuclear shape)

**Computational analysis**:
- Intersect H3K27ac differential peaks with cLAD/fLAD annotation (ENCODE lamin B1 ChIP-seq in matched cell lines, or de novo CUT&RUN from same cells)
- Fisher's exact test for enrichment; requires LAD boundary exclusion analysis (±50 kb from LAD edges)

**Timeline**: 6 months for cell culture + CUT&Tag + CUT&RUN; 3 months for CRISPR validation; 12 months total for full experiment set.

---

## Key Literature

| Paper | Relevance |
|---|---|
| Swift et al. Science 2013 (PMID 23990565) | Lamin A/C scales 6-fold with tissue stiffness; foundational grounding claim |
| Guelen et al. Nature 2008 (PMID 18463634) | LAD genome coverage (~35%), 1,300 domains, 0.1–10 Mb |
| Kind et al. Cell 2015 (PMID 26365489) | Single-cell DamID confirms LAD repressive environment; H3K9me2-enriched |
| Meuleman et al. Genome Research 2013 | cLAD/fLAD distinction (70.76% vs 29.24% conserved across cell types) |
| Peric-Hupkes et al. Mol Cell 2010 | fLAD developmental dynamics (lineage-specific repositioning) |
| Sun et al. PNAS 2020 (PMID 32270037) | Nuclear periphery genes resist force-induced H3K9me3 demethylation |
| Xu et al. 2023 (PMID 37229211) | Matrix stiffness upregulates lamin A/C in osteogenesis |
| Mandal et al. 2025 (PMID 41004043) | ECM + lamin A/C + chromatin genomic stability (gap confirmation) |
| Cosgrove et al. Science 2025 (PMID 40997217) | Post-cutoff: mechanoenhancers via ATAC-seq; does NOT address LAD stratification |
| Pigeot et al. bioRxiv 2025 | Post-cutoff: ECM stiffness + lamin + PRC2 at bivalent genes; not enhancer-level |

---

## Known Concerns / Limitations

1. **LAD map variability**: Cell-type-specific LAD maps show 70–75% concordance; experiment must use cLAD/fLAD annotations from the same cell type. Use de novo lamin B1 CUT&RUN in parallel.

2. **fLAD mechanism is parametric**: The claim that fLAD anchoring is stiffness-modulated via lamin A/C is the central novel testable claim. No contradicting evidence found, but no confirming evidence either — this is the hypothesis.

3. **G9a/GLP-lamin interaction**: Cited as contributing to H3K9me2 maintenance at LADs; the specific lamin A/C Ig-fold interaction is not fully established but is not bridge-critical.

4. **Boundary effects**: LAD boundary regions (±50 kb) may confound the OR analysis. If included, OR may decrease toward null expectation. Analysis should exclude boundary regions as a sensitivity analysis.

5. **siLMNA confound**: LMNA knockdown alters nuclear shape and YAP mechanosensing independently of LAD anchoring. Use LMNA-R386K point mutant (separates tethering from nuclear rigidity) or combine with YAP-rescue experiment.

---

## Evolutionary Improvements Over Parent (H4)

1. **Null model corrected**: Replaced flawed >90% non-LAD absolute threshold (only 25–30 pp above 65% baseline) with OR ≥ 4.0 framing vs H3K4me1 null (chi-square test with power calculation; >95% power at N ≥ 2,000 peaks).

2. **cLAD/fLAD distinction formally incorporated**: Distinct mechanistic predictions per compartment; stiffness-lost peaks enriched in fLADs (not cLADs) as separate prediction.

3. **CRISPR tethering elevated to central causal test**: dCas9-LaminB1 at active CTGF SE elevated from supplementary to primary falsification experiment.
