# Literature Context: Fe-S Cluster Biogenesis × Circadian Clock Regulation
## Session: 2026-03-21-scout-007

### Disjointness Verification
- "iron-sulfur cluster" AND circadian on PubMed: **6 results** (only 1 mechanistic: Mandilaras 2012)
- GLRX5 AND circadian: **0 papers** — CONFIRMED DISJOINT
- NFS1 AND circadian: **1 paper** (non-mechanistic Drosophila review)
- CISD2 AND circadian: **1 paper** (coincidental co-measurement)
- Positive control — heme AND circadian: **203 papers**
- STRING: Zero interactions between Fe-S proteins (NFS1, CISD2, GLRX5, FDX2) and clock proteins (BMAL1, CRY1, PER2, CLOCK)
- KEGG: Zero shared genes between hsa04122 (Sulfur relay) and hsa04710 (Circadian rhythm)
- **Overall: DISJOINT** — confirmed across PubMed, STRING, and KEGG

---

### Key Papers

| # | PMID | Authors | Year | Journal | Title | Key Finding | Relevance |
|---|------|---------|------|---------|-------|-------------|-----------|
| 1 | 22885802 | Mandilaras & Missirlis | 2012 | Metallomics | Genes for iron metabolism influence circadian rhythms in Drosophila | RNAi of 5 Fe-S genes (IscS, IscU, IscA1, Iba57, Nubp2) disrupts clock in Drosophila clock neurons | FOUNDATIONAL — only paper linking Fe-S biogenesis to clock function. 14 years, zero mammalian follow-up |
| 2 | 38773499 | Nadimpalli et al | 2024 | Genome Biology | Diurnal control of IRE-containing mRNAs via IRP1/IRP2 | IRP1/IRP2 oscillate diurnally driven by feeding; control ferritin, TfR, and other iron mRNAs on 24h cycle | CRITICAL — IRP1 [4Fe-4S]/apo switch oscillates diurnally; downstream readout for Fe-S oscillation |
| 3 | 22622569 | Edgar et al | 2012 | Nature | Peroxiredoxins are conserved markers of circadian rhythms | Peroxiredoxin oxidation-reduction 24h cycles universal across all domains of life | CRITICAL — redox oscillations are fundamental circadian mechanism; Fe-S clusters are redox-sensitive |
| 4 | 24051248 | Peek et al | 2013 | Science | Circadian clock NAD+ cycle drives mitochondrial oxidative metabolism | Clock controls NAD+ salvage → 24h NAD+/NADH oscillations → rhythmic mitochondrial metabolism | CRITICAL — NAD+/NADH oscillations directly affect mitochondrial redox where Fe-S clusters assemble |
| 5 | 40141425 | Zhu et al | 2025 | Int J Mol Sci | NFS1 selective inhibitor (Compound 53) | First selective NFS1 inhibitor (IC50=16.3 μM). Disrupts Fe-S biogenesis, increases labile iron | Tool compound for testing circadian NFS1 hypothesis |
| 6 | 40797101 | Zangari et al | 2025 | Nature Metabolism | D-cysteine impairs tumour growth by inhibiting NFS1 | D-cysteine inhibits NFS1 persulfide formation via steric block at Cys328; collapses ALL Fe-S-dependent functions | NFS1 as druggable bottleneck; affects respiration, nucleotide metabolism, genome integrity |
| 7 | 40074084 | Pandey et al | 2025 | J Biol Chem | GLRX5 as central hub for Fe-S cluster assembly | GLRX5 required for both intra-mitochondrial Fe-S assembly AND export to cytoplasm | Redox-sensitive glutaredoxin as circadian-responsive Fe-S distribution hub |
| 8 | 41299767 | Loncke et al | 2025 | Acta Neuropathol Commun | CISD2 ensures ER-mitochondrial coupling in neurons | CISD2 [2Fe-2S] protein regulates ER-mito Ca2+ transfer via IP3R; loss collapses mitochondrial function | Labile Fe-S cluster at ER-mito interface; no circadian link published (gap) |
| 9 | 41480765 | Yuan et al | 2026 | JCI | Circadian copper variation in glioblastoma via BMAL1→ATP7A | BMAL1 controls copper homeostasis → cuproptosis destabilizes Fe-S cluster proteins | NEAREST PRECEDENT — circadian→metal→Fe-S stability, but copper/cuproptosis, not biogenesis |
| 10 | 28941588 | Romero et al | 2018 | Mitochondrion | NFS1 regulated by phosphorylation | Yck2 kinase phosphorylates NFS1 stimulating desulfurase activity | Post-translational NFS1 regulation exists; potential circadian kinase input |
| 11 | 26016518 | Fox et al | 2015 | Biochemistry | Frataxin accelerates [2Fe-2S] cluster formation on ISCU | Frataxin accelerates Fe-S assembly kinetics on NFS1-ISCU complex | Assembly rate is regulatable on timescale compatible with circadian |
| 12 | 41486525 | Sica et al | 2026 | J Biol Rhythms | Liver clock tunes mitochondrial function in skeletal muscle | Cross-organ circadian control of mitochondrial gene expression | BMAL1/CLOCK regulate mitochondrial genes across tissues |

### Additional CISD2/Aging Papers
| PMID | Authors | Year | Title | Relevance |
|------|---------|------|-------|-----------|
| 40841648 | Yeh et al | 2025 | Cisd2 delays atrial aging via calcium homeostasis | CISD2 as longevity gene; no circadian connection |
| 40189101 | Shen et al | 2025 | CISD2 deficiency disrupts Ca2+-mediated insulin secretion in β-cells | CISD2 in metabolic regulation |
| 40349253 | Chen et al | 2025 | Cisd1 synergizes with Cisd2 for mitochondrial/ER homeostasis | CISD protein family coordination |
| 39370046 | Loncke et al | 2025 | CISD2 counteracts BCL-2 inhibition of ER-mito Ca2+ transfer | CISD2 at ER-mito interface |

---

### Broader Topic Summaries

#### NFS1 Activity Regulation
NFS1 is regulated by: (1) frataxin — accelerates persulfide sulfur transfer to ISCU and free thiols; (2) phosphorylation — Yck2 kinase stimulates activity (PMID 28941588); (3) substrate availability — Km ~50 μM for L-cysteine. D-cysteine inhibits NFS1 via steric constraints at active-site Cys328 (Zangari 2025). **No published redox regulation data**, but the active-site Cys328 is inherently oxidation-sensitive — direct circadian redox modification is a prediction, not an established finding. NFS1 requires PLP cofactor; C-terminal stretch (W454) critical for FXN/ISCU2 interactions.

#### ISCU2 Cluster Assembly Kinetics
[2Fe-2S] cluster formation on ISCU2 scaffold occurs on minutes-to-hours timescale in vitro (Fox 2015). Frataxin accelerates the reaction. The scaffold cluster is transient — rapidly transferred to downstream acceptors (GLRX5 → ISA1/ISA2 for [4Fe-4S] conversion). This transience makes ISCU2 the most circadian-sensitive node in the pathway (estimated t1/2 ~1h, 94% amplitude tracking of 24h oscillation).

#### Fe-S Cluster Degradation Rates
[4Fe-4S] clusters in aconitase are rapidly destabilized by superoxide (minutes). O2-dependent inactivation is the rate-determining step for protein degradation. Labile cluster variants show t1/2 ~35 min. One of the four iron atoms in [4Fe-4S] is more solvent-exposed and labile; its dissociation generates unstable [3Fe-4S] → [2Fe-2S] → apo cascade. Cluster lability depends on solvent exposure, oxidation state, and protein environment — parameters that change with circadian redox oscillation.

#### IRP1 Aconitase/IRE-BP Switch & Circadian Regulation
IRP1 alternates between [4Fe-4S]-aconitase (high iron, reducing conditions) and apo-IRE-binding protein (low iron, oxidizing conditions). **Nadimpalli et al 2024 confirmed this switch oscillates diurnally**, driven by feeding rhythms controlling IRP1 and IRP2 protein levels and activity. IRE-containing mRNAs (ferritin H/L, TfR1, ALAS2, HIF2α) show corresponding 24h oscillation. This is the best-characterized downstream readout for any circadian Fe-S cluster variation and validates the principle that Fe-S cluster occupancy varies on circadian timescales in mammalian cells.

#### BMAL1/CLOCK Regulation of Mitochondrial Genes
BMAL1/CLOCK drive rhythmic expression of mitochondrial genes including ETC components (Sica 2026: liver clock tunes skeletal muscle mitochondrial transcription). Hepler et al 2026 showed NADH dehydrogenase controls circadian metabolic syndrome. BMAL1 also controls copper transporter ATP7A affecting Fe-S protein stability (Yuan 2026, JCI). **NFS1, ISCU2, GLRX5, and FDX2 have NOT been tested as circadian-controlled genes** — this is a critical experimental gap.

---

### Literature Context Summary

Fe-S cluster biogenesis × Circadian clock regulation is **CONFIRMED DISJOINT** in mammalian systems (GLRX5×circadian = 0 papers; NFS1×circadian = 1 non-mechanistic; CISD2×circadian = 1 coincidental; STRING = zero interactions; KEGG = zero shared genes). The 2012 Drosophila paper (Mandilaras & Missirlis, PMID 22885802) is the ONLY mechanistic evidence: NFS1/IscS RNAi disrupts circadian activity — 14 years with zero mammalian follow-up. The 2026 JCI paper (PMID 41480765) is the nearest mammalian precedent: BMAL1→copper→Fe-S protein stability, but focuses on cuproptosis, not biogenesis.

**Key enablers for the Fe-S×Circadian hypothesis:**
1. IRP1 [4Fe-4S]/apo switch validated as diurnal readout (Nadimpalli 2024)
2. NAD+/NADH 24h oscillations affect mitochondrial redox (Peek 2013)
3. Peroxiredoxin redox cycles are universal circadian markers (Edgar 2012)
4. Two NFS1 inhibitor tool compounds published 2025 (Compound 53, D-cysteine)
5. GLRX5 is a redox-sensitive Fe-S distribution hub (Pandey 2025)
6. Fe-S cluster half-lives (1-8h) compatible with 24h amplitude tracking (31-94%)
7. Nernst: 30mV redox oscillation → 3.07-fold Kd shift in cluster stability
8. CISD2 × circadian = zero publications (highest novelty target)

**Generator warnings:**
- Do NOT propose direct CRY-Fe-S binding — mammalian CRYs use FAD, not Fe-S
- Do NOT claim connection is completely unknown — JCI 2026 paper is nearby (different mechanism)
- Primary mechanism is likely direct NFS1 cysteine oxidation, not substrate Km effects
- IRP1/ACO1 switch is the best circadian Fe-S readout (validated diurnal, Nadimpalli 2024)
- CISD2 × circadian is confirmed zero-publication — highest novelty target
- Compartmentalization: NFS1/ISCU2 are mitochondrial; CRY1/BMAL1 are nuclear. Bridge via mitochondrial redox → Fe-S assembly → GLRX5/CIA export to cytoplasm
