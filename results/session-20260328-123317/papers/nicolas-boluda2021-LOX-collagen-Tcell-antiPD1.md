# Tumor Stiffening Reversion Through Collagen Crosslinking Inhibition Improves T Cell Migration and Anti-PD-1 Treatment

**Authors:** Alba Nicolas-Boluda, Juliette Vaquero, Laure Vimeux, Thomas Guilbert, Samuel Barrin, Chahrazade Kantari-Mimoun, et al.
**Journal:** eLife, Vol. 10, e58688 (2021)
**DOI:** 10.7554/eLife.58688
**PubMed:** PMID 34106045
**PMC:** PMC8203293

## Abstract Summary
Demonstrates that LOX inhibition reverses tumor ECM stiffening, improves T cell migration (up to 5-fold), and synergizes with anti-PD-1 therapy in pancreatic cancer models. Establishes tumor stiffness as a predictive physical marker of T cell motility.

## Key Quantitative Findings
- **T cell displacement**: 5-fold increase in mPDAC (mouse pancreatic ductal adenocarcinoma) model with BAPN treatment
- **CD8+ T cell infiltration**: 3–4-fold increase in stroma and tumor islets in KPC model
- **LOX inhibitor**: BAPN (beta-aminopropionitrile) at 3 mg/mL in drinking water
- **Stiffness-migration correlation**: Steep inverse linear correlation between tumor stiffness and T cell migration speed across 5 tumor models
- **Synergy**: BAPN + anti-PD-1 significantly delayed tumor progression in KPC pancreatic model; neither agent alone was significant
- **Cytokine readout**: Elevated GrzmB+CD8+ T cells, increased CD8+/Treg ratio, elevated TNFα and RANTES

## Models Tested
- EGI-1 (bile duct carcinoma)
- mPDAC (mouse pancreatic ductal adenocarcinoma)
- MMTV-PyMT (breast cancer)
- KPC (pancreatic cancer) — showed strongest therapeutic synergy

## Methods
- Non-invasive shear wave elastography for tumor stiffness
- Second-harmonic generation (SHG) imaging for collagen architecture
- Dynamic confocal microscopy on fresh tumor slices for T cell tracking
- Flow cytometry for immune profiling

## Key Numbers for Percolation Modeling
- LOX inhibition reduces collagen crosslinking → reduces p (bond occupation probability)
- T cell speed in untreated mPDAC: ~1 µm/min (nearly static)
- After LOX inhibition: estimated ~5 µm/min based on 5-fold improvement
- Stiffness range: varies from ~0.5 kPa (soft) to >5 kPa (stiff) across tumor models

## Relevance to Session 015
- **Direct evidence**: LOX crosslinking density (= bond occupation probability p in percolation model) is the key control parameter for T cell infiltration
- **Critical gap**: No paper in this field defines a THRESHOLD value of LOX activity or collagen crosslinking density at which T cell infiltration transitions from excluded to infiltrating — this is exactly the percolation threshold p_c that our hypothesis would predict
- **Missing**: No application of percolation scaling laws (ξ ~ |p-p_c|^(-ν)) to predict spatial correlation of T cell exclusion zones

## Source URLs
- https://elifesciences.org/articles/58688
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8203293/
