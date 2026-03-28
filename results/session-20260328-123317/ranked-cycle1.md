# Hypothesis Ranking — Cycle 1
## Session: session-20260328-123317
## Fields: Statistical mechanics (bond percolation theory) x Tumor immunology (ECM-mediated immune exclusion)
## Date: 2026-03-28
## Ranker: Sonnet / Hypothesis Ranker v5.2 | Cycle: 1

---

## Per-Hypothesis Scoring Tables

All hypotheses scored on 6 canonical dimensions (canonical immutable weights per CONSTRAINTS):
Novelty 20% | Mechanistic Specificity 20% | Cross-field Distance 10% | Testability 20% | Impact Paradigm 5% | Impact Translational 5% | Groundedness 20%

Cross-domain bonus (+0.5) applied to all hypotheses: Statistical mechanics (critical phenomena, fractal geometry, universality classes) and tumor immunology/pharmacology span 2+ disciplinary boundaries (physics/mathematics -> cell biology -> immunology/pharmacology). Non-biomedical retrieval tools (PubMed, KEGG, STRING) structurally underserve the statistical mechanics side of these hypotheses. Log: "Cross-domain bonus applied: +0.5" to each scoring table below.

Surviving hypotheses (6): H1, H2, H3, H4, H6, H8
Killed hypotheses (2): H5 (quantitative insufficiency), H7 (biology contradiction)

---

### Hypothesis H1: LOX Collagen Crosslink Density Maps to Bond Occupation Probability, Creating a Sharp Percolation Phase Transition in T Cell Immune Exclusion

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed zero papers directly connecting percolation theory to T cell infiltration in tumors (PubMed co-occurrence = 0 for "percolation T cell tumor"). Ashworth 2015 (PMID 25881025) is the closest prior art — percolation applied to connective tissue cell invasion in collagen scaffolds — but it explicitly does not cover T cells, LOX-mediated crosslinking, or tumor immunology. The specific application to LOX-controlled ECM as a bond occupation probability governing immune exclusion is genuinely novel. Score of 8 rather than 9 because Ashworth 2015 partially occupies the "percolation + collagen" conceptual space. |
| Mechanistic Specificity | 20% | 8 | Names specific enzymes (LOX, LOXL1-4), specific mathematical quantities (p_c = 0.2488, active correction to 0.21-0.24, order parameter exponent beta = 0.41), a specific concentration range (critical collagen 5-10 mg/mL versus tumor range 5-50 mg/mL), and a specific T cell squeeze constraint (Wolf 2013, imprecisely cited as 3 um but correct value is ~2.3 um diameter / 4 um^2 cross-section). The quantitative prediction (>80% infiltration drop within +/-1 mg/mL window, log-log slope beta = 0.41 +/- 0.1) distinguishes it from qualitative proposals. One unresolved gap: the mapping from crosslink fraction to bond occupation probability on a disordered collagen fiber network (not a regular lattice) is not resolved and represents the load-bearing assumption of the entire hypothesis. |
| Cross-field Distance | 10% | 9 | Statistical mechanics of critical phenomena (percolation theory, universality, order parameters) and tumor immunology (ECM biology, LOX enzymology, adaptive immune exclusion) share no practitioners, no shared vocabulary in the literature, and no methodological overlap. The bridge requires fluency in both fields simultaneously. Score of 9 rather than 10 because biophysics (mechanics of cell migration in ECM) sits between these fields and provides some intellectual scaffolding. |
| Testability | 20% | 8 | Test protocol explicit and complete: 3D collagen matrices at 8-10 densities spanning 2-20 mg/mL, activated CD8+ T cell infiltration by confocal at 24h, infiltration density vs. collagen concentration, sharp sigmoidal transition vs. gradual decrease as falsifying contrast. Estimated 3-6 months using standard collagen gel fabrication, confocal microscopy, and single-cell tracking. The predicted result if TRUE (>80% drop within 1 mg/mL window, slope beta = 0.41) and if FALSE (monotonic gradual decrease) are clearly distinguished. Docked one point because SHG imaging for network extraction adds a specialized requirement. |
| Impact: Paradigm | 5% | 7 | If the immune exclusion transition is a sharp phase transition rather than a continuous process, it fundamentally reframes the hot/cold tumor binary: these categories are not arbitrary cutoffs in a continuous distribution but two phases separated by a true thermodynamic boundary. Would redirect therapeutic strategy from "reduce collagen" to "cross the percolation threshold" and introduce statistical mechanics as a quantitative framework for tumor immunology. Would not create an entirely new field but would substantially redirect a subfield. |
| Impact: Translational | 5% | 7 | The threshold-crossing framework directly informs dosing strategy for LOX inhibitors (already in clinical trials for fibrosis): not "more BAPN is better" but "there is a critical dose that must be crossed." Changes trial design from maximizing dose to identifying the percolation-crossing dose. The combination of LOX inhibitors with anti-PD-1 immunotherapy (qualitatively supported by Nicolas-Boluda 2021) would benefit from a quantitative percolation model of when ECM is permissive. |
| Groundedness | 20% | 7 | Critic assessed approximately 70% of claims grounded. Verified: LOX crosslinking mechanism (Nicolas-Boluda 2021, eLife, confirmed), LOX inhibition improving T cell infiltration (PMID 38267662, 38305736, confirmed 2024 papers), percolation threshold and critical exponents (Stauffer & Aharony 1994, canonical textbook), collagen density threshold for T cell cytotoxic function (Kuczek 2019, confirmed), active percolation framework in 2D (Saha 2024, Soft Matter, confirmed). One imprecise citation (Wolf 2013 threshold 3 um, correct ~2.3 um). Parametric: active p_c in 3D, lattice topology of disordered collagen, concentration-to-crosslink-fraction mapping. |
| **Composite (pre-bonus)** | | **7.80** | 0.20x8 + 0.20x8 + 0.10x9 + 0.20x8 + 0.05x7 + 0.05x7 + 0.20x7 = 1.60 + 1.60 + 0.90 + 1.60 + 0.35 + 0.35 + 1.40 = 7.80 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (statistical mechanics -> tumor immunology -> pharmacology: 2+ disciplinary boundaries) |
| **Composite (final)** | | **8.30** | |

---

### Hypothesis H2: Universal Critical Exponent nu=0.88 Predicts T Cell Clustering Length Scale Across Tumor Types Independent of Molecular Details

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic confirmed no papers applying percolation universality to T cell spatial distributions in any tumor type. The cross-tumor universality prediction — that breast, pancreatic, colorectal, and lung tumors should show the same correlation length scaling with the same exponent despite vastly different molecular compositions — is entirely novel. No prior literature frames tumor immune infiltration as a universality-class problem. Score of 9 rather than 10 because general percolation approaches to tumor ECM (Ashworth 2015, Jiang 2016) establish some conceptual prior ground. |
| Mechanistic Specificity | 20% | 6 | Names specific exponent values (nu = 0.88 in 3D, contrasted with DP exponents nu_parallel = 1.73, nu_perp = 1.10), specific measurable length scales at specified distances from threshold (15 um at 10% above p_c, 115 um at 1% above, 430 um at 0.1% above, derived from a = 5 um assumption), and a data-collapse prediction across tumor types. The significant deduction: the Critic identified that active particles (Pe ~ 3) likely break isotropic universality, meaning the specific exponent nu = 0.88 is probably wrong for this system even if power-law scaling exists. The hypothesis names the right type of prediction (universality) but potentially the wrong specific numbers. |
| Cross-field Distance | 10% | 9 | Renormalization group theory and universality classes (mathematical physics) applied to multi-tissue cancer biology. Requires simultaneous expertise in statistical field theory and clinical tumor pathology — communities that never interact. Score of 9 for the same reasoning as H1. |
| Testability | 20% | 5 | Test feasible in a specialized lab with 6-12 months: fresh tissue from 4 tumor types, SHG imaging, T cell position mapping, correlation function extraction, log-log collapse. Critical practical barrier: test requires tumor samples sitting near p_c, which cannot be selected from clinical samples in advance. Additionally, extracting correlation lengths requires the T cell pair correlation function to follow a power law over at least one decade, requiring large fields of view and dense T cell populations. The "near p_c" selection problem is a fundamental testability constraint. |
| Impact: Paradigm | 5% | 8 | If confirmed, this would be among the most striking demonstrations that a universal physical law governs immune biology regardless of molecular context. True universality — the same exponent across all tumor types — would be a landmark result uniting statistical physics and cancer immunology. The potential paradigm impact is high. |
| Impact: Translational | 5% | 5 | The universality prediction does not directly suggest a therapeutic intervention. Its translational value is indirect: confirming universality validates the entire percolation framework, which then guides dosing (H4), timing (H6), and patient stratification. A confirming result would accelerate the translational pipeline but is not itself actionable. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% grounded. Verified: percolation critical exponents (textbook), universality theorem (renormalization group, canonical), correlation length formula (grounded). Parametric: measurable length scales (derived from assumed a = 5 um, not independently verified), cross-tumor universality (conditional on isotropic percolation class, which active particles may violate), collagen alignment changing effective dimensionality (known theoretical concern, no direct data). Munoz 2018 (smeared transitions in complex networks) provides literature-level counter-evidence. |
| **Composite (pre-bonus)** | | **6.55** | 0.20x9 + 0.20x6 + 0.10x9 + 0.20x5 + 0.05x8 + 0.05x5 + 0.20x5 = 1.80 + 1.20 + 0.90 + 1.00 + 0.40 + 0.25 + 1.00 = 6.55 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (statistical mechanics -> multi-tissue tumor biology: 2+ disciplinary boundaries) |
| **Composite (final)** | | **7.05** | |

---

### Hypothesis H3: Subdiffusive MSD Exponent alpha=0.53 as Diagnostic Fingerprint for ECM-Mediated Immune Exclusion

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | Critic classified as PARTIALLY_NOVEL. T cell subdiffusion in 3D collagen is already observed and published (Riedl et al. 2020, Biophys J, PMC7732778 — CTL subdiffusion in 3D collagen with multiple motility modes). The percolation interpretation of that subdiffusion is new. The "fingerprint" framing and the three-regime prediction (alpha = 1.0 -> 0.53 -> 0 as collagen density increases) are novel. Score of 6 because the observed phenomenon is published; only the explanation is new. |
| Mechanistic Specificity | 20% | 6 | Names specific exponent (alpha = 0.53 = 2/d_w = 2/3.8, from Alexander & Orbach 1982), predicts three distinguishable regimes as a function of crosslink density, and proposes velocity autocorrelation function as the distinguishing measurement between percolation and run-and-pause subdiffusion. Significant weakness: the same alpha value (0.5-0.7) is produced by T cell run-and-pause behavior without any percolation constraint (Krummel 2016). The hypothesis is specific about the value but not sufficiently specific about what distinguishes it from the confounding mechanism. Additionally, d_w = 3.8 is a numerical estimate (Alexander-Orbach conjecture proven only in high dimensions), introducing a theoretical approximation. |
| Cross-field Distance | 10% | 9 | Fractal geometry and anomalous diffusion on percolation clusters (mathematical physics) -> biophysical diagnostics in tumor immunology. Connects the theory of random walks on fractal structures (a specialized subfield of statistical mechanics) with clinical measurement in tumor immunology. Score of 9 for same reasoning as H1. |
| Testability | 20% | 5 | In vitro collagen gradient + single-cell tracking at 10-second intervals for 4+ hours achievable with standard confocal microscopy (3-6 months). Critical point: the MSD exponent alone is insufficient to distinguish percolation from run-and-pause subdiffusion. The test requires additional velocity autocorrelation function analysis, cluster size distribution measurements, and independent crosslink density measurement — substantially expanding scope. Furthermore, the crossover time t_xi may be very short, making the alpha = 0.53 regime experimentally inaccessible for most samples not precisely at p_c. |
| Impact: Paradigm | 5% | 5 | A validated diagnostic fingerprint for the mechanism of immune exclusion (ECM topology vs. motility-intrinsic) would be a useful scientific tool. However, the impact is moderate because the distinction (percolation vs. run-and-pause) is mechanistically interesting but does not change the clinical picture dramatically — both lead to reduced T cell infiltration regardless of cause. |
| Impact: Translational | 5% | 4 | A biophysical diagnostic extractable from intravital microscopy data could guide patient stratification (ECM-topology-driven exclusion vs. other causes), but measurement requirements (long trajectories, high temporal resolution, in vivo feasibility) severely limit immediate clinical applicability. More useful in a research context than a clinical one. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% grounded. Alexander-Orbach d_w = 3.8 in 3D (numerical estimate, grounded in literature). T cell single-cell tracking in collagen feasible (grounded). Viscoelastic subdiffusion range alpha = 0.5-0.9 (Metzler & Klafter 2000, grounded). Three-regime prediction (parametric). Active correction for MSD exponent (parametric). Crucially, Riedl et al. 2020 provides a published alternative explanation for the same observation, and Krummel 2016 establishes run-and-pause as an independent cause of the predicted alpha value. |
| **Composite (pre-bonus)** | | **5.75** | 0.20x6 + 0.20x6 + 0.10x9 + 0.20x5 + 0.05x5 + 0.05x4 + 0.20x5 = 1.20 + 1.20 + 0.90 + 1.00 + 0.25 + 0.20 + 1.00 = 5.75 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (fractal geometry / anomalous diffusion theory -> tumor immunology diagnostics: 2+ disciplinary boundaries) |
| **Composite (final)** | | **6.25** | |

---

### Hypothesis H4: BAPN Dose-Response Predicts a Sharp Nonlinear Phase Transition in Immune Infiltration — LOX Inhibitor as Percolation Control Knob

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed NOVEL. Nicolas-Boluda 2021 tested a single BAPN dose combined with anti-PD-1 — not a dose-response experiment and not examining the shape of the curve. No papers connect BAPN dose-response shape to percolation physics or predict the shape should be a power-law onset rather than a Hill equation. The specific prediction that the percolation signature is distinguishable from standard pharmacology by the shape of the infiltration onset curve is genuinely novel. |
| Mechanistic Specificity | 20% | 8 | Names specific drug with known pharmacodynamics (BAPN, irreversible LOX inhibitor, covalent mechanism verified), specific exponent for dose-response onset (I(d) ~ (d - d_c)^beta with beta = 0.41, universal, not a free parameter), specific contrast with Hill equation (smooth sigmoid vs. true zero below threshold), and ECM equilibration timescale requirement (48-72 hours minimum). Identifies the two unknowns (dose -> LOX activity; LOX activity + MMP rate -> equilibrium crosslink density) clearly. Citation date error (Tang 2017 cited; correct is Tang 1983) noted but does not affect the mechanism. Score of 8 because mechanism is highly specific even with two unknowns explicitly flagged. |
| Cross-field Distance | 10% | 9 | Statistical mechanics (percolation phase transitions, order parameter exponents) -> tumor pharmacology (BAPN dosing, LOX inhibition, ECM remodeling kinetics) -> tumor immunology (CD8+ T cell infiltration). Three-domain bridge: physics, pharmacology, immunology. Score of 9 consistent with set. |
| Testability | 20% | 8 | Most directly testable hypothesis in the set. Experiment sweeps through p_c by design (increasing BAPN dose decreases crosslink density), rather than requiring tumors to happen to be near p_c. Standard animal models (4T1 breast, KPC pancreatic), established BAPN dosing protocols (7-day treatment from Nicolas-Boluda 2021), quantitative readouts (CD8+ T cell density by IHC, crosslink density by pyridinoline assay, total collagen by hydroxyproline assay). 6-12 months. Predicted result if TRUE (sharp sigmoid with beta = 0.41 onset, universal exponent across tumor types despite different d_c) and if FALSE (Hill equation with variable coefficient) are quantitatively distinguishable. |
| Impact: Paradigm | 5% | 6 | Reframes LOX inhibition from a collagen density reduction strategy to a percolation control parameter strategy, introducing the concept of a critical dose rather than a maximal tolerated dose for ECM-targeted immunotherapy. Significant conceptual reframing within the tumor immunology subfield. |
| Impact: Translational | 5% | 8 | LOX inhibitors in clinical trials for fibrosis (direct translational context). Percolation prediction provides quantitative dosing principle: find the critical dose that crosses the percolation threshold, not the maximum dose. Immediately actionable in trial design. Combined LOX inhibitor + immunotherapy is an active area. The quantitative shape prediction (beta = 0.41, not a Hill coefficient) would be testable in Phase I dose-finding studies. |
| Groundedness | 20% | 6 | Critic assessed approximately 65% grounded. BAPN mechanism correctly described despite citation date error (Tang 1983, confirmed). Nicolas-Boluda 2021 qualitative direction verified. MMP crosslink turnover timescale (MMP-1 t_1/2 ~ 4-12 hours) grounded. beta = 0.41 textbook-grounded. Phase transition shape prediction is parametric (mapping from percolation to pharmacology not demonstrated). p(dose) function is parametric and load-bearing. Score of 6 because the key novel prediction (shape of dose-response) is entirely parametric and contingent on H1's lattice mapping being valid. |
| **Composite (pre-bonus)** | | **7.60** | 0.20x8 + 0.20x8 + 0.10x9 + 0.20x8 + 0.05x6 + 0.05x8 + 0.20x6 = 1.60 + 1.60 + 0.90 + 1.60 + 0.30 + 0.40 + 1.20 = 7.60 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (statistical mechanics -> pharmacology -> tumor immunology: 3-domain bridge, 2+ disciplinary boundaries) |
| **Composite (final)** | | **8.10** | |

---

### Hypothesis H6: MMP/LOX Kinetic Balance Creates Dynamic Percolation, Generating Temporal Windows of Immune Infiltration in Tumors

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed NOVEL. No papers apply dynamic percolation theory to ECM remodeling or immune infiltration. The concept of temporal windows of immune infiltration arising from oscillatory MMP/LOX balance — T cells catching the window (reaching tumor core) or missing it (producing peri-tumoral accumulation) — is not present in the literature. Score of 8 because the qualitative concept of ECM remodeling enabling immune access is discussed in the field; the percolation formalization and temporal window quantification are the novel contributions. |
| Mechanistic Specificity | 20% | 5 | Provides a kinetic model (p_ss = k_LOX/(k_LOX + k_MMP)), identifies specific molecular players (>20 MMPs, 4 LOX family members, STRING interactions: TGFB1 = 0.623, IL1B = 0.727, CCL2 = 0.710), gives a timescale analysis (LOX crosslinking hours, MMP degradation 4-12 hours, T cell transit 10-200 minutes), and predicts pulsatile infiltration correlated with MMP activity peaks. Critical weakness: the kinetic model is dramatically oversimplified (20+ MMPs, 4 TIMPs, spatial heterogeneity ignored). The steady-state formula ignores that LOX-crosslinked collagen is specifically resistant to MMP degradation (potentially invalidating the timescale matching). |
| Cross-field Distance | 10% | 9 | Non-equilibrium statistical mechanics (dynamic percolation, time-dependent bond processes) -> tumor ECM kinetics -> tumor immunology. Dynamic percolation is a distinct and more sophisticated branch of statistical mechanics than static percolation, adding disciplinary distance. Score of 9 consistent with set. |
| Testability | 20% | 6 | Ex vivo organotypic tumor slice culture with fluorescent CD8+ T cells + SHG + DQ-collagen fluorescent MMP activity sensors is technically feasible in a specialized lab. Correlating temporal MMP activity peaks (r > 0.5) with T cell infiltration bursts over 48 hours is a clear measurable prediction. Concerns reducing score: (1) LOX-crosslinked collagen may be resistant to MMP degradation (timescale days-weeks not hours), making predicted dynamic range unobservable; (2) organotypic culture requires fresh tumor tissue and specialized expertise; (3) real-time MMP sensors are not standard in immunology labs. Score of 6 reflects feasibility in specialized lab with significant barriers. |
| Impact: Paradigm | 5% | 7 | The dynamic percolation view of immune exclusion reframes peri-tumoral T cell accumulation from a static barrier to a dynamic timing failure. Would suggest the same tumor can be permissive or restrictive at different times, opening the concept of immunotherapy timing windows. Conceptually significant reframing even if molecular details are uncertain. |
| Impact: Translational | 5% | 6 | If infiltration is temporally gated by MMP/LOX balance, the translational implication is to synchronize immunotherapy with peak MMP activity (or use MMP activators to open windows). Concrete clinically testable strategy, though MMP activity monitoring in patients is a barrier. |
| Groundedness | 20% | 4 | Critic assessed approximately 55% of named components as grounded, but key mechanistic elements are parametric. Grounded: LOX crosslinking (Nicolas-Boluda 2021), MMP degradation biology (Lu et al. 2011), STRING LOX interaction scores (TGFB1, IL1B, CCL2), peri-tumoral T cell accumulation (Salmon et al. 2012), T cell migration speed (Krummel 2016). Parametric: kinetic rate constants, p(t) model, pulsatile infiltration prediction, timescale matching for LOX-crosslinked collagen. Critical penalty: Salmon 2012 explicitly attributes peri-tumoral trapping to collagen FIBER ALIGNMENT, not network connectivity — a direct grounded alternative explanation for the key observation the hypothesis is built to explain. |
| **Composite (pre-bonus)** | | **6.15** | 0.20x8 + 0.20x5 + 0.10x9 + 0.20x6 + 0.05x7 + 0.05x6 + 0.20x4 = 1.60 + 1.00 + 0.90 + 1.20 + 0.35 + 0.30 + 0.80 = 6.15 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (non-equilibrium statistical mechanics -> ECM kinetics -> tumor immunology: 2+ disciplinary boundaries) |
| **Composite (final)** | | **6.65** | |

---

### Hypothesis H8: Directed Percolation from Chemotaxis — T Cell Migration Shifts to Directed Percolation Universality Class

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic confirmed NOVEL. No papers analyze whether T cell infiltration follows isotropic or directed percolation universality. Jiang 2016 used isotropic percolation for tumor cell proliferation without addressing chemotactic directionality. Wang 2025 involves surface cascade, not directional transport. The prediction that chemotaxis shifts the universality class — changing the mathematical framework's predictions rather than merely adding a correction term — is entirely novel. The self-limiting framing (specifies when H1-H4 fail) adds further intellectual novelty. |
| Mechanistic Specificity | 20% | 6 | Names specific exponents (nu_parallel = 1.73, nu_perp = 1.10 in 3D DP, from Hinrichsen 2000), identifies the crossover condition (Pe ~ 1), defines a specific observable (anisotropic correlation function ratio xi_parallel/xi_perp diverges as p -> p_c), and maps the condition to chemokine sources (CCL5, CXCL9/10 from Nagarsheth 2017). Significant mechanistic weakness: directed percolation requires a single fixed preferred direction. Real tumor chemokine gradients are multi-source, non-monotonic, spatially variable — potentially averaging to isotropic on length scales comparable to xi. Pe ~ 3 places the system in the crossover regime where neither isotropic nor directed percolation exponents apply cleanly, leaving the core prediction ambiguous. |
| Cross-field Distance | 10% | 9 | Directed percolation (non-equilibrium statistical mechanics, distinct universality class) -> chemokine signaling (cell biology) -> tumor immunology. Requires simultaneous expertise in non-equilibrium phase transitions and cancer immunology. Score of 9 consistent with set. |
| Testability | 20% | 4 | The test requires: (1) inferring chemokine gradient orientation from CXCL9/10 immunostaining, (2) measuring T cell pair correlation functions separately along parallel and perpendicular directions, (3) extracting xi_parallel and xi_perp from directional correlation functions, (4) repeating across multiple samples near p_c. Requires specialized computational pipeline not standard in tumor immunology labs and large annotated datasets with known gradient orientation. Additionally, Pe ~ 3 sits in the crossover regime, meaning expected xi_parallel/xi_perp values are not precisely predicted, weakening falsifiability of the specific quantitative test. |
| Impact: Paradigm | 5% | 7 | Establishing the correct universality class would be a significant theoretical result: specifies which mathematical framework (isotropic vs. directed percolation) governs the entire hypothesis family and corrects the predictions of H1-H4. If the system is in the DP class, then nu = 0.88 is wrong and nu_parallel = 1.73 is right — a 2x correction to the key exponent. Paradigmatically important for the percolation framework as applied to immunology. |
| Impact: Translational | 5% | 3 | Identifying the universality class has minimal direct translational value. The practical treatment strategy (inhibit LOX, cross the percolation threshold) remains the same regardless of whether the exponent is 0.88 or 1.73. Translational benefit is indirect: correct exponents produce more accurate quantitative dosing predictions. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% grounded. Verified: directed percolation exponents nu_parallel = 1.73, nu_perp = 1.10 in 3D (Hinrichsen 2000, Adv Phys 49:815-958, confirmed). T cell chemotaxis toward CXCL9/10 (Nagarsheth et al. 2017, Nat Rev Immunol, grounded). Parametric: Pe ~ 3 estimate (computational validation, not independently verified), isotropic-to-directed crossover at Pe ~ 1 (standard physics expectation, not demonstrated for biological system), anisotropic correlation length measurement in tumors (novel proposal). Internal consistency concern: H8 predicts directed DP class while H2 assumes isotropic DP class — structural weakness across the hypothesis set. |
| **Composite (pre-bonus)** | | **6.20** | 0.20x9 + 0.20x6 + 0.10x9 + 0.20x4 + 0.05x7 + 0.05x3 + 0.20x5 = 1.80 + 1.20 + 0.90 + 0.80 + 0.35 + 0.15 + 1.00 = 6.20 |
| Cross-domain bonus | | +0.5 | Cross-domain bonus applied: +0.5 (directed percolation / non-equilibrium phase transitions -> chemokine biology -> tumor immunology: 2+ disciplinary boundaries) |
| **Composite (final)** | | **6.70** | |

---

## Final Ranking Table

| Rank | ID | Title (abbreviated) | Composite (pre-bonus) | Bonus | Composite (final) | Verdict |
|------|----|---------------------|----------------------|-------|-------------------|---------|
| 1 | H1 | LOX Crosslink Density = Bond Occupation Probability | 7.80 | +0.5 | **8.30** | CONDITIONAL_PASS (conf 5) |
| 2 | H4 | BAPN Dose-Response Sharp Phase Transition | 7.60 | +0.5 | **8.10** | CONDITIONAL_PASS (conf 5) |
| 3 | H2 | Universal Critical Exponent nu=0.88 Cross-Tumor Biomarker | 6.55 | +0.5 | **7.05** | CONDITIONAL_PASS (conf 4) |
| 4 | H8 | Directed Percolation from Chemotaxis | 6.20 | +0.5 | **6.70** | CONDITIONAL_PASS (conf 3) |
| 5 | H6 | Dynamic Percolation MMP/LOX Infiltration Windows | 6.15 | +0.5 | **6.65** | CONDITIONAL_PASS (conf 3) |
| 6 | H3 | Subdiffusive MSD alpha=0.53 Diagnostic Fingerprint | 5.75 | +0.5 | **6.25** | CONDITIONAL_PASS (conf 4) |

---

## Diversity Check

### Top-5 Hypotheses Under Review: H1, H4, H2, H8, H6

**Pair-wise mechanism similarity analysis:**

**H1 vs H4**: H4 is the pharmacological operationalization of H1's framework — both use the LOX crosslink density = bond occupation probability mapping. However, H4 is not a minor variation: it is a distinct experiment (dose-response sweep vs. matrix density scan), a distinct falsifiable prediction (power-law onset shape vs. sharp threshold), and has distinct translational implications (drug dosing principle). H1 tests the existence of the sharp transition; H4 tests whether a clinical drug can produce it. Connected but not redundant.

**H1 vs H2**: Both depend on H1's lattice mapping, but H2 focuses on universality across tumor types (correlation length scaling) rather than the phase transition itself. Different experimental systems and different testable predictions. H2 is downstream but not redundant.

**H4 vs H2**: H4 tests critical exponent beta in dose-response; H2 tests critical exponent nu in spatial clustering. Different experimental approaches, different biological systems, different predictions. Not redundant.

**H2 vs H8**: Internally contradictory — H2 assumes isotropic percolation (nu = 0.88) while H8 argues the system belongs to the directed percolation class (nu_parallel = 1.73). Including both is scientifically appropriate: one is right and the other wrong, and both are testable. H8 provides a diagnostic test for which exponent applies.

**H8 vs H6**: Different bridge mechanisms — H8 concerns the universality class (isotropy of the walker), H6 concerns the temporal evolution of the lattice (dynamic percolation). Different experimental systems, different predictions. Not redundant.

**H1 vs H6**: H6 is the dynamic extension of H1. They share the underlying LOX = bond occupation probability mapping but address different aspects (static threshold vs. temporal dynamics) and require different experimental systems. Not redundant.

**Convergence assessment**: Top-5 spans 5 distinct mechanistic angles:
- Static phase transition existence (H1)
- Pharmacological threshold crossing (H4)
- Cross-tumor universality (H2)
- Framework boundary condition / universality class (H8)
- Temporal window / dynamic ECM (H6)

**Diversity check PASSES.** No adjustment needed. The top-5 is mechanistically diverse despite all drawing on percolation theory as the bridge concept.

**Note**: H3 (MSD fingerprint) is left at rank 6 — weakest hypothesis (affirming-the-consequent logic issue, published alternative explanation from Riedl 2020, MSD exponent alone is insufficient as diagnostic). No diversity promotion needed.

---

## Elo Tournament Sanity Check (Top 6: H1, H4, H2, H8, H6, H3)

15 pairwise comparisons (N=6, N*(N-1)/2 = 15). For each pair: which hypothesis would a domain researcher want to test FIRST, and why?

**H1 vs H4**: H1 first — H4's dose-response prediction is explicitly contingent on H1 being true. Testing whether a sharp transition exists (H1) is the necessary prerequisite before testing whether BAPN produces it (H4). H1 wins.

**H1 vs H2**: H1 first — H2's universality prediction requires knowing the system is in the percolation universality class, established by H1. H1 also requires simpler infrastructure (single collagen gradient, one tumor type). H1 wins.

**H1 vs H8**: H1 first — must establish whether percolation applies at all before asking which universality class it belongs to (H8). H1 has a more direct experimental design. H1 wins.

**H1 vs H6**: H1 first — static percolation is simpler and more fundamental. H6 requires H1's framework to be established first and additionally requires the ECM to be dynamic on T cell transit timescales. H1 wins.

**H1 vs H3**: H1 first — more fundamental, higher groundedness, and predictions (sharp phase transition in infiltration density) are more directly testable and interpretable than H3's confounded MSD fingerprint. H1 wins.

**H4 vs H2**: H4 first — directly testable with controlled animal experiment sweeping through p_c by design. H2 requires tumors to happen to sit near p_c, which cannot be engineered. H4 is more immediately actionable. H4 wins.

**H4 vs H8**: H4 first — dose-response experiment generates clean quantitative data on transition existence. H8 requires inferring gradient orientation from immunostaining and measuring anisotropic correlation functions in the crossover regime (Pe ~ 3). H4 wins.

**H4 vs H6**: H4 first — sweeps through p_c experimentally and generates a clean dose-response curve. H6 requires time-lapse organotypic culture with real-time MMP sensors, with uncertain timescale matching for LOX-crosslinked collagen. H4 wins.

**H4 vs H3**: H4 first — more directly testable and has cleaner falsifiable predictions. H3's MSD fingerprint requires ruling out run-and-pause subdiffusion as confound, adding substantial analysis burden. H4 wins.

**H2 vs H8**: H2 first — confirmatory test of universality within the isotropic percolation framework, before the more esoteric question of whether the framework needs replacement by directed percolation (H8). H2's data output (correlation length values) is informative regardless of whether the slope matches nu = 0.88 exactly. H2 wins.

**H2 vs H6**: H2 first — prediction (cross-tumor data collapse) is experimentally cleaner despite requiring tumors near p_c. H6's dynamic percolation prediction requires time-resolved imaging with MMP sensors, more technically demanding with uncertain timescales. H2 wins.

**H2 vs H3**: H2 first — universality prediction is more ambitious and falsifiable than H3's fingerprint prediction (run-and-pause confound). Researcher wanting a high-impact result would tackle H2 over H3. H2 wins.

**H8 vs H6**: H8 very narrow win — asks which universality class governs T cell migration (more fundamental question with broader implications for the hypothesis set). However, H6's experimental test is more tractable than H8's anisotropic correlation function measurement. H8 wins narrowly on conceptual priority.

**H8 vs H3**: H8 first — more novel (NOVEL vs. PARTIALLY NOVEL), directed percolation question is more fundamental, H3 has a confounding mechanism problem. H8 wins.

**H6 vs H3**: H6 first — clear prediction (pulsatile infiltration correlated with MMP peaks) and direct experimental test (time-lapse organotypic culture). H3's fingerprint claim is undermined by the run-and-pause confound. H6 wins.

### Elo Win Tally:

| Hypothesis | Wins | Losses | Win Rate | Elo Rank |
|------------|------|--------|----------|----------|
| H1 | 5 | 0 | 1.00 | 1 |
| H4 | 4 | 1 | 0.80 | 2 |
| H2 | 3 | 2 | 0.60 | 3 |
| H8 | 2 | 3 | 0.40 | 4 |
| H6 | 1 | 4 | 0.20 | 5 |
| H3 | 0 | 5 | 0.00 | 6 |

### Elo vs. Linear Ranking Comparison:

| Rank | Linear Composite | Elo Tournament |
|------|-----------------|----------------|
| 1 | H1 (8.30) | H1 |
| 2 | H4 (8.10) | H4 |
| 3 | H2 (7.05) | H2 |
| 4 | H8 (6.70) | H8 |
| 5 | H6 (6.65) | H6 |
| 6 | H3 (6.25) | H3 |

**Elo confirms linear ranking.** Both methods produce the identical ranking H1 > H4 > H2 > H8 > H6 > H3. The pairwise tournament captures a foundationality dimension: H1 is prerequisite for H4, H2, H6; H4 is most directly actionable; H2 tests the deep universality prediction; H8 and H6 are further from testability. The consistent ordering increases confidence in selecting H1, H4, H2 as primary evolution candidates.

---

## Evolution Selection

**Selected for Cycle 2 Evolution (primary): H1, H4, H2**

Top-3 composite scores: H1 (8.30), H4 (8.10), H2 (7.05). All above the 6.5 Evolver-skip threshold. The 7.0 early-complete threshold is marginally met (H2 = 7.05). Meaningful structural improvements are possible per the Critic's questions, so the Evolver should run.

**Carry forward (secondary): H8, H6**

H8 addresses when H1-H4 predictions fail (universality class question). H6 adds the temporal dimension that static percolation ignores. Both provide mechanistically distinct angles that diversify the evolved pool.

**Not selected: H3**

The affirming-the-consequent problem and Riedl 2020's published alternative explanation make H3 the lowest-priority evolution candidate.

**Evolver instructions for cycle 2:**

H1: Address the disordered lattice abstraction — explore Voronoi/random geometric graph percolation as replacement for regular lattice; quantify how intratumoral collagen density heterogeneity smears the sharp transition; correct Wolf 2013 threshold to 4 um^2 cross-section (~2.3 um diameter).

H4: Correct Tang citation from 2017 to 1983 (Tang, Trackman & Kagan, J Biol Chem 258:4331); estimate shape of p(dose) function for BAPN given LOX enzyme kinetics and MMP turnover rates; assess whether cooperative LOX activity threshold would produce spurious inflections in the dose-response curve.

H2: Address directed percolation concern from H8: characterize what exponent the Pe ~ 3 system actually uses; redesign test to measure the exponent empirically rather than assume nu = 0.88; consider whether in vitro collagen gels with known crosslink densities (rather than clinical tissue) could be used to measure the exponent.
