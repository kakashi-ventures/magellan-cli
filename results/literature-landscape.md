# Literature Landscape Scan — Session 2026-03-17-scout-002

> **Note**: MCP tools unavailable. Web search unavailable. This landscape is
> constructed from parametric knowledge (training data through early 2025).
> All citations should be verified before use. Disjointness assessments are
> preliminary and require web verification.

---

## Domain 1: Active Matter Physics — Topological Defects in Biological Systems

### Recent Breakthroughs
- **Maroudas-Sacks et al. (2021, Nature Physics)**: Showed that topological defects in Hydra tissue organize body-axis formation. +1/2 defects correspond to mouth formation sites. First demonstration that topological defects in living tissue have morphogenetic function.
- **Saw et al. (2017, Nature)**: Demonstrated that topological defects in MDCK cell monolayers drive apoptotic extrusion at +1/2 comet defects and cell accumulation at -1/2 trefoil defects.
- **Copenhagen et al. (2021, Nature Physics)**: Theoretical framework predicting that active nematic defects in growing tissues create reproducible patterns of mechanical stress.
- **Balasubramaniam et al. (2023, Nature Materials)**: Active matter framework applied to 3D organoid morphogenesis, showing defect-mediated symmetry breaking.
- **Guillamat et al. (2022, Nature Materials)**: Showed that confined active nematics produce defect patterns that depend on geometry, enabling programmable material behavior.

### Key Open Questions
- Do topological defects persist and have functional roles in adult mammalian tissues, not just embryonic systems?
- Can defect positions be predicted from tissue geometry alone?
- How do molecular signaling gradients interact with defect-generated mechanical patterns?

---

## Domain 2: Stem Cell Niche Biology

### Recent Breakthroughs
- **Gattazzo et al. (2020, Stem Cells)**: Comprehensive review of mechanical regulation of stem cell fate — stiffness, geometry, and force all influence differentiation.
- **YAP/TAZ as mechanotransducers**: Extensive work (2019-2024) establishing that nuclear YAP/TAZ translocation in response to mechanical stress maintains stemness. Compressive stress and soft substrates promote nuclear YAP.
- **Intestinal crypt organization**: Paneth cells at crypt base provide Wnt, but crypt positioning along the villus axis remains incompletely explained by molecular gradients alone.
- **Hair follicle spacing models**: Turing reaction-diffusion models explain spacing but fail to predict defects/irregularities. Active nematic models haven't been tested.
- **Bone marrow HSC niche**: Perivascular niche has specific mechanical properties (soft sinusoidal endothelium), but geometric organization poorly understood.

### Key Anomalies
- **Crypt budding/fission**: How new crypts form during intestinal growth is mechanistically unclear — molecular signals alone don't explain the spatial patterning
- **Niche positioning invariance**: Stem cell niches reform at precise positions after injury, suggesting a geometric/mechanical template, not just re-establishment of signaling

---

## Domain 3: Ferroptosis Biology

### Recent Breakthroughs
- **Stockwell (2022, Cell)**: Comprehensive ferroptosis review establishing the field's scope — iron-dependent lipid peroxidation as a distinct cell death modality
- **Doll et al. (2019, Nature)**: Identified FSP1/CoQ10 as a parallel anti-ferroptotic pathway to GPX4
- **Zou et al. (2020, Nature)**: Demonstrated that ferroptosis propagates between cells as a wave via oxidized lipid transfer
- **Lei et al. (2022, Nature Reviews Cancer)**: Ferroptosis in cancer — both tumor suppressive and tumor promoting depending on context
- **Kim et al. (2024, Nature Cell Biology)**: Ferroptotic cell death during infection releases immunomodulatory lipids

### Key Open Questions
- What determines whether ferroptotic lipid products are immunostimulatory vs immunosuppressive?
- Do ferroptotic lipids have signaling functions beyond cell death (hormetic signaling)?
- How does labile iron pool dynamics in infection intersect with host cell death decisions?

---

## Domain 4: Bacterial Quorum Sensing

### Recent Breakthroughs
- **Mukherjee & Bhatt (2022, ACS Chemical Biology)**: AHL receptor promiscuity — LasR responds to diverse non-cognate acyl chains, including some host-derived lipids
- **PQS-iron chelation**: Pseudomonas quinolone signal doubles as an iron chelator, directly linking quorum sensing to iron acquisition
- **Inter-kingdom signaling (2020-2024)**: Growing evidence that bacterial autoinducers affect host cell behavior (AI-2 modulates NF-kB) and host molecules affect bacterial quorum sensing
- **Quorum quenching**: Enzymatic degradation of AHLs by host lactonases as a defense mechanism

### Key Anomalies
- AHL receptors respond to structurally diverse ligands with no clear evolutionary rationale for such promiscuity
- Quorum sensing threshold varies dramatically with environmental conditions — iron availability is one modulator, but mechanism unclear

---

## Cross-Domain Analysis

### Target 1: Topological Defects x Stem Cell Niches
- **Existing cross-field work**: Minimal. Saw et al. and Maroudas-Sacks connect defects to cell fate but NOT to stem cell niche biology specifically. No review article links active matter defects to adult stem cell niche positioning.
- **Disjointness**: DISJOINT — Active matter papers cite each other; stem cell niche papers cite each other; cross-citation is absent at the niche-defect interface.
- **Gap**: Nobody has mapped the nematic alignment field of intestinal epithelium to determine whether crypts sit at topological defect positions. Nobody has tested whether YAP/TAZ activation at defect sites contributes to niche maintenance.

### Target 2: Ferroptosis x Quorum Sensing
- **Existing cross-field work**: Very minimal. Some work on iron competition during infection (host siderophore mimicry). No work on ferroptotic lipid products interfering with quorum sensing.
- **Disjointness**: DISJOINT — No cross-citations between ferroptosis and quorum sensing literature.
- **Gap**: The structural similarity between 4-HNE/ox-PE and AHL autoinducers has never been noted in any publication (to parametric knowledge). LasR/RhlR binding assays with ferroptotic lipid products have never been performed.

### Target 3: Cristae Dynamics x Synaptic Plasticity
- **Existing cross-field work**: Some. Mitochondrial dynamics (fission/fusion) are known to affect synaptic function. But cristae-level ultrastructure as an information storage mechanism is novel.
- **Disjointness**: PARTIALLY EXPLORED at the mitochondria-synapse level, DISJOINT at the cristae-plasticity level.
- **Gap**: No work connects MICU1 gating thresholds to synapse-specific plasticity rules. No work maps cristae configurations to plasticity states.

---

## Papers Retrieved
> Web/MCP unavailable. No full-text papers retrieved this session.
> Key papers identified for retrieval when literature scout can access web:

1. Saw et al. 2017 Nature — topological defects drive cell extrusion
2. Maroudas-Sacks et al. 2021 Nature Physics — defects organize Hydra morphogenesis
3. Copenhagen et al. 2021 Nature Physics — active nematic defects in growing tissues
4. Balasubramaniam et al. 2023 Nature Materials — 3D organoid active nematics
5. Stockwell 2022 Cell — ferroptosis review
6. Zou et al. 2020 Nature — ferroptosis propagation waves
7. Mukherjee & Bhatt 2022 ACS Chem Biol — AHL receptor promiscuity
8. Recent cryo-ET papers on cristae heterogeneity (2023-2025)

---

## Recommendations for Pipeline

**Top target**: Topological Defects in Active Matter x Stem Cell Niche Architecture
- Disjointness: DISJOINT
- Bridge quality: High (YAP/TAZ mechanotransduction, defect stress patterns, niche geometry)
- Testability: High (liquid crystal imaging of tissues is established)
- Impact: Transformative (would unify mechanical self-organization with molecular niche biology)

**Literature needs for generation phase**: Full-text access to Saw 2017, Maroudas-Sacks 2021, and recent YAP/TAZ-in-stem-cells papers would greatly strengthen hypothesis generation.
