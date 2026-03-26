# Cycle 2 Ranking — Session 2026-03-26-targeted-001

**Target:** Mechanobiology (extracellular matrix mechanics) × Epigenomics (genomic enhancer regulation)
**Mode:** BLIND
**Hypotheses ranked:** 8 (5 C2 survivors + 3 C1 evolved)
**Ranker model:** sonnet
**Generated:** 2026-03-26

---

## Note on Cross-Domain Bonus

All 8 hypotheses bridge ECM mechanobiology and epigenomics — both subfields within biomedical cell biology. The v5.8 cross-domain bonus (+0.5) applies when a hypothesis "bridges domains that span 2+ disciplinary boundaries" with examples of materials science → neuroscience, topology → developmental biology. Mechanobiology → Epigenomics are adjacent disciplines within the life sciences; both rely on the same retrieval infrastructure (PubMed, KEGG, STRING), the stated reason for the bonus. **No cross-domain bonus is applied.** This differs from Cycle 1 scoring (which applied +0.5 uniformly) but is the correct interpretation of the v5.8 rule. Future sessions in non-biomedical domains would qualify.

---

## Per-Hypothesis Scoring Tables

---

### Hypothesis C2-H6: HDAC3-NCoR Eraser Depletion by ECM Stiffness

*Full title: HDAC3-NCoR Eraser Depletion by ECM Stiffness Creates Enhancer Stabilization Independent of Writer Activation*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic confirmed: "eraser-depletion model is conceptually orthogonal to all writer-activation models in the field. No paper has connected ECM stiffness → HDAC3 loss → enhancer landscape changes." All mechanoepigenetics papers assume writer activation; C2-H6 inverts the paradigm entirely. This represents a genuine creative inversion, not an incremental extension. |
| Mechanistic Specificity | 20% | 7 | Clearly names HDAC3-NCoR/SMRT complex, Fu 2024 as anchor evidence, H3K27ac retention via reduced eraser kinetics, and a triple orthogonal experimental design (RGFP966/A-485/AAV rescue). Two parametric claims (HDAC3 dominance at enhancers vs HDAC1/2 compensation, H3K27ac half-life extension magnitude) prevent a higher score. The mechanism is more directional (depletion → retention) than most cascade models. |
| Cross-field Distance | 10% | 5 | Bridges ECM stiffness sensing (mechanobiology) and histone deacetylation/enhancer stability (epigenomics). Adjacent disciplines within biomedical cell biology — the same range as all hypotheses in this session. No bonus warranted; both communities share core methodology and vocabulary. |
| Testability | 20% | 9 | Best experimental design in the entire batch per Critic. The triple test is elegant: RGFP966 on soft ECM (phenocopies eraser-stabilized subset), A-485 on stiff ECM (removes writer-activated but spares eraser-stabilized), HDAC3 AAV rescue on stiff ECM (collapses eraser-stabilized). All established methods (WB, ChIP-seq, AAV). A PhD student could execute this in ~3 months with standard cell biology equipment. |
| Impact | 10% | 7 | Would redirect the mechanoepigenetics field from exclusive writer-activation focus to include eraser depletion as an independent mechanism. Opens HDAC3-targeting therapeutic strategies for fibrosis/stiffness diseases. Establishes a new mechanistic category (eraser-based enhancer stabilization). Moderate-to-high impact for the field. |
| Groundedness | 20% | 6 | Groundedness 67% (4/6 grounded). All 4 citations verified with zero hallucinations: Fu Bone Research 2024 ✓, You Cell 2013 ✓, Xu Materials Today Bio 2023 ✓, Watson Nature 2012 ✓. Key limitation: Fu 2024 used HDAC3→Parkin (a non-histone substrate) in chondrocytes during OA-related stiffening — the connection to enhancer H3K27ac is an inference not yet demonstrated. HDAC3 dominance at enhancers across cell types is parametric. |
| **Composite** | | **7.4** | 0.20×9 + 0.20×7 + 0.10×5 + 0.20×9 + 0.10×7 + 0.20×6 = 1.8+1.4+0.5+1.8+0.7+1.2 |

---

### Hypothesis E1-H4: TET2-DNA Methylation Memory Handoff

*Full title: Mechanically-Induced H3K27ac Serves as a 6-12h Temporal Window That Recruits TET2-Mediated CpG Demethylation at Stiffness-Responsive Enhancers, Creating a DNA Methylation-Based Mechanical Memory That Persists (Days-Weeks) Beyond H3K27ac Decay*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The H3K27ac temporal window → TET2 recruitment → 5hmC → CpG demethylation → mechanical memory handoff is novel. TET2 is established in development and cancer contexts, but has never been linked to ECM stiffness mechanotransduction. The "temporal window handoff" framing (H3K27ac as a transient enabling signal rather than the memory medium itself) is a creative reframing. Some novelty diluted because TET enzymes at H3K27ac+ enhancers is established in other contexts (Vella 2013, Williams 2011). |
| Mechanistic Specificity | 20% | 8 | Highly specific: TET2 recruited within the 6-12h H3K27ac window via OGT/CXXC domain targeting, 5hmC intermediate, TDG-mediated BER completion (24-72h), DNMT1 maintenance kinetics in non-cycling hMSCs. Internally consistent timescales. The priming cycling experiment (50→1→50 kPa) with siTET2 in first cycle is a particularly specific prediction. Three parametric claims (TET2 co-occupancy under stiffness, CpG demethylation rate, DNMT1 kinetics) are acknowledged. |
| Cross-field Distance | 10% | 5 | ECM mechanobiology → DNA methylation memory (epigenomics). Adjacent biomedical sub-disciplines; same range as others in this session. DNA methylation is slightly further from cell mechanics than histone acetylation, but still firmly within molecular cell biology. |
| Testability | 20% | 9 | Excellent experimental suite introducing entirely new evidence classes: 5hmC DIP-seq, RRBS (days-to-weeks timescale), priming cycling experiment. All are established methods; the combination is comprehensive. TET2 CUT&RUN + siTET2 dissection + A-485 timing + 5-azacytidine positive control provides very high experimental rigor. |
| Impact | 10% | 7 | Would establish a new mechanism for long-term mechanical memory that operates at the DNA methylation level, independent of histone modifications. Has implications for fibrosis, cancer stroma stiffening, and developmental mechanobiology. The priming/hysteresis prediction is particularly impactful — it would explain why cells that experienced stiffness respond differently upon re-stiffening. |
| Groundedness | 20% | 6 | Groundedness=6 (from Evolver). TET2-H3K27ac co-enrichment generally grounded (Williams 2011, Vella 2013); TET2 biochemistry (5mC→5hmC→5fC→5caC) and TDG-BER well-established. The key novel claim — TET2 co-occupancy at stiffness-gained H3K27ac peaks in hMSCs — is parametric. Timescale consistency (6-12h window, BER 24-72h) is internally sound based on known kinetics. |
| **Composite** | | **7.2** | 0.20×7 + 0.20×8 + 0.10×5 + 0.20×9 + 0.10×7 + 0.20×6 = 1.4+1.6+0.5+1.8+0.7+1.2 |

---

### Hypothesis E1-H3: Sequential Two-Phase UTX Bivalent Enhancer Activation

*Full title: Sequential Two-Phase Bivalent Enhancer Activation Under ECM Stiffness: YAP-EP300 Non-Bivalent Priming (Phase 1, 2-4h) Feeds Forward to UTX(KDM6A)/MLL3-COMPASS Bivalent-to-Active Conversion (Phase 2, 12-24h), with KDM6A vs. KDM6B Paralog Disambiguation*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The two-phase feedforward temporal model (EP300 Phase 1 primes, UTX-COMPASS Phase 2 converts bivalent enhancers, 8-14h gap) is novel. The UTX specification (over KDM6B) was indicated by Critic questions, so this is a directed improvement rather than an independent discovery. No paper proposes a strict EP300→COMPASS feedforward cascade at enhancers under ECM stiffness. The paralog disambiguation (siKDM6A vs siKDM6B) is a genuinely new experimental prediction. |
| Mechanistic Specificity | 20% | 8 | Exceptionally specific: Phase 1 (0-4h, EP300 at non-bivalent CTGF/CYR61 loci) → Phase 2 (12-24h, UTX-COMPASS at bivalent SNAI1/RUNX2 distal loci), 8-14h temporal gap, A-485 at 0h vs 8h dissection, four-arm siRNA experiment (siKDM6A/siKDM6B/combined/NT), KDM6A CUT&RUN time-course. The feedforward mechanism (BRD4-NIPBL-mediated proximity from Dorighi 2017 extended) remains parametric but is grounded in existing co-occupancy data. |
| Cross-field Distance | 10% | 5 | ECM stiffness mechanobiology → bivalent enhancer biology (epigenomics). Standard bridge distance for this session. |
| Testability | 20% | 9 | All methods are established (PA hydrogels, CUT&Tag, CUT&RUN, siRNA). The four-arm siRNA experiment is definitive for paralog disambiguation. The A-485 timing experiment (0h vs 8h) cleanly tests feedforward dependency. Phase-specific inhibitor sensitivity is an elegant experimental logic. A PhD student with access to PA hydrogel equipment could execute this in 3 months. |
| Impact | 10% | 6 | Would establish the first temporal model of enhancer activation under ECM stiffness, clarify UTX vs KDM6B roles in mechanosensing, and provide the first evidence for a feedforward enhancer cascade under mechanical stimulation. Important for mechanobiology and chromatin biology, but more incremental than E1-H4 (no new evidence class) and less paradigm-shifting than C2-H6 (conceptual inversion). |
| Groundedness | 20% | 6 | Groundedness=6. EP300-BRD4 co-occupancy (STRING 0.988), CTGF/CYR61 as canonical YAP targets, EP300-MLL3/4-COMPASS co-occupancy at enhancers (Dorighi Cell 2017), UTX as canonical COMPASS-associated enhancer demethylase — all grounded. The feedforward mechanism, 8-14h temporal gap as a mechanistic (not kinetic) prediction, and COMPASS transfer mechanism are parametric. Zero citation hallucinations in generation. |
| **Composite** | | **7.1** | 0.20×7 + 0.20×8 + 0.10×5 + 0.20×9 + 0.10×6 + 0.20×6 = 1.4+1.6+0.5+1.8+0.6+1.2 |

---

### Hypothesis C2-H2: Integrated Three-Phase Enhancer Memory Cascade with Feedforward

*Full title: Integrated Three-Phase Enhancer Memory Cascade with Strict Feedforward Dependencies Under ECM Stiffness*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The three-phase strict feedforward cascade (EP300 Phase 1 → UTX-COMPASS Phase 2 → TET2 Phase 3) is novel as an integrated hypothesis. No paper proposes this three-phase hierarchy under ECM stiffness. However, novelty is partially diluted because C2-H2 explicitly extends E1-H3 and E1-H4 — it is an integration rather than an independent discovery. The novel contribution is the STRICT FEEDFORWARD dependency claim (each phase requires the previous). |
| Mechanistic Specificity | 20% | 7 | Very specific: three phases with distinct time windows, molecular steps (BRD4-NIPBL proximity, COMPASS transfer, TDG-BER), and phase-specific inhibitors. The strict hierarchy prediction (A-485 at 0h blocks all three; at 8h blocks Phase 2+3; siTET2 blocks only Phase 3) is an unusually precise mechanistic fingerprint. Parametric: the feedforward mechanism itself, COMPASS transfer via BRD4-NIPBL proximity, and strict one-directional dependency. |
| Cross-field Distance | 10% | 5 | Same bridge as E1-H3 and E1-H4. |
| Testability | 20% | 8 | Phase-specific inhibitor timing (A-485 at 0h vs 8h, GSK-J4, siTET2, siNIPBL) combined with CUT&Tag time-course and RRBS provides excellent experimental granularity. All methods established. Slightly below E1-H3 and E1-H4 (9) because C2-H2 requires validating the full three-phase hierarchy simultaneously, which is more complex to interpret. The 4C-seq adds technical load. |
| Impact | 10% | 7 | A confirmed three-phase feedforward enhancer cascade would be a significant discovery — potentially a general model for how sequential chromatin state transitions are wired under mechanical stimulation. Would inform understanding of fibrosis, mechanically-driven cell fate, and epigenetic reprogramming. Higher impact potential than individual phase hypotheses alone. |
| Groundedness | 20% | 5 | Groundedness=5, 56% (5/9 grounded). EP300-BRD4 interaction (STRING 0.988), CTGF/CYR61 as YAP targets, EP300-COMPASS co-occupancy (Dorighi 2017), TET2 oxidation cascade, TDG-BER — all grounded. But the feedforward dependency, COMPASS transfer mechanism, and strict one-directional hierarchy are all parametric. The key novel claim (strict feedforward) is explicitly challenged by independent UTX-COMPASS recruitment via MLL3/4 PHD→H3K4me1. |
| **Composite** | | **6.6** | 0.20×7 + 0.20×7 + 0.10×5 + 0.20×8 + 0.10×7 + 0.20×5 = 1.4+1.4+0.5+1.6+0.7+1.0 |

---

### Hypothesis C2-H7: H3K9me3 Demethylation Competence Windows

*Full title: Integrin Force-Induced H3K9me3 Demethylation at Nuclear Interior Enhancers Creates Competence Windows for H3K27ac Activation*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Novel extension of Sun 2020 (which showed force→H3K9me3 demethylation at promoters) to enhancers, combined with the "competence window" concept (accessible but not yet active). No paper proposes force-induced H3K9me3 demethylation at enhancers under ECM stiffness. The two-step model (Step 1: derepression via H3K9me3 removal; Step 2: activation via H3K27ac gain) is a creative borrowing from developmental biology's "poising" concept. |
| Mechanistic Specificity | 20% | 6 | Names specific molecular actors (integrin-LINC-KDM4A, H3K9me3 removal at nuclear interior enhancers, DamID-seq for lamin B1 localization, chaetocin+ML324 perturbations). But KDM4A identity is explicitly speculative (Sun 2020 did not identify the enzyme), the cyclic vs. static force transfer mechanism is unaddressed, and the "5-15% of enhancers" estimate is parametric. Missing the mechanistic link from sustained static ECM stiffness to KDM4A activation. |
| Cross-field Distance | 10% | 6 | Slightly higher than other hypotheses: bridges physical force transmission (mechanobiology/biophysics) directly to heterochromatin derepression (epigenomics) via nuclear mechanics, skipping the standard biochemical signaling relay. The force-to-chromatin-structure bridge is more physically direct than the signaling-based hypotheses, making it marginally farther from standard epigenomics. |
| Testability | 20% | 8 | Well-designed: CUT&Tag H3K9me3/H3K27ac/H3K4me1 time course, DamID-seq for nuclear interior mapping, chaetocin±YAP(S127A) two-step dissection, ML324 KDM4A inhibitor, magnetic bead replication of Sun 2020 on soft ECM. All established methods. Sun 2020 replication provides solid experimental anchor. Slightly below E1-H3/H4 because the cyclic vs. static force issue adds a required preliminary validation step. |
| Impact | 10% | 6 | Would establish force-induced heterochromatin derepression as a new mechanistic class in mechanoepigenetics, distinct from all signaling-based approaches. Provides a physical bridge between nuclear mechanics and epigenome regulation that bypasses the biochemical relay. Moderate impact — field-important but not paradigm-transforming given that only 5-15% of enhancers may be in H3K9me3 domains. |
| Groundedness | 20% | 5 | Groundedness=5, 50% (3/6 grounded). Sun Sci Advances 2020 for force→H3K9me3 demethylation at nuclear interior ✓, Roadmap Epigenomics for H3K4me1+H3K9me3 co-occurrence ✓, nuclear interior vs periphery differential force response (Sun 2020) ✓. KDM4A identity, 5-15% enhancer fraction estimate, and two-step model are all parametric. The fundamental concern — Sun 2020 used cyclic magnetic bead force, not static ECM stiffness — undermines the direct mechanistic grounding. |
| **Composite** | | **6.4** | 0.20×7 + 0.20×6 + 0.10×6 + 0.20×8 + 0.10×6 + 0.20×5 = 1.4+1.2+0.6+1.6+0.6+1.0 |

---

### Hypothesis E1-H5: Dual YAP+MRTF in CTCF-Permitted Domains

*Full title: ECM Stiffness Selectively Activates Two Independent H3K27ac Programs (YAP-TEAD and MRTF-SRF) Each Contacting Distinct Promoters Within Pre-Established CTCF-Anchored Loop Domains*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Dual-program (YAP-TEAD + MRTF-SRF) contact network analysis with CTCF-permitted framing is novel. H3K27ac HiChIP under ECM stiffness looking at two programs simultaneously has not been done. The CTCF-permitted reframing (activating within existing topology vs. creating new loops) is more conservative than the parent but more grounded. The non-overlapping contact network prediction (<20% shared targets) is testable and non-trivial. |
| Mechanistic Specificity | 20% | 7 | Specific: TEAD-motif vs CArG-box enhancers, separate contact networks, CTCF-anchored loop domain constraint, NIPBL-cohesin extrusion mechanism, verteporfin vs C3-transferase dissection, HiChIP + 4C-seq from CTGF and ACTA2 promoters. BRD4-NIPBL demoted to secondary. Parametric: non-overlapping contact networks prediction, CArG-motif contact frequency enhancement under stiffness. |
| Cross-field Distance | 10% | 5 | ECM stiffness → 3D chromatin architecture / epigenomics. Slightly farther (physical chromatin topology vs biochemical histone modification) but still within cell biology. |
| Testability | 20% | 7 | HiChIP is more technically demanding and expensive than CUT&Tag/ChIP-seq (requires more cells, sophisticated library prep, expensive sequencing). The dual program + multiple inhibitor design is comprehensive but complex. 4C-seq adds further technical load. Achievable in a well-equipped genomics lab but not routine for a standard cell biology lab. 3-4 months with good HiChIP expertise. |
| Impact | 10% | 6 | Would show how two independent mechanosensing transcription factor programs create distinct 3D chromatin contact networks. Advances understanding of chromatin topology in mechanosensing. Important for the field but somewhat descriptive (empirical survey rather than mechanistic model). The CTCF-permitted framing limits the mechanistic claim. |
| Groundedness | 20% | 5 | Groundedness=5. CTCF loop topology well-established, NIPBL-cohesin mechanism grounded, MRTF-SRF targets CArG-box enhancers (Miralles 2003) ✓, YAP-TEAD targets TEAD motifs ✓. The specific predictions (non-overlapping contact networks, CArG-motif HiChIP signal under stiffness) are parametric. CTCF positions unchanged under stiffness is plausible but not verified. |
| **Composite** | | **6.3** | 0.20×7 + 0.20×7 + 0.10×5 + 0.20×7 + 0.10×6 + 0.20×5 = 1.4+1.4+0.5+1.4+0.6+1.0 |

---

### Hypothesis C2-H3: Differential Stiffness Thresholds YAP vs MRTF (Decoder)

*Full title: Differential Stiffness Thresholds for YAP-TEAD vs. MRTF-SRF Create a Tissue-Stiffness-to-Enhancer Decoder*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | The stiffness decoder model with comparative thresholds (MRTF ~5-10 kPa, YAP ~15-25 kPa) is conceptually novel as a systematic study — no paper has mapped both programs across fine-grained stiffness gradients with enhancer resolution. However, the concept of MRTF activating at lower stiffness than YAP is a relatively intuitive extension of known G-actin dynamics, and the Critic notes this was explicitly requested from C1 criticism. The decoder framing is creative but less surprising than the mechanistic inversions in C2-H6 or C2-H7. |
| Mechanistic Specificity | 20% | 5 | Names specific thresholds (MRTF ~5-10 kPa, YAP ~15-25 kPa), motifs (CArG-box vs TEAD), and inhibitors (verteporfin vs CCG-1423 at 10 kPa). But MRTF threshold is entirely parametric with no direct measurement data — the core novel claim is an estimate with no experimental anchor. The "ratchet mechanism" (MRTF→contractility→stiffening→YAP) is a reasonable model but mechanistically unspecified. |
| Cross-field Distance | 10% | 5 | Standard bridge for this session. |
| Testability | 20% | 9 | Highest testability in the C2 batch: 7-stiffness-gradient (0.5/2/5/10/15/25/50 kPa) with dual inhibitor dissection (verteporfin vs CCG-1423), H3K27ac ChIP-seq + ATAC-seq, MRTF-A/YAP IF dose-response, CArG vs TEAD motif enrichment analysis. All established methods. The experiment is elegant and would be definitive. Very clean null model structure. |
| Impact | 10% | 6 | Would provide the first stiffness-to-enhancer decoder map. Important for understanding fibrosis progression (why ~15 kPa feels like a tipping point for tissue stiffness diseases), cancer stroma, and developmental tissue patterning. Moderate impact — primarily a characterization study rather than a mechanistic discovery. |
| Groundedness | 20% | 5 | Groundedness=5, 50% (4/8 grounded). MRTF-A sequestration by G-actin (Miralles 2003) ✓, YAP threshold ~15-20 kPa in hMSCs (Dupont 2011) ✓, CArG-box ✓, TEAD motif ✓. MRTF threshold ~5-10 kPa is entirely parametric with no direct measurement. Critic noted cardiac fibroblasts require ~25 kPa for MRTF — same as YAP, which would collapse the decoder model. |
| **Composite** | | **6.1** | 0.20×6 + 0.20×5 + 0.10×5 + 0.20×9 + 0.10×6 + 0.20×5 = 1.2+1.0+0.5+1.8+0.6+1.0 |

---

### Hypothesis C2-H1: Metabolic Gatekeepers (Acetyl-CoA / α-KG)

*Full title: Acetyl-CoA and α-Ketoglutarate as Metabolic Gatekeepers for the ECM Stiffness-Enhancer Enzyme Cascade*

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 5 | Critic: "PARTIAL — metabolic-epigenetic nexus is heavily studied (Wellen 2009, Carey 2015, Lu & Thompson 2012). Bertero 2016 already connected stiffness → glutaminolysis via YAP." The narrow remaining novelty — nuclear metabolite levels being RATE-LIMITING for enhancer enzyme activity under ECM stiffness — is plausible but quantitatively implausible given cofactor concentrations 5-100x above enzyme Km. Novelty exists in the specific ECM stiffness context but the metabolic-epigenetic link itself is well-trodden. |
| Mechanistic Specificity | 20% | 6 | Names specific molecules: ACLY → acetyl-CoA → EP300, glutaminolysis → αKG → UTX/TET2, ACSS2 backup, specific inhibitors (SB-204990, BPTES) and rescue agents (dmαKG, sodium acetate). The experimental design (orthogonal metabolic dissection of the temporal cascade) is clever. Penalized because the core rate-limiting claim is mechanistically implausible: acetyl-CoA (~10-50 µM) is 5-10x above EP300 Km (~0.5-4 µM), and αKG (~100-400 µM) is 5-100x above UTX Km (~2-60 µM). |
| Cross-field Distance | 10% | 5 | Mechanobiology → metabolism → epigenomics. Includes metabolism as an intermediary field, making this a three-field bridge. However, all three fields (ECM sensing, metabolic reprogramming, histone modification) are firmly within the life sciences umbrella. |
| Testability | 20% | 8 | Very testable: LC-MS metabolomics in nuclear fractions (standard in metabolomics labs), CUT&Tag, SB-204990/BPTES/dmαKG rescue. The orthogonal inhibitor dissection is elegant. Even if the rate-limiting hypothesis fails, the experiment is informative (Critic: "even if hypothesis fails, experiment is informative"). LC-MS nuclear fractionation is more specialized than standard cell biology but well-established. |
| Impact | 10% | 5 | If the rate-limiting model were true, it would explain why metabolic status affects mechanoepigenetic responses and open metabolic intervention strategies. But given the quantitative problem (cofactors in excess of Km), the main contribution is likely the measurement of nuclear metabolites under ECM stiffness — informative but not field-transforming. |
| Groundedness | 20% | 5 | All 6 cited papers are verified (Wellen 2009, Enzo 2015, Carey 2015, Agger 2007, Tahiliani 2009, Bertero 2016). However, the 3 parametric claims are the core novel claims (nuclear acetyl-CoA under stiffness, EP300 Km in vivo, rate-limiting status) — the grounded claims are established background, not the hypothesis's novel contribution. The Critic's quantitative attack (cofactors 5-100x above Km) undermines the central mechanistic claim. Score 5 to reflect that verified citations support background but the novel claim is quantitatively implausible. |
| **Composite** | | **5.8** | 0.20×5 + 0.20×6 + 0.10×5 + 0.20×8 + 0.10×5 + 0.20×5 = 1.0+1.2+0.5+1.6+0.5+1.0 |

---

## Final Ranking Table (All 8 Hypotheses)

| Rank | ID | Title (abbreviated) | N (20%) | MS (20%) | CD (10%) | T (20%) | I (10%) | G (20%) | Composite |
|------|----|--------------------|---------|----------|----------|---------|---------|---------|-----------|
| 1 | **C2-H6** | HDAC3 Eraser Depletion | 9 | 7 | 5 | 9 | 7 | 6 | **7.4** |
| 2 | **E1-H4** | TET2 DNA Methylation Memory | 7 | 8 | 5 | 9 | 7 | 6 | **7.2** |
| 3 | **E1-H3** | Sequential UTX Two-Phase Feedforward | 7 | 8 | 5 | 9 | 6 | 6 | **7.1** |
| 4 | C2-H2 | Three-Phase Cascade (EP300→UTX→TET2) | 7 | 7 | 5 | 8 | 7 | 5 | 6.6 |
| 5 | **C2-H7** | H3K9me3 Competence Windows | 7 | 6 | 6 | 8 | 6 | 5 | **6.4** |
| 6 | **E1-H5** | Dual YAP+MRTF CTCF Loops | 7 | 7 | 5 | 7 | 6 | 5 | **6.3** |
| 7 | C2-H3 | Differential YAP/MRTF Thresholds | 6 | 5 | 5 | 9 | 6 | 5 | 6.1 |
| 8 | C2-H1 | Metabolic Gatekeepers | 5 | 6 | 5 | 8 | 5 | 5 | 5.8 |

*N=Novelty, MS=Mechanistic Specificity, CD=Cross-field Distance, T=Testability, I=Impact, G=Groundedness*
*No cross-domain bonus applied (all hypotheses bridge adjacent biomedical sub-disciplines)*

---

## Diversity Check — Top 5

**Pre-adjustment top 5:** C2-H6 (7.4), E1-H4 (7.2), E1-H3 (7.1), C2-H2 (6.6), C2-H7 (6.4)

### Pairwise Similarity Assessment

| Pair | Same bridge? | Same subfields? | Same prediction type? | Verdict |
|------|-------------|----------------|----------------------|---------|
| C2-H6 vs E1-H4 | No (eraser vs memory) | Adjacent | No | **DIVERSE** |
| C2-H6 vs E1-H3 | No (eraser vs cascade) | Adjacent | No | **DIVERSE** |
| C2-H6 vs C2-H2 | No (eraser vs cascade) | Adjacent | No | **DIVERSE** |
| C2-H6 vs C2-H7 | No (eraser vs force-derepression) | Adjacent | No | **DIVERSE** |
| E1-H4 vs E1-H3 | Partial (both temporal cascade) | Same | Partially (both temporal) | **BORDERLINE — DIVERSE** |
| **E1-H4 vs C2-H2** | **YES — C2-H2 Phase 3 = E1-H4's entire central mechanism** | Same | Yes (Phase 3 overlap) | **CONVERGENT** |
| E1-H4 vs C2-H7 | No | Adjacent | No | DIVERSE |
| **E1-H3 vs C2-H2** | **YES — C2-H2 Phase 1→2 = E1-H3's entire central mechanism** | Same | Yes (Phase 1-2 overlap) | **CONVERGENT** |
| E1-H3 vs C2-H7 | No (enzymatic vs force-direct) | Adjacent | No | DIVERSE |
| C2-H2 vs C2-H7 | No | Adjacent | No | DIVERSE |

### Cluster Identification

**Cluster A — Temporal Enzymatic Cascade (ECM stiffness → sequential enzyme recruitment → H3K27ac dynamics):**
- E1-H3 (Phase 1→2: EP300→UTX feedforward, 7.1)
- E1-H4 (Phase 3: H3K27ac→TET2→DNA methylation memory, 7.2)
- C2-H2 (Phase 1→2→3: integrated cascade — directly extends both E1-H3 and E1-H4, 6.6)

C2-H2 is explicitly described as "extends E1-H3 and E1-H4" — it is a strict superset of the other two hypotheses' mechanisms. Including all three in the evolution selection would send three hypotheses to Quality Gate that test overlapping biology.

### Diversity Adjustment

**Rule triggered:** 3 of top 5 (E1-H3, E1-H4, C2-H2) share the same temporal cascade mechanism.

**Action:** C2-H2 is demoted. It is the most convergent member of the cluster (it directly integrates E1-H3+E1-H4 and adds only the strict feedforward dependency claim beyond the sum of its parents). Keeping E1-H3 and E1-H4 independently provides more experimental information per Quality Gate slot than keeping C2-H2, which requires validating both parents' mechanisms simultaneously.

**Rationale for keeping both E1-H3 and E1-H4:** Despite sharing the temporal cascade approach, they make genuinely different predictions in different timeframes (hours vs. days-weeks), use different molecular readouts (KDM6A CUT&RUN vs. 5hmC DIP-seq/RRBS), and test different biological phenomena (bivalent enhancer conversion vs. DNA methylation memory). They are borderline diverse.

**Promoted hypothesis:** E1-H5 (6.3) — CTCF-permitted dual program; genuinely distinct mechanism (3D chromatin architecture, HiChIP).

**Note:** C2-H3 (6.1) and C2-H1 (5.8) remain below the selection threshold.

---

## Elo Tournament Sanity Check (Top 6 Pre-Diversity)

**Participants:** C2-H6 (7.4), E1-H4 (7.2), E1-H3 (7.1), C2-H2 (6.6), C2-H7 (6.4), E1-H5 (6.3)

**Question for each pair:** "Which would a domain researcher want to test FIRST, and why?"

### 15 Pairwise Comparisons

1. **C2-H6 vs E1-H4** → **C2-H6 wins.** The eraser-depletion model is completely orthogonal to existing biology — a domain researcher would test the paradigm-challenging hypothesis first to see if the field's writer-activation focus needs to be broadened. E1-H4's TET2 memory handoff builds on well-understood mechanisms.

2. **C2-H6 vs E1-H3** → **C2-H6 wins.** C2-H6 tests a conceptually inverted mechanism with no analogues in the field; E1-H3 tests a temporal specification of a known cascade (EP300→UTX). The inverted model has higher expected information gain.

3. **C2-H6 vs C2-H2** → **C2-H6 wins.** C2-H6 introduces an entirely new mechanistic axis; C2-H2 integrates known cascade biology with an added strictness claim. Novel eraser model tested before more complex cascade.

4. **C2-H6 vs C2-H7** → **C2-H6 wins.** C2-H6 has higher groundedness (Fu 2024 direct evidence vs Sun 2020 cyclic/static ambiguity). C2-H7 has a fundamental unresolved methodological question (cyclic vs static force).

5. **C2-H6 vs E1-H5** → **C2-H6 wins.** C2-H6 is more mechanistically specific with higher novelty. E1-H5 requires expensive HiChIP; C2-H6 requires standard ChIP-seq + AAV rescue.

6. **E1-H4 vs E1-H3** → **E1-H4 wins (narrow).** TET2-based mechanical memory answers a more fundamental question (how does mechanical history persist beyond signal decay?) and introduces entirely new evidence classes (5hmC DIP-seq, RRBS). E1-H3's paralog disambiguation is important but more incremental.

7. **E1-H4 vs C2-H2** → **E1-H4 wins.** If the Phase 1-2 feedforward (E1-H3) and Phase 3 TET2 memory (E1-H4) are tested individually, C2-H2 adds minimal new information beyond their combination. Testing E1-H4 first provides cleaner interpretation of Phase 3 independently.

8. **E1-H4 vs C2-H7** → **E1-H4 wins.** E1-H4 has higher groundedness (TET2 biochemistry well-established) and no fundamental methodological ambiguity. C2-H7's cyclic/static force issue requires a preliminary validation study before the main hypothesis can be tested.

9. **E1-H4 vs E1-H5** → **E1-H4 wins.** E1-H4 is more mechanistically specific with cleaner experimental logic. E1-H5's HiChIP demand reduces accessibility.

10. **E1-H3 vs C2-H2** → **E1-H3 wins.** Testing the foundational Phase 1→Phase 2 feedforward (E1-H3) first provides the prerequisite data for C2-H2's three-phase model. If E1-H3 feedforward fails, C2-H2 collapses with it. More information-efficient to test E1-H3 first.

11. **E1-H3 vs C2-H7** → **E1-H3 wins.** E1-H3 has fewer unresolved preliminary questions (no cyclic/static ambiguity, established UTX-COMPASS machinery). C2-H7 requires first demonstrating that static ECM can replicate cyclic force effects.

12. **E1-H3 vs E1-H5** → **E1-H3 wins.** E1-H3 is more mechanistically specific, higher groundedness (6 vs 5), and more accessible experimentally (CUT&Tag vs HiChIP).

13. **C2-H2 vs C2-H7** → **C2-H2 wins.** Three-phase cascade provides richer biological insight with lower methodological risk. C2-H7's fundamental cyclic/static question must be addressed before the main hypothesis is testable.

14. **C2-H2 vs E1-H5** → **C2-H2 wins.** C2-H2 makes more falsifiable mechanistic predictions with standard methods; E1-H5's HiChIP requires more infrastructure and produces a characterization study rather than a mechanistic test.

15. **C2-H7 vs E1-H5** → **C2-H7 wins (narrow).** C2-H7's force-to-heterochromatin mechanism is more conceptually novel and addresses a genuine mechanistic gap (force-direct vs signaling-relay). E1-H5's empirical survey framing is lower-risk but less exciting.

### Win Tally

| Hypothesis | Wins | Win Rate | Elo Rank |
|------------|------|----------|----------|
| C2-H6 | 5/5 | 100% | #1 |
| E1-H4 | 4/5 | 80% | #2 |
| E1-H3 | 3/5 | 60% | #3 |
| C2-H2 | 2/5 | 40% | #4 |
| C2-H7 | 1/5 | 20% | #5 |
| E1-H5 | 0/5 | 0% | #6 |

### Elo vs. Linear Comparison

**Verdict: Elo CONFIRMS linear ranking.** Perfect agreement on all 6 positions:
- Linear: C2-H6 > E1-H4 > E1-H3 > C2-H2 > C2-H7 > E1-H5
- Elo: C2-H6 > E1-H4 > E1-H3 > C2-H2 > C2-H7 > E1-H5

The linear composite and pairwise tournament are fully consistent. The pairwise comparison captures an implicit dimension the 6-dimension average also captures: **experimental independence and information gain**. C2-H6's complete orthogonality to existing models (1.0 Elo win rate, 7.4 composite) reflects that both the dimensions AND the pairwise judgment agree that an inverted paradigm test is more valuable than cascade elaboration.

The only implicit factor the Elo surface more clearly: **methodological accessibility.** E1-H5 (0.0 win rate, 6.3 composite) is penalized by both metrics partly because HiChIP requires specialized infrastructure. The pairwise preference for "test FIRST" down-weights technically demanding experiments in a way the 6-dimension average partially captures through Testability (7) but not fully.

---

## Evolution Selection (Post-Diversity Check)

**Top 5 for Quality Gate:**

| Selection Rank | ID | Composite | Mechanism | Selection Rationale |
|---|---|---|---|---|
| 1 | **C2-H6** | 7.4 | Eraser depletion (HDAC3-NCoR) | Highest composite; genuinely orthogonal mechanism; best experimental design; paradigm-challenging |
| 2 | **E1-H4** | 7.2 | TET2-DNA methylation memory | Second highest; new evidence class (5hmC/RRBS); answers fundamental memory question |
| 3 | **E1-H3** | 7.1 | Sequential UTX feedforward | Third highest; distinct from E1-H4 (different timescale and prediction); paralog disambiguation |
| 4 | **C2-H7** | 6.4 | Force-direct H3K9me3 derepression | Distinct mechanism (force-physical vs signaling-relay); only non-signaling hypothesis; cross-field distance bonus |
| 5 | **E1-H5** | 6.3 | CTCF dual-program 3D loops | Promoted after C2-H2 demotion; distinct 3D architecture mechanism; dual-program design novel |

**Demoted (diversity adjustment):**
- C2-H2 (6.6): Directly extends E1-H3+E1-H4; adds strict feedforward claim but is redundant when both parents advance. Recommended for Cycle 3 if feedforward hypothesis remains untested.

**Eliminated (below threshold):**
- C2-H3 (6.1): High testability but MRTF threshold claim entirely parametric; lowest mechanistic specificity (5). Salvageable as supporting experiment within C2-H6 or C2-H7.
- C2-H1 (5.8): Quantitatively implausible rate-limiting claim (cofactors 5-100x above enzyme Km); lowest composite.
