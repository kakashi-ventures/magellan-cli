# Hypothesis Ranking — Cycle 1
## Session: session-20260328-123317
## Fields: Statistical mechanics (bond percolation theory) x Tumor immunology (ECM-mediated immune exclusion)
## Date: 2026-03-28
## Ranker: Sonnet | Cycle: 1

---

## Per-Hypothesis Scoring Tables

All hypotheses scored on 6 canonical dimensions (weights from CONSTRAINTS):
Novelty 20% | Mechanistic Specificity 20% | Cross-field Distance 10% | Testability 20% | Impact Paradigm 5% | Impact Translational 5% | Groundedness 20%

Cross-domain bonus (+0.5) applied to all hypotheses: Statistical mechanics (critical phenomena, fractal geometry, universality classes) and tumor immunology/pharmacology span 2+ disciplinary boundaries (physics/mathematics -> cell biology -> immunology/pharmacology). Non-biomedical retrieval tools (PubMed, KEGG, STRING) structurally underserve the statistical mechanics side of these hypotheses.

---

### Hypothesis H1: LOX Collagen Crosslink Density Maps to Bond Occupation Probability, Creating a Sharp Percolation Phase Transition in T Cell Immune Exclusion

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed zero papers directly connecting percolation theory to T cell infiltration in tumors (PubMed co-occurrence = 0 for "percolation T cell tumor"). Ashworth 2015 (PMID 25881025) is the closest prior art, applying percolation to connective tissue cell invasion in collagen scaffolds, but it explicitly does not cover T cells, LOX-mediated crosslinking, or tumor immunology. The specific application to LOX-controlled ECM as a bond occupation probability governing immune exclusion is genuinely novel. Score of 8 rather than 9 because Ashworth 2015 partially occupies the "percolation + collagen" conceptual space. |
| Mechanistic Specificity | 20% | 8 | The hypothesis names specific enzymes (LOX, LOXL1-4), specific mathematical quantities (p_c = 0.2488, active correction to 0.21-0.24, order parameter exponent beta = 0.41), a specific concentration range (critical collagen 5-10 mg/mL versus tumor range 5-50 mg/mL), and a specific T cell squeeze constraint (Wolf 2013, imprecisely cited but corrected in critique). The quantitative prediction (>80% infiltration drop within +/-1 mg/mL window, log-log slope beta = 0.41 +/- 0.1) distinguishes it from qualitative proposals. One unresolved gap: the mapping from crosslink fraction to bond occupation probability on a disordered collagen fiber network (not a regular lattice) is not resolved and represents the load-bearing assumption of the entire hypothesis. |
| Cross-field Distance | 10% | 9 | Statistical mechanics of critical phenomena (percolation theory, universality, order parameters) and tumor immunology (ECM biology, LOX enzymology, adaptive immune exclusion) share no practitioners, no shared vocabulary in the literature, and no methodological overlap. The bridge requires fluency in both fields simultaneously. Score of 9 rather than 10 because biophysics (mechanics of cell migration in ECM) sits between these fields and provides some intellectual scaffolding. |
| Testability | 20% | 8 | The test protocol is explicit and complete: 3D collagen matrices fabricated at 8-10 densities spanning 2-20 mg/mL, activated CD8+ T cell infiltration measured by confocal at 24h, infiltration density plotted vs. collagen concentration, sharp sigmoidal transition compared against gradual decrease as falsifying contrast. Estimated 3-6 months using standard collagen gel fabrication, confocal microscopy, and single-cell tracking — all of which are routine in multiple labs. The predicted result if TRUE (>80% drop within 1 mg/mL window) and if FALSE (monotonic gradual decrease) are clearly distinguished. Docked one point because SHG imaging for network extraction adds a specialized requirement. |
| Impact: Paradigm | 5% | 7 | If the immune exclusion transition is a sharp phase transition rather than a continuous process, it fundamentally reframes the hot/cold tumor binary: these categories are not arbitrary cutoffs in a continuous distribution but two phases separated by a true thermodynamic boundary. This would redirect therapeutic strategy from "reduce collagen" to "cross the percolation threshold" and introduce statistical mechanics as a quantitative framework for tumor immunology. Would not create an entirely new field but would substantially redirect a subfield with significant precedent in cancer biophysics. |
| Impact: Translational | 5% | 7 | The threshold-crossing framework directly informs dosing strategy for LOX inhibitors (already in clinical trials for fibrosis): the prediction is not "more BAPN is better" but "there is a critical dose that must be crossed." This changes trial design from optimizing maximum tolerated dose to identifying the percolation-crossing dose. The combination of LOX inhibitors with anti-PD-1 immunotherapy (qualitatively supported by Nicolas-Boluda 2021) would benefit from a quantitative percolation model of when ECM is permissive. |
| Groundedness | 20% | 7 | Critic assessed approximately 70% of claims as grounded. Verified: LOX crosslinking mechanism (Nicolas-Boluda 2021, eLife, confirmed), LOX inhibition improving T cell infiltration (PMID 38267662, 38305736, confirmed 2024 papers), percolation threshold and critical exponents (Stauffer & Aharony 1994, canonical textbook), collagen density threshold for T cell cytotoxic function (Kuczek 2019, confirmed), active percolation framework in 2D (Saha 2024, Soft Matter, confirmed). One imprecise citation (Wolf 2013 threshold stated as 3 um pore diameter, correct value is ~2.3 um corresponding to 4 um^2 cross-sectional area). Parametric: active p_c in 3D (extrapolated from 2D), lattice topology of disordered collagen, specific concentration-to-crosslink-fraction mapping. |
| **Composite (pre-bonus)** | | **7.80** | 0.20x8 + 0.20x8 + 0.10x9 + 0.20x8 + 0.05x7 + 0.05x7 + 0.20x7 = 1.60 + 1.60 + 0.90 + 1.60 + 0.35 + 0.35 + 1.40 = 7.80 |
| Cross-domain bonus | | +0.5 | Statistical mechanics -> tumor immunology -> pharmacology: 2+ disciplinary boundaries crossed. |
| **Composite (final)** | | **8.30** | |

---

### Hypothesis H2: Universal Critical Exponent nu=0.88 Predicts T Cell Clustering Length Scale Across Tumor Types Independent of Molecular Details

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic confirmed no papers applying percolation universality to T cell spatial distributions in any tumor type. The cross-tumor universality prediction — that breast, pancreatic, colorectal, and lung tumors should show the same correlation length scaling with the same exponent despite vastly different molecular compositions — is entirely novel. No prior literature even frames tumor immune infiltration as a universality-class problem. Score of 9 rather than 10 because the general percolation approach to tumor ECM (Ashworth 2015, Jiang 2016) establishes some conceptual prior ground. |
| Mechanistic Specificity | 20% | 6 | Names specific exponent values (nu = 0.88 in 3D, contrasted with DP exponents nu_parallel = 1.73, nu_perp = 1.10), specific measurable length scales at specified distances from threshold (15 um at 10% above p_c, 115 um at 1% above, 430 um at 0.1% above, derived from a = 5 um lattice spacing assumption), and a data-collapse prediction across tumor types. The significant deduction: the Critic identified that active particles (Pe ~ 3) likely break isotropic universality, meaning the specific exponent nu = 0.88 is probably wrong for this system even if power-law scaling exists. The hypothesis names the right type of prediction (universality) but potentially the wrong specific numbers. |
| Cross-field Distance | 10% | 9 | Renormalization group theory and universality classes (mathematical physics) applied to multi-tissue cancer biology. This bridge requires simultaneous expertise in statistical field theory and clinical tumor pathology — communities that never interact. Score of 9 for the same reasoning as H1. |
| Testability | 20% | 5 | The test (obtain fresh tissue from 4 tumor types, SHG imaging, T cell position mapping, correlation function extraction, log-log collapse) is technically feasible in a specialized lab with 6-12 months of work. However, the Critic identifies a critical practical barrier: the test requires tumor samples sitting near p_c, which cannot be selected from clinical samples in advance — the researcher must screen many tumors to find ones near threshold. This requirement cannot be engineered in vitro without knowing the threshold value a priori. Additionally, extracting correlation lengths requires the T cell pair correlation function to follow a power law over at least one decade of length scale, which requires large fields of view and dense T cell populations. |
| Impact: Paradigm | 5% | 8 | If confirmed, this would be among the most striking demonstrations that a universal physical law governs immune biology regardless of molecular context. Universality in biology — true universality where the exponent is identical across all systems — would be a landmark result uniting statistical physics and cancer immunology, and would justify building an entire quantitative framework on percolation universality. The potential paradigm impact is high. |
| Impact: Translational | 5% | 5 | The universality prediction itself does not directly suggest a therapeutic intervention. Its translational value is indirect: confirming universality validates the entire percolation framework, which then guides dosing (H4), timing (H6), and patient stratification. A confirming result would accelerate the translational pipeline but is not itself actionable. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% of claims as grounded. Verified: percolation critical exponents (textbook), universality theorem (renormalization group, canonical), correlation length formula (grounded). Parametric: measurable length scales (derived from assumed a = 5 um lattice spacing, not independently verified), cross-tumor universality (conditional on system being in isotropic percolation class, which active particles may violate), collagen alignment changing effective dimensionality in desmoplastic tumors (known theoretical concern, no direct data). Munoz 2018 (smeared phase transitions in complex networks) provides literature-level counter-evidence. |
| **Composite (pre-bonus)** | | **6.55** | 0.20x9 + 0.20x6 + 0.10x9 + 0.20x5 + 0.05x8 + 0.05x5 + 0.20x5 = 1.80 + 1.20 + 0.90 + 1.00 + 0.40 + 0.25 + 1.00 = 6.55 |
| Cross-domain bonus | | +0.5 | Statistical mechanics -> multi-tissue tumor biology: 2+ disciplinary boundaries crossed. |
| **Composite (final)** | | **7.05** | |

---

### Hypothesis H3: Subdiffusive MSD Exponent alpha=0.53 as Diagnostic Fingerprint for ECM-Mediated Immune Exclusion

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | Critic classified as PARTIALLY_NOVEL. T cell subdiffusion in 3D collagen is already observed and published (Riedl et al. 2020, Biophys J, PMC7732778 — CTL subdiffusion in 3D collagen with multiple motility modes). The percolation interpretation of that subdiffusion is new. The "fingerprint" framing and the three-regime prediction (alpha = 1.0 -> 0.53 -> 0 as collagen density increases) are novel. Score of 6 because the observed phenomenon is published; only the explanation is new. |
| Mechanistic Specificity | 20% | 6 | Names specific exponent (alpha = 0.53 = 2/d_w = 2/3.8, from Alexander & Orbach 1982), predicts three distinguishable regimes as a function of crosslink density, and proposes velocity autocorrelation function as the distinguishing measurement between percolation and run-and-pause subdiffusion. The significant weakness identified by the Critic: the same alpha value (0.5-0.7) is produced by T cell run-and-pause behavior without any percolation constraint (Krummel 2016). The hypothesis is specific about the value but not sufficiently specific about what distinguishes it from the confounding mechanism. Additionally, d_w = 3.8 is a numerical estimate (Alexander-Orbach conjecture proven only in high dimensions), introducing a theoretical approximation into the core prediction. |
| Cross-field Distance | 10% | 9 | Fractal geometry and anomalous diffusion on percolation clusters (mathematical physics) -> biophysical diagnostics in tumor immunology. This bridge connects the theory of random walks on fractal structures (a specialized subfield of statistical mechanics) with clinical/biological measurement in tumor immunology. Score of 9 for same reasoning as H1. |
| Testability | 20% | 5 | In vitro collagen gradient + single-cell tracking at 10-second intervals for 4+ hours is achievable with standard confocal microscopy (3-6 months). However, the Critic makes a critical point: the MSD exponent alone is insufficient to distinguish percolation from run-and-pause subdiffusion. The test requires additional velocity autocorrelation function analysis, cluster size distribution measurements, and crosslink density independent measurement — substantially expanding scope. Furthermore, the crossover time t_xi (between subdiffusive and normal regimes) may be very short, making the alpha = 0.53 regime experimentally inaccessible for most tumor samples not precisely at p_c. |
| Impact: Paradigm | 5% | 5 | A validated diagnostic fingerprint for the mechanism of immune exclusion (ECM topology vs. motility-intrinsic) would be a useful scientific tool. However, the impact is moderate because the distinction being made (percolation vs. run-and-pause) is mechanistically interesting but does not change the clinical picture dramatically — both lead to reduced T cell infiltration regardless of cause. |
| Impact: Translational | 5% | 4 | A biophysical diagnostic that can be extracted from intravital microscopy data could in principle guide patient stratification (which patients have ECM-topology-driven exclusion vs. other causes), but the measurement requirements (long trajectories, high temporal resolution, in vivo feasibility) severely limit immediate clinical applicability. The diagnostic is more useful in a research context than a clinical one. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% grounded. Alexander-Orbach d_w = 3.8 in 3D (numerical estimate, grounded in literature). T cell single-cell tracking in collagen matrices feasible (grounded — multiple labs do this). Viscoelastic subdiffusion range alpha = 0.5-0.9 (Metzler & Klafter 2000, grounded). Three-regime prediction (parametric — mapping from lattice theory). Active correction for MSD exponent (parametric — unknown for 3D active percolation). Crucially, Riedl et al. 2020 provides a published alternative explanation for the same observation, and Krummel 2016 establishes run-and-pause as an independent cause of the predicted alpha value. |
| **Composite (pre-bonus)** | | **5.75** | 0.20x6 + 0.20x6 + 0.10x9 + 0.20x5 + 0.05x5 + 0.05x4 + 0.20x5 = 1.20 + 1.20 + 0.90 + 1.00 + 0.25 + 0.20 + 1.00 = 5.75 |
| Cross-domain bonus | | +0.5 | Fractal geometry / anomalous diffusion theory -> tumor immunology diagnostics: 2+ disciplinary boundaries crossed. |
| **Composite (final)** | | **6.25** | |

---

### Hypothesis H4: BAPN Dose-Response Predicts a Sharp Nonlinear Phase Transition in Immune Infiltration — LOX Inhibitor as Percolation Control Knob

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed NOVEL. Nicolas-Boluda 2021 tested a single BAPN dose combined with anti-PD-1 — it is not a dose-response experiment and does not examine the shape of the dose-response curve. No papers connect BAPN dose-response shape to percolation physics or predict that the shape should be a power-law onset rather than a Hill equation. The specific prediction that the percolation signature is distinguishable from standard pharmacology by the shape of the infiltration onset curve is genuinely novel. |
| Mechanistic Specificity | 20% | 8 | Names specific drug with known pharmacodynamics (BAPN, irreversible LOX inhibitor, covalent mechanism verified), specific exponent for dose-response onset (I(d) ~ (d - d_c)^beta with beta = 0.41, universal, not a free parameter), specific contrast with Hill equation (smooth sigmoid vs. true zero below threshold), and ECM equilibration timescale requirement (48-72 hours minimum for new crosslink formation to be blocked and existing crosslinks to turn over). Identifies the two unknowns (dose -> LOX activity mapping; LOX activity + MMP rate -> equilibrium crosslink density) clearly. The citation date error (Tang 2017 cited; correct is Tang 1983) is noted but does not affect the mechanism. Score of 8 because the mechanism is highly specific even with the two unknowns explicitly flagged. |
| Cross-field Distance | 10% | 9 | Statistical mechanics (percolation phase transitions, order parameter exponents) -> tumor pharmacology (BAPN dosing, LOX inhibition, ECM remodeling kinetics) -> tumor immunology (CD8+ T cell infiltration). This is a three-domain bridge: physics, pharmacology, and immunology. Score of 9 for the same baseline as other hypotheses in this set. |
| Testability | 20% | 8 | This is the most directly testable hypothesis in the set. The experiment sweeps through p_c by design (increasing BAPN dose decreases crosslink density), rather than requiring tumors to happen to be near p_c. Standard animal model (4T1 breast, KPC pancreatic), established BAPN dosing protocols (7-day treatment used in Nicolas-Boluda 2021), quantitative readouts (CD8+ T cell density by IHC, crosslink density by pyridinoline assay, total collagen by hydroxyproline assay). 6-12 months, requiring animal work (IACUC) and 8-10 dose groups. The predicted result if TRUE (sharp sigmoid with beta = 0.41 onset, universal exponent across tumor types despite different d_c) and if FALSE (Hill equation with variable coefficient) are quantitatively distinguishable with standard regression. |
| Impact: Paradigm | 5% | 6 | Reframes LOX inhibition from a collagen density reduction strategy to a percolation control parameter strategy, introducing the concept of a critical dose rather than a maximal tolerated dose for ECM-targeted immunotherapy. This is a significant conceptual reframing within the tumor immunology subfield. |
| Impact: Translational | 5% | 8 | LOX inhibitors are in clinical trials for fibrosis (direct translational context). The percolation prediction provides a quantitative dosing principle: find the critical dose that crosses the percolation threshold, not the maximum dose. This is immediately actionable in trial design. Combined LOX inhibitor + immunotherapy is an active area. The quantitative shape prediction (beta = 0.41, not a Hill coefficient) would be testable in Phase I dose-finding studies. |
| Groundedness | 20% | 6 | Critic assessed approximately 65% grounded. BAPN mechanism is correctly described despite citation date error (Tang 1983, not 2017, confirmed from MedChemExpress and multiple sources). Nicolas-Boluda 2021 qualitative direction verified (BAPN + anti-PD-1 improves infiltration). MMP crosslink turnover timescale (MMP-1 t_1/2 ~ 4-12 hours) grounded. beta = 0.41 is textbook-grounded. Phase transition shape prediction is parametric (mapping from percolation to pharmacology not demonstrated). p(dose) function is parametric and load-bearing. Score of 6 rather than 7 because the key novel prediction (shape of dose-response) is entirely parametric and contingent on H1's lattice mapping being valid. |
| **Composite (pre-bonus)** | | **7.60** | 0.20x8 + 0.20x8 + 0.10x9 + 0.20x8 + 0.05x6 + 0.05x8 + 0.20x6 = 1.60 + 1.60 + 0.90 + 1.60 + 0.30 + 0.40 + 1.20 = 7.60 |
| Cross-domain bonus | | +0.5 | Statistical mechanics -> pharmacology -> tumor immunology: 3-domain bridge, 2+ disciplinary boundaries. |
| **Composite (final)** | | **8.10** | |

---

### Hypothesis H6: MMP/LOX Kinetic Balance Creates Dynamic Percolation, Generating Temporal Windows of Immune Infiltration in Tumors

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed NOVEL. No papers apply dynamic percolation theory to ECM remodeling or immune infiltration. The concept of temporal windows of immune infiltration arising from oscillatory MMP/LOX balance — with T cells either catching the window (reaching tumor core) or missing it (producing peri-tumoral accumulation) — is not present in the literature. Score of 8 because the qualitative concept of ECM remodeling enabling immune access is discussed in the field; the percolation formalization and temporal window quantification are the novel contributions. |
| Mechanistic Specificity | 20% | 5 | Provides a kinetic model (p_ss = k_LOX/(k_LOX + k_MMP)), identifies specific molecular players (>20 MMPs, 4 LOX family members, STRING interactions with TGFB1 = 0.623, IL1B = 0.727, CCL2 = 0.710), gives a timescale analysis (LOX crosslinking hours, MMP degradation 4-12 hours, T cell transit 10-200 minutes), and predicts pulsatile infiltration correlated with MMP activity peaks. The critical weakness: the kinetic model is acknowledged to be a dramatic simplification of a complex regulatory network (20+ MMPs, 4 TIMPs, spatial heterogeneity in enzyme expression). The steady-state formula p_ss = k_LOX/(k_LOX + k_MMP) ignores spatial heterogeneity, cooperative regulation, and the fact that LOX-crosslinked collagen is specifically resistant to MMP degradation (potentially invalidating the timescale matching). |
| Cross-field Distance | 10% | 9 | Non-equilibrium statistical mechanics (dynamic percolation, time-dependent bond processes) -> tumor ECM kinetics -> tumor immunology. The dynamic percolation framework is a distinct and more sophisticated branch of statistical mechanics than static percolation, adding an additional disciplinary distance beyond H1. Score of 9 consistent with other hypotheses in this set. |
| Testability | 20% | 6 | The ex vivo organotypic tumor slice culture with fluorescent CD8+ T cells + SHG imaging + DQ-collagen fluorescent MMP activity sensors is technically feasible in a specialized lab. Correlating temporal MMP activity peaks (r > 0.5) with T cell infiltration bursts over 48 hours of time-lapse imaging is a clear and measurable prediction. However, several concerns reduce testability: (1) the Critic identified that LOX-crosslinked collagen may be resistant to MMP degradation (timescale days-weeks, not hours), making the predicted dynamic range potentially unobservable on the experiment's timescale; (2) the organotypic culture system requires fresh tumor tissue and expertise in ex vivo culture; (3) real-time MMP activity sensors are specialized reagents not standard in all immunology labs. Score of 6 reflects feasibility in a specialized lab but significant barriers. |
| Impact: Paradigm | 5% | 7 | The dynamic percolation view of immune exclusion reframes the clinical observation of peri-tumoral T cell accumulation from a static barrier (H1 framework) to a dynamic timing failure. This would suggest that the same tumor can be permissive or restrictive at different times, opening the concept of immunotherapy timing windows. This is a conceptually significant reframing even if the molecular details are uncertain. |
| Impact: Translational | 5% | 6 | If infiltration is temporally gated by MMP/LOX balance, the translational implication is to synchronize immunotherapy administration with peak MMP activity (or to use MMP activators to open windows). This is a concrete, clinically testable strategy. The clinical feasibility of MMP activity monitoring in patients is a barrier, but the principle is actionable. |
| Groundedness | 20% | 4 | Critic assessed approximately 55% of named components as grounded, but the key mechanistic elements are parametric. Grounded: LOX crosslinking (Nicolas-Boluda 2021), MMP degradation biology (Lu et al. 2011), STRING interaction scores for LOX (TGFB1, IL1B, CCL2 — confirmed from computational validation), peri-tumoral T cell accumulation (Salmon et al. 2012), T cell migration speed (Krummel 2016). Parametric: kinetic rate constants for LOX and MMPs, p(t) model, pulsatile infiltration prediction, timescale matching for LOX-crosslinked (not free) collagen. Critical: Salmon 2012 explicitly attributes peri-tumoral trapping to collagen FIBER ALIGNMENT, not network connectivity — this is a direct alternative explanation for the key observation the hypothesis is built to explain, and it is grounded in the literature. This reduces groundedness of the hypothesis's explanatory claim substantially. Score of 4. |
| **Composite (pre-bonus)** | | **6.15** | 0.20x8 + 0.20x5 + 0.10x9 + 0.20x6 + 0.05x7 + 0.05x6 + 0.20x4 = 1.60 + 1.00 + 0.90 + 1.20 + 0.35 + 0.30 + 0.80 = 6.15 |
| Cross-domain bonus | | +0.5 | Non-equilibrium statistical mechanics -> ECM kinetics -> tumor immunology: 2+ disciplinary boundaries. |
| **Composite (final)** | | **6.65** | |

---

### Hypothesis H8: Directed Percolation from Chemotaxis — T Cell Migration Shifts to Directed Percolation Universality Class

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic confirmed NOVEL. No papers analyze whether T cell infiltration follows isotropic or directed percolation universality. Jiang 2016 used isotropic percolation for tumor cell proliferation without addressing chemotactic directionality. Wang 2025 involves surface cascade, not directional transport. The prediction that chemotaxis shifts the universality class — changing the mathematical framework's predictions rather than merely adding a correction term — is entirely novel. The self-limiting framing (this hypothesis specifies when H1-H4 fail) adds further intellectual novelty. |
| Mechanistic Specificity | 20% | 6 | Names specific exponents (nu_parallel = 1.73, nu_perp = 1.10 in 3D DP, from Hinrichsen 2000), identifies the crossover condition (Pe ~ 1), defines a specific observable (anisotropic correlation function ratio xi_parallel/xi_perp diverges as p -> p_c), and maps the condition to chemokine sources (CCL5, CXCL9/10 from Nagarsheth 2017). The significant mechanistic weakness: directed percolation requires a single fixed preferred direction. Real tumor chemokine gradients are multi-source, non-monotonic, and spatially variable — potentially averaging to isotropic on length scales comparable to xi. The Pe ~ 3 estimate places the system in the crossover regime where neither isotropic nor directed percolation exponents apply cleanly, leaving the core prediction (which exponents to expect) ambiguous. |
| Cross-field Distance | 10% | 9 | Directed percolation (non-equilibrium statistical mechanics, distinct universality class from standard percolation) -> chemokine signaling (cell biology, receptor biology) -> tumor immunology. Requires simultaneous expertise in non-equilibrium phase transitions and cancer immunology. Score of 9 consistent with the set. |
| Testability | 20% | 4 | The test requires: (1) inferring chemokine gradient orientation from combined CXCL9/10 immunostaining in tumor sections, (2) measuring T cell pair correlation functions separately along parallel and perpendicular directions, (3) extracting xi_parallel and xi_perp independently from these directional correlation functions, (4) repeating across multiple samples near p_c. This requires a specialized computational pipeline not standard in any tumor immunology lab and a large annotated dataset with known gradient orientation. The Critic notes this is "practically difficult to test." Additionally, Pe ~ 3 sits in the crossover regime, meaning the expected values of xi_parallel/xi_perp are not precisely predicted, weakening the falsifiability of the specific quantitative test. Score of 4 reflects a meaningful observable that is technically very demanding to measure. |
| Impact: Paradigm | 5% | 7 | Establishing the correct universality class for T cell infiltration would be a significant theoretical result: it would specify which mathematical framework (isotropic vs. directed percolation) governs the entire hypothesis family and correct the predictions of H1-H4. If the system is in the DP class, then nu = 0.88 is wrong and nu_parallel = 1.73 is right — a 2x correction to the key exponent. This is paradigmatically important for the percolation framework as applied to immunology. |
| Impact: Translational | 5% | 3 | Identifying the universality class has minimal direct translational value. The practical treatment strategy (inhibit LOX, cross the percolation threshold) remains the same regardless of whether the exponent is 0.88 or 1.73. The translational benefit is indirect: using the correct exponents produces more accurate quantitative dosing predictions. |
| Groundedness | 20% | 5 | Critic assessed approximately 55% grounded. Verified: directed percolation exponents nu_parallel = 1.73, nu_perp = 1.10 in 3D (Hinrichsen 2000, Adv Phys 49:815-958, confirmed). T cell chemotaxis toward CXCL9/10 (Nagarsheth et al. 2017, Nat Rev Immunol, grounded). Parametric: Pe ~ 3 estimate (from computational validation, not independently verified), isotropic-to-directed crossover at Pe ~ 1 (standard physics expectation, not demonstrated for biological system), anisotropic correlation length measurement in tumors (novel proposal). The internal consistency concern (H8 predicts the directed DP class while H2 assumes isotropic DP class) is a structural weakness across the hypothesis set. |
| **Composite (pre-bonus)** | | **6.20** | 0.20x9 + 0.20x6 + 0.10x9 + 0.20x4 + 0.05x7 + 0.05x3 + 0.20x5 = 1.80 + 1.20 + 0.90 + 0.80 + 0.35 + 0.15 + 1.00 = 6.20 |
| Cross-domain bonus | | +0.5 | Directed percolation / non-equilibrium phase transitions -> chemokine biology -> tumor immunology: 2+ disciplinary boundaries. |
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

**H1 vs H4**: H4 is explicitly derivative of H1 — it is the pharmacological operationalization of H1's framework. H4 states: "If LOX crosslinks map to bond occupation probability (H1), then BAPN provides a control knob for p." They share the same bridge mechanism (LOX crosslink density = p), the same quantitative prediction (beta = 0.41 onset), and the same experimental system. However, H4 is not a minor variation — it is a distinct experimental prediction (dose-response shape vs. matrix density scan) with distinct translational implications (drug dosing principle). These are connected but not redundant: H1 tests the existence of the sharp transition; H4 tests whether a clinical drug can produce it. They should both be selected.

**H1 vs H2**: Partially overlapping — both depend on H1's lattice mapping, but H2 focuses on universality across tumor types (correlation length scaling) rather than the phase transition itself. Different experimental systems (multi-tumor correlation function measurement vs. single-tumor infiltration density scan) and different testable predictions. H2 is not redundant with H1 though it is downstream.

**H4 vs H2**: H4 tests for the critical exponent beta in dose-response; H2 tests for the critical exponent nu in spatial clustering. Different experimental approaches, different biological systems, different predictions. Not redundant.

**H2 vs H8**: These are internally contradictory — H2 assumes isotropic percolation (nu = 0.88) while H8 argues the system belongs to the directed percolation class (nu_parallel = 1.73). They connect the same subfields (percolation theory x T cell clustering) but make incompatible predictions. Including both is scientifically appropriate: one of them is right and the other wrong, and both are testable. H8 provides a diagnostic test for which exponent applies.

**H8 vs H6**: Different bridge mechanisms — H8 concerns the universality class (isotropy of the walker), H6 concerns the temporal evolution of the lattice (dynamic percolation). Different experimental systems, different predictions. Not redundant.

**H1 vs H6**: H6 is an extension of H1 to the dynamic case. They share the underlying LOX = bond occupation probability mapping but H6 asks what happens when p(t) fluctuates rather than being static. They address different aspects (static threshold vs. temporal dynamics) and require different experimental systems. Not redundant.

**Convergence assessment**: The top-5 do NOT constitute 3+ conceptually similar hypotheses. H1 and H4 are the most closely related, but they are genuinely distinct experiments. H2 and H8 are mutually exclusive predictions that together serve as diagnostic tests for the correct universality class. H6 addresses temporal dynamics rather than threshold existence. The top-5 spans:
- Static phase transition existence (H1)
- Pharmacological threshold crossing (H4)
- Cross-tumor universality (H2)
- Framework boundary condition / universality class (H8)
- Temporal window / dynamic ECM (H6)

**Diversity check PASSES.** No adjustment needed. The top-5 is mechanistically diverse despite all drawing on percolation theory as the bridge concept.

**Note**: H3 (MSD fingerprint) is left at rank 6 because it is the weakest hypothesis (affirming-the-consequent logic issue, published alternative explanation from Riedl 2020, insufficient as sole diagnostic). No diversity promotion needed.

---

## Elo Tournament Sanity Check (Top 6: H1, H4, H2, H8, H6, H3)

15 pairwise comparisons (N=6, N*(N-1)/2 = 15):

**H1 vs H4**: A researcher would test H1 first because it is the foundational hypothesis — H4's prediction is explicitly contingent on H1 being true. Testing H1 (do tumors show a sharp percolation transition in ECM density?) is the necessary prerequisite before H4 (does BAPN dose-response follow percolation shape?). H1 wins.

**H1 vs H2**: A researcher would test H1 first because H2's universality prediction requires knowing that the system is in the percolation universality class (established by H1). H1 also requires simpler experimental infrastructure (single collagen gradient, one tumor type). H1 wins.

**H1 vs H8**: H1 should be tested first to establish whether percolation applies at all before asking which universality class it belongs to (H8). H1 also has a more direct experimental design. H1 wins.

**H1 vs H6**: H1 (static percolation) is the simpler and more fundamental hypothesis. H6 (dynamic percolation) requires H1's framework to be established first and additionally requires the ECM to be dynamic on T cell transit timescales — an added requirement. H1 wins.

**H1 vs H3**: H1 is more fundamental and has higher groundedness than H3, which suffers from the affirming-the-consequent confound. H1's predictions (sharp phase transition in infiltration density) are more directly testable and interpretable. H1 wins.

**H4 vs H2**: H4 is directly testable with a controlled animal experiment that sweeps through p_c by design. H2 requires tumors to happen to sit near p_c, which cannot be engineered. H4 is more immediately actionable for a researcher. H4 wins.

**H4 vs H8**: H4's dose-response experiment provides quantitative data on the existence of the transition. H8's directed percolation test requires inferring gradient orientation from immunostaining and measuring anisotropic correlation functions — a substantially more complex experimental challenge with an ambiguous expected value (Pe ~ 3 is in the crossover regime). H4 wins.

**H4 vs H6**: H4 sweeps through p_c experimentally and generates a clean dose-response curve. H6 requires time-lapse organotypic culture with real-time MMP sensors — technically much more demanding, with uncertain timescale matching (LOX-crosslinked collagen may not degrade on the timescale of the experiment). H4 wins.

**H4 vs H3**: H4 is more directly testable and has cleaner falsifiable predictions. H3's MSD fingerprint requires ruling out run-and-pause subdiffusion as confound, adding substantial analysis burden. H4 wins.

**H2 vs H8**: A researcher would test H2 first as a confirmatory test of universality within the isotropic percolation framework, before the more esoteric question of whether the framework needs to be replaced by directed percolation (H8). H2 also provides a quantitative output (correlation length data collapse) that is inherently informative regardless of whether the slope matches nu = 0.88. H2 wins.

**H2 vs H6**: H2's prediction (cross-tumor data collapse) is experimentally cleaner despite requiring tumors near p_c. H6's dynamic percolation prediction requires time-resolved imaging with MMP sensors — more technically demanding with uncertain timescales. H2 wins.

**H2 vs H3**: H2's universality prediction is more ambitious and falsifiable than H3's fingerprint prediction (which suffers from the run-and-pause confound). A researcher wanting a high-impact result would tackle H2 over H3. H2 wins.

**H8 vs H6**: H8 asks which universality class governs T cell migration (a more fundamental question); H6 asks about temporal dynamics. H8's framework applicability question has broader implications for the entire hypothesis set. However, H6's experimental test (time-lapse organotypic culture) is more tractable than H8's anisotropic correlation function measurement. Both are low confidence hypotheses. H8 very narrow win for conceptual priority.

**H8 vs H3**: H8 is more novel (NOVEL vs. PARTIALLY NOVEL) and the directed percolation question is more fundamental. H3 has a confounding mechanism problem. H8 wins.

**H6 vs H3**: H6 has a clear prediction (pulsatile infiltration correlated with MMP peaks) and a direct experimental test (time-lapse organotypic culture). H3's fingerprint claim is undermined by the run-and-pause confound. H6 wins.

### Elo Win Tally:

| Hypothesis | Wins | Losses | Win Rate | Elo Rank |
|------------|------|--------|----------|----------|
| H1 | 5 | 0 | 5/5 = 1.00 | 1 |
| H4 | 4 | 1 | 4/5 = 0.80 | 2 |
| H2 | 3 | 2 | 3/5 = 0.60 | 3 |
| H8 | 2 | 3 | 2/5 = 0.40 | 4 |
| H6 | 1 | 4 | 1/5 = 0.20 | 5 |
| H3 | 0 | 5 | 0/5 = 0.00 | 6 |

### Elo vs. Linear Ranking Comparison:

| Rank | Linear Composite | Elo Tournament |
|------|-----------------|----------------|
| 1 | H1 (8.30) | H1 |
| 2 | H4 (8.10) | H4 |
| 3 | H2 (7.05) | H2 |
| 4 | H8 (6.70) | H8 |
| 5 | H6 (6.65) | H6 |
| 6 | H3 (6.25) | H3 |

**Elo confirms linear ranking.** Both methods produce the identical ranking H1 > H4 > H2 > H8 > H6 > H3. The pairwise tournament captures an implicit prioritization dimension (foundational vs. derivative hypotheses) that reinforces the linear composite: H1 is the foundational mapping; H4 is the pharmacological test; H2 tests universality; H8 tests framework boundary conditions; H6 adds temporal complexity; H3 has a confounding mechanism problem. This consistent ordering increases confidence in selecting H1, H4, and H2 as the primary evolution candidates.

---

## Evolution Selection

**Selected for Cycle 2 Evolution: H1, H4, H2**

Top-3 composite scores: H1 (8.30), H4 (8.10), H2 (7.05). All scores are below the 6.5 threshold for Evolver skip only when ALL top-3 are >= 6.5. The scores exceed 6.5 so the skip condition requires top-3 >= 6.5 — that condition IS met (7.05, 8.10, 8.30). However, none of the top-3 scores reach the >= 7.0 early-completion threshold for Cycle 1. Recommend RUNNING the Evolver on H1, H4, H2.

**Also carry forward to Evolver for potential promotion: H8, H6**

These two provide distinct mechanistic angles (universality class boundary and temporal dynamics) that diversify the evolved hypothesis pool. H8 addresses when H1-H4 predictions fail, which is scientifically valuable even if H8 itself is hard to test. H6 adds the temporal dimension that static percolation ignores.

**H3 (MSD fingerprint) is the lowest priority for evolution.** The affirming-the-consequent problem and the published alternative explanation (Riedl 2020) make it the weakest candidate. If Evolver capacity is limited to 3-5 hypotheses, H3 should be deprioritized.

**Evolver instructions for cycle 2:**
- H1: Address the disordered lattice abstraction problem — can Voronoi network percolation (random geometric graph) replace the regular lattice and still recover the same universality class? Quantify how much intratumoral heterogeneity smears the transition.
- H4: Correct Tang citation (1983 not 2017). Estimate the shape of p(dose) function for BAPN given known LOX enzyme kinetics and MMP turnover rates. Assess whether a cooperative LOX activity threshold (if it exists) would produce spurious inflections.
- H2: Address the directed percolation concern (H8) directly — what is the effective universality class for Pe ~ 3 active particles? If the exponents are uncertain, can the test be redesigned to measure the exponent rather than assume it equals 0.88?
