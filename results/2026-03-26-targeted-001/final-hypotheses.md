# Final Hypotheses -- Session 2026-03-26-targeted-001 (BLIND MODE)

## Mechanobiology (ECM Mechanics) x Epigenomics (Genomic Enhancer Regulation)

---

## C2-H6: HDAC3-NCoR Eraser Depletion by ECM Stiffness Creates Enhancer Stabilization Independent of Writer Activation

**Verdict**: CONDITIONAL_PASS | **Composite**: 7.4 | **Confidence**: 4/10 | **Groundedness**: 6/10

**Core Claim**: ECM stiffening suppresses HDAC3 expression/activity (established by Fu et al. 2024 in chondrocytes), depleting the H3K27ac eraser at mechanosensitive enhancers. This creates enhancer stabilization by reducing deacetylation rate rather than increasing acetylation rate -- a paradigm inversion from the writer-activation models (YAP-EP300).

**Mechanism**: ECM stiffness (5-50 kPa) -> integrin/FAK signaling -> HDAC3-NCoR complex downregulation -> reduced H3K27ac deacetylation at active enhancers -> enhancer stabilization with unchanged EP300 activity -> amplified transcriptional output at pre-existing active enhancers

**Key Prediction**: HDAC3 ChIP-seq shows reduced HDAC3 occupancy at mechanosensitive enhancers on stiff ECM. HDAC3 overexpression abolishes stiffness-induced H3K27ac gain. TSA (pan-HDAC inhibitor) on soft ECM mimics stiffness H3K27ac pattern.

**Test Protocol**: MCF10A on PA hydrogels (1/10/50 kPa, 24h). HDAC3 ChIP-seq + H3K27ac CUT&Tag. HDAC3 OE lentiviral + TSA (50nM) + siFAK. EP300 activity assay (unchanged = eraser-depletion confirmed).

**Counter-evidence**: HDAC1/2 may compensate. Fu 2024 substrate was Parkin (non-histone), not enhancer H3K27ac. HDAC3 may be constitutively low at some enhancers.

---

## E1-H4: Mechanically-Induced H3K27ac as 6-12h Temporal Window for TET2-Mediated CpG Demethylation -> DNA Methylation Mechanical Memory

**Verdict**: CONDITIONAL_PASS | **Composite**: 7.2 | **Confidence**: 4/10 | **Groundedness**: 6/10

**Core Claim**: ECM stiffness-induced H3K27ac creates a 6-12h temporal window enabling TET2 recruitment and 5hmC deposition at mechano-enhancer CpG shores. BER converts 5hmC to unmethylated CpG within 24-72h. Demethylated CpGs persist days-to-weeks as mechanical memory beyond H3K27ac decay.

**Mechanism**: ECM stiffness -> YAP-EP300 -> H3K27ac at enhancers (0-12h window) -> TET2 recruitment via OGT/CXXC4 -> 5hmC deposition -> BER -> CpG demethylation (24-72h) -> persistent memory (days-weeks) -> asymmetric priming for future stiffness responses

**Key Predictions**:
1. RRBS: CpG demethylation >15% at mechano-enhancer shores after 50 kPa; >50% retained at day 3 post-transfer to 1 kPa
2. TET2 CUT&RUN: >3-fold enrichment at stiffness-gained H3K27ac peaks vs neutral peaks
3. siTET2 abolishes CpG demethylation but not H3K27ac levels
4. Priming: Previously stiff-exposed cells show >1.5x faster H3K27ac re-induction

**Test Protocol**: hMSCs on PA hydrogels (1 vs 50 kPa, transfer experiments). H3K27ac CUT&Tag + TET2 CUT&RUN + 5hmC DIP-seq + RRBS at multiple timepoints. siTET1/siTET2 genetics.

---

## E1-H3: Sequential Two-Phase Bivalent Enhancer Activation Under ECM Stiffness

**Verdict**: CONDITIONAL_PASS | **Composite**: 7.1 | **Confidence**: 5/10 | **Groundedness**: 6/10

**Core Claim**: ECM stiffness activates enhancers in two temporally distinct phases. Phase 1 (0-4h): YAP-EP300 acetylates non-bivalent enhancers at TEAD-motif sites. Phase 2 (12-24h): UTX (KDM6A)/MLL3-COMPASS resolves bivalent enhancers (H3K27me3+H3K4me1) to active (H3K27ac+H3K4me1). An 8-14h temporal gap between phases is the central falsifiable prediction.

**Key Predictions**:
1. Temporal gap >=8h between H3K27ac at non-bivalent (CTGF, 4-6h) and bivalent (SNAI1 distal, 12-18h) enhancers
2. siKDM6A (not siKDM6B) reduces bivalent H3K27ac >50% at 24h while leaving CTGF intact
3. A-485 at 0h blocks both phases; A-485 at 8h blocks Phase 2 but spares Phase 1

**Test Protocol**: hMSCs on PA hydrogels (1->50 kPa, time course). CUT&Tag H3K27ac + H3K27me3. KDM6A CUT&RUN. Four-arm siRNA (siKDM6A/siKDM6B/combined/NT). A-485 timing experiment (0h vs 8h).

---

## C2-H7: Integrin Force-Induced H3K9me3 Demethylation Creates Competence Windows for H3K27ac

**Verdict**: CONDITIONAL_PASS | **Composite**: 6.4 | **Confidence**: 3/10 | **Groundedness**: 5/10

**Core Claim**: Integrin-transmitted forces induce H3K9me3 demethylation at nuclear interior enhancers (building on Sun 2020), creating competence windows for subsequent H3K27ac activation. Two-key gating: H3K9me3 removal (30-120 min) must precede H3K27ac deposition (hours).

**Key Prediction**: H3K9me3 removal at mechano-enhancers precedes H3K27ac gain by 2-6h (time-course CUT&Tag). UNC0642 (H3K9me3 writer inhibitor) on soft ECM partially phenocopies stiff-ECM enhancer activation at interior genes.

---

## E1-H5: Dual YAP-TEAD + MRTF-SRF Programs in CTCF-Permitted Loop Domains

**Verdict**: CONDITIONAL_PASS | **Composite**: 6.3 | **Confidence**: 3/10 | **Groundedness**: 5/10

**Core Claim**: ECM stiffness activates two independent H3K27ac programs (YAP-TEAD at CTGF/CYR61 and MRTF-SRF at ACTA2/VCL) within pre-established CTCF loop domains. <20% shared target genes. Verteporfin suppresses Network A; C3-transferase suppresses Network B.

**Key Prediction**: H3K27ac HiChIP at 1/10/50 kPa reveals two non-overlapping contact networks. >70% of stiffness-gained loop pairs anchored within 10kb of constitutive CTCF sites.
