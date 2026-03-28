# Cycle 2 Combined Ranking — Session 2026-03-28-scout-014

**Target**: Non-equilibrium statistical mechanics (Mpemba effect spectral theory) × Neurodegenerative protein biochemistry (amyloid aggregation selectivity)
**Ranker**: Ranker v5.2 | Canonical 6-dimension weights
**Date**: 2026-03-28
**Hypotheses ranked**: 5 cycle-2 survivors (C2-H1 to C2-H5) + 6 cycle-1 evolved hypotheses (E1-H5 through E6-H1xH5)
**Excluded**: C2-H6, C2-H7, C2-H8 (KILLED by Critic)

**Weight schema (canonical, immutable)**:
- Novelty 20% · Mechanistic Specificity 20% · Cross-Field Distance 10%
- Testability 20% · Impact-Paradigm 5% · Impact-Translational 5% · Groundedness 20%
- Cross-domain bonus +0.5 for 2+ disciplinary boundaries (applied to all 11 hypotheses — statistical mechanics → protein biochemistry/disease is a genuine crossing)

---

## Part I — Per-Hypothesis Scoring Tables

---

### C2-H1: A* State Population Is the Protein Mpemba Overlap Coefficient — A Quantitative Unification

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Directly equating A* population (Chakraborty et al. 2020) with the Mpemba overlap coefficient (Klich et al. 2019) is a new quantitative unification not found in the literature. The Critic's web searches confirmed absence of any paper linking these two mathematical objects. Score is 7 rather than 8 because the Critic's strongest attack — that Boltzmann thermodynamics (ΔF(A*) → population → aggregation rate) explains the core diagnostic prediction without Mpemba theory — challenges the mechanistic novelty of the connection even if the nomenclature mapping is new. |
| Mechanistic Specificity | 20% | 7 | Names specific molecular constructs: A* state from Chakraborty 2020, psi_2 eigenmode of the transition matrix, sigma_2 overlap integral, and derives a quantitative population fraction from ΔF. The CONDITIONAL fixes require acknowledging that psi_2 separating native from aggregation-prone basins is an assumption, not a verified MSM finding, and that the reported A* percentages must be computed from ΔF rather than stated as directly measured. These corrections reduce specificity from 8. |
| Cross-Field Distance | 10% | 7 | Bridges Klich et al. 2019 statistical mechanics (PRX) with Chakraborty et al. 2020 protein biochemistry (J. Am. Chem. Soc.) — two communities with no citation crossover. The communities do share Markov chain formalism (reducing distance slightly), but the physical phenomenon (anomalous relaxation) and the biological application (amyloid intermediate states) are genuinely distinct. |
| Testability | 20% | 7 | Computationally executable via re-analysis of existing Abeta42 trajectories: build MSM, decompose transition matrix, identify psi_2 eigenmode, compute overlap integral with Boltzmann-weighted ensemble, compare with experimental A* population estimates. Standard pyEMMA/deeptime methodology. A PhD student with computational biophysics experience could complete this in 3 months with existing trajectory data. Deducted 1 point because the psi_2 basin assignment requires additional validation steps beyond standard MSM construction. |
| Impact: Paradigm | 5% | 6 | If the A* state IS the Mpemba overlap coefficient, this reframes the entire A* intermediate literature under a kinetic-spectral rather than purely thermodynamic lens. Moderate paradigm shift within the protein biophysics community. Would not open a new field but would meaningfully reinterpret existing measurements. |
| Impact: Translational | 5% | 4 | The reinterpretation suggests A* population could be computed from MSMs rather than measured directly, but downstream therapeutic implications are remote. Diagnostic value for variant screening is possible but speculative at this stage. |
| Groundedness | 20% | 6 | Chakraborty et al. 2020 is real and correctly described. Klich et al. 2019 PRX is real. The mathematical mapping between the two is derived correctly in principle. However, Critic assessed MEDIUM groundedness: psi_2 separating native from aggregation basins is unverified for any IDP; A* percentages must be recomputed from ΔF rather than taken at face value; Boltzmann alternative undermines the causal framing. Approximately 65% of factual claims are traceable. |
| **Raw Composite** | | **6.60** | 0.20×7 + 0.20×7 + 0.10×7 + 0.20×7 + 0.05×6 + 0.05×4 + 0.20×6 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics (Mpemba theory) → protein biochemistry (amyloid intermediate states): 2+ disciplinary boundaries |
| **Final Composite** | | **7.10** | |

---

### C2-H2: Measured D_misfold/D_fold Ratio of PrP Predicts Bimodal Eigenvalue Spectrum via Zwanzig-Kramers Bridge

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | Using empirically measured D_misfold/D_fold from Yu et al. 2015 PrP force spectroscopy to ground the Zwanzig roughness formula → bimodal MSM prediction is a specific novel application. However, the broader roughness-to-bimodality bridge is already developed in E1-H5 (the cycle-1 evolved predecessor), and C2-H2 focuses on the PrP-specific grounding step rather than introducing a new conceptual bridge. Score of 6 reflects genuine novelty within a family where similar ideas already exist. |
| Mechanistic Specificity | 20% | 8 | Exceptionally specific: names the Yu et al. 2015 measured D ratio (~100–1000x for PrP under applied force), applies the Zwanzig-Kramers formula (D_eff = D_0·exp(-(ε/kT)²)), derives a quantitative epsilon from the D ratio, and predicts bimodal spectrum with Sarle BC > 0.555 criterion. CONDITIONAL fixes require explicitly acknowledging that force-spectroscopy D measurements under applied load differ from free-diffusion landscape diffusivity — this limitation is mechanistically precise. |
| Cross-Field Distance | 10% | 6 | Force spectroscopy (experimental biophysics) → MSM eigenspectrum (computational biophysics) is an intra-field bridge within the biophysics community. Both communities share practitioners. Zwanzig's formula is well-known in protein folding theory. Cross-field distance is lower than hypotheses bridging physics → biology from outside the biophysics community. |
| Testability | 20% | 6 | PrP force spectroscopy is established (Woodside lab methods). PrP MSM construction is feasible from existing coarse-grained simulations or REMD trajectories. Computing the bimodal coefficient from the resulting eigenspectrum is straightforward. However, PrP-specific high-quality MSMs do not yet exist, requiring either new simulation or careful trajectory curation — adding 2–3 months. Also, free-diffusion PrP measurements to validate the D ratio transfer are needed, adding experimental complexity. 3–6 month realistic timeline. |
| Impact: Paradigm | 5% | 5 | Validates the Zwanzig-MSM connection for a clinically relevant prion protein. Moderate contribution: confirms the physical mechanism but does not generalize beyond PrP without further work. Extends the E1-H5 framework to a specific measured system. |
| Impact: Translational | 5% | 4 | PrP is relevant to prion diseases (CJD, BSE), but the connection from D ratio → bimodal spectrum → therapeutic strategy requires many additional steps. Near-term translational impact is low. |
| Groundedness | 20% | 7 | Critic assessed MEDIUM-HIGH. Yu et al. 2015 force spectroscopy D ratio is a real, verified experimental measurement. Zwanzig 1988 PNAS formula is established. Sarle's bimodality coefficient is established. The main unverified step — that force-spectroscopy D measurements transfer to free-diffusion landscape parameters — is explicitly flagged by Critic as a reasonable approximation needing acknowledgment. Approximately 75% of factual claims are traceable. |
| **Raw Composite** | | **6.45** | 0.20×6 + 0.20×8 + 0.10×6 + 0.20×6 + 0.05×5 + 0.05×4 + 0.20×7 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics / physics (Zwanzig roughness, force spectroscopy) → protein biophysics: 2+ disciplinary boundaries |
| **Final Composite** | | **6.95** | |

---

### C2-H3: Cooling-Rate-Dependent Fibril Polymorph Selection in Abeta42 via Eigenmode Branching

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | Using cooling rate to select amyloid fibril polymorphs via eigenmode branching is a novel prediction. Fibril polymorphism under different conditions is established (Petkova 2005 Science), but the eigenmode explanation and its quantitative connection to thermal history are new. Score is 6 rather than 7 because E3-H7xH5 (the evolved version switching from PrP to insulin/beta-2m) addresses the same prediction with better experimental tractability; C2-H3 is the weaker Abeta42-centric formulation. |
| Mechanistic Specificity | 20% | 5 | The eigenmode branching mechanism is described but weakened by the Abeta42 IDP problem: Abeta42 lacks a defined folding funnel, making D_fold poorly defined and MSM bimodality analysis problematic. The CONDITIONAL fixes require providing order-of-magnitude quantitative predictions for polymorph ratio changes as a function of cooling rate — these are not yet provided. The "denaturation threshold" framing for an IDP was incorrectly applied and requires removal. |
| Cross-Field Distance | 10% | 6 | Thermal physics (eigenmode branching, temperature-dependent relaxation) → protein structural biology (fibril polymorph selection). The statistical mechanics and structural biology communities do not significantly overlap, but this is within the broad biophysics sphere. |
| Testability | 20% | 5 | Fibril polymorph characterization by cryo-EM and ssNMR is experimentally feasible. However, the primary computational requirement — MSM construction for Abeta42 — is problematic given IDP nature. The CONDITIONAL fixes require acknowledging that slow cooling allows ensemble re-equilibration, limiting the eigenmode-overlap argument to fast quenches only. The quantitative prediction for polymorph ratios (required by Critic) is missing. These gaps reduce testability to 5. |
| Impact: Paradigm | 5% | 6 | Polymorph selection via thermal history would provide a new mechanistic explanation for fibril strain diversity in Alzheimer's disease. The connection between amyloid strains and disease phenotypes (Condello 2018) gives this moderate paradigm impact within the amyloid field. |
| Impact: Translational | 5% | 4 | In vivo cooling rates are not pharmacologically controllable, and industrial protein folding (e.g., biopharmaceutical manufacturing) is a limited niche. Translational value is low without a clearer therapeutic hook. |
| Groundedness | 20% | 5 | Critic assessed MEDIUM. Fibril polymorphism under different conditions is established. Eigenmode branching mechanism for Abeta42 is speculative without existing MSMs. The IDP limitation is fundamental — Abeta42 does not have a bimodal eigenspectrum in the same sense as globular proteins with defined folding funnels. The slow-cooling re-equilibration objection has not been quantitatively addressed. Approximately 55% of factual claims are traceable. |
| **Raw Composite** | | **5.30** | 0.20×6 + 0.20×5 + 0.10×6 + 0.20×5 + 0.05×6 + 0.05×4 + 0.20×5 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics (thermal relaxation theory) → protein structural biology (fibril polymorphism): 2+ disciplinary boundaries |
| **Final Composite** | | **5.80** | |

---

### C2-H4: Maximum-Likelihood Non-Reversible MSMs Reveal Non-Normal Dynamics in Amyloidogenic Proteins

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Applying the Henrici non-normality measure delta(Q) to non-symmetrized protein MSMs as a classifier for amyloidogenic propensity is novel. The specific combination of non-reversible MSM estimators + non-normality theory from mathematical physics + amyloid biology is not in the literature. Score is 7 rather than 8 because the Critic's strongest attack (non-normality is trivially guaranteed for any absorbing-state system, including all protein MSMs with aggregation states) critically undermines the discriminative specificity of the approach. |
| Mechanistic Specificity | 20% | 6 | Proposes a specific measure (Henrici delta(Q)) and a specific estimator class (maximum-likelihood non-reversible transition matrices). However, the CONDITIONAL fix requiring a quantitative discriminative prediction — how much larger should delta(Q) be for amyloidogenic vs. non-amyloidogenic proteins, and why — is not yet provided. Without this, the hypothesis is not mechanistically specific enough to be falsifiable as a discriminative claim. |
| Cross-Field Distance | 10% | 7 | Non-normal matrix theory (pure mathematics/linear algebra) + transient amplification dynamics (mathematical physics) → protein MSMs (computational biophysics) → amyloid disease (biochemistry). The mathematical physics of non-normal operators is substantially distant from protein biochemistry, and practitioners rarely cross this boundary. |
| Testability | 20% | 6 | Non-reversible MSM estimators (dtram, MBAR without detailed-balance enforcement) are established software tools. Computing Henrici delta(Q) is mathematically straightforward. However, the Critic's required CONDITIONAL fix — providing a quantitative discriminative prediction for delta(Q) differences — is not yet specified, making the refutation criterion ambiguous. Additionally, identifying MD datasets that sample both equilibrium folding and aggregation-committed states is non-trivial. Score of 6 reflects feasibility in principle with significant execution challenges. |
| Impact: Paradigm | 5% | 6 | Non-normality as a biophysical classification tool would be a methodological contribution bridging matrix theory and protein biophysics. Would extend the MSM toolbox and potentially explain why certain proteins show transient misfolding bursts. |
| Impact: Translational | 5% | 3 | Non-normality measure is a computational classifier with no direct therapeutic connection at this stage. Very low near-term translational value. |
| Groundedness | 20% | 5 | Critic assessed LOW-MEDIUM. The non-trivial non-normality claim for amyloidogenic proteins under standard equilibrium MSMs is undermined by the trivial-non-normality objection (absorbing states guarantee non-normality for all proteins). The PMID 40566167 (2025 Entropy) reference for quantum Mpemba non-normal dynamics is real. TRAM and dtram are established. But the core discriminative prediction lacks quantitative support. Approximately 50% of claims are traceable. |
| **Raw Composite** | | **5.95** | 0.20×7 + 0.20×6 + 0.10×7 + 0.20×6 + 0.05×6 + 0.05×3 + 0.20×5 |
| Cross-domain bonus applied: +0.5 | | | Non-normal matrix theory (mathematics/physics) → computational biophysics → amyloid disease: 2+ disciplinary boundaries |
| **Final Composite** | | **6.45** | |

---

### C2-H5: Resource-Theoretic Mpemba Monotone Predicts Therapeutic Window for Aggregation Reversal

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Importing resource theory (a framework from quantum information theory) into protein aggregation biology via the Mpemba monotone is genuinely novel and represents the furthest conceptual leap in this session's hypothesis family. The formal mapping of protein conformational distributions to resource theory monotones has no precedent in the protein biophysics literature, and the Critic's web search confirmed absence. Score of 8 reflects both conceptual novelty and the sobering CONDITIONAL fix (the therapeutic framing must be dropped, narrowing the novel claim). |
| Mechanistic Specificity | 20% | 6 | The resource-theoretic Mpemba monotone (KL divergence between non-equilibrium and Boltzmann distributions) is a mathematically precise construct. However, after dropping therapeutic claims per CONDITIONAL fix, the specific experimental test reduces to denaturant-dilution experiments, which are much less mechanistically distinctive. The Critic's question (what remains testable beyond simpler denaturation kinetics?) is a real concern that reduces specificity. |
| Cross-Field Distance | 10% | 9 | Quantum information theory (resource theory, monotones) → statistical mechanics (Mpemba effect) → protein aggregation biochemistry (aggregation reversal). This is the largest disciplinary gap in the session: resource theory practitioners work in quantum computing/information theory and very rarely engage with protein biochemistry literature. Three distinct disciplinary communities bridged. |
| Testability | 20% | 5 | After mandatory CONDITIONAL fix dropping therapeutic claims, the remaining testable prediction is the denaturant-dilution experiment: a specific conformational ensemble (prepared by rapid denaturant dilution from a non-equilibrium starting state with low KL divergence) should show reduced aggregation. This is experimentally feasible. However, the Critic's question — distinguishing this from simpler denaturation/refolding kinetics — is unresolved, reducing testability score because the refutation criterion is insufficiently distinctive. The nanosecond-microsecond Mpemba window is also far shorter than experimental measurement capabilities. |
| Impact: Paradigm | 5% | 7 | If resource theory monotones prove applicable to protein conformational biology, this would open a genuinely new theoretical framework at the interface of quantum information theory and biophysics. The paradigm impact is substantial — resource theory would join the toolkit of structural biologists and computational biophysicists. |
| Impact: Translational | 5% | 3 | The CONDITIONAL fix explicitly requires dropping pharmaceutical and therapeutic claims (no pharmacological tool can target eigenmode overlap coefficients). The remaining experimental predictions are in vitro biophysics with no direct therapeutic path. Very low translational impact at this stage. |
| Groundedness | 20% | 5 | Critic assessed MEDIUM. The resource theory framework is well-established in quantum information (Brandao et al.). The Mpemba monotone formulation is traceable to the quantum Mpemba literature. However, the application to protein conformational distributions is speculative — proteins are open, dissipative, non-Markovian systems that violate the closed-system assumption of resource theory. DKL ~ 0.013 nats making the therapeutic window "vanishingly narrow" is a concrete quantitative objection. Approximately 55% of claims are traceable. |
| **Raw Composite** | | **6.20** | 0.20×8 + 0.20×6 + 0.10×9 + 0.20×5 + 0.05×7 + 0.05×3 + 0.20×5 |
| Cross-domain bonus applied: +0.5 | | | Quantum information theory (resource theory) → statistical mechanics → protein biochemistry: 3 disciplinary boundaries — clearest multi-boundary crossing in the set |
| **Final Composite** | | **6.70** | |

---

### E1-H5: Rough Energy Landscape Diffusion Asymmetry Creates the Spectral Signature That the Mpemba Index Detects (Sharpened Falsification)

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The specific quantitative connection between Zwanzig roughness amplitude ε, the derived crossover threshold ε_cross ~ 1.0 kT, Sarle's bimodality coefficient BC > 0.555, and amyloidogenic protein classification is not in the literature. Teza 2025 (comprehensive Mpemba review) confirms no prior paper has applied the Zwanzig formula to MSM eigenspectrum bimodality for amyloid classification. The sharpened falsification criterion (ε_cross derivation from Zwanzig formula) is a novel contribution beyond the parent H5. Feng et al. 2026 PRL is cited as the closest existing D measurement. |
| Mechanistic Specificity | 20% | 9 | Extraordinarily specific: derives ε_cross ~ 1.0 kT from the condition D_misfold/D_fold = 0.1 (kT·√ln10); predicts BC > 0.555 for amyloidogenic proteins (Abeta42, alpha-synuclein, tau-K18, IAPP) and BC < 0.555 for non-amyloidogenic controls (Abeta40, beta-synuclein, MAP2-MTBD, calcitonin); specifies Zwanzig roughness fit to MFPT data as the computational step; links both BC threshold and ε_cross as co-conditions that must simultaneously hold. Step 5 explicitly links bimodality to Mpemba index from E2-H1, creating an internally coherent multi-level framework. |
| Cross-Field Distance | 10% | 7 | Rough energy landscape physics (Bryngelson-Wolynes theory, Jia et al. 2020 PNAS) + Zwanzig 1988 formula (condensed matter physics) → protein MSMs (computational biophysics) → amyloid disease classification. The materials physics / condensed matter community and the computational biophysics/amyloid community are different enough to score 7. |
| Testability | 20% | 8 | Very concrete: build MSMs for 4+4 protein pairs from existing enhanced sampling or published trajectory data, compute full eigenspectrum, Sarle BC on log-timescale distribution, fit Zwanzig MFPT formula, extract ε per protein, plot BC vs ε correlation, verify that the two conditions co-segregate. Chapman-Kolmogorov validation specified. Step 5 links to Mpemba index computation. A computational biophysics PhD student could execute this in 3–5 months using existing Abeta42 (Rosenman 2013), alpha-synuclein, and Abeta40 trajectory data. The dual-condition refutation criterion (both BC and ε must hold) makes this cleanly falsifiable. |
| Impact: Paradigm | 5% | 7 | Provides a molecular physics basis (Zwanzig roughness) for the fundamental question: why do some proteins aggregate and others don't? If validated, establishes a physical threshold (ε_cross) that separates amyloidogenic from non-amyloidogenic sequences regardless of specific sequence features. Would be a landmark result in the energy landscape theory of protein aggregation. |
| Impact: Translational | 5% | 5 | The ε_cross threshold could become a computational screening criterion for amyloidogenic variants in drug design and protein engineering. If the bimodality coefficient can be computed from existing MD data, this provides a practical aggregation risk classifier. Moderate translational relevance for protein therapeutics and neurodegenerative disease drug discovery. |
| Groundedness | 20% | 8 | Zwanzig 1988 PNAS is established. Bryngelson et al. 1995 Proteins energy landscape is established. Jia et al. 2020 PNAS is real and directly relevant. Feng et al. 2026 PRL 136:128403 cited for D measurements. Sarle's bimodality coefficient is established. The Zwanzig formula application to derive ε_cross is a new derivation but follows directly from established mathematics. The main unverified empirical claim — that amyloidogenic proteins actually have ε > 1.0 kT — is the testable prediction, not a grounding claim. High groundedness reflects that nearly all supporting citations are verifiable. |
| **Raw Composite** | | **7.90** | 0.20×8 + 0.20×9 + 0.10×7 + 0.20×8 + 0.05×7 + 0.05×5 + 0.20×8 |
| Cross-domain bonus applied: +0.5 | | | Condensed matter physics (Zwanzig roughness theory) → computational biophysics → amyloid disease: 2+ disciplinary boundaries |
| **Final Composite** | | **8.40** | |

---

### E2-H1: Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity (Citations Corrected)

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Applying the Mpemba index (zero-crossing count of eigenmode overlap integrals, Klich et al. 2019 PRX) as an aggregation propensity classifier for amyloidogenic proteins is genuinely novel. Teza 2025 comprehensive review confirms no prior paper has applied Klich's Mpemba index to protein MSMs. The addition of Schuler et al. 2023 PNAS (PMID 37606329) as biological precedent for kinetic bypass of aggregation intermediates strengthens the mechanistic framing. Three citation errors from H1 are corrected, restoring credibility. |
| Mechanistic Specificity | 20% | 7 | Specifies the Mpemba index computation (overlap integral ⟨P(T)|v₁⟩ vs T, zero crossings), names specific protein pairs (Abeta42/Abeta40, alpha-synuclein/beta-synuclein, tau-K18/MAP2-MTBD), references Rosenman et al. 2013 J. Mol. Biol. 425:3338 for Abeta42 MSM construction. Score of 7 rather than 8 reflects the IDP MSM quality concern (alpha-synuclein MSM resolution limit acknowledged with confidence interval reporting step) — a genuine mechanistic limitation. The 3-state kinetic sanity check is a helpful addition. |
| Cross-Field Distance | 10% | 7 | Statistical mechanics (Mpemba index, anomalous relaxation, PRX) → computational biophysics/biochemistry (protein folding MSMs, amyloid aggregation). The PRX community and the protein folding MSM community are different — different journals, different conferences, different language. Score of 7 reflects genuine but not extreme disciplinary distance. |
| Testability | 20% | 8 | Test protocol is very specific: retrieve published conformational ensembles, compute eigendecomposition with established tools (pyEMMA), identify slowest eigenmode, evaluate overlap integral at 100 temperature points (280–400 K, 1 K steps), count zero crossings = Mpemba index. Mann-Whitney U test with n ≥ 4 pairs. Spearman rho against ThT half-times from Arosio et al. 2015. 3-state sanity check included. A computational biophysics PhD student could execute this in 3 months using published Abeta42 and Abeta40 ensembles. Clean refutation criterion: if Spearman rho < 0.7 across ≥ 4 pairs with p > 0.05, hypothesis is refuted. |
| Impact: Paradigm | 5% | 7 | The Mpemba index as an aggregation propensity classifier would be a new biophysical tool bridging statistical physics and amyloid biochemistry. Would provide a kinetic-spectral interpretation of why sequence determines aggregation risk beyond thermodynamic stability. Paradigm shift within the protein biophysics community. |
| Impact: Translational | 5% | 5 | Mpemba index as a sequence-based screening tool (if computable from MSMs) could complement TANGO, CamSol, and other aggregation predictors for variant screening in biologics development and neurodegenerative disease research. Moderate translational potential. |
| Groundedness | 20% | 8 | Three citation errors from H1 were corrected. Klich et al. 2019 PRX 9:021060 is real and the Mpemba index definition is accurate. Rosenman et al. 2013 J. Mol. Biol. 425:3338 is verified. Eschmann et al. 2015 J. Phys. Chem. B 119:14421 corrected and role clarified as experimental reference. Schuler et al. 2023 PNAS PMID 37606329 is real. Arosio et al. 2015 Trends Pharmacol. Sci. 36:592 is real. Main uncertainty is that alpha-synuclein MSM quality is lower than globular proteins — explicitly flagged with confidence interval reporting. High groundedness with this transparency. |
| **Raw Composite** | | **7.50** | 0.20×8 + 0.20×7 + 0.10×7 + 0.20×8 + 0.05×7 + 0.05×5 + 0.20×8 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics (Mpemba index, PRX) → protein biochemistry (amyloid aggregation): 2+ disciplinary boundaries |
| **Final Composite** | | **8.00** | |

---

### E3-H7xH5: Cooling-Rate-Dependent Fibril Polymorph Selection in Tractable Amyloid Systems via Eigenmode Branching from Rough Landscape Asymmetry

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The crossover temperature T_cross prediction (where dominant polymorph switches between Type-A and Type-B) as a discriminant between eigenmode branching and Ostwald kinetic competition is novel and not in the literature. The specific switch to insulin at pH 2 (from PrP, which was untractable) and beta-2-microglobulin as a model system with existing trajectory data is a creative problem-solving move. The non-monotonic structural crossover vs. monotonic kinetic competition discriminant is a genuine contribution beyond the parent H7 hypothesis. |
| Mechanistic Specificity | 20% | 8 | Very specific: insulin at pH 2 (0.5 mg/mL, 20 mM KCl), T range 55–65°C, T_cross predicted between 45–55°C, Protocol A (rapid quench < 2 min), Protocol B (slow cool 0.1°C/min), solid-state NMR chemical shift discrimination (Δ ≥ 2 ppm on Phe sidechains), FTIR amide I band Gaussian decomposition (1625 vs 1630 cm⁻¹), cryo-EM class averaging. The mechanism discrimination criterion (T_cross must match experiment within ±5°C) is mechanistically sharp and was absent in parent H7. |
| Cross-Field Distance | 10% | 7 | Eigenmode branching (statistical mechanics / MSM spectral theory) + rough landscape diffusion asymmetry (physical chemistry / Zwanzig) → fibril polymorph selection (structural biology / cryo-EM). The computational physics and structural biology communities are genuinely different with distinct methodologies and journals. |
| Testability | 20% | 8 | Protocol is exceptionally concrete: the computational step (MSM for insulin B-chain at pH 2) is feasible from existing high-temperature enhanced sampling trajectories; the in vitro experiment specifies exact conditions; the structural characterization uses three independent methods (cryo-EM, ssNMR, FTIR); the T_cross test uses 5 cooling rates and both the polymorph identity AND the T_cross prediction must hold within ±5°C. This is genuinely testable by a well-equipped structural biology / biophysics lab in 6–9 months. |
| Impact: Paradigm | 5% | 7 | If eigenmode branching from rough landscape asymmetry determines fibril polymorph identity, this would provide a physical mechanism for amyloid strain selection — a central unsolved problem in Alzheimer's, Parkinson's, and prion diseases. A mechanistic explanation for conformational strains would be a significant advance in the amyloid field. |
| Impact: Translational | 5% | 5 | Fibril polymorph control via thermal history is directly relevant to insulin pharmaceutical formulation (insulin polymorphism causes stability problems in biopharmaceuticals). The general principle of cooling-rate-controlled polymorph selection has potential industrial applications. Some translational value. |
| Groundedness | 20% | 7 | Petkova et al. 2005 Science 307:262 for fibril polymorph selection is real. Insulin fibril polymorphism is established. Klich et al. 2019 PRX is established. The rough landscape asymmetry mechanism is inherited from E1-H5 (high groundedness). The predicted T_cross and eigenmode branching for insulin are unverified — these are the testable predictions, not grounding claims. The forced-denaturation concern from C2-H3 is avoided by using 55–65°C and pH 2 conditions. Approximately 70% of claims traceable. |
| **Raw Composite** | | **7.50** | 0.20×8 + 0.20×8 + 0.10×7 + 0.20×8 + 0.05×7 + 0.05×5 + 0.20×7 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics (eigenmode branching, spectral theory) + physical chemistry (Zwanzig roughness) → structural biology (fibril polymorphism): 2+ disciplinary boundaries |
| **Final Composite** | | **8.00** | |

---

### E4-H3: Non-Equilibrium Maximum-Likelihood MSMs Reveal Non-Normal Transient Dynamics in Amyloidogenic Proteins under Cellular Driving

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The specific resolution of the standard-MSM non-normality problem by shifting to non-equilibrium Hsp70-coupled simulations (where detailed balance is genuinely broken) is a creative and novel reformulation. The combination of non-equilibrium MSM estimators (dtram/MBAR without symmetrization) + Hsp70 ATPase cycling + Henrici non-normality measure + transient amplification during chaperone release window is not in the literature. PMID 40566167 (2025 Entropy) for quantum Mpemba non-normal dynamics is correctly cited to replace the mischaracterized Lapolla & Godec 2020 reference. |
| Mechanistic Specificity | 20% | 8 | Very specific: k_ATPase ~ 5–10 s⁻¹; Henrici delta(Q) thresholds (>0.3 for amyloidogenic, <0.1 for non-amyloidogenic); transient amplification ratio >2 for amyloidogenic over 100 ms–10 s window; non-equilibrium MSM estimators specified (dtram, MBAR without detailed balance); stopped-flow experimental design with Hsp70 + Hsp40 + NEF (Bag1) + ATP regenerating system; FRET monitoring over 100 ms–10 s. The quantitative discriminative prediction (delta(Q) > 0.3 vs < 0.1) addresses the CONDITIONAL fix from C2-H4 for the non-normality discriminative prediction. |
| Cross-Field Distance | 10% | 8 | Non-equilibrium statistical mechanics (non-normal operator theory, transient amplification) + non-equilibrium MSM methodology (dtram) → Hsp70 chaperone biology (molecular biology/biochemistry) → amyloid disease. Three communities: mathematical physics, molecular biology, and structural biochemistry. Practitioners rarely cross all three. |
| Testability | 20% | 7 | The computational part (Hsp70-coupled coarse-grained simulation + non-equilibrium MSM) is more technically demanding than the other hypotheses — requiring coarse-grained protein + explicit Hsp70 interaction model, which is non-trivial to set up but possible. The experimental stopped-flow assay (sudden ATP dilution + FRET monitoring) is established in principle for chaperone kinetics labs (e.g., Mayer lab, Bhattacharya lab). Timeline is 6–12 months, slightly longer than most other hypotheses. Score of 7 reflects genuine feasibility with elevated technical complexity. |
| Impact: Paradigm | 5% | 7 | Non-equilibrium non-normality as a cellular mechanism for transient misfolding amplification would provide a new framework for understanding why protein aggregation increases with age (chaperone imbalance → increased non-equilibrium driving → transient amplification windows). This is a conceptually important contribution to the aging-aggregation connection. |
| Impact: Translational | 5% | 5 | If chaperone imbalance creates non-normal dynamics that amplify misfolding probability, this suggests therapeutic strategies targeting the chaperone network balance (e.g., HSF1 activation, Hsp70 supplementation) could reduce transient misfolding amplification. Moderate translational potential for neurodegeneration. |
| Groundedness | 20% | 6 | Non-equilibrium MSM estimators (TRAM, dtram) are established. Hsp70 ATPase cycling rates (~5–10 s⁻¹) are known from literature. PMID 40566167 is real. Hsp40 + NEF (Bag1) system is established for in vitro chaperone reconstitution. The specific prediction that amyloidogenic proteins show delta(Q) > 0.3 under Hsp70-coupled simulation is the novel testable claim — unverified but mechanistically grounded. The central conceptual step (Hsp70 driving genuinely breaks detailed balance in the protein conformational ensemble) is physically plausible but not yet computationally demonstrated. Approximately 60% traceable. |
| **Raw Composite** | | **7.20** | 0.20×8 + 0.20×8 + 0.10×8 + 0.20×7 + 0.05×7 + 0.05×5 + 0.20×6 |
| Cross-domain bonus applied: +0.5 | | | Non-equilibrium statistical physics + mathematical operator theory → molecular chaperone biology → neurodegeneration: 3 disciplinary boundaries |
| **Final Composite** | | **7.70** | |

---

### E5-H4: Inverse Mpemba Cooling Protocol Suppresses Amyloid Fibril Formation in Systems with Genuine Non-Monotonic Nucleation Temperature Dependence

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The inverse Mpemba protocol for fibril suppression is novel after the fatal correction (replacing the fabricated Kusumoto 1998 Abeta42 claim with real non-monotonic systems: insulin pH 2 and beta-lactoglobulin pH 2). The specific prediction of ≥40% fibril suppression by rapid quench from above the nucleation peak (relative to slow cooling) is quantitative and not in the literature. Score is 7 rather than 8 because the general idea of cooling-rate effects on protein aggregation has been explored in pharmaceutical protein formulation, and the eigenmode-overlap interpretation is the new element. |
| Mechanistic Specificity | 20% | 8 | Very specific: insulin at pH 2 (0.5 mg/mL, 20 mM HCl/KCl), 65°C pre-heat, rapid quench (<2 min) vs slow cool (0.1°C/min), ThT fluorescence at 48h, ≥40% difference criterion, non-monotonic nucleation peak at ~52°C. Step 1 (confirm non-monotonic T-curve at 37/42/47/52/57/62°C) is correctly required before the main test. Lysozyme pH 7 control included to distinguish from simpler "less time at high T" null hypothesis. Intermediate endpoint tests (quench to 42/47/52/57°C) provide non-monotonic structure validation. |
| Cross-Field Distance | 10% | 7 | Inverse Mpemba effect (statistical mechanics, non-equilibrium thermodynamics) → amyloid fibril nucleation kinetics (biochemistry/biophysics). The statistical physics of the inverse Mpemba effect and the protein aggregation kinetics community are genuinely different. The pharmaceutical formulation angle adds another community (pharmaceutical sciences). |
| Testability | 20% | 8 | The most experimentally accessible hypothesis in the set. Required equipment: spectrofluorometer (ThT assay), water bath with precise temperature control, basic protein preparation (insulin pH 2 is trivial). Protocol is fully specified with exact concentrations, temperatures, and timepoints. Step 1 (non-monotonic T-curve confirmation) guards against the fatal null hypothesis failure. Lysozyme control distinguishes mechanism from confound. A protein biochemistry PhD student could complete the core experiment in 2–3 months. This is the quickest-to-test hypothesis in the combined ranking. |
| Impact: Paradigm | 5% | 6 | A confirmed inverse Mpemba effect in protein fibrillation would be the first experimental demonstration of an Mpemba-related phenomenon in a biologically relevant aggregation system. Moderate paradigm impact within amyloid biophysics; broader impact if the eigenmode interpretation is validated computationally. |
| Impact: Translational | 5% | 6 | Direct application to insulin pharmaceutical formulation: insulin drugs undergo thermal excursions during manufacturing and storage, and fibril suppression via controlled cooling rates would be directly applicable. Also relevant for biopharmaceutical protein stability testing. Higher translational value than most other hypotheses. |
| Groundedness | 20% | 7 | Fatal error from H4 (Kusumoto 1998 showing monotonic Abeta42 T-dependence) has been fixed. Gosal et al. 2004 J. Mol. Biol. 336:221 for beta-lactoglobulin non-monotonic T-dependence is real. Nielsen et al. 2001 Biochemistry 40:6036 for insulin nucleation kinetics is real. Brange et al. 1997 J. Pharm. Sci. 86:517 is real. Klich et al. 2019 is established. The eigenmode overlap interpretation of the nucleation peak is the novel mechanistic claim — physically plausible but computationally unverified for insulin. Approximately 70% traceable. |
| **Raw Composite** | | **7.30** | 0.20×7 + 0.20×8 + 0.10×7 + 0.20×8 + 0.05×6 + 0.05×6 + 0.20×7 |
| Cross-domain bonus applied: +0.5 | | | Statistical mechanics (inverse Mpemba effect) → protein aggregation kinetics (biochemistry) → pharmaceutical sciences: 2+ disciplinary boundaries |
| **Final Composite** | | **7.80** | |

---

### E6-H1xH5: Hierarchical Spectral Scoring — Zwanzig Roughness Predicts Bimodality, Bimodality Enables Mpemba Index, Mpemba Index Predicts Aggregation Propensity

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The three-level hierarchical causal chain (Level 1: Zwanzig ε → bimodality; Level 2: bimodality ↔ Mpemba index defined; Level 3: Mpemba index → aggregation propensity) with independent falsification at each level is novel as a synthesized framework. The critical novel contribution beyond either parent (E1-H5 or E2-H1) is the Level 2 test: bimodality is claimed to be necessary and sufficient for the Mpemba index to be defined at ≥2. This is a new internal validation step absent in both parents. The failure mode attribution (Step 6) adds further novelty as a structured negative result framework. |
| Mechanistic Specificity | 20% | 9 | Three quantitative thresholds with mechanistic derivation: (1) ε_cross ~ 1.0 kT from Zwanzig formula; (2) BC > 0.555 threshold (Sarle); (3) Spearman ρ > 0.7 against ThT half-times. Each level specifies independent falsification criteria and the three must simultaneously hold. The failure mode attribution explicitly identifies which transition breaks if results are partial. This is the most mechanistically specified hypothesis in the combined ranking. |
| Cross-Field Distance | 10% | 8 | Zwanzig rough landscapes (condensed matter physics) → spectral bimodality (computational mathematics/biophysics) → Mpemba index (statistical mechanics) → aggregation propensity (biochemistry) → neurodegenerative disease (medicine). Four disciplines, three quantitative thresholds. The cross-disciplinary span is greater than individual parent hypotheses. |
| Testability | 20% | 8 | Three-level test protocol is concrete and builds on the same MSM construction infrastructure as E1-H5 and E2-H1 (8 proteins, 4+4 pairs). The key innovation is that each level independently tests a prediction, and failure at one level is diagnostically informative. Step 6 (failure mode attribution) makes even a partial negative result scientifically productive. Timeline: 4–6 months for a well-equipped computational biophysics group with existing trajectory data. |
| Impact: Paradigm | 5% | 9 | If all three levels validate, this would establish a new physical theory for amyloid aggregation propensity based on energy landscape roughness, spectral bimodality, and anomalous relaxation — a truly landmark result. The three-level structure provides the causal explanation missing from empirical aggregation predictors (TANGO, CamSol): WHY does rough energy landscape → aggregation? This could reshape the conceptual framework of protein aggregation for decades. Score of 9 reflects genuinely transformative potential. |
| Impact: Translational | 5% | 5 | The ε_cross threshold and BC criterion could become computational screening tools for amyloidogenic risk assessment in protein engineering and biopharmaceutical development. The diagnostic pathway (compute ε from MD → predict aggregation risk) is plausible if computationally validated. Moderate translational value. |
| Groundedness | 20% | 7 | Inherits groundedness from both E1-H5 (Zwanzig formula, Jia et al. 2020, Feng et al. 2026) and E2-H1 (Klich et al. 2019, Rosenman et al. 2013, Schuler et al. 2023). The quantitative thresholds are derived (not arbitrary). The novel three-level synthesis itself is the main unverified element — specifically, the Level 2 claim that bimodality is necessary and sufficient for Mpemba index ≥ 2 is a new prediction without independent verification. Score of 7 reflects high groundedness of individual components with modest uncertainty at the synthesis level. |
| **Raw Composite** | | **7.90** | 0.20×8 + 0.20×9 + 0.10×8 + 0.20×8 + 0.05×9 + 0.05×5 + 0.20×7 |
| Cross-domain bonus applied: +0.5 | | | Condensed matter physics → computational mathematics → statistical mechanics → biochemistry → medicine: 3+ disciplinary boundaries |
| **Final Composite** | | **8.40** | |

---

## Part II — Final Ranking (All 11 Hypotheses)

| Rank | ID | Source | Title (abbreviated) | Pre-Bonus | Final Composite | Cycle |
|------|----|--------|---------------------|-----------|-----------------|-------|
| 1 | **E1-H5** | Evolved C1 | Rough Landscape Diffusion Asymmetry → Spectral Signature (Sharpened) | 7.90 | **8.40** | C1 evolved |
| 1 | **E6-H1xH5** | Evolved C1 | Hierarchical Spectral Scoring (3-level causal chain) | 7.90 | **8.40** | C1 evolved |
| 3 | **E2-H1** | Evolved C1 | Mpemba Index → Aggregation Propensity (Citations Corrected) | 7.50 | **8.00** | C1 evolved |
| 3 | **E3-H7xH5** | Evolved C1 | Cooling-Rate Fibril Polymorph Selection in Insulin (Crossover) | 7.50 | **8.00** | C1 evolved |
| 5 | **E5-H4** | Evolved C1 | Inverse Mpemba Cooling Protocol Suppresses Fibril Formation | 7.30 | **7.80** | C1 evolved |
| 6 | **E4-H3** | Evolved C1 | Non-Equilibrium MSMs Reveal Non-Normal Dynamics under Hsp70 Driving | 7.20 | **7.70** | C1 evolved |
| 7 | **C2-H1** | Cycle 2 | A* State = Mpemba Overlap Coefficient (Quantitative Unification) | 6.60 | **7.10** | C2 |
| 8 | **C2-H2** | Cycle 2 | Measured D Ratio of PrP → Bimodal Eigenspectrum (Zwanzig-Kramers) | 6.45 | **6.95** | C2 |
| 9 | **C2-H5** | Cycle 2 | Resource-Theoretic Mpemba Monotone (after dropping therapeutic claims) | 6.20 | **6.70** | C2 |
| 10 | **C2-H4** | Cycle 2 | Non-Reversible MSMs Reveal Non-Normal Dynamics | 5.95 | **6.45** | C2 |
| 11 | **C2-H3** | Cycle 2 | Cooling-Rate Polymorph Selection in Abeta42 (IDP-limited) | 5.30 | **5.80** | C2 |

**Cross-domain bonus applied to all 11**: The Mpemba effect / statistical mechanics (Klich 2019 PRX; Zwanzig 1988 PNAS; resource theory) → protein biochemistry / amyloid disease bridge spans 2+ disciplinary boundaries for every hypothesis in this session.

**Pattern**: The 6 cycle-1 evolved hypotheses (E1–E6) dominate the top 6 positions. All cycle-2 hypotheses (C2-H1 through C2-H5) rank 7th–11th. This confirms the Critic's finding: iterated cycle-1 descendants significantly outperform newly generated cycle-2 hypotheses, and evolution was more productive than new generation for this target.

---

## Part III — Diversity Check

### Pairwise Mechanism Overlap Analysis (Top 5)

Post-linear-ranking Top 5: E1-H5, E6-H1xH5, E2-H1, E3-H7xH5, E5-H4

| Pair | Mechanism Overlap | Assessment |
|------|-----------------|------------|
| E1-H5 ↔ E6-H1xH5 | **>80%** | E6 IS a synthesis of E1-H5 + E2-H1; shares Zwanzig roughness → bimodality → Mpemba chain exactly. E1 is subsumed by E6. **REDUNDANT** |
| E1-H5 ↔ E2-H1 | ~55% | Both use MSM eigenspectrum; E1 predicts ε_cross threshold; E2 predicts Mpemba index aggregation correlation. Different levels of the same chain. Acceptable. |
| E1-H5 ↔ E3-H7xH5 | ~50% | Both use rough landscape asymmetry; E1 predicts aggregation classification; E3 predicts polymorph selection via T_cross. Different phenomena. Acceptable. |
| E1-H5 ↔ E5-H4 | ~35% | E1 is spectral classification; E5 is fibril suppression via cooling protocol. Different mechanisms, different experimental systems. Clear. |
| E6-H1xH5 ↔ E2-H1 | ~65% | E2-H1 is Level 3 of E6's causal chain. E6 is the broader framework. Overlap is high but E6 subsumes rather than duplicates — retaining both would be redundant. Acceptable since E1-H5 is dropped. |
| E6-H1xH5 ↔ E3-H7xH5 | ~45% | E6 predicts aggregation classification; E3 predicts fibril polymorphism via T_cross. Share rough landscape basis but different predictions and experimental systems. Acceptable. |
| E6-H1xH5 ↔ E5-H4 | ~35% | E6 is spectral framework; E5 is experimental suppression protocol. Different. Acceptable. |
| E2-H1 ↔ E3-H7xH5 | ~40% | Both use MSM eigenmodes; E2 predicts aggregation propensity from Mpemba index; E3 predicts polymorph switching from T_cross. Different predictions, different experimental systems. Acceptable. |
| E2-H1 ↔ E5-H4 | ~40% | E2 uses Mpemba index for classification; E5 uses inverse Mpemba for suppression. Different applications of Mpemba framework. Acceptable. |
| E3-H7xH5 ↔ E5-H4 | ~55% | Both involve cooling rate and fibril formation. However, E3 predicts polymorph switching at T_cross (structural identity); E5 predicts fibril yield suppression (quantity). Different phenomena, different protein systems (insulin polymorphism vs insulin fibril yield). Acceptable, but this pair should be monitored. |

### Diversity Action

**Action taken**: E1-H5 and E6-H1xH5 share >80% mechanistic overlap (E6 synthesizes E1). Per diversity rule: keep the highest-scoring and most comprehensive representation.

**Tie**: Both E1-H5 and E6-H1xH5 score 8.40. Decision criterion: E6-H1xH5 subsumes E1-H5 as Level 1 of its 3-level causal chain and adds the Level 2 (bimodality ↔ Mpemba index) and Level 3 (Mpemba index → aggregation) tests plus failure mode attribution. E6 is strictly more comprehensive and retains all of E1's scientific content. **E1-H5 is dropped from evolution selection; E6-H1xH5 is retained.**

**Promotion**: E4-H3 (7.70, #6 in linear ranking) is promoted to Top 5 to replace E1-H5.

### Post-Diversity-Check Top 5 (Evolution Selection)

| Evolution Rank | ID | Final Composite | Rationale |
|---|---|---|---|
| 1 | **E6-H1xH5** | 8.40 | Most comprehensive mechanistic framework; highest paradigm impact (9/10); 3-level independent falsification. Primary evolution target. |
| 2 | **E2-H1** | 8.00 | Clean Mpemba index classifier; computationally executable in 3 months; high groundedness; complementary to E6 (its Level 3). |
| 3 | **E3-H7xH5** | 8.00 | Most experimentally distinctive; T_cross discriminant vs Ostwald competition; insulin at pH 2 is accessible. Structural biology prediction distinct from classification framework. |
| 4 | **E5-H4** | 7.80 | Most immediately executable experimentally (2–3 months, basic ThT assay); highest translational impact (insulin formulation). First hypothesis that should be tested. |
| 5 | **E4-H3** | 7.70 | Non-equilibrium MSM framework is the most distinct mechanistically; Hsp70-driven non-normality addresses cellular context absent from all other hypotheses. Maximum diversity value. |

**Note on E1-H5**: Although excluded from evolution selection due to overlap with E6-H1xH5, E1-H5 (8.40) remains the single best-grounded individual component and should be treated as the computational core of E6's Level 1 test.

---

## Part IV — Elo Tournament Sanity Check

### Top 6 for tournament

E1-H5 (8.40), E6-H1xH5 (8.40), E2-H1 (8.00), E3-H7xH5 (8.00), E5-H4 (7.80), E4-H3 (7.70)

### Pairwise comparisons (15 total)

**Question per pair**: "Which hypothesis would a domain researcher want to test FIRST, and why?"

| Match | Winner | Reasoning |
|-------|--------|-----------|
| E1-H5 vs E6-H1xH5 | **E6** | E6 subsumes E1 into a three-level causal framework that generates more informative outcomes even on partial failure. Testing E6 tests E1 as its first level. |
| E1-H5 vs E2-H1 | **E1** | E1 provides the physical mechanism (roughness → bimodality → ε_cross) that would validate E2's aggregation correlation. Researchers would test the physical foundation before the prediction. |
| E1-H5 vs E3-H7xH5 | **E1** | E1's computational BC threshold test uses existing trajectory data and requires no new experiments. E3 requires new insulin in vitro experiments plus MSM construction. E1 is faster to test first. |
| E1-H5 vs E5-H4 | **E5** | E5 requires only a spectrofluorometer and basic protein preparation — 2–3 month timeline. E1 requires MSM construction for 8 proteins — 3–5 months. The experimental simplicity of E5 wins pairwise. |
| E1-H5 vs E4-H3 | **E1** | E4 requires coarse-grained Hsp70-coupled simulations and stopped-flow FRET — technically demanding setup. E1's computational test is faster and less specialized. |
| E6-H1xH5 vs E2-H1 | **E2** | E2 is the simplest test of the Mpemba index prediction and serves as a fast validation step before committing to E6's full three-level protocol. Researchers prefer quick validation before investment. |
| E6-H1xH5 vs E3-H7xH5 | **E3** | E3's experimental T_cross crossover test can refute or confirm eigenmode branching in a single well-designed experiment. E6 requires full MSM infrastructure for 8 proteins. E3 offers the fastest experimental verdict. |
| E6-H1xH5 vs E5-H4 | **E5** | Same reasoning as E1 vs E5: E5 is the most experimentally immediate hypothesis (ThT assay, 2–3 months). E6 is the most theoretically comprehensive. Researchers prefer experimental validation early. |
| E6-H1xH5 vs E4-H3 | **E6** | E4's non-equilibrium MSM + stopped-flow FRET design is more technically demanding than E6's equilibrium MSM + eigendecomposition. E6 wins on comparative technical accessibility. |
| E2-H1 vs E3-H7xH5 | **E2** | E2 uses published conformational ensembles (Rosenman 2013, existing alpha-synuclein trajectories) — pure computational test in 3 months. E3 requires new MD simulation of insulin pH 2 + in vitro experiments. E2 is faster. |
| E2-H1 vs E5-H4 | **E5** | E5 has a more immediate experimental protocol (bench experiment) vs E2's computational pipeline (MSM construction, eigendecomposition, ThT literature comparison). Researchers prefer wet lab feasibility for early validation. |
| E2-H1 vs E4-H3 | **E2** | E2 is a pure computational test on existing data. E4 requires non-equilibrium MD + Hsp70 experimental reconstitution. E2 wins on speed and technical accessibility. |
| E3-H7xH5 vs E5-H4 | **E5** | E5 (ThT assay on insulin pH 2) requires no specialized structural biology equipment. E3 requires cryo-EM, solid-state NMR, and FTIR — all specialized. E5 is far more accessible. |
| E3-H7xH5 vs E4-H3 | **E3** | E3's experimental protocol, while requiring specialized characterization, provides cleaner falsification (T_cross crossover) than E4's complex non-equilibrium simulation + FRET setup. E3 wins on experimental clarity. |
| E5-H4 vs E4-H3 | **E5** | E5 is a simple bench experiment. E4 requires non-equilibrium simulations and specialized chaperone FRET assays. E5 wins overwhelmingly on experimental accessibility. |

### Win tallies

| ID | Wins | Losses | Win Rate |
|----|------|--------|----------|
| **E5-H4** | 5 | 0 | **1.00** |
| **E1-H5** | 3 | 2 | **0.60** |
| **E2-H1** | 3 | 2 | **0.60** |
| **E6-H1xH5** | 2 | 3 | **0.40** |
| **E3-H7xH5** | 2 | 3 | **0.40** |
| **E4-H3** | 0 | 5 | **0.00** |

### Elo ranking

1. E5-H4 (5 wins)
2. E1-H5 / E2-H1 (tied, 3 wins each)
4. E6-H1xH5 / E3-H7xH5 (tied, 2 wins each)
6. E4-H3 (0 wins)

### Linear composite vs. Elo comparison

| Rank | Linear Composite | Elo Tournament |
|------|-----------------|----------------|
| 1–2 | E1-H5 / E6-H1xH5 (8.40) | **E5-H4** (5/5 wins) |
| 3–4 | E2-H1 / E3-H7xH5 (8.00) | E1-H5 / E2-H1 (3/5 wins) |
| 5 | E5-H4 (7.80) | E6-H1xH5 / E3-H7xH5 (2/5 wins) |
| 6 | E4-H3 (7.70) | E4-H3 (0/5 wins) |

**Verdict**: Rankings DIVERGE. The linear composite places E5-H4 at rank 5; the Elo tournament places it at rank 1.

**Divergence explanation**: E5-H4 wins every pairwise comparison because it has **proximal experimental testability** that the linear Testability score (8/10) captures in magnitude but not in degree of immediacy. The linear Testability dimension measures "can a PhD student test this in 3 months with existing methods?" — all top-6 score 7–8 on this. But E5-H4 is the ONLY hypothesis testable in 2–3 months with no specialized equipment (spectrofluorometer + insulin + pH 2 buffer). Every other hypothesis requires either MSM construction from published or new trajectories (E1, E2, E6), specialized structural biology (cryo-EM, ssNMR for E3), or non-equilibrium simulation infrastructure (E4). The pairwise comparison captures this immediacy gradient that the linear 1–10 scale compresses.

**What E5-H4 lacks that keeps it at rank 5 linearly**: Lower Novelty (7 vs 8), lower Cross-Field Distance (7 vs 7–8), lower Impact-Paradigm (6 vs 7–9). The linear composite gives equal weight to conceptual dimensions that researchers value theoretically but not in first-to-test decisions.

**Diagnostic signal for evolution**: **E5-H4 should be the first hypothesis tested experimentally**, even though E6-H1xH5 is the most theoretically compelling. The divergence recommends running E5-H4 in parallel as a fast-feedback experiment while the computational MSM infrastructure for E6/E2 is being built. **E4-H3 (0 Elo wins) should be evolution-deprioritized** — its non-equilibrium MSM complexity imposes the highest barrier to falsification.

---

## Summary

**Evolution selection (post-diversity-check, ordered for testing priority):**

1. **E6-H1xH5** (8.40) — Hierarchical framework; highest theoretical value; primary computational target
2. **E5-H4** (7.80) — START HERE experimentally; 2–3 month bench test; immediate feedback for the broader framework
3. **E2-H1** (8.00) — Computational Mpemba index validation; 3 months with existing data; Level 3 validation for E6
4. **E3-H7xH5** (8.00) — T_cross polymorph prediction; unique experimental discriminant; test after E5
5. **E4-H3** (7.70) — Non-equilibrium cellular context; maximum diversity; lower priority due to experimental complexity

**Note on cycle-2 survivors**: All 5 cycle-2 hypotheses (C2-H1 through C2-H5) rank below their cycle-1 evolved counterparts. The highest-ranking cycle-2 survivor is C2-H1 at 7.10 (rank 7). This pattern — cycle-1 evolved > cycle-2 new generation — confirms the evolver's diversity constraint worked correctly and that further evolution of the cycle-1 hypotheses was more productive than novel generation. C2-H1 (A* unification) and C2-H5 (resource theory) have sufficient novelty and cross-field distance to merit mentioning in the session report, even without evolution selection.
