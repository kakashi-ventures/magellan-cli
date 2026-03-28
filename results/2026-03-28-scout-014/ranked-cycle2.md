# Ranked Hypotheses — Cycle 2
# Session: 2026-03-28-scout-014
# Target: Non-equilibrium statistical mechanics (Mpemba effect spectral theory) x Neurodegenerative protein biochemistry (amyloid aggregation selectivity)
# Ranker: Sonnet 4.6 (structured scoring mode)
# Cycle: 2
# Date: 2026-03-28

---

## Scoring Notes

**Survivors evaluated (5 total):** C2-H1, C2-H2, C2-H4, C2-H5, C2-H7.
Killed in cycle 2 critique: C2-H3 (evolutionary tradeoff), C2-H6 (tau PTM biomarker), C2-H8 (chaperone Mpemba).

**Cross-domain bonus eligibility:** All five surviving hypotheses bridge non-equilibrium statistical mechanics / mathematical physics to protein biochemistry / neurodegenerative disease biology, spanning at least two disciplinary boundaries (physics -> chemistry -> biology). The +0.5 cross-domain bonus applies to all five hypotheses per v5.8 rules.

**Groundedness penalties applied per Critic assessment:**
- C2-H1: Chakraborty PNAS pages cited as 16817 (actual: 19926); ~75% grounded after correcting this as a citation detail error (paper content accurate, pages fabricated). One moderate penalty.
- C2-H2: Bowman & Geissler 2012 slightly mischaracterized as "ensemble docking" when it is cryptic pocket discovery; ~65% grounded.
- C2-H4: All four grounded citations verified; sigma-spike magnitude is derived (speculative) not fabricated; ~80% grounded. No penalty.
- C2-H5: Cohen et al. 2012/109:9761 persistent error (actual: 2013/110:9758) — flagged in cycle 1 critique and NOT corrected; ~75% grounded. Penalized for failure to self-correct.
- C2-H7: All citations verified; ~80% grounded. No penalty.

**Comparison baseline (Cycle 1 Quality Gate results):**
- E-H5: 7.0 (adjusted) — bimodal eigenspectrum from Zwanzig roughness
- E-H4: 6.5 — cooling protocol suppresses fibril formation
- E-H1: 6.5 — Mpemba index classifier
- E-H7: 6.0 — eigenmode branching -> polymorph selection
- Best cycle 1 Ranker composite: H5 = 7.50 (pre-QG)

---

## Per-Hypothesis Scoring Tables

---

### C2-H5: Refined Hierarchical Spectral Scoring with Yu et al. D_misfold Calibration and Cross-Validation Against TANGO/CamSol

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The Critic confirms no published work combines Zwanzig roughness calibration with MSM eigenspectral scoring and secondary nucleation kinetics into a three-level hierarchy. The new elements added in cycle 2 — anchoring to Yu et al. measured D_misfold/D_fold and introducing TANGO/CamSol cross-validation — meaningfully advance beyond the cycle 1 version. Score 8 rather than 9 because this is an iterative refinement of cycle 1 E6-H1xH5 rather than a conceptually novel bridge; the component frameworks are each established independently. |
| Mechanistic Specificity | 20% | 8 | Three-level hierarchy is fully specified: Level 1 anchors epsilon_misfold ~ 3.3 kT from Yu et al. 2015 measured D ratio; Level 2 uses BC > 0.555 bimodality threshold; Level 3 introduces k_n ~ k_+ * M_eff * c^(n_c) concentration correction from Cohen et al. secondary nucleation. Cross-validation against TANGO/CamSol with predicted rho = 0.4-0.7 is a precisely quantitative orthogonality claim. The functional form of k_n is postulated rather than derived from first principles, which prevents a score of 9, but the overall mechanistic architecture is the most concrete of any cycle 2 hypothesis. |
| Cross-field Distance | 10% | 7 | Bridges statistical mechanics (Zwanzig roughness, 1988) through biophysical chemistry (MSM eigenspectral analysis) to amyloid biochemistry (secondary nucleation kinetics, TANGO sequence-based predictor). The bridge is real but the component fields share the MSM formalism as common currency, reducing effective distance compared to a pure physics-to-biology bridge. Score unchanged from cycle 1 H5 baseline; the cross-validation against TANGO adds a sequence biology element without fundamentally changing the disciplinary span. |
| Testability | 20% | 8 | Five specific predictions with quantitative ranges and explicit refutation criteria: epsilon_misfold in 2.8-3.8 kT for 4 proteins; M_eff vs TANGO rho = 0.4-0.7; M_eff better than TANGO for >= 2 disagreements; Abeta42 lag times at 1/5/25 uM within 2-fold; automatic self-refutation if rho > 0.9 (TANGO already captures everything). Standard tools (PyEMMA, TANGO server, ThT assay) support all steps. The timeline is 4-6 months for a well-resourced computational biophysics group. Score 8 (not 9) because constructing the full 8-protein MSM panel is the same bottleneck as cycle 1 — the testability advances are on the validation side, not the primary data generation side. |
| Impact: Paradigm | 5% | 6 | If the three-level hierarchy is validated and M_eff adds orthogonal information beyond TANGO, it would establish spectral physics as a complementary predictor to sequence-based aggregation tools — a meaningful extension of the current paradigm but not an overthrow of it. The framework's primary contribution is mechanistic interpretation of a known phenomenon (why some proteins are more amyloidogenic), not prediction of a new one. Score 6: extends existing frameworks, opens a new physical-chemical approach to neurodegeneration. |
| Impact: Translational | 5% | 5 | A validated M_eff score could be incorporated into computational aggregation risk assessment pipelines for therapeutic protein engineering (reducing aggregation propensity of biopharmaceuticals) and potentially for identifying aggregation-prone sequence variants in neurodegeneration. The translational pathway is plausible but requires multiple additional validation steps (in vitro, cell models, clinical relevance). Score 5: eventual applications are clear but the clinical pathway is multi-step. |
| Groundedness | 20% | 7 | Yu et al. 2015 PNAS 112:8308 verified; Fernandez-Escamilla et al. 2004 Nat. Biotechnol. 22:1302 (TANGO) verified; Zwanzig 1988 verified; BC threshold verified. The persistent Cohen et al. citation error (cited as 2012/109:9761, actual 2013/110:9758) was flagged in cycle 1 and not corrected in cycle 2 — this is penalized as a self-correction failure. The paper content is accurate but the citation details are wrong. Grounding is approximately 75% (strong theoretical grounding, one persistent citation error). Score 7 reflects solid grounding with a documented and uncorrected citation error. |
| **Composite (pre-bonus)** | | **7.55** | Novelty: 8*0.20=1.60; Mech. Spec.: 8*0.20=1.60; Cross-field: 7*0.10=0.70; Testability: 8*0.20=1.60; Paradigm: 6*0.05=0.30; Translational: 5*0.05=0.25; Groundedness: 7*0.20=1.40. Sum = 7.45. |
| **Cross-domain bonus** | | **+0.5** | Physics (Zwanzig 1988 statistical mechanics, Mpemba formalism) -> Chemistry (protein energy landscape, D_misfold measurements) -> Biology (amyloid secondary nucleation kinetics, clinical aggregation assays): 2+ disciplinary boundaries confirmed. Cross-domain bonus applied: +0.5 |
| **Composite (final)** | | **7.95** | 7.45 + 0.50 |

*Note: Arithmetic check — 1.60+1.60+0.70+1.60+0.30+0.25+1.40 = 7.45 (pre-bonus), 7.45+0.50 = 7.95 (final).*

---

### C2-H7: Cooling-Rate-Dependent Fibril Polymorph Selection in Insulin: Refined T_cross Prediction with Three-Arm Mechanism Discrimination

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The Critic confirms that while temperature-dependent insulin polymorphism is known (Jimenez 2002, Nielsen 2001), the eigenmode-based T_cross prediction and the three-arm mechanism discrimination design (distinguishing eigenmode branching from Ostwald competition) are entirely novel. No published work applies MSM eigenmode decomposition to predict a quantitative polymorph-switching temperature or uses the specific intermediate-cooling-rate arm to adjudicate between competing mechanisms. Score 8: specific bridge is novel; the broader phenomenon (conditions affect polymorphs) has prior literature, preventing a score of 9. |
| Mechanistic Specificity | 20% | 8 | The mechanism is precisely stated: eigenmodes v_2 and v_3 correspond to distinct misfolded basins; temperature-dependent overlap coefficients c_k(T) = <P(T)|v_k> determine which basin dominates; T_cross is where c_2(T_cross) = c_3(T_cross). The critical experimental discriminant at the intermediate cooling rate is cleanly specified: eigenmode branching predicts polymorph A (high-T composition not yet relaxed), Ostwald predicts polymorph B (more stable). The T_cross prediction of 45-55C is quantitative. The score does not reach 9 because the claim of exactly two dominant eigenmodes (v_2, v_3) in insulin at pH 2 is an assumption rather than a result — the eigenspectrum may be denser. |
| Cross-field Distance | 10% | 7 | Bridges non-equilibrium statistical mechanics (MSM eigendecomposition, Mpemba formalism) through computational biophysics to experimental protein chemistry (insulin fibrillation, cryo-EM/FTIR/ssNMR characterization). The insulin fibrillation community and the Mpemba physics community have no overlap. Score 7 rather than 8 because the bridge to actual prion or neurodegeneration biology (score 9 in cycle 1 H7) has been narrowed to insulin fibrillation, which is a more proximate domain to physical chemistry. The tradeoff is lower disciplinary distance for dramatically better testability. |
| Testability | 20% | 9 | This is the most practically testable hypothesis in the cycle 2 set. The three-arm experiment (rapid quench, 0.1 C/min, 0.5 C/min) requires standard laboratory equipment (ThT fluorimeter, FTIR spectrometer, temperature-controlled incubator). Insulin fibrillation at pH 2 is a routine model system. Cryo-EM, FTIR, and ssNMR are standard characterization tools available at most major research institutions. The computational component (REMD of insulin B-chain) is tractable — insulin B-chain is a 30-residue peptide, orders of magnitude more manageable than full Abeta42 MSMs. A PhD student could execute the three-arm experimental component in 2-3 months; the computational T_cross prediction adds 2-3 more months. Score 9: the experimental test is executable essentially immediately; only the MSM-based T_cross prediction requires new computation. |
| Impact: Paradigm | 5% | 6 | If eigenmode branching is validated as the mechanism of polymorph selection in insulin, it would extend the Mpemba framework to a new domain (polymorphism) and provide the first quantitative physical explanation for a widely observed but poorly understood phenomenon (condition-dependent fibril polymorphism). This opens a new predictive approach to polymorph control in both research and pharmaceutical manufacturing. Score 6: significant extension of existing framework; unlikely to open a new field but would enrich both the Mpemba and protein polymorphism literatures substantially. |
| Impact: Translational | 5% | 7 | Insulin fibril polymorphism is directly relevant to pharmaceutical formulation: different polymorphs have different stability and immunogenicity profiles. A validated T_cross prediction tool for polymorph control would have immediate application in biopharmaceutical manufacturing (controlling the cooling protocols during insulin formulation to select desired polymorph). More concretely translational than other cycle 2 hypotheses. Score 7: clear manufacturing application if validated; polymer control is an active industrial concern for therapeutic proteins. |
| Groundedness | 20% | 8 | Jimenez et al. 2002 PNAS 99:9196 verified (correct title, volume, pages); Nielsen et al. 2001 Biochemistry 40:6036 verified; Klich et al. 2019 PRX 9:021060 verified. No fabricated citations. The T_cross prediction (45-55C) is clearly labeled as speculative and derivable from computational predictions, not from existing data. The stochastic polymorphism concern is acknowledged. Insulin fibril characterization methods are standard and correctly cited. Groundedness approximately 80%. Score 8: cleanest citation record in the cycle 2 set. |
| **Composite (pre-bonus)** | | **8.10** | Novelty: 8*0.20=1.60; Mech. Spec.: 8*0.20=1.60; Cross-field: 7*0.10=0.70; Testability: 9*0.20=1.80; Paradigm: 6*0.05=0.30; Translational: 7*0.05=0.35; Groundedness: 8*0.20=1.60. Sum = 7.95. |
| **Cross-domain bonus** | | **+0.5** | Physics (MSM eigendecomposition, Mpemba index formalism) -> Physical chemistry (protein energy landscape, molecular dynamics) -> Experimental biochemistry (insulin fibrillation, cryo-EM, pharmaceutical formulation): 2+ disciplinary boundaries confirmed. Cross-domain bonus applied: +0.5 |
| **Composite (final)** | | **8.45** | 7.95 + 0.50 |

*Note: Arithmetic check — 1.60+1.60+0.70+1.80+0.30+0.35+1.60 = 7.95 (pre-bonus), 7.95+0.50 = 8.45 (final).*

---

### C2-H1: Resource-Theoretic Mpemba Vulnerability Score: Relative Entropy of A* Ensemble as Unified Aggregation Predictor

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | The Critic's web searches confirm zero prior work connecting Avanzini et al. 2026 resource-theoretic Mpemba unification to protein A* excited states via D_KL(P_A* || P_eq). "KL divergence relative entropy protein folding Markov state model eigenmode" returns no relevant hits; "resource theory Mpemba protein" returns 0 results. The connection between the Avanzini 2026 PRX framework and Chakraborty 2020 PNAS A* states is genuinely original. Score 9 (not 10) because D_KL is a standard MSM convergence metric and the novelty is specifically in the aggregation prediction application; the mathematical tools are well-established. |
| Mechanistic Specificity | 20% | 7 | The mechanism is well-specified mathematically: D_KL(P_A* || P_eq) = sum_i P_A*(i) * ln(P_A*(i) / P_eq(i)), computable from any protein MSM; spectral decomposition as sum_k (c_k)^2 / (2|lambda_k|); canonical limit D_KL = delta_F/kT connecting to Chakraborty A* free energy gaps. Quantitative predictions include 1.5-fold lower D_KL for Abeta42 vs Abeta40, Spearman rho > 0.8 vs ThT, and >80% spectral concentration in 2 slowest eigenmodes for amyloidogenic proteins. The score does not reach 8 because the D_KL = delta_F/kT identity is valid only at equilibrium while P_A* is a non-equilibrium ensemble — the Critic identifies this as an overextension of a canonical identity to a non-canonical setting, which is a genuine mechanistic weakness. |
| Cross-field Distance | 10% | 8 | Bridges resource theory from quantum information / non-equilibrium statistical mechanics (Avanzini 2026 PRX framework) through protein MSM biophysics to amyloid biochemistry (Chakraborty 2020 PNAS A* excited states). The Avanzini 2026 framework itself spans quantum and classical Mpemba effects — connecting it to protein aggregation crosses from mathematical physics into biochemistry in a way that requires expert knowledge in both fields. Score 8: broader than the standard Mpemba-amyloid bridge due to the resource-theoretic element. |
| Testability | 20% | 6 | The computation of D_KL(P_A* || P_eq) from protein MSMs is straightforward once MSMs are constructed. The predictions are specific and falsifiable with Mann-Whitney tests. The core bottleneck is the same as cycle 1 H1: building reliable MSMs for 8 proteins, and identifying A* states consistently across proteins (the A* identification is algorithm-dependent, as the Critic notes). The D_KL computation itself is simpler than the Mpemba index (which requires eigendecomposition), but the A* identification step introduces a new algorithm-dependence concern. Score 6: testable in principle, requires substantial new MSM construction effort. Not executable by a PhD student in 3 months without pre-existing MD data. |
| Impact: Paradigm | 5% | 7 | If D_KL unifies the three-level hierarchy into a single computable scalar AND outperforms the Mpemba index alone (Spearman rho > 0.8 vs rho > 0.7), it would establish resource-theoretic relative entropy as the fundamental quantity governing amyloid aggregation vulnerability — a significant conceptual unification connecting quantum information theory to protein biochemistry. This would be a stronger paradigm claim than the Mpemba index alone because D_KL is a universal monotone that quantifies "distance from equilibrium." Score 7: genuine paradigm extension that would connect information theory to neurodegeneration; unlikely to open a new field but would produce a compelling conceptual unification. |
| Impact: Translational | 5% | 4 | The D_KL score would function as a computational aggregation risk predictor, similar to TANGO/Zyggregator but grounded in statistical mechanics. The translational pathway requires validation through multiple intermediate steps (MSM construction -> D_KL computation -> correlation with ThT -> correlation with cellular aggregation -> disease relevance). No direct clinical application is suggested beyond risk scoring. Score 4: longer translational pathway than C2-H5 or C2-H7; purely computational output at this stage. |
| Groundedness | 20% | 6 | Avanzini et al. 2026 PRX 16:011065 verified (resource-theoretic Mpemba unification); Klich et al. 2019 PRX 9:021060 verified; Lu & Raz 2017 PNAS 114:5083 verified. The Chakraborty et al. 2020 PNAS citation has wrong page numbers: cited as 117:16817, actual is approximately 117:19926-19937 (the Critic confirms the page number is fabricated while the content claim is accurate). The D_KL = delta_F/kT identity is correctly identified as a canonical ensemble approximation, not an exact relationship for non-equilibrium ensembles — this is a theory overextension, not a citation error, but it affects groundedness of the central mechanistic claim. Overall grounding approximately 75% by citation count, reduced to 6 for the combination of the fabricated page number and the overextended canonical identity. |
| **Composite (pre-bonus)** | | **7.10** | Novelty: 9*0.20=1.80; Mech. Spec.: 7*0.20=1.40; Cross-field: 8*0.10=0.80; Testability: 6*0.20=1.20; Paradigm: 7*0.05=0.35; Translational: 4*0.05=0.20; Groundedness: 6*0.20=1.20. Sum = 6.95. |
| **Cross-domain bonus** | | **+0.5** | Physics/quantum information (resource theory, Mpemba effect, PRX 2026) -> Biophysical chemistry (protein MSM, relative entropy) -> Biochemistry (A* excited states, amyloid aggregation): 2+ disciplinary boundaries confirmed; resource theory element adds a third boundary (quantum information theory). Cross-domain bonus applied: +0.5 |
| **Composite (final)** | | **7.45** | 6.95 + 0.50 |

*Note: Arithmetic check — 1.80+1.40+0.80+1.20+0.35+0.20+1.20 = 6.95 (pre-bonus), 6.95+0.50 = 7.45 (final).*

---

### C2-H4: Spectral Entropy Production Rate Distinguishes Folding from Misfolding Pathways in Non-Equilibrium Protein Dynamics

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The Critic's searches find active literature on stochastic thermodynamics of protein folding (PNAS 2024 entropy production in single-molecule experiments), but none applying Schnakenberg entropy production specifically to discriminate folding from misfolding trajectories in MSMs via a sigma-spike signature. The specific sigma-spike as a misfolding commitment diagnostic is genuinely novel. Score 8 rather than 9 because the broader area (entropy production in protein folding) is an active research field — the novelty is in the specific application and prediction, not in bringing entropy production to biology for the first time. |
| Mechanistic Specificity | 20% | 7 | The mechanism is concretely specified with the Schnakenberg formula (sigma(t) = sum_{i,j} [W_ij*P_j - W_ji*P_i] * ln[W_ij*P_j / W_ji*P_i]), the quantitative spike magnitude estimate (delta_sigma/sigma_baseline ~ 7 for epsilon differences of 3.3 vs 2.0 kT), and the specific temporal prediction (t_spike/tau_2 = 0.5-2.0). The formula is derived from verified parameters. Score 7 rather than 8 because the Critic identifies a genuine signal-to-noise concern: sigma(t) measures GLOBAL entropy production from all transitions, not just those entering the misfolding basin — the misfolding-specific spike may be obscured in the full system signal. The Prigogine regime distinction (folding = near-equilibrium, misfolding = far-from-equilibrium) is also not rigorously justified from a common 400K initial condition. |
| Cross-field Distance | 10% | 8 | Bridges stochastic thermodynamics / irreversible thermodynamics (Schnakenberg 1976, Seifert 2012) through non-equilibrium statistical mechanics to protein biochemistry (MSM trajectory analysis for amyloid systems). The Prigogine-regime analysis applied to molecular simulations is a connection rarely made between the stochastic thermodynamics community and the computational protein folding community. Score 8: genuine disciplinary distance, with the entropy production angle providing a new bridge mechanism distinct from the Mpemba index or resource-theoretic approaches of other cycle 2 hypotheses. |
| Testability | 20% | 7 | The test protocol is computationally well-specified: generate kinetic Monte Carlo trajectories from Abeta42 MSMs, apply Schnakenberg decomposition at each step, classify trajectories by endpoint, detect sigma-spikes. Standard tools (PyEMMA, MDTraj) support trajectory generation; the Schnakenberg calculation is standard stochastic thermodynamics. The bottleneck is the same MSM construction requirement as other cycle 2 hypotheses, but unlike C2-H1 or C2-H2, the subsequent computation (sigma(t) along trajectories) is straightforward once the MSM exists. Score 7: executable within 3-5 months for a group with existing Abeta42 MSM data; somewhat longer for a group building MSMs from scratch. The main testability risk is the signal-to-noise concern — the sigma-spike may not be detectable above background entropy production noise, which is an empirical question resolvable in the test itself. |
| Impact: Paradigm | 5% | 7 | If sigma(t) spike reliably identifies trajectory-level misfolding commitment, it would provide the first real-time thermodynamic readout of whether a protein molecule is on a folding or misfolding trajectory — a fundamentally new observable in protein biophysics. This would connect irreversible thermodynamics directly to single-molecule amyloid biology. Score 7: would open a new measurement paradigm in computational protein biophysics; the sigma-spike concept could generalize beyond amyloid to any system with competing metastable states. |
| Impact: Translational | 5% | 3 | The sigma-spike is a trajectory-level computational observable with no direct clinical or diagnostic application in the near term. Its translational value lies entirely downstream: if validated, it would identify which molecular trajectories lead to misfolding, which could eventually guide drug design (perturbing conditions to increase monotonic sigma trajectories). The pathway from computational trajectory classification to therapeutic application is long and indirect. Score 3: primarily a tool for mechanistic understanding; translational application is highly speculative at this stage. |
| Groundedness | 20% | 8 | All four grounded citations are fully verified by the Critic: Schnakenberg 1976 Rev. Mod. Phys. 48:571 (verified); Seifert 2012 Rep. Prog. Phys. 75:126001 (verified, 3668+ citations); Yu et al. 2015 PNAS 112:8308 (verified, D_misfold/D_fold ~ 10^-3 content confirmed); Zwanzig 1988 PNAS 85:2029 (verified). The sigma-spike magnitude estimate is derived from verified parameters using standard formulas — the Critic confirms the derivation is correct given stated assumptions. The speculation is clearly labeled (spike magnitude is derived, not independently measured). Score 8: strongest citation grounding in the cycle 2 set; no fabricated or misattributed citations. |
| **Composite (pre-bonus)** | | **7.30** | Novelty: 8*0.20=1.60; Mech. Spec.: 7*0.20=1.40; Cross-field: 8*0.10=0.80; Testability: 7*0.20=1.40; Paradigm: 7*0.05=0.35; Translational: 3*0.05=0.15; Groundedness: 8*0.20=1.60. Sum = 7.30. |
| **Cross-domain bonus** | | **+0.5** | Stochastic thermodynamics / irreversible thermodynamics (Schnakenberg, Seifert) -> Statistical mechanics of non-equilibrium systems (Markov chain dynamics) -> Protein biochemistry (amyloid trajectory analysis): 2+ disciplinary boundaries confirmed. Cross-domain bonus applied: +0.5 |
| **Composite (final)** | | **7.80** | 7.30 + 0.50 |

*Note: Arithmetic check — 1.60+1.40+0.80+1.40+0.35+0.15+1.60 = 7.30 (pre-bonus), 7.30+0.50 = 7.80 (final).*

---

### C2-H2: Mpemba-Guided Aggregation Inhibitor Design: Small Molecules That Maximize Eigenmode Overlap Disruption

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | The Critic confirms that eigenmode-overlap as a drug design criterion is entirely unexplored. "Eigenmode overlap drug design MSM protein misfolding small molecule" returns no relevant results. The concept of designing small molecules to minimize <P_drug|v_slow> — the overlap integral with the slowest misfolding eigenmode — as a rational drug design principle is genuinely new. Score 9 rather than 10 because the practical question of whether this adds value over existing aggregation-state docking (structure-based drug design to aggregation-prone conformations) is open, and the novelty may be more mathematical than practical. |
| Mechanistic Specificity | 20% | 6 | The mechanism is specified at a conceptual level: identify high-|v_slow(i)| microstates from the apo MSM; find binders via ensemble docking (citing Bowman & Geissler 2012 cryptic pocket methodology); apply Boltzmann reweighting exp(-delta_G_bind(i)/kT); recompute overlap <P_drug|v_slow>. The Critic identifies three serious mechanistic concerns: (1) eigenmode structure changes upon ligand binding, making the apo v_slow an unreliable target; (2) Boltzmann reweighting diverges for strong binders (exp(11.7) for Kd < 10 uM), trivially suppressing any eigenmode overlap; (3) IDP high-|v_slow| states may lack binding pockets. Score 6: the conceptual mechanism is specified but has documented mechanistic flaws that the hypothesis acknowledges without resolving. |
| Cross-field Distance | 10% | 8 | Bridges non-equilibrium statistical mechanics (Mpemba eigenmode overlap integral) through computational structural biology (MSM-guided drug design) to medicinal chemistry (small molecule aggregation inhibitor design). The Mpemba physics community and the drug design community are genuinely disjoint; no researcher works in both areas. Score 8: wide disciplinary bridge that would require collaboration between a statistical physicist, a computational chemist, and a medicinal chemist. |
| Testability | 20% | 6 | The enrichment factor test (>2 for known inhibitors at Mpemba-target vs random microstates) is well-defined and falsifiable. The computational pipeline (apo MSM -> eigendecomposition -> microstate ranking -> ensemble docking -> reweighting) is executable with existing tools (AutoDock Vina, POVME, fpocket). The main testability challenges: (1) building a reliable Abeta42 apo MSM is a substantial project in itself; (2) for IDP systems, high-|v_slow| microstates may lack stable pockets detectable by fpocket; (3) the prospective validation (ThT assay for top-ranked ZINC compounds) requires wet lab resources. Score 6: testable in principle but requires MSM construction, docking campaign, and wet lab validation — a 9-12 month research project rather than a 3-month experiment. |
| Impact: Paradigm | 5% | 7 | If eigenmode-overlap-guided drug design produces selective aggregation inhibitors with novel binding sites, it would establish a new paradigm for rational aggregation inhibitor development grounded in spectral physics rather than thermodynamic endpoint targeting. This would be a significant conceptual contribution to both the Mpemba physics literature and the amyloid drug design literature, opening a new design principle. Score 7: would open a new approach to a long-standing problem (rational aggregation inhibitor design) if the validation succeeds. |
| Impact: Translational | 5% | 7 | Amyloid aggregation inhibitors are an active therapeutic target for Alzheimer's, Parkinson's, and type 2 diabetes (IAPP). If the enrichment factor validates the eigenmode-targeting principle and prospective screening identifies a hit compound with sub-uM ThT activity, the translational pathway to a lead compound is direct. Score 7: clearer translational endpoint than most hypotheses in this session — a validated hit from the Mpemba-guided screen could enter a drug discovery pipeline immediately. |
| Groundedness | 20% | 5 | Klich et al. 2019 PRX 9:021060 verified; Bulawa et al. 2012 PNAS 109:9629 (tafamidis) verified. The Bowman & Geissler 2012 PNAS 109:11681 citation is verified but mischaracterized: described as "ensemble docking" when the paper is about cryptic pocket DISCOVERY, not ensemble docking per se — ensemble docking is a separate methodology. EGCG as Abeta42 modulator is verified but the Critic confirms EGCG is a pan-assay interference compound (PAINS), undermining the enrichment factor test design. The IDP binding pocket absence for high-|v_slow| states is a known concern acknowledged but not resolved. Groundedness approximately 65%; one methodological mischaracterization and one acknowledged structural problem with the test compound set. Score 5: functional framework grounding is partial; key mechanistic assumptions lack verification. |
| **Composite (pre-bonus)** | | **6.60** | Novelty: 9*0.20=1.80; Mech. Spec.: 6*0.20=1.20; Cross-field: 8*0.10=0.80; Testability: 6*0.20=1.20; Paradigm: 7*0.05=0.35; Translational: 7*0.05=0.35; Groundedness: 5*0.20=1.00. Sum = 6.70. |
| **Cross-domain bonus** | | **+0.5** | Statistical mechanics (Mpemba eigenmode overlap) -> Computational structural biology (MSM-guided docking, cryptic pocket discovery) -> Medicinal chemistry (aggregation inhibitor design, ThT validation): 2+ disciplinary boundaries confirmed. Cross-domain bonus applied: +0.5 |
| **Composite (final)** | | **7.20** | 6.70 + 0.50 |

*Note: Arithmetic check — 1.80+1.20+0.80+1.20+0.35+0.35+1.00 = 6.70 (pre-bonus), 6.70+0.50 = 7.20 (final).*

---

## Score Computation Summary

### Detailed Weighted Calculations

**C2-H7 (Insulin Polymorph Selection):**
- Novelty: 8 * 0.20 = 1.60
- Mechanistic Specificity: 8 * 0.20 = 1.60
- Cross-field Distance: 7 * 0.10 = 0.70
- Testability: 9 * 0.20 = 1.80
- Impact Paradigm: 6 * 0.05 = 0.30
- Impact Translational: 7 * 0.05 = 0.35
- Groundedness: 8 * 0.20 = 1.60
- Pre-bonus total: **7.95**
- Cross-domain bonus: +0.50
- **Final composite: 8.45**

**C2-H5 (Refined Hierarchical Scoring):**
- Novelty: 8 * 0.20 = 1.60
- Mechanistic Specificity: 8 * 0.20 = 1.60
- Cross-field Distance: 7 * 0.10 = 0.70
- Testability: 8 * 0.20 = 1.60
- Impact Paradigm: 6 * 0.05 = 0.30
- Impact Translational: 5 * 0.05 = 0.25
- Groundedness: 7 * 0.20 = 1.40
- Pre-bonus total: **7.45**
- Cross-domain bonus: +0.50
- **Final composite: 7.95**

**C2-H4 (Entropy Production Spike):**
- Novelty: 8 * 0.20 = 1.60
- Mechanistic Specificity: 7 * 0.20 = 1.40
- Cross-field Distance: 8 * 0.10 = 0.80
- Testability: 7 * 0.20 = 1.40
- Impact Paradigm: 7 * 0.05 = 0.35
- Impact Translational: 3 * 0.05 = 0.15
- Groundedness: 8 * 0.20 = 1.60
- Pre-bonus total: **7.30**
- Cross-domain bonus: +0.50
- **Final composite: 7.80**

**C2-H1 (Resource-Theoretic D_KL):**
- Novelty: 9 * 0.20 = 1.80
- Mechanistic Specificity: 7 * 0.20 = 1.40
- Cross-field Distance: 8 * 0.10 = 0.80
- Testability: 6 * 0.20 = 1.20
- Impact Paradigm: 7 * 0.05 = 0.35
- Impact Translational: 4 * 0.05 = 0.20
- Groundedness: 6 * 0.20 = 1.20
- Pre-bonus total: **6.95**
- Cross-domain bonus: +0.50
- **Final composite: 7.45**

**C2-H2 (Mpemba-Guided Drug Design):**
- Novelty: 9 * 0.20 = 1.80
- Mechanistic Specificity: 6 * 0.20 = 1.20
- Cross-field Distance: 8 * 0.10 = 0.80
- Testability: 6 * 0.20 = 1.20
- Impact Paradigm: 7 * 0.05 = 0.35
- Impact Translational: 7 * 0.05 = 0.35
- Groundedness: 5 * 0.20 = 1.00
- Pre-bonus total: **6.70**
- Cross-domain bonus: +0.50
- **Final composite: 7.20**

---

## Final Ranking Table

| Rank | ID | Title | Pre-bonus | Final Composite | Critic Verdict | Cycle 2 Status |
|------|----|-------|-----------|-----------------|----------------|----------------|
| 1 | C2-H7 | Cooling-Rate-Dependent Fibril Polymorph Selection in Insulin | 7.95 | **8.45** | SURVIVES | Advance |
| 2 | C2-H5 | Refined Hierarchical Spectral Scoring with Yu et al. Calibration | 7.45 | **7.95** | SURVIVES | Advance |
| 3 | C2-H4 | Spectral Entropy Production Rate Distinguishes Folding from Misfolding | 7.30 | **7.80** | WOUNDED | Advance |
| 4 | C2-H1 | Resource-Theoretic D_KL as Unified Aggregation Predictor | 6.95 | **7.45** | WOUNDED | Advance |
| 5 | C2-H2 | Mpemba-Guided Aggregation Inhibitor Design | 6.70 | **7.20** | WOUNDED | Advance (diversity role) |

**All five cycle 2 survivors advance.** See diversity check below for final selection of top 3-5 for quality gate.

**Cycle 2 vs Cycle 1 comparison:**
- Best cycle 1 Ranker score: H5 = 7.50
- Best cycle 2 Ranker score: C2-H7 = **8.45** — EXCEEDS cycle 1 top score by +0.95
- C2-H5 = 7.95 — EXCEEDS cycle 1 top score by +0.45
- C2-H4 = 7.80 — EXCEEDS cycle 1 top score by +0.30
- C2-H1 = 7.45 — Approximately tied with cycle 1 best
- C2-H7's score of 8.45 represents the highest composite in this session. Flag raised: all top 4 cycle 2 hypotheses exceed 7.0.

---

## Diversity Check

### Top-5 Analysis

Pair assessments:

| Pair | Same bridge mechanism? | Same subfields? | Same prediction type? | Convergent? |
|------|----------------------|-----------------|----------------------|-------------|
| C2-H7 vs C2-H5 | Partial — both use MSM eigenspectral analysis; H7 predicts polymorph switching, H5 predicts aggregation propensity ranking | Adjacent (insulin fibrillation vs Abeta42 aggregation) | Different (T_cross + polymorph ID vs M_eff + TANGO comparison) | MODERATE — same formalism, different systems and predictions |
| C2-H7 vs C2-H4 | Different — H7 is experimental polymorph; H4 is trajectory entropy production | Different (insulin experiment vs Abeta42 simulation) | Different (experimental polymorph vs computational trajectory classifier) | LOW convergence |
| C2-H7 vs C2-H1 | Different — H7 is eigenmode branching; H1 is D_KL resource theory | Adjacent (both protein aggregation) | Different (experimental polymorph vs computational propensity score) | LOW convergence |
| C2-H7 vs C2-H2 | Different — H7 is polymorph selection mechanism; H2 is drug design using eigenmodes | Different (mechanism vs drug design application) | Different prediction types | LOW convergence |
| C2-H5 vs C2-H4 | Different — H5 is three-level hierarchy aggregation predictor; H4 is entropy production along trajectories | Adjacent (both Abeta42, both computational) | Somewhat different (propensity ranking vs trajectory classification) | MODERATE — different methods on overlapping systems |
| C2-H5 vs C2-H1 | SAME formalism — both compute MSM-derived scalars to predict aggregation propensity; H5 uses M_eff, H1 uses D_KL | SAME (Abeta42, 8-protein panel, ThT comparison) | SAME prediction type (scalar predictor correlates with ThT half-time) | HIGH convergence — these are alternative formulations of the same prediction |
| C2-H5 vs C2-H2 | Different — H5 is propensity predictor; H2 is drug design pipeline | Different applications | Different | LOW convergence |
| C2-H4 vs C2-H1 | Different — H4 is trajectory-level sigma(t); H1 is ensemble-level D_KL | Same system (Abeta42 MSMs) | Different (trajectory classifier vs ensemble predictor) | LOW convergence — conceptually distinct despite shared MSM infrastructure |
| C2-H4 vs C2-H2 | Different — H4 is thermodynamic trajectory analysis; H2 is docking campaign | Different | Different | LOW convergence |
| C2-H1 vs C2-H2 | Partial — both use MSM eigenmodes; H1 uses D_KL as propensity score; H2 uses eigenmodes as drug design target | Adjacent (both Abeta42 MSM-based) | Different (predictor vs drug design) | MODERATE convergence on infrastructure; divergent on application |

### Convergence Assessment

**Critical convergence pair: C2-H5 vs C2-H1**

These two are the most convergent in the set. Both:
- Operate on protein MSM eigenvalue spectra for Abeta42 and 7 other proteins
- Produce a single scalar predictor correlating with ThT half-time (Spearman rho > threshold)
- Use an 8-protein test panel with amyloidogenic vs non-amyloidogenic comparison

The difference: H5 uses M_eff (the refined Mpemba vulnerability score from the three-level hierarchy) while H1 uses D_KL(P_A* || P_eq) (the resource-theoretic relative entropy). These are mathematically distinct quantities, and H1 additionally draws on the Avanzini 2026 PRX framework which H5 does not. They are ALTERNATIVE unification strategies for the same predictive problem, not redundant computations.

**Diversity rule assessment:** 3 of the top 5 are not conceptually similar by the constraint's definition (share same bridge mechanism, same subfields, same prediction type — requiring 2 of 3). Only C2-H5 and C2-H1 are clearly convergent (HIGH). C2-H5 vs C2-H4 is MODERATE but different prediction type. No diversity demotion triggered: fewer than 3 of top 5 are conceptually similar.

**No diversity adjustments made.** The top 5 cover distinct mechanisms and prediction types:
- C2-H7: experimental polymorph selection (insulin, wet lab)
- C2-H5: calibrated three-level hierarchy aggregation predictor (Abeta42, computational)
- C2-H4: trajectory-level entropy production classifier (stochastic thermodynamics)
- C2-H1: resource-theoretic D_KL propensity score (information theory)
- C2-H2: eigenmode-guided drug design (medicinal chemistry application)

**However, for quality gate selection:** Given the C2-H5/C2-H1 convergence, if only 4 hypotheses are advanced to quality gate, C2-H1 should be kept over C2-H2 because C2-H1 scores higher (7.45 vs 7.20) and brings the resource-theoretic / quantum information bridge that C2-H5 does not. If all 5 advance, the diversity is adequate.

---

## Elo Tournament Sanity Check (Top-5, 10 pairwise comparisons)

*Prompt for each pair: "Which hypothesis would a domain researcher want to test FIRST, and why?"*

**Comparison 1: C2-H7 vs C2-H5**
C2-H7 wins. A researcher would test C2-H7 first because it requires no heroic MSM construction — the experimental three-arm design (rapid quench vs slow cool vs intermediate) can be executed immediately with standard insulin fibrillation protocols. C2-H5's advantage (calibrated hierarchy) is theoretical; C2-H7 produces an empirical result within months.
*Winner: C2-H7*

**Comparison 2: C2-H7 vs C2-H4**
C2-H7 wins. C2-H7 can be tested experimentally in a wet lab in 2-3 months; C2-H4 requires first constructing an Abeta42 MSM, then running 1000 kinetic Monte Carlo trajectories, then applying Schnakenberg analysis — a 5-8 month computational project. The empirical testability premium is decisive.
*Winner: C2-H7*

**Comparison 3: C2-H7 vs C2-H1**
C2-H7 wins. C2-H1 requires building MSMs for 8 proteins, identifying A* states, and computing D_KL — a multi-year computational effort. C2-H7 can produce a definitive result (polymorph identity vs cooling rate) in one focused wet-lab experiment. A PI allocating student time would prioritize C2-H7.
*Winner: C2-H7*

**Comparison 4: C2-H7 vs C2-H2**
C2-H7 wins clearly. C2-H7's experimental design is clean and immediate. C2-H2 faces the IDP binding pocket problem (high-|v_slow| states in Abeta42 may have no pockets) and requires a full MSM + docking campaign before producing any result. C2-H7 is testable; C2-H2's central assumption (IDP states have pockets) may be empirically false.
*Winner: C2-H7*

**Comparison 5: C2-H5 vs C2-H4**
C2-H5 wins narrowly. Both are computational and require MSM construction. C2-H5's output (M_eff vs TANGO cross-validation) directly demonstrates whether the spectral approach adds value over existing tools — a clear go/no-go criterion. C2-H4's sigma-spike is harder to interpret clinically and has unresolved signal-to-noise concerns. A researcher wanting a publishable decision in the shortest time prefers C2-H5.
*Winner: C2-H5*

**Comparison 6: C2-H5 vs C2-H1**
C2-H5 wins. C2-H5 and C2-H1 are both 8-protein MSM propensity predictors. C2-H5 has a cleaner theoretical foundation (no overextended canonical identity), better-grounded citations, and an explicit cross-validation design against TANGO that defines "success" clearly. C2-H1's D_KL = delta_F/kT identity is valid only at equilibrium, introducing a mechanistic weakness that C2-H5 avoids.
*Winner: C2-H5*

**Comparison 7: C2-H5 vs C2-H2**
C2-H5 wins. C2-H5 produces a validated aggregation propensity predictor, which is a complete research output. C2-H2 requires a docking campaign that may be blocked by the IDP pocket problem and uses EGCG (a PAINS compound) as a reference, weakening the validation design. C2-H5 is the more tractable research path.
*Winner: C2-H5*

**Comparison 8: C2-H4 vs C2-H1**
C2-H4 wins. Both require MSM construction. C2-H4's entropy production calculation is straightforward once the MSM exists (standard Schnakenberg formula applied to kinetic Monte Carlo trajectories). C2-H1's D_KL computation additionally requires A* state identification, which introduces algorithm-dependence and requires decisions about clustering methodology that C2-H4 avoids. C2-H4's citations are also fully verified with no errors.
*Winner: C2-H4*

**Comparison 9: C2-H4 vs C2-H2**
C2-H4 wins. C2-H4's prediction is theory-driven and relies on a rigorously derived formula. C2-H2's IDP binding pocket problem is a likely fatal flaw that cannot be resolved without additional feasibility work. A researcher would rather test the sigma-spike (which has a clear yes/no outcome based on trajectory statistics) than pursue IDP pocket identification (which may be physically impossible for Abeta42 high-|v_slow| states).
*Winner: C2-H4*

**Comparison 10: C2-H1 vs C2-H2**
C2-H1 wins. Both are computationally intensive. C2-H1 produces a cleaner output (D_KL scalar vs ThT correlation) with a known mathematical framework (resource theory). C2-H2's additional step (ensemble docking) adds IDP-specific challenges on top of the MSM requirement. The enrichment factor test is well-designed but depends on known inhibitors being non-PAINS compounds, which the EGCG counter-evidence undermines.
*Winner: C2-H1*

### Elo Win Tally

| Hypothesis | Wins | Losses | Win Rate |
|------------|------|--------|----------|
| C2-H7 | 4 | 0 | 4/4 = 100% |
| C2-H5 | 3 | 1 | 3/4 = 75% |
| C2-H4 | 2 | 2 | 2/4 = 50% |
| C2-H1 | 1 | 3 | 1/4 = 25% |
| C2-H2 | 0 | 4 | 0/4 = 0% |

### Elo vs Linear Ranking Comparison

| | Linear Composite | Elo Win Rate | Elo Rank |
|---|---|---|---|
| C2-H7 | 8.45 (1st) | 100% | 1st |
| C2-H5 | 7.95 (2nd) | 75% | 2nd |
| C2-H4 | 7.80 (3rd) | 50% | 3rd |
| C2-H1 | 7.45 (4th) | 25% | 4th |
| C2-H2 | 7.20 (5th) | 0% | 5th |

**Result: Elo confirms linear ranking.** The pairwise tournament agrees exactly with the composite score ordering at all five positions.

**Diagnostic signal from Elo:** The Elo tournament captures a "practical testability premium" that amplifies C2-H7's advantage beyond what the composite score reflects. C2-H7 wins all 4 matchups convincingly because it has both a strong composite score AND immediate experimental executability — the only hypothesis where no MSM construction is strictly required to begin the key test (the three-arm experiment). In pairwise comparison, this asymmetry is decisive: a researcher would rather have an empirical result in 3 months than wait 12 months for the MSM-dependent hypotheses to produce any data. The Elo tournament also clarifies C2-H2's position: despite its high novelty and translational scores (both 9 and 7), the IDP binding pocket problem is a structural barrier that makes it the last hypothesis a researcher would attempt with limited resources.

**Signal for quality gate:** C2-H7's 8.45 composite represents the strongest hypothesis in the session so far. C2-H4's emergence at rank 3 (above C2-H1) is validated by Elo — its clean groundedness and tractable computation overcome C2-H1's novelty advantage.

---

## Evolution Selection

**Top 4 hypotheses selected for quality gate (post-diversity-check):**

1. **C2-H7** — Composite 8.45 — Strongest hypothesis in cycle 2; cleanest citation record; most immediately testable experimental design; sharp three-arm mechanism discriminant. Advance directly to quality gate. Focus: address stochastic polymorphism risk (protocol for assessing across-replicate reproducibility) and clarify whether insulin B-chain MSM captures the full hormone.

2. **C2-H5** — Composite 7.95 — Most robust computational hypothesis; well-calibrated three-level hierarchy; TANGO cross-validation adds a clear falsification criterion. Advance to quality gate. Focus: correct the persistent Cohen et al. citation error (2012/109:9761 -> 2013/110:9758); address the force-spectroscopy-to-solution-conditions transfer assumption for the Yu et al. D values.

3. **C2-H4** — Composite 7.80 — Novel application of stochastic thermodynamics; fully verified citations; distinct from other hypotheses (trajectory-level classifier vs ensemble predictor). Advance to quality gate. Focus: quantify the signal-to-noise ratio for the sigma-spike relative to background global entropy production; address the Prigogine-regime distinction concern raised by the Critic.

4. **C2-H1** — Composite 7.45 — Highest novelty in cycle 2; resource-theoretic bridge adds unique angle not covered by other hypotheses; D_KL complements M_eff conceptually. Advance to quality gate. Focus: correct Chakraborty page numbers; restrict the D_KL = delta_F/kT claim to the equilibrium approximation context; address the A* state identification algorithm-dependence.

**C2-H2 (7.20) is borderline.** It is the lowest scoring survivor and the Elo tournament gives it 0 wins. However, its translational impact (eigenmode-guided drug design) is distinct from the other four and it carries the highest novelty score in the set (9). Recommendation: **advance C2-H2 conditionally** if the quality gate has capacity. If resource constraints require choosing 4, exclude C2-H2 and note that the eigenmode-as-druggable-target concept should be revisited after the IDP binding pocket feasibility question is resolved (e.g., test first on TTR or lysozyme, not Abeta42).

**Flag: All top 4 cycle 2 hypotheses exceed the cycle 1 best (7.0 QG adjusted / 7.50 Ranker).** C2-H7 at 8.45 and C2-H5 at 7.95 are substantially above the cycle 1 peak. This is an unusually strong cycle 2 cohort. The Orchestrator should consider whether the early-completion criterion (top-3 >= 7.0) applies in the quality gate phase and whether an additional evolution cycle is warranted.

---

*Cycle 2 ranking complete. Top 4 hypotheses advance to quality gate.*
*Highest composite score (C2-H7): 8.45 — exceeds cycle 1 top score (7.50) by +0.95.*
*All top 4 cycle 2 composites exceed 7.0.*
*Session phase: cycle2_quality_gate*
