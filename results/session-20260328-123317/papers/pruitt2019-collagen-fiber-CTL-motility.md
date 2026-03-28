# Collagen Fiber Structure Guides 3D Motility of Cytotoxic T Lymphocytes

**Authors:** Hawley C. Pruitt, Wen Xu, et al. (Duke University)
**Journal:** Matrix Biology, Vol. 85-86, pp. 7–19 (2020; published online Feb 2019)
**DOI:** 10.1016/j.matbio.2019.02.003
**PubMed:** PMID 30776427
**PMC:** PMC6697628

## Abstract Summary
CD8+ cytotoxic T lymphocytes (CTLs) move faster and more persistently in aligned collagen matrices vs. unaligned matrices. CTLs migrate along the axis of alignment. MLCK inhibition abolishes the effect of fiber alignment on CTL motility, implicating actomyosin contractility.

## Key Quantitative Findings
- **Collagen concentration**: 3 mg/mL
- **Fiber alignment**: Microfluidic devices produce aligned vs. unaligned collagen gels
- **Speed**: CD8+ T cells show "increased speed" and "enhanced instantaneous velocity" in aligned conditions (exact values in figures, not tabulated in text)
- **MSD**: MSD along alignment axis (X) > MSD perpendicular (Y) in aligned conditions; significant difference between aligned and unaligned
- **Track characteristics**: Straighter trajectories, smaller turning angles in aligned collagen
- **Motility coefficient**: Significantly increased in aligned vs. unaligned conditions
- **Mechanism**: MLCK inhibition (ML-7 drug) nullifies alignment effect → myosin-based traction force required

## Experimental Context
- Human primary CD8+ T cells (activated)
- At least 50 cells analyzed per condition, experiments repeated 3x
- Metrics: MSD, cumulative track length, motility coefficient, displacement along/perpendicular to alignment, track straightness, turning angles

## Key Numbers for Percolation Modeling
- T cell size: ~10 µm diameter
- Collagen at 3 mg/mL: intermediate density, near boundary between permissive and restrictive
- Aligned collagen (parallel fibers) = anisotropic pore network → channeled diffusion (anomalous exponent depends on orientation)
- Unaligned collagen = isotropic random network → standard percolation applies
- The paper demonstrates anisotropic MSD as a function of collagen topology — consistent with what percolation predicts for anisotropic networks

## Critical Gap
- No measurement at varying collagen concentrations (only 3 mg/mL)
- No measurement near a transition threshold
- No comparison with passive particle diffusion
- Does not invoke percolation theory

## Relevance to Session 015
- Provides quantitative MSD framework for T cell motility in collagen
- Shows MSD is anisotropic based on fiber orientation — percolation theory predicts this
- Gap: No paper measures T cell MSD vs. crosslinking density (LOX activity) to identify the transition from diffusive to sub-diffusive motion (signature of approaching percolation threshold)

## Source URLs
- https://pubmed.ncbi.nlm.nih.gov/30776427/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6697628/
