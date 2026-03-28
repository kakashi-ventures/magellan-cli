# Active Brownian Particles Moving in a Random Lorentz Gas

**Authors:** M. Zeitz, K. Wolff, H. Stark
**Journal:** European Physical Journal E, 40:23 (2017)
**DOI:** 10.1140/epje/i2017-11510-0
**PubMed:** PMID 28236113
**arXiv:** arXiv:1611.07892

## Abstract Summary
Compares active Brownian particles (ABPs) with passive Brownian particles moving through a random array of obstacles (Lorentz gas). Near the percolation density, both exhibit subdiffusive behavior, but the active particle reaches steady state faster. Counterintuitively, high activity leads to LOWER effective diffusion due to self-trapping.

## Key Findings
- **Near percolation density** (η ≈ 0.28 for 2D random disk obstacles): both Brownian and active particles exhibit subdiffusion with exponent α ≈ 0.66
- **Active particles**: Initially superdiffusive (α > 1.0) at short times; transition to subdiffusion near percolation density
- **Self-trapping paradox**: At high activity, active particles are LESS mobile than Brownian particles — persistent propulsion causes particles to wedge behind obstacles
- **Steady state**: Active particles reach their long-time behavior more rapidly than passive ones

## Physics Parameters
- Percolation density for 2D random obstacle array: η_c ≈ 0.28 (obstacle volume fraction)
- Long-time diffusion exponent: α ≈ 0.66 at percolation (standard 3D bond percolation gives α = 0.696)
- Active velocity: Pe (Peclet number) controls activity; self-trapping dominates at Pe > ~10

## Perspective Article (arXiv 2603.04602, March 2026)
A 2026 perspective article revisits Zeitz et al. and identifies key open questions:
- Most work has been 2D; 3D active Lorentz gas has different threshold
- Chiral active particles, deformable particles, hydrodynamic interactions remain unexplored
- Biological systems (bacteria in porous media) show "intermittent hopping from pore to pore" matching predictions

## Relevance to Session 015
- **Foundational**: Establishes that T cell-like active particles in disordered ECM networks need active-particle corrections to standard percolation
- **Self-trapping warning**: T cells with high motility in dense ECM may actually be MORE excluded than passive particles — relevant to understanding why immunotherapy fails in stiff tumors
- **3D gap**: Most active percolation theory is 2D; tumor ECM is 3D — threshold values differ (p_c ≈ 0.249 for 3D bond percolation vs. 0.593 for 2D square bond)
- **No application to tumor immunology in any of these papers**

## Key Numbers for Computational Validation
- 3D bond percolation threshold (simple cubic): p_c = 0.2488
- 2D bond percolation (square lattice): p_c = 0.5
- Correlation length exponent 3D: ν = 0.876 (1/ν = 1.141)
- Subdiffusion exponent at p_c: α = 0.696 (3D), 0.66 (2D near threshold)

## Source URLs
- https://link.springer.com/article/10.1140/epje/i2017-11510-0
- https://arxiv.org/abs/1611.07892
- https://arxiv.org/abs/2603.04602 (2026 perspective)
