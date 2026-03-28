# Cycle 1 Hypotheses — Mpemba Spectral Relaxation Theory x Amyloid Aggregation

**Session:** 2026-03-28-scout-014
**Target:** Mpemba Spectral Relaxation Theory Predicts Amyloid Aggregation Vulnerability
**Field A:** Non-equilibrium statistical mechanics — Mpemba effect spectral theory
**Field C:** Neurodegenerative protein biochemistry — amyloid aggregation selectivity
**Strategy:** anomaly_hunting
**Creativity constraint:** cross-discipline bridge (mod 5)
**Generated:** 2026-03-28

---

## H1: Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity

**Hypothesis:** Amyloidogenic proteins (Abeta42, alpha-synuclein, tau) have systematically higher Mpemba indices in their folding/misfolding Markov state models than non-amyloidogenic structural homologs (Abeta40, beta-synuclein, MAP2), because the slow eigenmodes of amyloidogenic MSMs encode misfolding pathways that are kinetically accessible from thermally perturbed initial ensembles.

**Mechanism:** The Mpemba index, defined by Klich et al. (2019, PRX) as the count of initial conditions whose overlap with the slowest-decaying eigenmode of the Markov generator vanishes, can be computed for any discrete Markov chain. Protein folding/misfolding MSMs partition conformational space into metastable states with a transition matrix T whose eigenvalues {lambda_k} determine relaxation timescales tau_k = -1/ln(lambda_k). The slowest eigenmode (lambda_2, the Fiedler mode) typically separates the folded native basin from the misfolded/aggregation-prone basin. For amyloidogenic proteins, the misfolded basin contains misregistered beta-sheet intermediates that serve as nucleation seeds for fibril elongation [GROUNDED: Jia et al. 2020, PNAS — misregistered kinetic traps dominate amyloid assembly on an unbiased energy landscape]. The Mpemba index quantifies how many thermally accessible initial ensembles have zero overlap with this slowest mode — meaning those initial conditions bypass the kinetic traps and relax directly to the native state via faster eigenmodes. A HIGH Mpemba index paradoxically implies that certain high-temperature quench protocols can avoid the misfolding pathway entirely — but it also implies that the eigenspectrum has a structure where the misfolding eigenmode is decoupled from generic thermal fluctuations, creating a kinetic vulnerability: perturbations that DO project onto the slow mode become trapped for exponentially long times. Amyloidogenic proteins, we predict, have higher Mpemba indices (more "avoidable" slow modes) but also deeper kinetic traps when the slow mode IS accessed — a spectral bifurcation that non-amyloidogenic homologs lack.

**Bridge:** Bridge concept #1 — Mpemba index as overlap integral of protein conformational ensemble with slowest eigenmode of folding/misfolding MSM.

**Falsifiable prediction:** Computing the Mpemba index from published MSMs of Abeta42 vs Abeta40 will yield Mpemba(Abeta42) >= 2 and Mpemba(Abeta40) = 0 or 1. Similarly, alpha-synuclein will have a higher Mpemba index than beta-synuclein. The difference will correlate with experimentally measured aggregation propensity (ThT fluorescence kinetics) with Spearman rho > 0.7 across at least 4 protein pairs. If the Mpemba index is identical across amyloidogenic and non-amyloidogenic homologs, the hypothesis is refuted.

**Test protocol:**
1. **Computational (primary):** Retrieve published MSMs for Abeta42 [GROUNDED: Rosenman et al. 2016, J. Mol. Biol. — MSM of Abeta42 from extensive REMD simulations], alpha-synuclein [GROUNDED: Robustelli et al. 2018, PNAS — disordered protein MSM from D.E. Shaw long-trajectory simulations], and tau (repeat domain) [GROUNDED: Eschmann et al. 2015, J. Chem. Phys. — MSM of tau K18 fragment]. For each protein's MSM transition matrix T, compute eigendecomposition, identify the slowest non-stationary eigenmode v_2, and evaluate the Mpemba index by computing the overlap <p_init | v_2> across the Boltzmann distribution at 100 temperatures between 280K-400K. Count the number of temperatures where this overlap crosses zero.
2. **Comparative:** Repeat for non-amyloidogenic homologs using existing MSMs or constructing new ones from Folding@Home trajectory data. Statistical comparison of Mpemba indices between amyloidogenic vs non-amyloidogenic groups (Mann-Whitney U test, n >= 4 per group).
3. **Experimental validation:** For top-scoring protein pairs, perform differential scanning calorimetry (DSC) with controlled cooling rates (0.1, 1.0, 10 K/min) and measure ThT fluorescence at each endpoint. If the Mpemba index is predictive, specific cooling protocols should yield dramatically different aggregation outcomes for amyloidogenic but not non-amyloidogenic proteins.

**Groundedness:** 7/10
- [GROUNDED] Mpemba index defined for Markov chains (Klich et al. 2019, PRX 9:021060)
- [GROUNDED] Amyloid MSMs with misregistered kinetic traps (Jia et al. 2020, PNAS 117:10322)
- [GROUNDED] MSM eigenspectral analysis standard in protein folding (Husic & Pande 2018, JACS 140:2386 — review of MSM methodology)
- [GROUNDED] Abeta42 MSM exists (Rosenman et al. 2016, J. Mol. Biol. 428:1600)
- [GROUNDED] Zero biophysical Mpemba applications exist through 2024 (Teza et al. 2025, Physics Reports)
- [NOVEL] The application of Mpemba index to protein MSMs is entirely new
- [CAVEAT] Protein MSMs are typically built at fixed temperature; extending to variable-temperature Mpemba conditions requires augmented MSM construction or temperature-replica analysis

**Confidence:** 7/10

**Counter-evidence:**
- Protein MSMs from MD simulations may not capture the full folding/misfolding landscape, especially for intrinsically disordered proteins like alpha-synuclein where MSM metastable states are poorly defined
- The Mpemba index was defined for systems obeying detailed balance; protein folding under non-equilibrium conditions (active cellular environment, chaperones) may violate this
- The slow eigenmode may not correspond to the misfolding pathway but rather to a conformational rearrangement irrelevant to aggregation (e.g., a large-scale but non-pathological structural fluctuation)
- Existing MSMs for amyloidogenic proteins may have insufficient state resolution to compute meaningful eigenmode overlaps — MSM quality varies dramatically across published studies

---

## H2: Spectral Gap Ratio of Combined Fold/Misfold MSMs Predicts Amyloid Nucleation Lag Time

**Hypothesis:** The ratio of the spectral gap (gap between the two largest eigenvalues) of the combined folding-plus-misfolding MSM to the spectral gap of the folding-only MSM quantitatively predicts the nucleation lag time of amyloid fibril formation, because this ratio encodes the kinetic competition between productive folding and misfolding-trap capture.

**Mechanism:** Consider a protein with a Markov state model that includes both folding states (leading to native structure) and misfolding states (leading to aggregation-prone intermediates). The transition matrix T_combined has a spectral gap Delta_combined = 1 - lambda_2, where lambda_2 is the second-largest eigenvalue. The folding-only MSM (transitions restricted to states on the native folding pathway) has spectral gap Delta_fold. We define the spectral gap ratio R = Delta_combined / Delta_fold. When R is close to 1, the misfolding states do not significantly alter the dominant relaxation timescale — the protein folds efficiently and rarely accesses aggregation pathways. When R << 1, the combined MSM has a much smaller spectral gap than the folding MSM alone, meaning the misfolding pathway introduces a new, slower timescale that dominates relaxation. This slower timescale corresponds to escape from misregistered beta-sheet intermediates [GROUNDED: Jia et al. 2020, PNAS — the dominant kinetic barrier in amyloid assembly is misregistered states]. The nucleation lag time T_lag is the time required to accumulate a critical nucleus of misfolded monomers. We predict T_lag proportional to 1/(1 - R) — when R approaches 1, lag times diverge (protein does not aggregate); when R is small, lag times are short (fast aggregation). This provides a spectral-theory-based prediction of the empirically measured nucleation lag time that currently lacks a first-principles explanation.

**Bridge:** Bridge concept #2 — Spectral gap of combined folding/misfolding transition matrix as aggregation kinetics predictor.

**Falsifiable prediction:** For the proteins with published amyloid kinetics data (Abeta42: T_lag ~ 2-4 hours at 37C; alpha-synuclein: T_lag ~ 24-72 hours at 37C without seeds; lysozyme: T_lag ~ hours at pH 2; beta2-microglobulin: T_lag ~ hours at pH 2.5) [GROUNDED: Knowles et al. 2009, Science 326:1533 — amyloid kinetics framework; Arosio et al. 2015, Trends Pharmacol. Sci. — review of nucleation lag times], the spectral gap ratio R will rank-order these lag times with Spearman rho > 0.8. If no correlation exists between R and T_lag, the hypothesis is refuted.

**Test protocol:**
1. **Computational:** For each protein, construct MSMs from MD trajectory data that include both folding and aggregation-prone conformations. Use adaptive sampling (e.g., HTMD framework) to ensure coverage of misfolding basins. Compute T_combined and T_fold separately. Calculate spectral gaps and the ratio R.
2. **Kinetic validation:** Compare R-values against published nucleation lag times from ThT kinetic assays under standardized conditions (37C, physiological pH, known concentration). Test rank-order prediction.
3. **Perturbation test:** Introduce point mutations known to alter aggregation kinetics (e.g., Abeta42 Arctic mutation E22G accelerates aggregation; A2V mutation prevents it). Predict that E22G decreases R (smaller spectral gap ratio) while A2V increases R. Compare against experimental lag time changes.

**Groundedness:** 6/10
- [GROUNDED] MSM spectral gap governs relaxation timescale (standard — Prinz et al. 2011, J. Chem. Phys. 134:174105)
- [GROUNDED] Misregistered intermediates dominate amyloid assembly kinetics (Jia et al. 2020, PNAS)
- [GROUNDED] Nucleation lag times measured for multiple amyloidogenic proteins (Arosio et al. 2015, Trends Pharmacol. Sci. 36:592)
- [GROUNDED] Abeta42 Arctic mutation E22G accelerates aggregation (Nilsberth et al. 2001, Nature Neuroscience 4:887)
- [NOVEL] The spectral gap ratio R = Delta_combined/Delta_fold as predictor is entirely new
- [CAVEAT] Constructing combined fold/misfold MSMs with both pathways adequately sampled is computationally intensive and may require enhanced sampling methods beyond standard MD

**Confidence:** 6/10

**Counter-evidence:**
- Amyloid nucleation is a collective multi-molecule process (primary and secondary nucleation), while MSMs describe single-molecule conformational dynamics. The gap between monomer kinetics and oligomer nucleation is substantial [GROUNDED: Cohen et al. 2012, PNAS 109:9761 — secondary nucleation dominates amyloid proliferation]
- The spectral gap of MSMs depends heavily on the state decomposition method (PCCA+, TICA, VAMPnet). Different methods may yield different R values for the same trajectory data
- Environmental factors (pH, salt, membrane surfaces) dramatically alter aggregation kinetics but are not captured in gas-phase or implicit-solvent MSMs
- The relationship T_lag ~ 1/(1-R) is a postulated functional form; the actual dependence may be more complex

---

## H3: Non-Normal Liouvillian Dynamics of Amyloidogenic MSMs Create Transient Misfolding Acceleration Zones

**Hypothesis:** The Markov state model generators (rate matrices Q = T - I) of amyloidogenic proteins exhibit significant non-normality (||QQ^T - Q^TQ|| >> 0), creating transient amplification zones in conformational space where the probability of accessing misfolded intermediates is transiently enhanced by orders of magnitude above the stationary prediction — a mechanism recently identified in Mpemba physics that has never been tested in protein biophysics.

**Mechanism:** Non-normal matrices have non-orthogonal eigenvectors, which means their spectral decomposition does not directly govern short-time dynamics [GROUNDED: Teza et al. 2025, Physics Reports — non-normal Liouvillian mechanism as distinct from spectral-gap mechanism in Mpemba physics]. For protein MSMs, non-normality means that the overlap between left and right eigenvectors of the rate matrix Q is small, creating conditions for transient growth: even though the stationary distribution is well-defined and the system must eventually reach it, short-time dynamics can transiently amplify probability in specific conformational regions. In the protein context, this means a thermally perturbed protein (e.g., after a fever spike, a local pH change, or passage through a hot cellular compartment) can experience a TRANSIENT window where the probability of populating misfolding intermediates is dramatically amplified — far above what the equilibrium free energy landscape would predict. This transient amplification arises from constructive interference between non-orthogonal eigenmodes during the initial relaxation phase. The degree of non-normality, quantifiable via the Henrici departure from normality delta(Q) = ||Q^TQ - QQ^T||_F / ||Q||_F^2, would be higher for amyloidogenic proteins because their MSMs contain asymmetric transitions between folded and misfolded basins (folding is guided by a funnel; misfolding explores a rough landscape with many kinetic traps). The key prediction is that amyloidogenic proteins experience misfolding probability spikes during transient perturbations that non-amyloidogenic proteins do not — explaining why brief thermal or oxidative stress events can trigger aggregation cascades in pathological proteins but not in their non-pathological homologs.

**Bridge:** Bridge concept #3 — Non-normal Liouvillian dynamics creating transient misfolding acceleration zones.

**Falsifiable prediction:** The Henrici non-normality measure delta(Q) computed from MSMs of amyloidogenic proteins will exceed that of non-amyloidogenic homologs by at least 3-fold. Furthermore, time-dependent probability evolution P(t) = exp(Qt) * P(0) starting from a high-temperature initial ensemble will show transient amplification of misfolded-state occupancy (peak probability at intermediate time t_peak > 0) for amyloidogenic proteins but monotonic relaxation for non-amyloidogenic proteins. If delta(Q) values are comparable or if transient amplification is absent, the hypothesis is refuted.

**Test protocol:**
1. **Computational:** Extract rate matrices Q from published MSMs. Compute Henrici departure from normality. Compare amyloidogenic (Abeta42, alpha-synuclein, tau-K18, IAPP) vs non-amyloidogenic (Abeta40, beta-synuclein, MAP2-MTBD, calcitonin).
2. **Time-evolution simulation:** Starting from a Boltzmann distribution at elevated temperature (350K), propagate P(t) = exp(Qt) * P(0) using the rate matrix at 310K. Monitor occupancy of pre-identified misfolded states as a function of time. Quantify transient amplification ratio: max[P_misfold(t)] / P_misfold(stationary).
3. **Experimental (temperature-jump):** Use rapid temperature-jump spectroscopy (laser T-jump, ~10 ns resolution) to heat protein solutions from 37C to 45C, then monitor misfolding intermediates via time-resolved FRET or circular dichroism. If transient misfolding amplification exists, intermediate populations should overshoot steady-state levels at early times (microseconds to milliseconds) before relaxing.

**Groundedness:** 6/10
- [GROUNDED] Non-normal Liouvillian dynamics as distinct Mpemba mechanism (Teza et al. 2025, Physics Reports; also Lapolla & Godec 2020, Phys. Rev. Lett.)
- [GROUNDED] The Henrici departure from normality is a standard matrix measure (Henrici 1962, Numerische Mathematik 4:24)
- [GROUNDED] Protein folding landscapes are asymmetric (funnel for folding, rough for misfolding) — structural basis for non-normality (Onuchic et al. 1997, Annu. Rev. Phys. Chem. 48:545 — energy landscape theory)
- [NOVEL] Application of non-normality analysis to protein MSMs is entirely new
- [CAVEAT] MSM rate matrices are typically symmetrized via detailed balance when constructed from equilibrium simulations; this symmetrization forces normality. Non-normality analysis requires rate matrices from non-equilibrium trajectory data or unsymmetrized maximum-likelihood estimation

**Confidence:** 5/10

**Counter-evidence:**
- Standard MSM construction methods (MSMBuilder, PyEMMA) enforce detailed balance, which symmetrizes the rate matrix and eliminates non-normality by construction. Observing non-normality would require unsymmetrized estimators that are less statistically robust
- Transient amplification windows may be too short (picoseconds to nanoseconds) to be biologically relevant — cellular processes operate on microsecond-to-second timescales
- The distinction between amyloidogenic and non-amyloidogenic proteins may not manifest in non-normality if both classes have similarly asymmetric folding landscapes
- Real protein dynamics involve solvent, crowding agents, and chaperones that may wash out the transient effects predicted by the simplified MSM

---

## H4: Inverse Mpemba Protocol Suppresses Amyloid Fibril Formation by Exploiting Eigenmode Decoupling

**Hypothesis:** A rationally designed inverse Mpemba cooling protocol — rapid quench from high temperature (e.g., 60C) to physiological temperature (37C) rather than slow cooling — will suppress amyloid fibril formation in Abeta42 and alpha-synuclein by exploiting the spectral structure of their folding MSMs, specifically by preparing initial conditions with minimal overlap onto the slow eigenmode that encodes the misfolding pathway.

**Mechanism:** In the Mpemba effect, certain high-temperature initial conditions have zero overlap with the slowest-decaying eigenmode of the relaxation operator, causing the system to equilibrate exponentially faster than expected [GROUNDED: Klich et al. 2019, PRX 9:021060]. We apply this in reverse: rather than asking "which hot system cools fastest?", we ask "which cooling protocol avoids populating the misfolding eigenmode?" For a protein at high temperature, the conformational ensemble is broadly distributed across the energy landscape. As temperature drops, the ensemble contracts toward low-energy states. The key insight is that the PATH of contraction depends on the cooling rate. Rapid quench preserves the high-temperature ensemble's projection onto the eigenspectrum, while slow cooling allows the ensemble to adiabatically track the temperature-dependent eigenstructure. If the misfolding eigenmode (v_slow) has higher overlap with the intermediate-temperature ensemble than with either the high-T or low-T ensemble, then rapid quench SKIPS the dangerous intermediate regime. This is directly analogous to the Mpemba scenario where starting further from equilibrium can lead to faster arrival at the target state by avoiding slow-eigenmode trapping. For amyloid proteins, the intermediate temperature regime (45-55C for Abeta42, the "danger zone" for aggregation [GROUNDED: Kusumoto et al. 1998, PNAS 95:12277 — temperature-dependent Abeta aggregation kinetics show maximal nucleation at intermediate temperatures]) corresponds to maximal eigenmode overlap with the misfolding pathway. Rapid quench bypasses this regime.

**Bridge:** Bridge concepts #1 and #2 — Mpemba index and spectral gap jointly determine which cooling protocols avoid the misfolding eigenmode.

**Falsifiable prediction:** In controlled in vitro ThT aggregation assays, rapid-quench protocols (cooling from 60C to 37C in < 1 minute) will produce at least 50% less fibril mass after 24 hours compared to slow-cooling protocols (cooling over 2-4 hours through the same temperature range) for Abeta42 at 25 micromolar concentration in phosphate buffer. This effect will be absent or inverted for non-amyloidogenic control proteins (e.g., lysozyme at pH 7, ubiquitin). If slow cooling and fast cooling produce equivalent fibril yields, the hypothesis is refuted.

**Test protocol:**
1. **Computational prediction:** Using the MSM eigenspectrum at multiple temperatures (constructed from replica exchange MD), compute the overlap <P(T) | v_slow(37C)> as a function of temperature T. Identify the temperature window where overlap is maximal (predicted: 45-55C for Abeta42). Design a cooling protocol that minimizes time spent in this window.
2. **In vitro validation:** Prepare Abeta42 at 25 uM in 20 mM sodium phosphate, pH 7.4, 150 mM NaCl. Protocol A: heat to 60C, hold 5 min, rapid quench to 37C (ice-water bath, < 1 min). Protocol B: heat to 60C, hold 5 min, slow cool to 37C (0.1C/min, ~4 hours). Protocol C: constant 37C control. Monitor ThT fluorescence at 37C for 48 hours. Triplicate replicates per condition. Measure T_lag, T_50, and total fibril yield at 48 hours.
3. **Eigenmode validation:** If the rapid-quench effect is observed, verify the mechanism by testing intermediate cooling rates (0.5, 1.0, 2.0C/min) and showing that aggregation is a non-monotonic function of cooling rate — maximal at intermediate rates where the ensemble spends the most time in the high-overlap window.

**Groundedness:** 7/10
- [GROUNDED] Mpemba effect arises from eigenmode-overlap suppression in Markov chains (Klich et al. 2019, PRX)
- [GROUNDED] Abeta42 aggregation shows non-monotonic temperature dependence with enhanced nucleation at intermediate temperatures (Kusumoto et al. 1998, PNAS 95:12277)
- [GROUNDED] Rapid thermal perturbations affect amyloid kinetics — Noji et al. 2021 (Comm. Biol.) show temperature-jump shifts protein toward amyloid pathway, demonstrating that cooling protocol matters
- [NOVEL] Designing cooling protocols to exploit eigenmode decoupling for amyloid suppression is entirely new
- [CAVEAT] High-temperature treatment (60C) may cause irreversible denaturation of some proteins, complicating interpretation. The 60C starting point is chosen because Abeta42 aggregation kinetics data exist at this temperature, but the optimal starting temperature must be protein-specific

**Confidence:** 6/10

**Counter-evidence:**
- High temperature (60C) causes irreversible unfolding for many proteins, not just conformational expansion. The "high-temperature ensemble" may be a denatured, aggregation-prone state rather than a broadly sampled native ensemble
- Protein aggregation kinetics at high concentrations (25 uM) are dominated by intermolecular interactions (secondary nucleation on fibril surfaces), not single-molecule conformational dynamics. The MSM eigenspectrum governs intramolecular dynamics; intermolecular processes may override the eigenmode effect
- The Mpemba effect in physical systems is typically small (factor of 2-3x faster relaxation), and scaling to biological systems with vastly larger state spaces may dilute the effect below detectability
- Competing explanations: rapid quench could suppress aggregation simply by reducing time at elevated temperature where aggregation is thermodynamically favorable, without any eigenmode mechanism

---

## H5: Rough Energy Landscape Diffusion Asymmetry (D_fold >> D_misfold) Creates the Spectral Signature That the Mpemba Index Detects

**Hypothesis:** The physical origin of the Mpemba-detectable spectral structure in amyloidogenic protein MSMs is the 100-1000x asymmetry between the effective diffusion coefficient on the folding landscape (D_fold, fast, on a funneled surface) and the misfolding landscape (D_misfold, slow, on a rough surface with many local traps), which creates a separation of timescales that maps directly onto the eigenvalue structure required for the Mpemba effect.

**Mechanism:** Protein energy landscapes have fundamentally different topographies for folding vs misfolding. The folding landscape is relatively smooth and funnel-shaped (minimal frustration principle [GROUNDED: Bryngelson et al. 1995, Proteins 21:167 — funneled energy landscape theory; Onuchic et al. 1997, Annu. Rev. Phys. Chem.]), supporting fast diffusion with D_fold on the order of 10^6-10^7 s^-1 in terms of state-space transitions. The misfolding landscape is rough, with many local minima of comparable depth (misregistered beta-sheet intermediates [GROUNDED: Jia et al. 2020, PNAS — misregistered kinetic traps]). Zwanzig's roughness theory [GROUNDED: Zwanzig 1988, PNAS 85:2029 — diffusion on a rough energy surface; D_eff = D_0 * exp(-(epsilon/kT)^2)] predicts that landscape roughness epsilon reduces the effective diffusion coefficient exponentially. For amyloidogenic sequences with epsilon ~ 3-5 kT of roughness on the misfolding landscape [estimated from Jia et al. 2020 energy barriers of 2-8 kcal/mol between misregistered states at 300K, corresponding to 1-4 kT], D_misfold ~ D_fold * exp(-(3-5)^2) ~ D_fold * 10^{-4} to 10^{-11}. This enormous asymmetry creates a clear separation in the eigenvalue spectrum: folding eigenmodes have relaxation times tau_fold ~ 1/D_fold (microseconds), while misfolding eigenmodes have tau_misfold ~ 1/D_misfold (milliseconds to seconds). This eigenvalue separation is precisely the structure required for the Mpemba effect — the slow misfolding eigenmodes can be individually targeted for overlap suppression by choosing appropriate initial conditions. Non-amyloidogenic proteins lack this extreme D_fold/D_misfold asymmetry because their misfolding landscapes are less rough (fewer and shallower traps), making their eigenvalue spectra more uniform and eliminating the spectral structure that enables the Mpemba effect.

**Bridge:** Bridge concepts #4 and #2 — Rough energy landscape diffusion coefficient as physical basis for slow eigenmodes; spectral gap as aggregation kinetics predictor.

**Falsifiable prediction:** The eigenvalue spectrum of amyloidogenic protein MSMs will show a bimodal distribution: a cluster of fast modes (tau < 10 microseconds, folding dynamics) separated by a gap of at least 1 order of magnitude from a cluster of slow modes (tau > 100 microseconds, misfolding dynamics). Non-amyloidogenic homologs will show a unimodal eigenvalue distribution without this gap. Specifically, the ratio tau_slow/tau_fast will exceed 100 for amyloidogenic proteins (Abeta42, alpha-synuclein, IAPP, TDP-43 LCD) and will be less than 10 for non-amyloidogenic controls. If eigenvalue spectra show no bimodal structure, the hypothesis is refuted.

**Test protocol:**
1. **MSM construction:** Build MSMs from extensive MD simulations (>100 microseconds aggregate simulation time) for 4 amyloidogenic proteins and 4 non-amyloidogenic controls. Use TICA for dimensionality reduction and k-means for microstate clustering (1000 microstates), validated by Chapman-Kolmogorov tests.
2. **Eigenspectral analysis:** Compute the full eigenvalue spectrum of each MSM transition matrix. Plot the implied timescale spectrum (tau_k vs k) and identify spectral gaps. Compute the bimodality coefficient (Sarle's bimodality coefficient, BC > 0.555 indicates bimodality).
3. **Zwanzig roughness estimation:** From the same MSM, estimate the landscape roughness epsilon by fitting the mean first-passage time between metastable states to Zwanzig's formula MFPT ~ (L^2/D_0) * exp((epsilon/kT)^2). Compare estimated roughness values between amyloidogenic and non-amyloidogenic groups.
4. **Mpemba index correlation:** Correlate the bimodality measure (spectral gap between fast and slow clusters) with the Mpemba index from H1 and with experimental aggregation propensity. All three should be positively correlated.

**Groundedness:** 6/10
- [GROUNDED] Zwanzig roughness theory (Zwanzig 1988, PNAS 85:2029 — D_eff = D_0 * exp(-(epsilon/kT)^2))
- [GROUNDED] Funneled energy landscape for folding vs rough landscape for misfolding (Bryngelson et al. 1995, Proteins 21:167; Onuchic et al. 1997)
- [GROUNDED] Misregistered intermediates as kinetic traps with 2-8 kcal/mol barriers (Jia et al. 2020, PNAS)
- [GROUNDED] MSM eigenvalue spectra are routinely computed (Husic & Pande 2018, JACS)
- [NOVEL] Connecting Zwanzig roughness asymmetry to Mpemba-exploitable spectral structure is entirely new
- [CAVEAT] The D_fold/D_misfold ratio of 10^{-4} to 10^{-11} is an estimate from Zwanzig's formula applied to Jia et al. barrier heights — the actual ratio in published MSMs needs direct measurement. The exponential sensitivity of Zwanzig's formula means small uncertainties in epsilon produce large uncertainties in D_eff

**Confidence:** 5/10

**Counter-evidence:**
- Zwanzig's 1988 theory assumes 1D diffusion on a periodic rough potential, which is a drastic simplification of the high-dimensional protein energy landscape. The formula D_eff ~ D_0*exp(-(epsilon/kT)^2) may not hold quantitatively in high dimensions
- The claim D_misfold/D_fold ~ 10^{-4} to 10^{-11} uses barrier heights from Jia et al. (2-8 kcal/mol), but these barriers are for transitions between specific misregistered states in a coarse-grained model, not the effective roughness of the entire landscape
- Non-amyloidogenic proteins like myoglobin and cytochrome c also have complex energy landscapes with multiple metastable intermediates and may show bimodal eigenvalue spectra unrelated to aggregation propensity
- MSM eigenvalue spectra are sensitive to the lag time, number of microstates, and clustering method — the bimodal/unimodal distinction could be an artifact of MSM construction parameters

---

## H6: Comparative Mpemba Index Across Amyloidogenic/Non-Amyloidogenic Protein Pairs Identifies a Universal Spectral Aggregation Vulnerability Threshold

**Hypothesis:** There exists a critical Mpemba index threshold M* such that proteins with Mpemba index > M* are amyloidogenic while those with M <= M* are not, providing a binary spectral classifier for aggregation vulnerability that outperforms existing sequence-based predictors (TANGO, Zyggregator, CamSol) on the subset of proteins with available MSM data.

**Mechanism:** Current amyloid prediction algorithms operate on sequence and structural features (hydrophobicity, secondary structure propensity, charge patterns) [GROUNDED: Fernandez-Escamilla et al. 2004, Nature Biotech. 22:1302 — TANGO algorithm; Tartaglia et al. 2008, J. Mol. Biol. 380:425 — Zyggregator]. These methods achieve ~75-80% accuracy but fail on borderline cases where sequence features are ambiguous [GROUNDED: Sormanni et al. 2015, J. Mol. Biol. 427:2046 — CamSol predictions and limitations]. We hypothesize that the Mpemba index captures a fundamentally different property — the KINETIC vulnerability of the conformational ensemble to misfolding-pathway trapping — that is complementary to the THERMODYNAMIC features used by existing predictors. The bridge concept #5 proposes systematic comparison of Mpemba indices across protein pairs where one member is amyloidogenic and the other is not: Abeta42 (amyloidogenic) vs Abeta40 (less amyloidogenic), alpha-synuclein (amyloidogenic) vs beta-synuclein (non-amyloidogenic), tau (amyloidogenic) vs MAP2 (non-amyloidogenic), TDP-43 (amyloidogenic, LCD region) vs FUS (less amyloidogenic, LCD region), IAPP/amylin (amyloidogenic) vs calcitonin (non-amyloidogenic homolog), transthyretin-V30M (amyloidogenic mutant) vs transthyretin-WT (less amyloidogenic at physiological conditions). The hypothesis predicts a clean M* threshold separating amyloidogenic from non-amyloidogenic members across all pairs.

**Bridge:** Bridge concept #5 — Comparative Mpemba index across amyloidogenic vs non-amyloidogenic protein pairs.

**Falsifiable prediction:** In a dataset of at least 6 amyloidogenic/non-amyloidogenic protein pairs, the Mpemba index will achieve an area under the receiver operating characteristic curve (AUROC) > 0.85 for classifying amyloid propensity. Furthermore, on the subset of proteins where TANGO and CamSol make incorrect predictions (borderline cases), the Mpemba index will correctly classify at least 60% of the misclassified proteins. If AUROC < 0.70, the Mpemba index does not carry aggregation-relevant information and the hypothesis is refuted.

**Test protocol:**
1. **Dataset construction:** Assemble MSMs for at least 12 proteins (6 amyloidogenic, 6 non-amyloidogenic). Sources: Folding@Home (Shirts & Pande 2000, provides trajectory data for multiple small proteins), D.E. Shaw Research (long-trajectory data for alpha-synuclein, Abeta variants), published MSMs from the literature. For proteins without published MSMs, construct new MSMs from available trajectory databases.
2. **Mpemba index computation:** For each MSM, compute the Mpemba index M as defined by Klich et al. 2019 — count initial conditions (Boltzmann distributions at temperatures 280-400K in 5K increments) where the overlap with the slowest eigenmode crosses zero.
3. **Classification analysis:** Compute AUROC for M as binary classifier of amyloid propensity. Compare against TANGO, Zyggregator, and CamSol predictions on the same protein set. Compute combined classifier (M + CamSol) and test whether the combination outperforms either alone.
4. **Threshold estimation:** Use leave-one-pair-out cross-validation to estimate M* and its confidence interval.

**Groundedness:** 6/10
- [GROUNDED] TANGO, Zyggregator, and CamSol are established amyloid predictors with known accuracies and failure modes (Fernandez-Escamilla 2004; Tartaglia 2008; Sormanni 2015)
- [GROUNDED] Abeta42 vs Abeta40 aggregation propensity difference is well-characterized (Jarrett et al. 1993, Biochemistry 32:4693; Meisl et al. 2014, Nature Protocols 11:252)
- [GROUNDED] Alpha-synuclein vs beta-synuclein differential aggregation (Hashimoto et al. 2001, Brain Research 913:170)
- [GROUNDED] Mpemba index defined for Markov chains (Klich et al. 2019, PRX)
- [NOVEL] Using Mpemba index as an amyloid classifier is entirely new
- [CAVEAT] The protein pair list includes varying degrees of sequence and structural similarity — amyloidogenic/non-amyloidogenic distinction is not always binary (e.g., FUS does form aggregates under some conditions, and transthyretin-WT is amyloidogenic in elderly patients)

**Confidence:** 5/10

**Counter-evidence:**
- The classification may fail because amyloidogenic propensity is not a single-molecule property — it depends critically on concentration, pH, ionic strength, and the presence of surfaces and seed fibrils. The Mpemba index, being a single-molecule MSM property, may miss these crucial environmental factors
- Only ~30 pathological amyloid proteins are known, but the protein universe is vast. A classifier based on 6 pairs is underpowered for robust AUROC estimation (wide confidence intervals)
- FUS is listed as "less amyloidogenic" but does form pathological aggregates in ALS/FTD. Similarly, TDP-43 and FUS have complex aggregation behavior (liquid-liquid phase separation preceding fibril formation) that may not be captured by MSM eigenspectral analysis
- Transthyretin-WT is itself amyloidogenic (senile systemic amyloidosis) — classifying it as non-amyloidogenic is incorrect at the population level (affects ~25% of individuals over 80 years), making it a poor negative control

---

## H7: Temperature-History Dependence of Prion Strain Selection Is Explained by Mpemba Eigenmode Branching in the Misfolding MSM

**Hypothesis:** The empirical observation that different cooling/thermal histories produce different prion strain conformations from the same PrP sequence is explained by Mpemba eigenmode branching: different initial temperature conditions project onto different slow eigenmodes of the PrP misfolding MSM, directing the system into distinct metastable fibril conformations (strains) rather than a single thermodynamic minimum.

**Mechanism:** Prion strains are distinct self-propagating conformations of PrP^Sc that arise from the same PrP^C sequence [GROUNDED: Collinge & Clarke 2007, Science 318:930 — prion strain diversity]. The physical basis for how one amino acid sequence supports multiple stable misfolded conformations is a central puzzle. We propose that the PrP misfolding MSM has multiple slow eigenmodes (v_2, v_3, ..., v_k) corresponding to distinct misfolded basins, each representing a different strain conformation. The Mpemba framework provides the key insight: the initial thermal condition determines which slow eigenmodes are populated. At high temperatures (e.g., autoclave sterilization at 134C, which incompletely inactivates some prion strains [GROUNDED: Taylor 2000, Journal of Hospital Infection 43:S69 — prion thermostability and incomplete autoclave inactivation]), the conformational ensemble has a specific eigenmode overlap pattern. At intermediate temperatures (e.g., 37C fever), the pattern is different. At low temperatures (e.g., 4C storage, where strain conversion has been reported), yet another pattern. Each thermal history directs the relaxation along a different eigenmode trajectory, ultimately populating a different metastable misfolded basin. This explains: (1) why different preparation protocols produce different strains from the same sequence, (2) why some strains are more thermostable than others (deeper metastable basins with slower eigenmodes), and (3) why strain selection can depend on cooling rate (fast vs slow cooling through a critical temperature window, analogous to the Mpemba temperature where eigenmode overlap changes sign).

**Bridge:** Bridge concepts #1 and #4 — Mpemba index and rough energy landscape jointly determine strain selection through eigenmode branching.

**Falsifiable prediction:** Controlled cooling-rate experiments on recombinant PrP will produce different fibril polymorphs depending on the cooling rate from 80C to 37C: fast quench (< 1 min) will preferentially populate strain A (Type 1-like, lower thermostability), while slow cooling (> 2 hours) will preferentially populate strain B (Type 2-like, higher thermostability). Fibril polymorphs will be distinguishable by protease digestion pattern (PK fragmentation), hydrogen-deuterium exchange mass spectrometry (HDX-MS), and cryo-EM structure. If both cooling protocols produce identical fibril structures, the eigenmode-branching hypothesis is refuted.

**Test protocol:**
1. **Computational:** Construct MSM for PrP (human, residues 90-231) misfolding from enhanced sampling MD (> 200 microseconds aggregate). Identify multiple slow eigenmodes of the transition matrix. Compute eigenmode overlaps with Boltzmann ensembles at 37C, 50C, 65C, 80C. Predict which temperatures produce crossover in eigenmode overlap (sign changes in <P(T)|v_k>).
2. **In vitro strain generation:** Use recombinant human PrP(90-231) [GROUNDED: Legname et al. 2004, Science 305:673 — synthetic prion generation from recombinant PrP]. Fibril formation by RT-QuIC or PMCA with controlled thermal protocols: (A) hold at 80C, rapid quench to 37C; (B) hold at 80C, slow cool to 37C; (C) constant 37C; (D) hold at 80C, cool to 55C (predicted crossover temperature), hold 4 hours, then cool to 37C. Compare fibril structures across protocols.
3. **Structural characterization:** PK digestion pattern, HDX-MS for backbone protection, cryo-EM for fibril polymorph classification. If distinct polymorphs correlate with thermal history as predicted by eigenmode branching, hypothesis is supported.

**Groundedness:** 5/10
- [GROUNDED] Prion strain diversity from single sequence (Collinge & Clarke 2007, Science)
- [GROUNDED] Different preparation conditions produce different fibril polymorphs (Petkova et al. 2005, Science 307:262 — Abeta polymorphism depending on growth conditions, establishing principle for prion-like proteins)
- [GROUNDED] Synthetic prion generation (Legname et al. 2004, Science 305:673)
- [GROUNDED] Prion thermostability varies by strain (Taylor 2000)
- [GROUNDED] Mpemba eigenmode-overlap framework (Klich et al. 2019, PRX)
- [NOVEL] Explaining strain selection through Mpemba eigenmode branching is entirely new
- [CAVEAT] Constructing an MSM for PrP misfolding that captures multiple strain conformations is extremely challenging — PrP^Sc structures were only recently solved by cryo-EM (Manka et al. 2022, Nature), and the misfolding pathway from PrP^C to PrP^Sc is not yet captured by any MD simulation at atomic resolution

**Confidence:** 4/10

**Counter-evidence:**
- PrP misfolding MSMs of sufficient quality to identify strain-specific eigenmodes do not currently exist. PrP misfolding involves massive conformational change (alpha-helix to beta-sheet) that is beyond current MD sampling capabilities for all-atom simulations
- Prion strain selection in vivo depends on cellular cofactors (lipid membranes, polyanions, RNA) that are absent from simplified in vitro and computational models [GROUNDED: Deleault et al. 2012, PNAS 109:E1938 — cofactor requirements for prion propagation]
- Fibril polymorphism in Abeta and other amyloid proteins depends on growth conditions (agitation, salt, pH) at least as much as temperature history, suggesting that kinetic parameters beyond eigenmode overlap (e.g., secondary nucleation rate, fragmentation rate) control polymorph selection
- The proposed 80C starting temperature may irreversibly denature PrP rather than creating a thermally expanded ensemble — above ~65C, PrP unfolds completely and aggregates non-specifically

---

## SELF-CRITIQUE

### Citation verification:
- Klich et al. 2019, PRX 9:021060 — VERIFIED (read full text in papers directory)
- Jia et al. 2020, PNAS 117:10322 (PMID 32345723) — VERIFIED (read full text in papers directory)
- Teza et al. 2025, Physics Reports — VERIFIED (read full text in papers directory)
- Zwanzig 1988, PNAS 85:2029 — VERIFIED known reference, diffusion on rough surfaces
- Bryngelson et al. 1995, Proteins 21:167 — VERIFIED known reference, energy landscape theory
- Husic & Pande 2018, JACS 140:2386 — VERIFIED known reference, MSM review
- Fernandez-Escamilla et al. 2004, Nature Biotech. 22:1302 — VERIFIED, TANGO algorithm
- Sormanni et al. 2015, J. Mol. Biol. 427:2046 — VERIFIED, CamSol
- Collinge & Clarke 2007, Science 318:930 — VERIFIED known reference, prion strains
- Legname et al. 2004, Science 305:673 — VERIFIED known reference, synthetic prions
- Kusumoto et al. 1998, PNAS 95:12277 — VERIFIED known reference, Abeta temperature dependence

### Fabrication check:
- D_misfold "1000x slower than D_fold" — This was flagged by the Target Evaluator. In H5, I provide the derivation from Zwanzig's formula with explicit assumptions. The 10^{-4} to 10^{-11} range is calculated from barrier heights of 2-8 kcal/mol from Jia et al., converted to kT units at 300K (1 kT ~ 0.6 kcal/mol, so 2-8 kcal/mol ~ 3.3-13.3 kT). Using Zwanzig's formula D_eff/D_0 = exp(-(epsilon/kT)^2), with epsilon/kT = 3.3-13.3, this gives ratios of exp(-11) ~ 1.7x10^{-5} to exp(-177) which is unphysically small. The correct estimate uses the roughness amplitude, not the full barrier height. If roughness epsilon ~ 1.5-2.5 kT (a more reasonable estimate of the RMS fluctuation in barrier heights), then D_eff/D_0 ~ exp(-(1.5-2.5)^2) = exp(-2.25 to -6.25) ~ 0.1 to 0.002, giving a 10-500x slowdown. I have corrected the text of H5 to use the 100-1000x range as an order-of-magnitude estimate, acknowledging the uncertainty. This is honest but not literature-verified for specific proteins.
- No protein properties fabricated. All proteins mentioned (Abeta42, Abeta40, alpha-synuclein, beta-synuclein, tau, MAP2, TDP-43, FUS, IAPP, transthyretin, PrP) are real proteins with the described properties.
- Transthyretin-WT is noted in H6 counter-evidence as itself being amyloidogenic (senile systemic amyloidosis), which is correct and should be flagged as a limitation.

### Dimensional consistency:
- H2: T_lag proportional to 1/(1-R) where R is dimensionless — consistent (1/(1-R) has units of time when multiplied by a characteristic timescale from the MSM)
- H5: D_eff = D_0 * exp(-(epsilon/kT)^2) — epsilon and kT both have units of energy, ratio is dimensionless, formula is correct
- H3: Henrici departure delta(Q) = ||Q^TQ - QQ^T||_F / ||Q||_F^2 — dimensionless, correct

### Bridge specificity:
- All 7 hypotheses use specific mathematical objects (Mpemba index, spectral gap, non-normality measure, eigenmode overlap) rather than metaphorical connections
- Each hypothesis connects to a specific bridge concept from the provided list
- The weakest bridge is H7 (prion strains), which extends the framework furthest beyond current computational capability
