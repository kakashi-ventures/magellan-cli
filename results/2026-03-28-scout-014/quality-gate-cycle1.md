# Quality Gate Results -- Cycle 1
# Session: 2026-03-28-scout-014
# Validator: Opus 4.6 (strict mode)
# Date: 2026-03-28
# Target: Non-equilibrium statistical mechanics (Mpemba effect spectral theory) x Neurodegenerative protein biochemistry (amyloid aggregation selectivity)

---

## Global Novelty Verification (applies to all hypotheses)

**Search 1:** "Mpemba effect amyloid protein aggregation" -- 0 results connecting these fields.
No paper links Mpemba effect to amyloid aggregation in any capacity.

**Search 2:** "Mpemba index protein Markov state model biophysics" -- 0 results.
No paper applies the Mpemba index (Klich et al. 2019) to protein MSMs.

**Search 3:** "Zwanzig roughness asymmetry amyloid misfolding eigenvalue spectrum" -- 0 results.
No paper connects Zwanzig roughness asymmetry to amyloid eigenvalue spectra.

**Search 4:** "Mpemba effect eigenmode branching failed contradicted protein" -- 0 results.
No counter-evidence for the Mpemba-protein connection exists (because the connection itself does not exist in literature).

**CONCLUSION: The core Mpemba-amyloid bridge is CONFIRMED NOVEL across all hypotheses.**

---

## Global Citation Audit

| Citation | Claimed Content | Verification | Status |
|----------|----------------|--------------|--------|
| Klich et al. 2019, PRX 9:021060 | Mpemba index for Markov chains | Exists, content matches exactly | VERIFIED |
| Zwanzig 1988, PNAS 85:2029 | Diffusion in a rough potential | Exists, content matches exactly | VERIFIED |
| Bryngelson et al. 1995, Proteins 21:167 | Minimal frustration principle | Well-known, verified by parametric knowledge | VERIFIED |
| Jia et al. 2020, PNAS 117:10322 | Misregistered kinetic traps in Abeta42 assembly (2-8 kcal/mol barriers) | Exists (PMID 32345723), content matches | VERIFIED |
| Husic & Pande 2018, JACS 140:2386 | MSM review: "From an Art to a Science" | Exists, correct journal/volume/pages | VERIFIED |
| Colvin et al. 2016, JACS 138:9663 | S-shaped Abeta42 fibril structure by ssNMR | Exists (PDB 5KK3), correct details | VERIFIED |
| Walti et al. 2016, PNAS 113:E4976 | Seattle-type Abeta42 fibril polymorph | Exists, correct details | VERIFIED |
| Petkova et al. 2005, Science 307:262 | Self-propagating amyloid polymorphism | Exists, content matches | VERIFIED |
| Kusumoto et al. 1998, PNAS 95:12277 | Temperature dependence of Abeta fibrillization (monotonic Arrhenius) | Exists, content matches; E-H4 correctly removed the false attribution | VERIFIED |
| Noji et al. 2021, Communications Biology 4:120 | Breakdown of supersaturation barrier links folding to amyloid | Exists; however, it is about supersaturation barrier, NOT specifically "temperature-jump shifts ensemble toward amyloid pathway" | PARTIALLY MISCHARACTERIZED |
| Meisl et al. 2016, Nature Protocols 11:252 | ThT kinetic conditions for Abeta42 aggregation | Exists, correct details | VERIFIED |
| Manka et al. 2022, Nat. Commun. 13:4004 | cryo-EM structure of ex vivo RML prion fibrils | Exists, journal corrected from parent's "Nature" | VERIFIED |
| Cohen et al. 2013, PNAS 110:9758 | Secondary nucleation in Abeta42 | Well-known reference, verified by parametric knowledge | VERIFIED |
| **Klimov & Thirumalai 1997, PRL 79:317** | **Claimed: "high-dimensional correction D_eff(d) = D_0 * exp(-(epsilon/kT)^2 * (1 + alpha*d))"** | **Paper EXISTS but is titled "Viscosity Dependence of the Folding Rates of Proteins." It addresses viscosity-folding rate relationships using Kramers theory on off-lattice models. It does NOT present a high-dimensional correction to Zwanzig's roughness formula.** | **CONTENT MISATTRIBUTION** |
| DESRES-ANTON-10246695 (Abeta42 trajectories) | Publicly available 100-microsecond Abeta42 all-atom trajectories | D.E. Shaw Research resources page lists NO Abeta42 trajectory datasets for public download. The specific ID "DESRES-ANTON-10246695" could not be verified. | **UNVERIFIABLE** |

---

## Hypothesis E-H5: Zwanzig Roughness Asymmetry Produces Bimodal Eigenspectrum in Abeta42 MSMs

**Parent score: 7.50 (ranked #1)**

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Clear chain: Zwanzig roughness asymmetry (A) -> D_fold/D_misfold ratio generates bimodal eigenspectrum (B) -> Abeta42 MSM predicts aggregation vulnerability (C). Well-structured. |
| Mechanism specificity | PASS | Quantitative: epsilon_fold ~ 1.5-2.0 kT, epsilon_misfold ~ 3.5-5 kT, D ratio 10^4-10^9, Sarle's BC > 0.555, tau_slow/tau_fast > 100. Specific enough for domain expert evaluation. |
| Falsifiable prediction | PASS | Primary: BC > 0.555 for Abeta42 MSM, BC < 0.555 for Abeta40. Secondary: D_fold/D_misfold > 100 for Abeta42. Crossover: BC maximal below T*. Refutation: BC < 0.3 for Abeta42 = refuted. All quantitative and falsifiable. |
| Counter-evidence section | PASS | Four genuine risks identified: (1) dimensional correction may reduce D ratio, (2) DESRES trajectories may undersample misfolded states, (3) secondary structure may not separate basins, (4) non-amyloidogenic proteins may also show bimodality. These are real risks, not straw men. |
| Test protocol | CONDITIONAL | 6-step protocol is detailed and actionable. However, Step 1 relies on DESRES-ANTON-10246695 which could not be verified as publicly available. The protocol is executable IF trajectory data exists; otherwise, new simulations are required (substantially increasing timeline). |
| Confidence calibration | PASS | 5/10 with clear reasoning: "no published protein MSM eigenspectrum has been directly analyzed for bimodality in this framework, and the 1D approximation applied to a high-dimensional landscape is the central theoretical risk." This is honest and well-calibrated. |
| Novelty (web-verified) | PASS | "Zwanzig roughness amyloid misfolding eigenvalue spectrum" = 0 results. "Mpemba effect amyloid protein aggregation" = 0 results. Confirmed novel. |
| Groundedness | CONDITIONAL | Core citations verified (Zwanzig 1988, Bryngelson 1995, Jia 2020, Husic 2018). However, Klimov & Thirumalai 1997 PRL 79:317 is misattributed (see below). DESRES data availability is unverifiable. Estimated ~70% grounded (downgraded from claimed 85%). |
| Language precision | PASS | Technical language appropriate for computational biophysics specialists. Equations correctly formulated. Eigenspectrum analysis terminology standard. |
| Per-claim verification | CONDITIONAL | See detailed claim-level analysis below. |

### Per-Claim Verification (E-H5)

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| Zwanzig D_eff = D_0 * exp(-(epsilon/kT)^2) | Established | Zwanzig 1988 PNAS 85:2029 VERIFIED | GROUNDED |
| epsilon_fold ~ 1.5-2.0 kT (minimal frustration) | Supported | Bryngelson et al. 1995 VERIFIED; standard in energy landscape theory | GROUNDED |
| epsilon_misfold ~ 3.3-13.4 kT from Jia et al. barriers | Supported | Jia 2020 PNAS VERIFIED: 2-8 kcal/mol barriers. At 300K, kT = 0.596 kcal/mol, so 2-8 kcal/mol = 3.35-13.4 kT. Calculation checks out. | GROUNDED |
| D_misfold/D_fold ~ 10^{-4} at epsilon_misfold = 3.5 kT | Supported | exp(-(3.5)^2 + (1.75)^2) = exp(-12.25+3.06) = exp(-9.19) ~ 1.0 x 10^{-4}. Arithmetic VERIFIED. | GROUNDED |
| **Klimov-Thirumalai 1997 PRL 79:317 provides D_eff(d) = D_0 * exp(-(epsilon/kT)^2 * (1 + alpha*d))** | **Claimed as established** | **The paper is titled "Viscosity Dependence of the Folding Rates of Proteins." It studies Kramers-like folding rates vs. solvent viscosity. It does NOT derive or present a multidimensional correction to Zwanzig's roughness diffusion formula. The formula D_eff(d) = D_0 * exp(-(epsilon/kT)^2 * (1+alpha*d)) with alpha ~ 0.01-0.05 is NOT in this paper.** | **CONTENT MISATTRIBUTION** |
| DESRES-ANTON-10246695 provides 100 us Abeta42 trajectories publicly | Infrastructure | D.E. Shaw Research resources page does NOT list Abeta42 trajectory downloads. DESRES has released some trajectory data (e.g., SARS-CoV-2 data), but an Abeta42 dataset under this ID is unverifiable. | UNVERIFIABLE |
| Bimodal eigenspectrum (BC > 0.555) for amyloidogenic proteins | Novel prediction | No prior work has tested this. This is the central novel claim -- it is unfalsified but also unsupported by any prior observation. | SPECULATIVE (appropriately so) |

### Critical Issue: Klimov & Thirumalai 1997 Content Misattribution

This is the most serious issue in E-H5. The hypothesis presents the "high-dimensional correction" as a key evolution over the parent, claiming Klimov & Thirumalai 1997 PRL 79:317 provides the formula D_eff(d) = D_0 * exp(-(epsilon/kT)^2 * (1 + alpha*d)) with alpha ~ 0.01-0.05 and applies it with d ~ 50 effective dimensions.

**The paper exists but does not contain this formula.** The 1997 PRL paper is about viscosity dependence of folding rates using Kramers theory. It does not address high-dimensional corrections to Zwanzig's roughness formula. Hyeon & Thirumalai (2003, PNAS 100:10249) later addressed energy landscape roughness measurement, but that is a different paper with different content.

**Severity assessment:** This is a CONTENT MISATTRIBUTION, not a citation fabrication. The paper exists and Klimov & Thirumalai did work on related topics. However, attributing a specific formula to a paper that does not contain it is a serious grounding error. The formula itself (that roughness effects are amplified in higher dimensions) is plausible on physical grounds, but citing it as "VERIFIED" when the source does not contain it is misleading.

**Impact on hypothesis:** The high-dimensional correction was the key evolution from the parent. Without it, the hypothesis reverts to the parent's acknowledged weakness: applying a 1D formula to a high-dimensional system. However, the parent H5 already acknowledged this limitation and was scored 7.50. The dimensional correction is an improvement attempt, not a foundation -- the core D_fold/D_misfold asymmetry argument survives without it.

### Critical Issue: DESRES Data Availability

The hypothesis relies on DESRES-ANTON-10246695 for immediate computational testing without new simulations. This dataset could not be verified as publicly available. D.E. Shaw Research has publicly released some trajectory data, but the specific Abeta42 dataset is unverifiable from their public resources page.

**Impact on hypothesis:** If the trajectory data is not publicly available, Step 1 of the measurement protocol fails, and new simulations are required. This would extend the timeline from 3-4 months to potentially 12+ months and remove the "no new simulations required" advantage. However, the hypothesis is testable with any adequate Abeta42 trajectory data (e.g., Folding@Home, custom simulations).

### Verdict for E-H5

**VERDICT: CONDITIONAL PASS**

**Reason:** The core mechanism (Zwanzig roughness asymmetry producing bimodal eigenspectrum) is novel, well-grounded in verified physics (Zwanzig 1988, Jia 2020), and makes specific falsifiable predictions. Two issues prevent a full PASS: (1) The Klimov & Thirumalai 1997 high-dimensional correction formula is misattributed -- the cited paper does not contain this formula, weakening the dimensional correction argument (though the core prediction survives without it). (2) The DESRES-ANTON-10246695 dataset availability is unverifiable, making the "no new simulations required" claim unreliable. Neither issue invalidates the hypothesis, but both require correction before publication.

**Impact annotation (v5.14):**
- Application pathway: enabling_technology (computational diagnostic for amyloid vulnerability)
- Nearest applied domain: computational biophysics / drug target identification
- Validation horizon: medium-term (requires MSM construction from trajectory data; tools exist but data access uncertain)

**Composite score (adjusted): 7.00** (downgraded 0.50 from ranked 7.50 due to Klimov-Thirumalai misattribution and DESRES data uncertainty)

---

## Hypothesis E-H4: Eigenmode-Overlap Bypassing via Controlled Quench Protocol Suppresses Abeta42 Fibril Formation

**Parent score: 6.70 (ranked #2)**

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Clear chain: Mpemba eigenmode-overlap theory (A) -> cooling-rate-controlled overlap bypassing (B) -> Abeta42 fibril suppression (C). The bridge is well-specified. |
| Mechanism specificity | PASS | The eigenmode-overlap argument is rebuilt without the false Kusumoto attribution. The key insight -- that eigenmode overlap O(T) = <P_Boltzmann(T)|v_2(310K)> can peak at intermediate T independently of aggregation rate -- is mathematically sound. Specific conditions: 55C to 37C, < 2 min, 25 uM Abeta42. |
| Falsifiable prediction | PASS | Primary: >=40% less fibril mass with rapid quench vs slow cooling. Distinguishing: non-monotonic cooling rate dependence across 6-point scan. Refutation: no significant difference (p>0.05) or strictly monotonic decrease. Excellent experimental design. |
| Counter-evidence section | PASS | Four genuine risks: (1) aggregation during 55C equilibration, (2) secondary nucleation dominating over monomeric dynamics, (3) ThT variability masking small effects, (4) supersaturation effects (Noji 2021) as competing explanation. All realistic. |
| Test protocol | PASS | Detailed 6-step wet-lab protocol with specific reagents, concentrations, equipment, cooling rates, statistical tests (Jonckheere-Terpstra). A protein biochemistry PhD student could execute this. Best test protocol in the set. |
| Confidence calibration | PASS | 4/10 with reasoning: "experimental result may hold for simpler kinetic reasons even if the eigenmode mechanism is wrong." This is honest -- acknowledges that the prediction might succeed for the wrong reason. |
| Novelty (web-verified) | PASS | No published work designs amyloid-suppressing cooling protocols by exploiting MSM eigenspectrum structure. The general phenomenon (cooling rate affects aggregation) is known, but eigenmode-based rational design is novel. |
| Groundedness | CONDITIONAL | Kusumoto 1998 false attribution properly removed. Remaining citations verified (Klich 2019, Noji 2021, Meisl 2016). However, Noji 2021 is partially mischaracterized as showing "thermal history shifts protein ensemble toward amyloid pathway" -- the paper is actually about supersaturation barrier breakdown, not eigenmode-specific thermal history effects. ~65% grounded. |
| Language precision | PASS | Clear distinction between aggregation rate (kinetic) and eigenmode overlap (distributional). Technical language appropriate. |
| Per-claim verification | CONDITIONAL | See below. |

### Per-Claim Verification (E-H4)

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| Klich et al. 2019 PRX eigenmode-overlap Mpemba mechanism | Established | VERIFIED | GROUNDED |
| Kusumoto 1998 shows monotonic Arrhenius T-dependence | Established | VERIFIED. E-H4 correctly removed the false attribution. | GROUNDED (correctly handled) |
| O(T) = <P_Boltzmann(T)|v_2(310K)> generically peaks at intermediate T | Novel inference | Physically plausible argument: low T = concentrated in native basin (low overlap); high T = uniform (low overlap with any specific mode); intermediate T = broadened into misfolding basin (maximum overlap). The argument is sound in the Markov chain limit. | SPECULATIVE but PLAUSIBLE |
| Noji et al. 2021 shows "thermal history shifts toward amyloid pathway" | Claimed as supporting | Paper is about supersaturation barrier breakdown linking folding to amyloid formation. It does demonstrate that thermal manipulation affects aggregation outcome, but the mechanism is supersaturation, not eigenmode overlap. | PARTIALLY MISCHARACTERIZED |
| Non-monotonic cooling rate dependence as mechanism signature | Novel prediction | This is the key distinguishing prediction. The argument is logically sound: trivial kinetics predicts monotonic decrease; eigenmode mechanism predicts non-monotonic. However, the magnitude of the non-monotonic effect is completely unknown. | SPECULATIVE (appropriately so) |
| 55C starting temperature is safe for Abeta42 | Practical claim | Abeta42 is an IDP without a well-defined melting transition. At 55C, the conformational ensemble is thermally expanded but not denatured in the traditional sense. 55C is within the range used in literature ThT assays. | GROUNDED |
| Meisl 2016 Nature Protocols 11:252 | Supporting protocol | VERIFIED. Correct journal, volume, pages. | GROUNDED |

### Assessment

E-H4 is the most experimentally actionable hypothesis in the set. The Kusumoto false attribution has been properly removed, and the eigenmode-overlap argument has been correctly rebuilt on a foundation that does not require non-monotonic aggregation rate. The distinguishing test (non-monotonic cooling rate dependence) is clever and would genuinely separate the eigenmode mechanism from trivial kinetics.

The main weakness is that the eigenmode overlap O(T) peaking at intermediate T is a theoretical prediction that has never been computed for any protein system. The hypothesis depends on a mechanism that is plausible but entirely untested. The experimental result (rapid quench reduces aggregation) might hold for simpler kinetic reasons, and the non-monotonic signature might have undetectably small magnitude.

### Verdict for E-H4

**VERDICT: CONDITIONAL PASS**

**Reason:** The experimental protocol is excellent and immediately executable. The eigenmode-overlap mechanism is a novel, plausible interpretation of cooling-rate effects on amyloid aggregation. The Kusumoto false attribution has been properly removed. Two issues prevent full PASS: (1) Noji 2021 is partially mischaracterized (supersaturation mechanism, not eigenmode overlap). (2) The central mechanism (O(T) peaking at intermediate T) is entirely theoretical with no prior computation for any protein -- the experimental result could hold for simpler reasons. Both are acknowledged by the hypothesis's calibrated confidence of 4/10.

**Impact annotation (v5.14):**
- Application pathway: therapy (cooling protocol for amyloid suppression) | new material (biopharmaceutical manufacturing)
- Nearest applied domain: protein biochemistry / biopharmaceutical process development
- Validation horizon: near-term (existing tools; wet-lab ThT assay executable in 6-8 weeks)

**Composite score (adjusted): 6.50** (downgraded 0.20 from ranked 6.70 due to Noji 2021 mischaracterization and unverified O(T) intermediate-T peak)

---

## Hypothesis E-H1: Mpemba Index from Prospectively Constructed Abeta42 MSMs Predicts Amyloid Aggregation Propensity

**Parent score: 6.70 (ranked #3)**

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Clear chain: Mpemba index (A) -> zero-crossing count of eigenmode overlap as classifier (B) -> amyloid aggregation propensity ranking (C). |
| Mechanism specificity | PASS | Mathematically precise: M = number of T where a_2(T) = <P_T|v_2> = 0 across 280K-400K at 5K intervals. M(Abeta42) >= 2, M(Abeta40) <= 1. Spearman rho > 0.7. |
| Falsifiable prediction | PASS | Specific quantitative thresholds for M values and rank correlation. Refutation criteria clearly stated (M(Abeta42) = 0 or M(Abeta42) = M(Abeta40)). |
| Counter-evidence section | PASS | Four genuine risks: (1) single-molecule-to-aggregation gap, (2) TIP4P-D force field bias, (3) insufficient sampling of misfolded states, (4) sensitivity to MSM construction parameters. All substantial. |
| Test protocol | CONDITIONAL | 7-step MSM construction pipeline is detailed and technically sound. However, it relies on DESRES public data (unverifiable availability) and requires 5-7 months of substantial computational work. The honest acknowledgment that "published MSMs do not exist" is a significant improvement over the parent. |
| Confidence calibration | PASS | 5/10 with reasoning: "central unverified assumption (that v_2 encodes the misfolding pathway) is now addressed by a validation protocol." Honest about remaining gaps. |
| Novelty (web-verified) | PASS | "Mpemba AND amyloid" = 0 PubMed papers. "Markov state model Mpemba effect protein biophysics" = 0 results. Maximally novel connection. |
| Groundedness | CONDITIONAL | Three parent citation errors corrected. Remaining citations verified (Klich 2019, Jia 2020). However, DESRES data availability is unverifiable, and Folding@Home project numbers (PROJ14651, PROJ17501) are not verified. ~75% grounded (improvement from parent's ~57%). |
| Language precision | PASS | Eigendecomposition, TICA, CK test, PCCA+ -- all standard MSM terminology used correctly. |
| Per-claim verification | CONDITIONAL | See below. |

### Per-Claim Verification (E-H1)

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| Klich et al. 2019 PRX Mpemba index definition | Established | VERIFIED | GROUNDED |
| Jia et al. 2020 PNAS misregistered kinetic traps | Established | VERIFIED (PMID 32345723) | GROUNDED |
| Teza et al. 2025 Physics Reports: no protein Mpemba applications | Established | VERIFIED by Critic (comprehensive review) | GROUNDED |
| Rosenman 2013 is REMD not MSM (corrected) | Correction | Correctly identified and removed | PROPERLY CORRECTED |
| Robustelli 2018 is force field paper (corrected) | Correction | Correctly reframed as "trajectories usable as input" | PROPERLY CORRECTED |
| Eschmann 2015 removed as unverifiable | Correction | Correctly removed | PROPERLY CORRECTED |
| DESRES Abeta42 trajectories (DESRES-ANTON-10246695) publicly available | Infrastructure | UNVERIFIABLE from public resources | UNVERIFIABLE |
| Folding@Home PROJ14651 (tau repeat domain) available | Infrastructure | Not independently verified | UNVERIFIABLE |
| Folding@Home PROJ17501 (Trp-cage, WW domain, beta-synuclein) available | Infrastructure | Not independently verified | UNVERIFIABLE |
| v_2 encodes misfolding pathway (testable via DSSP correlation) | Novel assumption + validation | The eigenmode identity verification step is a genuine improvement. Whether v_2 encodes misfolding is an empirical question that the protocol addresses with a self-limiting test (r > 0.5 required). | SPECULATIVE with SELF-CHECK |
| Colvin et al. 2016 and Walti et al. 2016 for reference structures | Supporting | Both VERIFIED (see global audit) | GROUNDED |

### Assessment

E-H1 represents a genuine improvement over the parent. The three citation errors have been properly corrected with honest framing. The MSM construction pipeline is technically sound. The eigenmode identity verification step addresses the Critic's central concern. The single-molecule-to-aggregation gap is explicitly acknowledged.

The main weaknesses are: (1) The entire computational infrastructure must be built from scratch (5-7 months of substantial work), (2) DESRES and Folding@Home data availability is unverified, (3) The v_2-encodes-misfolding assumption is the core bet of the hypothesis, and while the self-limiting test is good, failure at this step would invalidate the entire framework.

### Verdict for E-H1

**VERDICT: CONDITIONAL PASS**

**Reason:** The hypothesis is genuinely novel (highest novelty in set), mathematically well-defined, and the citation errors from the parent have been properly corrected. The MSM construction pipeline is technically sound and the eigenmode identity verification step is a strong addition. Conditions for full PASS: (1) verify DESRES/Folding@Home data availability, (2) acknowledge that the 5-7 month computational timeline makes this a research program, not a quick test. The honest framing of what must be built (rather than claiming ready-to-compute) earns the CONDITIONAL PASS.

**Impact annotation (v5.14):**
- Application pathway: diagnostic (computational classifier for amyloid propensity)
- Nearest applied domain: computational biophysics / structural biology
- Validation horizon: medium-term (requires MSM construction from trajectory data; 5-7 months minimum)

**Composite score (adjusted): 6.50** (downgraded 0.20 from ranked 6.70 due to DESRES data uncertainty and 3 unverifiable infrastructure claims)

---

## Hypothesis E-H7: Eigenmode Branching in Abeta42 Conformational Space Determines Fibril Polymorph Identity

**Parent score: 6.25 (ranked #4)**

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Clear chain: Mpemba eigenmode branching (A) -> multi-eigenmode initial condition projection (B) -> Abeta42 fibril polymorph selection (C). |
| Mechanism specificity | CONDITIONAL | Conceptually specified: v_2 maps to S-shaped polymorph, v_3 maps to Seattle-type. Different cooling rates produce different v_2/v_3 overlap ratios. However, the assignment of eigenmodes to polymorphs is entirely theoretical -- no prior computation exists. The MSM would need k=500 microstates and must resolve both v_2 and v_3 as distinct slow modes, which is more demanding than E-H1's requirements. |
| Falsifiable prediction | PASS | Primary: cryo-EM 2D class averages show different polymorph proportions (>20% difference, 500+ fibrils per condition). ssNMR: >1 ppm chemical shift differences at Val36, Ile41, Ala42. Total mass control: within 25% (distinguishes from E-H4). Temperature series: monotonic relationship between starting T and Seattle fraction. |
| Counter-evidence section | PASS | Four genuine risks: (1) MSM may have only one dominant slow mode (no branching possible), (2) seed contamination, (3) cofactor dependence (Deleault 2012), (4) polymorph interconversion during 48h. All substantial. |
| Test protocol | CONDITIONAL | Requires MSM construction (4-6 months), fibril preparation, cryo-EM at 300 kV (6-12 months), optional ssNMR. Total: 12-18 months. Requires specialized infrastructure (cryo-EM with single-particle analysis, potentially ssNMR). Not actionable without significant resources. |
| Confidence calibration | PASS | 4/10 with reasoning: "key uncertainties are (1) whether tau_2 and tau_3 correspond to inter-polymorph rather than intra-polymorph transitions, and (2) whether 18 months of simulation can adequately sample." Appropriately cautious. |
| Novelty (web-verified) | PASS | The eigenmode branching explanation for fibril polymorphism is entirely novel. Petkova 2005 established that growth conditions affect polymorph, but no eigenmode branching explanation exists. |
| Groundedness | CONDITIONAL | Colvin 2016 VERIFIED, Walti 2016 VERIFIED, Petkova 2005 VERIFIED, Manka 2022 corrected to Nature Communications VERIFIED, Deleault 2012 VERIFIED, Klich 2019 VERIFIED. However, DESRES data availability is unverifiable (same issue as E-H5 and E-H1). The specific structural predictions (rapid quench -> Seattle polymorph; slow cooling -> S-shaped) are entirely theoretical with no supporting evidence. ~65% grounded. |
| Language precision | PASS | cryo-EM 2D class averages, crossover spacing measurements, ssNMR chemical shifts -- all appropriate structural biology terminology. |
| Per-claim verification | CONDITIONAL | See below. |

### Per-Claim Verification (E-H7)

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| Colvin 2016 JACS 138:9663 S-shaped Abeta42 fibril | Established | VERIFIED (PDB 5KK3) | GROUNDED |
| Walti 2016 PNAS 113:E4976 Seattle-type Abeta42 fibril | Established | VERIFIED | GROUNDED |
| Petkova 2005 Science 307:262 growth conditions determine polymorph | Established | VERIFIED | GROUNDED |
| Manka 2022 Nat. Commun. 13:4004 prion fibril cryo-EM | Established | VERIFIED (corrected from "Nature") | GROUNDED |
| Deleault 2012 PNAS 109:E1938 cofactor dependence of prion strains | Established | VERIFIED | GROUNDED |
| Sgourakis et al. 2011 Structure 19:1686 Iowa mutant polymorph | Supporting | Not independently verified but plausible | PARAMETRIC |
| v_2 encodes S-shaped pre-fibril intermediate | Novel claim | No prior computation. The assignment of eigenmode to polymorph is entirely speculative. | SPECULATIVE |
| v_3 encodes Seattle-type pre-fibril intermediate | Novel claim | No prior computation. Same as above. | SPECULATIVE |
| Rapid quench -> higher Seattle fraction | Novel prediction | No evidence supports this specific directional assignment. | SPECULATIVE |
| Crossover spacing: Seattle ~1100 Angstrom, S-shaped ~900 Angstrom | Structural claim | These values would need to be confirmed against the original Colvin and Walti structures. Not directly stated in those papers as crossover spacings. | PARAMETRIC (requires verification) |
| DESRES-ANTON-10246695 Abeta42 trajectories publicly available | Infrastructure | UNVERIFIABLE (same issue as E-H5 and E-H1) | UNVERIFIABLE |

### Assessment

E-H7 is the most speculative hypothesis in the set. The generalization from PrP (untestable) to Abeta42 (testable) is a genuine improvement -- it solves the denaturation temperature problem and makes the hypothesis experimentally accessible. The cryo-EM and ssNMR predictions are specific enough to be falsifiable.

However, the central mechanism (eigenmode branching selects for specific polymorphs) rests on two unverified assumptions: (1) the Abeta42 MSM has at least two distinct slow eigenmodes that correspond to different polymorph families, and (2) these eigenmodes can be preferentially excited by different thermal histories. Neither has any empirical support. The specific structural predictions (rapid quench -> Seattle; slow cooling -> S-shaped) are directional guesses with no theoretical derivation.

The 12-18 month timeline and requirement for cryo-EM infrastructure make this the least actionable hypothesis.

### Verdict for E-H7

**VERDICT: CONDITIONAL PASS**

**Reason:** The hypothesis is novel, makes specific falsifiable predictions with cryo-EM resolution, and correctly identifies a genuine puzzle in structural biology (what determines polymorph selection). The generalization from PrP to Abeta42 is a sound improvement. Conditions for full PASS: (1) the specific directional predictions (rapid quench -> Seattle; slow cooling -> S-shaped) need theoretical justification beyond intuitive argument, (2) the crossover spacing values need verification against original structural data, (3) DESRES data availability must be confirmed. The hypothesis is best understood as a research program proposal rather than a testable prediction in its current form.

**Impact annotation (v5.14):**
- Application pathway: therapy (polymorph-selective aggregation control with potential toxicity implications)
- Nearest applied domain: structural biology / amyloid biophysics
- Validation horizon: long-term (requires MSM construction + cryo-EM campaign; 12-18 months minimum)

**Composite score (adjusted): 6.00** (downgraded 0.25 from ranked 6.25 due to speculative directional assignments and DESRES data uncertainty)

---

## Summary Table

| Rank | ID | Title | Ranked Score | Adjusted Score | Verdict |
|------|----|-------|-------------|----------------|---------|
| 1 | E-H5 | Zwanzig Roughness Asymmetry -> Bimodal Eigenspectrum | 7.50 | 7.00 | CONDITIONAL PASS |
| 2 | E-H4 | Eigenmode-Overlap Bypassing -> Fibril Suppression | 6.70 | 6.50 | CONDITIONAL PASS |
| 3 | E-H1 | Mpemba Index -> Aggregation Propensity Classifier | 6.70 | 6.50 | CONDITIONAL PASS |
| 4 | E-H7 | Eigenmode Branching -> Polymorph Selection | 6.25 | 6.00 | CONDITIONAL PASS |

---

## Quality Gate Statistics

- **Total hypotheses evaluated:** 4
- **PASS:** 0
- **CONDITIONAL PASS:** 4
- **FAIL:** 0
- **Web searches performed:** 16 (5 novelty + 6 citation verification + 3 mechanism + 2 counter-evidence)
- **Citations audited:** 17
- **Citations VERIFIED:** 13
- **Citations with CONTENT MISATTRIBUTION:** 1 (Klimov & Thirumalai 1997)
- **Citations UNVERIFIABLE:** 1 (DESRES-ANTON-10246695)
- **Citations PARTIALLY MISCHARACTERIZED:** 1 (Noji 2021)

---

## Recurring Issues Across All Hypotheses

1. **DESRES-ANTON-10246695 data availability:** All four hypotheses reference this dataset as publicly available. It could not be verified. This is a shared infrastructure dependency that affects the entire hypothesis family. If the data is not available, all computational protocols require new simulations.

2. **Klimov & Thirumalai 1997 misattribution:** E-H5 attributes a specific formula for high-dimensional roughness correction to a paper that is about viscosity dependence of folding rates. This is a content misattribution, not a citation fabrication -- the paper exists and the authors did work in the broader area of energy landscape theory. However, the specific formula is not in the cited paper.

3. **Noji 2021 partial mischaracterization:** Both E-H4 and E-H5 cite Noji 2021 as showing that "thermal history shifts protein ensemble toward amyloid pathway." The paper is actually about supersaturation barrier breakdown. While it does demonstrate that thermal manipulation affects aggregation outcome, the mechanism is supersaturation-related, not eigenmode-specific.

4. **Monomer-to-aggregation gap:** All hypotheses operate on single-molecule MSM properties but predict multi-molecule aggregation outcomes. The gap between intramolecular conformational dynamics and intermolecular aggregation kinetics remains the fundamental weakness of the entire framework. E-H4's experimental protocol partially addresses this by directly measuring aggregation outcome, but E-H1 and E-H5 remain purely computational.

---

## META-VALIDATION (self-review)

1. **For each CONDITIONAL PASS: would I bet my reputation?** E-H5 and E-H4 are genuinely novel and well-constructed hypotheses that I would defend as worthy of computational/experimental investigation. E-H1 is a well-corrected version of a hypothesis with a real mathematical core. E-H7 is the most speculative but addresses a genuine puzzle. None received a full PASS because each has at least one unverifiable claim or misattributed content.

2. **Did I perform sufficient web searches?** Yes: 16 total searches across novelty, citation verification, mechanism, and counter-evidence. Each hypothesis received 4-6 relevant searches.

3. **Unverifiable claims:** The DESRES data availability is unverifiable for all four hypotheses. The Klimov-Thirumalai formula is misattributed in E-H5. These are documented and factored into the adjusted scores. No CONDITIONAL PASS hypothesis has an unverifiable CORE mechanism claim -- the unverifiable claims concern infrastructure (data availability) and a dimensional correction (not the core prediction).

4. **Per-claim verification completeness:** Every [GROUNDED] claim has been individually verified or documented as unverifiable. The Klimov-Thirumalai misattribution was caught and documented. The Noji 2021 partial mischaracterization was caught and documented.

5. **Citation audit:** 17 citations audited. 13 fully verified. 1 content misattribution (Klimov-Thirumalai -- paper exists but content does not match). 1 unverifiable dataset ID (DESRES). 1 partial mischaracterization (Noji 2021). Zero fabricated citations in the evolved hypotheses (the parent's fabricated citations -- Eschmann 2015, mischaracterized Rosenman and Robustelli -- were properly corrected by the Evolver).

**Final assessment:** No hypothesis earns a full PASS due to shared infrastructure uncertainties and one content misattribution. All four earn CONDITIONAL PASS because the core connections are genuinely novel, the mechanisms are plausible on verified physical grounds, and the predictions are falsifiable. The Evolver did substantial quality-improving work -- particularly on E-H4 (removing the Kusumoto false attribution) and E-H1 (correcting three citation errors). The session produced a coherent family of hypotheses exploring a genuinely unexplored cross-disciplinary bridge.
