# Cycle 1 Critique (v2) — Mpemba Spectral Theory × Amyloid Aggregation

**Session:** 2026-03-28-scout-014
**Critic model:** Opus (max effort)
**Date:** 2026-03-28
**Hypotheses evaluated:** 7
**Verdicts:** 0 SURVIVES, 5 WOUNDED, 2 KILLED
**Kill rate:** 2/7 (28.6%)

> Note: This is a re-critique with enhanced adversarial pressure. The previous
> critique (0 kills) was insufficiently adversarial per Minimum Adversarial Standard.

---

## Summary

| ID | Title | Verdict | Conf | Ground | Key Fatal/Severe Issue |
|----|-------|---------|------|--------|------------------------|
| H1 | Mpemba Index Predicts Amyloid Propensity | WOUNDED | 5←7 | 5←7 | 3 citation errors; single→multi molecule gap |
| H2 | Spectral Gap Ratio Predicts Lag Time | WOUNDED | 4←6 | 4←6 | Ad hoc T_lag~1/(1-R); multi-molecule gap; underpowered |
| H3 | Non-Normal Liouvillian Transient Amplification | **KILLED** | 2←5 | 3←6 | Detailed balance eliminates non-normality by construction |
| H4 | Inverse Mpemba Protocol Suppresses Amyloid | WOUNDED | 3←6 | 4←7 | Kusumoto 1998 misrepresented; 60C denaturation; simpler explanation |
| H5 | Rough Landscape Diffusion Asymmetry | WOUNDED | 4←5 | 5←6 | Zwanzig 1D→high-dim extrapolation; non-amyloid proteins also rough |
| H6 | Comparative Mpemba Index as Universal Classifier | WOUNDED | 3←5 | 4←6 | 2/6 controls are actually amyloidogenic; statistically underpowered |
| H7 | Prion Strain Selection via Eigenmode Branching | **KILLED** | 2←4 | 3←5 | PrP MSM infeasible; phenomenon already known; adds no prediction |

---

## H1: Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity

### VERDICT: WOUNDED
### Revised Confidence: 5/10 (down from 7)
### Revised Groundedness: 5/10 (down from 7)

**ATTACKS:**

**1. Novelty Kill**
- Query: "Mpemba index protein folding Markov state model amyloid" → 0 results
- Query: "Mpemba effect biological self-assembly eigenmode" → Found Chittari & Lu 2023 (J. Chem. Phys.), "Geometric approach to nonequilibrium hasty shortcuts" — eigenmode decomposition applied to viral capsid assembly model. Partial precedent but does NOT compute Mpemba index for protein MSMs.
- **Novelty HOLDS.** Zero papers apply Mpemba index theory to amyloid protein MSMs.

**2. Mechanism Kill (MEDIUM)**
Mechanism chain (MSM eigendecomposition → Fiedler mode → Mpemba index → aggregation prediction) is mathematically valid for any discrete Markov chain. Klich et al. 2019 PRX confirmed. However, the mapping from single-molecule MSM eigenspectrum to multi-molecule aggregation behavior has a fundamental gap. Amyloid aggregation is dominated by intermolecular processes: primary nucleation, secondary nucleation on fibril surfaces (Cohen et al. 2012 PNAS), fragmentation, and elongation. The MSM eigenspectrum governs intramolecular conformational dynamics. The connection between monomer conformational properties and population-level nucleation kinetics is asserted, not derived.

**3. Logic Kill (LOW)**
Reasonable inference from formalism. Not a logical fallacy but an untested extrapolation.

**4. Falsifiability Kill**
PASSES. Mpemba(Abeta42) >= 2, Mpemba(Abeta40) = 0 or 1, Spearman rho > 0.7 across 4+ pairs — all falsifiable. Practical falsifiability depends on MSM availability.

**5. Triviality Kill**
NOT trivial. Cross-field connection is non-obvious.

**6. Counter-Evidence Search**
No direct counter-evidence found. The MSM-for-aggregation literature (Narayan et al. 2020) confirms MSMs are used for pathway analysis but no one computes Mpemba indices. Absence of counter-evidence is a positive sign.

**7. Groundedness Attack**
- Klich et al. 2019, PRX 9:021060: VERIFIED
- Jia et al. 2020, PNAS 117:10322: VERIFIED (but for fragment Aβ16-22, not full Abeta42)
- Husic & Pande 2018, JACS 140:2386: VERIFIED
- Rosenman et al. "2016, J. Mol. Biol. 428:1600": **WRONG YEAR AND NOT AN MSM**. Paper is from 2013 (J. Mol. Biol. 425:3338). It's a REMD structural ensemble study, not an MSM transition matrix.
- Robustelli et al. 2018 PNAS: **MISCHARACTERIZED**. This is a force field paper (a99SB-disp, PNAS 115:E4758), not "a disordered protein MSM from D.E. Shaw long-trajectory simulations."
- Eschmann et al. 2015: **WRONG JOURNAL**. Published in J. Phys. Chem. B 119:14421, not J. Chem. Phys. Studies tau via EPR/DNP, not MSM construction.
- **3/6 cited MSM sources are wrong or mischaracterized. Groundedness drops to 5/10**

**8. Hallucination-as-Novelty Check**
Novelty is genuine — bridging two independently verified formalisms. Low hallucination risk.

**9. Claim-Level Fact Verification**
- "Abeta42 MSM exists" → True (confirmed via computational validator) but the specific citation is wrong
- "Robustelli 2018 provides alpha-synuclein MSM" → FALSE (force field paper)
- "Eschmann 2015 provides tau K18 MSM" → FALSE (EPR/DNP experimental study)
- The test protocol assumes "retrieving published MSMs" from wrongly cited sources

**SURVIVAL NOTE:** Core concept (Mpemba index from protein MSMs) is genuinely novel and mathematically sound. Bridge is the strongest in the suite. But grounding is weakened by 3 citation errors, and the single→multi molecule gap is a fundamental conceptual challenge. Survives as wounded because the mathematical framework is correct even if the specific citations are wrong.

---

## H2: Spectral Gap Ratio of Combined Fold/Misfold MSMs Predicts Amyloid Nucleation Lag Time

### VERDICT: WOUNDED
### Revised Confidence: 4/10 (down from 6)
### Revised Groundedness: 4/10 (down from 6)

**ATTACKS:**

**1. Novelty Kill**
- Query: "spectral gap ratio MSM folding misfolding aggregation prediction" → 0 direct results
- **Novelty HOLDS.** The ratio R = Delta_combined/Delta_fold as predictor is novel.

**2. Mechanism Kill (HIGH)**
T_lag ~ 1/(1-R) is an entirely ad hoc functional form with no theoretical derivation. Why this function and not T_lag ~ exp(1/R) or T_lag ~ R^{-alpha}? No first-principles argument connects a single-molecule spectral gap ratio to a multi-molecule nucleation lag time. Nucleation lag time depends on protein concentration, secondary nucleation rates (Cohen et al. 2012), fragmentation rates, surface catalysis, pH, ionic strength — none captured by a spectral gap ratio.

**3. Logic Kill (MEDIUM)**
Timescale analogy: because MSM spectral gap governs relaxation time and nucleation lag is also a timescale, they "must" be related via a simple function. This is correlation-by-construction, not a mechanistic argument.

**4. Falsifiability Kill**
PASSES in principle. But rank-ordering 4 proteins with Spearman rho > 0.8 can happen by chance — with N=4, there are only 24 possible orderings, and chance alone gives rho > 0.8 for 4/24 = 17% of orderings. This is not a stringent test.

**5. Triviality Kill**
Not trivial conceptually. But fitting a 1-parameter monotonic function to 4 data points is trivially achievable.

**6. Counter-Evidence Search**
- Cohen et al. 2012 (PNAS 109:9761): secondary nucleation dominates Abeta42 proliferation. This is STRONG counter-evidence — the rate-limiting step is a multi-molecule, fibril-surface-dependent process, not a single-molecule conformational transition.
- MSM spectral gaps are sensitive to construction methodology (TICA, PCCA+, VAMPnet) — different methods yield different R values for identical trajectory data.

**7. Groundedness Attack**
- Prinz et al. 2011: VERIFIED
- Jia et al. 2020: VERIFIED (fragment)
- Arosio et al. 2015: VERIFIED
- Nilsberth et al. 2001 (E22G Arctic mutation): VERIFIED
- Cohen et al. 2012: VERIFIED (but is counter-evidence!)
- "T_lag ~ 1/(1-R)": UNGROUNDED — ad hoc postulate
- "Construction of combined fold/misfold MSMs": Computational validator confirms these are "not off-the-shelf"

**8. Hallucination-as-Novelty Check**
Components real; functional form speculative. Risk: curve-fitting masquerading as prediction.

**9. Claim-Level Fact Verification**
- "Abeta42 T_lag ~ 2-4h at 37C": Approximately correct
- "Alpha-synuclein T_lag ~ 24-72h without seeds": Approximately correct
- "E22G accelerates aggregation": VERIFIED
- "A2V mutation prevents aggregation": Oversimplified — A2V is protective in heterozygous form but may accelerate in homozygous (Di Fede et al. 2009 Science)

**SURVIVAL NOTE:** Novel concept with real components. The ad hoc functional form, the single→multi molecule gap (Cohen et al. secondary nucleation), the trivially achievable statistical test (4 proteins), and non-existent combined MSMs collectively weaken it. The specific functional form needs theoretical derivation.

---

## H3: Non-Normal Liouvillian Dynamics of Amyloidogenic MSMs Create Transient Misfolding Acceleration Zones

### VERDICT: KILLED
### Revised Confidence: 2/10 (down from 5)
### Revised Groundedness: 3/10 (down from 6)

**ATTACKS:**

**1. Novelty Kill**
- Query: "non-normal Liouvillian transient amplification protein misfolding" → 0 results
- Novel in this domain. **But the novelty may be because the mechanism is structurally impossible under standard methods.**

**2. Mechanism Kill — FATAL**
**Standard MSM construction tools (PyEMMA, MSMBuilder) enforce detailed balance by default.** Web search confirmed: PyEMMA's `estimate_markov_model` constrains models to be reversible; MSMBuilder documentation states "the model is constrained to be reversible (satisfy detailed balance)."

Detailed balance produces time-reversible transition matrices. The detailed-balance-symmetrized matrix (D^{1/2} Q D^{-1/2}, where D = diag(pi)) is symmetric, hence NORMAL, hence QQ^T = Q^TQ, hence Henrici departure delta(Q) = 0 by construction.

**ANY MSM built with standard tools will show delta(Q) = 0. The hypothesis cannot detect what it claims to detect.**

Unsymmetrized estimators exist but are non-standard, less statistically robust, and their biological interpretation is debated. The hypothesis does not propose using them.

**3. Logic Kill (HIGH)**
Asymmetric energy landscape does NOT equal non-normal rate matrix. The landscape can be topologically asymmetric (funnel for folding, rough for misfolding) while equilibrium transition dynamics satisfy detailed balance perfectly. This confuses landscape topology with dynamical symmetry.

**4. Falsifiability Kill — EFFECTIVELY FAILS**
Under standard methodology, delta(Q) approximately equals 0 for ALL proteins. The hypothesis is vacuously satisfied for every protein, making it unfalsifiable.

**5. Triviality Kill**
A physicist working with non-normal dynamics would immediately recognize that detailed-balance systems are normal.

**6. Counter-Evidence Search**
Web search confirmed standard MSM estimation enforces reversibility. "Symmetrized estimator biases results towards starting distribution" — even unsymmetrized alternatives have known bias problems.

**7. Groundedness Attack**
- Teza et al. 2025 Physics Reports: VERIFIED (non-normal Liouvillian is real in physics)
- Lapolla & Godec 2020 PRL 125:110602: VERIFIED ("Faster Uphill Relaxation")
- Henrici 1962: VERIFIED
- Onuchic et al. 1997: VERIFIED
- "Amyloidogenic MSM generators exhibit significant non-normality": CANNOT BE TRUE under standard construction.
- Groundedness drops to 3/10: real physics components assembled into an impossible claim.

**8. Hallucination-as-Novelty Check**
**This IS hallucination-as-novelty.** The hypothesis appears novel BECAUSE the connection it proposes is structurally impossible under standard MSM construction. Nobody has done it because detailed balance prevents it.

**9. Claim-Level Fact Verification**
- "||QQ^T - Q^TQ|| >> 0 for amyloidogenic MSMs": STRUCTURALLY FALSE under standard construction
- "Transient amplification of misfolded-state occupancy": Requires non-normality which doesn't exist under standard methods. Circular reasoning.
- "Henrici departure higher for amyloidogenic proteins because of asymmetric transitions": Detailed balance eliminates this regardless of landscape asymmetry.

**SURVIVAL NOTE:** KILLED. The physics of non-normal transient amplification is real (Teza et al. 2025). But protein MSMs built with standard tools are normal by construction. The hypothesis fails at the most basic methodological level. Rescue path: unsymmetrized estimators for non-equilibrium trajectories (e.g., MSMs with irreversible aggregation sink states), but the hypothesis does not propose this.

---

## H4: Inverse Mpemba Protocol Suppresses Amyloid Fibril Formation by Exploiting Eigenmode Decoupling

### VERDICT: WOUNDED (severe)
### Revised Confidence: 3/10 (down from 6)
### Revised Groundedness: 4/10 (down from 7)

**ATTACKS:**

**1. Novelty Kill**
- Query: "cooling rate amyloid fibril formation temperature protocol aggregation suppression" → Found temperature effect literature but NO work using Mpemba eigenmode-overlap to design cooling protocols.
- **Novelty HOLDS** for the eigenmode mechanism.

**2. Mechanism Kill (HIGH)**
Depends on "danger zone" at 45-55C where eigenmode overlap is maximal. This claim cites Kusumoto 1998 — which does NOT support it. At 60C, Abeta42 is substantially denatured. The "high-temperature ensemble" is a denatured, aggregation-prone state, not a broadly sampled conformational space.

**3. Logic Kill (MEDIUM)**
**Competing simpler explanation:** Rapid quench minimizes time at elevated temperature where aggregation is thermodynamically favorable. Occam's razor favors the simpler explanation over an elaborate eigenmode mechanism.

**4. Falsifiability Kill**
PASSES. The experiment is straightforward. But if the effect IS observed, it cannot distinguish eigenmode mechanism from simpler thermal exposure explanation without the non-monotonic cooling-rate control.

**5. Triviality Kill**
The prediction (rapid cooling → less aggregation) might be trivially expected from Arrhenius kinetics.

**6. Counter-Evidence Search**
- Query: "Abeta42 aggregation non-monotonic temperature nucleation rate maximum" → No evidence for nucleation maximum at intermediate temperatures for Abeta42.
- Literature shows mostly monotonic temperature dependence until denaturation.

**7. Groundedness Attack**
- Klich et al. 2019: VERIFIED
- **Kusumoto et al. 1998, PNAS 95:12277: MISREPRESENTED.** Paper measures fibril ELONGATION rates (not nucleation) from 4-40C and shows MONOTONIC Arrhenius behavior (activation energy ~23 kcal/mol). Does NOT show "maximal nucleation at intermediate temperatures." The hypothesis falsely attributes non-monotonic T-dependence to this paper.
- Noji et al. 2021: VERIFIED (about supersaturation barrier — characterization is loose but acceptable)
- Groundedness: 4/10 — the CENTRAL claim about non-monotonic T-dependence is based on a misrepresented source.

**8. Hallucination-as-Novelty Check**
The "danger zone at 45-55C" for Abeta42 appears to be a fabricated parametric claim. No source supports this specific temperature range as a nucleation maximum.

**9. Claim-Level Fact Verification — CRITICAL**
- "Abeta42 aggregation shows non-monotonic temperature dependence with enhanced nucleation at intermediate temperatures (Kusumoto et al. 1998)": **FALSE.** Kusumoto 1998 shows MONOTONIC Arrhenius kinetics for fibril elongation across 4-40C.
- "60C hold → rapid quench preserves high-T ensemble projection": At 60C, Abeta42 is denatured. The "preserved ensemble" is a denatured state.
- "Intermediate temperature regime (45-55C for Abeta42) = danger zone": No evidence found.

**SURVIVAL NOTE:** The general concept (cooling-protocol-dependent aggregation via eigenmode avoidance) is creative. But the Abeta42 application is built on a misrepresented citation, a fabricated danger zone, and denaturation at the proposed starting temperature. Severely wounded. Could be rescued with correct temperature ranges for a protein system where non-monotonic behavior is documented.

---

## H5: Rough Energy Landscape Diffusion Asymmetry (D_fold >> D_misfold) Creates the Spectral Signature That the Mpemba Index Detects

### VERDICT: WOUNDED
### Revised Confidence: 4/10 (down from 5)
### Revised Groundedness: 5/10 (down from 6)

**ATTACKS:**

**1. Novelty Kill**
- Query: "Zwanzig roughness Mpemba spectral structure protein" → 0 results
- **Novelty HOLDS.** Connecting Zwanzig roughness to Mpemba spectral structure is novel.

**2. Mechanism Kill (MEDIUM)**
Zwanzig's D_eff = D_0 * exp(-(epsilon/kT)^2) is derived for 1D diffusion on a periodic rough potential. Proteins live in 10^3-10^5 dimensional spaces. The extrapolation is not rigorous. Exponential sensitivity means small epsilon uncertainties produce orders-of-magnitude D_eff uncertainty — "100-1000x" could be off by 10^6.

**3. Logic Kill (LOW)**
Physical motivation at each step of the chain. Not a logical fallacy.

**4. Falsifiability Kill**
PASSES. Bimodal eigenvalue spectrum (Sarle's BC > 0.555 for amyloidogenic, < 0.555 for non-amyloidogenic) is specific and testable. Most falsifiable hypothesis in the suite.

**5. Triviality Kill**
NOT trivial. Connection is non-obvious.

**6. Counter-Evidence Search**
Non-amyloidogenic proteins (myoglobin, cytochrome c) have roughness epsilon ~ 2-3 kT (Hyeon & Thirumalai 2003). The assumption that non-amyloidogenic proteins lack comparable landscape roughness is unverified and possibly wrong.

**7. Groundedness Attack**
- Zwanzig 1988, PNAS 85:2029: VERIFIED
- Bryngelson et al. 1995: VERIFIED
- Jia et al. 2020: VERIFIED (for Aβ16-22 fragment)
- Husic & Pande 2018: VERIFIED
- D_misfold/D_fold ratio: Computational validator marks "PLAUSIBLE" but NO published paper has directly measured this for any amyloidogenic protein. Untested prediction.
- All citations correct. Groundedness: 5/10 (correct citations, theoretical predictions).

**8. Hallucination-as-Novelty Check**
Bridge mechanism (Zwanzig roughness) exists independently. Low hallucination risk.

**9. Claim-Level Fact Verification**
- "Roughness epsilon ~ 3-5 kT for misfolding landscape": Partially supported by literature. Specific amyloidogenic values are estimated, not measured.
- "Non-amyloidogenic proteins lack extreme asymmetry": UNVERIFIED. Counter-evidence from myoglobin (epsilon ~ 2-3 kT).
- "Bimodal eigenvalue spectrum": Theoretical prediction — no published MSM demonstrates this.

**SURVIVAL NOTE:** Best citation accuracy in the suite. Most falsifiable predictions. Provides the mechanistic backbone for H1 and H2. But 1D→high-dimensional extrapolation, unverified non-amyloidogenic roughness assumption, and no empirical validation prevent SURVIVES. Worth pursuing computationally as the first test of the whole framework.

---

## H6: Comparative Mpemba Index Across Protein Pairs Identifies a Universal Spectral Aggregation Vulnerability Threshold

### VERDICT: WOUNDED (severe)
### Revised Confidence: 3/10 (down from 5)
### Revised Groundedness: 4/10 (down from 6)

**ATTACKS:**

**1. Novelty Kill**
Novel — nobody has computed Mpemba indices from protein MSMs. **Novelty HOLDS**, but proposing threshold M* before computing a single index is premature.

**2. Mechanism Kill (HIGH)**
BINARY classifier for CONTINUOUS, context-dependent phenomenon. Amyloid propensity depends on concentration, pH, ionic strength, temperature, surfaces, seeds, cofactors. Single-molecule MSM threshold cannot capture these.

**3. Logic Kill (HIGH)**
- **Statistical naivety**: AUROC > 0.85 from 12 proteins has enormous confidence intervals via DeLong's method.
- **Circular comparison**: Outperforming TANGO/CamSol "on borderline cases" with perhaps 2-3 such cases is meaningless.
- **Corrupted controls**: 2/6 "non-amyloidogenic" proteins are actually amyloidogenic.

**4. Falsifiability Kill**
AUROC < 0.70 with N=12 has ~17% false-positive rate from random classifier. Unacceptably high.

**5. Triviality Kill**
Concept is not trivial; proposed test is trivially underpowered.

**6. Counter-Evidence Search**
TANGO/CamSol/Zyggregator validated on hundreds of proteins. Comparing with 12 is methodologically unfair.

**7. Groundedness Attack**
- Fernandez-Escamilla 2004 (TANGO): VERIFIED
- Tartaglia 2008 (Zyggregator): VERIFIED
- Sormanni 2015 (CamSol): VERIFIED
- **Hashimoto et al. 2001: WRONG JOURNAL.** Published in Neuron, not Brain Research. Content correctly described.
- "~75-80% accuracy": Approximately correct per benchmarks.

**8. Hallucination-as-Novelty Check**
Not hallucinatory. But "universal threshold" from 6 pairs is overreach.

**9. Claim-Level Fact Verification — CRITICAL**
- **FUS classified as "less amyloidogenic"**: WRONG. FUS forms pathological aggregates in ALS/FTD (Kwiatkowski et al. 2009 Science). Not a valid negative control.
- **TTR-WT classified as "less amyloidogenic"**: WRONG. Wild-type transthyretin causes ATTRwt amyloidosis in ~25% of individuals over 80 (Ruberg et al. 2019 JACC). Hypothesis acknowledges this in counter-evidence but still proposes it as negative control — internally inconsistent.
- With 2/6 controls corrupted, clean dataset = 4 pairs. AUROC from 4 pairs is meaningless.

**SURVIVAL NOTE:** The concept (kinetic MSM-based classifier complementing thermodynamic sequence-based classifiers) is appealing. But 2/6 negative controls are positive, dataset is underpowered, and "universal threshold" from 6 pairs is unjustified. Could be rescued by correcting protein pairs, expanding dataset, and framing as hypothesis-generating.

---

## H7: Temperature-History Dependence of Prion Strain Selection Is Explained by Mpemba Eigenmode Branching

### VERDICT: KILLED
### Revised Confidence: 2/10 (down from 4)
### Revised Groundedness: 3/10 (down from 5)

**ATTACKS:**

**1. Novelty Kill (PARTIAL)**
- Query: "prion strain selection temperature cooling rate PrP fibril polymorph" → EXTENSIVE literature showing temperature affects PrP polymorphism. The PHENOMENON is well-known.
- What's novel is the EXPLANATION (eigenmode branching). But it requires a PrP MSM that doesn't exist.

**2. Mechanism Kill — FATAL**
PrP^C → PrP^Sc involves massive conformational change (alpha-helix → beta-sheet) beyond current all-atom MD capabilities. No PrP misfolding MSM exists or can realistically be constructed. The hypothesis requires ">200 microseconds enhanced sampling" — infeasible for this transition.

**3. Logic Kill (HIGH)**
Prion strain selection depends on cofactors (lipids, polyanions, RNA — Deleault et al. 2012 PNAS), host PrP polymorphisms, species barriers. Published evidence: "at least two main fibril populations from seemingly homogeneous seeds" (PMC 10100569) suggests stochastic kinetic trapping, not deterministic eigenmode branching.

**4. Falsifiability Kill — EFFECTIVELY FAILS**
Computational test (build PrP MSM) is infeasible. Experimental test (cooling protocols → different polymorphs) is ALREADY KNOWN. The hypothesis doesn't predict WHICH polymorph forms at WHICH rate — only THAT different rates produce different polymorphs (already established).

**5. Triviality Kill (MEDIUM)**
Prediction (different thermal histories → different polymorphs) is already known.

**6. Counter-Evidence Search**
- Temperature-dependent PrP polymorphism: demonstrated without eigenmode theory
- Competing fibril populations under identical conditions: suggests stochastic trapping, not deterministic eigenmode branching

**7. Groundedness Attack**
- Collinge & Clarke 2007: VERIFIED
- Petkova et al. 2005: VERIFIED (but Abeta, not PrP specifically)
- Legname et al. 2004: VERIFIED
- Taylor 2000: VERIFIED
- "PrP MSM with strain-specific eigenmodes": FABRICATED — no such model exists.

**8. Hallucination-as-Novelty Check**
Novel because UNTESTABLE — not because genuinely unexplored. Unfalsifiable novelty.

**9. Claim-Level Fact Verification**
- "80C starting temperature": PrP denatures above ~65C. At 80C, protein is irreversibly unfolded.
- "Fast quench yields Type 1-like, slow yields Type 2-like": No evidence. Type 1/2 defined by PK digestion of brain prions, not in vitro cooling.
- "Predicted crossover temperature ~55C": Cannot be computed without nonexistent MSM.

**SURVIVAL NOTE:** KILLED. Phenomenon is known, explanation is untestable, predictions don't exceed existing knowledge, 80C denatures PrP, and no PrP misfolding MSM can be built. No rescue path exists with current technology.

---

## META-CRITIQUE

### Kill rate: 2/7 (28.6%)
- H3: Structural impossibility (detailed balance → normality)
- H7: Infeasibility + triviality + no new predictions
- Borderline: H4 nearly killed (misrepresented citation, fabricated danger zone)

### Strongest case for kill that wasn't made
H4: Kusumoto 1998 misrepresentation is severe. But the general eigenmode concept could work for a protein system where non-monotonic T-dependence actually exists.

### Web search completeness
18+ distinct searches. Every hypothesis has novelty + counter-evidence + claim verification searches.

### GROUNDED claim verification summary
- **Citation errors**: Rosenman 2013 not 2016, Hashimoto in Neuron not Brain Research, Eschmann in J. Phys. Chem. B not J. Chem. Phys.
- **Mischaracterizations**: Robustelli 2018 = force field not MSM; Kusumoto 1998 = monotonic not non-monotonic
- **Impossible claims**: H3 non-normality in standard MSMs; H7 PrP MSM with strain eigenmodes
- **0 outright fabricated citations** — all papers exist, some with wrong details or mischaracterized content

### Cross-hypothesis structural weakness
All 7 share: single-molecule MSM eigenspectral analysis vs multi-molecule aggregation kinetics gap. Amyloid aggregation is concentration-dependent, dominated by secondary nucleation (Cohen et al. 2012). This is the suite's Achilles heel.

---

## Critic Questions for Cycle 2

1. **H1 (MSM citations):** Which published MSMs provide transition matrices for eigendecomposition for Abeta42, alpha-synuclein, and tau? Cited Rosenman 2013 is REMD ensembles, Robustelli 2018 is a force field, Eschmann 2015 is EPR/DNP.

2. **H1/H2/H4/H6 (single→multi molecule gap):** How does single-molecule MSM eigenspectral property predict multi-molecule aggregation dominated by secondary nucleation (Cohen et al. 2012)?

3. **H3 (detailed balance rescue):** How would you construct a non-reversible MSM preserving non-normality? Under what conditions does detailed balance not apply?

4. **H4 (non-monotonic T-dependence):** Kusumoto 1998 shows monotonic Arrhenius kinetics. Provide correct citation for non-monotonic Abeta42 nucleation or reformulate.

5. **H5 (bimodal spectra):** Published examples of bimodal MSM eigenvalue spectra for amyloidogenic proteins?

6. **H6 (negative controls):** FUS (ALS/FTD) and TTR-WT (~25% elderly) are amyloidogenic. How can they be negative controls?

7. **H7 (PrP MSM feasibility):** Realistic path to PrP misfolding MSM within 5 years?
