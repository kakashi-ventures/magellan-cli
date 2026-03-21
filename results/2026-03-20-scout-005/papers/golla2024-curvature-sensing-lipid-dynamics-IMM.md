# Curvature Sensing Lipid Dynamics in a Mitochondrial Inner Membrane Model

**Authors:** Vinaya Kumar Golla, Kevin J. Boyd, Eric R. May
**Year:** 2024
**Journal:** Communications Biology
**DOI/URL:** https://www.nature.com/articles/s42003-023-05657-6 | PMC10770132
**Status:** Peer-reviewed

---

## Abstract

Investigates lipid partitioning in the inner mitochondrial membrane using coarse-grained molecular dynamics simulations. Models curved bilayer systems containing PC, PE, and cardiolipin. Key finding: CDL has a stronger preference for accumulating in regions of negative curvature than PE lipids, and lipid partitioning propensity is dominated by sensitivity to mean curvature.

---

## Key Findings

**Curvature Sensitivity (quantified):**
- Lipids show strong negative correlation with mean curvature: average Pearson correlation -0.81
- Weaker but consistent sensitivity to Gaussian curvature: average -0.32
- Preference hierarchy: CDL-1 > CDL-2 > DOPE > POPE > POPC for negative curvature regions

**Quantified Partitioning:**
- Maximum localized lipid accumulations: 2.1%–6.7% across system compositions
- Up to 25% increase in local CDL concentration at high-curvature regions

**Critical Anomalous Finding:**
- CL has preference for ZERO Gaussian curvature (possibly due to asymmetric molecular geometry)
- PE may have stronger preference for nonzero Gaussian curvature phases
- This contradicts the simple packing parameter prediction that CL (P >1) should prefer negative Gaussian curvature

**Methods:**
- Coarse-grained MARTINI 2.2 force field, GROMACS 2020
- BUMPy tool for cylindrical membrane geometries (5–15 nm radii)
- MemSurfer for curvature calculations
- 4-microsecond NVT production simulations at 310 K

**What the Paper Does NOT Do:**
- No explicit packing parameter quantification
- No spontaneous curvature values reported
- No phase transition language
- No OPA1/MICOS protein interactions
- No liquid crystal physics terminology invoked

---

## Why Selected

Best quantitative paper on CL Gaussian curvature preference in the mitochondrial context. Explicitly measures both mean and Gaussian curvature sensitivity — the key parameters for an LC phase framework — but does not connect them to LC theory. The CL/Gaussian curvature anomaly (preference for zero, not negative Gaussian curvature despite cone shape) is a critical unexplained result that an LC phase transition framework would need to address.
