# Hypothesis Card: Sequential Two-Phase Bivalent Enhancer Resolution Under ECM Stiffness

**Session**: 2026-03-26-targeted-001 (Blind Mode — Holdout Validation)
**Target**: Mechanobiology (ECM mechanics) × Epigenomics (genomic enhancer regulation)
**ID**: H2-v2 | **Parent**: H2 — Coordinated Bivalent-to-Active Enhancer Conversion via Dual ECM-Stiffness-Controlled Enzymes (KDM6B + EP300)
**Generation cycle**: 1 (evolved, mutation + specification operations)
**Date**: 2026-03-26

---

## One-Line Summary

ECM stiffness drives a sequential two-phase bivalent enhancer activation program: Phase 1 (0–4h) sees fast EP300-dependent H3K27ac at accessible non-bivalent enhancers (CTGF, CYR61); Phase 2 (12–24h) sees delayed KDM6B demethylation of H3K27me3 at distal bivalent enhancers (SNAI1, RUNX2), creating an 8–14h temporal gap that constitutes the novel testable prediction and implies KDM6B demethylation is the rate-limiting gate for bivalent-to-active enhancer conversion at cell fate decision loci.

---

## Quality Gate Verdict

| Dimension | Score |
|---|---|
| Mechanistic Specificity | 1.5/2.0 |
| Novelty | 2.0/2.0 |
| Groundedness | 1.5/2.0 |
| Testability | 1.5/2.0 |
| Impact | 1.0/2.0 |
| **Total** | **7.5/10** |

**Verdict**: CONDITIONAL_PASS
**Confidence**: 0.62 | **Groundedness**: 7/10
**QG mode**: Post-blind web-verified (7+ searches, 0 citation hallucinations)
**Condition**: Remove/replace unverifiable "Whitworth 2024" citation (EP300-YAP at TEAD sites) with verified reference (e.g., PMID 38048728 or similar EP300-YAP study). Claim is independently supported; citation is not bridge-critical.
**Key novelty confirmation**: No paper proposes a two-phase temporal model for bivalent enhancer resolution under ECM stiffness. KDM6B 2025 ECM study is limited to promoters. KDM6B at distal enhancers shown in neuroblastoma (Nat Commun 2021, different context) but not in mechanosensing.

---

## Bridge Mechanism (A → B → C)

**A** — ECM stiffness (1–25 kPa): RhoA-ROCK1 → actomyosin contractility → YAP nuclear translocation (15–60 min); parallel: RhoA-MRTF-SRF → transcriptional upregulation of *KDM6B* (delayed, requires new protein synthesis, ~6–12h)

**B** — Sequential enzymatic handoff:
- Phase 1 (0–4h): YAP-TEAD + EP300 → H3K27ac at H3K4me1+/H3K27ac-accessible (non-bivalent) enhancers at CTGF, CYR61 loci
- Rate-limiting step: KDM6B demethylation of H3K27me3 at bivalent distal enhancers (H3K4me1+/H3K27me3+) is required before EP300 can acetylate H3K27; mutual exclusivity of H3K27me3 and H3K27ac enforces sequential operation
- Phase 2 (12–24h): RhoA-SRF-dependent KDM6B upregulation → KDM6B recruited to H3K4me1+ distal enhancers via PHD-Tudor domain recognition of H3K4me1 context [PARAMETRIC] → H3K27me3 removal → EP300 acetylation

**C** — Temporally gated bivalent-to-active enhancer conversion with 8–14h gap between Phase 1 and Phase 2 peaks; delayed activation of cell fate genes (SNAI1, RUNX2) requiring KDM6B-dependent bivalent resolution

---

## Detailed Mechanism

**Step 1** — Stiff ECM (>5 kPa, <10 min) activates integrin-FAK-RhoA-ROCK1 cascade → actomyosin contractility → cytoskeletal tension → YAP dephosphorylation and nuclear translocation (peak ~30–60 min). YAP binds TEAD and co-recruits EP300 to TEAD-binding sites at non-bivalent enhancers (YAP1-EP300 STRING: 0.692 [GROUNDED]).

**Step 2** — EP300 writes H3K27ac at non-bivalent enhancers (H3K4me1+, H3K27me3−, accessible nucleosomes): CTGF enhancer at ~2h, CYR61 enhancer at ~2–4h. These are the "fast" mechanosensitive targets representing Phase 1. At bivalent enhancers (H3K4me1+, H3K27me3+), EP300 cannot acetylate H3K27 because H3K27me3 occupies the same residue — mutual exclusivity enforces the temporal gate.

**Step 3** — Simultaneously, RhoA → MRTF-A/B nuclear accumulation → SRF-dependent transcription upregulates *KDM6B* (and other mechanoresponsive genes). KDM6B protein appears at ~6–12h (requiring mRNA synthesis and translation). KDM6B demethylates H3K27me3 at bivalent distal enhancers via its JmjC domain.

**Step 4** — KDM6B recruitment to distal bivalent enhancers (H3K4me1+, H3K27me3+) is the central novel testable claim [PARAMETRIC: PHD-Tudor domain recognition of H3K4me1 context inferred from KDM6B domain structure; KDM6B can act at enhancers per Nat Commun 2021 neuroblastoma]. Following demethylation, H3K27 becomes available for EP300 acetylation → Phase 2 H3K27ac deposition at SNAI1 distal enhancer (~12–18h), RUNX2 distal enhancer (~14–18h).

**Step 5** — Three-armed paralog disambiguation: GSK-J4 (inhibits both KDM6A/UTX and KDM6B) vs. siKDM6B (specific) vs. siKDM6A/UTX (specific) must be used to distinguish paralog contributions. KDM6A (UTX) is the canonical H3K27me3 demethylase at enhancers (MLL3/4-COMPASS complex); KDM6B at distal enhancers is the novel testable claim. Prediction: siKDM6B, not siKDM6A, blocks Phase 2 H3K27ac at bivalent distal enhancers.

---

## Quantitative Predictions

1. **Temporal gap** (primary): H3K27ac at non-bivalent enhancers (CTGF/CYR61) peaks at 4–6h; H3K27ac at bivalent enhancers (SNAI1/RUNX2 distal) peaks at 12–18h post-stiffening. Temporal gap ≥ 8h between peak times of two enhancer classes (Kolmogorov-Smirnov test, p < 0.001).

2. **KDM6B paralog specificity**: siKDM6B (not siKDM6A/UTX) reduces H3K27ac >50% at bivalent distal enhancers at 24h post-stiffening. GSK-J4 control inhibits both; siKDM6A control is non-effective at bivalent distal enhancers.

3. **KDM6B CUT&RUN** (causal): KDM6B enrichment at H3K4me1+ distal enhancers (confirmed bivalent by re-ChIP: H3K27me3 then H3K27ac at SNAI1 distal enhancer) detectable at 12–24h post-stiffening but not at 0–4h.

4. **Same-locus conversion** (mechanistic): Sequential re-ChIP experiment at SNAI1 distal enhancer: H3K27me3 antibody (Phase 1 time: 4h) → H3K27ac antibody (Phase 2 time: 18h) demonstrates same-locus conversion rather than parallel activation of distinct genomic elements.

---

## Experimental Protocol

**Cell model**: MCF10A or HFFs on polyacrylamide hydrogels (1 kPa soft / 10–25 kPa stiff), n = 3 biological replicates per time point, 5,000 cells/cm² at standardized density + fibronectin-coated 1,000 μm² circular micropatterns (decouple stiffness from spreading-area YAP activation).

**Time course**: 0, 2, 4, 8, 12, 18, 24h post-stiffening (transfer from soft → stiff PA gel).

**Readouts**:
- H3K27ac CUT&Tag (enhancer activation kinetics)
- H3K27me3 CUT&Tag (bivalent enhancer resolution)
- H3K4me1 CUT&Tag (enhancer identity marker)
- KDM6B CUT&RUN (recruitment to bivalent enhancers)

**Perturbations** (24h time point):
- GSK-J4 (1 μM, dual KDM6A/KDM6B inhibitor)
- siKDM6B (2 targeting siRNAs, confirm >80% protein knockdown)
- siKDM6A/UTX (2 targeting siRNAs)
- A-485 (3 μM, dual EP300+CBP inhibitor, to distinguish from CBP compensation)

**Validation assay**: Sequential re-ChIP (H3K27me3 → H3K27ac) at SNAI1 distal enhancer site (chr20:~48.6 Mb) at 4h and 18h time points.

**Transcriptional readout**: RT-qPCR for SNAI1, CTGF, CYR61, RUNX2 mRNA to confirm temporal correlation with enhancer activation kinetics.

**Timeline**: 6 months for time course CUT&Tag; 3 months for perturbation + KDM6B CUT&RUN; 3 months for re-ChIP; 12–15 months total.

---

## Key Literature

| Paper | Relevance |
|---|---|
| KDM6B 2025 (S2ID 251aa09; ECM stiffness thyroid cancer) | ECM stiffness upregulates KDM6B mRNA/protein; limited to promoters (SNAI1/TWIST promoters) |
| Rada-Iglesias et al. Genome Research 2011 | Bivalent enhancers (H3K4me1 + H3K27me3) defined as poised state |
| Dupont et al. Nature 2011 (PMID 21765798) | YAP nuclear translocation kinetics (15–60 min) |
| Hsia et al. J Cell Sci 2023 (PMID 37330288) | Force-epigenome mechanobiology review (mechanical memory context) |
| Zhu et al. Nat Commun 2021 | KDM6B at distal enhancers in neuroblastoma (partial supporting evidence for enhancer targeting) |
| Herz et al. Nat Struct Mol Biol 2010 | UTX (KDM6A) in MLL3/4-COMPASS at enhancers (canonical demethylase — KDM6B must be distinguished) |
| Xu et al. 2023 (PMID 37229211) | Matrix stiffness upregulates lamin A/C → chromatin changes |

---

## Known Concerns / Limitations

1. **KDM6B at distal enhancers is parametric**: The central novel claim. KDM6B at PROMOTERS is established (2025 ECM paper). KDM6B at DISTAL ENHANCERS is shown in neuroblastoma (Nat Commun 2021) but not confirmed in mechanosensing context. PHD-Tudor recognition of H3K4me1 is the proposed recruitment mechanism [PARAMETRIC].

2. **KDM6A vs. KDM6B identity**: KDM6A (UTX) is the canonical enhancer demethylase via MLL3/4-COMPASS; KDM6B is primarily known at promoters. The three-armed experiment is essential to disambiguate. If siKDM6B has no effect and siKDM6A does, the hypothesis needs revision.

3. **Same-locus vs. parallel activation**: The temporal gap could reflect activation of DIFFERENT enhancer subsets rather than sequential modification of the SAME enhancers. The re-ChIP experiment directly tests this.

4. **RhoA-SRF-KDM6B transcriptional link**: RhoA-MRTF-SRF is well-established; SRF → KDM6B transcriptional upregulation is inferred but unpublished [PARAMETRIC]. Need to verify KDM6B has SRF/MRTF-binding CArG boxes in its promoter.

5. **Unverifiable citation**: "Whitworth 2024" (EP300 at YAP-TEAD sites) is unverified. Replace with PMID 38048728 or similar verified EP300-YAP study. Claim is independently supported by STRING 0.692 and canonical YAP-EP300 biology.

---

## Evolutionary Improvements Over Parent (H2)

1. **KDM6B-at-enhancer elevated to central novel claim**: Parent extrapolated from promoter evidence. Evolved hypothesis designates KDM6B CUT&RUN at distal enhancers as the key falsification experiment. PHD-Tudor domain recognition is the [PARAMETRIC] recruitment mechanism.

2. **Sequential two-phase temporal model**: Parent assumed simultaneous coordination. Evolved hypothesis predicts 8–14h temporal gap with specific kinetics per enhancer class — a quantitatively precise and falsifiable prediction.

3. **Three-armed KDM6B vs. KDM6A experiment**: GSK-J4 (dual) vs. siKDM6B (specific) vs. siKDM6A (UTX-specific) to resolve paralog contributions and confirm KDM6B is the relevant enzyme at enhancers (not just UTX).
