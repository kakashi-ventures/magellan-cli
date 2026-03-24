# Literature Landscape — Session session-20260324-200851
## Disjointness Verification for 6 Scout Candidates
## Date: 2026-03-24

---

## T1: Cryo-EM heterogeneity analysis x OMV cargo sorting

### Cross-field search results
- "cryo-EM outer membrane vesicle cargo sorting" — Very few results. Some cryo-EM/cryo-ET images of OMVs exist (Beveridge group, Kulp et al. 2015 mBio) but these are purely morphological — NO heterogeneity analysis, NO 3D classification of cargo content, NO cryoDRGN on OMP conformational states.
- "cryo-electron tomography bacterial outer membrane vesicle" — Roier et al. 2016, Toyofuku et al. 2019 review mention cryo-EM imaging of OMVs. These are descriptive, not analytical.
- "cryoDRGN bacterial" or "3DVA bacterial membrane" — NO results connecting these heterogeneity tools to bacterial OMV biology.
- Key finding: The cargo sorting mechanism is explicitly identified as unknown in multiple reviews (Schwechheimer & Kuehn 2015 Nat Rev Microbiol, Toyofuku et al. 2019 Nat Rev Microbiol, McMillan & Kuehn 2021 Microbiol Mol Biol Rev).
- Recent: Bos et al. 2021 used cryo-ET to visualize OMV budding but without particle classification.

### Disjointness Assessment: **DISJOINT**
- Cross-field co-citations: ~2-3, all descriptive imaging
- No paper applies cryo-EM heterogeneity analysis tools to OMV cargo sorting
- The analytical toolset (cryoDRGN, 3DVA, RELION 3D classification) has never been deployed on bacterial vesicle populations
- Score: 9/10 (near-complete disjointness)

---

## T2: Patch-clamp electrophysiology x Plant turgor sensing

### Cross-field search results
- "patch clamp plant protoplast mechanosensitive" — Small literature exists. Cosgrove & Hedrich 1991 showed stretch-activated channels in guard cell protoplasts. More recent: Haswell et al. 2008 showed MSL channels in plant patch-clamp. Hamilton et al. 2015 characterized OSCA1 in HEK293 heterologous expression.
- "pressure clamp plant turgor" — Very few results. Most plant electrophysiology uses osmotic steps, NOT direct pressure-clamp protocols.
- KEY FINDING: OSCA1/OSCA1.3 have been characterized by patch-clamp — BUT in heterologous expression systems (HEK293, Xenopus oocytes), NOT in native plant protoplasts at turgor-relevant pressures.
- The gap is specific: native plant protoplast patch-clamp with calibrated pressure-clamp at 0.1-1 MPa range has NOT been done because standard patch-clamp pressure ranges are ~0-50 mmHg (~7 kPa), far below turgor (0.1-1 MPa = 750-7500 mmHg).
- Technical barrier is real and potentially blocking: turgor pressures exceed standard pressure-clamp capabilities by >100x.

### Disjointness Assessment: **PARTIALLY_EXPLORED**
- Cross-field co-citations: ~15-20 (plant patch-clamp is a small but existing niche)
- Key issue: The pressure range mismatch means the specific bridge (patch-clamp at turgor pressures) may be technically infeasible, not just unattempted
- Score: 5/10 (moderate disjointness, significant technical barrier)
- FLAG: Bridge may be factually problematic — standard pressure-clamp cannot reach turgor pressures

---

## T3: FLIM-FRET biosensors x Bacterial persister metabolism

### Cross-field search results
- "FLIM persister" — 0 results
- "FRET biosensor persister bacteria" — 0-1 results. One tangential paper using GFP reporters (not FRET biosensors).
- "fluorescence lifetime bacterial" — Some papers on FLIM of bacterial biofilms (autofluorescence), but these use intrinsic fluorescence, NOT genetically encoded FRET biosensors.
- "QUEEN ATP bacteria" — Yaginuma et al. 2014 Cell developed QUEEN in E. coli, but it has NOT been used for persister phenotyping. The biosensor EXISTS in bacteria but the persister application does not.
- "SoNar bacteria" — Zhao et al. 2015 developed SoNar for NADH in E. coli. NOT applied to persisters.
- KEY FINDING: Both QUEEN (ATP) and SoNar (NAD+/NADH) have been expressed and validated in E. coli. The tool-target gap is real: biosensors work in bacteria, but nobody has used them to measure metabolite levels in persister subpopulations.
- The persister field uses mostly bulk measurements, microfluidics + time-lapse with simple reporters (GFP, mCherry), and single-cell RNA (MERFISH).
- Conlon et al. 2016 (Nature) and Shan et al. 2017 (Science) established the metabolic state debate but lack single-cell metabolite data.

### Disjointness Assessment: **DISJOINT**
- Cross-field co-citations: 0-1 (essentially zero)
- The biosensors exist and work in bacteria. The question exists and is central to the field. The connection has not been made.
- Score: 9/10 (near-complete disjointness)

---

## T4: Optogenetic c-di-GMP tools x Biofilm dispersal

### Cross-field search results
- "optogenetic biofilm" — Multiple results. Reade et al. 2023 (likely others) have used light-activated tools in biofilm contexts.
- "LAPD c-di-GMP biofilm" — Ryu & Bhatt 2016 developed LAPD. It HAS been used in several synthetic biology papers with biofilm-related readouts.
- KEY FINDING: Huang et al. 2018 (ACS Synth Biol) used near-infrared optogenetic c-di-GMP control in E. coli biofilms. This directly addresses the proposed bridge.
- "BphS biofilm dispersal" — Found in Ryu, Zheng, & Bhatt group publications. BphS/BphG system has been deployed in biofilm contexts.
- The therapeutic biofilm dispersal angle may add novelty, but the core bridge (optogenetic c-di-GMP manipulation in biofilms) EXISTS.

### Disjointness Assessment: **WELL_EXPLORED**
- Cross-field co-citations: >10
- Optogenetic c-di-GMP tools have been used in biofilm contexts by multiple groups
- EXCLUDE from further consideration
- Score: 2/10 (well-explored)

---

## T5: AFM force spectroscopy x IDP condensate mechanics

### Cross-field search results
- "AFM condensate" — Multiple results. Alshareedah et al. 2021 used AFM nanoindentation on condensates. Jawerth et al. 2020 (Science) measured condensate material properties including with AFM.
- "atomic force microscopy phase separation protein" — Established connection. Multiple papers use AFM imaging and nanoindentation on protein condensates.
- "single molecule force spectroscopy condensate" — Fewer results, but optical tweezers pulling from condensates has been done (Ghosh et al. 2019).
- KEY FINDING: AFM nanoindentation of condensates is an active area. Single-molecule force spectroscopy (pulling individual chains from droplets) is less explored but the AFM-condensate connection is NOT disjoint.
- The specific bridge of pulling individual IDP chains from condensate droplets using SMFS may be novel, but the broader connection is established.

### Disjointness Assessment: **PARTIALLY_EXPLORED**
- Cross-field co-citations: >20
- AFM nanoindentation of condensates is an active area with multiple published papers
- The single-molecule pulling variant may be novel but the field pairing is not disjoint
- Score: 4/10 (substantially explored)

---

## T6: EIS x Gut microbiome monitoring

### Cross-field search results
- "impedance spectroscopy gut microbiome" — Very few results. Most hits are about TEER (transepithelial electrical resistance) measurements of gut epithelial barrier, not microbiome.
- "electrochemical impedance microbiome" — Sparse. Some papers on EIS detection of specific pathogens (E. coli, Salmonella) using antibody-functionalized electrodes, but these are biosensors for pathogen detection, NOT metabolic state monitoring.
- "impedance fecal" — Very few. Some impedance-based stool consistency measurements (Bristol scale automation).
- KEY FINDING: Microbial fuel cell and bioelectrochemical systems literature measures electrochemical activity of microbial communities but does NOT use EIS frequency analysis for metabolic state fingerprinting. The electrochemistry-microbiome connection exists in bioelectrochemical systems but EIS-specific frequency sweep analysis for gut microbiome functional monitoring appears genuinely novel.
- Ingestible electronics for gut monitoring exist (pH, temperature, gas sensing) but NOT impedance spectroscopy.
- The equivalent circuit modeling approach (Randles circuit, Warburg diffusion) applied to characterize microbiome metabolic state is genuinely novel.

### Disjointness Assessment: **DISJOINT**
- Cross-field co-citations: ~2-3 (tangential pathogen detection papers)
- The specific bridge (EIS frequency analysis for metabolic state fingerprinting) has no precedent
- Ingestible capsule form factor is technically mature but never combined with EIS for microbiome
- Score: 8/10 (strong disjointness)

---

## Summary Table

| Target | Field A | Field C | Disjointness | Score | Flag |
|---|---|---|---|---|---|
| T1 | Cryo-EM heterogeneity | OMV cargo sorting | DISJOINT | 9/10 | Clean |
| T2 | Patch-clamp electrophysiology | Plant turgor sensing | PARTIALLY_EXPLORED | 5/10 | Pressure range mismatch may make bridge infeasible |
| T3 | FLIM-FRET biosensors | Bacterial persisters | DISJOINT | 9/10 | Clean — biosensors validated in bacteria but not used for persisters |
| T4 | Optogenetic c-di-GMP | Biofilm dispersal | WELL_EXPLORED | 2/10 | EXCLUDE — multiple published papers |
| T5 | AFM-SMFS | IDP condensates | PARTIALLY_EXPLORED | 4/10 | AFM nanoindentation of condensates active area |
| T6 | EIS | Gut microbiome monitoring | DISJOINT | 8/10 | EIS metabolic fingerprinting novel, some tangential pathogen detection papers |
