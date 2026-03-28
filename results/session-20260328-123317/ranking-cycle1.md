# Ranking — Session 015, Cycle 1

**Session**: session-20260328-123317
**Target**: Percolation Threshold Theory x T Cell Infiltration in Solid Tumors
**Date**: 2026-03-28
**Ranker**: Hypothesis Ranker v5.2
**Input**: 7 surviving hypotheses (H1, H2, H3, H4, H5, H7, H8); H6 KILLED by Critic

---

## Dimension Weights

| Dimension | Weight |
|-----------|--------|
| Novelty | 15% |
| Testability | 20% |
| Mechanistic Specificity | 20% |
| Groundedness | 20% |
| Impact: Paradigm | 5% |
| Impact: Translational | 5% |
| Cross-domain Creativity | 15% |
| Total | 100% |

Cross-domain creativity bonus of +0.5 applied to all hypotheses bridging 2+ disciplinary boundaries. All seven surviving hypotheses bridge statistical mechanics / physics to tumor immunology / clinical oncology, qualifying each for the bonus.

---

## Per-Hypothesis Scoring Tables

---

### H1: LOX Crosslink Density as Bond Occupation Probability Predicts a Universal Immune Exclusion Threshold at p ~ 0.21-0.25

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | The Critic's 20+ web searches found zero papers applying percolation critical phenomena to T cell infiltration or immune exclusion. Ashworth 2015 is adjacent (percolation in collagen scaffolds for tissue engineering) but restricted to fibroblasts. The four-way differentiation from Ashworth — tumor immunology context, active particle formalism, full critical phenomena, LOX as molecular actuator — is explicitly novel and verified by targeted searches. |
| Testability | 20% | 7 | The BAPN titration experiment (0-3 mg/mL, 6 dose points, MSD measurement in ex vivo tumor slices) is well-specified and uses existing reagents established by Nicolas-Boluda 2021. The key discriminating measurement — MSD exponent alpha transitioning from 1.0 to 0.53 — requires single-cell tracking with established imaging; feasible but requires specialized equipment and careful exponent fitting to distinguish from simpler threshold models. |
| Mechanistic Specificity | 20% | 8 | Names specific molecules (LOX, BAPN), specific equations (p_c = 0.2488, Pe ~ 3, alpha = 0.53 at p_c), specific lattice parameters, and specific BAPN concentrations. The four-component mechanistic chain (LOX crosslinks collagen → pore constriction below 3 um → bond closure → p falls below p_c) is well-articulated. Penalized one point for the PARAMETRIC gap in the LOX-to-p mapping function and for the unvalidated 3D active-particle correction (p_c(active) range 0.21-0.24 flagged SPECULATIVE by Critic). |
| Groundedness | 20% | 6 | Core citations verified: Wang 2013 PRE (p_c = 0.2488), Nicolas-Boluda 2021 eLife, PMID 38267662 (LOXL1 restricts CD8+ T cells), Ashworth 2015. Zero citation hallucinations. Two key bridge claims are PARAMETRIC: the LOX crosslink density to open pore fraction mapping has never been quantified, and the 3D active particle percolation threshold at Pe ~ 3 has no published calculation (Saha 2024 is 2D only). Approximately 55-60% of mechanism claims are grounded; remainder are parametric or speculative. |
| Impact: Paradigm | 5% | 7 | If validated, this hypothesis reframes immune exclusion as a physical phase transition with specific, parameter-free exponents — a conceptual shift from descriptive hot/cold tumor classification to quantitative statistical mechanics. It would establish a new research program rather than merely extending existing immunology frameworks. |
| Impact: Translational | 5% | 7 | The percolation model directly predicts a therapeutic window for LOX inhibitor dosing — actionable for combination immunotherapy trials. Nicolas-Boluda 2021 showed LOX inhibition improves anti-PD-1 efficacy; this provides the quantitative dosing rationale. Penalized for BAPN failing to improve tumor control in 4/5 models (Nicolas-Boluda 2021) and Simtuzumab Phase 2 failure. |
| Cross-domain Creativity | 15% | 9 | Bridges statistical mechanics (bond percolation, universality classes, critical exponents) to tumor immunology (ECM-mediated immune exclusion) to clinical oncology (immunotherapy dosing), with soft matter physics (Pe number, Brownian particle dynamics) as a fourth disciplinary layer. The structural mapping of LOX activity to the physical control parameter p is inventive and precise. |
| **Composite (before bonus)** | | **7.60** | 0.15x9 + 0.20x7 + 0.20x8 + 0.20x6 + 0.05x7 + 0.05x7 + 0.15x9 = 1.35 + 1.40 + 1.60 + 1.20 + 0.35 + 0.35 + 1.35 = 7.60 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics → soft matter physics → tumor immunology → clinical oncology: 3+ disciplinary boundaries. |
| **Composite (final)** | | **8.10** | |

---

### H2: Correlation Length Exponent nu = 0.88 Predicts T Cell Cluster Size Distribution Near the Hot-Cold Tumor Boundary

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | Critic search "T cell cluster size distribution power law tumor" returned no papers analyzing T cell spatial distributions through a percolation lens. Search "spatial statistics T cell tumor immunohistochemistry cluster" returned papers using Ripley's K function but none testing percolation scaling predictions. The parameter-free exponent prediction tau ~ 2.19 from Fisher's hyperscaling relation has never been proposed for immune cell distributions. |
| Testability | 20% | 7 | Testable in existing spatial transcriptomics datasets (Visium, MERFISH) without new experiments — a significant practical advantage. The Critic confirms feasibility but flags statistical demands: requires tumors near the hot-cold boundary, large cluster statistics, and correction for finite-size effects. Distinguishing tau = 2.19 from nearby values requires large cohorts near the transition. The lattice constant ambiguity (a ~ 2 um vs 5 um) introduces factor-of-5 uncertainty in xi values but does not affect the tau exponent prediction itself. |
| Mechanistic Specificity | 20% | 7 | Names specific mathematical relationships: xi ~ |p - p_c|^(-0.876), tau = 1 + d/d_f = 2.19 (verified independently by Critic via hyperscaling), d_f = 2.52-2.54. Xi values at three distances from p_c explicitly calculated. Penalized for the factor-of-2 numerical error in xi(0.1%) (correct value ~850 um, not 430 um as stated) and for the ambiguous lattice constant. The biological mapping from T cell cluster sizes to ECM connectivity clusters is the main mechanistic gap. |
| Groundedness | 20% | 6 | Percolation exponents (nu = 0.876, d_f = 2.52-2.54, tau ~ 2.19) rigorously verified by Wang 2013 and confirmed by the Critic's independent calculation. Multiple published spatial transcriptomics datasets of tumor-infiltrating T cells exist. However, the key predictive bridge — that T cell cluster size distribution will track ECM connectivity cluster statistics — is entirely PARAMETRIC. The factor-of-2 numerical error in xi(0.1%) also penalizes grounding. Approximately 50% of mechanism claims grounded. |
| Impact: Paradigm | 5% | 6 | Confirmation of tau ~ 2.19 in spatial transcriptomics data would establish a quantitative link between ECM physics and T cell spatial patterning and provide a physical explanation for hot/cold tumor boundary sharpness. This substantially extends the existing framework without opening a fully new field. |
| Impact: Translational | 5% | 5 | A confirmed tau exponent from biopsy spatial data could serve as a novel biomarker for tumor proximity to the immune exclusion threshold. The application pathway is real but several steps removed from clinical utility, and the measurement procedure is technically demanding with existing pathology infrastructure. |
| Cross-domain Creativity | 15% | 8 | Bridges 3D statistical mechanics (percolation scaling, fractal cluster geometry) to spatial tumor immunology (T cell spatial distributions from transcriptomics) to digital pathology (cluster size analysis from IHC). The specific use of Fisher's hyperscaling exponent as a pathological measurement target is a creative and original transfer. |
| **Composite (before bonus)** | | **7.10** | 0.15x9 + 0.20x7 + 0.20x7 + 0.20x6 + 0.05x6 + 0.05x5 + 0.15x8 = 1.35 + 1.40 + 1.40 + 1.20 + 0.30 + 0.25 + 1.20 = 7.10 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics → spatial transcriptomics / digital pathology → tumor immunology: 2+ disciplinary boundaries. |
| **Composite (final)** | | **7.60** | |

---

### H3: Finite-Size Scaling of T Cell MSD Explains Discordant Infiltration Scores Between Core Biopsies and Resection Specimens

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 8 | Critic search "finite-size scaling biopsy immunoscore discordance" returned no results. No paper has applied finite-size scaling from statistical physics to clinical biopsy sampling artifacts. Biopsy-resection discordance is actively studied but always framed in terms of biological heterogeneity, never physical scaling laws. The specific inverted-U variance profile prediction with peak width determined by L^(-1/nu) is original. |
| Testability | 20% | 7 | The inverted-U variance prediction is testable in existing paired biopsy-resection immunoscoring datasets available for gastric, breast, and lung cancers. Comparing 18-gauge vs 14-gauge biopsy variance is feasible with existing collections. However, the unique percolation discriminator (L^(-1/nu) scaling) requires biopsies of varying sizes from the same tumor — not standard practice. The 2024 gastric cancer study found discordance in 60% of tumors overall without preferential enrichment at intermediate scores, partially undermining the hypothesis. |
| Mechanistic Specificity | 20% | 6 | Names the specific scaling relationship (Delta_p ~ L^(-1/nu), nu = 0.876) and provides numerical predictions. However, the Critic identified a factor-of-4 error in the sharpness ratio (~76x, not ~20x as stated) and a factor-of-5 error in the resection Delta_p value. These errors indicate approximate computation. The lattice constant is PARAMETRIC and undefined, making quantitative numerical predictions unreliable. |
| Groundedness | 20% | 5 | Finite-size scaling theory is exact (standard statistical mechanics). Clinical biopsy-resection discordance is well-documented (2024 gastric study: 60% discordant, verified by Critic). However, the connection — that discordance follows the L^(-1/nu) percolation scaling law — is entirely PARAMETRIC. No component of the bridge mechanism has been tested. The dominant source of discordance is likely biological heterogeneity (MHC-I, PD-L1, antigen density), not ECM topology. Approximately 35-40% of claims grounded. |
| Impact: Paradigm | 5% | 5 | If validated, this would provide the first physical model for a well-known clinical problem (biopsy sampling error), establishing that sampling artifacts scale quantitatively with proximity to a phase transition. Interesting conceptual contribution but does not overturn an established paradigm. |
| Impact: Translational | 5% | 7 | A practical prediction about when immunoscoring is reliable vs. unreliable has immediate clinical value for patient stratification in immunotherapy trials. The inverted-U variance prediction could guide biopsy protocol selection without requiring new molecular assays. |
| Cross-domain Creativity | 15% | 7 | Bridges statistical mechanics (finite-size scaling) to clinical oncology (biopsy protocol design) through tumor immunology (immunoscoring discordance). The transfer of a theoretical physics concept to a clinical sampling problem is creative, though the biological mechanism is less elaborated than other hypotheses — finite-size scaling is used more as a structural analogy here. |
| **Composite (before bonus)** | | **6.45** | 0.15x8 + 0.20x7 + 0.20x6 + 0.20x5 + 0.05x5 + 0.05x7 + 0.15x7 = 1.20 + 1.40 + 1.20 + 1.00 + 0.25 + 0.35 + 1.05 = 6.45 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics → clinical pathology / biopsy design → tumor immunology: 2+ disciplinary boundaries. |
| **Composite (final)** | | **6.95** | |

---

### H4: Collagen I/III Ratio Acts as a Lattice Topology Switch That Shifts p_c, Explaining Why Macrophage Depletion Converts Cold to Hot Tumors

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | Critic search "collagen I III ratio percolation threshold" returned no results. Fusilier 2025 (Science Immunology) established the macrophage-Tcf4-collagen I/III switching mechanism but provided no quantitative framework. No paper has proposed that collagen types I and III represent different percolation lattice topologies with different p_c values but identical universality-class exponents. The reframing of macrophage depletion as a lattice topology switch is genuinely original. |
| Testability | 20% | 8 | Well-specified experimental design: compare T cell MSD in ex vivo slices from macrophage-depleted (Col III-enriched) vs. control (Col I-dominated) tumors at matched total collagen density. SHG imaging can distinguish collagen fiber types and quantify alignment. The key prediction — identical critical exponents at different absolute p_c values — is the strongest discriminator against simpler models. Completable in 12-18 months using existing mouse tumor models. Received an ADVANCE verdict (no kill pattern match) from the Critic. |
| Mechanistic Specificity | 20% | 7 | Names specific molecules (Tcf4, collagen I, collagen III, macrophages), specific biological process (Fusilier 2025 macrophage-Tcf4 axis), specific topological distinction (anisotropic quasi-1D vs. isotropic 3D lattice), and specific percolation parameters (p_c range 0.2-0.25 for Col III, 0.35-0.45 for Col I, with identical nu and beta). The p_c values are PARAMETRIC (no published computation for these lattice types). The hypothesis does not fully address the directed percolation complication flagged by the Critic for strongly aligned collagen I networks. |
| Groundedness | 20% | 7 | Fusilier 2025 directly confirms macrophage suppression of Tcf4-driven collagen III deposition (verified by Critic). Percolation universality (same exponents, different p_c for different lattice topologies) is an exact mathematical result (Wang 2013). STRING interactions LOX-COL3A1 (0.843) and LOX-COL1A1 (0.808) verified. The molecular bridge maps precisely onto a 2025 experimental finding. Only the specific p_c values and the applicability to real mixed heterotypic collagen fibers are PARAMETRIC. Approximately 65-70% of claims grounded. |
| Impact: Paradigm | 5% | 7 | Provides a physical mechanism for why macrophage depletion sometimes converts cold tumors to hot — reframing variable CSF1R inhibitor efficacy as a quantitative topological phase transition. This is a meaningful paradigm shift within tumor microenvironment biology. |
| Impact: Translational | 5% | 7 | Macrophage-targeting therapies (CSF1R inhibitors) are in clinical trials with variable efficacy. The p_c topology model predicts a patient stratification strategy: measure Col I/III ratio to assess which patients are near the new, lower p_c after macrophage depletion. Practical, actionable clinical hypothesis with currently available therapeutic agents. |
| Cross-domain Creativity | 15% | 9 | Bridges percolation theory on anisotropic lattices (statistical mechanics) to collagen fiber biology (biophysics / matrix biology) to macrophage-mediated ECM regulation (immunology / cell biology) to clinical macrophage-targeting therapy response prediction (clinical oncology). The structural mapping — different collagen types as different lattice topologies — is a deep and specific cross-domain insight grounded in a 2025 experimental system. |
| **Composite (before bonus)** | | **7.80** | 0.15x9 + 0.20x8 + 0.20x7 + 0.20x7 + 0.05x7 + 0.05x7 + 0.15x9 = 1.35 + 1.60 + 1.40 + 1.40 + 0.35 + 0.35 + 1.35 = 7.80 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics → matrix biology / biophysics → immunology → clinical oncology: 3+ disciplinary boundaries. |
| **Composite (final)** | | **8.30** | |

---

### H5: LOX Inhibitor Dose-Response Follows the Order Parameter Scaling P_inf ~ (p - p_c)^0.417, Enabling Therapeutic Window Prediction

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | Critic search "LOX inhibitor percolation dose response" returned no results. No published study has proposed that drug dose-response should follow a percolation order parameter scaling law rather than a sigmoid Hill equation. The prediction of a specific parameter-free power-law exponent (beta = 0.417) for the dose-response curve is a new application of critical phenomena to pharmacology. The framing of a therapeutic window as Delta_p ~ 0.05 above p_c is a novel conceptual contribution to LOX inhibitor trial design. |
| Testability | 20% | 6 | Feasible in principle (titrated BAPN experiment, 6-8 dose points with independent p measurement via confocal/SHG at each dose). However, two major analytical challenges were identified by the Critic: (1) BAPN dose-to-p mapping is nonlinear and saturating (PMID 2354637), potentially obscuring the power-law signature in dose space; (2) distinguishing P_inf ~ (p - p_c)^0.417 from a Hill equation with n ~ 4 requires approximately 2 decades of response data. The hypothesis requires independent p measurement — technically demanding. Feasible within 2 years but analytically ambitious. |
| Mechanistic Specificity | 20% | 7 | Names specific molecules (LOX, BAPN, LOX-IN-3), specific parameter values (beta = 0.417, dose range 0-3 mg/mL), specific predictions (threshold dose below which no improvement, power-law above threshold with exponent 0.417, not 1.0 linear or 0.5 diffusion-limited). The mapping from inhibitor dose to effective p is acknowledged as PARAMETRIC, which is the main specificity gap. The pharmacological therapeutic window argument is well-articulated. |
| Groundedness | 20% | 6 | Beta = 0.417 is exact (Wang 2013, verified). Nicolas-Boluda 2021 eLife (BAPN improves T cell displacement; one dose only, verified). PMID 39101793 (LOX-IN-3 enhances T cell infiltration in cholangiocarcinoma, verified). The fundamental problem: the dose-to-p mapping is unknown and BAPN kinetics are saturating, meaning the grounded half (beta = 0.417 in p-space) may be unobservable in dose space. The BAPN bone dose-response (PMID 2354637, saturating) undermines observability. Approximately 50% of operationally relevant claims grounded. |
| Impact: Paradigm | 5% | 6 | If validated, this would establish that percolation scaling governs pharmacological response in matrix-targeting therapies — a new principle potentially applicable beyond LOX inhibitors to any drug targeting a threshold-dependent physical property of the ECM. This extends existing pharmacology rather than replacing a paradigm. |
| Impact: Translational | 5% | 8 | The therapeutic window prediction is highly translatable: if percolation scaling governs LOX inhibitor response, sub-maximal dosing near p_c is optimal, reducing normal-tissue toxicity. LOX inhibitor + immunotherapy combinations are currently being designed (newer selective inhibitors post-Simtuzumab failure), making this immediately relevant to trial design. |
| Cross-domain Creativity | 15% | 8 | Bridges statistical mechanics (order parameter scaling, beta exponent) to pharmacology (dose-response modeling, therapeutic window) to tumor immunology (LOX-collagen-T cell axis) to clinical trial design. The translation of a physics order parameter into a pharmacodynamic response curve is creative and specific. |
| **Composite (before bonus)** | | **7.05** | 0.15x9 + 0.20x6 + 0.20x7 + 0.20x6 + 0.05x6 + 0.05x8 + 0.15x8 = 1.35 + 1.20 + 1.40 + 1.20 + 0.30 + 0.40 + 1.20 = 7.05 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics → pharmacology → tumor immunology → clinical trial design: 3+ disciplinary boundaries. |
| **Composite (final)** | | **7.55** | |

---

### H7: Universality Class Critical Exponents Are Tumor-Type-Invariant, Enabling a Single Percolation Model Across PDAC, Breast, and Lung Cancers

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | Critic search "universality critical exponents tumor immune exclusion" returned no results. No paper has proposed that a single percolation model with universal exponents could predict T cell infiltration across tumor types. The pan-cancer universality prediction — nu = 0.876 +/- 0.01 regardless of tumor type — is a falsifiable, genuinely original hypothesis. The Harris criterion analysis (refined by the Critic to show exponential correlations preserve universality) adds mathematical depth absent from existing literature. |
| Testability | 20% | 5 | In principle testable by measuring MSD exponents at the respective p_c values across PDAC, breast, and lung cancers. However, the Critic identified a major practical barrier: most tumors are likely far from the critical point, making scaling predictions unmeasurable unless patients near the hot-cold boundary are specifically selected. Cost and logistics make this a 3-5 year project, substantially above the 2-year feasibility threshold. Testable in principle but practically demanding. |
| Mechanistic Specificity | 20% | 7 | Names specific exponents (nu = 0.876, beta = 0.417, d_f = 2.53, alpha = 0.53 at p_c in 3D — the Critic corrected the source text's alpha = 0.70 to 0.53, which is the correct 3D value). Specifies three distinct tumor types with expected ECM architecture differences. The prediction structure (same exponents at different p_c values) is mechanistically precise. Penalized for the uncorrected alpha error in the source text and the directed percolation complication for strongly aligned PDAC fibers. |
| Groundedness | 20% | 6 | Universality of 3D percolation exponents is mathematically exact (Wang 2013, verified). ECM architecture variation across tumor types is verified (Salmon 2012, Kuczek 2019, Xiao 2023, all verified by Critic). Harris criterion correctly applied after Critic's correction. However, the application of universality to real tumor ECM with correlated disorder, fiber alignment, and finite boundaries is entirely PARAMETRIC. The alpha = 0.70 error (should be 0.53) also penalizes grounding. Approximately 50-55% of claims grounded. |
| Impact: Paradigm | 5% | 8 | This is the highest paradigm-impact hypothesis in the batch: if validated, it would establish that a single parameter-free physical model predicts immune infiltration across all solid tumor types — a major conceptual unification of tumor immunology under statistical mechanics. The shift from tumor-type-specific empirical immunoscoring to physics-based universal prediction is substantial. |
| Impact: Translational | 5% | 6 | A validated pan-cancer percolation model would enable prediction of anti-PD-1 response from a single physical measurement rather than genomic profiling. The translational pathway is real but long — science must first be validated across three tumor types before clinical application. |
| Cross-domain Creativity | 15% | 9 | Bridges universal theoretical physics (renormalization group, universality classes, fixed points) to pan-cancer tumor biology to clinical precision oncology. The hypothesis imports one of the deepest results in theoretical physics and asks whether it applies across the entire cancer landscape, connecting the mathematical physics of phase transitions to the messy biology of distinct cancer types. |
| **Composite (before bonus)** | | **7.00** | 0.15x9 + 0.20x5 + 0.20x7 + 0.20x6 + 0.05x8 + 0.05x6 + 0.15x9 = 1.35 + 1.00 + 1.40 + 1.20 + 0.40 + 0.30 + 1.35 = 7.00 |
| Cross-domain bonus applied | | +0.5 | Theoretical physics (renormalization group) → pan-cancer biology → clinical precision oncology: 3+ disciplinary boundaries. |
| **Composite (final)** | | **7.50** | |

---

### H8: TGF-beta Autocrine Signaling Constitutes "Bond-Correlated Percolation" That Shifts p_c and Explains Non-Linear LOX Inhibitor + Anti-TGF-beta Synergy

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 9 | Critic search "correlated percolation TGF-beta LOX collagen tumor" returned no results. LOX inhibitor + anti-TGF-beta combination trials exist but synergy is analyzed only by standard pharmacological models (Bliss independence, Loewe additivity). No paper has proposed a percolation-based mechanism for this synergy through threshold de-correlation. The mapping of the TGF-beta positive feedback loop to bond-correlated percolation is a specific insight with no prior art. |
| Testability | 20% | 8 | The experimental design is one of the best in the batch, explicitly noted as such by the Critic: a 3D collagen gel with embedded CAFs and T cells, testing BAPN alone, galunisertib alone, and combination, with SHG imaging of crosslink spatial autocorrelation as the mechanistic discriminator. This design uniquely distinguishes the percolation synergy mechanism from immunological synergy — if anti-TGF-beta de-correlates the spatial crosslink pattern without changing total density, the percolation mechanism is supported. Received ADVANCE verdict (no kill pattern match). Feasible within 18 months. |
| Mechanistic Specificity | 20% | 8 | Names specific molecules (TGF-beta, LOX, SMAD4/FOXO1, alpha-v-beta-6 integrin, CAFs, galunisertib, fresolimumab, BAPN), specific STRING interaction score (LOX-TGFB1 = 0.623), specific pathway (TGF-beta → LOX upregulation in CAFs → correlated bond closure), specific percolation prediction (simultaneous p increase via LOX inhibition and p_c decrease via TGF-beta de-correlation). The directional prediction (positive bond correlations raise p_c for bond percolation) was verified by a 2025 ScienceDirect paper. The effective TGF-beta signaling range (~50-100 um paracrine, ~10-20 um via integrin contact) is PARAMETRIC. |
| Groundedness | 20% | 7 | TGF-beta activates LOX in fibrosis (Cancer Research 2013, STRING LOX-TGFB1 = 0.623, both verified). High-density collagen activates TGF-beta in T cells via SMAD4/FOXO1 (Kuczek 2019 JITC, verified). Positive bond correlations raise p_c for bond percolation (verified by 2025 ScienceDirect paper). Alpha-v-beta-6 integrin activates latent TGF-beta (verified). Each step of the mechanistic chain is supported by independent literature. Only the super-additive synergy prediction and the effective TGF-beta correlation range are PARAMETRIC. Approximately 70% of claims grounded — highest in the batch. |
| Impact: Paradigm | 5% | 6 | Reframes drug synergy from independent pathway combination to threshold de-correlation — a conceptually distinct mechanism providing a physical explanation for non-additive drug effects that currently lack mechanistic interpretation in standard pharmacology. The paradigm shift is genuine but scoped to combination therapy modeling. |
| Impact: Translational | 5% | 8 | LOX inhibitor + TGF-beta pathway combinations are actively being explored in multiple tumor types. The percolation synergy model would guide combination design: moderate doses of both drugs (bringing the system above the de-correlated p_c) should outperform high doses of either alone. Multiple targeted agents are available (galunisertib, fresolimumab for TGF-beta; BAPN, LOX-IN-3 for LOX), reducing time to translation. |
| Cross-domain Creativity | 15% | 9 | Bridges correlated percolation theory (statistical mechanics) to TGF-beta-LOX signaling feedback biology (cell biology / fibrosis) to combination pharmacology (percolation-based synergy prediction) to clinical oncology (trial design for LOX inhibitor + anti-TGF-beta). The structural mapping — a positive feedback loop as spatially correlated bond closure — is mathematically precise and biologically grounded, combining theoretical physics, molecular biology, matrix biology, and pharmacology in a single coherent framework. |
| **Composite (before bonus)** | | **8.00** | 0.15x9 + 0.20x8 + 0.20x8 + 0.20x7 + 0.05x6 + 0.05x8 + 0.15x9 = 1.35 + 1.60 + 1.60 + 1.40 + 0.30 + 0.40 + 1.35 = 8.00 |
| Cross-domain bonus applied | | +0.5 | Statistical mechanics (correlated percolation) → molecular cell biology → pharmacology → clinical oncology: 3+ disciplinary boundaries. |
| **Composite (final)** | | **8.50** | |

---

## Summary Scoring Table

| Hypothesis | Novelty (15%) | Testability (20%) | Mech Spec (20%) | Groundedness (20%) | Paradigm (5%) | Translational (5%) | Creativity (15%) | Pre-bonus | Bonus | Composite |
|---|---|---|---|---|---|---|---|---|---|---|
| H8 | 9 | 8 | 8 | 7 | 6 | 8 | 9 | 8.00 | +0.5 | **8.50** |
| H4 | 9 | 8 | 7 | 7 | 7 | 7 | 9 | 7.80 | +0.5 | **8.30** |
| H1 | 9 | 7 | 8 | 6 | 7 | 7 | 9 | 7.60 | +0.5 | **8.10** |
| H2 | 9 | 7 | 7 | 6 | 6 | 5 | 8 | 7.10 | +0.5 | **7.60** |
| H5 | 9 | 6 | 7 | 6 | 6 | 8 | 8 | 7.05 | +0.5 | **7.55** |
| H7 | 9 | 5 | 7 | 6 | 8 | 6 | 9 | 7.00 | +0.5 | **7.50** |
| H3 | 8 | 7 | 6 | 5 | 5 | 7 | 7 | 6.45 | +0.5 | **6.95** |

---

## Ranked List (with diversity check)

1. **H8** — TGF-beta Autocrine Signaling as Bond-Correlated Percolation — Composite: **8.50**
   Bridge mechanism: Correlated percolation / TGF-beta-LOX positive feedback as spatially correlated bond closure

2. **H4** — Collagen I/III Ratio as Lattice Topology Switch — Composite: **8.30**
   Bridge mechanism: Lattice topology modulation of p_c / macrophage-Tcf4-collagen axis

3. **H1** — LOX Crosslink Density as Bond Occupation Probability — Composite: **8.10**
   Bridge mechanism: Bond occupation probability threshold crossing / LOX as molecular actuator of p

4. **H2** — Correlation Length Exponent Predicts T Cell Cluster Size Distribution — Composite: **7.60**
   Bridge mechanism: Correlation length scaling / spatial cluster statistics in transcriptomics

5. **H5** — LOX Inhibitor Dose-Response Follows Order Parameter Scaling — Composite: **7.55**
   Bridge mechanism: Order parameter scaling / pharmacological therapeutic window

6. **H7** — Universality Class Exponents Are Tumor-Type-Invariant — Composite: **7.50**
   Bridge mechanism: Universality / pan-cancer critical exponent invariance

7. **H3** — Finite-Size Scaling Explains Biopsy-Resection Discordance — Composite: **6.95**
   Bridge mechanism: Finite-size scaling / clinical sampling artifact

---

## Diversity Check

Requirement: at least 3 distinct bridge mechanisms in top-5; no two adjacent-ranked hypotheses share the same primary bridge mechanism.

Top-5 bridge mechanisms:
1. H8 — Correlated percolation / TGF-beta-LOX positive feedback
2. H4 — Lattice topology modulation (collagen fiber type as lattice geometry)
3. H1 — Bond occupation probability threshold crossing (LOX as actuator of p)
4. H2 — Correlation length scaling (spatial cluster size statistics)
5. H5 — Order parameter scaling (pharmacological dose-response)

Adjacent-pair check:
- H8 (correlated percolation) vs H4 (lattice topology): DISTINCT — one changes p_c via spatial correlations, the other changes p_c via geometric anisotropy
- H4 (lattice topology) vs H1 (bond occupation threshold): DISTINCT — one varies lattice structure, the other varies p at fixed structure
- H1 (bond occupation threshold) vs H2 (correlation length): DISTINCT — one predicts the threshold crossing, the other predicts spatial cluster statistics near the threshold
- H2 (correlation length) vs H5 (order parameter): DISTINCT — one predicts spatial cluster distributions, the other predicts the macroscopic order parameter dose-response

Distinct mechanism count in top-5: 5 of 5. Well above minimum of 3.

**Verdict: PASS** — full diversity across all five top-ranked hypotheses. No reordering required.

---

## Elo Tournament Sanity Check (Top-6 Pairwise)

Top-6 hypotheses entered: H8, H4, H1, H2, H5, H7. H3 (#7) excluded from tournament.

All 15 pairwise comparisons (N*(N-1)/2 = 15 for N=6):

| Match | Winner | Reasoning |
|-------|--------|-----------|
| H8 vs H4 | H8 | H8's SHG spatial autocorrelation readout can specifically isolate the percolation mechanism from immunological synergy; H4's experiment cannot cleanly separate topological from biochemical collagen effects (integrin binding confound flagged by Critic). H8's experimental discriminator is mechanistically tighter. |
| H8 vs H1 | H8 | H8's mechanistic chain has approximately 70% of claims grounded with multiple independent literature confirmations, vs H1's approximately 55-60% where the core LOX-to-p mapping is the critical unverified step. H8's experimental design provides a unique structural readout; H1 requires independent p measurement at each dose. |
| H8 vs H2 | H8 | H8 makes a mechanistically richer prediction with clearer experimental discrimination; H2's tau ~ 2.19 prediction is non-unique (multiple mechanisms generate power-law distributions), making positive results in existing datasets harder to interpret. H8 wins on specificity and interpretability. |
| H8 vs H5 | H8 | H8 has clearly superior testability (8 vs 6): its experimental design mechanistically discriminates the percolation mechanism from immunological alternatives. H5 faces the unresolved nonlinear dose-to-p mapping problem that may make the beta = 0.417 exponent unobservable in practice. |
| H8 vs H7 | H8 | H8 is testable within 18 months in a focused 3D gel system; H7 requires finding tumors near their respective critical points across three tumor types, a 3-5 year undertaking. H7 has higher paradigm impact (8 vs 6) but practical testability drives the first-choice preference for a domain researcher. |
| H4 vs H1 | H4 | H4 is directly grounded in Fusilier 2025 (Science Immunology), which provides the exact biological substrate for the proposed percolation mapping; H1's core assumption (LOX crosslink density maps inversely to open pore fraction) lacks equivalent direct experimental support. |
| H4 vs H2 | H4 | H4's experimental design is more controlled (matched total collagen density, variable fiber type, compare MSD transition positions); H2's test depends on finding tumors precisely at the hot-cold boundary in existing uncontrolled datasets. |
| H4 vs H5 | H4 | H4 has higher Testability (8 vs 6) and Groundedness (7 vs 6); H5 faces the saturating BAPN kinetics barrier that may make the power-law signature undetectable in dose space. H4 has no analogous practical obstruction. |
| H4 vs H7 | H4 | H4 can be tested in 12-18 months with a focused ex vivo experiment using existing mouse tumor models; H7 requires a pan-cancer study with cohort demands extending the timeline beyond 2 years. Sequential logic favors establishing the single-tumor-type result first. |
| H1 vs H2 | H1 | H1 is the foundational hypothesis of the entire framework with the most direct experimental design (BAPN titration + single-cell MSD measurement in a controlled ex vivo system); H2 depends on uncontrolled tumor proximity to p_c and power-law non-uniqueness. |
| H1 vs H5 | H1 | H1 tests the threshold itself (the primary prediction); H5 extends it to dose-response pharmacology but inherits H1's assumptions plus the additional dose-to-p mapping uncertainty. The cleaner, more foundational test should be performed first. |
| H1 vs H7 | H1 | H1 is testable in a single tumor type with controllable LOX activity; H7 requires demonstrating the same exponents across three tumor types at their respective critical points — a project that is sequentially dependent on H1's success. |
| H2 vs H5 | H2 | H2 can leverage existing spatial transcriptomics datasets without new experiments, while H5 requires new titration experiments plus independent p measurement; H2 wins on near-term accessibility despite both facing discriminability challenges. |
| H2 vs H7 | H2 | H2's prediction can be tested on existing multi-tumor-type transcriptomics datasets, partially sidestepping H7's critical-point-proximity requirement; H2 is more immediately actionable despite its own dataset demands. |
| H5 vs H7 | H5 | H5's titrated BAPN experiment is more tractable in the near term than H7's pan-cancer critical exponent measurement, and H5's therapeutic window prediction provides clearer translational motivation for grant funding. |

Win-rate tally:

| Hypothesis | Wins | Losses | Win Rate | Elo Rank |
|-----------|------|--------|----------|----------|
| H8 | 5 | 0 | 1.00 | 1st |
| H4 | 4 | 1 | 0.80 | 2nd |
| H1 | 3 | 2 | 0.60 | 3rd |
| H2 | 2 | 3 | 0.40 | 4th |
| H5 | 1 | 4 | 0.20 | 5th |
| H7 | 0 | 5 | 0.00 | 6th |

Elo ranking: H8 > H4 > H1 > H2 > H5 > H7

Comparison with linear composite ranking: H8 (1st), H4 (2nd), H1 (3rd), H2 (4th), H5 (5th), H7 (6th) — identical ordering.

**Verdict: Elo confirms linear ranking.** The pairwise tournament produces identical top-6 ordering to composite scoring across all 15 comparisons. The composite correctly captures testability as the major differentiator — H7's high Novelty and Creativity are consistently overridden by low Testability (5/10) when researchers must choose what to test first. No rank inversions observed.

---

## Recommendations for Evolver

### Top-3 for Evolution (post-diversity check)

1. **H8** (Composite: 8.50) — TGF-beta Autocrine Signaling as Bond-Correlated Percolation
2. **H4** (Composite: 8.30) — Collagen I/III Ratio as Lattice Topology Switch
3. **H1** (Composite: 8.10) — LOX Crosslink Density as Bond Occupation Probability

Recommended 4th evolution candidate: **H2** (Composite: 7.60) — its "computation on existing data" profile is uniquely accessible, and the spatial statistics prediction is mechanistically distinct from all top-3.

### Cycle decision flags

- Top-3 average composite: (8.50 + 8.30 + 8.10) / 3 = **8.30**
- Early-complete threshold (top-3 >= 7.0): **MET** — 8.30 >> 7.0
- Evolver-skip threshold for cycle 2 (top-3 >= 6.5): **MET**
- Orchestrator note: Given top-3 composite of 8.30, early-complete is strongly supported. The Critic's open questions (CQ3, CQ4, CQ9) address solvable gaps that the Evolver can target. One evolution cycle addressing those questions before Quality Gate is recommended.

### Specific evolution suggestions per hypothesis

**H8 — priority: refine experimental design and quantify mechanism**
- Address Critic question CQ9: specify an in vitro protocol isolating percolation-specific synergy from immunological TGF-beta blockade effects. Concrete proposal: use a collagen-only 3D gel system (no cancer antigens, no antigen-presenting cells) where TGF-beta's direct immunological effects on T cells are absent, isolating the ECM de-correlation mechanism via SHG autocorrelation before and after anti-TGF-beta treatment.
- Quantify the predicted p_c shift magnitude from correlated percolation theory using the TGF-beta correlation length estimate — a first-order perturbation expansion may be tractable.
- Address positive feedback depth concern: does the TGF-beta-LOX feedback push most tumors deep below p_c (making critical-point analysis irrelevant) or produce a stable near-threshold steady state accessible to therapy?

**H4 — priority: address directed percolation complication and biochemical confounding**
- If strongly aligned collagen I fibers enter the directed percolation universality class (different exponents), propose a measurement to distinguish this from failure of the isotropic model. SHG order parameter quantifying fiber alignment could gate which universality class applies.
- Compute approximate p_c values for anisotropic lattice geometries using published directed/anisotropic bond percolation results, replacing the PARAMETRIC range 0.35-0.45 with a literature-grounded estimate.
- Propose an experimental control comparing collagen I and III surfaces at matched mechanical stiffness to isolate topology from mechanotransduction (integrin binding, stiffness-dependent signaling).

**H1 — priority: operationalize the LOX-to-p mapping and address multiple-barrier problem**
- Address Critic question CQ3: specify a concrete imaging method to independently measure the lattice constant a. Second-harmonic generation combined with confocal reflectance microscopy can measure fiber spacing statistics; compare to pore size inferred from collagen density via published empirical correlations.
- Address Critic question CQ4: propose a first-order experiment partitioning immune exclusion attributable to ECM topology vs. endothelial immunosuppression and chemokine absence. A desmoplastic vs. inflamed tumor model comparison at matched T cell input would provide the partition.
- Refine the active-particle p_c estimate: acknowledge the 0.21-0.24 range is extrapolated from 2D and propose a 3D active percolation simulation as a needed prior step.

**H2 — if included as 4th evolution target**
- Identify specific public spatial transcriptomics datasets (GEO accession numbers) from PDAC or breast cancer with sufficient CD8+ T cell spatial density near the hot-cold boundary to test tau ~ 2.19.
- Propose a statistical power calculation for distinguishing tau = 2.19 from tau = 2.0 or 2.5 given realistic tumor sample sizes.
- Address power-law non-uniqueness: specify additional structural predictions unique to percolation (e.g., fractal dimension d_f = 2.53 of cluster boundaries measurable from 3D confocal reconstructions) that would distinguish this mechanism from branching processes or preferential attachment.

---

*Ranker: Hypothesis Ranker v5.2 | Session 015 | Cycle 1 | 2026-03-28*
