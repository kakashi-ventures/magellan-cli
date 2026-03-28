# Bond and Site Percolation in Three Dimensions

**Authors:** J. Wang, Z. Zhou, W. Zhang, T.M. Garoni, Y. Deng
**Journal:** Physical Review E, 87:052107 (2013)
**DOI:** 10.1103/PhysRevE.87.052107
**PubMed:** PMID 23767487
**arXiv:** arXiv:1302.0421

## Key Findings
- Definitive Monte Carlo simulation study of 3D percolation critical properties
- System sizes up to L = 512 on simple cubic lattices
- High-precision estimates of threshold and critical exponents

## Critical Values (3D Bond Percolation, Simple Cubic Lattice)
- **Percolation threshold**: p_c(bond) = 0.24881182(10)
- **Correlation length exponent**: ν = 0.8764(12) [i.e., 1/ν = 1.1410(15)]
- These are the benchmark values used in all subsequent work

## Universality Class
- 3D bond and site percolation belong to the same universality class
- Critical exponents depend only on dimension and local symmetry, NOT lattice type or whether bond vs. site percolation
- This universality is key for biological application: exact collagen network topology matters less than being in the same universality class

## Other 3D Critical Exponents (standard values from literature)
- β ≈ 0.417 (order parameter exponent — fraction of sites in giant cluster)
- γ ≈ 1.793 (susceptibility exponent)
- ν ≈ 0.876 (correlation length: ξ ~ |p - p_c|^(-ν))
- d_f ≈ 2.53 (fractal dimension of percolating cluster)
- Subdiffusion exponent at p_c: α ≈ 0.696 (D_w = 2 + β/ν ≈ 2.87)

## Scaling Laws Relevant to Hypothesis
- Correlation length: ξ ~ |p - p_c|^(-0.876)
- Order parameter: P_∞ ~ (p - p_c)^0.417 for p > p_c
- Characteristic domain size: L ~ (p - p_c)^(-0.876) → predicts spatial scale of T cell exclusion zones
- Finite-size scaling: transition sharpens as system size increases → explains why some tumors show sharp exclusion boundary

## Application to Session 015 Hypothesis
- **p** = LOX-mediated collagen crosslink density (bond occupation probability)
- **p_c** = critical crosslink density at which spanning pore cluster disappears (immune exclusion transition)
- **ξ** = spatial correlation length of T cell exclusion zones (diverges near p_c as ξ ~ |p - p_c|^(-0.876))
- **Finite-size scaling**: small tumor biopsies show "rounded" transition; large tumors show sharp exclusion front
- **Universality prediction**: different tumor types (PDAC, breast, lung) should yield the same critical exponent ν ≈ 0.876 regardless of specific collagen network topology

## Source URLs
- https://journals.aps.org/pre/abstract/10.1103/PhysRevE.87.052107
- https://arxiv.org/abs/1302.0421
