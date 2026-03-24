# Literature Landscape — Session 012
## Disjointness Verification for 6 Scout Candidates
Generated: 2026-03-24

---

## T1: Manganese Speciation Toxicology x Deinococcus Mn-Antioxidant Defense
**Disjointness: DISJOINT**
- PubMed cross-search "manganese neurotoxicity Deinococcus": **0 results**
- PubMed "Daly Deinococcus manganese neuroprotection": **0 results**
- PubMed "manganese complex neuroprotection antioxidant": **5 results** — but these are synthetic Mn-salen complexes (catalase mimetics), NOT Deinococcus-derived Mn-OP complexes. Different mechanism entirely.
- The DP1 decapeptide and Mn-OP non-enzymatic ROS scavenging from Daly lab has never been tested in any neurodegenerative context.
- Bridge validation: DP1 peptide IS characterized (Daly et al.), SLC30A10 mutations DO cause manganism — both bridges are factually correct.
- **Assessment**: STRONGLY DISJOINT. Zero cross-field papers. Two completely separate research communities.

---

## T2: Polymer Brush Physics x Glycocalyx-Mediated Mechanotransduction
**Disjointness: PARTIALLY_EXPLORED**
- PubMed "glycocalyx polymer brush": **11 results** spanning 2011-2025
- Key papers:
  - "Physical Principles of Membrane Shape Regulation by the Glycocalyx" (2019) — explicitly models glycocalyx as polymer brush
  - "Red blood cell dynamics in polymer brush-coated microcapillaries: A model of endothelial glycocalyx in vitro" (2018) — uses polymer brush as glycocalyx model
  - "Simulation and modelling of slip flow over surfaces grafted with polymer brushes and glycocalyx fibres" (2013)
  - Weinbaum et al. 2003 PNAS — mechanotransduction model explicitly using glycocalyx as polymer brush layer
- The polymer brush analogy for glycocalyx is an ESTABLISHED concept in biophysics. Multiple groups have used Alexander-de Gennes scaling for glycocalyx modeling.
- **Assessment**: PARTIALLY_EXPLORED to WELL_EXPLORED. The specific scaling law application exists. The Bridge is NOT novel.

---

## T3: Classical Nucleation Theory x Ferroptosis Iron Pool Dynamics
**Disjointness: DISJOINT**
- PubMed "classical nucleation theory ferroptosis": **0 results**
- PubMed "ferritin nucleation ferrihydrite kinetics": **3 results** — these study ferrihydrite core formation in ferritin BUT:
  - "Observation of the Assembly of the Nascent Mineral Core at the Nucleation Site of Human Mitochondrial Ferritin" (2025) — cryo-EM structural study, no CNT formalism
  - "Reconstitution of manganese oxide cores in horse spleen and recombinant ferritins" (1993) — experimental, no nucleation theory
  - "Influence of site-directed modifications on the formation of iron cores in ferritin" (1991) — biochemical study, no CNT
- NO paper applies CNT free energy barrier formalism (DeltaG*, supersaturation S, critical nucleus r*) to ferritin-encaged ferrihydrite nucleation
- NO paper connects ferrihydrite nucleation kinetics to ferroptosis LIP dynamics
- Bridge validation: CNT formalism IS applicable to nanoconfined crystallization. Ferrihydrite IS the mineral form in ferritin. LIP overflow IS a ferroptosis trigger. All bridges factually correct.
- **Assessment**: STRONGLY DISJOINT. Materials science CNT and ferroptosis cell biology have zero cross-citations. Even ferritin mineralization studies lack CNT formalism.

---

## T4: Topological Insulator Surface States x Bacterial Biofilm Electrical Signaling
**Disjointness: DISJOINT**
- PubMed "topological insulator biofilm electrical signaling": **0 results**
- No papers apply topological band theory concepts to biofilm signaling of any kind.
- Bridge validation: Biofilm K+ signaling IS established (Prindle et al. 2015 Nature). Topological protection IS a real phenomenon. However, the mathematical mapping between quantum topological protection and classical ion diffusion is WEAK — topological protection in physics requires quantum coherence (Hamiltonian with specific symmetries), which has no classical analogue in biofilm ion channels.
- **Assessment**: DISJOINT but BRIDGE FACTUALLY QUESTIONABLE. The analogy may be phenomenological (looks similar) rather than structural (same mathematics). Topological protection in condensed matter requires time-reversal symmetry or particle-hole symmetry — concepts with no biofilm analogue.

---

## T5: Reaction-Diffusion Morphogenesis x Tumor Mutational Burden Spatial Heterogeneity
**Disjointness: PARTIALLY_EXPLORED**
- PubMed "Turing instability cancer": **4 results**
  - "Bidirectional Endothelial Feedback Drives Turing-Vascular Patterning and Drug-Resistance Niches" (2025) — DIRECTLY applies Turing instability analysis to tumor vascular patterning, including spatial wavelength predictions
  - "Spatiotemporal pattern formation and selection induced by cross-diffusion in a cancer growth model" (2024)
  - Two older theoretical papers on reaction-diffusion in tumor context (2016, 2009)
- PubMed "Turing pattern tumor immune": **7 results** — broader related work
- The specific idea of Turing instability in tumor spatial patterning EXISTS in recent literature (2025 paper is directly relevant)
- However: the 2025 paper focuses on Turing-VASCULAR patterning, not Turing-MUTATIONAL BURDEN patterning. The connection to mutational heterogeneity and immunotherapy response prediction is NOVEL.
- **Assessment**: PARTIALLY_EXPLORED. Core concept (Turing in tumor biology) exists. Specific application to mutational burden spatial heterogeneity is new, but field is actively developing.

---

## T6: Granular Jamming Physics x Chromatin Compaction Phase Transitions
**Disjointness: DISJOINT**
- PubMed "granular jamming chromatin compaction": **0 results**
- PubMed "jamming chromatin": **2 results**
  - "Replication-guided nucleosome packing and nucleosome breathing expedite the formation of dense arrays" (2014) — uses "packing" but NOT jamming physics formalism
  - One other tangential result
- PubMed "chromatin jamming nucleus packing": **1 result** — same paper
- The jamming transition phase diagram (Liu-Nagel), Edwards entropy, dilatancy, and Gardner transition have NOT been applied to chromatin in any paper.
- Polymer physics (worm-like chain, loop extrusion) dominates chromatin modeling — jamming physics is an entirely different framework.
- Bridge validation: Nucleosome packing fractions ARE calculable from known dimensions. Jamming transition IS a real physical phenomenon at phi_c ~ 0.64 for spheres. The dimensional analysis connecting nucleosome sizes to packing fraction is factually sound.
- **Assessment**: STRONGLY DISJOINT. Soft matter jamming physics and chromatin biology have essentially zero cross-citations.

---

## Summary Table

| Target | PubMed Cross-Field | Disjointness | Bridge Valid? | Notes |
|---|---|---|---|---|
| T1: Mn speciation x Deinococcus | 0 | DISJOINT | YES | Strongest disjointness. Priority deferred target. |
| T2: Polymer brush x Glycocalyx | 11 | PARTIALLY_EXPLORED | YES (but known) | Bridge is established in biophysics literature |
| T3: CNT x Ferroptosis LIP | 0 | DISJOINT | YES | CNT formalism never applied to ferritin nucleation or ferroptosis |
| T4: Topological insulator x Biofilm | 0 | DISJOINT | QUESTIONABLE | Phenomenological analogy, not structural isomorphism |
| T5: Turing x Tumor heterogeneity | 4 | PARTIALLY_EXPLORED | YES (partially known) | Turing in cancer exists; specific mutational burden application is new |
| T6: Jamming x Chromatin | 0 | DISJOINT | YES | Jamming formalism never applied to chromatin |
