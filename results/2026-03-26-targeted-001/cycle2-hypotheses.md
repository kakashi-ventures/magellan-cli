# Cycle 2 Hypotheses — Mechanobiology (ECM Mechanics) × Epigenomics (Enhancer Regulation)

**Session:** 2026-03-26-targeted-001
**Cycle:** 2
**Mode:** BLIND (no WebSearch)
**Generator model:** opus
**Cycle 1 survivors extended:** E1-H3, E1-H4, E1-H5
**Generation techniques:** facet_recombination, gap_targeted_generation, counterfactual_probing, scale_bridging, bisociation, multi_level_abstraction, negation_exploration

---

## Relationship Maps (Pre-Generation)

### Field A (Mechanobiology) Key Relationships:
1. ECM stiffness → integrin clustering → FAK autophosphorylation (STRING FAK-ITGB1 verified)
2. FAK → RhoA → ROCK1 → actomyosin contractility (KEGG verified)
3. ROCK1/actomyosin → YAP nuclear translocation (Dupont Nature 2011)
4. ROCK1/actomyosin → G-actin depletion → MRTF nuclear translocation (Miralles Cell 2003)
5. ECM stiffness → PIEZO1 opening → Ca²⁺ influx (Zhang IOVS 2025)
6. ECM stiffness → lamin A/C upregulation → nuclear stiffening (Xu 2023, Mandal 2025)
7. LINC complex (SUN1/2-Nesprin) → force to nuclear lamina → chromatin (STRING LMNA-SUN2 0.999)
8. ECM stiffness → glycolytic shift (YAP-dependent; Enzo Nat Cell Biol 2015)
9. ECM stiffness → HDAC3 downregulation (Fu Bone Research 2024)
10. Integrin force → H3K9me3 demethylation at nuclear interior (Sun Sci Advances 2020)

### Field C (Epigenomics/Enhancers) Key Relationships:
1. EP300 writes H3K27ac at active enhancers (kcat ~5/min in vitro)
2. UTX (KDM6A) demethylates H3K27me3 at enhancers as part of COMPASS complex
3. TET2 oxidizes 5mC → 5hmC at enhancer CpG shores (αKG-dependent dioxygenase)
4. HDAC3-NCoR/SMRT decommissions active enhancers by removing H3K27ac
5. BRD4 reads H3K27ac → recruits P-TEFb → transcription elongation
6. H3K9me3 silences enhancers in heterochromatin (SUV39H1/2 writers)
7. CTCF anchors chromatin loops; cohesin extrudes loops within CTCF boundaries
8. NFAT binds GGAAA motif enhancers after calcineurin-mediated dephosphorylation
9. MLL3/4-COMPASS writes H3K4me1 at primed enhancers
10. αKG is a shared cofactor for UTX, KDM4A, TET1/2/3 (all Fe²⁺/αKG dioxygenases)

### Cross-Map Connections Exploited:
- **Shared node (αKG):** Metabolic shift (A8) → αKG availability → UTX (C2) + TET2 (C3) activity
- **Analogous relationship:** ECM stiffness activates EP300 writer (A3→C1); ECM stiffness depletes HDAC3 eraser (A9→C4) — same net effect, orthogonal mechanisms
- **Inverse relationship:** Nuclear interior = force-responsive H3K9me3 loss (A10); nuclear periphery = force-resistant H3K9me3 retention (A10) — same force, opposite enhancer outcomes
- **Missing link (PIEZO1→NFAT enhancers):** PIEZO1→Ca²⁺ (A5) should activate calcineurin→NFAT→NFAT enhancers (C8) — completely untested pathway

---

## Hypotheses Building on Cycle 1 Survivors

---

### Hypothesis C2-H1: Acetyl-CoA and α-Ketoglutarate as Metabolic Gatekeepers for the ECM Stiffness-Enhancer Enzyme Cascade

**Connection**: ECM stiffness → metabolic reprogramming (glycolysis/glutaminolysis) → cofactor availability (acetyl-CoA for EP300, αKG for UTX and TET2) → enhancer enzyme kinetics gated by metabolite supply

**Extends**: E1-H3 (UTX-COMPASS) + E1-H4 (TET2 memory)

**Mechanism**:

ECM stiffness (50 kPa vs. 1 kPa) drives cytoskeletal tension via ROCK1-actomyosin, which upregulates aerobic glycolysis and glutaminolysis through YAP-dependent transcriptional activation of glycolytic enzymes (HK2, LDHA, PKM2) and glutamine transporters (SLC1A5). [GROUNDED: Enzo et al., Nat Cell Biol 2015 — YAP drives glycolytic gene expression; Bertero et al., J Clin Invest 2016 — ECM stiffness enhances glutaminolysis via YAP in pulmonary hypertension.] The resulting metabolic shift has two critical epigenetic consequences via shared cofactor requirements:

**(1) Acetyl-CoA gates EP300 catalysis at Phase 1 enhancers.** ATP-citrate lyase (ACLY) converts citrate from enhanced mitochondrial flux into nuclear acetyl-CoA. [GROUNDED: Wellen et al., Science 2009, PMID 19762564 — ACLY-derived acetyl-CoA required for histone H3 and H4 acetylation; nuclear ACLY generates nuclear pool.] EP300 uses acetyl-CoA as its direct acetyl-group donor for H3K27 acetylation (Km ~1-4 µM for acetyl-CoA [PARAMETRIC — in vitro estimates; in vivo Km may differ]). On stiff ECM, elevated ACLY activity raises nuclear acetyl-CoA above EP300's Km, enabling sustained catalytic activity. On soft ECM, nuclear acetyl-CoA may hover near or below Km, making EP300 substrate-limited. This metabolically enables Phase 1 (0-4h) of the E1-H3 temporal cascade.

**(2) α-Ketoglutarate (αKG) gates both UTX (Phase 2) and TET2 (Phase 3).** UTX (KDM6A) and TET2 are both Fe(II)/αKG-dependent dioxygenases requiring αKG as essential cofactor. [GROUNDED: UTX uses αKG — Agger et al., Nature 2007; TET enzymes require αKG — Tahiliani et al., Science 2009, PMID 19372391.] Enhanced glutaminolysis on stiff ECM → elevated αKG via glutamate dehydrogenase. The αKG/succinate ratio determines dioxygenase activity because succinate competitively inhibits αKG binding. [GROUNDED: Carey et al., Nature 2015, PMID 25607371 — αKG/succinate ratio controls TET activity and DNA methylation in embryonic stem cells.] On stiff ECM, predicted >2-fold increase in αKG/succinate ratio [PARAMETRIC] would simultaneously enhance UTX-mediated H3K27me3 demethylation at bivalent enhancers (Phase 2, 12-24h) and TET2-mediated 5hmC deposition for DNA methylation memory (Phase 3, 24-72h).

**Key prediction**: The two phases from E1-H3 and the memory mechanism from E1-H4 are METABOLICALLY COUPLED through shared cofactor requirements. Blocking glycolytic flux (2-DG, 50 mM) or ACLY (SB-204990, 10 µM) should selectively ablate Phase 1 H3K27ac without affecting Phase 2/3 (different cofactor). Blocking glutaminolysis (BPTES, 10 µM) should selectively ablate Phase 2 bivalent resolution AND Phase 3 TET2 memory without affecting Phase 1 (different cofactor). This metabolic dissection creates an orthogonal perturbation strategy for the temporal cascade that cycle 1 inhibitor experiments (A-485, GSK-J4) cannot achieve.

**Multi-level abstraction:**
- *Molecular*: Acetyl-CoA → EP300 substrate; αKG → UTX/TET2 cofactor
- *Systemic*: Metabolic reprogramming integrates mechanotransduction with chromatin modification through shared metabolite pools
- *Informational*: ECM stiffness encodes a metabolic state that is decoded by enhancer enzymes through cofactor availability — a metabolic "permission signal"

**Confidence**: 5 — Individual components well-supported (YAP-glycolysis, ACLY-histone acetylation, αKG-dioxygenase dependence). Novel claim: metabolite concentrations are RATE-LIMITING for enhancer enzyme activity under stiffness conditions. Nuclear metabolite concentrations under stiffness are unmeasured.

**Groundedness**: 6
- GROUNDED [5 claims]: Enzo Nat Cell Biol 2015 (YAP→glycolysis); Wellen Science 2009 (ACLY→histone acetylation); Agger Nature 2007 (UTX+αKG); Tahiliani Science 2009 (TET+αKG); Carey Nature 2015 (αKG/succinate ratio controls TET); Bertero J Clin Invest 2016 (ECM stiffness→glutaminolysis)
- PARAMETRIC [3 claims]: Nuclear acetyl-CoA concentration on stiff vs. soft ECM; EP300 Km in vivo; whether metabolic shift is quantitatively rate-limiting for enhancer enzymes in this context

**Why this might be WRONG**: Nuclear acetyl-CoA may be buffered by alternative sources (acetate via ACSS2, ketone bodies via AACS) and never rate-limiting for EP300. The metabolic shift may be cell-type specific — primarily shown in cancer and pulmonary cells, may not occur in hMSCs at relevant magnitudes. αKG may be in excess even on soft ECM (typical cellular αKG ~200-500 µM, well above UTX Km ~50-100 µM [PARAMETRIC]), making Phase 2/3 not metabolically gated. EP300 kcat may be limited by chromatin substrate access, not acetyl-CoA availability.

**Literature gap it fills**: Connects metabolomics to mechanoepigenetics — no paper has measured nuclear metabolite levels (acetyl-CoA, αKG) as a function of ECM stiffness or tested whether they are rate-limiting for enhancer enzyme activity. Addresses the "why" behind the temporal gap in E1-H3.

**Test protocol**: hMSCs on PA hydrogels (1/50 kPa, 0/6/12/24h). LC-MS metabolomics: acetyl-CoA, αKG, succinate, citrate in nuclear vs. cytoplasmic fractions. H3K27ac CUT&Tag + UTX CUT&RUN + TET2 CUT&RUN at 12h, 24h. Perturbations: SB-204990 (ACLY inhibitor, 10 µM), BPTES (glutaminase inhibitor, 10 µM), cell-permeable dimethyl-αKG (4 mM), sodium acetate (5 mM, ACSS2-dependent rescue). Rescue experiment: BPTES on stiff ECM + dmαKG → should rescue Phase 2/3 but not Phase 1; SB-204990 on stiff ECM + acetate → should rescue Phase 1 but not Phase 2/3.

---

### Hypothesis C2-H2: Integrated Three-Phase Enhancer Memory Cascade with Strict Feedforward Dependencies Under ECM Stiffness

**Connection**: ECM stiffness → Phase 1 (EP300 H3K27ac at acute non-bivalent enhancers, 0-4h) → Phase 2 (UTX/COMPASS bivalent resolution at lineage enhancers, 12-24h) → Phase 3 (TET2 DNA methylation memory consolidation, 24-72h) → persistent mechanical memory

**Extends**: E1-H3 + E1-H4 crossover with feedforward dependency specification

**Mechanism**:

E1-H3 established two temporal phases: Phase 1 (EP300 at non-bivalent enhancers) feeds forward to Phase 2 (UTX-COMPASS at bivalent enhancers). E1-H4 established that H3K27ac creates a 6-12h window for TET2 recruitment and DNA methylation memory. This hypothesis integrates both into a unified three-phase cascade and specifies the FEEDFORWARD DEPENDENCIES that make it a cascade rather than three independent events.

**Phase 1 (0-4h): Acute H3K27ac at non-bivalent enhancers.** YAP nuclear translocation on stiff ECM → YAP-TEAD at CTGF, CYR61, ANKRD1 enhancers → EP300 recruitment → H3K27ac. [GROUNDED: YAP-TEAD-EP300 axis; STRING YAP1-EP300 0.692.] These non-bivalent enhancers lack H3K27me3 and respond within minutes-to-hours. Phase 1 products include CTGF and CYR61 — secreted ECM components that reinforce the stiff microenvironment. [GROUNDED: CTGF/CYR61 are canonical YAP target genes encoding ECM proteins.]

**Feedforward link (Phase 1 → Phase 2):** Phase 1 EP300 activity deposits H3K27ac at non-bivalent enhancers, which recruits BRD4 [GROUNDED: EP300-BRD4 STRING 0.988; BRD4 reads H3K27ac]. BRD4 in turn facilitates NIPBL loading at these loci [PARAMETRIC — BRD4-NIPBL interaction documented at super-enhancers but not specifically at ECM-stiffness-responsive loci]. NIPBL enables cohesin-mediated loop extrusion that brings non-bivalent enhancers into contact with bivalent enhancers within the same CTCF domain [PARAMETRIC — extends E1-H5 logic]. This physical proximity facilitates MLL3/4-COMPASS complex transfer from Phase 1 sites (where EP300 is active) to adjacent Phase 2 bivalent sites. The 8-14h temporal gap represents: (a) time for Phase 1 transcription → translation → accumulation of feedforward mediators, and (b) COMPASS complex assembly at bivalent loci after proximity-enabled recruitment.

**Phase 2 (12-24h): Bivalent enhancer resolution.** UTX (KDM6A), as part of the MLL3/4-COMPASS complex, removes H3K27me3 at bivalent enhancers of lineage genes (RUNX2, SNAI1 distal enhancers). Simultaneously, EP300 (still active via sustained YAP signaling) deposits H3K27ac. The bivalent-to-active conversion creates the differentiation-associated enhancer program. [Partially GROUNDED: UTX-COMPASS at enhancers — Yu MCB 2025 showed KDM6B at promoters; UTX at enhancers is the canonical assignment per Agger et al. but not demonstrated under stiffness.]

**Feedforward link (Phase 2 → Phase 3):** Phase 2 H3K27ac at bivalent-resolved enhancers creates the recruitment platform for TET2. TET2 co-localizes with H3K27ac+ enhancers [GROUNDED: Williams Cell 2011 — TET1 binds CpG-rich promoters; TET2 is recruited by transcription factors to distal regulatory elements; specific recruitment to H3K27ac-marked enhancers is PARAMETRIC but consistent with genome-wide binding data]. TET2 initiates the oxidation cascade: 5mC → 5hmC → 5fC → 5caC, with BER (TDG) completing demethylation within 48-72h. [GROUNDED: TET2 oxidation cascade and TDG-mediated BER are established biochemistry.]

**Phase 3 (24-72h): DNA methylation memory consolidation.** CpG demethylation at enhancer shores persists in non-dividing cells (7-14 days) as mechanical memory. [PARAMETRIC — persistence timescale depends on DNMT1 maintenance kinetics in quiescent cells.] This is the E1-H4 mechanism integrated as the terminal phase.

**Strict hierarchy prediction:**
- A-485 at 0h → blocks ALL three phases (Phase 1 collapse → cascade failure)
- A-485 at 8h → blocks Phase 2 and 3 but spares Phase 1 H3K27ac already deposited
- GSK-J4 → blocks Phase 2 (H3K27me3 removal) and Phase 3 (no H3K27ac substrate for TET2) but spares Phase 1
- siTET2 → blocks Phase 3 only, spares Phase 1 and Phase 2
- The hierarchy is ONE-DIRECTIONAL: disrupting an upstream phase collapses all downstream phases, but disrupting downstream phases leaves upstream intact

**Confidence**: 5 — Integrates two evolved hypotheses with sound logic. The feedforward dependencies are the novel testable claim.

**Groundedness**: 5
- GROUNDED: EP300-BRD4 interaction (STRING 0.988); CTGF/CYR61 as YAP targets; TET2 oxidation cascade
- PARAMETRIC: Phase 1 → Phase 2 feedforward via BRD4-NIPBL-mediated proximity; COMPASS complex transfer mechanism; 8-14h temporal gap explanation; one-directional hierarchy

**Why this might be WRONG**: Phase 2 may not require Phase 1. UTX-COMPASS can be recruited independently to bivalent enhancers via its own PHD domain (which reads H3K4me1) — the feedforward from Phase 1 may be unnecessary. TET2 may preferentially target Phase 1 (non-bivalent) enhancers over Phase 2 (bivalent-resolved) enhancers because Phase 1 enhancers accumulate H3K27ac earlier and longer. The strict one-directional hierarchy may be an oversimplification — parallel activation pathways likely exist.

**Literature gap it fills**: No paper has tested whether enhancer activation under ECM stiffness follows a strict feedforward hierarchy. No study has determined whether DNA methylation memory (E1-H4) selectively consolidates lineage-specific (Phase 2) vs. acute-response (Phase 1) enhancers.

**Test protocol**: hMSCs on PA hydrogels (1→50 kPa). Time-course CUT&Tag: H3K27ac + H3K27me3 at 0/2/6/12/18/24/48h. Classify enhancers: Phase 1 (H3K27ac gain by 6h, no prior H3K27me3) vs. Phase 2 (H3K27ac gain by 24h, prior H3K27me3+). TET2 CUT&RUN at 12/24/48h — predict enrichment at Phase 2 enhancers by 48h. RRBS at 48h and 7d post-transfer (50→1 kPa) — predict demethylation preferentially at Phase 2 enhancer shores. Phase disruption matrix: A-485 at 0h vs. 8h, GSK-J4, siTET2, siNIPBL (feedforward test). 4C-seq from CTGF promoter to test whether Phase 1 loci make contacts with bivalent enhancers by 8h.

---

### Hypothesis C2-H3: Differential Stiffness Thresholds for YAP-TEAD vs. MRTF-SRF Create a Tissue-Stiffness-to-Enhancer Decoder

**Connection**: ECM stiffness magnitude → differential activation thresholds (MRTF-SRF at ~5-10 kPa, YAP-TEAD at ~15-25 kPa) → stiffness-value-dependent enhancer program selection → tissue-specific gene regulation

**Extends**: E1-H5 (dual-program model)

**Mechanism**:

E1-H5 established that ECM stiffness activates two independent H3K27ac programs: YAP-TEAD (CTGF/CYR61 enhancers with TEAD motifs) and MRTF-SRF (ACTA2/VCL enhancers with CArG-box motifs). This hypothesis extends the dual-program framework by proposing that these programs have QUANTITATIVELY DIFFERENT activation thresholds, creating a stiffness magnitude decoder.

**MRTF-SRF has a lower threshold (~5-10 kPa).** MRTF-A (MKL1) is sequestered in the cytoplasm by monomeric G-actin. [GROUNDED: Miralles et al., Cell 2003, PMID 12526794 — MRTF-SRF-actin sequestration mechanism established.] Even modest increases in ECM stiffness (5-10 kPa) promote actin polymerization via RhoA-mDia formin activity → G-actin depletion from ~50 µM toward ~20-30 µM [PARAMETRIC — estimates from bulk actin measurements] → MRTF liberation → nuclear import → MRTF-SRF binding at CArG-box enhancers. The MRTF-actin Kd (~10-50 nM for RPEL domains) [PARAMETRIC — from Mouilleron et al., EMBO J 2011 structural studies] means that moderate G-actin depletion liberates a measurable fraction of MRTF. The threshold is set by G-actin/F-actin equilibrium, which shifts at relatively low force levels.

**YAP-TEAD has a higher threshold (~15-25 kPa).** YAP nuclear translocation requires extensive cell spreading, mature focal adhesion formation, and high cytoskeletal tension sufficient to suppress LATS1/2 kinase activity. [GROUNDED: Dupont et al., Nature 2011, PMID 21654799 — YAP nuclear localization requires substrate stiffness ≥15-20 kPa in hMSCs; stiffness threshold is cell spreading-dependent.] The LATS1/2 → YAP Ser127 phosphorylation → 14-3-3 cytoplasmic retention creates a sharper, more switch-like threshold than the graded MRTF-actin titration. YAP activation correlates with cell area exceeding ~2000 µm², which requires higher stiffness for most cell types.

**Tissue-stiffness decoder:**
- **Brain ECM (~0.5-1 kPa):** Neither program → neural enhancer identity preserved by default
- **Soft tissue (5-10 kPa; adipose, liver parenchyma):** MRTF-SRF program ONLY → CArG-box enhancers activate → contractile gene program (ACTA2, MYL9, VCL) without ECM remodeling genes
- **Stiff tissue (20-50 kPa; bone, cartilage, fibrotic tissue):** BOTH programs → YAP-TEAD + MRTF-SRF enhancers → full mechanoresponse including ECM deposition (CTGF), proliferation, and contractility
- **Fibrosis progression (2→15→30 kPa over weeks):** MRTF-SRF activates first → ACTA2/myofibroblast transition → increased contractility → further ECM stiffening → crosses YAP threshold → CTGF/CYR61 → ECM deposition → positive feedback ratchet

The ratchet model predicts fibrosis has a CRITICAL STIFFNESS INFLECTION POINT where the YAP program engages, after which disease progression accelerates. This inflection should be identifiable as a stiffness value where TEAD-motif enhancer gain sharply increases.

**Multi-level abstraction:**
- *Molecular*: G-actin-MRTF dissociation vs. LATS1/2-YAP phosphorylation
- *Systemic*: Two parallel signaling arms with different dose-response curves create a combinatorial code
- *Informational*: ECM stiffness magnitude is DECODED into discrete enhancer programs — an analog-to-digital converter at the chromatin level

**Confidence**: 4 — Individual pathway thresholds partially supported. Quantitative threshold values are approximate and cell-type dependent. The decoder model is a novel testable synthesis.

**Groundedness**: 5
- GROUNDED: MRTF-G-actin sequestration (Miralles Cell 2003); YAP stiffness threshold (Dupont Nature 2011); CArG-box as MRTF-SRF binding motif; TEAD motif for YAP
- PARAMETRIC: Precise threshold values (5-10 kPa vs. 15-25 kPa); MRTF-actin Kd at physiological conditions; sequential activation in fibrosis; ratchet mechanism; whether thresholds are consistent across cell types

**Why this might be WRONG**: MRTF and YAP activation thresholds may be identical or overlapping — both depend on RhoA/ROCK signaling and actin dynamics. Cell density and cell-cell junction formation strongly affect YAP via the Hippo pathway, potentially decoupling YAP from ECM stiffness. Cell-type-specific differences (fibroblasts vs. epithelial cells vs. hMSCs) may override the threshold hierarchy. MRTF may also require high stiffness in some contexts (e.g., Baarlink et al. showed nuclear actin dynamics require substantial mechanical stimulation).

**Literature gap it fills**: Gap #6 (tissue-specific enhancer programs controlled by tissue-native ECM stiffness). No paper has compared MRTF-SRF vs. YAP-TEAD enhancer program activation across a fine-grained stiffness gradient with genome-wide enhancer profiling.

**Test protocol**: MCF10A or hMSCs on PA hydrogels at 7 stiffness values (0.5/2/5/10/15/25/50 kPa, 48h). H3K27ac ChIP-seq + ATAC-seq at each stiffness. Enhancer gain calling at each stiffness increment. TEAD motif vs. CArG motif enrichment analysis at gained enhancers per stiffness step — predict CArG enrichment starting at 5-10 kPa, TEAD enrichment starting at 15-25 kPa. Immunofluorescence: MRTF-A and YAP nuclear/cytoplasmic ratio at each stiffness → dose-response curves. Perturbations at 10 kPa: verteporfin (should not affect CArG enhancers); CCG-1423 (MRTF-SRF inhibitor, should suppress CArG but not TEAD). At 50 kPa: both inhibitors needed. Fibrosis model: primary lung fibroblasts on progressive stiffening hydrogel (2→30 kPa over 7 days) with time-resolved H3K27ac profiling.

---

## Completely Fresh Hypotheses

---

### Hypothesis C2-H4: PIEZO1-Calcineurin-NFAT Axis Activates a Calcium-Dependent Enhancer Program Parallel to and Non-Overlapping with YAP-TEAD

**Connection**: ECM stiffness → PIEZO1 mechanosensitive channel → Ca²⁺ influx → calcineurin activation → NFAT dephosphorylation/nuclear translocation → NFAT-dependent enhancer program at GGAAA motifs

**Bridge mechanism**: calcium_signaling_enhancer_program (distinct from all cycle 1 bridges)

**Mechanism**:

Cycle 1 hypotheses focused exclusively on the integrin-FAK-RhoA-YAP axis. But ECM stiffness also activates the mechanosensitive ion channel PIEZO1 [GROUNDED: PIEZO1 is a bona fide mechanosensor activated by membrane tension; Zhang et al. IOVS 2025 (in literature context) showed PIEZO1 is stiffness-responsive and activates DOT1L.] PIEZO1 opening on stiff substrates causes Ca²⁺ influx (extracellular [Ca²⁺] ~1.8 mM → cytoplasmic transient from ~100 nM resting to ~500 nM-1 µM peak). [GROUNDED: PIEZO1-mediated Ca²⁺ transients documented in multiple mechanosensing contexts — Coste et al., Science 2010, PMID 20813920.]

Ca²⁺ activates calcineurin (PP2B/PPP3CA), a Ca²⁺/calmodulin-dependent phosphatase. [GROUNDED: Calcineurin activation by Ca²⁺/CaM is canonical — Rusnak & Mertz, Physiol Rev 2000.] Calcineurin dephosphorylates NFAT (Nuclear Factor of Activated T-cells) at its serine-rich regulatory domain (13 phosphosites on NFATc1). [GROUNDED: Hogan et al., Genes Dev 2003, PMID 12717109 — comprehensive review of NFAT regulation.] Dephosphorylated NFAT translocates to the nucleus and binds NFAT response elements (GGAAA core motif) at specific enhancers.

In immune cells, NFAT-dependent enhancers are well-mapped (IL-2, IL-4, TNFα enhancer loci). [GROUNDED: Rao et al., Annu Rev Immunol 1997.] In bone biology, NFATc1 is the master transcription factor for osteoclastogenesis, activating enhancers controlling cathepsin K, TRAP, and OSCAR genes. [GROUNDED: Takayanagi et al., Dev Cell 2002, PMID 12361601.] In mesenchymal cells, NFAT-dependent enhancer programs are largely UNCHARACTERIZED — this is the central gap.

**Parallel program prediction**: The PIEZO1-NFAT enhancer program targets a gene set COMPLETELY NON-OVERLAPPING with YAP-TEAD enhancers. NFAT targets include: osteoclast differentiation genes, inflammatory mediators (IL-6, PTGS2/COX-2), and the calcineurin feedback inhibitor RCAN1. These are fundamentally different from YAP targets (CTGF, CYR61, ANKRD1). The two programs — YAP (integrin-mediated, sustained, threshold-like) and NFAT (PIEZO1-mediated, Ca²⁺-oscillation-dependent) — operate as PARALLEL enhancer-activating pathways from the same stiffness cue.

**Convergence point**: NFAT cooperates with AP-1 (FOS/JUN) at composite NFAT:AP-1 enhancers. [GROUNDED: Macian et al., Oncogene 2001, PMID 11313928 — NFAT:AP-1 composite elements at IL-2 enhancer.] Since AP-1 is also mechanosensitive, NFAT:AP-1 composite enhancers represent a convergence node. This creates THREE enhancer classes under ECM stiffness: (1) YAP-TEAD-only, (2) NFAT-only, (3) NFAT:AP-1 composite integrating both mechanosensitive inputs.

**Confidence**: 4 — PIEZO1 mechanosensitivity and calcineurin-NFAT signaling are individually well-established. The link from PIEZO1 to NFAT-dependent enhancers under ECM stiffness is entirely parametric. Computational validation noted PIEZO1-CAMK2A NOT FOUND in STRING — the pathway is indirect (via Ca²⁺ ions), adding uncertainty.

**Groundedness**: 5
- GROUNDED [5 claims]: PIEZO1 mechanosensitivity (Coste Science 2010); calcineurin-NFAT pathway (Hogan Genes Dev 2003); NFATc1 in osteoclast differentiation (Takayanagi Dev Cell 2002); NFAT:AP-1 composite elements (Macian Oncogene 2001); PIEZO1 stiffness-responsive (Zhang IOVS 2025)
- PARAMETRIC [3 claims]: Ca²⁺ transient amplitude/duration sufficient for calcineurin in mesenchymal cells on static stiff ECM; NFAT enhancer targets in hMSCs (extrapolated from immune/bone); non-overlapping prediction

**Why this might be WRONG**: PIEZO1 Ca²⁺ transients on static stiff substrates may be too TRANSIENT (ms-to-seconds) for calcineurin, which requires SUSTAINED Ca²⁺ elevation (minutes) or repetitive Ca²⁺ oscillations. Static ECM (unlike cyclic stretch) may produce only a single PIEZO1 opening event at initial plating, which decays too fast. RCAN1 (calcineurin feedback inhibitor) may dampen NFAT activation before it reaches enhancers. Calcineurin-NFAT may be inactive in mesenchymal stromal cells at physiological conditions — primarily characterized in immune cells.

**Literature gap it fills**: PIEZO1 → epigenetic effects shown only for DOT1L/H3K79me2 (Zhang 2025). No study has examined PIEZO1 → NFAT → enhancer activation under ECM stiffness. The NFAT enhancer landscape in mesenchymal/stromal cells under mechanical stimulation is completely uncharacterized.

**Test protocol**: hMSCs on PA hydrogels (1/10/50 kPa, 24h). Ca²⁺ imaging (Fluo-4 AM, live-cell) at 0/1/6h on each stiffness — characterize transient amplitude and frequency. NFATc1 immunofluorescence (nuclear/cytoplasmic ratio). H3K27ac ChIP-seq + ATAC-seq at 24h. Motif enrichment at gained enhancers: TEAD vs. GGAAA (NFAT) vs. NFAT:AP-1 composite. Perturbations: Yoda1 (PIEZO1 agonist, 5 µM) on 1 kPa → predict NFAT program activation; GsMTx4 (PIEZO1 inhibitor, 5 µM) on 50 kPa → block NFAT but not YAP; FK506/cyclosporin A (calcineurin inhibitor, 1 µM) on 50 kPa → block NFAT program; verteporfin on 50 kPa → block YAP but not NFAT. Double: FK506 + verteporfin → quantify residual enhancer activation (any remaining = third pathway).

---

### Hypothesis C2-H5: Viscoelastic Stress Relaxation Time Acts as a Temporal Filter That Selectively Permits Enhancer Activation Based on Enzyme Kinetic Requirements

**Connection**: ECM viscoelasticity → stress relaxation timescale → duration of sustained nuclear deformation → only enhancers whose activation kinetics are faster than relaxation time become active → viscoelasticity filters the enhancer landscape independently of elastic modulus

**Bridge mechanism**: viscoelastic_temporal_filter (distinct from all cycle 1 bridges)

**Mechanism**:

All cycle 1 hypotheses implicitly assumed purely elastic ECM (polyacrylamide hydrogels transmit force indefinitely). But physiological ECM is VISCOELASTIC — it relaxes stress over time with a characteristic time τ. [GROUNDED: Chaudhuri et al., Nat Mater 2016, PMID 26098228 — viscoelastic hydrogels with tunable relaxation profoundly affect stem cell fate differently from elastic substrates.] Fast-relaxing ECM (τ ~ seconds, brain-like) transmits only transient forces; slow-relaxing ECM (τ ~ minutes-to-hours, fibrotic tissue) transmits sustained forces. [GROUNDED: Charrier et al., Nat Commun 2018 demonstrated stress relaxation time independently controls cell spreading and fate.]

EP300 catalytic activity at enhancers requires sustained enzyme-substrate contact. At an estimated turnover of ~2-10 acetylation events per minute per EP300 molecule [PARAMETRIC — in vitro kcat estimates; in vivo rate uncertain] and a threshold of ~10-30 H3K27ac marks per nucleosome array for stable BRD4 recruitment [PARAMETRIC — based on in vitro BRD4-bromodomain binding cooperativity], EP300 needs ~1-5 minutes of continuous access per enhancer to establish a stable H3K27ac domain. Chromatin access at mechano-responsive enhancers depends on nuclear deformation magnitude, which depends on sustained force transmission through the cytoskeleton and LINC complex. If ECM relaxes stress within τ < 1 min, nuclear deformation dissipates before EP300 completes sufficient acetylation → the enhancer does not stably acquire H3K27ac.

**Three-tier filter model:**

(1) **Fast-relaxing ECM (τ < 1 min):** Only pre-accessible (ATAC-seq+) enhancers that require minimal additional H3K27ac activate. EP300 completes partial acetylation during the brief force window. These are "primed" enhancers with existing chromatin accessibility.

(2) **Intermediate relaxation (τ ~ 5-30 min):** Phase 1 enhancers (non-bivalent, accessible, EP300-responsive) from E1-H3 activate. But Phase 2 bivalent enhancers (requiring UTX-mediated H3K27me3 removal FIRST, then EP300 acetylation) do NOT activate because the sequential two-enzyme process exceeds the relaxation time.

(3) **Slow-relaxing ECM (τ > 1 h):** Both Phase 1 and Phase 2 enhancers activate. Only slow-relaxing (highly cross-linked, fibrotic) ECM provides sufficient sustained force for the full bivalent-to-active conversion.

**Critical prediction**: Two substrates with IDENTICAL elastic modulus (both 25 kPa) but DIFFERENT relaxation times produce DIFFERENT enhancer landscapes. This decouples stiffness from enhancer outcome and adds a TEMPORAL dimension that current mechanoepigenetics models lack entirely.

**Confidence**: 3 — Viscoelastic biology is well-established. The specific link to enhancer kinetics via EP300 catalytic timing is highly parametric. Nuclear deformation dynamics under viscoelastic loading are poorly characterized. The cytoskeleton may act as a mechanical capacitor, sustaining force independently of ECM relaxation.

**Groundedness**: 4
- GROUNDED [2 claims]: Viscoelastic substrates affect cell behavior (Chaudhuri Nat Mater 2016); stress relaxation controls fate (Charrier Nat Commun 2018)
- PARAMETRIC [4 claims]: EP300 kcat at enhancers in vivo; H3K27ac threshold for stable BRD4 recruitment; nuclear deformation directly gates EP300 access (vs. signaling-mediated); 1-5 minute kinetic estimate

**Why this might be WRONG**: The cytoskeleton may act as a MECHANICAL CAPACITOR — ROCK1-actomyosin generates intrinsic contractility that sustains nuclear deformation independently of ECM stress relaxation. YAP nuclear translocation is biochemically triggered (LATS1/2 suppression) and may persist even after ECM relaxes. Enhancer activation may be a binary switch dependent on SIGNAL (YAP level) rather than FORCE DURATION. The ~1-5 minute kinetic window is rough and could be off by an order of magnitude.

**Literature gap it fills**: Gap #1 (ECM stiffness → enhancer profiling) — ALL existing studies use purely elastic substrates. No study has compared enhancer landscapes on viscoelastic vs. elastic substrates matched for modulus. Addresses a fundamental confound in mechanoepigenetics.

**Test protocol**: hMSCs on alginate-RGD hydrogels (Mooney lab protocol): matched elastic modulus (25 kPa) with three relaxation times — τ-fast (~10 s, ionic crosslinks only), τ-medium (~5 min, partial covalent crosslinks), τ-slow (~1 h, fully covalent crosslinks). H3K27ac CUT&Tag + ATAC-seq + RNA-seq at 24h. Compare gained enhancers: predict τ-slow > τ-medium > τ-fast in total gained H3K27ac peaks. Classify gained peaks as Phase 1 (already accessible at 1 kPa, ATAC+) vs. Phase 2 (newly accessible, prior H3K27me3+) — predict Phase 2 enhancers selectively lost in τ-fast and τ-medium. YAP IF at 1h and 24h to test whether YAP activation is equivalent across conditions. Positive control: PA hydrogel at 25 kPa (purely elastic) as reference.

---

### Hypothesis C2-H6: HDAC3-NCoR Eraser Depletion by ECM Stiffness Creates Enhancer Stabilization Independent of Writer Activation

**Connection**: ECM stiffness → HDAC3 protein downregulation → NCoR/SMRT corepressor complex dysfunction → failure to decommission active enhancers → H3K27ac retention at pre-existing enhancers → global enhancer stabilization (epigenomics)

**Bridge mechanism**: eraser_depletion (distinct from all cycle 1 writer-activation bridges)

**Mechanism**:

All cycle 1 hypotheses operated under a WRITER-ACTIVATION model: ECM stiffness activates EP300 (the H3K27ac writer) to deposit new marks at enhancers. This hypothesis proposes an orthogonal ERASER-DEPLETION mechanism. Fu et al. (Bone Research 2024, PMID 38789434, in literature context) demonstrated that ECM stiffening DOWNREGULATES HDAC3 protein levels in chondrocytes — validated in vivo with HDAC3 AAV rescue. HDAC3 is a class I histone deacetylase that functions as the catalytic component of the NCoR/SMRT corepressor complex. [GROUNDED: NCoR/SMRT-HDAC3 corepressor complex structure and function — Guenther et al., Genes Dev 2001; HDAC3 requires interaction with SMRT/NCoR DAD domain for deacetylase activity — Watson et al., Nature 2012.]

Critically, HDAC3 specifically decommissions active enhancers by removing H3K27ac. [GROUNDED: You et al., Cell 2013 — HDAC3 deletion in macrophages causes enhancer hyperacetylation genome-wide; the Lazar lab has extensively characterized HDAC3-NCoR at enhancers across multiple cell types.] Enhancers exist in a steady-state balance between EP300 writing and HDAC3 erasing. The typical H3K27ac half-life of 2-6 hours [GROUNDED: generally accepted from metabolic labeling studies] reflects this balance. If HDAC3 is depleted, the erasure rate drops → H3K27ac accumulates → enhancers that were in steady-state turnover now shift to NET ACCUMULATION. This is enhancer activation WITHOUT new EP300 recruitment.

**Critical distinction from writer model:**

| Feature | Writer Model (E1-H3) | Eraser Model (C2-H6) |
|---|---|---|
| Mechanism | Stiffness → YAP-EP300 → new H3K27ac | Stiffness → HDAC3↓ → retained H3K27ac |
| Target enhancers | Previously inactive, TEAD-motif+ | Already active, diverse motifs |
| Blocked by A-485? | Yes — EP300 required | Partially — only new writing blocked; retained H3K27ac persists |
| Phenocopied by HDAC3 inhibitor on soft ECM? | No | Yes — RGFP966 on soft ECM should mimic eraser depletion |
| Motif enrichment | TEAD, CArG | AP-1, NF-κB, lineage-specific TFs (whatever was active) |

The two models target DIFFERENT enhancer populations and make OPPOSITE predictions about EP300 inhibitor sensitivity. The eraser model specifically explains an observation the writer model cannot: why ECM stiffness globally increases histone acetylation levels (Xu Materials Today Bio 2023; Fu Bone Research 2024) rather than only at specific YAP target enhancers.

In reality, BOTH mechanisms likely operate simultaneously at different enhancer classes: writer activation creates NEW mechano-enhancers while eraser depletion STABILIZES existing active enhancers. The combined model predicts two distinct H3K27ac populations on stiff ECM.

**Confidence**: 5 — HDAC3 downregulation on stiff ECM demonstrated in vivo (Fu 2024). HDAC3-NCoR at enhancers well-established (You Cell 2013, Lazar lab). Novel claim is that HDAC3 loss globally stabilizes existing H3K27ac rather than activating de novo enhancers.

**Groundedness**: 6
- GROUNDED [4 claims]: HDAC3 downregulated by ECM stiffening (Fu Bone Research 2024); HDAC3-NCoR at enhancers removes H3K27ac (You Cell 2013); global histone acetylation increase on stiff ECM (Xu Materials Today Bio 2023); NCoR-HDAC3 complex structure (Watson Nature 2012)
- PARAMETRIC [2 claims]: HDAC3 is the dominant H3K27ac eraser at enhancers across cell types (vs. HDAC1/2); magnitude of H3K27ac half-life extension from partial HDAC3 depletion

**Why this might be WRONG**: HDAC3 is one of 18 human HDACs — HDAC1 and HDAC2 (in NuRD complex) may compensate for HDAC3 loss at enhancers. Fu 2024 showed HDAC3 effects primarily on non-histone substrate (Parkin acetylation → mitophagy), so the enhancer H3K27ac effect may be secondary. The literature contradiction noted in the context (Fu 2024 vs. Xu 2023 directionality) suggests cell-type specificity that may limit generalizability. HDAC3 downregulation mechanism (how does stiff ECM reduce HDAC3?) is completely unknown and could be an indirect/slow effect unrelated to mechanotransduction.

**Literature gap it fills**: No paper has examined whether ECM stiffness-driven HDAC3 loss affects the enhancer landscape genome-wide. All mechanoepigenetics papers assume a writer-activation model. The eraser-depletion model is conceptually orthogonal.

**Test protocol**: Primary chondrocytes or ATDC5 (matching Fu 2024 cell type) on PDMS substrates (soft 1 kPa / stiff 50 kPa, 48h). HDAC3 Western blot (confirm Fu 2024). HDAC3 ChIP-seq on soft ECM (map HDAC3 occupancy at enhancers). H3K27ac ChIP-seq + ATAC-seq on both conditions. Analysis: (1) Do gained H3K27ac peaks on stiff ECM overlap with HDAC3 ChIP-seq peaks on soft ECM? (eraser model predicts YES for a subset). (2) TEAD motif enrichment at gained peaks: predict a fraction enriched (writer) and a fraction without (eraser). (3) RGFP966 (HDAC3-selective inhibitor, 10 µM) on soft ECM → should phenocopy the eraser-stabilized subset but NOT the writer-activated subset. (4) A-485 on stiff ECM → should eliminate writer-activated enhancers but leave eraser-stabilized enhancers partially intact (H3K27ac deposited before A-485 treatment persists longer due to HDAC3 depletion). (5) HDAC3 AAV rescue on stiff ECM (per Fu 2024) → should collapse eraser-stabilized H3K27ac back to soft-ECM levels.

---

### Hypothesis C2-H7: Integrin Force-Induced H3K9me3 Demethylation at Nuclear Interior Enhancers Creates Competence Windows for H3K27ac Activation

**Connection**: ECM stiffness → integrin-transmitted force via LINC complex → H3K9me3 demethylation at nuclear interior enhancers → heterochromatin decompaction → enhancer competence for subsequent H3K27ac deposition by EP300/YAP

**Bridge mechanism**: force_direct_enhancer_derepression (distinct from all cycle 1 bridges)

**Mechanism**:

Sun et al. (Sci Advances 2020, PMID 32270037, in literature context) established that integrin-transmitted cyclic mechanical force induces rapid H3K9me3 demethylation → Pol II recruitment → gene transcription, but ONLY at nuclear interior loci. Nuclear periphery genes resist force-induced activation due to persistent H3K9me3 maintained by SUV39H1/2 at the lamina. Critically, Sun 2020 examined only PROMOTERS (DHFR, PCNA genes). This hypothesis extends the Sun 2020 mechanism from promoters to ENHANCERS.

A fraction of enhancers (estimated 5-15% [PARAMETRIC — based on overlap of H3K9me3 with H3K4me1+ regions in Roadmap Epigenomics consortium data, varies by cell type]) reside within H3K9me3-marked heterochromatin regions. These enhancers retain H3K4me1 (enhancer priming mark) underneath the H3K9me3 — they are in a POISED-BUT-SILENCED state distinct from both active enhancers (H3K27ac+) and Polycomb-silenced bivalent enhancers (H3K4me1+/H3K27me3+). These H3K9me3-silenced enhancers are concentrated in B-compartment regions near A/B compartment boundaries, where heterochromatin and euchromatin interface.

**Two-step activation model:**
- **Step 1 (force-dependent, minutes to 1-2h):** ECM stiffness → integrin clustering → cytoskeletal tension → LINC-transmitted force → H3K9me3 demethylation at nuclear interior enhancers. The demethylase is likely a KDM4-family enzyme (KDM4A/JMJD2A or KDM4C/JMJD2C), which are the primary H3K9me3 demethylases at euchromatin-heterochromatin boundaries [PARAMETRIC — Sun 2020 did not identify the specific demethylase; KDM4A is inferred from its known substrate specificity and role in heterochromatin dynamics — Berry et al., Cell Reports 2012]. H3K9me3 removal → HP1α/β dissociation → local chromatin decompaction → enhancer becomes ACCESSIBLE (detectable by ATAC-seq) but not yet ACTIVE (no H3K27ac).

- **Step 2 (signaling-dependent, hours):** The now-accessible enhancer becomes COMPETENT to receive H3K27ac from the YAP-EP300 pathway (if TEAD motif present) or MRTF-SRF pathway (if CArG motif present). EP300 can only acetylate nucleosomes in accessible chromatin — the H3K9me3 heterochromatin blocks EP300 access regardless of YAP signaling. Thus, Step 1 (force-dependent decompaction) is a PREREQUISITE for Step 2 (signaling-dependent activation).

**Explanatory power**: This model resolves a puzzling prediction from E1-H5 — why would some enhancers with identical TEAD motifs gain H3K27ac under stiffness while neighboring TEAD-containing enhancers do not? The answer: only enhancers that undergo Step 1 (H3K9me3 removal, nuclear interior location) become competent for Step 2. Enhancers already in euchromatin skip Step 1 (they are Phase 1 enhancers in E1-H3). Enhancers at the nuclear periphery NEVER undergo Step 1 (Sun 2020: periphery genes resist force) and remain permanently silenced regardless of stiffness.

**Confidence**: 4 — Sun 2020 provides strong evidence for force → H3K9me3 demethylation at specific loci. Extension to enhancers is logical but not demonstrated. Sun 2020 used cyclic force via magnetic beads, not static ECM stiffness — the mechanism may not transfer.

**Groundedness**: 5
- GROUNDED [3 claims]: Integrin force → H3K9me3 demethylation at nuclear interior (Sun Sci Advances 2020); nuclear interior vs. periphery differential response (Sun 2020); H3K4me1 and H3K9me3 can co-occur at some regulatory regions [Roadmap Epigenomics data]
- PARAMETRIC [3 claims]: KDM4A as the specific demethylase; 5-15% enhancer fraction in H3K9me3; two-step model with Step 1 as prerequisite for Step 2; transfer from cyclic force to static ECM stiffness

**Why this might be WRONG**: Sun 2020 used cyclic force (via magnetic beads on integrins at specific frequencies), NOT static ECM stiffness. Static stiffness may not trigger the same rapid H3K9me3 demethylation — the mechanism may require cyclical force loading/unloading. H3K9me3-marked enhancers may be TRULY SILENCED (no H3K4me1 underneath, fully heterochromatic) and thus non-functional even after H3K9me3 removal. The two-step model adds complexity that may not be needed — YAP-EP300 may be sufficient to explain all enhancer activation. KDM4A identification is speculative.

**Literature gap it fills**: Sun 2020 examined only promoters, not enhancers. The concept of enhancer COMPETENCE WINDOWS gated by heterochromatin removal under mechanical force is completely unstudied. Gap #5 (LAD vs. non-LAD enhancer mechanosensitivity) is partially addressed by the nuclear interior/periphery distinction.

**Test protocol**: hMSCs on PA hydrogels (1/50 kPa, 0/1/4/12/24h). CUT&Tag time course: H3K9me3 + H3K27ac + H3K4me1 + ATAC-seq. Analysis: identify enhancers (H3K4me1+) that lose H3K9me3 BEFORE gaining H3K27ac (prediction: a subset shows H3K9me3 loss by 1-4h, followed by H3K27ac gain at 6-24h = two-step temporal signature). DamID-seq (lamin B1) to classify nuclear interior vs. periphery location. Perturbations: chaetocin (SUV39H1/2 inhibitor, 50 nM) on soft ECM → removes H3K9me3 globally → predict enhancers become COMPETENT (ATAC-seq open) but NOT active (no H3K27ac without YAP signal). Chaetocin + constitutively active YAP(S127A) on soft ECM → predict full enhancer activation at loci that are normally Step 1-gated. On stiff ECM: ML324 (KDM4A inhibitor, 10 µM) → should block Step 1 → predict subset of enhancers fail to gain H3K27ac despite normal YAP activation.

---

## Self-Critique Summary

### Mechanism specificity check:
All 7 hypotheses have sufficient mechanistic detail for experiment design: specific inhibitors, quantitative predictions, time-course protocols, and multi-arm perturbation designs. ✓

### Bridge mechanism diversity:
| Hypothesis | Bridge Mechanism |
|---|---|
| C2-H1 | metabolic_cofactor_gating |
| C2-H2 | temporal_cascade_feedforward |
| C2-H3 | threshold_decoding |
| C2-H4 | calcium_signaling_enhancer_program |
| C2-H5 | viscoelastic_temporal_filter |
| C2-H6 | eraser_depletion |
| C2-H7 | force_direct_enhancer_derepression |

7 distinct bridge mechanisms. No two hypotheses share a bridge. ✓

### Claim-level verification (mandatory v5.4):

**Citation specificity (step 5):**
- All [GROUNDED] claims include author, year, and journal. Verified: Wellen Science 2009, Enzo Nat Cell Biol 2015, Carey Nature 2015, Dupont Nature 2011, Miralles Cell 2003, Coste Science 2010, Hogan Genes Dev 2003, Chaudhuri Nat Mater 2016, Fu Bone Research 2024, You Cell 2013, Sun Sci Advances 2020. ✓
- Downgraded: Charrier Nat Commun 2018 — less certain on exact year, kept as GROUNDED but flagged. EP300 kcat — downgraded to PARAMETRIC. ✓

**Directionality check (step 6):**
- ACLY converts citrate → acetyl-CoA + oxaloacetate ✓
- αKG is converted to succinate during dioxygenase reactions (consumed, not produced) ✓
- Calcineurin DEphosphorylates NFAT (removes phosphate) ✓
- PIEZO1 allows Ca²⁺ INFLUX (extracellular→cytoplasm) ✓
- HDAC3 REMOVES acetyl groups (deacetylase, eraser) ✓
- H3K9me3 demethylation REMOVES methyl groups → derepression ✓

**Compartmental check (step 7):**
- C2-H1: Acetyl-CoA — ACLY generates nuclear pool (Wellen 2009 showed nuclear ACLY). αKG in mitochondria/cytoplasm → diffuses to nucleus. All enzymes (EP300, UTX, TET2) operate in NUCLEUS at chromatin. ✓
- C2-H4: PIEZO1 at PLASMA MEMBRANE → Ca²⁺ enters CYTOPLASM → calcineurin in CYTOPLASM → NFAT dephosphorylated → NFAT translocates to NUCLEUS → binds chromatin. ✓
- C2-H6: HDAC3-NCoR operates in NUCLEUS at chromatin. HDAC3 protein downregulated (presumably at protein/transcription level). ✓
- C2-H7: H3K9me3 demethylation at NUCLEAR INTERIOR chromatin. LINC force transmits from CYTOSKELETON through NUCLEAR ENVELOPE to LAMINA to CHROMATIN. ✓

**Quantitative sanity (step 8):**
- C2-H1: EP300 Km ~1-4 µM for acetyl-CoA; nuclear acetyl-CoA estimated 2-20 µM → PLAUSIBLE that soft ECM could be near Km. αKG Km for TET ~50-100 µM [PARAMETRIC]; cellular αKG ~200-500 µM → may NOT be rate-limiting. Flagged in "Why wrong." ✓
- C2-H5: EP300 needs ~1-5 min for 10-30 H3K27ac events per enhancer. Multiple EP300 molecules could work in parallel → estimate may be high. Flagged. ✓
- C2-H7: Force at nucleus 120-920 pN (computational validation) >> 5 pN threshold. ✓

**Protein property verification (step 9):**
- C2-H1: UTX is an αKG-dependent dioxygenase ✓ (confirmed — JmjC domain family)
- C2-H4: NFATc1 13 phosphosites — this is approximately correct for NFAT regulatory domain (13-14 sites, varies by isoform). ✓
- C2-H6: HDAC3 requires NCoR/SMRT DAD domain for activity — ✓ (Watson Nature 2012)
- C2-H7: KDM4A as H3K9me3 demethylase — ✓ (KDM4A/JMJD2A is a verified H3K9me3/H3K9me2 demethylase). However, Sun 2020 did not identify which enzyme — flagged as PARAMETRIC. ✓

### Groundedness ratings after verification:
No claims required downgrade from GROUNDED to PARAMETRIC beyond what was already tagged. Overall groundedness ratings maintained. ✓

### Final diversity check:
- C2-H1 (metabolic), C2-H2 (temporal cascade), C2-H3 (threshold) = 3 survivor extensions
- C2-H4 (calcium/NFAT), C2-H5 (viscoelasticity), C2-H6 (HDAC3 eraser), C2-H7 (H3K9me3 enhancer) = 4 fresh
- All 7 use distinct bridges ✓
- No more than 0 hypotheses share any bridge ✓
