# Final Hypotheses: Mechanobiology (ECM Mechanics) x Epigenomics (Enhancer Regulation)

Session: 2026-03-25-targeted-002 | Status: SUCCESS | 2 PASS + 4 CONDITIONAL_PASS

---

## PASS #1: YAP-BRD4 Condensate Supralinear Stiffness Encoding (H3)

**Score**: 7.85 | **Confidence**: 0.63 | **Groundedness**: 6/10 | **Disciplines**: mechanobiology, condensate biophysics, enhancer epigenomics

### Core Claim
YAP nuclear concentration increases approximately linearly with ECM stiffness (~4x from 1 to 50 kPa). However, BRD4-YAP-MED1 phase-separated condensate assembly at mechanoenhancers is cooperative (Hill coefficient n=2-4), creating supralinear transcriptional amplification. This means the cell's transcriptional response to ECM stiffness functions as a mechanical threshold switch at ~8-15 kPa, not a graded rheostat. This explains why fibrotic ECM (20-50 kPa) triggers dramatically different transcriptional programs than healthy ECM (1-5 kPa) despite only a 3-10x stiffness difference.

### Mechanism
ECM stiffness -> Hippo pathway -> YAP nuclear (linear, ~4x) -> YAP-BRD4 condensate at mechanoenhancers (cooperative, ~16-256x) -> transcriptional output proportional to stiffness^(1.5-3.0)

### Key Evidence
- [GROUNDED] YAP-BRD4 condensates at super-enhancers: Zanconato et al. 2018 Nature Medicine (269 citations)
- [GROUNDED] Endogenous YAP condensates with BRD4 under actin tension: iScience 2024 PMID 38784009
- [GROUNDED] Condensates are cooperative (threshold behavior): Shin et al. 2018 Cell
- [GROUNDED] EP300-BRD4 interaction: STRING 0.988
- [INFERRED] Hill coefficient n=2-4 for BRD4-YAP: estimated from generic LLPS biophysics
- [INFERRED] Threshold stiffness ~8-15 kPa: predicted from YAP concentration + BRD4 critical concentration

### Falsifiable Prediction
Transcriptional output of mechanoenhancer-controlled genes (CTGF, CYR61 by smFISH) on 5-point stiffness gradient (1, 5, 10, 20, 50 kPa) fits power law model (output proportional to stiffness^n, n>1.5) significantly better than linear model. BRD4 condensate volume (super-resolution) scales supralinearly with nuclear YAP. JQ1 (BRD4 inhibitor, 250 nM) linearizes the stiffness-transcription relationship.

### Counter-Evidence
- YAP nuclear concentration may plateau above ~20 kPa (PNAS 2021 spatial model)
- BRD4 condensate nature (true LLPS vs protein cluster) still debated
- BRD4 condensates sensitive to ATP levels, temperature, PTMs beyond mechanics

---

## PASS #2: Two-Phase Temporal Coincidence Gate (C2-H1)

**Score**: 7.85 | **Confidence**: 0.62 | **Groundedness**: 7/10 | **Disciplines**: mechanobiology, calcium signaling, enhancer epigenomics

### Core Claim
Mechanoenhancer activation requires two sequential phases that are NOT independent parallel pathways but obligatorily dependent. Phase 1 (Piezo1 -> Ca2+ -> CaMKII -> HDAC4/5 nuclear export -> EP300 derepression -> H3K27ac, <15 min) creates H3K27ac "landing pads" at mechanoenhancers. Phase 2 (YAP nuclear entry -> BRD4 reads H3K27ac -> BRD4-YAP condensate nucleation, 30-120 min) requires the Phase 1 marks for BRD4 bromodomain chromatin anchoring. Loss of Piezo1 abolishes BOTH phases, not just Phase 1.

### Mechanism
FAST LANE: ECM stiffness -> Piezo1 Ca2+ -> CaMKII -> HDAC4/5 Ser467/498 phosphorylation -> HDAC4/5 nuclear export -> EP300 freed from class IIa HDAC repression -> H3K27ac at mechanoenhancers (<15 min)
SLOW LANE: ECM stiffness -> cytoskeletal tension -> YAP nuclear (30-60 min) -> BUT BRD4 BD1/BD2 needs H3K27ac marks -> marks from FAST LANE serve as condensate nucleation sites

### Key Evidence
- [GROUNDED] BRD4 bromodomain binds acetylated histones (BD1/BD2 structure)
- [GROUNDED] CaMKII -> HDAC4 Ser467/498 phosphorylation -> nuclear export: Backs et al. 2006 J Clin Invest
- [GROUNDED] BRD4 heterogeneous nucleation on H3K27ac: Mol Biol Cell 2024 PMC11238092
- [GROUNDED] Piezo1 -> CaMKII activation within 3 min
- [INFERRED] H3K27ac from Phase 1 is necessary for BRD4 condensate nucleation in mechanoenhancer context -- well-supported by independent BRD4 condensation literature

### Falsifiable Prediction
Piezo1 KO (CRISPR) reduces H3K27ac at mechanoenhancers at BOTH 15 min AND 120 min on 50 kPa hydrogels. Piezo1 KO reduces BRD4 CUT&RUN at mechanoenhancers at 120 min. dCas9-p300 targeted to CYR61 mechanoenhancer in Piezo1 KO rescues BRD4 condensate nucleation at that locus (proving H3K27ac marks are the prerequisite, not other Piezo1 effects).

### Counter-Evidence
- HDAC5 not directly responsive to CaMKII -- requires HDAC4 hetero-oligomerization
- EP300 "freeing" via HDAC4/5 export is oversimplified; class IIa HDACs repress via NCoR/SMRT/HDAC3
- Cardiomyocyte-to-fibroblast translation gap for CaMKII/HDAC pathway

---

## CONDITIONAL_PASS #1: MRTF-A CaRG-Box Mechanoenhancer Occupancy (H4)

**Score**: 7.55 | **Confidence**: 0.62 | **Groundedness**: 7/10

### Core Claim
MRTF-A (mechanosensitive coactivator, nuclear on stiff ECM) binds CaRG-box motifs at mechanoenhancers on stiff ECM, directly recruiting EP300 (STRING 0.710) to deposit H3K27ac. This activates a cytoskeletal/contractility gene program spatially and functionally distinct from the YAP/TEAD program.

### Condition for Full PASS
MRTF-A ChIP-seq under ECM stiffness conditions required. Existing data shows promoter-dominant binding (Esnault 2014). If mechanical context shifts binding to enhancers, this is novel and significant. If binding remains promoter-dominant under mechanical conditions, hypothesis fails.

---

## CONDITIONAL_PASS #2: KDM6B Bivalent Ratchet in IPF (H1e)

**Score**: 7.25 | **Confidence**: 0.56 | **Groundedness**: 6/10

### Core Claim
In IPF fibroblasts (retaining epigenetic plasticity), a subset of mechanoenhancers carries bivalent chromatin (H3K4me1+H3K27me3) on soft ECM. ECM stiffening activates KDM6B (Tayler 2026), converting bivalent mechanoenhancers to active state. This is an irreversible "epigenetic ratchet" -- once H3K27me3 is removed, the cell cannot return to the bivalent state even if returned to soft ECM.

### Condition for Full PASS
CUT&RUN must confirm H3K27me3 at mechanoenhancer loci in IPF fibroblasts on soft ECM. If mechanoenhancers are primed (H3K4me1+/H3K27me3-) rather than bivalent, KDM6B has no substrate and the hypothesis is irrelevant.

---

## CONDITIONAL_PASS #3: Condensate Volume Threshold for Multi-Enhancer Hubs (H5e)

**Score**: 7.10 | **Confidence**: 0.53 | **Groundedness**: 5/10

### Core Claim
The 86.2% of mechanoenhancer-gene connections lacking annotated loops (Cosgrove 2025) are regulated via condensate-volume-dependent spatial co-localization. Above critical ECM stiffness (~8-15 kPa), YAP-BRD4 condensate volume crosses a threshold sufficient to physically capture multiple non-looped mechanoenhancers.

### Condition for Full PASS
Oligopaint FISH must demonstrate stiffness-dependent spatial proximity (<300 nm) at non-looped mechanoenhancer loci. RAD21 knockdown must NOT abolish contacts (proving cohesin-independence). IDR-deleted YAP mutant must abolish contacts (proving condensate-dependence).

---

## CONDITIONAL_PASS #4: Lamin A/C Cell-Intrinsic Threshold (C2-H2)

**Score**: 5.95 | **Confidence**: 0.42 | **Groundedness**: 8/10

### Core Claim
Cell-to-cell variation in lamin A/C expression calibrates the ECM stiffness threshold for mechanoenhancer activation. Low-lamin cells activate mechanoenhancers at lower stiffness than high-lamin cells.

### Condition for Full PASS
Must demonstrate advancement beyond 2024 Nat Comms (PMID 39578439) which already shows lamin A/C -> YAP threshold. The mechanoenhancer-specific H3K27ac resolution is the new contribution.
