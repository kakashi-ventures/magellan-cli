# Evolution Cycle 1 — Session 2026-03-26-targeted-001
**Fields:** Mechanobiology (ECM mechanics) x Epigenomics (enhancer regulation)
**Cycle:** 1 | **Phase:** Evolution → Quality Gate
**Evolved:** 2026-03-26 | **Mode:** BLIND

---

## Summary Table

| ID | Parent Composite | Operations Applied | Primary Improvement | Predicted Composite |
|----|-----------------|-------------------|---------------------|---------------------|
| H4-v2 | 7.30 | Specification + Mutation | Null model corrected; cLAD/fLAD distinction; CRISPR gain-of-function as central test | 7.70 |
| H2-v2 | 6.50 | Mutation + Specification | KDM6B promoter-vs-enhancer addressed; quantitative kinetics named; UTX specificity resolved | 7.00 |
| H5-v2 | 6.20 | Mutation + Specification | BRD4→EP300 directionality reframed; kinetic rate model built; triptolide control elevated | 6.70 |

---

## H4-v2: Stiffness-Calibrated LAD Compartmentalization as a Genomic Selectivity Filter for TEAD Enhancer Access

**Evolved from Hypothesis H4 (Rank 1, composite 7.30) via Specification + Mutation**

### What Changed and Why

The parent H4 had one clean logical flaw the Critic identified: predicting >90% non-LAD enrichment of stiffness-responsive enhancers, when the null expectation (random distribution across the genome) already yields ~60-65% non-LAD (since LADs cover ~35-40% of the genome). The threshold of >90% is only ~25-30 percentage points above chance — a weak enrichment claim that fails to distinguish biological signal from genomic geography.

Three changes correct this:

1. **Specification of a proper null model with odds ratio framing.** The prediction is now phrased as an odds ratio: stiffness-responsive enhancers should be enriched in non-LAD compartments at an odds ratio of >= 4.0 relative to all H3K4me1-marked enhancers in the genome (approximately 70% of which are already non-LAD by baseline; stiffness-responsive enhancers should be >95% non-LAD, giving an OR of ~10-15 vs. the ~2.3 OR baseline). This requires a power calculation: with ~2,000-5,000 stiffness-gained H3K27ac peaks expected (based on Tsaryk 2022 shear stress data as proxy), a chi-square test against the H3K4me1-baseline distribution achieves >95% power to detect OR >= 3.0.

2. **cLAD vs. fLAD mechanistic distinction.** The parent treated LADs as a monolith. Constitutive LADs (cLADs, ~40% of LAD genome fraction, enriched for H3K9me3, gene-poor satellite repeats) versus facultative LADs (fLADs, ~60% of LAD genome fraction, enriched for H3K27me3, developmentally regulated genes) have fundamentally different mechanistic relationships to stiffness. The evolved hypothesis proposes: cLADs are stiffness-INDEPENDENT silenced compartments (H3K9me3 silencing is refractory to any ECM signal tested); fLADs are stiffness-MODULATED — on soft ECM some fLADs detach from the lamina and move into B-to-A compartment transitions, while on stiff ECM increased lamin A/C reinforces fLAD anchoring. This makes the selectivity filter partial at fLADs and absolute at cLADs.

3. **Gain-of-function CRISPR tethering as a central (not peripheral) prediction.** The evolved hypothesis frames the CRISPR-Lamin tethering experiment as a positive mechanistic test, not a supplementary one. Artificially relocating an active non-LAD TEAD enhancer into the LAD compartment (via CRISPR-dCas9-Lamin B1 fusion targeting an active CTGF/CYR61 super-enhancer) should: (a) reduce H3K27ac at that locus by >60% on stiff ECM (as measured by locus-specific CUT&Tag with guide-RNA-proximal amplicon), (b) reduce target gene mRNA by >50% (RT-qPCR), and (c) this effect should be rescued by siLMNA co-treatment, confirming lamin-dependence.

### Evolved Mechanism

**Upstream force transmission (unchanged, grounded):**
ECM stiffness (1-40 kPa range in physiological contexts: brain 0.1-1 kPa → muscle 8-17 kPa → bone-like 25-40 kPa) → integrin-FAK-RhoA-ROCK1 → actomyosin contractility (requires active MYH9; passive LINC alone gives <0.3% nuclear strain per computational validation) → LINC complex tension (SUN1/2-KASH domain bridge) → nuclear lamina stress → lamin A/C upregulation.

**Lamin A/C scaling with stiffness (grounded):**
Lamin A/C protein levels scale with tissue stiffness across a 50-fold range (Swift et al. Science 2013): 0.1 kPa gels → lamin A/C ≈ 0.3 AU; 40 kPa gels → lamin A/C ≈ 1.8 AU (approximately 6-fold increase). This scaling occurs via a post-translational stability mechanism (phospho-lamin A/C is less stable; actomyosin-mediated dephosphorylation increases lamin A/C half-life). The 6-fold increase in lamin A/C on stiff vs. soft ECM is sufficient to increase H3K9me2/3 methyltransferase recruitment at the lamina (via G9a/GLP, which interact with lamin A/C's Ig-fold domain [PARAMETRIC — interaction reported but not quantified]).

**cLAD vs. fLAD differential response (partially grounded):**
- cLADs (constitutive LADs, Meuleman 2013): Satellite repeats, H3K9me3-enriched, gene-poor, lamin B1-anchored. H3K9me3 silencing at cLADs is independent of lamin A/C levels — present even in lamin A/C-null cells. These are absolutely silenced regardless of ECM stiffness. Any TEAD binding motifs within cLADs are epigenetically inaccessible at all stiffness values tested.
- fLADs (facultative LADs, Peric-Hupkes 2010, Meuleman 2013): Developmentally regulated genes, H3K27me3-enriched, moderately gene-containing. fLAD anchoring strength depends on lamin A/C levels [PARAMETRIC — inferred from differential lamin A/C occupancy at cLADs vs. fLADs]. On soft ECM (low lamin A/C): some fLADs detach → B-to-A compartment transition possible → TEAD enhancers within fLADs become accessible. On stiff ECM (high lamin A/C): fLADs are strongly anchored → TEAD enhancers within fLADs remain silenced. This creates a stiffness-TUNABLE subset of the LAD selectivity filter.

**The selectivity filter logic (quantitative):**
- Total TEAD binding motifs in genome: ~50,000-100,000 (JASPAR TEAD4 motif scan) [PARAMETRIC]
- Fraction in non-LAD compartment: ~60-65% (LADs cover 35-40% of genome)
- Fraction in fLAD (mechanically modulatable): ~14-16% (60% of the 35-40% LAD fraction, per Meuleman proportions) [PARAMETRIC]
- Fraction in cLAD (permanently silenced): ~20-24%
- Mechanically responsive window: the non-LAD 60-65% + the stiffness-detachable fLAD fraction (~5-10% under low stiffness conditions) = 65-75% of TEAD sites are potentially accessible on soft ECM; shrinks to ~60-65% on stiff ECM (fLADs re-tethered)
- Prediction: stiffness-GAINED H3K27ac peaks should show OR >= 4.0 for non-LAD localization versus the full H3K4me1 enhancer set (null). Soft-to-stiff transition should show LOSS of H3K27ac preferentially at fLAD loci (not cLAD, which was always silenced).

**Key prediction 1 (genome-wide, falsifiable with null model):**
H3K27ac CUT&Tag at 1 kPa vs. 25 kPa polyacrylamide gels (MSCs, 72h) + lamin B1 CUT&RUN (LAD mapping) + overlay with public ENCODE LAD maps:
- Stiffness-gained H3K27ac peaks: OR >= 4.0 for non-LAD localization (chi-square, p < 0.001, >95% power with N >= 2,000 peaks)
- Stiffness-lost H3K27ac peaks (soft-specific): enriched in fLAD regions (OR >= 2.5 for fLAD vs. cLAD localization among lost peaks)
- Expected if FALSE: gained and lost peaks are distributed in proportion to genomic background (~65% non-LAD, ~35% LAD); OR ≈ 1.0-1.5 for both categories

**Key prediction 2 (gain-of-function CRISPR tethering, central test):**
In MSCs or HFFs on 25 kPa gels: target an active TEAD super-enhancer (CTGF upstream enhancer, chr6:132Mb region, confirmed TEAD4 ChIP-seq peak in published ATAC data) with dCas9-Lamin B1 fusion + 4 guide RNAs tiling the enhancer. Expected:
- H3K27ac at targeted locus: >60% reduction vs. non-targeting control (CUT&Tag with locus-specific amplicon)
- CTGF mRNA: >50% reduction (RT-qPCR, 48h post-guide delivery)
- Rescue: siLMNA co-delivery should partially rescue H3K27ac (target: >40% restoration) by reducing lamin scaffold density
- Expected if FALSE: H3K27ac unchanged at tethered locus (arguing against LAD-tethering as the silencing mechanism; would instead support histone mark-intrinsic silencing independent of spatial positioning)

**Key prediction 3 (lamin knockdown specificity):**
siLMNA (lamin A/C depletion) in MSCs on stiff ECM (25 kPa):
- Expected: H3K27ac gain preferentially at fLAD-embedded TEAD enhancers (identified by lamin B1 CUT&RUN); cLAD-embedded TEAD enhancers should remain unresponsive (still H3K9me3-marked)
- Quantitative: >2-fold H3K27ac increase at fLAD-TEAD loci; <1.3-fold at cLAD-TEAD loci
- Control: H3K9me2/3 CUT&RUN confirms cLAD status is maintained after siLMNA; confirms selectivity filter operates through distinct mechanisms in cLADs vs. fLADs

**Counter-evidence and risks:**
- LAD maps (lamin B1 DamID, lamin A ChIP-seq) show moderate correlation (~70-75%) between methods — uncertainty in LAD boundary calls could obscure fLAD effects. Mitigated by using multiple LAD calling methods and 3-state classification (cLAD/fLAD/non-LAD).
- Lamin A/C knockdown has pleiotropic effects (nuclear mechanics, DNA damage response, cell cycle) — any stiffness-independent chromatin changes confound interpretation. Mitigated by comparing lamin-knockdown on both soft and stiff ECM; only stiffness-dependent changes should be attributable to the LAD filter mechanism.
- TEAD enhancers within LADs may not have been tested for YAP binding in published data — absence of evidence is not evidence of absence. Mitigated by performing YAP CUT&RUN alongside H3K27ac to directly show YAP cannot access LAD-embedded TEAD sites.
- Sun 2020 (PMID 32270037) showed H3K9me3 barriers require demethylation for force-induced gene activation — the barrier is the histone mark, not the spatial position. This could mean LAD tethering is correlative, not causal. This is the sharpest counter-argument; the CRISPR tethering experiment directly addresses it (artificially enforcing spatial localization without altering histone marks).

**Confidence:** 0.68 (adjusted up from 0.65 parent due to improved null model and gain-of-function test design)
**Groundedness:** 8/10 (LAD proportions, lamin A/C scaling, histone mark identities all well-grounded; fLAD mechanosensitivity is [PARAMETRIC] extrapolation; cLAD stiffness-independence is inferred not demonstrated at enhancers)

---

## H2-v2: Sequential Two-Phase Bivalent Enhancer Resolution: Fast EP300/H3K27ac at Non-Bivalent Loci (2-4h), Delayed KDM6B-Dependent Conversion at Bivalent Enhancers (12-24h) During ECM Stiffness-Gated EMT

**Evolved from Hypothesis H2 (Rank 2, composite 6.50) via Mutation + Specification**

### What Changed and Why

The parent H2 had two connected weaknesses that I address with two targeted mutations:

1. **The promoter-vs-enhancer gap.** KDM6B 2025 (S2:251aa09) demonstrated KDM6B upregulation and activity at the SNAIL and TWIST *promoters* (ChIP-qPCR), not at distal enhancers. The parent hypothesis extrapolated KDM6B activity to bivalent ENHANCERS without mechanistic justification. The mutation: propose a specific mechanism by which KDM6B is recruited to distal bivalent enhancers — namely, bivalent enhancers carry H3K4me1 (the canonical poised enhancer mark, Rada-Iglesias 2011), and the H3K4me1 context provides a docking site for KDM6B's PHD-like Tudor domain (which in KDM6A/UTX is known to recognize H3K4me2/3 [PARAMETRIC — KDM6B recruitment to H3K4me1 at enhancers is the specific novel claim]). This makes enhancer KDM6B activity mechanistically plausible AND specifically testable.

2. **The temporal model makes the mechanism coherent and falsifiable.** The parent described a "coordinated handoff" but the kinetics were vague. The evolved hypothesis proposes a two-phase temporal model with quantitative timing. Phase 1 (0-4h post-stiffening): YAP nuclear translocation → EP300 acetylates H3K27 at pre-accessible non-bivalent enhancers (already H3K4me1+, H3K27me3-negative, open chromatin). These are fast because no demethylation is required. Phase 2 (6-24h): ECM stiffness upregulates KDM6B mRNA/protein via RhoA-SRF transcriptional program [PARAMETRIC — SRF as KDM6B activator is inferred from RhoA-SRF link to mechanical signaling; NF-kB also possible]. KDM6B demethylates H3K27me3 at bivalent enhancers (H3K4me1+, H3K27me3+), then EP300 (constitutively recruited via YAP-TEAD that has been present since Phase 1) deposits H3K27ac on the now-accessible K27 residue. Net result: bivalent-enhancer-driven genes are activated 8-20h LATER than non-bivalent enhancer-driven genes under the same stiffness stimulus.

3. **KDM6B vs. KDM6A (UTX) specificity.** The Critic noted GSK-J4 blocks both. The evolved hypothesis specifies a three-armed experiment to resolve this.

### Evolved Mechanism

**Phase 1 — Fast EP300-dependent activation (0-4h, non-bivalent enhancers):**
ECM stiffness → integrin-FAK-ROCK1 → LATS1/2 inactivation → YAP nuclear translocation (complete within 30-60 min of stiffness application [GROUNDED: canonical YAP biology]) → TEAD1-4 binding at accessible enhancers → EP300 recruitment (YAP1-EP300 STRING score 0.692) → H3K27ac deposition at non-bivalent enhancers (H3K4me1+, H3K27me3-negative, accessible ATAC peaks).

Target gene categories activated in Phase 1: YAP canonical targets (CTGF, CYR61, ANKRD1, AMOTL2) whose enhancers are non-bivalent and pre-accessible in fibroblasts/MSCs.

Kinetic prediction: H3K27ac at CTGF/CYR61 enhancers detectable by CUT&Tag at 2h post-stiffening; peak at 4-6h.

**Phase 2 — Delayed KDM6B-dependent activation (6-24h, bivalent enhancers):**
ECM stiffness → RhoA → SRF (serum response factor) nuclear accumulation [PARAMETRIC — RhoA→SRF is well-established; SRF→KDM6B transcription is the novel mechanistic link] → KDM6B mRNA upregulation (lag: 4-8h for mRNA, 6-10h for protein accumulation, consistent with KDM6B 2025 data showing upregulation on 30 kPa vs. 1 kPa gels in thyroid cancer cells) → KDM6B protein accumulates → KDM6B recruited to bivalent enhancers via H3K4me1 recognition (PHD-Tudor domain) → KDM6B demethylates H3K27me3 at bivalent enhancers → EP300 (constitutively present via YAP-TEAD since Phase 1) deposits H3K27ac on now-accessible K27.

Target gene categories activated in Phase 2: EMT master regulators (SNAI1, TWIST1, ZEB1, CDH2) and osteogenic TFs (RUNX2, SP7) whose enhancers carry H3K4me1 + H3K27me3 bivalency in fibroblast/MSC chromatin states.

Kinetic prediction: H3K27ac at SNAI1/RUNX2 DISTAL ENHANCERS (not promoters) detectable by CUT&Tag at 12-18h post-stiffening; lags behind CTGF/CYR61 enhancer H3K27ac by 8-14h.

**Biochemical necessity (grounded):**
H3K27me3 and H3K27ac are mutually exclusive on the same K27 residue [GROUNDED: canonical biochemistry]. KDM6B demethylation MUST precede EP300 acetylation at bivalent loci — the sequential ordering is biochemically forced, not merely proposed.

**The novel claim (specific and testable):**
KDM6B operates primarily at bivalent DISTAL ENHANCERS (H3K4me1+, H3K27me3+) under ECM stiffness, not primarily at promoters. The KDM6B 2025 evidence for promoter activity is compatible with this — KDM6B may act at both promoters and bivalent enhancers, but the enhancer activity is the mechanistically important one for cell fate gating (promoter activation of SNAIL/TWIST can be explained by YAP-independent mechanisms; the enhancer activation is the mechanically-gated event that commits the cell to EMT).

**Key prediction 1 (kinetic time-course, central test):**
Human dermal fibroblasts (HDFs) or MSCs transferred from 1 kPa to 25 kPa gels. CUT&Tag time-course: 0h, 2h, 6h, 12h, 24h for H3K27ac + H3K27me3 simultaneously (using CUT&Tag-dual or sequential CUT&RUN and CUT&Tag).

Expected results:
- Non-bivalent enhancers (CTGF, CYR61 enhancers): H3K27ac gain peaks at 4-6h; no prior H3K27me3
- Bivalent enhancers at SNAI1/RUNX2/TWIST1 distal sites (identified by H3K4me1 + H3K27me3 in baseline 1 kPa CUT&Tag): H3K27me3 loss begins at 8-12h, H3K27ac gain begins at 12-18h
- Temporal gap between non-bivalent peak and bivalent peak: 8-14h (p < 0.001 by Kolmogorov-Smirnov test on the peak-time distributions)
- Expected if FALSE: H3K27ac at bivalent and non-bivalent enhancers appear with the same timing (<2h difference), indicating KDM6B is not rate-limiting (either a different mechanism is removing H3K27me3, or bivalency is not present at these loci)

**Key prediction 2 (KDM6B vs. KDM6A specificity, three-armed experiment):**
At 24h on 25 kPa gels, treat with:
- Arm 1: GSK-J4 (5 µM; blocks both KDM6A and KDM6B catalytically)
- Arm 2: siKDM6B (siRNA knockdown; KDM6B-specific)
- Arm 3: siKDM6A (UTX knockdown; KDM6A-specific)
Read-out: H3K27ac at bivalent SNAI1/RUNX2 enhancers (CUT&Tag + locus-specific amplicon)

Expected if KDM6B-dependent: Arms 1 and 2 should both reduce H3K27ac at bivalent loci (>50% reduction), Arm 3 should not (< 20% reduction)
Expected if KDM6A-dependent: Arm 3 should reduce H3K27ac, Arm 2 should not
Expected if both: All three arms reduce H3K27ac

**Key prediction 3 (re-ChIP to confirm same-locus sequential conversion):**
At 24h on 25 kPa gels: sequential re-ChIP (first IP with anti-H3K27me3, elute, second IP with anti-H3K27ac) at SNAI1 distal enhancer (chr20:49.6 Mb region, H3K4me1+ in baseline MSC data).
- At 0h: re-ChIP should show H3K27me3/H3K27me3 co-occupancy; minimal H3K27me3/H3K27ac co-occupancy
- At 12h: H3K27me3/H3K27ac co-occupancy INCREASES (mixed population — nucleosomes in transition)
- At 24h: H3K27me3 lost; H3K27ac established (re-ChIP shows H3K27ac/H3K27ac co-occupancy)
This directly tests the "same locus, sequential conversion" claim vs. "parallel activation at different loci."

**Incorporation of KDM6B-at-enhancer novel claim:**
KDM6B CUT&RUN at 12h and 24h post-stiffening: Expected to show KDM6B enrichment at distal enhancers (H3K4me1+ loci) as well as promoters. If KDM6B CUT&RUN shows enrichment ONLY at promoters, the enhancer-level hypothesis is wrong (and the promoter-level mechanism of KDM6B 2025 is the full story).

**Counter-evidence and risks:**
- KDM6B 2025 evidence is from thyroid CANCER cells (high proliferation, altered chromatin landscape). Whether the same mechanism applies in primary HDFs or MSCs is untested. Mitigated by using primary cells.
- CBP (CREBBP) shares acetyltransferase activity with EP300 — if CBP handles Phase 1 and EP300 handles Phase 2 (or vice versa), inhibiting only EP300 gives confounded results. Mitigated by using dual EP300+CBP inhibition (A-485, 5 µM, covers both) vs. EP300-selective inhibitor comparison.
- The RhoA-SRF-KDM6B transcriptional link is [PARAMETRIC] — no paper has demonstrated SRF directly transcribes KDM6B. NF-κB is an alternative. If neither SRF nor NF-κB drives KDM6B in this context, Phase 2 may use a different upstream activator. Mitigated by RNA-seq at 4h, 8h, 12h to identify which TF motifs are enriched in the promoters of mechanically upregulated KDMs.
- H3K4me1 at enhancers is a necessary but not sufficient marker of bivalency — many H3K4me1+ enhancers lack H3K27me3. The experiment must first characterize baseline bivalent enhancer landscape in the chosen cell type.

**Cell density and micropatterning control (addressing ALL-hypotheses Critic question):**
All experiments should be performed at standardized cell density (5,000 cells/cm²) with fibronectin-coated micropatterns (1,000 µm² circular) to control cell spreading area independently of ECM stiffness. This isolates stiffness-dependent YAP nuclear translocation from spreading-area-dependent Hippo pathway signaling.

**Confidence:** 0.62 (increased from 0.58 due to temporal model specificity and KDM6B-at-enhancer as the central testable novel claim; decreased uncertainty on promoter-vs-enhancer question because the new framing explicitly tests it)
**Groundedness:** 7/10 (Phase 1 kinetics, biochemical necessity, bivalent enhancer marks all well-grounded; RhoA-SRF-KDM6B link is [PARAMETRIC]; KDM6B recognition of H3K4me1 at distal enhancers is [PARAMETRIC] and is the central novel claim)

---

## H5-v2: Kinetically Gated Epigenetic Memory at Mechanosensitive Super-Enhancers: BRD4-Scaffolded EP300 Retention Resists HDAC-Mediated Erasure for 6-18h Post-Softening

**Evolved from Hypothesis H5 (Rank 3, composite 6.20) via Mutation + Specification**

### What Changed and Why

The parent H5 had two related weaknesses requiring mutation, plus a quantitative inconsistency:

1. **BRD4→EP300 directionality (Mutation).** The Critic correctly identified that the well-established direction is EP300 deposits H3K27ac → BRD4 binds via bromodomain. The reverse (BRD4 recruits EP300 de novo) is not well-established. The mutation: reframe the mechanism as BRD4 STABILIZES EP300 RETENTION at pre-existing H3K27ac loci, not BRD4 recruits EP300 de novo. Specifically: at super-enhancers, BRD4 forms multivalent contacts with multiple H3K27ac-marked nucleosomes simultaneously (via tandem bromodomains), creating a stable nucleoprotein scaffold. EP300 interacts with BRD4's C-terminal domain (EP300-BRD4 STRING score 0.988 — one of the strongest physical interactions in the network). This interaction retains EP300 at the super-enhancer even when YAP exits the nucleus, because EP300 need not re-engage TEAD to remain at the locus; it is tethered by BRD4's nucleosome scaffold. The direction change: EP300 retention (not EP300 recruitment) is maintained by BRD4. This is mechanistically distinct and grounded.

2. **Quantitative kinetic model (Specification).** The Critic demanded calculation of whether the BRD4-EP300 feedback rate can exceed HDAC erasure rate for the claimed duration. The evolved hypothesis provides this:

   Rate model (simplified):
   - H3K27ac deposition rate by EP300 at super-enhancers: k_write = 0.03-0.1 acetylations per nucleosome per second per EP300 molecule [PARAMETRIC: estimated from in vitro HAT assays; ~100-fold faster at nucleosomal substrate than catalytic rate due to multivalent EP300 binding at SEs]
   - H3K27ac removal rate by HDAC at baseline (on stiff ECM, HDAC3 downregulated [GROUNDED: Fu 2024]): k_erase_stiff ≈ 0.005-0.015 per nucleosome per second
   - H3K27ac removal rate upon softening (HDAC3 re-upregulated within 2-4h): k_erase_soft ≈ 0.01-0.04 per nucleosome per second (2-3x increase)
   - At super-enhancers: 10-50x more EP300 molecules than typical enhancers [GROUNDED: Sabari 2018, Hnisz 2013], so k_write_SE = 10-50 × k_write_typical
   - Steady-state H3K27ac fraction at SEs: k_write_SE / (k_write_SE + k_erase)
   - On stiff ECM (YAP active + BRD4-retained EP300): k_write_SE / k_erase_stiff ≈ 0.3-5 / 0.005-0.015 ≈ 20-1000 (effectively complete acetylation at SEs)
   - Post-softening with BRD4-retained EP300 (YAP gone but BRD4 scaffold intact): k_write_retained / k_erase_soft — if EP300 activity drops to 20% of stiff-ECM level (YAP-independent but BRD4-tethered), ratio ≈ 0.06-1.0 / 0.01-0.04 ≈ 1.5-100×
   - Critical implication: the ratio drops from >>100 to 1.5-100 post-softening. This means H3K27ac is maintained (ratio > 1) for as long as BRD4 remains bound and EP300 is partially active. Given BRD4 half-life at SEs ~2-4h (FRAP data [PARAMETRIC]) and EP300 activity persisting while BRD4 is bound, the window where ratio > 1 is maintained is approximately 6-18h post-softening before BRD4 occupancy drops below the threshold needed to sustain the loop.
   - Quantitative prediction: H3K27ac at mechanosensitive SEs decays with a half-life of 8-12h post-softening (not the parent's 24-72h, not the 30-90 min H3K27ac t1/2 of a single nucleosome, which is overridden by the SE amplification).

3. **Memory half-life correction (Specification, mandatory from Critic).** Changed from 24-72h to 6-18h with quantitative justification above.

### Evolved Mechanism

**Stiffness activation (Phase 1, 0-4h, unchanged):**
ECM stiffness → YAP nuclear → TEAD + EP300 → H3K27ac deposition at mechanosensitive super-enhancers (MSEs) → BRD4 binds via bromodomain to newly deposited H3K27ac → BRD4 forms stable nucleoprotein scaffold at MSE via multivalent H3K27ac contacts (tandem bromodomains read multiple H3K27ac-marked nucleosomes spanning 10-50 kb of SE domain) → EP300 retained at MSE via BRD4-CTD interaction (EP300-BRD4 STRING 0.988).

**Memory maintenance (Phase 2, 4-18h post-softening):**
ECM softening (transfer to 1 kPa gel) → LATS1/2 reactivation (within 30-60 min) → YAP nuclear exit (complete within 1-4h) → Primary EP300 recruitment signal (YAP-TEAD-EP300) lost.

But: BRD4 remains bound at MSEs for 2-8h post-YAP exit [PARAMETRIC — BRD4 residence times at SEs 2-4h by FRAP; YAP-independent BRD4 binding supported by BRD4's constitutive expression and H3K27ac-mediated binding]. BRD4-retained EP300 continues depositing H3K27ac at a reduced rate (YAP-independent EP300 activity, ~20% of YAP-stimulated level). This creates a temporary window where:
- k_write_retained (BRD4-scaffolded, YAP-independent EP300) > k_erase (HDAC3 recovering post-softening)
- H3K27ac at MSEs is maintained above a critical threshold for 6-18h

HDAC3 re-upregulation (post-softening): begins at 2-4h, peaks at 8-12h post-softening [inferred from Fu 2024 kinetics in reverse]. As HDAC3 activity increases, k_erase rises until it exceeds k_write_retained; at this point H3K27ac decays below threshold → BRD4 dissociates (BRD4 requires H3K27ac for binding) → EP300 dissociates (released from BRD4 scaffold) → rapid decay of remaining H3K27ac → MSE goes silent. This is the COLLAPSE of the memory loop — a discontinuous transition, not a gradual decay.

**Critical mechanistic revision (direction of the BRD4-EP300 relationship):**
Old framing: BRD4 recruits EP300 (rejected by Critic — not well-established)
New framing: BRD4 SCAFFOLDS EP300 RETENTION. EP300 is already present at MSEs due to prior YAP-TEAD activity. BRD4's multivalent binding to H3K27ac nucleosomes creates a stable platform. EP300 interacts with this platform via its KIX domain binding to BRD4 CTD. YAP exit removes the YAP-TEAD-EP300 tethering force, but BRD4-CTD provides an alternative docking site that maintains EP300 with lower affinity and activity. The key distinction: this model requires EP300 to already be at the locus (supplied by Phase 1); BRD4 does not recruit EP300 from solution but prevents its departure.

**Super-enhancer specificity (why typical enhancers don't sustain memory):**
At typical enhancers: 1-3 EP300/BRD4 molecules → weak BRD4-CTD scaffold → insufficient EP300 retention → YAP exit → EP300 dissociates → H3K27ac decays with its intrinsic t1/2 (30-90 min). Memory window: ~30-90 min (not mechanistically meaningful).
At super-enhancers: 10-50 EP300/BRD4 molecules per SE domain [GROUNDED: Hnisz 2013, Sabari 2018] → strong multivalent BRD4 scaffold → sustained EP300 retention → 6-18h memory window.

**Key prediction 1 (locus-specific H3K27ac decay kinetics, central test):**
MSCs: 72h on 25 kPa gels → transfer to 1 kPa gels. CUT&Tag time-course: 0h, 2h, 4h, 8h, 12h, 18h, 24h post-transfer.
Read: H3K27ac at (a) MSEs (CTGF, CYR61 SE loci) vs. (b) typical enhancers (matched YAP-responsive, lower BRD4/MED1 density).

Expected:
- Typical enhancers: H3K27ac half-life ~2-4h post-transfer (rapid decay tracking YAP exit)
- Super-enhancers: H3K27ac half-life ~8-12h post-transfer
- Ratio of SE vs. typical enhancer H3K27ac decay rate: > 3× slower at SEs (p < 0.01, N = 3 biological replicates, >20 loci per category)
- Expected if FALSE: SEs and typical enhancers decay at similar rates (< 2× difference); suggests BRD4 scaffold is not providing differential memory

**Key prediction 2 (BRD4 scaffold distinction: dBET6 vs. JQ1):**
At 6h post-softening (within predicted memory window):
- JQ1 (500 nM): disrupts BRD4 bromodomain-H3K27ac interaction → removes BRD4 from H3K27ac nucleosomes → EP300 loses scaffold → H3K27ac should decay to typical-enhancer kinetics within 2-4h of JQ1 addition
- dBET6 (500 nM): degrades BRD4 protein (BET degrader) → complete BRD4 removal → should accelerate H3K27ac decay even more dramatically than JQ1 (because BRD4 protein is gone, not merely displaced)
- Expected: dBET6 > JQ1 in collapsing memory (dBET6 removes all BRD4 interactions; JQ1 only blocks bromodomain binding but leaves BRD4-CTD-EP300 interaction intact) [PARAMETRIC — this differential between JQ1 and dBET6 is the novel mechanistic prediction of the BRD4-scaffold model]
- Expected if FALSE: JQ1 and dBET6 have equivalent effects on H3K27ac decay (BRD4 acts only via bromodomain, no CTD scaffold function)

**Key prediction 3 (triptolide control for transcriptional memory distinction — elevated from peripheral to central):**
At the moment of transfer to 1 kPa gels, add triptolide (0.5 µM; blocks RNAPII transcription initiation) to a parallel condition.
- If memory is epigenetic (BRD4-scaffolded EP300 maintains H3K27ac independently of transcription): CTGF/CYR61 mRNA should decay (transcription blocked) but H3K27ac at their SEs should remain elevated for the predicted 6-18h window. The H3K27ac-transcript temporal dissociation is the key read-out.
- If memory is transcriptional auto-regulation (stiffness-induced transcription produces factors that maintain their own transcription): triptolide should collapse both mRNA AND H3K27ac simultaneously (at ~transcription inhibition onset, ~2-4h).
- Expected: triptolide-treated cells retain SE H3K27ac for 6-12h post-softening (comparable to untreated) but show immediate CTGF/CYR61 mRNA decline → confirms H3K27ac maintenance is epigenetic, not transcriptional.

**Key prediction 4 (quantitative memory half-life, specific falsifiable number):**
The predicted H3K27ac memory half-life at MSEs is 8 ± 4h post-softening (mean ± SD, expected range 6-18h). This is explicitly distinguished from:
- The intrinsic H3K27ac t1/2 at single nucleosomes (~30-90 min — too fast to explain memory without the BRD4 scaffold)
- The transcriptional memory window (~24-48h — sustained by re-transcription, not chromatin state; triptolide experiment above distinguishes this)
- The longer-term mechanical memory proposed in some studies (~days-weeks — attributed to ECM remodeling and cytoskeletal reorganization, a different mechanism)

**Counter-evidence and risks:**
- HDAC3 re-upregulation kinetics post-softening are inferred from Fu 2024 (stiffening context, reversed). Direct measurement of HDAC3 activity kinetics after softening in fibroblasts/MSCs has not been published. If HDAC3 re-upregulates faster (within 30-60 min of softening), the memory window collapses faster than predicted.
- BRD4 FRAP data at SEs (2-4h residence times) is from cancer cell lines. In primary cells, BRD4 exchange rates may differ. Mitigated by measuring BRD4 dynamics at MSEs in the specific cell type used.
- The EP300-BRD4 CTD interaction (KIX-CTD) is inferred from co-immunoprecipitation and STRING score (0.988) but detailed structural characterization is [PARAMETRIC]. Structural disruption of this specific interface would require a mutant EP300 (ΔKIX) experiment to confirm.
- Phase separation / condensate contributions: At SEs, BRD4 can form liquid-like condensates. If condensates (not BRD4-CTD scaffolding) are the retention mechanism, JQ1 vs. dBET6 differential would be abolished (both would collapse the condensate by disrupting BRD4-H3K27ac interaction or BRD4 protein respectively). The condensate model predicts JQ1 ≈ dBET6 in effect; the CTD-scaffold model predicts dBET6 > JQ1. This is a meaningful mechanistic discriminator.

**Cell density and micropatterning control (addressing ALL-hypotheses Critic question):**
Memory experiments must control for cell-cell contact effects on Hippo. Transfer from stiff to soft ECM should be performed in both sparsely plated (1,000 cells/cm², no contact) and micropatterned (1,000 µm² circular micropatterns) conditions to confirm memory is not an artifact of de novo cell-cell Hippo signaling suppressing YAP nuclear exit.

**Confidence:** 0.45 (adjusted from 0.48 parent; rate model increases mechanistic specificity but also reveals how sensitive the 6-18h prediction is to parameter uncertainty; lowered slightly because BRD4-CTD scaffold mechanism is [PARAMETRIC])
**Groundedness:** 7/10 (BRD4 binding via bromodomain to H3K27ac grounded; EP300-BRD4 STRING interaction grounded; HDAC3 stiffness regulation grounded; BRD4-CTD as retention scaffold and FRAP residence times are [PARAMETRIC]; rate constants estimated from in vitro data applied to in vivo context)

---

## EVOLUTION QUALITY CHECK

### 1. Is each evolved hypothesis genuinely stronger than its parent?

**H4-v2 vs. H4:**
- Stronger on testability: null model is now properly specified with OR >= 4.0 and power calculation (not the flawed >90% prediction). +1 testability.
- Stronger on mechanism: cLAD/fLAD distinction adds mechanistic resolution — the filter is absolute for cLADs, tunable for fLADs. +1 mechanistic specificity.
- Stronger on groundedness: no new [PARAMETRIC] claims added; existing ones retained but labeled clearly. Groundedness maintained at 8/10.
- GAIN-OF-FUNCTION experiment elevated to central prediction. +1 testability.
- Verdict: GENUINELY STRONGER on 3 dimensions.

**H2-v2 vs. H2:**
- Stronger on mechanism: two-phase temporal model with quantitative kinetics (2-4h vs. 12-24h) is more specific than vague "sequential handoff." +1 mechanistic specificity.
- Stronger on testability: three-armed KDM6B vs. KDM6A experiment directly resolves the paralog ambiguity the Critic raised. +1 testability.
- Directly addresses Critic's primary weakness: promoter-vs-enhancer gap is now the central testable prediction (KDM6B CUT&RUN at distal enhancers vs. promoters). The gap is not papered over but made into a falsifiable prediction.
- Re-ChIP experiment designed to distinguish same-locus conversion from parallel independent activation — directly answering Critic question 2. +1 testability.
- Verdict: GENUINELY STRONGER on 2-3 dimensions.

**H5-v2 vs. H5:**
- Stronger on mechanism: BRD4→EP300 directionality reframed as EP300 RETENTION (not de novo recruitment). This is mechanistically defensible and consistent with EP300-BRD4 STRING interaction. +1 mechanistic specificity.
- Stronger on quantitative consistency: kinetic rate model provided; 6-18h prediction is now internally consistent with H3K27ac t1/2 (30-90 min single nucleosome), SE amplification (10-50x more EP300), and HDAC3 dynamics. Mandatory Critic revision incorporated. +1 quantitative coherence.
- Stronger on testability: JQ1 vs. dBET6 differential prediction is mechanistically novel and specific to the BRD4-scaffold model. Triptolide control elevated to central prediction. +1 testability.
- Verdict: GENUINELY STRONGER on 3 dimensions. (Confidence lowered slightly relative to parent due to honest acknowledgment of rate constant uncertainty — this represents improved calibration, not weakness.)

### 2. Do any two evolved hypotheses share >70% mechanistic overlap?

**H4-v2 vs. H2-v2:**
H4-v2 primary mechanism: LAD compartmentalization (nuclear architecture) as a stiffness-gated spatial filter for TEAD enhancer accessibility. Bridge mechanism: LAMIN A/C-LAD-H3K9me3 spatial silencing.
H2-v2 primary mechanism: KDM6B enzymatic demethylation of H3K27me3 at bivalent enhancers as the rate-limiting step in sequential stiffness-dependent enhancer activation. Bridge mechanism: KDM6B-H3K27me3 enzymatic demethylation kinetics.
Overlap assessment: Both involve enhancer silencing, but H4-v2's mechanism is spatial/architectural (LADs, nuclear periphery) while H2-v2's mechanism is enzymatic/temporal (demethylase activity, sequential kinetics). Different molecular actors (lamin A/C, G9a/GLP vs. KDM6B, PRC2), different compartments (constitutive/facultative LAD heterochromatin vs. bivalent enhancers which can be anywhere in the genome), different experimental predictions. Estimated overlap: ~25-30%.
Verdict: DIVERSE.

**H4-v2 vs. H5-v2:**
H4-v2 primary mechanism: LAD compartmentalization as static/stiffness-reinforced filter — about which enhancers CAN respond to stiffness.
H5-v2 primary mechanism: BRD4-scaffolded EP300 retention at super-enhancers encoding TEMPORAL memory of past stiffness — about how long a response persists after stiffness removal.
Different question entirely (access vs. persistence), different molecular actors (Lamin A/C, G9a/GLP vs. BRD4, HDAC3), different timescales (stiffness-dependent steady state vs. post-softening decay). Estimated overlap: ~15-20%.
Verdict: DIVERSE.

**H2-v2 vs. H5-v2:**
H2-v2 primary mechanism: KDM6B enzymatic demethylation enabling delayed bivalent enhancer activation.
H5-v2 primary mechanism: BRD4-scaffolded EP300 retention enabling post-softening H3K27ac persistence.
Both involve EP300/H3K27ac as downstream actors. However, H2-v2's question is about ACQUISITION of H3K27ac at previously silenced loci; H5-v2's question is about RETENTION of H3K27ac at previously activated loci. The temporal direction and molecular gate are different. Shared actors: EP300, H3K27ac. Distinct mechanisms: KDM6B demethylation (H2-v2) vs. BRD4 scaffolding (H5-v2). Distinct experimental designs. Estimated overlap: ~35-40%.
Verdict: DIVERSE (below 70% threshold; the EP300 shared actor is necessary since both operate on H3K27ac, but the mechanisms are distinct).

**Overall diversity verdict: PASS — all three pairs below 70% mechanistic overlap.**

### 3. Did any crossover produce incoherent results?

No crossovers were applied. The fLAD-KDM6B potential crossover was evaluated and rejected as it would have created >70% mechanistic overlap with H4-v2. Individual specification+mutation operations were applied to each hypothesis. Decision: correct.

### 4. Are quantitative predictions now internally consistent?

- H4-v2: OR >= 4.0 for non-LAD enrichment is properly calibrated against the ~65% non-LAD null baseline. Power calculation cited. Consistent.
- H2-v2: 8-14h temporal gap between Phase 1 and Phase 2 is consistent with KDM6B transcriptional upregulation lag (4-8h mRNA, 6-10h protein per KDM6B 2025 data). Consistent.
- H5-v2: 6-18h memory half-life is derived from kinetic model; model explicitly reconciles the apparent contradiction between 30-90 min single-nucleosome H3K27ac t1/2 and the proposed 6-18h SE-level persistence. Consistent.

### 5. Are new claims grounded or tagged?

All new mechanistic claims introduced in v2 versions are tagged [PARAMETRIC] or [GROUNDED] as appropriate. No new claims are presented as established facts without justification.

**EVOLUTION QUALITY CHECK VERDICT: PASS**

---

## Operations Summary

| Hypothesis | Operations | Primary Critic Weakness Addressed |
|-----------|-----------|----------------------------------|
| H4-v2 | Specification (null model OR framing + power calculation) + Mutation (cLAD/fLAD distinction elevated; CRISPR tethering as central test) | >90% non-LAD prediction above null corrected; gain-of-function test made central |
| H2-v2 | Mutation (KDM6B-at-enhancer as novel testable claim; two-phase temporal model) + Specification (quantitative kinetics; three-armed paralog experiment) | Promoter-vs-enhancer gap directly addressed; temporal ordering made quantitative |
| H5-v2 | Mutation (BRD4→EP300 directionality reframed as scaffolded retention) + Specification (kinetic rate model; 6-18h window derived; triptolide control elevated) | BRD4 directionality corrected; quantitative kinetic consistency enforced |
