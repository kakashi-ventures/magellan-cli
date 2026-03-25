# Tumor Stiffening Reversion Improves T Cell Migration

**Title:** Tumor stiffening reversion through collagen crosslinking inhibition improves T cell migration and anti-PD-1 treatment
**Authors:** Nicolas-Boluda A, Vaquero J, Viguier L, Guilbert T, Andrieux G, Bikfalvi A, Quartier Dit Maire L, Laurent-Puig P, Boilève A, Ballet S, et al.
**Year:** 2021
**Journal:** eLife
**DOI:** 10.7554/eLife.58688
**PMC:** PMC8203293
**PMID:** 34106045

## Abstract

In five preclinical mouse tumor models, collagen crosslinking inhibition with BAPN (a LOX inhibitor) reduces tumor stiffness, disrupts collagen fiber alignment, and significantly improves T cell migration and anti-PD-1 immunotherapy efficacy.

## Key Findings

- **LOX inhibition with BAPN:**
  - Reduces tumor stiffness (Young's modulus)
  - Decreases collagen fiber width and linearization
  - Creates more dispersed/intermingled collagen architecture
  - Reduces densely packed collagen regions

- **T cell improvements post-LOX inhibition:**
  - Up to 5-fold increase in cell displacement
  - 3–4-fold increase in CD8+ T cell infiltration (KPC tumors)
  - Improved migration speed and trajectory straightness

- **Therapeutic synergy:** BAPN + anti-PD-1 significantly delays tumor progression vs. either monotherapy

## What Framework Is NOT Used

- **No percolation or network-theoretic framework.** Analysis uses mechanical measurements and microscopy-based characterization.
- LOX is described as a collagen crosslinking enzyme (molecular mechanism), not as a bond-probability parameter in a percolation model.
- No quantitative threshold analysis for infiltration.

## Relevance to T1 (Percolation × T cell infiltration)

This paper is the closest existing link between LOX crosslinking and T cell infiltration. It shows:
1. LOX crosslinking density → collagen network architecture → T cell exclusion
2. A threshold-like effect (reducing crosslinking transforms immune desert → inflamed)

The T1 hypothesis proposes formalizing this as a **bond percolation problem**: LOX crosslinking events = bond probability p, collagen volume fraction = p_c (bond threshold), correlation length exponent ν determines how rapidly the infiltration changes near threshold. This percolation-theoretic treatment is NOT in this paper or anywhere in the literature.

**Partially explores the connection, but the percolation framework is novel.**
