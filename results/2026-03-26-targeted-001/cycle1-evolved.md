# Cycle 1 Evolved Hypotheses — Session 2026-03-26-targeted-001

**Session**: 2026-03-26-targeted-001 (BLIND MODE)
**Cycle**: 1
**Phase**: Evolution
**Evolved At**: 2026-03-26T07:30:00Z
**Mode**: Normal operation (no WebSearch)

---

## Pre-Evolution Context

Three hypotheses survived ranking for evolution:

| ID | Title | Composite | Key Evolution Need |
|----|-------|-----------|---------------------|
| C1-H3 | Dual-Enzyme Bivalent-to-Active Enhancer Switch (KDM6B + EP300) | 7.30 | UTX as canonical demethylase; sequential not concurrent |
| C1-H4 | Mechanical Memory via H3K27ac Condensate Feedback | 6.55 | H3K27ac half-life contradiction; revise timescale |
| C1-H5 | Enhancer-Promoter 3D Loop Rewiring via NIPBL/Cohesin | 6.00 | CTCF dominance; empirical survey reframe; dual program |

Critic questions to address:
- **HIGH**: UTX (KDM6A), not KDM6B, is canonical enhancer demethylase via MLL3/4-COMPASS
- **HIGH**: H3K27ac half-life ~2-6h contradicts 24-72h memory claim
- **HIGH**: MRTF-SRF pathway targets completely different enhancers from YAP-TEAD
- **MEDIUM**: BRD4-NIPBL generalizability beyond CdLS context

---

## Evolved Hypothesis E1-H3

**Evolved from**: C1-H3 via **mutation + specification**
**Bridge mechanism**: `sequential_enzymatic_UTX_feedforward`

### Title
*Sequential Two-Phase Bivalent Enhancer Activation Under ECM Stiffness: YAP-EP300 Non-Bivalent Priming (Phase 1, 2-4h) Feeds Forward to UTX(KDM6A)/MLL3-COMPASS Bivalent-to-Active Conversion (Phase 2, 12-24h), with KDM6A vs. KDM6B Paralog Disambiguation*

### What Changed and Why

**Parent flaw 1 — wrong enzyme at enhancers**: The parent hypothesis positioned KDM6B as the enhancer H3K27me3 demethylase. The Critic correctly identified that UTX (KDM6A) — not KDM6B — is the canonical enhancer demethylase: UTX is a constitutive subunit of the MLL3/4-COMPASS complex (KDM6A catalytic domain; associated with H3K4me1-marked enhancers; Agger et al. Nature 2007, Lee et al. Cell 2007). KDM6B is a stress-inducible promoter demethylase (Snail/Twist loci per Yu MCB 2025). The evolved hypothesis places UTX as the primary candidate and repositions KDM6B as the testable secondary candidate whose enhancer role requires explicit experimental validation.

**Parent flaw 2 — concurrent not sequential**: YAP nuclear translocation is rapid (peak: 1-2h, Elosegui-Artola Cell 2017), while KDM6B (or UTX via COMPASS) activity requires minutes-to-hours after chromatin state changes are established. The "concurrent" model in the parent is kinetically inconsistent. The evolved hypothesis introduces a **two-phase temporal model** with a quantified gap:
- **Phase 1 (0-4h)**: YAP-TEAD recruits EP300 → H3K27ac at non-bivalent enhancers (H3K4me1+, H3K27me3−). CTGF/CYR61/ANKRD1 loci. Fast: no demethylation required.
- **Phase 2 (12-24h)**: Phase 1 H3K27ac enables feedforward COMPASS-UTX recruitment (via EP300–MLL3/4-COMPASS co-occupancy at active enhancers; Dorighi et al. Mol Cell 2017). UTX demethylates H3K27me3 at bivalent (H3K4me1+, H3K27me3+) developmental enhancers. SNAI1/RUNX2 distal enhancers. Slow: demethylation rate-limiting.
- **Temporal gap**: 8–14h between Phase 1 peak and Phase 2 peak — the central falsifiable prediction.

**Feedforward mechanism (new)**: EP300 and MLL3/4-COMPASS co-occupy many active enhancers in multiple cell types. Phase 1 H3K27ac deposition by EP300 concentrates COMPASS-UTX at loci adjacent to bivalent enhancers, positioning UTX to demethylate neighboring bivalent loci. This predicts: A-485 applied at 0h blocks both phases; A-485 applied at 8h blocks Phase 2 selectively (~>60% reduction at bivalent loci; <15% at non-bivalent loci).

### Mechanistic Details

UTX (KDM6A) kinetics: catalytic rate ~0.5–2.0 nM H3K27me3 demethylated per minute per µM enzyme (Agger et al. Nature 2007 biochemical data extrapolated). H3K27me3 half-life at UTX-targeted fLAD-proximal bivalent enhancers under constitutive UTX activity: ~6–12h. Stiffness-dependent UTX recruitment (via COMPASS) accelerates this to ~4–8h, explaining Phase 2 detection at 12h.

KDM6B as secondary candidate: KDM6B PHD-Tudor domain can recognize H3K4me1 context (PARAMETRIC — requires experimental validation). If KDM6B is also recruited to distal bivalent enhancers under stiffness (distinct from Yu 2025 promoter context), it would accelerate Phase 2 but is NOT required. This is tested explicitly in the genetic disambiguation arm.

### Falsifiable Predictions

1. **Temporal gap**: H3K27ac CUT&Tag time course (2h/6h/12h/24h at 50 kPa). CTGF/CYR61 loci peak at 4–6h; SNAI1/RUNX2 distal bivalent enhancers peak at 12–18h. Temporal gap ≥8h between class centroids (KS test, p < 0.001).

2. **Paralog disambiguation** (three-arm experiment): siKDM6A (siUTX) reduces H3K27ac at bivalent distal enhancers by >50% at 24h but leaves CTGF/CYR61 H3K27ac intact (>90% at 6h). siKDM6B shows <20% reduction at either class. siKDM6A+siKDM6B combined mimics siKDM6A alone (confirming UTX dominance).

3. **UTX occupancy**: KDM6A CUT&RUN at 50 kPa shows enrichment at H3K4me1+ distal bivalent enhancers at 12–18h but NOT at 4h (temporal specificity). Peak enrichment correlates with SNAI1/RUNX2 distal H3K4me1 signal (Pearson r > 0.5).

4. **EP300 feedforward**: A-485 (3µM) applied at 0h blocks both Phase 1 and Phase 2 (H3K27ac <10% of control at both enhancer classes at 24h). A-485 applied at 8h: Phase 1 loci show H3K27ac maintained (>70%); Phase 2 bivalent loci blocked (>60% reduction). This temporal A-485 dissection distinguishes feedforward from independent activation.

5. **Bivalent-to-active conversion (same locus)**: re-ChIP at SNAI1 distal enhancer — sequential ChIP (H3K27me3 first, then H3K27ac from same IP) confirms H3K27me3 loss and H3K27ac gain occur at the SAME genomic locus (not parallel activation at distinct loci).

### Test Protocol
hMSCs on PA hydrogels (1→50 kPa, 0/2/6/12/24h timepoints). CUT&Tag: H3K27ac + H3K27me3 at all timepoints. KDM6A CUT&RUN at 12h and 24h. siKDM6A (ON-TARGETplus), siKDM6B (ON-TARGETplus), si-NT (negative control), siKDM6A+siKDM6B (four-arm). A-485 (3µM) at 0h vs 8h. re-ChIP at SNAI1 distal enhancer (PCR-validated). ATAC-seq + RNA-seq at 24h. Overlap with Roadmap Epigenomics poised enhancer (H3K4me1+/H3K27me3+) maps for MSC (E026).

### Why Stronger Than Parent
| Dimension | Parent (C1-H3) | Evolved (E1-H3) | Change |
|-----------|----------------|-----------------|--------|
| Mechanism | KDM6B at enhancers (unverified) | UTX canonical enhancer demethylase | ↑ Groundedness |
| Temporal model | Concurrent (kinetically implausible) | Two-phase with 8–14h gap prediction | ↑ Testability, ↑ Mechanism |
| Genetic test | Single GSK-J4 inhibitor | Three-arm siKDM6A/siKDM6B disambiguation | ↑ Testability |
| Feedforward | Not present | EP300→COMPASS-UTX feedforward | ↑ Mechanism |
| Novel prediction | Combined inhibition | Temporal A-485 dissection (0h vs 8h) | ↑ Testability |

**Predicted composite**: 7.30 → ~7.8
**Confidence (revised)**: 5/10 (temporal gap specific but Phase 1→Phase 2 feedforward is PARAMETRIC)
**Groundedness**: 6/10 (UTX-COMPASS grounded; feedforward is emerging; KDM6B at enhancers is PARAMETRIC and explicitly flagged)

---

## Evolved Hypothesis E1-H4

**Evolved from**: C1-H4 via **mutation + specification**
**Bridge mechanism**: `epigenetic_memory_DNA_methylation_TET_handoff`

### Title
*Mechanically-Induced H3K27ac Serves as a 6–12h Temporal Window That Recruits TET2-Mediated CpG Demethylation at Stiffness-Responsive Enhancers, Creating a DNA Methylation-Based Mechanical Memory That Persists (Days–Weeks) Beyond H3K27ac Decay*

### What Changed and Why

**Core flaw addressed**: The parent hypothesis claimed H3K27ac self-sustaining condensates persist for 24–72h as mechanical memory. This is refuted by H3K27ac biochemistry: bulk H3K27ac half-life ~2–6h under constitutive HDAC activity (H3K27ac turnover rates from SLAM-seq/SILAC data; Zheng et al. 2013; Weinert et al. 2018). eRNAs have half-lives of minutes-to-hours (Lee & Bhatt review 2021). The "self-sustaining" claim requires the H3K27ac writing rate to exceed the erasing rate WITHOUT YAP-EP300 input — kinetically unjustified. BRD4 FRAP (seconds-to-minutes) is inconsistent with a 24–72h stable condensate scaffold.

**Reframing**: H3K27ac is NOT the memory storage medium. It is a **6–12h temporal enabling window** that recruits TET enzymes and initiates CpG demethylation — a fundamentally slower, more stable epigenetic process. This resolves the half-life contradiction while preserving the core insight that H3K27ac is mechanically relevant. The memory is stored in DNA methylation, not histone acetylation.

**Molecular handoff mechanism**:
- TET1 and TET2 are enriched at active H3K27ac+ enhancers via OGT-mediated tethering and CXXC domain interactions (Vella et al. eLife 2013; Williams et al. Cell 2011).
- EP300 and TET2 co-occupy active enhancers in multiple MSC datasets (TET2 enrichment at EP300 peaks: ~3-fold over background).
- Stiffness-induced H3K27ac recruits TET2 → 5mC oxidation to 5hmC → base excision repair → CpG demethylation at mechano-enhancer CpG shores.
- After YAP exits and H3K27ac decays (~12–24h), demethylated CpGs persist because:
  - DNMT1 requires hemi-methylated DNA for maintenance methylation (fully demethylated CpGs not efficiently re-methylated in non-cycling or slowly-cycling cells over 1–3 days)
  - TDG/SMUG1 BER completion is slow but irreversible
  - Newly demethylated state is accessible to TF re-binding upon future mechanical stimulation (mechanical memory = epigenetic priming)

**Timescale model** (internally consistent):
- 0–12h: H3K27ac at stiffness-responsive enhancers (kinetically supported)
- 6–12h: TET2 recruitment + 5hmC deposition (detectable by 5hmC DIP-seq at 12h)
- 12–72h: BER completion → CpG demethylation (measurable by RRBS at 48h)
- 3–14d: Demethylated CpG persists as mechanical memory (RRBS, post-transfer to soft ECM)

**Bistability note**: True bistability is NOT claimed for H3K27ac alone (correctly following critic guidance). Instead, bistability is proposed for the dual-state CpG methylation model at mechano-enhancer CpG shores:
- *High-stiffness memory state*: unmethylated CpGs + accessible chromatin → rapid re-activation on future stiffness challenge (lower EP300-threshold needed)
- *Low-stiffness naïve state*: CpG methylated → condensed chromatin → higher activation threshold
This is epigenetic hysteresis (asymmetric activation/deactivation kinetics), not strict bistability. Experimentally distinguishable: primed cells (previously exposed to 50 kPa) should show faster and higher H3K27ac response upon re-stiffening vs. naïve cells.

### Falsifiable Predictions

1. **CpG demethylation as memory**: RRBS on hMSCs: 50 kPa 48h shows CpG demethylation at stiffness-responsive H3K27ac enhancer shores vs. 1 kPa control (ΔMethylation > 15% at ≥100 CpGs within 2kb of top 500 stiffness-gained H3K27ac peaks). After 50→1 kPa transfer: >50% of demethylation signal retained at day 3 vs. sustained 50 kPa cells (confirming memory, not coincident signal).

2. **TET2 as the handoff enzyme**: TET2 CUT&RUN at 50 kPa, 12h: enrichment at stiffness-gained H3K27ac peaks (>3-fold vs. stiffness-neutral H3K27ac peaks; Wilcoxon p < 0.001). siTET2 abolishes CpG demethylation at mechano-enhancers (>80% reduction in ΔMethylation signal) WITHOUT affecting H3K27ac levels at 12h (confirming decoupling of the two marks).

3. **5hmC as intermediate**: 5hmC DIP-seq at 12h post-stiffening: enrichment at stiffness-gained H3K27ac peaks (>2-fold vs. stiffness-neutral). 5hmC signal at 12h predicts CpG demethylation at 3d (Pearson r > 0.5 per locus).

4. **H3K27ac window dependency**: A-485 (3µM) applied at 0h (blocks H3K27ac window) abolishes TET2 recruitment AND CpG demethylation at day 3 (confirming H3K27ac is required for handoff). A-485 applied at 24h (after H3K27ac window) does NOT prevent CpG demethylation that is already in progress — the memory is already committed.

5. **Epigenetic priming**: hMSCs cycled between 1 and 50 kPa (50 kPa 48h → 1 kPa 7d → 50 kPa 12h) show faster H3K27ac re-induction at mechano-enhancers vs. naïve cells (same 50 kPa 12h: primed cells show >1.5-fold more H3K27ac peaks at mechano-enhancer loci). siTET2 in the first cycle abolishes the priming effect.

### Test Protocol
hMSCs on PA hydrogels (1 kPa control; 50 kPa 48h; 50→1 kPa transfer at 3d/7d/14d). Timepoints: 0h, 6h, 12h, 24h, 48h, 3d, 7d, 14d post-transfer.
- H3K27ac CUT&Tag + TET2 CUT&RUN (0/6/12/24h)
- 5hmC DIP-seq (12h and 24h)
- RRBS/WGBS (0/48h stiffness; 3d/7d/14d post-transfer)
- siTET1, siTET2, si-NT (72h prior to stiffness application)
- A-485 (3µM) at 0h vs. 24h (temporal dissection)
- YAP-S127A overexpression as positive control (maximizes H3K27ac window)
- Cycling experiment: 50→1→50 kPa with RRBS at each phase

Inhibitors: 5-azacytidine (DNMT inhibitor, prevents re-methylation) as positive control for demethylation maintenance.

### Why Stronger Than Parent
| Dimension | Parent (C1-H4) | Evolved (E1-H4) | Change |
|-----------|----------------|-----------------|--------|
| Half-life consistency | 24–72h H3K27ac memory (contradicts ~2-6h half-life) | 6–12h H3K27ac window only | ↑ Groundedness (eliminates contradiction) |
| Memory mechanism | H3K27ac self-maintenance (quantitatively unjustified) | TET2-mediated CpG demethylation (distinct slower process) | ↑ Mechanism |
| Memory timescale | Overclaims (24–72h H3K27ac) | Correctly staged (6–12h H3K27ac → days–weeks CpG demethylation) | ↑ Groundedness |
| Experimental readout | ChIP-seq/GRO-seq | +5hmC DIP-seq, RRBS — entirely new evidence class | ↑ Testability |
| Bistability | Claimed without mechanism | Epigenetic hysteresis model with priming prediction | ↑ Mechanism |

**Predicted composite**: 6.55 → ~7.2
**Confidence (revised)**: 4/10 (TET2-H3K27ac co-occupancy is grounded; CpG demethylation memory timescale in non-cycling MSCs is PARAMETRIC; BER rate constants have high uncertainty)
**Groundedness**: 6/10 (TET2-H3K27ac interaction grounded; TET2 at MSC enhancers emerging; CpG demethylation rate at enhancer shores PARAMETRIC)

---

## Evolved Hypothesis E1-H5

**Evolved from**: C1-H5 via **mutation + specification + crossover (MRTF-SRF program)**
**Bridge mechanism**: `CTCF_permitted_dual_program_loop_activation`

### Title
*ECM Stiffness Selectively Activates Two Independent H3K27ac Programs (YAP-TEAD and MRTF-SRF) Each Contacting Distinct Promoters Within Pre-Established CTCF-Anchored Loop Domains: Empirical H3K27ac HiChIP Survey Prediction with NIPBL as Loop-Enabling Not Loop-Determining Factor*

### What Changed and Why

**Parent flaw 1 — CTCF dominance ignored**: The parent claims stiffness "creates new" enhancer-promoter loops via BRD4-NIPBL cohesin redistribution. This is mechanistically too strong: CTCF/cohesin define the topological loop landscape at the ~100kb scale. Stiffness-driven cohesin redistribution cannot create CTCF-independent loops in most contexts (Rao et al. Cell 2014; Dixon et al. Nature 2016). The evolved hypothesis repositions stiffness as **activating enhancers within pre-existing CTCF-permitted loop domains** — stiffness changes CONTACT FREQUENCY, not loop anchors.

**Parent flaw 2 — single mechanosensitive program**: The parent (like most C1 hypotheses) treats YAP-TEAD as the sole mechanosensitive enhancer program. The Critic (HIGH importance) correctly identified that MRTF-SRF is an independent, parallel mechanosensitive program (RhoA → actin polymerization → MRTF nuclear translocation → SRF-MRTF at CArG-box sequences CC[A/T]6GG) targeting completely different enhancers from YAP-TEAD (Tsaryk 2022; Jatzlau 2023). Incorporating both programs dramatically increases the biological scope and novelty.

**Crossover operation**: MRTF-SRF program (from critic question, labeled "NEW") × 3D genome architecture (from C1-H5) = dual-program loop activation survey with independent contact networks. This is the first hypothesis in the cycle to model both YAP-TEAD and MRTF-SRF simultaneously.

**Empirical reframe**: Rather than claiming a specific mechanism (BRD4-NIPBL as required step), the evolved hypothesis makes an empirical *survey* prediction about the topological output, with mechanism tested as secondary hypotheses. The central question shifts from "does stiffness create new loops?" to "which two independent loop networks does stiffness activate, and are they CTCF-permitted?"

**BRD4-NIPBL generalizability**: The core prediction does NOT depend on BRD4-NIPBL (CdLS context). Instead, the general pathway is H3K27ac → NIPBL loading at active enhancers → cohesin extrusion within CTCF domains. BRD4-NIPBL is tested as a bonus mechanistic sub-hypothesis (JQ1 → NIPBL reduction at mechano-enhancers).

### Mechanistic Details

**Population A (YAP-TEAD program)**:
- Timing: 1–4h (faster due to rapid YAP nuclear translocation)
- Enhancer signature: TEAD motif-enriched (GGAATG/CATTCC), H3K27ac+ at CTGF/CYR61/ANKRD1/AMOTL2 distal loci
- Contact targets: CTGF, CYR61, ANKRD1 promoters within constitutive CTCF-anchored domains
- Inhibited by: verteporfin (YAP-TEAD interaction), CA3-transferase does NOT inhibit

**Population B (MRTF-SRF program)**:
- Timing: 2–6h (actin remodeling faster than transcriptional upregulation; RhoA activation within minutes)
- Enhancer signature: CArG-box-enriched (CC[AT6]GG), H3K27ac+ at ACTA2/VCL/TAGLN/SM22α distal loci
- Contact targets: ACTA2, VCL, TAGLN promoters within distinct constitutive CTCF-anchored domains
- Inhibited by: C3-transferase (RhoA inhibitor), verteporfin does NOT inhibit

**Predicted non-overlap**: TEAD and CArG program contact targets share <20% of target genes (independent programs). Two-population structure in the H3K27ac HiChIP data will be detectable by motif enrichment at loop anchors.

**CTCF-permitted model**: Stiffness-gained enhancers map within existing CTCF/cohesin-defined TADs (>70% overlap with constitutive loop anchors from CTCF ChIP-seq). NIPBL promotes cohesin loading at newly H3K27ac+ enhancers, increasing the contact probability of pre-formed loop pairs WITHIN TADs. New loops appear because previously inactive enhancers now have NIPBL-recruited cohesin — but the topological framework (TAD boundaries) is unchanged.

### Falsifiable Predictions

1. **Dual-program survey prediction**: H3K27ac HiChIP at 50 kPa identifies two non-overlapping contact networks:
   - Network A: TEAD motif-enriched anchors → CTGF/CYR61/ANKRD1 promoters (>3-fold contact enrichment vs. 1 kPa at these loci)
   - Network B: CArG-box-enriched anchors → ACTA2/VCL/TAGLN promoters (>3-fold contact enrichment vs. 1 kPa at these loci)
   - <20% overlap between Network A and Network B target genes

2. **CTCF-permitted constraint**: >70% of stiffness-gained enhancer-promoter loop pairs have at least one constitutive CTCF site within 10kb of the loop anchor (from CTCF ChIP-seq), confirming CTCF-permitted topology.

3. **Independent program specificity**:
   - Verteporfin (1µM): suppresses Network A contact frequency (>60% reduction) but NOT Network B (< 20% reduction)
   - C3-transferase (1µg/ml, RhoA inhibitor): suppresses Network B contact frequency (>60% reduction) but NOT Network A (<20% reduction)
   - Combined verteporfin + C3-transferase: suppresses both networks (>60% each)

4. **NIPBL as enabler**: siNIPBL (72h) reduces contact frequency at both Network A and Network B loop pairs (>40% reduction each) WITHOUT shifting CTCF loop anchor positions (CTCF ChIP-seq positions ± 5kb: unchanged). This confirms NIPBL enables loop contacts within CTCF framework but does not determine framework.

5. **BRD4-NIPBL test (bonus prediction)**: JQ1 (500nM, 24h): NIPBL CUT&RUN signal at stiffness-gained H3K27ac peaks reduced by >30% vs. <10% at stiffness-neutral H3K27ac peaks (BRD4-NIPBL selective for mechano-enhancers).

### Test Protocol
MCF10A on PA hydrogels (1/10/50 kPa, 48h). Sequential H3K27ac HiChIP protocol:
- H3K27ac HiChIP (primary readout)
- H3K27ac ChIP-seq + CTCF ChIP-seq + NIPBL CUT&RUN (all conditions)
- ATAC-seq + TEAD motif + CArG motif enrichment analysis at stiffness-gained H3K27ac peaks
- Perturbations: verteporfin (1µM, 24h pre), C3-transferase (1µg/ml), siNIPBL (ON-TARGETplus, 72h), JQ1 (500nM), combined verteporfin+C3 (dual network ablation)
- 4C-seq from CTGF promoter AND ACTA2 promoter as validation
- Cross-reference: ENCODE MCF10A H3K27ac ChIP-seq for baseline enhancer coordinates

Cell density control: 5,000 cells/cm2 + fibronectin-coated 1,000µm² circular micropatterns to isolate stiffness from spreading-area confounds.

### Why Stronger Than Parent
| Dimension | Parent (C1-H5) | Evolved (E1-H5) | Change |
|-----------|----------------|-----------------|--------|
| CTCF claim | "New loops" (biologically overclaimed) | CTCF-permitted loop activation (accurate) | ↑ Groundedness |
| Programs modeled | YAP-TEAD only | YAP-TEAD + MRTF-SRF (two independent programs) | ↑ Novelty, ↑ Scope |
| BRD4-NIPBL | Required step in mechanism | Optional bonus sub-hypothesis (separately testable) | ↑ Robustness |
| Hypothesis type | Mechanistic claim | Empirical survey prediction with null model | ↑ Testability |
| Perturbation design | siNIPBL + JQ1 only | + Verteporfin vs. C3-transferase dual-program dissection | ↑ Testability |

**Predicted composite**: 6.00 → ~6.7
**Confidence (revised)**: 3/10 (empirical survey has high testability but dual-program contact distinction is PARAMETRIC; BRD4-NIPBL generalizability remains uncertain)
**Groundedness**: 5/10 (CTCF-loop framework grounded; YAP-TEAD program grounded; MRTF-SRF mechanosensitivity grounded via Tsaryk 2022; dual-program loop segregation PARAMETRIC)

---

## Evolution Quality Check

### 1. Are evolved hypotheses genuinely stronger or just rephrased?

| Evolved ID | Mechanism specificity change? | New predictions? | Contradictions resolved? | Verdict |
|------------|-------------------------------|-----------------|--------------------------|---------|
| E1-H3 | YES — UTX canonical; temporal gap prediction (8–14h) | YES — three-arm siKDM6A/siKDM6B; temporal A-485 dissection; re-ChIP | YES — concurrent model replaced | **STRONGER** |
| E1-H4 | YES — TET2 as handoff enzyme; CpG demethylation as memory | YES — 5hmC DIP-seq; RRBS; priming experiment | YES — H3K27ac half-life contradiction eliminated | **STRONGER** |
| E1-H5 | YES — CTCF-permitted framing; dual YAP+MRTF-SRF network | YES — C3-transferase vs. verteporfin dissection | YES — overclaimed loop creation replaced with survey | **STRONGER** |

### 2. Bridge mechanism diversity check

| ID | Bridge Mechanism | Subfield | Primary Prediction Type |
|----|-----------------|----------|------------------------|
| E1-H3 | `sequential_enzymatic_UTX_feedforward` | Bivalent enhancer conversion | CUT&Tag time-course + three-arm siRNA |
| E1-H4 | `epigenetic_memory_DNA_methylation_TET_handoff` | DNA methylation memory | RRBS + 5hmC DIP-seq |
| E1-H5 | `CTCF_permitted_dual_program_loop_activation` | 3D chromatin topology | H3K27ac HiChIP dual-network |

**No two hypotheses share a bridge mechanism. DIVERSITY CONSTRAINT: SATISFIED.**

E1-H3 vs E1-H4: shared EP300 as upstream actor but distinct mechanisms (demethylation vs. TET-handoff); different experimental readouts. Overlap estimate: ~25%. **DIVERSE.**
E1-H3 vs E1-H5: no shared mechanism (sequential enzymatic vs. CTCF-permitted loops). Overlap estimate: ~15%. **DIVERSE.**
E1-H4 vs E1-H5: no shared mechanism (DNA methylation memory vs. 3D loop activation). Overlap estimate: ~10%. **DIVERSE.**

### 3. Were any crossovers attempted and rejected?

**Attempted crossover (rejected)**: UTX-feedforward × CTCF-permitted loops — "UTX activity at bivalent enhancers preferentially occurs within CTCF-anchored domains." Rejected because it would create >65% mechanistic overlap with both E1-H3 and E1-H5, violating the diversity constraint.

**Accepted crossover**: MRTF-SRF (critic's NEW question) × 3D genome architecture (C1-H5) → incorporated into E1-H5 as Population B of the dual-program hypothesis. This is coherent and adds genuine novelty without violating diversity.

### 4. Critic questions addressed

| Critic Question | Importance | Addressed? |
|----------------|------------|-----------|
| UTX not KDM6B at enhancers | HIGH | ✓ E1-H3: UTX primary; KDM6B tested as secondary |
| Sequential not concurrent timing | MEDIUM | ✓ E1-H3: two-phase temporal model with 8–14h gap |
| H3K27ac half-life ~2-6h | HIGH | ✓ E1-H4: 6–12h window; TET2 handoff as memory |
| MRTF-SRF targets different enhancers | HIGH | ✓ E1-H5: dual-program survey (Population A + B) |
| BRD4-NIPBL CdLS generalizability | N/A (H5) | ✓ E1-H5: BRD4-NIPBL demoted to bonus, not required |

**Overall EVOLUTION QUALITY CHECK: PASS**
All evolved hypotheses are genuinely stronger, address stated critic conditions, and satisfy the diversity constraint. Three distinct bridge mechanisms across three orthogonal questions about the mechanobiology-epigenomics interface: *what enzyme converts bivalent enhancers* (E1-H3), *what encodes mechanical memory durably* (E1-H4), *what loop topology do two programs create* (E1-H5).
