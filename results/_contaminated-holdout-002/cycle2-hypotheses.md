# Cycle 2 Hypotheses: Mechanobiology × Enhancer Epigenomics
## Session: 2026-03-25-targeted-002 | Cycle 2 | Generated: 2026-03-25

**Agent**: generator-v5.2 | Cycle 2
**Informed by**: Cycle 1 critique questions (CQ1-CQ5), evolved hypotheses (H1e, H5e), Quality Gate new evidence
**Recommended focus areas**: H1, H4, H2 (from critic_summary)
**Hypotheses generated**: 3

---

## CYCLE 2 GENERATION STRATEGY

The critic questions from cycle 1 are answered. CQ1 (CaMKII→HDAC4/5 route) → confirmed by literature. CQ2 (bivalent enhancers) → addressed by H1e. CQ3 (YAP condensates in fibroblasts) → partially confirmed by iScience 2024. CQ4 (IDR-deleted YAP) → built into H5e. CQ5 (CUT&RUN at mechanoenhancers) → identified as foundational experiment.

Cycle 2 generation focuses on what was NOT captured in cycle 1: **emergent properties of the mechanoenhancer system** — temporal coordination, cell-to-cell heterogeneity, and the mutual dependency between the fast (Piezo1) and slow (YAP) pathways. These are second-order consequences of the cycle 1 mechanistic chain, not reworkings of existing hypotheses.

---

## C2-H1: Two-Phase Mechanoenhancer Activation Constitutes a Temporal Coincidence Gate

**Confidence**: 0.61
**Disciplinary distance**: 3 (mechanobiology × calcium signaling × enhancer epigenomics)

### Core claim

The Piezo1-CaMKII-HDAC4/5-EP300 axis (Phase 1, <15 min) does not simply provide an independent route to H3K27ac at mechanoenhancers — it is a **prerequisite** for the YAP-BRD4 condensate amplification step (Phase 2, 30-120 min). Without Phase 1 H3K27ac pre-marking, YAP-BRD4 condensates cannot nucleate at mechanoenhancers because BRD4 requires acetylated H3K27 for bromodomain-mediated chromatin anchoring. The two phases therefore constitute a TEMPORAL COINCIDENCE GATE: a cell on stiff ECM that lacks Piezo1 activity (GsMTx4, Piezo1 KO) will fail both Phase 1 AND Phase 2 — not just Phase 1 — because Phase 2 requires the H3K27ac marks deposited by Phase 1.

This is conceptually distinct from both H2 (which treats Phase 1 as independent) and H3 (which treats YAP-BRD4 condensates as the primary mechanism). The integrated model predicts that Piezo1 loss abolishes the entire mechanoenhancer gene program, not just its early (15-min) component.

### Mechanistic chain

ECM stiffness → PARALLEL:
- FAST LANE: Piezo1 → Ca²⁺ → CaMKII → HDAC4/5 nuclear export → EP300 freed → H3K27ac at mechanoenhancers (within 15 min)
- SLOW LANE: Stiffness-integrin-cytoskeleton → YAP nuclear entry (30-60 min) → YAP-BRD4 condensate assembly → BUT: BRD4 bromodomain binding requires H3K27ac → H3K27ac marks from FAST LANE are the nucleation sites for SLOW LANE condensates

**Mutual dependency**: Phase 1 MARKS → Phase 2 AMPLIFIES. Without marks, no amplification. Without amplification, gene expression remains low despite H3K27ac marks.

### Grounded elements

- [GROUNDED] Piezo1 → CaMKII activation (within 3 min): Multiple 2025 papers (NEC paper confirmed in QG)
- [GROUNDED] BRD4 bromodomain binds acetylated histones (H3K27ac, H3K14ac): BRD4 BD1/BD2 structure + multiple reviews
- [GROUNDED] H3K27ac at mechanoenhancers increases with stiffness (indirect from CYR61, CTGF loci): Cosgrove 2025 extended data + H4 QG note
- [GROUNDED] YAP-BRD4 condensates form at acetylated chromatin regions: Zanconato 2018; iScience 2024
- [INFERRED] Phase 1 H3K27ac marks are NECESSARY for Phase 2 BRD4 condensate nucleation: the mechanism is logical (BRD4 bromodomain requires H3K27ac) but has not been directly tested in the mechanoenhancer context

### Primary falsifiable prediction

In human lung fibroblasts on stiff ECM (50 kPa):
1. **Piezo1 KO reduces H3K27ac at mechanoenhancers at BOTH 15 min AND 120 min** (not just 15 min)
2. **Piezo1 KO reduces BRD4 CUT&RUN at mechanoenhancers at 120 min** (condensate nucleation lost)
3. **YAP overexpression on soft ECM CANNOT drive BRD4 condensates at mechanoenhancers** without prior H3K27ac establishment

Critical discriminant: Add exogenous H3K27ac to Piezo1 KO cells (using p300 activator or dCas9-p300 targeted to mechanoenhancers) → this should rescue BRD4 condensate nucleation in Piezo1 KO, proving that H3K27ac marks are the prerequisite, not Piezo1 signaling per se.

### Test protocol

Cell system: Piezo1 KO (CRISPR) and control human lung fibroblasts
Substrate: 1 kPa vs 50 kPa hydrogels
Time course: 0, 15, 30, 60, 120 min
Assay: CUT&RUN for H3K27ac (EP300 activity), BRD4 occupancy, YAP (ChIP by proximity)
Rescue: dCas9-p300 targeted to CYR61 mechanoenhancer → test BRD4 condensate by STORM
Focus loci: CYR61, CTGF, MYH9

### Counter-evidence and limitations

- BRD4 may nucleate at mechanoenhancers via YAP protein-protein interaction independent of H3K27ac
- H3K27ac from the basal state (soft ECM) may be sufficient for BRD4 nucleation even without Phase 1 increase
- The coupling may be unidirectional (Phase 1 enhances Phase 2) rather than obligatory (Phase 1 required for Phase 2)

### Critique self-check

**FALSE_PREMISE check**: H3K27ac at soft ECM mechanoenhancers is already present (they are ATAC-accessible). Does this challenge the "Phase 1 marks are required for BRD4 nucleation" premise? PARTIAL — if H3K27ac already exists at soft ECM levels, Phase 1 increase may still be quantitatively required for condensate threshold crossing. The argument: condensate NUCLEATION requires a minimum H3K27ac density, which is only achieved after Phase 1 increase.

**MECHANISTIC_CHAIN check**: Is BRD4 bromodomain H3K27ac binding the dominant mode of BRD4 anchoring? Some literature suggests BRD4 phase-separation is transcription factor-mediated (YAP interaction) rather than purely histone-mark mediated. Acknowledge: BRD4 may be brought to mechanoenhancers via YAP (protein-protein) rather than via H3K27ac (bromodomain). The prediction still holds if BRD4 phase-separation REQUIRES H3K27ac-dense chromatin for stable condensate assembly.

---

## C2-H2: Lamin A/C Concentration Sets the Cell-Intrinsic Stiffness Sensing Threshold for Mechanoenhancer Activation

**Confidence**: 0.58
**Disciplinary distance**: 2 (mechanobiology × enhancer epigenomics, with nuclear mechanics bridging)

### Core claim

Even on a uniform-stiffness substrate, individual cells show heterogeneous nuclear YAP concentrations and heterogeneous mechanoenhancer H3K27ac levels. This cell-to-cell variability is not noise — it is systematically controlled by nuclear lamin A/C content. Cells with low lamin A/C (soft, deformable nuclei) concentrate nuclear YAP more effectively at any given ECM stiffness, lowering their effective stiffness sensing threshold. Cells with high lamin A/C (stiff nuclei) require a higher ECM stiffness to achieve equivalent YAP nuclear enrichment. Lamin A/C therefore acts as a CELL-INTRINSIC RHEOSTAT that calibrates the mechanoenhancer H3K27ac response.

This is distinct from H4 (which focuses on MRTF-A at CaRG-box mechanoenhancers) and H2 (which focuses on Piezo1 kinetics). It addresses the cell-population heterogeneity that all hypotheses so far have treated as unexplained variance.

### Mechanistic chain

Stiff ECM → cytoskeletal tension → LINC complex (SUN1/SUN2, nesprin) → nuclear deformation → two competing effects:
- High lamin A/C: nuclear stiffness resists deformation → less mechanical signal transmitted to chromatin → higher YAP activation threshold
- Low lamin A/C: nuclear deformability → greater chromatin deformation → lower YAP activation threshold → mechanoenhancers activated at lower stiffness

Consequence: Within a cell population on uniform ECM, lamin A/C variability creates a distribution of stiffness-sensing thresholds → some cells activate mechanoenhancers, others don't → population-level heterogeneity in fibrotic gene expression.

### Grounded elements

- [GROUNDED] Lamin A/C expression scales with ECM stiffness (stiff ECM → more lamin A/C): multiple papers 2011-2025
- [GROUNDED] Lamin A/C knockout → increased nuclear deformability → enhanced mechanosensing in some contexts: multiple 2023-2025 papers
- [GROUNDED] Nuclear YAP concentration shows cell-to-cell variability on uniform substrates: observable in published single-cell IF images
- [GROUNDED] Lamin A/C determines nuclear mechanical stiffness (Young's modulus ~2-3 kPa with lamin, ~0.1-0.3 kPa without): Swift et al. 2013 Science
- [INFERRED] Lamin A/C variability translates to H3K27ac variability at mechanoenhancers in a quantitatively predictable way — requires direct CUT&RUN measurement

### Primary falsifiable prediction

In human lung fibroblasts on 10 kPa hydrogels (intermediate stiffness):
1. Single-cell H3K27ac at CYR61 mechanoenhancer (scCUT&RUN or CUT&RUN coupled with lamin A/C IF) shows BIMODAL distribution — cells are either "on" or "off" at this locus
2. "ON" cells have systematically lower lamin A/C protein levels than "OFF" cells (quantified by IF)
3. lamin A/C overexpression (doxycycline-inducible lamin A) shifts the stiffness threshold RIGHT: cells now require HIGHER stiffness to activate mechanoenhancers
4. Progeria (mutant lamin A/C, dysfunctional) shifts threshold LEFT: mechanoenhancers activate at LOWER stiffness

### Test protocol

Cell system: Human lung fibroblasts + lamin A/C knockdown (siRNA) + lamin A overexpression lines
Substrate: 5-point stiffness gradient (1, 5, 10, 20, 50 kPa)
Assay: scCUT&RUN for H3K27ac (10-cell resolution) + lamin A/C quantitative IF (same cells)
Statistical: Threshold stiffness (EC50) for H3K27ac at CYR61 mechanoenhancer vs lamin A/C level
Control: Progerin-expressing cells (premature aging, aberrant lamin A) as positive shift control

### Counter-evidence and limitations

- Lamin A/C variability is correlated with cell cycle stage; proliferating cells have less lamin A/C → confounded with cycling vs quiescent
- The bimodal distribution may reflect TAD-level chromatin state switching (binary gene activation) rather than lamin A/C threshold
- Single-cell CUT&RUN resolution at individual loci is technically challenging

---

## C2-H3: Nuclear Actin Polymerization State Directly Regulates MRTF-A Residence Time at CaRG-Box Mechanoenhancers

**Confidence**: 0.60
**Disciplinary distance**: 2 (mechanobiology × enhancer epigenomics)

### Core claim

MRTF-A nuclear localization is regulated by cytoplasmic G-actin/F-actin ratio, but MRTF-A ChIP-seq residence time at specific CaRG-box mechanoenhancers is additionally regulated by NUCLEAR actin polymerization dynamics. On stiff ECM, nuclear F-actin structures form (SRF-dependent nuclear actin assembly). These nuclear F-actin fibers physically tether MRTF-A to CaRG-box-containing chromatin, increasing its dwell time and thus EP300 recruitment efficiency. On soft ECM, nuclear actin is predominantly G-form → MRTF-A releases rapidly from CaRG-box motifs → H3K27ac not deposited despite MRTF-A nuclear entry.

This mechanistic specificity (nuclear F-actin as chromatin tether, not just cytoplasmic G-actin as release switch) explains why MRTF-A nuclear localization alone is insufficient for CaRG-box mechanoenhancer activation on intermediate stiffness substrates.

### Mechanistic chain

Stiff ECM → cytoskeletal tension → cortical F-actin → MRTF-A nuclear entry (classical) AND → nuclear actin polymerization (via mDia1/FHOD3 formin activity in nucleus) → nuclear F-actin cables → MRTF-A RPEL domain contacts nuclear F-actin → MRTF-A RESIDENCE TIME at CaRG-box chromatin increases (minutes from seconds) → EP300 dwell time increases proportionally → H3K27ac above threshold for enhancer activation

### Grounded elements

- [GROUNDED] MRTF-A nuclear localization is G-actin-depletion dependent: Miralles et al. 2003 Cell
- [GROUNDED] Nuclear actin polymerization occurs under mechanical stimulation and during SRF-target gene activation: Baarlink et al. 2013 Science + multiple reviews
- [GROUNDED] Formin mDia1 promotes nuclear actin polymerization: Baarlink et al. 2013 Science
- [GROUNDED] Nuclear F-actin structures are detectable by phalloidin-LifeAct in stimulated cells: Multiple 2020-2025 papers
- [INFERRED] MRTF-A RPEL domain contacts nuclear F-actin to increase CaRG-box dwell time: logical (RPEL is the G-actin binding domain), but nuclear F-actin binding by MRTF-A RPEL has not been demonstrated in the context of mechanoenhancer occupancy

### Primary falsifiable prediction

In human lung fibroblasts on stiff ECM (50 kPa):
1. **MRTF-A CUT&RUN dwell time** (measured by kymography/SPT-CRISPR-tag) at CaRG-box mechanoenhancers is LONGER on stiff vs soft ECM, even when nuclear MRTF-A concentration is EQUAL (achieved by Latrunculin A treatment on stiff ECM, which depletes G-actin and drives nuclear entry but prevents nuclear F-actin assembly)
2. **Formin inhibitor (SMIFH2)** on stiff ECM: blocks nuclear F-actin polymerization, reduces MRTF-A CUT&RUN at CaRG-box mechanoenhancers despite equal nuclear MRTF-A concentration
3. **LifeAct-nuclear actin** imaging: nuclear F-actin structures co-localize with CaRG-box mechanoenhancer chromatin regions on stiff ECM (measured by live-cell imaging + DNA FISH)

### Test protocol

Cell system: MRTF-A-HaloTag endogenous knock-in, human lung fibroblasts
Substrate: 1 kPa vs 50 kPa hydrogels
Primary assay: Live SPT of MRTF-A-HaloTag: measure dwell time at chromatin (FCS, SMT)
Perturb: SMIFH2 (formin inhibitor, blocks nuclear F-actin) vs jasplakinolide (stabilizes F-actin, promotes nuclear F-actin) on soft ECM
Co-assay: LifeAct-GFP (nuclear actin visualization) + CUT&RUN for MRTF-A (steady-state occupancy)
Focus: CaRG-box mechanoenhancers (from Cosgrove 2025) vs non-CaRG mechanoenhancers (internal control)

### Counter-evidence and limitations

- SMIFH2 has many off-target effects (other formins, myosin)
- Nuclear F-actin polymerization is controversial — not all groups observe stable nuclear F-actin in non-stimulated conditions
- MRTF-A dwell time at enhancers may be regulated by SRF association (protein-protein) rather than actin tethering

### Critique self-check

**FALSE_PREMISE check**: Nuclear F-actin existence in fibroblasts is well-established (Baarlink 2013, multiple 2025 papers) but formation in response to physiological hydrogel stiffness is less certain. However, since stiff ECM drives cortical F-actin (established), and nuclear F-actin in response to mechanical stimulation is established, the extrapolation is reasonable.

**MECHANISTIC_CHAIN check**: MRTF-A RPEL domain binds G-actin (established). Does it also bind F-actin? The evidence is indirect — nuclear F-actin assembly by MRTF-A downstream targets is established, but direct MRTF-A RPEL/F-actin binding is not published. The dwell-time prediction is testable regardless of the specific molecular interaction.

---

## CYCLE 2 SELF-CRITIQUE

### Cross-hypothesis compatibility check

**C2-H1 × C2-H3**: Compatible. C2-H1 is about temporal dependency (Phase 1 Piezo1 MARKS → Phase 2 YAP AMPLIFIES). C2-H3 is about MRTF-A residence time on nuclear F-actin. They operate on different timescales (C2-H1: 15-120 min kinetics; C2-H3: steady-state MRTF-A occupancy) and different proteins (Piezo1/YAP/BRD4 vs MRTF-A/formin). COMPLEMENTARY. ✓

**C2-H1 × C2-H2**: Complementary. C2-H1 addresses temporal coordination (fast/slow phases). C2-H2 addresses cell-to-cell heterogeneity (lamin A/C threshold). Both are true simultaneously in a population. ✓

**C2-H2 × C2-H3**: Compatible. C2-H2 explains YAP-dependent mechanoenhancer heterogeneity. C2-H3 explains MRTF-A-specific mechanism. Different proteins, different regulatory axes, non-overlapping. ✓

### Novelty check vs cycle 1 hypotheses

- C2-H1 is NOT a rehash of H2 (Piezo1 pre-priming): H2 treats Phase 1 and Phase 2 as independent. C2-H1 proposes H3K27ac dependency between phases — a genuinely new claim.
- C2-H2 is NOT a rehash of H4 (MRTF-A CaRG): H4 asks IF MRTF-A binds CaRG mechanoenhancers. C2-H2 asks WHY individual cells on the same stiffness respond differently to any mechanosensory signal.
- C2-H3 is NOT a rehash of H4: H4 predicts MRTF-A occupancy at CaRG-box mechanoenhancers. C2-H3 explains the MOLECULAR MECHANISM of that occupancy (nuclear F-actin dwell time regulation).

**All three are genuine cycle 2 advances.**

---

## HYPOTHESES SUMMARY TABLE

| ID | Title | Confidence | Distance | Focus area |
|----|-------|------------|----------|------------|
| C2-H1 | Two-Phase Temporal Coincidence Gate | 0.61 | 3 | H2 area (Piezo1 kinetics) |
| C2-H2 | Lamin A/C as Stiffness-Sensing Threshold Rheostat | 0.58 | 2 | H1 area (cell context) |
| C2-H3 | Nuclear Actin Regulates MRTF-A CaRG Dwell Time | 0.60 | 2 | H4 area (MRTF-A mechanism) |
