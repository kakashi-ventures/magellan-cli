# Final Hypothesis Cards — Session 013

## Target: Cryo-EM heterogeneity methods × OMV cargo sorting
## Strategy: Tool repurposing | Disjointness: DISJOINT

---

## Card 1: GMM/BIC Population Analysis of OMV Biogenesis Pathways

| Field | Value |
|-------|-------|
| **ID** | C2-H1 |
| **Quality Gate** | PASS |
| **Cross-model** | PROMISING (GPT: 5, Gemini: 9) |
| **Composite** | 8.35 |
| **Confidence** | 7/10 |
| **Groundedness** | 7/10 |
| **Novelty** | 9/10 |

**Mechanism:** Apply Gaussian Mixture Model analysis with Bayesian Information Criterion model selection to cryo-EM-derived OMV descriptors (diameter, surface roughness, radial density profile, circularity). Test whether P. aeruginosa OMV populations are best described as discrete biogenesis pathway modes or a continuum. BIC selects optimal K; proteomics of SEC fractions assigns pathway labels.

**Falsifiable prediction:** BIC-optimal GMM with K≥3 components. Components separable by diameter (means differ >30 nm) AND protein-to-lipid ratio. Delta-ompA mutant loses one component.

**Bridge concept:** GMM/BIC is standard in ML and used in RELION for cryo-EM heterogeneity but has never been applied to whole-vesicle population analysis.

**Counter-evidence:** Heterogeneity may be continuous (K=1 or K=2 optimal) — important negative result meaning cargo sorting is single-vesicle, not pathway-level.

**Cross-model corrections:** OprF prediction may be inverted (OprF-poor regions more bud-prone). Require proteomics validation before interpreting clusters as pathways.

**Test protocol:** (1) Purify PAO1 OMVs by SEC. (2) Cryo-EM >50,000 particles. (3) Measure 5+ per-particle features. (4) Fit GMM K=1..6, compute BIC. (5) If K≥3: proteomics per SEC fraction. (6) Validate: delta-ompA should lose one component.

---

## Card 2: Power Analysis for OMV Budding Site Subtomogram Averaging

| Field | Value |
|-------|-------|
| **ID** | C2-H2 |
| **Quality Gate** | CONDITIONAL PASS |
| **Cross-model** | NEEDS WORK |
| **Composite** | 8.55 (pre-adjustment) |
| **Confidence** | 6/10 (downgraded) |
| **Groundedness** | 6/10 (downgraded) |
| **Novelty** | 7/10 |

**Mechanism:** Determine feasibility of cryo-ET subtomogram averaging campaign on OMV budding intermediates by calculating minimum particle count needed for target resolution, benchmarked against published datasets (HIV-1 capsid, T4SS).

**Falsifiable prediction:** Empirical pilot of 50-100 tomograms determines budding event frequency per cell and achievable resolution. If <1 event per 10 tomograms, campaign is infeasible at current throughput.

**Bridge concept:** Power analysis for subtomogram averaging is routine in cryo-ET but has never been applied to OMV budding sites.

**CRITICAL ISSUE (GPT-5.4):** Original N_min formula yields ~460,000 particles when computed, not 200-500 as stated. Must reframe as empirical pilot rather than closed-form calculation. Citation: Schur et al. 2016 published in *Science*, not *Nature*.

**Test protocol (revised):** (1) Collect 50-100 tilt series of stressed PAO1. (2) Count budding events per tomogram. (3) Build empirical resolution-vs-N curve from pilot. (4) Extrapolate total required data collection. (5) State feasibility from data.

---

## Card 3: DegP/MucD Cryo-ET Difference Mapping at OMV Budding Sites

| Field | Value |
|-------|-------|
| **ID** | C2-H3 |
| **Quality Gate** | PASS |
| **Cross-model** | PROMISING (strongest agreement) |
| **Composite** | 8.20 |
| **Confidence** | 6/10 |
| **Groundedness** | 7/10 |
| **Novelty** | 9/10 |

**Mechanism:** Compare cryo-ET tomographic averages of wild-type vs DegP-S210A (protease-dead) mutant OMVs to identify chaperone-dependent density at budding sites. DegP hexameric cage (~12 nm) should appear as localized density at periplasmic face of budding membrane. Delta-surA control for specificity.

**Falsifiable prediction:** Difference map (WT minus S210A) shows localized density loss at budding sites corresponding to DegP hexameric cage. Luminal density also reduced in S210A OMVs. Delta-surA shows different pattern (different client proteins).

**Bridge concept:** Cryo-ET difference mapping established for molecular machines (flagellar components) but never applied to periplasmic chaperone localization in OMV context.

**Cross-model corrections:** P. aeruginosa uses MucD as primary HtrA-family chaperone, not DegP — must use correct species ortholog. Verify enrichment biochemically before investing in cryo-ET.

**Test protocol:** (1) Generate MucD-S210A and delta-surA mutants in PAO1. (2) Cryo-ET of WT, MucD-S210A, delta-surA. (3) Subtomogram averaging of budding sites per strain. (4) Compute difference maps. (5) Dock hexamer structure into difference density. (6) Proteomics validation.

---

## Card 4: ML Template Matching for OMV Cargo Identification (Needs Re-scoping)

| Field | Value |
|-------|-------|
| **ID** | C2-H4 |
| **Quality Gate** | PASS |
| **Cross-model** | NEEDS RE-SCOPING |
| **Composite** | 8.15 |
| **Confidence** | 5/10 |
| **Groundedness** | 7/10 |
| **Novelty** | 10/10 |

**Mechanism:** Apply ML-guided structural identification tools (DeePiCt — supervised 3D CNN; TomoTwin — metric learning embeddings) to cryo-ET of P. aeruginosa OMVs to identify cargo proteins in situ without labels. Generate per-OMV "cargo manifests."

**Falsifiable prediction (re-scoped):** Template matching identifies one large structurally distinctive complex (e.g., secretin, TonB-dependent receptor) per OMV with validated precision-recall on simulated tomograms. Knockout control removes predicted signal.

**Bridge concept:** ML template matching in cryo-ET (2023 Nature Methods tools) has never been applied to OMV cargo identification. Genuinely novel tool-transfer.

**Cross-model consensus:** At 20-30Å tomographic resolution, most OMP beta-barrels have indistinguishable Fourier signatures. Must re-scope from "general OMP identification" to "one large distinctive complex with knockout control." Benchmark on simulated data first.

**Test protocol (re-scoped):** (1) Select one large distinctive target (e.g., PilQ secretin). (2) Simulate tomograms with known positions. (3) Benchmark precision-recall. (4) Apply to real PAO1 OMV tomograms. (5) Validate with pilQ knockout. (6) Only if validated: expand to additional targets.
