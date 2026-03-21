# Literature Context: Fe-S Cluster Biogenesis (Field A) — Session 007

**Target:** Fe-S cluster biogenesis × Circadian clock regulation
**Date:** 2026-03-21
**Focus:** Field A — Fe-S Cluster Biogenesis Machinery
**MCP Status:** MCP UNAVAILABLE (connection error) — fell back to WebSearch + WebFetch
**STRING API:** Queried successfully (6 proteins, human)
**KEGG API:** Queried successfully (NFS1 gene hsa:9054, hsa04122 pathway)

---

## Recent Breakthroughs in Fe-S Cluster Biogenesis (2024-2025)

### 1. FDX2 Two-Stage Binding Mechanism (Steinhilper et al. 2024, Nature Communications)
- **Finding:** Cryo-EM structures reveal FDX2 binds the ISC complex in DISTAL (23 Å from assembly site) and PROXIMAL (14 Å) conformations
- **Key mechanism:** Distal→Proximal conformational change is required for electron transfer. FDX2 and frataxin compete for overlapping sites — sequential binding creates regulatory node
- **Significance:** First structural explanation for how FDX2 delivers electrons. The conformational competition with FXN creates a tunable rate control point
- **Source:** PMID 39632806, Nature Commun. 2024; full text via PubMed fetch

### 2. Cross-Regulation by FDX2 and Frataxin (Lill group, Nature 2025)
- **Finding:** Efficient [2Fe-2S] synthesis requires ~equimolar FDX2:FXN. ANY deviation (excess of either) DOWNREGULATES Fe-S synthesis
- **Key mechanism:** FXN excess impairs FDX2 persulfide reductase; FDX2 excess slows persulfide transfer to ISCU2
- **Significance:** STOICHIOMETRIC RATIO is the regulatory parameter — not just activity. Creates a bistable-like regulatory circuit
- **Therapeutic:** FDX2 knockdown in FRDA Drosophila extends lifespan — validates the antagonism in vivo
- **Source:** DOI 10.1038/s41586-025-09822-1, Nature 2025; abstract from search

### 3. GLRX5 as Three-Way Central Hub (Pandey et al. 2025, JBC)
- **Finding:** GLRX5 routes [2Fe-2S] clusters to three distinct destinations: (1) direct mitochondrial recipients, (2) ISA complex for [4Fe-4S] generation, (3) ABCB7 transporter for cytoplasmic export
- **Key mechanism:** Without GLRX5, ALL downstream Fe-S proteins fail — central hub function. Cluster transfer is GSH/redox-dependent
- **Significance:** GLRX5 is the highest-leverage regulatory node; controls entire downstream Fe-S proteome
- **Source:** PMID 40074084, JBC 2025; full text via PubMed fetch

### 4. D-Cysteine as NFS1 Inhibitor (Zangari et al. 2025, Nature Metabolism)
- **Finding:** D-cysteine (mirror image of L-Cys) selectively inhibits NFS1 by steric blockage. Cancer-selective via xCT/CD98 transporter overexpression
- **Key parameters:** Kdapp (d-Cys) = 25.6 µM vs. Kdapp (l-Cys) = 2.15 µM (12-fold selectivity)
- **Downstream effects:** Mitochondrial respiration, nucleotide metabolism, genome integrity all disrupted
- **Significance:** First pharmacological proof that NFS1 is rate-limiting for ALL cellular Fe-S dependent functions
- **Source:** PMID 40797101, Nature Metabolism 2025

### 5. Compound 53 — First Selective NFS1 Small Molecule Inhibitor (Zhu et al. 2025, IJMS)
- **Finding:** Structure-based virtual screening of ChemDiv library against NFS1 (PDB: 5WLW) identifies Compound 53
- **IC50:** 40.5 µM (purified enzyme), 16.3 µM (A549 lung cancer cells)
- **Selectivity:** No inhibition of CBS or CSE (other PLP-dependent enzymes) at 100 µM
- **Source:** DOI 10.3390/ijms26062782, IJMS 2025; full PMC text retrieved

### 6. Sulfur Transfer Dynamics in [2Fe-2S] Assembly on ISCU2 (Nat. Commun. 2024, PMID 38627381)
- **Finding:** High-resolution cryo-EM of persulfide transfer from Cys381-NFS1 → Cys138-ISCU2
- **Key mechanism:** FXN addition optimally positions assembly site residues; FDX2 persulfide reduction completes [2Fe-2S] assembly
- **Significance:** Atomic-level mechanism of the rate-limiting sulfur transfer step
- **Source:** PMID 38627381, Nature Communications 2024

### 7. Frataxin Traps Low-Abundance Quaternary Structure (Biochemistry 2025, PMC 11840927)
- **Finding:** Three distinct quaternary structures for cysteine desulfurase subcomplexes. FXN acts as "molecular lock" shifting equilibrium toward active architecture
- **Source:** PMC 11840927, Biochemistry 2025

---

## NFS1 Mechanism — Core Facts Established

| Parameter | Value | Source |
|-----------|-------|--------|
| Substrate | L-cysteine | Multiple |
| Cofactor | Pyridoxal 5′-phosphate (PLP) | Multiple |
| Active site Cys | Cys381 (flexible loop) | Cryo-EM 2024 |
| Km (L-Cys) | ~2.15 µM (Kdapp, Zangari 2025) or ~50 µM (earlier kinetics) | Zangari 2025; earlier papers |
| Persulfide transfer distance | >20 Å via flexible Cys-loop | Cryo-EM 2024 |
| Core ISC complex | NFS1-ISD11-ACP1 + ISCU2 + FXN + FDX2 | Multiple |
| Redox sensitivity | YES — FDX2 provides electrons via NADPH | Multiple |
| Selectivity window | d-Cys: 12-fold less active than l-Cys | Zangari 2025 |

---

## CISD2 / NAF-1 Biology — Key Facts

| Parameter | Value | Source |
|-----------|-------|--------|
| Localization | ER, MAM, outer mito membrane | Multiple |
| Cluster type | [2Fe-2S] coordinated 3Cys:1His | Karmi 2018 |
| Cluster lability | High — His coordination enables proton-coupled release | Karmi 2018 |
| pH sensitivity | Lower pH → faster cluster loss | Karmi 2018 |
| Function | Ca²⁺ transfer at ER-MAM; longevity regulator | Multiple |
| Longevity | CISD2 knockout mice: shortened lifespan, early aging | Multiple |
| PDB structure | 3FNV | Literature |
| Circadian connection | NONE found directly | This search |

**Important indirect connection identified:** CISD2 is at the ER-MAM junction and regulates Ca²⁺ transfer. ER Ca²⁺ signals regulate circadian clock timing. A 2025 paper confirms: neurons lacking CISD2 show "severely impaired agonist-evoked cytosolic Ca²⁺ signals." A separate paper (Acta Neuropathologica Communications, 2025) links CISD2 to ER-mitochondrial coupling in neurons.

---

## Fe-S Cluster Stability and Redox Sensitivity

### Standard [2Fe-2S] Cluster Properties
- Oxidized state: 2×Fe³⁺ (diferric) — natural state for protein-bound clusters
- Reduced state: Fe²⁺/Fe³⁺ — one electron reduced
- Oxidation by O₂ or ROS → cluster disassembly
- **Exact half-lives under physiological conditions:** Not precisely quantified in current literature

### NEET Protein [2Fe-2S] Properties (pH-Labile)
- pH 6.5-6.8 pKa for proton-coupled electron transfer at coordinating His
- **Lower pH → faster cluster loss** (specific half-life values require original Nechushtai lab papers)
- His→Cys mutation stabilizes cluster (removes lability)

### FDX2 Redox Potential
- **Estimated:** ~-270 mV (from adrenoxin analogy, similar ferredoxin family member)
- **Not directly measured for human FDX2** in papers retrieved
- FDX2 receives electrons from FDXR (ferredoxin reductase) which uses NADPH

### GLRX5 Redox Potential
- **Dithiol glutaredoxins (hGrx1, hGrx2):** -232 and -221 mV
- **GLRX5 is a MONOTHIOL glutaredoxin** — different redox properties
- **Specific measured value for GLRX5 [2Fe-2S] form:** Not found in retrieved literature

---

## IRP1 Aconitase / IRE Switch

### Established Mechanism
- IRP1 exists in two interconvertible forms:
  - **Fe-S loaded form:** Cytoplasmic aconitase (catalytic)
  - **Apo form (no Fe-S):** Binds IRE stem-loops in mRNAs
- Switch is controlled by: iron availability, oxidative stress, NO, phosphorylation
- **Fe-S cluster occupancy is the primary regulatory input**

### Diurnal Regulation (Nadimpalli et al. 2024, Genome Biology — KEY PAPER)
- **IRP1/ACO1 protein: CONSTANT throughout day** (does not oscillate)
- **IRP2: 10-fold amplitude diurnal oscillation** in mouse liver (peak ZT12)
- **Driver: FEEDING RHYTHMS, not intrinsic clock**
- Most strongly regulated targets: Ferritin (Fth1, Ftl1), ALAS2, TFRC
- **CRITICAL GAP: Fe-S cluster occupancy of IRP1 across 24h has NOT been measured**
- If Fe-S biogenesis rate oscillates → IRP1 aconitase/IRE ratio should oscillate even though protein level is constant

---

## Mammalian Fe-S Proteome Scale

- **~70 mammalian proteins** contain Fe-S clusters (comprehensive catalog, 2024)
- ~half localize to nucleus (DNA repair, replication, transcription)
- Key Fe-S dependent processes:
  - **Respiratory chain:** Complex I (~8-9 Fe-S clusters), Complex II (3 clusters), Complex III (1 cluster)
  - **TCA cycle:** Aconitase (ACO2, mitochondrial), aconitase-like ACO1 (IRP1)
  - **DNA repair helicases:** XPD, FANCJ — Fe-S required for activity; rate-limited by MMS19-mediated cluster delivery
  - **Translation:** ABCE1 — essential for ribosome recycling; Fe-S cluster required
  - **Nucleotide synthesis:** DPYD — reduced activity upon MMS19 depletion
  - **tRNA modification:** CDKAL1 (pancreatic β-cells) — Fe-S dependent

### Rate Limitation Evidence
- MMS19 depletion → decreased XPD, FANCJ, DPYD activities
- NFS1 suppression → decreased SDHB, LIAS, CDKAL1, ACO2 (Molenaars 2024, bioRxiv)
- **Conclusion: NFS1 IS rate-limiting for multiple Fe-S dependent processes in vivo**

---

## MagR / IscA1 — Iron-Sulfur Cluster Protein That Binds Cryptochrome

### Discovery and Properties
- **MagR = IscA1** (mitochondrial targeting confirmed; PubMed 2024)
- **Forms rod-like complex with Cryptochrome (CRY)**
- Contains [2Fe-2S] and/or [3Fe-4S] clusters under aerobic conditions
- Has intrinsic magnetic moment: ~0.09-0.1 µB/f.u. in vitro

### Circadian Connection (Zhang et al. 2023, IJMS)
- In migratory insect Nilaparvata lugens:
- **MagR knockdown → significantly downregulated Cry1 expression**
- Cry1/Cry2 double knockdown → MagR upregulation
- Cry1 = "blue-light circadian photoreceptor"; Cry2 = "transcriptional repressor in clockwork"
- MagR expression responds to magnetic field changes as small as several µT

### Significance for Bridge
- IscA1/MagR is a bona fide Fe-S cluster assembly protein that DIRECTLY INTERACTS with CRY
- This interaction MODULATES CRY1 expression in insects
- **NOT studied in mammals** — mammalian MagR is imported into mitochondria (different compartment from cytoplasmic/nuclear CRY)
- Represents a PARTIALLY EXPLORED cross-field connection — but via magnetoreception, not core circadian mechanism

---

## KEGG Pathway Analysis Results

### NFS1 (hsa:9054) — KEGG Pathways
- hsa00730: Thiamine metabolism
- hsa01100: Metabolic pathways
- hsa01240: Biosynthesis of cofactors
- **hsa04122: Sulfur relay system**

### Sulfur Relay System (hsa04122) — Genes Listed
- MOCS3, CTU2, MOCS2, MPST, TST, URM1, CTU1, NFS1
- **ZERO circadian clock genes** in this pathway

### GLRX5 KEGG Query
- Query returned empty (Gene ID 25823 may need alternative notation)

### STRING Network Results (NFS1 + BMAL1 + CLOCK + CRY1 + CRY2 + ISCU2 + GLRX5, human)
- **Fe-S protein interactions:** GLRX5-NFS1: score 0.909 (high confidence)
- **Circadian protein interactions:** CRY1-CRY2, CRY1-CLOCK, CRY1-ARNTL, ARNTL-CLOCK, ARNTL-CRY2, CLOCK-CRY2 — all score 0.999
- **Cross-cluster interactions: ZERO** — no STRING interactions detected between Fe-S biogenesis proteins and circadian clock proteins

---

## Disjointness Verification — Field A × Field C

### Search Results Summary
| Query | Result |
|-------|--------|
| "NFS1 circadian" | 0 relevant papers found |
| "ISCU2 circadian" | 0 relevant papers found |
| "iron sulfur biogenesis rhythm" | 0 mammalian papers; 1 Drosophila paper (2012) |
| "CISD2 circadian clock" | 0 direct papers; indirect Ca²⁺ connection possible |
| "GLRX5 circadian" | 0 papers found |
| "FDX2 circadian" | 0 papers found |
| "MagR IscA1 circadian" | MagR-CRY interaction in insect magnetoreception only |
| "iron sulfur" + CLOCK/BMAL1/CRY/PER | 0 papers directly linking Fe-S biogenesis to core clock proteins in mammals |
| STRING: Fe-S proteins × clock proteins | ZERO interactions |
| KEGG: Sulfur relay pathway | ZERO circadian clock genes |
| Human genome-wide RNAi circadian screen (2009) | Fe-S biogenesis genes NOT among hits |

### Existing Cross-Field Work
1. **Mandilaras & Missirlis 2012 (Metallomics):** Drosophila RNAi — IscS, IscU, IscA1 affect circadian period. MECHANISM UNKNOWN.
2. **Marelja, Leimkühler, Missirlis 2018 (Frontiers in Physiology):** Drosophila — NFS1/IscS RNAi in clock neurons causes arrhythmia. MECHANISM UNKNOWN.
3. **Zhang et al. 2023 (IJMS):** MagR (=IscA1)/Cryptochrome interaction in migratory insect. Via magnetoreception, not core clock.

These 3 papers are the ONLY published cross-field connections. All are Drosophila/insect. None proposes mechanism. None has mammalian follow-up as of March 2026.

---

## Disjointness Assessment

**Status: DISJOINT (confirmed)**

**Evidence:**
- STRING network: zero interactions between Fe-S biogenesis proteins and mammalian circadian clock proteins
- KEGG pathway analysis: zero shared pathways between core Fe-S biogenesis (sulfur relay, hsa04122) and circadian clock pathways
- 3 cross-field papers exist, ALL in Drosophila/insects, ALL lacking mechanism, NONE followed up in mammals
- Human genome-wide RNAi circadian screen (2009): Fe-S biogenesis genes not among thousands of hits
- Search terms "NFS1 circadian," "ISCU2 circadian," "GLRX5 circadian," "FDX2 circadian" all return ZERO results

**Implication:** The mammalian mechanism is genuinely unexplored. The Drosophila functional evidence (Fe-S biogenesis genes ARE required for circadian function) combined with the complete absence of mechanistic work creates a high-novelty opportunity.

---

## Indirect Connection Nodes Identified

The following INDIRECT connections were identified — none appear in any published hypothesis:

### Node 1: NADPH → FDX2 → Fe-S synthesis rate
- NADPH/NADP+ ratio oscillates circadianly (BMAL1-NAMPT-NAD⁺ axis)
- FDX2 depends on NADPH (via FDXR) for reduction
- Therefore: circadian NADPH oscillation → FDX2 electron availability → Fe-S synthesis rate
- **Not yet proposed in any paper**

### Node 2: Fe-S biogenesis → IRP1 Fe-S occupancy → iron homeostasis timing
- IRP2 oscillates 10-fold with feeding (Nadimpalli 2024)
- IRP1 protein is constant but its Fe-S OCCUPANCY is unmeasured
- If NFS1/ISCU2 activity oscillates → IRP1 aconitase/IRE ratio would oscillate
- **Gap: IRP1 Fe-S occupancy across 24h has never been measured**

### Node 3: Mitochondrial redox (GSH/GSSG) → GLRX5 cluster transfer → Fe-S delivery rate
- Mitochondrial GSH/GSSG oscillates circadianly
- GLRX5 cluster transfer is GSH-dependent
- Therefore: circadian redox oscillations could directly modulate GLRX5 hub function
- **Not yet proposed in any paper**

### Node 4: CISD2 cluster lability → ER-MAM Ca²⁺ transfer → circadian Ca²⁺ signaling
- CISD2 regulates ER-mito Ca²⁺ transfer at MAM
- Ca²⁺ signals regulate circadian clock timing (circadian Ca²⁺ oscillations documented)
- CISD2 cluster lability is pH/redox-dependent
- **Indirect connection: CISD2 may be a redox sensor for circadian Ca²⁺ gating**

### Node 5: Complex I Fe-S clusters → BMAL1/CLOCK directly regulate Complex I subunits
- 2026 Nature Metabolism paper: BMAL1/CLOCK modulate expression of Complex I subunits
- Complex I contains 8-9 Fe-S clusters
- Therefore: clock-regulated Complex I assembly → demand for Fe-S clusters oscillates
- **No paper addresses whether cluster demand drives upstream Fe-S biogenesis oscillation**

---

## Key Anomalies and Open Questions

1. **The Drosophila-mammal gap:** IscS/NFS1 RNAi causes arrhythmia in flies — but NO mammalian paper has tested whether NFS1 conditional knockout/knockdown affects mammalian circadian period or amplitude. This is the most obvious experiment not done.

2. **IRP1 Fe-S occupancy is unmeasured across 24h:** Given that IRP2 oscillates 10-fold and IRP1 aconitase activity controls iron homeostasis, the failure to measure IRP1 Fe-S occupancy over 24h is a significant omission in circadian iron biology.

3. **NADPH oscillation → FDX2 electron availability:** NADPH is known to oscillate circadianly (NAMPT/SIRT pathway). FDX2 depends on NADPH. No paper has measured FDX2 reduction state over 24h.

4. **Circadian Complex I regulation is INDEPENDENT of whether Fe-S cluster supply is the limiting factor:** The 2026 Nature Metabolism paper shows BMAL1 controls Complex I subunit expression, but whether Fe-S cluster availability (vs. protein expression) is the rate-limiting step for Complex I assembly over 24h is unknown.

5. **CISD2 cluster turnover rate:** The 3Cys:1His cluster of NEET proteins has pH-dependent lability, but no paper has measured CISD2 cluster occupancy over 24h, despite CISD2's established role in Ca²⁺ homeostasis that is itself circadianly regulated.

---

## Contradictions Found

1. **NFS1 Km for L-cysteine:** Zangari 2025 reports Kdapp = 2.15 µM; earlier kinetic studies cite ~50 µM. These may represent different conditions (Kdapp vs. Km; different complex compositions). Not strictly contradictory but numerically discrepant.

2. **Ferredoxin redox potential:** Adrenoxin (FDX1) = -274 mV; FDX2 exact value not measured but assumed similar. FDX1 and FDX2 have different functions (steroidogenesis vs. Fe-S biogenesis) — their redox potentials may differ significantly. Not contradictory but uncertain.

---

## Full-Text Papers Retrieved

| Paper | File | Why Selected |
|-------|------|--------------|
| Mandilaras 2012, Metallomics | results/papers/mandilaras2012-iron-sulfur-genes-circadian-drosophila.md | PRIMARY cross-field paper; Drosophila Fe-S × circadian |
| Zangari 2025, Nature Metab | results/papers/zangari2025-d-cysteine-NFS1-inhibitor-cancer.md | NFS1 pharmacological inhibition; rate-limiting proof |
| Steinhilper 2024, Nat Commun | results/papers/steinhilper2024-fdx2-two-stage-binding-ISC.md | FDX2 structural mechanism; redox regulation node |
| Pandey 2025, JBC | results/papers/pandey2025-GLRX5-central-hub-FeS-assembly.md | GLRX5 central hub; GSH-dependent redox control |
| Nadimpalli 2024, Genome Biol | results/papers/nadimpalli2024-IRP-diurnal-feeding-iron-homeostasis.md | IRP1/IRP2 diurnal oscillation; key bridge paper |
| Molenaars 2024, bioRxiv | results/papers/molenaars2024-NFS1-inhibition-metabolic-flexibility-mice.md | In vivo proof NFS1 rate-limiting for metabolic Fe-S enzymes |
| Lill 2025, Nature | results/papers/lill2025-cross-regulation-FDX2-frataxin-nature.md | FDX2:FXN ratio controls synthesis; NADPH-linked mechanism |
| Marelja 2018, Front Physiol | results/papers/marelja2018-iron-sulfur-drosophila-life-cycle.md | SECOND cross-field paper; NFS1/IscS RNAi → arrhythmia |
| Karmi 2018, JBIC | results/papers/karmi2018-NEET-cluster-lability-health-disease.md | CISD2 cluster lability; Ca²⁺-circadian indirect bridge |
| Zhu 2025, IJMS | results/papers/zhu2025-NFS1-inhibitor-compound53-lung-cancer.md | Compound 53; NFS1 first small-molecule inhibitor |

---

## Gap Analysis

### What Has Been Explored
- Fe-S biogenesis machinery (NFS1, ISCU2, FDX2, FXN, GLRX5) structural mechanisms — WELL studied (multiple Nature/Nat Commun papers 2024-2025)
- Fe-S cluster stability chemistry and NEET protein lability — WELL studied
- IRP1/IRP2 iron regulatory mechanisms and their diurnal oscillation patterns — STUDIED (Nadimpalli 2024)
- Circadian regulation of mitochondrial OXPHOS / Complex I activity — PARTIALLY studied (clock-dependent acetylation mechanism; 2026 BMAL1-Complex I paper)
- Drosophila Fe-S × circadian connection at behavioral level — STUDIED but mechanism unknown
- MagR/IscA1-Cryptochrome physical interaction — STUDIED in insects; not in mammals

### What Has NOT Been Explored
1. **Whether any mammalian Fe-S biogenesis gene (NFS1, ISCU2, GLRX5, FDX2, FXN) shows circadian oscillation in expression or activity** — NOT measured
2. **Whether IRP1's Fe-S cluster occupancy varies over 24h in any organism** — UNMEASURED (Nadimpalli 2024 explicitly notes this as a major challenge)
3. **Whether NADPH oscillations (circadian NAMPT/SIRT axis) modulate FDX2 reduction state and Fe-S synthesis rate** — NOT proposed
4. **Whether circadian redox state (GSH/GSSG) in mitochondria regulates GLRX5 cluster transfer rate** — NOT proposed
5. **Whether CISD2 cluster lability varies with circadian phase due to pH/redox oscillations in the ER/MAM** — NOT proposed
6. **Whether circadian demand for Fe-S clusters (via clock-controlled Complex I subunit expression) creates a feedback signal to upstream biogenesis (NFS1/ISCU2) rate** — NOT proposed
7. **The mammalian mechanism linking Fe-S biogenesis to circadian clock period/amplitude** — entirely unknown despite Drosophila evidence from 2012 and 2018
8. **Whether conditional knockout of NFS1 in SCN neurons affects circadian period in mice** — NOT done

### Most Promising Unexplored Directions

**Direction 1 [HIGHEST NOVELTY, HIGHEST TRACTABILITY]:** NADPH oscillation → FDX2 → Fe-S synthesis rate oscillation
- Specific mechanism: CLOCK→NAMPT→NAD⁺/NADPH→FDXR→FDX2 (distal→proximal transition)→persulfide reduction→[2Fe-2S] assembly rate
- Testable: Measure FDX2 reduction state (EPR spectroscopy) and Fe-S assembly rate across 24h in synchronized cells
- Prior art: NADPH oscillation established; FDX2 mechanism established; connection is MISSING

**Direction 2 [MEDIUM NOVELTY, STRONG MECHANISM]:** Fe-S biogenesis rate → IRP1 aconitase/IRE switch → circadian iron homeostasis
- Specific mechanism: Oscillating Fe-S biogenesis → oscillating IRP1 Fe-S occupancy → oscillating aconitase/IRE ratio → circadian modulation of ferritin, TFRC, ALAS2
- Would explain the Nadimpalli 2024 IRP2 oscillation: if Fe-S biogenesis oscillates, IRP1 activity oscillates, and IRP2 expression follows iron-mediated feedback
- Testable: Measure IRP1 aconitase activity vs. IRE-binding activity across 24h in mouse liver

**Direction 3 [HIGH NOVELTY, INDIRECT]:** CISD2 cluster lability as circadian redox sensor
- Specific mechanism: Circadian oscillations in ER/MAM redox state → CISD2 cluster loss → altered ER-MAM Ca²⁺ transfer → circadian Ca²⁺ signaling perturbation
- Would connect Fe-S chemistry to the well-established circadian Ca²⁺ oscillation literature
- Testable: CISD2 cluster occupancy (Mössbauer/EPR) across 24h; Ca²⁺ imaging in CISD2 KO cells under circadian synchronization

**Direction 4 [SPECULATIVE, HIGH IMPACT IF TRUE]:** NFS1 as circadian pacemaker component in SCN neurons
- Based on Drosophila: IscS/NFS1 RNAi → arrhythmia in clock neurons
- Mammalian experiment: SCN-specific NFS1 conditional KO (e.g., VIP-Cre × NFS1-flox) → wheel-running activity monitoring
- No mechanistic prediction, but would be transformative if true
- Testable with existing mouse genetic tools

---

*Report generated: 2026-03-21*
*Search method: WebSearch + WebFetch (MCP unavailable)*
*Papers retrieved and saved: 10 files in results/papers/*
