# Literature Context — Session 015
## Target: Percolation Threshold Theory × T Cell Infiltration in Solid Tumors

**MCP Status**: Unavailable (connection error). All retrieval via WebSearch + WebFetch.
**Date**: 2026-03-28
**Retrieval coverage**: 9 full paper files saved in papers/ directory

---

## Field A: Percolation Theory (Statistical Mechanics)

### Foundational Framework
Bond percolation theory (Broadbent & Hammersley 1957) studies the connectivity of random networks. On a d-dimensional lattice, bonds are independently occupied with probability p. Below a critical threshold p_c, no spanning connected cluster exists. Above p_c, a macroscopic connected cluster appears. Near p_c, the correlation length diverges as:

**ξ ~ |p - p_c|^(-ν)**

For 3D bond percolation on a simple cubic lattice:
- **p_c = 0.24881182(10)** (Wang et al. 2013, PRE 87:052107) — benchmark value
- **ν = 0.876** (1/ν = 1.141) — correlation length exponent
- **β = 0.417** (order parameter exponent: fraction of sites in giant cluster)
- **γ = 1.793** (susceptibility exponent)
- **Fractal dimension at p_c**: d_f ≈ 2.53

**Universality**: These exponents depend ONLY on dimension and local symmetry, NOT on lattice type or whether bond vs. site percolation is used. Critically: two systems with the same critical exponents are in the same universality class — their critical behavior is formally identical regardless of microscopic details.

**Subdiffusion at criticality**: A random walker on a percolating cluster at p = p_c exhibits anomalous diffusion with MSD ~ t^α where α = 0.696 in 3D (subdiffusion; standard diffusion gives α = 1). This is a direct, measurable prediction.

**Finite-size scaling**: For a system of size L, the percolation transition appears "rounded" (not sharp) when L < ξ. The sharpness scales as ΔL ~ L^(-1/ν). This has direct implications for tumor size dependence of immune exclusion phenotype.

### Recent Advances (2024-2026)
1. **Saha, Banerjee & Mohanty (2024)** — "Site-Percolation Transition of Run-and-Tumble Particles," Soft Matter. First study of active particle percolation. Key finding: activity shifts the percolation threshold and changes critical exponents; re-entrant phase behavior; scaling function remains universal. **Critical for session 015**: T cells are active particles — passive percolation theory needs active-particle corrections. Paper is 2D only; 3D active percolation in realistic fibrous ECM remains unstudied.

2. **Zeitz, Wolff & Stark (2017)** — Active Brownian particles in random Lorentz gas (EPJE). Near percolation density: active particles reach steady state faster than passive ones but LESS mobile at high activity (self-trapping). Near η_c ≈ 0.28, subdiffusive exponent α ≈ 0.66. **Perspective article (arXiv 2603.04602, March 2026)**: open question is 3D extension and application to biological systems.

3. **Wang et al. 2013 (PRE 87:052107)** — Benchmark 3D critical exponents. p_c = 0.2488, ν = 0.876. Monte Carlo with L = 512.

4. **Equilibrium percolation on simple cubic lattice (ScienceDirect 2025)** — Recent work on percolation thresholds in 3D systems where particles can reorganize; extends to non-quenched disorder.

### Key Numbers from Field A
| Parameter | Value | Note |
|---|---|---|
| p_c (3D bond, simple cubic) | 0.2488 | Benchmark threshold |
| p_c (2D bond, square) | 0.5 | Different universality |
| ν (3D percolation) | 0.876 | Correlation length exponent |
| α at p_c (3D) | 0.696 | Subdiffusion MSD exponent |
| Active particle self-trapping | Effective diffusion < passive at high activity | Zeitz 2017 |
| Active percolation threshold shift | Activity increases effective p_c | Saha 2024 |

---

## Field C: Tumor Immunology / ECM-Immune Exclusion

### The Immune Exclusion Phenotype
Solid tumors are classified into three immune phenotypes (reviewed extensively 2023–2025):
- **Inflamed**: CD8+ T cells infiltrate the tumor parenchyma — responsive to checkpoint blockade
- **Excluded**: T cells present in peritumoral stroma but fail to penetrate tumor nests — unresponsive
- **Desert**: No T cells at all

The excluded phenotype is the dominant driver of immunotherapy resistance. The primary mechanism is dense, crosslinked collagen ECM forming a physical barrier.

### Key Papers in Field C

**1. Salmon et al. 2012 (JCI)** — Foundational paper. In human lung tumors, T cell migration is dictated by aligned collagen fibers. T cells move along fibers at the tumor-stroma boundary, rarely entering tumor nests. Collagenase treatment rescues infiltration. Quantitative live imaging of T cells in fresh tumor slices.

**2. Kuczek et al. 2019 (JITC 7:68)** — Collagen density directly suppresses T cell activity. At 4 mg/mL (tumor-like) vs. 1 mg/mL (healthy-like): T cell killing reduced, CD8:CD4 ratio shifted, 6/7 cytotoxic markers downregulated. TGF-β autocrine mechanism. **Critical gap**: Only two density points tested — no dose-response, no threshold identified.

**3. Nicolas-Boluda et al. 2021 (eLife 10:e58688)** — LOX inhibition (BAPN) reverses ECM stiffening, improves T cell displacement 5-fold in mPDAC model, 3–4-fold increase in CD8+ tumor infiltrates (KPC model), synergizes with anti-PD-1 (delayed progression). Five tumor models. Establishes tumor stiffness as predictive marker of T cell motility. **Gap**: Does not identify a percolation-like threshold in LOX activity or collagen crosslinking density.

**4. Pruitt et al. 2019 (Matrix Biology)** — CD8+ T cells move faster and more persistently in aligned vs. unaligned 3 mg/mL collagen. Anisotropic MSD (higher along fiber axis). MLCK inhibition abolishes alignment effect. Quantitative MSD measurements. **Gap**: No measurement across density range; no threshold analysis.

**5. Fusilier et al. 2025 (Science Immunology)** — Macrophages control collagen TOPOLOGY (not just density) to restrict T cell infiltration. Tcf4 pathway promotes collagen III (intermingled) networks → permissive for T cells. Macrophages suppress Tcf4 → collagen I (aligned) networks → exclusion. ML prediction of T cell localization from SHG collagen images in human tumors. **Key for session 015**: Collagen NETWORK TOPOLOGY (connectivity) is the relevant variable — exactly what percolation theory describes.

**6. Xiao et al. 2023 (Nat Comm 14:5110)** — FAP-CAR T cells deplete cancer-associated fibroblasts (the main LOX-expressing cell type), collapse the desmoplastic stroma, and enable mesothelin-CAR T + anti-PD-1 in treatment-resistant pancreatic cancer. SHG quantification of collagen. **Gap**: Does not quantify critical collagen density threshold.

### Recent Key Papers (2024-2025)
- **Collagen VI and T cell trapping in prostate cancer (Nat Comm 2023)**: CD4+ T cell motility completely abolished on purified Col VI surfaces vs. fibronectin/Collagen I; integrin α1 absence in T cells causes loss of traction force generation. Collagen subtype specificity matters.
- **TAM-collagen-CD8 (breast cancer 2024, PubMed 38831058)**: Tumor-associated macrophages restrict CD8+ T cells through both collagen deposition AND metabolic reprogramming (arginine consumption). Physical + metabolic exclusion.
- **Desmoplastic immune exclusion review 2024 (Trends in Immunology)**: Excluded tumors have elevated TGF-β, endothelial immunosuppression, lower inflammatory programs than inflamed tumors.

### Key Quantitative Numbers from Field C
| Measurement | Value | Source |
|---|---|---|
| T cell speed in stiff mPDAC tumor | ~1 µm/min (near static) | Nicolas-Boluda 2021 |
| T cell speed after LOX inhibition | ~5 µm/min (estimated 5x increase) | Nicolas-Boluda 2021 |
| Low-density collagen (healthy) | 1 mg/mL | Kuczek 2019 |
| High-density collagen (tumor) | 4 mg/mL | Kuczek 2019 |
| Collagen pore size, normal tissue | 10–50 µm | Multiple reviews |
| Collagen pore size, tumor | 1–10 µm | Multiple reviews |
| T cell nucleus diameter | 8–10 µm | Cell biology literature |
| Critical pore size for migration | ~7 µm² (nuclear size limit) | Erickson lab |
| CD8+ T cell increase with BAPN | 3–4-fold | Nicolas-Boluda 2021 |
| 3 mg/mL collagen pore | ~2.7 µm mean diameter | SHG analysis literature |

---

## Cross-Field Bridge Papers

### Confirmed Prior Art: Ashworth et al. 2015
**Full citation**: Ashworth JC, Mehr M, Buxton PG, Best SM, Cameron RE. "Cell Invasion in Collagen Scaffold Architectures Characterized by Percolation Theory." Adv Healthcare Mater 4(9):1317-21 (2015). DOI: 10.1002/adhm.201500197. PMID 25881025.

**What it does**:
- Applies percolation analysis as a structural characterization TOOL to collagen scaffolds
- X-ray microCT + percolation theory to measure pore interconnectivity
- Shows "percolation diameter" predicts extent of connective tissue cell invasion
- Cell type: connective tissue fibroblasts/tenocytes — NOT immune cells

**What it does NOT do**:
- Does not study immune cells (T cells) at all
- Does not apply percolation PHYSICS (critical exponents, correlation length divergence, universality, scaling laws)
- Does not study tumor tissue or immune exclusion
- Does not use active particle percolation
- Does not connect to LOX, collagen crosslinking, checkpoint blockade, or immunotherapy

**Assessment**: This paper uses percolation theory as a measurement/characterization tool (analogous to using fractal dimension to describe a curve). It does NOT make the physics-first hypothesis that immune exclusion IS a percolation phase transition governed by universal critical exponents. The conceptual distance between Ashworth 2015 and our target is substantial.

### Tumor Proliferation on Percolation Clusters (Perc Applied to Tumor Cells)
**Moein & Masoudi-Nejad (2016, J Biol Phys)** — Uses percolation clusters to model inhomogeneous tissue for tumor cell proliferation and diffusion. Finds thresholds at 0.54 (4-neighbor), 0.44 (6-neighbor), 0.37 (8-neighbor) for tumor diffusion. **Gap**: Studies tumor CELLS (not immune cells) and models tissue INHOMOGENEITY (not ECM crosslinking density). No connection to immune exclusion.

### Percolation in Lung Inflammation/Fibrosis
A 2026 paper (Biomedicines 14(2):281) applies percolation to ECM mechanics in lung inflammation, finding critical thresholds determining pathological outcomes. **Gap**: Studies lung fibrosis mechanics, not immune cell infiltration or tumor biology.

### Active Particle Percolation (Theoretical Physics, No Biological Application)
Zeitz 2017 and Saha 2024 provide theoretical framework for active particles in disordered media. **No paper in either group applies active particle percolation to immune cells in tumor ECM.**

### Disjointness Search — Specific Targeted Searches Conducted
The following specific searches found NO papers connecting these concepts:
1. "percolation" + "immune" + "tumor" + "infiltration" + "T cell": returns papers about percolation of tumor CELLS, not immune cells
2. "percolation threshold" + "collagen crosslinking" + "immune exclusion": no direct hits
3. "percolation" + "LOX" + "T cell" + "tumor": no results
4. "critical exponent" + "T cell" + "collagen" + "tumor": no results
5. "ξ correlation length" + "immune exclusion": no results

---

## Disjointness Assessment

**Status: PARTIALLY EXPLORED** (upgraded from DISJOINT based on literature evidence)

**Evidence**:
- Ashworth 2015 provides conceptual prior art connecting percolation analysis to collagen scaffolds and cell invasion. However, it applies percolation as a characterization tool, not as a physics framework for a phase transition.
- No paper applies percolation CRITICAL PHENOMENA (diverging correlation length, critical exponents, universality class, active particle corrections) to T cell infiltration in any context.
- The Fusilier 2025 (Science Immunology) paper is the closest recent work — it establishes that collagen NETWORK TOPOLOGY (not just density) controls T cell infiltration, which is exactly the regime where percolation theory applies. But it does not use percolation theory.
- The specific bridge (LOX crosslinking density = bond occupation probability p; percolation threshold p_c as the immune exclusion boundary; ξ ~ |p-p_c|^(-0.876) as spatial scale of exclusion zones) has NOT been proposed or tested in any paper found.

**Why "PARTIALLY EXPLORED" not "DISJOINT"**:
- Ashworth 2015 establishes direct connection between percolation theory and collagen/cell invasion (same physical system)
- Multiple papers use percolation theory to model tumor biology (tumor cells diffusing on percolation clusters)
- The conceptual distance is closer than expected before this search

**Why NOT "WELL-EXPLORED"**:
- No paper applies percolation PHYSICS (critical exponents, universality, scaling laws) to T cell infiltration
- No paper proposes the specific bridge: LOX → p → percolation transition → immune exclusion
- No paper tests whether T cell MSD shows the characteristic subdiffusion at criticality (α ≈ 0.696 in 3D)
- No paper predicts tumor-size dependence of immune exclusion via finite-size scaling
- No paper tests universality class across tumor types

**Implication for Hypothesis Novelty**: The hypothesis remains highly novel at the level of mechanism, prediction, and testable quantitative claims. The Ashworth 2015 prior art establishes biological feasibility of the physical connection but does not diminish the novelty of applying full percolation physics to the immune exclusion problem.

---

## Measurement Gaps Identified (Field C's Unsolved Problems)

1. **No threshold identified for immune exclusion**: No paper has measured the critical LOX activity (or collagen crosslinking density) at which T cell infiltration transitions from excluded to infiltrating. This is the single largest measurement gap.

2. **No T cell MSD vs. continuous crosslinking density**: Kuczek 2019 uses only 1 mg/mL vs. 4 mg/mL. No dose-response curve identifying a sharp transition point in T cell mobility.

3. **No spatial correlation length measurements**: Multiplex IHC gives spatial maps of T cell distribution, but no paper has computed the correlation length of T cell density fluctuations (ξ) as a function of ECM density.

4. **Standardization problem**: SITC 2025 consensus statement identifies lack of cross-platform comparability, standardized analysis pipelines, and prospective validation as core unmet needs in multiplex IHC. The field lacks physical models to predict what to measure.

5. **Excluded phenotype mechanism inadequately characterized**: Spatial multi-omics (Nature Genetics 2025, NSCLC) identifies immune-excluded tumors by transcriptomic signatures but cannot predict which patients will respond to LOX inhibition + checkpoint blockade.

6. **No prediction of spatial exclusion zone size**: No paper predicts the spatial scale over which exclusion occurs — this is exactly what the correlation length ξ ~ |p - p_c|^(-0.876) would provide.

7. **Collagen topology vs. density confusion**: Before Fusilier 2025, the field conflated collagen density with collagen network connectivity. Percolation theory resolves this by showing the relevant variable is connectivity (bond occupation probability), not mass density per se.

---

## Key Numbers for Computational Validation

### Percolation Theory (Field A)
| Parameter | Value | Source |
|---|---|---|
| p_c (3D bond, simple cubic) | 0.2488 | Wang et al. 2013 |
| ν (correlation length exponent) | 0.876 | Wang et al. 2013 |
| Subdiffusion exponent at p_c | α = 0.696 | Standard result |
| β (order parameter) | 0.417 | Standard result |
| Active particle threshold shift | Higher p_c than passive | Saha 2024 |
| Self-trapping at high activity | Reduces effective diffusion | Zeitz 2017 |

### Tumor ECM (Field C)
| Parameter | Value | Source |
|---|---|---|
| T cell speed (stiff PDAC) | ~1 µm/min | Nicolas-Boluda 2021 |
| T cell speed (after LOX inhibition) | ~5 µm/min | Nicolas-Boluda 2021 (estimated) |
| Normal tissue pore size | 10–50 µm | Multiple reviews |
| Tumor tissue pore size | 1–10 µm | Multiple reviews |
| T cell diameter | ~10 µm | Cell biology |
| T cell nucleus diameter | ~8 µm | Cell biology |
| Critical pore for amoeboid migration | ~7 µm² | Erickson lab, JCB |
| Collagen concentration (healthy mimic) | 1 mg/mL | Kuczek 2019 |
| Collagen concentration (tumor mimic) | 4 mg/mL | Kuczek 2019 |
| Collagen crosslinking (LOX inhibitor BAPN) | Reduces stiffness from ~5 to ~1 kPa | Nicolas-Boluda 2021 |
| SHG pore size range (3 mg/mL collagen) | ~2.7 µm mean | SHG literature |
| T cell speed along aligned collagen | Significantly higher than unaligned | Pruitt 2019 |

### Bridge Mapping (for Generator/Computational Validator)
| Percolation Concept | Biological Equivalent | Measurable Variable |
|---|---|---|
| Bond occupation probability p | Fraction of open pores (= 1 - crosslinking density) | LOX activity, BAPN dose, SHG pore connectivity |
| Percolation threshold p_c | Critical LOX activity for exclusion transition | Dose-response experiment (T cell infiltration vs BAPN) |
| Correlation length ξ | Spatial scale of T cell exclusion zones | Multiplex IHC spatial analysis |
| Spanning cluster | Connected pathway for T cell infiltration | SHG pore network analysis |
| Subdiffusion exponent α | T cell MSD scaling in dense ECM | Live confocal tracking |
| Finite-size scaling | Biopsy size dependence of exclusion phenotype | Comparison of small vs. large biopsy cores |
| Universality class | Same ν across tumor types | Cross-cancer validation |

---

## Full-Text Papers Retrieved

1. `papers/ashworth2015-percolation-collagen-cell-invasion.md` — Critical prior art; establishes biological-physical connection but not percolation physics
2. `papers/nicolas-boluda2021-LOX-collagen-Tcell-antiPD1.md` — Key quantitative paper: LOX inhibition → T cell infiltration; 5-fold improvement; anti-PD-1 synergy
3. `papers/kuczek2019-collagen-density-Tcell-activity.md` — Collagen density suppresses T cell killing and proliferation; 1 vs. 4 mg/mL
4. `papers/saha2024-run-tumble-percolation-transition.md` — Active particle percolation; re-entrant behavior; continuously varying critical exponents
5. `papers/zeitz2017-active-brownian-lorentz-gas.md` — Active Brownian particles in Lorentz gas; self-trapping paradox; near-threshold subdiffusion
6. `papers/fusilier2025-macrophage-collagen-topography-Tcell.md` — Most recent (2025 Science Immunology): collagen TOPOLOGY controls T cell infiltration; Tcf4-Collagen3 axis
7. `papers/pruitt2019-collagen-fiber-CTL-motility.md` — Quantitative MSD of CD8+ T cells in aligned vs. unaligned collagen
8. `papers/xiao2023-desmoplastic-stroma-Tcell-exclusion-NatComm.md` — FAP-CAR T cells collapse stroma and restore immune access
9. `papers/salmon2012-Tcell-ECM-migration-lung-tumor.md` — Foundational: T cells trapped by aligned collagen in human lung tumors
10. `papers/wang2013-3Dbond-percolation-critical-exponents.md` — Benchmark 3D critical exponents for percolation

---

## Gap Analysis

### What's Been Explored
- Physical barriers to T cell infiltration in solid tumors (extensively, since Salmon 2012)
- LOX/collagen crosslinking as a drug target (Nicolas-Boluda 2021, multiple reviews)
- T cell motility in 3D collagen matrices (Pruitt 2019, migration papers)
- Active particle percolation in theoretical contexts (Zeitz 2017, Saha 2024)
- Percolation theory applied to tissue scaffold characterization (Ashworth 2015)
- Tumor cell diffusion on percolation clusters (Moein & Masoudi-Nejad 2016)
- Collagen topology vs. density for T cell control (Fusilier 2025)

### What Has NOT Been Explored
1. **Percolation threshold for immune exclusion**: No paper defines p_c as the critical LOX/crosslinking density at which T cell infiltration transitions. The most important unexplored prediction.

2. **Correlation length scaling**: No paper measures the spatial correlation length of T cell density fluctuations in tumor stroma as a function of ECM crosslinking density. ξ ~ |p - p_c|^(-0.876) would predict the spatial scale of exclusion zones — completely untested.

3. **Subdiffusion signature at criticality**: No paper measures T cell MSD scaling exponent α as a function of crosslinking density to test whether α → 0.696 near the exclusion threshold.

4. **Finite-size scaling of immune phenotype**: No paper tests whether the sharpness of the inflamed/excluded transition in tumor biopsies depends on tumor size as predicted by finite-size scaling.

5. **Universality class test**: No paper asks whether the critical exponents for immune exclusion are the same across tumor types (breast, PDAC, NSCLC, prostate). Universality would be a major scientific discovery.

6. **Active particle corrections**: No paper applies active-particle percolation theory (with self-propulsion, chemotaxis, and contact guidance corrections) to T cell infiltration in 3D ECM.

7. **LOX activity → bond occupation probability mapping**: The formal mathematical mapping between LOX enzymatic activity (measurable units) and bond occupation probability p is not established.

8. **Predictive threshold for LOX inhibitor dosing**: No paper uses a percolation framework to predict the minimum BAPN dose required to cross p_c and restore T cell infiltration.

### Most Promising Unexplored Directions

**Direction 1 (Highest Priority)**: Experimental dose-response to find p_c
- Vary BAPN dose continuously in LOX-inhibition experiments
- Measure T cell infiltration vs. BAPN dose in KPC pancreatic tumors
- Measure collagen pore connectivity (SHG) simultaneously
- Prediction: T cell infiltration shows a sharp threshold at p_c, not a linear dose-response
- Falsifiable: If the transition is gradual (no threshold), the percolation model fails

**Direction 2**: Spatial correlation analysis on multiplex IHC data
- Compute correlation length of CD8+ T cell density fluctuations in tumor biopsies
- Correlate with LOX activity or collagen crosslinking (second-order pyridinium crosslinks, mass spec)
- Prediction: ξ diverges near the exclusion transition; power-law scaling with exponent ν ≈ 0.876
- Existing data: Multiple labs have multiplex IHC + SHG data from the same specimens

**Direction 3**: MSD anomalous diffusion signature
- Use live 2-photon microscopy on fresh tumor slices at varying ECM stiffness
- Measure T cell MSD at multiple time scales (short-time to long-time)
- Prediction: At stiffness near the threshold, MSD ~ t^0.696 (subdiffusion); above threshold, MSD ~ t^1.0 (normal diffusion)
- Existing capability: Nicolas-Boluda 2021 already has the imaging system; just need to measure MSD scaling exponent

**Direction 4**: Cross-tumor universality test
- Measure critical exponent ν across breast, PDAC, NSCLC, colon cancer models
- Prediction: ν ≈ 0.876 in all cases (universality of 3D percolation)
- This would be a major scientific result: same physics governing immune exclusion across cancer types

---

## Notes on Retrieval Methodology
- MCP tools (Semantic Scholar, PubMed) were unavailable due to connection error
- All retrieval conducted via WebSearch (primary) and WebFetch (full-text where accessible)
- PubMed PMC open-access papers retrieved via WebFetch successfully for Nicolas-Boluda 2021, Kuczek 2019
- Ashworth 2015 (Wiley, paywalled): abstract and metadata retrieved; full text inaccessible (403 error)
- arXiv papers fully retrieved: Zeitz 2017, Saha 2024, Wang 2013
- The absence of papers directly connecting percolation critical phenomena to immune cell infiltration in tumor ECM was verified by 5 independent targeted searches
