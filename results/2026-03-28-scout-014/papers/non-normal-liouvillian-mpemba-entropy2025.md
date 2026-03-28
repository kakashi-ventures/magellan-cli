# Quantum Mpemba Effect from Non-Normal Dynamics

**Authors:** Multiple authors (Polimi group)
**Year:** 2025 (received May 12; published June 2025)
**Journal:** Entropy (MDPI)
**Volume:** 27, Article 581
**DOI:** 10.3390/e27060581
**PMC:** 12192005
**URL:** https://www.mdpi.com/1099-4300/27/6/581

## Summary (retrieved via WebSearch)
Identifies a novel, fundamentally distinct mechanism for the Mpemba effect rooted in the non-normal nature of the Liouvillian superoperator — separate from the spectral-gap mechanism of Klich/Raz. Demonstrated in waveguide quantum electrodynamics systems.

## Key Findings

**Non-normal Liouvillian mechanism:**
- When the Liouvillian superoperator is non-normal (its eigenmodes are non-orthogonal), transient interference between decaying modes induces anomalous relaxation
- This produces Mpemba-like behavior even WITHOUT the spectral gap condition (c_2 = 0) being satisfied
- "Delayed thermalization" and "transient freezing" are hallmarks: the system appears to not relax early on, then suddenly relaxes rapidly

**Distinction from strong Mpemba effect:**
- Strong Mpemba effect: zero overlap with slowest mode → exponential speedup (requires fine-tuned initial condition)
- Non-normal Mpemba effect: non-orthogonal mode interference → transient suppression of relaxation (generic, less fine-tuned, occurs over finite range of initial conditions)

**Physical mechanism:**
- Non-normality = non-orthogonal left/right eigenvectors of the dynamics generator
- Transient amplification (like Trefethen's pseudospectral theory): even stable systems can amplify perturbations transiently
- In protein terms: non-normal MSM transition matrix → transient INCREASE in misfolding probability from initially folded states before eventual equilibration

**Experimental platform:**
- Demonstrated in waveguide QED: quantum emitters interacting with photonic modes of 1D waveguide
- Long-range coherent and incoherent interactions mediate non-normality
- These naturally arise from non-equilibrium steady states — exactly like protein conformational dynamics under crowding or stress

## Relevance to Mpemba x Amyloid Bridge — HIGHLY RELEVANT

**Non-normal MSM dynamics in proteins:**
- Protein MSMs are generally non-normal: the transition rate matrix W does not commute with its transpose (because detailed balance is broken under aggregation conditions, or because of non-equilibrium cellular environment)
- Non-normality implies left and right eigenvectors are NOT identical → modes are non-orthogonal
- Consequence: protein initially in native state can transiently INCREASE its misfolded population before eventually equilibrating to the native basin — a non-normal Mpemba analog

**Transient misfolding acceleration zones:**
- Bridge concept #3 in the Scout's target: "Non-normal Liouvillian dynamics creating transient misfolding acceleration zones"
- This paper provides the exact theoretical mechanism: non-normal mode interference → transient amplification → the "transient misfolding acceleration zone" IS the non-normal Mpemba region
- Proteins with non-normal MSMs will show initial misfolding amplification from native states before long-time equilibration to native — this is a vulnerability zone for amyloid formation

**Prediction for amyloidogenic proteins:**
- Proteins with more asymmetric transition rate matrices (higher non-normality measure, e.g., ||W - W^T||_F) will have stronger transient misfolding zones
- This could explain why cellular stress (which perturbs non-equilibrium protein dynamics) triggers amyloid nucleation: it transiently amplifies non-normality → transient misfolding zone emerges
- Testable: compute non-normality of published α-synuclein, tau, Aβ42 MSMs; rank by predicted transient misfolding amplitude

**Distinguishing prediction:**
- Non-amyloidogenic proteins (structurally similar but non-aggregating controls) should have MORE normal MSM transition matrices (closer to detailed balance) → smaller transient misfolding zones → resistance to aggregation

## Relevance Score: 9/10
Directly provides the theoretical mechanism for bridge concept #3. Non-normality of protein MSMs is computable from existing datasets (α-synuclein, Aβ42, tau MSMs are published). This paper + Yu2015 + Chakraborty2020 form the complete mechanistic triad for the hypothesis.
