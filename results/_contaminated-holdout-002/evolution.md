# Evolution: Mechanobiology × Enhancer Epigenomics
## Session: 2026-03-25-targeted-002 | Cycle 1 → Cycle 2 Prep | Generated: 2026-03-25

**Agent**: evolver-v5.2
**Evolution fodder**: H1 (KDM6B→EP300 Sequential Relay), H5 (YAP Condensates Looping-Independent E-P Contacts)
**Reference set (top 3 passers)**: H3 (YAP-BRD4 Supralinear Encoding), H4 (MRTF-A CaRG Mechanoenhancers), H2 (Piezo1→CaMKII Pre-Priming)
**Operations applied**: Specification (H1), Cell-type mutation (H1), Crossover (H5 × H3), Mechanistic specification (H5)
**Diversity constraint check**: Both evolved hypotheses are mechanistically distinct from H2/H3/H4 — PASSED

---

## EVOLUTION QUALITY CHECK (pre-output)

Before finalizing evolved hypotheses, verify:

1. **Does H1.evolved escape the false premise that killed H1?** YES — the cell-type mutation reframes H1 to contexts (IPF fibroblasts, MSCs) where H3K27me3 bivalency at mechanoenhancers IS biologically plausible based on published evidence (Tayler 2026, KDM6B in MSC osteogenesis; IPF fibroblasts retain progenitor epigenetic marks per clinical literature).

2. **Does H5.evolved escape the 5-competing-alternatives problem that weakened H5?** YES — the crossover with H3 makes a *quantitative* prediction (condensate volume threshold determines spatial proximity) that is measurable and distinguishable from transcription factory clustering or eRNA bridging alternatives, because only the LLPS cooperativity mechanism predicts a discrete threshold with power-law stiffness dependence.

3. **Do both evolved hypotheses add to the set (not duplicate H2/H3/H4)?**
   - H1.evolved focuses on H3K27me3 ERASURE in dedifferentiated/progenitor cells — completely separate from H2 (Ca²⁺→EP300 deposition), H3 (YAP condensate supralinear encoding in normal fibroblasts), H4 (MRTF-A occupancy). ✓
   - H5.evolved focuses on SPATIAL CO-LOCALIZATION mechanism (condensate volume → multi-enhancer hubs → looping-independent contacts), distinct from H3 (stiffness encoding supralinearity) and H4/H2 (TF binding/kinase circuits). ✓

4. **Is the evolution set diverse?** TOP 5 after evolution covers: calcium signaling (H2), condensate supralinear encoding (H3), CaRG-box TF binding (H4), mechanosensitive KDM erasure in progenitors (H1.evolved), looping-independent hub formation (H5.evolved). HIGH DIVERSITY. ✓

---

## H1 → H1e: Mechanoepigenetic Bivalency Switch in Fibroblast Progenitor Contexts

### Evolution type: CELL-TYPE MUTATION + SPECIFICATION

**Original H1** was conditional on: "H3K27me3 bivalency at mechanoenhancers exists in differentiated lung fibroblasts." This prerequisite was identified as a weak point — Cosgrove 2025 showed mechanoenhancers are ATAC-accessible on soft ECM, inconsistent with Polycomb-silenced state.

**Mutation applied**: Shift cell-type context from terminal lung fibroblasts to:
(a) **IPF (Idiopathic Pulmonary Fibrosis) fibroblasts** — partially dedifferentiated, known to retain bivalent marks from progenitor states; epigenetically reprogrammed relative to normal fibroblasts
(b) **MSCs (mesenchymal stem cells)** — where Tayler 2026 directly shows KDM4B/KDM6B activated by ECM stiffness and stress relaxation during osteogenesis

**Specification applied**: Target the bivalent mechanoenhancer subset specifically. Rather than claiming ALL mechanoenhancers are H3K27me3-marked, H1e specifies the *subpopulation* of mechanoenhancers that carry bivalent H3K27me3+H3K4me1 marks in these dedifferentiated/progenitor contexts.

---

### H1e Hypothesis

**Title**: KDM6B-Mediated Bivalent Mechanoenhancer Resolution as an Epigenetic Ratchet in IPF Fibrosis

**Field**: Mechanobiology × Enhancer Epigenomics

**Core claim**: In cells retaining epigenetic plasticity (IPF fibroblasts or MSCs), a subset of mechanoenhancers carries bivalent chromatin (H3K4me1+H3K27me3, poised-repressed state) on physiological soft ECM. ECM stiffening activates KDM6B (H3K27me3 demethylase) via cytoskeletal tension, converting bivalent mechanoenhancers to fully active (H3K4me1+H3K27ac) state. This is mechanistically distinct from the YAP→EP300 pathway (which works in any cell type at accessible, H3K27me3-free mechanoenhancers) and represents a cell-type-restricted "epigenetic ratchet" that drives irreversible fibrotic commitment under sustained stiffness.

**Mechanistic chain**:
ECM stiffness (>10 kPa) → cytoskeletal tension → KDM6B nuclear enrichment → KDM6B demethylates H3K27me3 at bivalent mechanoenhancers → removal of repressive mark → EP300 HAT now recruits freely → H3K27ac deposited → fibrotic gene program activated

**What distinguishes this from H1 (original)**:
- Restricted to IPF fibroblasts or MSCs, not terminal normal lung fibroblasts
- Bivalent mechanoenhancer subset specifically, not all mechanoenhancers
- Framed as "epigenetic ratchet" — irreversible under sustained stiffness (unlike YAP shuttling which reverses)
- Therapeutic implication: KDM6B inhibition in IPF (where bivalent subset exists) but not in normal tissue (where it doesn't)

**Grounded elements**:
- [GROUNDED] KDM6B activated by ECM stiffness/stress relaxation: Tayler et al. 2026 (Semantic Scholar ca0fc00f)
- [GROUNDED] KDM6B upregulation in response to ECM stiffness → H3K27me3 demethylation → EMT: Yu et al. 2025 (Semantic Scholar 251aa0922f)
- [GROUNDED] EP300-BRD4 STRING interaction: 0.988 (database-verified)
- [GROUNDED] Bivalent enhancers convert to active state during differentiation via KDM6B: Bernstein et al. 2006 Cell + KDM6B/JMJD3 enhancer activation literature
- [INFERRED] IPF fibroblasts retain bivalent marks at mechanoenhancers: plausible given dedifferentiation in IPF, but requires direct CUT&RUN verification

**Primary falsifiable prediction**:
KDM6B CUT&RUN + H3K27me3 CUT&RUN in IPF fibroblasts on 1 kPa vs 50 kPa shows:
(1) H3K27me3 is detectable at a subset of Cosgrove 2025 mechanoenhancers on 1 kPa (soft)
(2) H3K27me3 is lost at these loci on 50 kPa (stiff), coinciding with KDM6B occupancy
(3) KDM6B knockdown on stiff ECM maintains H3K27me3 and blocks H3K27ac at these bivalent-subset mechanoenhancers, despite accessible chromatin
(4) The same experiment in NORMAL lung fibroblasts shows NO H3K27me3 at mechanoenhancers on soft ECM — demonstrating the cell-type specificity

**Internal control** (comparing IPF vs normal): If H3K27me3 is present at mechanoenhancers in IPF but absent in normal fibroblasts, this establishes the cell-type prerequisite. Normal fibroblasts would show no KDM6B-dependent effect (H3K27ac already derepressed via YAP pathway alone), while IPF fibroblasts would show KDM6B-dependent H3K27me3 removal and H3K27ac deposition.

**Confidence**: 0.56 (well-grounded for KDM6B-stiffness connection; bivalent marks in IPF at mechanoenhancers specifically is inferred; IPF → mechanoenhancer bivalency link requires direct verification)

**Clinical significance**: If IPF fibroblasts harbor bivalent mechanoenhancers that KDM6B converts to active state under lung stiffening, then KDM6B inhibition (e.g., GSK-J4) could block ECM-stiffness-driven fibrotic gene activation specifically in IPF without affecting mechanosensing in healthy cells that lack the bivalent mechanoenhancer substrate.

**Counter-evidence to address**:
- IPF fibroblast epigenome is globally reprogrammed but bivalent mechanoenhancers specifically are unstudied
- KDM6B evidence is in MSC/thyroid cancer contexts, not IPF
- The ratchet model (irreversible) needs distinction from reversible YAP effects

---

## H5 → H5e: Condensate Volume Threshold Drives Looping-Independent Multi-Enhancer Hub Formation

### Evolution type: CROSSOVER (H5 × H3) + MECHANISTIC SPECIFICATION

**Original H5** was weakened by: 5 competing non-condensate mechanisms all predicting the same spatial co-localization outcome; verteporfin mechanism wrong; low mechanistic specificity.

**Crossover applied**: Combine H5's *spatial co-localization* premise with H3's *condensate volume supralinear encoding* model. H3 predicts BRD4-YAP condensate size scales supralinearly with ECM stiffness. H5 predicts looping-independent E-P contacts at mechanoenhancers. The crossover: **condensate size IS the determinant of multi-enhancer spatial co-localization** — small condensates can't bridge spatially-separated enhancers, large (supralinear) condensates can, explaining the 86.2% anomaly.

**Mechanistic specification applied**: Replace the generic "condensate-driven spatial proximity" with a specific quantitative model: condensate radius (R) must exceed the genomic distance-in-3D between non-looped mechanoenhancer and target promoter (~200–500 nm based on polymer physics) for productive contact. This threshold is crossed only on stiff ECM (supralinear condensate growth from H3 model).

---

### H5e Hypothesis

**Title**: YAP-BRD4 Condensate Size Threshold Explains Looping-Independent Multi-Enhancer Hub Formation at Mechanoenhancers

**Field**: Mechanobiology × Condensate Biophysics × 3D Genome Architecture

**Core claim**: The 86.2% of mechanoenhancer-gene connections lacking annotated chromatin loops (Cosgrove 2025) are regulated via condensate-volume-dependent spatial co-localization. Below a critical stiffness (~8–15 kPa), YAP-BRD4 condensates are too small to bridge the spatial gap between non-looped mechanoenhancers and target promoters. Above this threshold, condensate volume crosses a size threshold sufficient to physically co-locate multiple non-looped mechanoenhancers and their gene targets, creating "multi-enhancer hubs" without cohesin-dependent extrusion. This directly links the supralinear condensate encoding model (H3) to the looping-independent mechanism (anomaly from H5).

**Mechanistic chain**:
ECM stiffness (above threshold ~8–15 kPa) → YAP nuclear enrichment supralinear → YAP-BRD4 condensate volume supralinear → condensate radius crosses 200–500 nm → spatial capture of non-looped mechanoenhancers within condensate volume → multi-enhancer hub forms → transcription factor clustering amplifies transcriptional output → looping-independent E-P activation

**Critical distinction from H5 (original)**:
H5 made the vague claim "condensates mediate looping-independent contacts" without specifying WHY condensates do this while competing mechanisms (eRNAs, transcription factories, etc.) don't, and without a threshold prediction. H5e predicts:
- A **specific stiffness threshold** (~8–15 kPa, matching H3 condensate assembly threshold) above which non-looped E-P contacts form
- **Condensate radius dependency**: contacts form only when condensate radius exceeds spatial gap between loci (testable by STORM + super-resolution Hi-C simultaneously)
- **COHESIN independence**: non-looped contacts are NOT abolished by WAPL/RAD21 knockdown (cohesin removal), distinguishing from cohesin-dependent looping
- **IDR-deleted YAP abolishes contacts**: condensate-incompetent YAP (same nuclear concentration) cannot form the multi-enhancer hub despite same transcription factor availability

**Grounded elements**:
- [GROUNDED] 86.2% of mechanoenhancer-gene connections lack annotated chromatin loops: Cosgrove et al. 2025, Science
- [GROUNDED] YAP condensates form in response to actin cytoskeletal tension: iScience 2024, PMID 38784009
- [GROUNDED] Condensate volume scales cooperatively with TF concentration: Shin et al. 2018, Cell + general LLPS literature
- [GROUNDED] YAP nuclear concentration increases ~4x from soft to stiff ECM: Dupont et al. 2011 Nature
- [GROUNDED] Phase-separated condensates can mechanically restructure nearby chromatin: Shin et al. 2018, Cell
- [INFERRED] Specific condensate radius of 200–500 nm sufficient to bridge non-looped mechanoenhancer-promoter pairs: requires STORM measurement at Cosgrove 2025 loci
- [INFERRED] Condensate volume threshold matches stiffness threshold from H3: logical prediction but not experimentally confirmed

**Primary falsifiable prediction**:
In human lung fibroblasts on stiff ECM (50 kPa):
(1) Non-looped mechanoenhancer pairs (from Cosgrove 2025 catalog) show <300 nm spatial proximity (measured by ORCA or MERFISH)
(2) This spatial proximity is **NOT abolished** by RAD21/WAPL knockdown (confirming loop-independence)
(3) This spatial proximity **IS abolished** by IDR-deleted YAP mutant (same nuclear concentration, condensate-incompetent)
(4) The stiffness-proximity relationship follows a threshold (contacts present only above ~8–15 kPa, matching H3 condensate threshold)

On soft ECM (1 kPa): non-looped mechanoenhancer pairs show >500 nm spatial distances (outside condensate capture radius).

**Critical discriminant**: IDR-deleted YAP vs wild-type YAP comparison is the cleanest test. If spatial proximity depends on YAP IDR (condensate), this supports H5e. If spatial proximity persists with IDR-deleted YAP, it supports a transcription factory or eRNA alternative.

**Confidence**: 0.53 (yAP condensates confirmed in relevant contexts now via iScience 2024; threshold prediction is quantitatively specific; but looping-independent E-P spatial co-localization at mechanoenhancers has not been directly measured; requires ORCA/MERFISH spatial genomics which is technically demanding)

**Connection to anomaly**: This hypothesis DIRECTLY EXPLAINS the Cosgrove 2025 anomaly: 86.2% of mechanoenhancer-gene connections lack loops because the dominant mechanism is condensate-volume-dependent spatial co-localization (stiffness-sensitive), not cohesin extrusion (stiffness-insensitive). Stiff ECM drives condensate growth → spatial capture → activation. Soft ECM → condensates below threshold → only 13.8% of connections (those with pre-existing loops) remain active.

**Counter-evidence to address**:
- Transcription factory clustering makes a similar spatial prediction
- Condensate size quantification in physiological-stiffness fibroblasts is not yet done
- ORCA/MERFISH resolution at single-locus level may not distinguish 200 nm from 300 nm robustly

---

## EVOLUTION SUMMARY TABLE

| ID | Original | Operation | Title | Confidence | Key Advance |
|----|----------|-----------|-------|------------|-------------|
| H1e | H1 | Cell-type mutation + Specification | KDM6B Bivalency Ratchet in IPF Fibroblasts | 0.56 | Resolves false premise by targeting cells WHERE bivalency is plausible; adds irreversibility/clinical angle |
| H5e | H5 × H3 | Crossover + Quantitative specification | Condensate Volume Threshold for Looping-Independent Hubs | 0.53 | Merges supralinear encoding (H3) with looping-independent mechanism (H5); directly explains 86.2% anomaly |

## DIVERSITY CHECK

Final 5-hypothesis set after evolution:
| ID | Mechanistic Class | Confidence |
|----|-------------------|------------|
| H3 | Condensate biophysics × stiffness supralinear encoding | 0.63 |
| H4 | TF (MRTF-A) binding at CaRG-box mechanoenhancers | 0.62 |
| H2 | Ion channel kinase (Piezo1-CaMKII) temporal pre-priming | 0.60 |
| H1e | KDM6B epigenetic demethylase ratchet (IPF/progenitor context) | 0.56 |
| H5e | Condensate volume threshold → multi-enhancer hub (looping-independent mechanism) | 0.53 |

**Overlap check**:
- H3 vs H5e: RESOLVED. H3 asks *HOW MUCH* stiffness drives transcription (supralinear scaling). H5e asks *WHERE* this happens (spatial co-localization mechanism). Complementary, not redundant.
- H1e vs H2: RESOLVED. H2 is fast (<15 min, reversible, normal fibroblasts). H1e is slow (hours, irreversible, IPF/progenitor cells). Mechanistically distinct.
- H4 vs H1e: RESOLVED. H4 is MRTF-A TF binding → H3K27ac deposition. H1e is KDM6B → H3K27me3 erasure (derepression, not deposition). Different marks, different enzymes, different cell contexts.

**Diversity status**: HIGH ✓

---

## EVOLVER NOTES

**H1 evolution rationale**: The KDM6B concept has strong biological logic and two papers directly supporting ECM stiffness → KDM6B → demethylation (Tayler 2026, Yu 2025). The problem was cell-type specificity — in terminal fibroblasts, mechanoenhancers are already ATAC-accessible (not Polycomb-repressed). IPF fibroblasts are the natural fix: they are known to be epigenetically reprogrammed relative to normal fibroblasts, retain markers of progenitor plasticity, and drive fibrosis through sustained ECM stiffening. This makes the bivalent mechanoenhancer premise physiologically sound. The "epigenetic ratchet" framing is a meaningful conceptual advance — distinguishing from reversible YAP-based mechanosensing.

**H5 evolution rationale**: H5 was the weakest hypothesis by Ranker (7.10) because of 5 competing alternatives at the same mechanistic level. The crossover with H3 solves this: by predicting a *quantitative threshold* (condensate radius > spatial gap), H5e now makes a distinguishable prediction. The competing mechanisms (eRNA bridges, transcription factories) do NOT predict a stiffness threshold for spatial co-localization with STORM-measurable condensate radius scaling. The power of this crossover is that a single STORM experiment measuring condensate radius simultaneously with ORCA measuring spatial proximity would test BOTH H3 (radius supralinear) and H5e (radius crosses threshold for contact) in one experiment.
