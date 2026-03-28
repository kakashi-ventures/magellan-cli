# Macrophages Restrict Tumor Immune Infiltration by Controlling Collagen Topography

**Authors:** Zoé Fusilier et al. (Ivaska Cell Adhesion and Cancer Lab, Turku)
**Journal:** Science Immunology (2025)
**DOI:** 10.1126/sciimmunol.adw8291
**PubMed:** PMID 41860994
**bioRxiv preprint:** 10.1101/2025.01.17.633527 (January 2025)

## Key Findings
- Macrophages shape fibrillar collagen topography in late-stage tumors and this dictates T cell localization
- Macrophage depletion activates a Tcf4-mediated fibrotic pathway promoting collagen III deposition
- Intermingled collagen III-rich networks FAVOR T cell and neutrophil infiltration
- Macrophages INHIBIT this Tcf4-Collagen3 axis → creates excluded phenotype
- Immune cell localization can be predicted from local fibrillar collagen topography (ML approach)
- Re-analysis of human solid tumor data confirms: TCF4, COL3A1 expression correlates strongly with T cell and neutrophil signatures

## Mechanism
- Tcf4 (transcription factor 4) in cancer and stromal cells promotes collagen III deposition
- Collagen III forms intermingled, less-aligned networks → favorable topology for immune cell passage
- Tumor-associated macrophages suppress Tcf4 → shift to collagen I-dominated aligned networks → exclusion
- The collagen TOPOLOGY (alignment, intermingling) matters more than density alone

## Quantitative Data Available
- Spatial correlation between TCF4/COL3A1 signatures and T cell density in human tumors (RNA-seq correlation data)
- Machine learning prediction of immune cell localization from SHG collagen images

## Relevance to Session 015
- **Critical new insight**: Collagen TOPOLOGY (network connectivity pattern) — not merely density — controls T cell infiltration
- This is precisely what percolation theory captures: the transition in network connectivity (not just fiber density) determines whether a spanning cluster of traversable pores exists
- Collagen I (aligned) = low-connectivity network (p < p_c)
- Collagen III (intermingled) = high-connectivity network (p > p_c)
- **Gap**: No one has quantified the connectivity of collagen I vs III networks using bond percolation metrics (bond occupation probability, correlation length)
- The Tcf4 axis provides a specific molecular handle on p (bond occupation probability)

## Source URLs
- https://www.science.org/doi/10.1126/sciimmunol.adw8291
- https://www.biorxiv.org/content/10.1101/2025.01.17.633527v1
