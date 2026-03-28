# Cycle 2 Rankings -- Mpemba Spectral Theory x Amyloid Aggregation Selectivity

**Session:** 2026-03-28-scout-014
**Cycle:** 2
**Ranker:** Ranker agent (Sonnet, high effort)
**Timestamp:** 2026-03-28
**Survivors scored:** 4 of 8 (C2-H4, C2-H6, C2-H7, C2-H8 killed)
**Weight scheme:** Canonical v5.2 -- Novelty 20%, Mech. Specificity 20%, Cross-field Distance 10%, Testability 20%, Impact Paradigm 5%, Impact Translational 5%, Groundedness 20%. Cross-domain bonus +0.5 for 2+ disciplinary boundaries.
**Overrides:** Previous ranker run used cycle-1 weights (novelty 15%, cross_domain_creativity 15%) and incorrectly scored C2-H4 as a conditional survivor. This run uses canonical v5.2 weights and 4 true survivors.

**Hypothesis file mapping:**
- C2-H1 maps to H1 in cycle2-hypotheses.md (Resource-Theoretic D_KL unified score)
- C2-H2 maps to H5 in cycle2-hypotheses.md (D_misfold/D_fold calibration + TANGO cross-validation)
- C2-H3 maps to H7 in cycle2-hypotheses.md (Cooling-rate polymorph selection, refined to insulin)
- C2-H5 has no direct equivalent in cycle2-hypotheses.md (resource-theoretic therapeutic window; session.json confirms builds_on H4 + E5-H4)

---

## Per-Hypothesis Scoring Tables

### Hypothesis: C2-H1 -- A* State Population Is the Protein Mpemba Overlap Coefficient: A Quantitative Unification

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 8 | Critic confirmed NOVEL. Bridges resource-theoretic Mpemba monotone (Summer et al. 2026 PRX, HALLUCINATED as Avanzini) with protein MSM A* populations and amyloid aggregation. No published work connects D_KL-based Mpemba monotones to amyloid-prone A* ensembles; Teza 2025 review confirms zero cross-field papers. Docked from 9 because it extends the cycle 1 flagship (H1) rather than introducing an entirely new bridge concept. |
| Mechanistic Specificity | 20% | 7 | Mathematically precise: D_KL = sum(c_k)^2/(2|lambda_k|), spectral concentration into slow modes, D_KL = deltaF/kT in canonical limit. Names specific molecules (Chakraborty A* states, Abeta42 vs Abeta40 D_KL comparison). However, the Fiedler vector (psi_2) partition of native vs aggregation-prone basins is completely unverified for any protein MSM -- the most critical mechanistic step is assumed. The canonical-ensemble D_KL conflation (static free energy != dynamic quantity) is an unresolved theoretical flaw. Monomer-to-aggregation gap persists. |
| Cross-field Distance | 10% | 8 | Traverses at least four disciplinary communities: (1) non-equilibrium statistical physics (Mpemba), (2) quantum information theory / resource theory (Summer et al. 2026), (3) Markov chain mathematics, (4) computational protein biophysics (MSM construction), (5) amyloid biochemistry. The inclusion of quantum information resource theory is the most extreme bridge in the cycle 2 set. |
| Testability | 20% | 6 | Test protocol specified: MSM construction for 8 proteins, A* identification via Chakraborty hierarchical clustering, D_KL computation, spectral decomposition, Spearman rho vs ThT half-time. Core prediction (D_KL >= 1.5-fold lower for Abeta42 than Abeta40) is falsifiable. However: IDP MSM construction is notoriously difficult; A* identification is algorithm-dependent; D_KL requires successful MSM diagonalization. Realistic timeline is 18-24 months for a specialized computational biophysicist, not a 3-month PhD project. |
| Impact: Paradigm | 5% | 7 | If D_KL provides a unified scalar subsuming TANGO, Zyggregator, and Mpemba index under a single thermodynamic framework, this substantially reframes aggregation vulnerability assessment. Would open a new analysis layer (resource-theoretic protein design) but fits within existing frameworks rather than overturning them. |
| Impact: Translational | 5% | 5 | D_KL screening across amyloidogenic protein variants could prioritize drug targets or diagnostic markers. Path from unified theoretical scalar to clinical application is indirect and speculative at this stage. |
| Groundedness | 20% | 5 | Critique: 2/5 grounded claims verified (40%). CRITICAL hallucination: "Avanzini et al. 2026 PRX 16:011065" is fabricated author attribution -- real paper is Summer, Moroder, Bettmann, Turkeshi, Marvian and Goold 2026 PRX. Fiedler partition unverified. D_KL = deltaF/kT conflation unresolved. Verified: Chakraborty 2020 PNAS 117:16817, Klich 2019 PRX 9:021060, Lu and Raz 2017 PNAS 114:5083. Maps to integer 5 (MEDIUM). |
| **Composite (pre-bonus)** | | **6.60** | 0.20x8 + 0.20x7 + 0.10x8 + 0.20x6 + 0.05x7 + 0.05x5 + 0.20x5 = 1.60+1.40+0.80+1.20+0.35+0.25+1.00 |
| **Cross-domain bonus** | | **+0.50** | Crosses non-equilibrium physics + quantum information theory + computational biophysics + amyloid biochemistry: clearly 2+ disciplinary boundaries. Cross-domain bonus applied: +0.5 |
| **Composite** | | **7.10** | |

---

### Hypothesis: C2-H2 -- Measured D_misfold/D_fold Ratio of PrP Predicts Bimodal Eigenvalue Spectrum via Zwanzig-Kramers Bridge

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 7 | Critic confirmed NOVEL. The specific quantitative connection -- Yu 2015 measured D ratio to Zwanzig roughness parameter to bimodal eigenvalue spectrum to aggregation prediction hierarchy -- has not appeared in the literature. TANGO cross-validation as an information-orthogonality test adds a new validation dimension. Docked from 8 because this calibrates and grounds cycle 1 H5 (roughness asymmetry) rather than introducing an entirely new bridge concept. |
| Mechanistic Specificity | 20% | 8 | Strongest mechanistic specificity in the survivor set. Yu et al. measured D_misfold ~10^3 nm^2/s and D_fold ~10^6 nm^2/s for PrP giving epsilon_misfold ~3.3 kT via Zwanzig formula. BC > 0.555 bimodality criterion quantitatively specified. Three-tier hierarchy (roughness to bimodality to Mpemba index to aggregation) fully articulated. k_n formula corrected for Cohen et al. secondary nucleation. TANGO provides external calibration. Weakness: Yu 2015 measured PrP DIMERS under single-molecule force spectroscopy, not monomers in free solution. |
| Cross-field Distance | 10% | 7 | Crosses condensed matter physics (Zwanzig 1988 roughness diffusion theory) to Markov chain spectral mathematics to protein biophysics (force spectroscopy, MSM) to amyloid biochemistry. Slightly less extreme than C2-H1 (no quantum information component) but spans clearly distinct disciplinary communities. |
| Testability | 20% | 7 | Excellent test protocol: epsilon_misfold within 2.8-3.8 kT for 4 amyloidogenic proteins; TANGO/CamSol cross-validation for all 8 sequences; disagreement adjudicated by ThT half-time; Abeta42 concentration test at 1/5/25 uM (Cohen 2013 anchored). Clear falsification: if M_eff and TANGO agree perfectly (rho > 0.9), spectral approach adds nothing. A PhD student with computational biophysics training could execute in ~12-18 months. Better than C2-H1 due to cross-validation anchor. |
| Impact: Paradigm | 5% | 6 | Provides first experimentally calibrated roughness-MSM-aggregation chain, validating whether the theoretical framework makes quantitative contact with measurable diffusion coefficients. More incremental than paradigm-shifting -- extends existing frameworks with experimental grounding. |
| Impact: Translational | 5% | 5 | D ratio screening across amyloidogenic protein variants could prioritize drug targets. Cohen 2013 secondary nucleation anchor enables concentration-dependent prediction. Translational pathway is indirect but more concrete than C2-H1. |
| Groundedness | 20% | 6 | Critique: 4/6 grounded claims verified (67%), revised groundedness 6/10 -- highest in the cycle 2 set. Verified: Yu et al. 2015 PNAS 112:8308 (D ratio), Cohen et al. 2012/2013 (secondary nucleation kinetics), Fernandez-Escamilla et al. 2004 (TANGO). PMID 41665928 unverified but "not fatal"; computational validator confirmed physics content. No fabricated author attributions. Maps to integer 6 (MEDIUM-HIGH). |
| **Composite (pre-bonus)** | | **6.85** | 0.20x7 + 0.20x8 + 0.10x7 + 0.20x7 + 0.05x6 + 0.05x5 + 0.20x6 = 1.40+1.60+0.70+1.40+0.30+0.25+1.20 |
| **Cross-domain bonus** | | **+0.50** | Crosses condensed matter physics + Markov spectral mathematics + protein biophysics + amyloid biochemistry: 2+ disciplinary boundaries. Cross-domain bonus applied: +0.5 |
| **Composite** | | **7.35** | |

---

### Hypothesis: C2-H3 -- Cooling-Rate-Dependent Fibril Polymorph Selection in Ab42/Insulin via Eigenmode Branching

Note: Cycle2-hypotheses.md H7 refines this to insulin at pH 2, addressing the critic concern that 50C may cause rapid Abeta42 aggregation. T_cross (45-55C) and three-arm design are retained.

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 7 | Critic confirmed NOVEL. Quantitative T_cross prediction with bootstrap confidence interval and the three-arm discriminant (eigenmode branching vs Ostwald ripening) are genuinely new experimental concepts. Connection between thermal history and fibril polymorphs has precedent (Petkova 2005 for Abeta40 with agitation) but the spectral eigenmode mechanism and quantitative switchover temperature are new. Docked from 8 because the phenomenological link (cooling rate to polymorph) was previously observed. |
| Mechanistic Specificity | 20% | 5 | Moderate. Specifies c_k(T) = <P(T)|v_k> eigenmode overlap as cooling-rate-dependent selector; T_cross where c_2 = c_3; bootstrap uncertainty propagation. Three-arm Arm C as Ostwald discriminant is clever. However, the critical mechanistic step -- how monomer MSM eigenmodes translate to fibril polymorph IDENTITY -- is absent. Critique correctly identifies: Chakraborty 2020 shows A* predicts aggregation RATE, not polymorph IDENTITY. The elongation phase (which dominates polymorph identity in most current models) is completely ignored. |
| Cross-field Distance | 10% | 7 | Crosses non-equilibrium statistical physics (Mpemba eigenmode branching) to soft matter and materials science (fibril polymorphism, cryo-EM, ssNMR) to protein biophysics (insulin self-assembly, MSM). Less extreme than C2-H1 but spans meaningful disciplinary distance. |
| Testability | 20% | 8 | Best testability of all 4 survivors. Highly specific: insulin 2 mg/mL at pH 2, three cooling arms (rapid quench, 0.1 C/min, 0.5 C/min), cryo-EM + FTIR + ssNMR polymorph characterization, T-scan from 45/50/55/60C. Clear falsification: if rapid quench and slow cool yield identical structures (cryo-EM RMSD < 3 Angstrom), hypothesis refuted. A lab with protein biochemistry + cryo-EM access could execute in ~12-18 months. Does not require specialized computational infrastructure. |
| Impact: Paradigm | 5% | 6 | Fibril polymorph control is a genuine open problem -- polymorphs correlate with disease subtype and propagation. If cooling-rate eigenmode branching determines polymorph identity, this would substantially reframe polymorph selection mechanisms. Competing explanation (Ostwald ripening) remains viable. |
| Impact: Translational | 5% | 6 | T_cross-guided temperature protocols could: (1) select specific polymorphs for structural studies; (2) screen cooling regimes for aggregation suppression; (3) inform manufacturing conditions for amyloid-based biomaterials. More concrete translational pathway than C2-H1/H2. |
| Groundedness | 20% | 5 | Critique: 3/6 grounded claims verified (50%), revised groundedness 5/10. Verified: Jimenez et al. 2002 PNAS 99:9196 (insulin polymorphs), Nielsen et al. 2001 Biochemistry 40:6036 (insulin kinetics), Klich et al. 2019 PRX (eigenmode framework). Unverified: PMID 37606329 (capsid assembly). Overclaimed: Chakraborty 2020 predicts rate not polymorph identity. Maps to integer 5 (MEDIUM). |
| **Composite (pre-bonus)** | | **6.30** | 0.20x7 + 0.20x5 + 0.10x7 + 0.20x8 + 0.05x6 + 0.05x6 + 0.20x5 = 1.40+1.00+0.70+1.60+0.30+0.30+1.00 |
| **Cross-domain bonus** | | **+0.50** | Crosses statistical physics + soft matter/materials science + protein biophysics: 2+ disciplinary boundaries. Cross-domain bonus applied: +0.5 |
| **Composite** | | **6.80** | |

---

### Hypothesis: C2-H5 -- Resource-Theoretic Mpemba Monotone Predicts Therapeutic Window for Aggregation Reversal

Note: No direct equivalent in cycle2-hypotheses.md. Session.json confirms builds_on: H4 (Inverse Mpemba Protocol) + E5-H4; bridge_mechanism: resource_theoretic_KL_divergence applied to therapeutic destabilization.

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|--------------|---------------|
| Novelty | 20% | 7 | Critic confirmed NOVEL. Using D_KL resource-theoretic monotone to identify a "therapeutic window" where partial destabilization creates a Mpemba-analogous shortcut to native fold has not been published. However, this hypothesis shares the exact same Summer et al. 2026 PRX resource-theoretic framework as C2-H1 (and the same hallucinated author attribution), significantly reducing its independent novelty contribution. |
| Mechanistic Specificity | 20% | 4 | Low specificity. States: destabilize protein to reach c_2 with D_KL(P_c2 || pi) < D_KL(P_native || pi), enabling Mpemba-faster relaxation to native fold. No specific molecules named. Denaturant titration to c_2=0 is flagged as "pure speculation" by the critic. The specific experimental quantity to target (which D_KL value constitutes the therapeutic window) is undefined. Conceptually interesting but lacks molecular-level specificity and an executable measurement protocol. |
| Cross-field Distance | 10% | 8 | Traverses: (1) non-equilibrium statistical physics (Mpemba), (2) quantum information resource theory (monotone framework), (3) protein biochemistry (aggregation-prone states), (4) pharmacology/drug development (therapeutic window concept). Application of physics resource theory to drug design is one of the most extreme disciplinary bridges in the session. |
| Testability | 20% | 3 | Practically unfalsifiable as stated. Critic: "no tool to target specific D_KL values." Denaturant titration changes protein stability but cannot be tuned to precise D_KL without a nonexistent measurement protocol. Hypothesis contradicts tafamidis (approved kinetic stabilizer for TTR amyloidosis) -- meaning it predicts benefit from the opposite of what clinically works. Markovian assumption violated by cellular chaperones restricts scope to artificial in vitro conditions. |
| Impact: Paradigm | 5% | 6 | The concept of using the Mpemba condition to achieve faster escape from aggregation-prone states would, if true, represent a conceptual reversal of the kinetic stabilizer paradigm. However, tafamidis contradicts this paradigm, making paradigm impact complex and contested. |
| Impact: Translational | 5% | 3 | Destabilization as therapeutic strategy is clinically counterintuitive and directly contradicted by the approved drug tafamidis. Translational pathway is highly speculative. |
| Groundedness | 20% | 4 | Critique: 2/5 grounded claims verified (40%), revised groundedness 4/10. CRITICAL: "Avanzini et al. 2026 PRX 16:011065" is hallucinated author attribution (same error as C2-H1 -- real paper: Summer et al. 2026 PRX). Markovian closed-system assumption violated by ATP-dependent chaperones. Destabilization prediction contradicts tafamidis clinical approval. Maps to integer 4 (LOW-MEDIUM). |
| **Composite (pre-bonus)** | | **4.85** | 0.20x7 + 0.20x4 + 0.10x8 + 0.20x3 + 0.05x6 + 0.05x3 + 0.20x4 = 1.40+0.80+0.80+0.60+0.30+0.15+0.80 |
| **Cross-domain bonus** | | **+0.50** | Crosses statistical physics + quantum information theory + protein biochemistry + pharmacology: 2+ disciplinary boundaries. Cross-domain bonus applied: +0.5 |
| **Composite** | | **5.35** | |

---

## Final Ranking Table

| Rank | ID | Title | Novelty | Mech.Spec | CrossFld | Testability | ImpactP | ImpactT | Grounds | Pre-bonus | Bonus | Composite | Verdict |
|------|----|-------|---------|-----------|----------|-------------|---------|---------|---------|-----------|-------|-----------|---------|
| 1 | C2-H2 | D_misfold/D_fold Bimodal Spectrum (Zwanzig-Kramers) | 7 | 8 | 7 | 7 | 6 | 5 | 6 | 6.85 | +0.5 | **7.35** | WOUNDED conf5 |
| 2 | C2-H1 | A* Population = Mpemba Overlap Coefficient (Resource-Theoretic D_KL) | 8 | 7 | 8 | 6 | 7 | 5 | 5 | 6.60 | +0.5 | **7.10** | WOUNDED conf5 |
| 3 | C2-H3 | Cooling-Rate Polymorph Selection via Eigenmode Branching (Insulin T_cross) | 7 | 5 | 7 | 8 | 6 | 6 | 5 | 6.30 | +0.5 | **6.80** | WOUNDED conf4 |
| 4 | C2-H5 | Resource-Theoretic Therapeutic Window for Aggregation Reversal | 7 | 4 | 8 | 3 | 6 | 3 | 4 | 4.85 | +0.5 | **5.35** | WOUNDED conf3 |

Score gap between rank 3 and rank 4 (6.80 to 5.35 = 1.45 points) is decisive. C2-H5 is a marginal survivor not recommended for evolution.

---

## Diversity Check

Top 3 under scrutiny: C2-H2, C2-H1, C2-H3

| Pair | Shared Bridge Mechanism? | Shared Subfield? | Same Prediction Type? | Verdict |
|------|--------------------------|------------------|----------------------|---------|
| C2-H2 x C2-H1 | NO: H2=D ratio to roughness (Zwanzig); H1=D_KL resource-theoretic unification | Partial: both use protein MSM to aggregation propensity | NO: H2=epsilon_misfold within kT range; H1=D_KL Spearman rho correlation | CONVERGENT but COMPLEMENTARY |
| C2-H2 x C2-H3 | NO: H2=roughness calibration; H3=cooling-rate eigenmode to polymorph | NO: H2=computational biophysics; H3=wet-lab polymorph | NO: H2=continuous correlation; H3=discrete polymorph outcome | DISTINCT |
| C2-H1 x C2-H3 | NO: H1=resource-theoretic D_KL; H3=T_cross eigenmode switching | NO: H1=aggregation propensity prediction; H3=polymorph identity | NO: H1=scalar predictor; H3=discrete material outcome | DISTINCT |

Analysis: C2-H2 and C2-H1 are CONVERGENT but COMPLEMENTARY -- distinct bridge mechanisms (measured D ratio vs resource-theoretic KL divergence), distinct quantitative predictions (roughness within kT range vs Spearman rho), distinct grounding literature (Yu 2015 force spectroscopy vs Summer 2026 resource theory). C2-H3 is genuinely distinct: different substrate (insulin), different output variable (discrete polymorph identity vs continuous aggregation propensity), different experimental approach (wet lab cooling protocol vs computational biophysics).

**Diversity verdict: PASS. No swap required.**

---

## Elo Tournament Sanity Check

N=4 survivors, 6 pairwise comparisons. Criterion: which hypothesis would a domain researcher want to test FIRST?

| Matchup | Winner | Reasoning |
|---------|--------|-----------|
| C2-H2 vs C2-H1 | **C2-H2** | C2-H2 has a concrete experimental anchor (Yu 2015 D ratio; measurable by force spectroscopy) and higher groundedness (6 vs 5). C2-H1 requires abstractly identifying A* states via clustering before any prediction -- an unverified computational step added to the front of the pipeline. |
| C2-H2 vs C2-H3 | **C2-H2** | C2-H2 offers mechanistic explanation spanning the full roughness to bimodality to aggregation hierarchy; C2-H3 predicts a phenotypic outcome (polymorph) without the critical elongation-step mechanism. H2 wins on theoretical depth and groundedness. |
| C2-H2 vs C2-H5 | **C2-H2** | Decisive. C2-H5 is practically unfalsifiable and contradicts tafamidis. No researcher would prefer C2-H5 first. |
| C2-H1 vs C2-H3 | **C2-H1** (narrow) | C2-H1 offers broader theoretical unification (D_KL scalar subsuming TANGO + Zyggregator + Mpemba index). C2-H3 is more immediately testable (wet lab vs computational). This is effectively a coin flip: a computational biophysicist picks C2-H1; an experimentalist picks C2-H3. |
| C2-H1 vs C2-H5 | **C2-H1** | C2-H1 has a defined MSM+D_KL test protocol; C2-H5 lacks a measurement protocol for its key parameter. Hallucinated citation in C2-H5 further disqualifies it. |
| C2-H3 vs C2-H5 | **C2-H3** | C2-H3 has a fully defined wet-lab protocol with clear falsification criteria. C2-H5 test protocol does not exist as stated. |

Elo win tallies:
- C2-H2: 3 wins (win rate 1.00) -> Elo rank 1
- C2-H1: 2 wins (win rate 0.67) -> Elo rank 2
- C2-H3: 1 win (win rate 0.33) -> Elo rank 3
- C2-H5: 0 wins (win rate 0.00) -> Elo rank 4

**Elo ranking: C2-H2 > C2-H1 > C2-H3 > C2-H5**
**Composite ranking: C2-H2 (7.35) > C2-H1 (7.10) > C2-H3 (6.80) > C2-H5 (5.35)**
**Verdict: Elo confirms linear ranking. Identical ordering across all 4 positions.**

Diagnostic note on C2-H1 vs C2-H3 (closest matchup, 0.30 composite gap, 1-win Elo margin): The Elo tournament captures a dimension the 6-dimension average underweights: time-to-first-experiment. C2-H3 wet-lab accessibility (no specialized MSM infrastructure required) would make it the first choice for most experimental protein biochemistry labs. The composite correctly prioritizes C2-H1 on theoretical impact (Novelty=8 vs 7, Paradigm Impact=7 vs 6). This divergence signal is informative for the Evolver: treat C2-H3 as the fast-start experimental hypothesis even if C2-H1 ranks higher theoretically.

---

## Cycle Comparison (Cycle 1 vs Cycle 2)

Important methodological note: Cycle 1 rankings used different weights (Novelty 15%, Cross-domain Creativity 15% as a separate sixth dimension). Cycle 2 uses canonical v5.2 (Novelty 20%, Cross-field Distance 10%). Direct score comparison is approximate.

Cycle 1 top scores (cycle 1 weights): H5=8.1, H1=7.5, H7=6.5, H3=6.4
Cycle 2 scores (canonical v5.2): C2-H2=7.35, C2-H1=7.10, C2-H3=6.80, C2-H5=5.35

Key observations:

1. Experimental grounding improved significantly. Cycle 2 top hypothesis (C2-H2, 7.35) anchors the theoretical framework to Yu 2015 measured D ratios and TANGO cross-validation. This is the pipeline working as intended.

2. Recurring hallucination crisis. Both C2-H1 and C2-H5 cite "Avanzini et al. 2026 PRX 16:011065" -- a fabricated author attribution for a real paper (Summer et al. 2026 PRX). Same error appearing in two independent hypotheses signals a persistent parametric error about this paper. Evolver must correct both.

3. C2-H3 polymorph selection (6.80) outperforms cycle 1 H7 prion strain hypothesis (6.5) by pivoting from computationally intractable PrP to experimentally accessible insulin system. The three-arm mechanism discrimination is a significant design improvement.

4. All 3 fresh cycle 2 hypotheses were killed (C2-H6, C2-H7, C2-H8). Iterated descendants of cycle 1 survivors outperformed completely fresh speculation.

5. C2-H5 (5.35) is the weakest survivor across both cycles: biologically contradicted (tafamidis works), unfalsifiable, hallucinated citation.

---

## Evolution Selection

Post-diversity-check selection (top 3):

| Priority | ID | Composite | Evolution directive |
|----------|----|-----------|---------------------|
| 1 | C2-H2 | 7.35 | Fix: verify PMID 41665928; clarify D ratio applies to native-fold proteins not IDPs; restrict epsilon_misfold claim to range not point estimate. Evolve: extend to direct measurement of epsilon_misfold via smFRET or AFM-SMFS to replace Yu 2015 dimer force-extension data. Anchor hypothesis for the mechanistic chain. |
| 2 | C2-H1 | 7.10 | Fix: correct Avanzini to Summer et al. 2026 PRX (Marvian and Goold as PIs); remove Fiedler partition claim or add explicit caveat that psi_2 must be independently validated; scope claims to misfolding propensity not aggregation rate. Evolve: derive D_KL directly from MSM eigendecomposition without assuming psi_2 separates native from aggregation-prone states. |
| 3 | C2-H3 | 6.80 | Fix: replace Chakraborty overclaim with weaker "monomer A* conformation predicts commitment toward aggregation-competent nucleus" (not polymorph identity); verify PMID 37606329. Evolve: add elongation-phase templating mechanism connecting eigenmode branching to polymorph propagation -- the critical missing mechanistic link. Fast-start experimental hypothesis. |

NOT recommended for evolution: C2-H5 (5.35). Unfalsifiable testability (3/10), hallucinated citation (same as C2-H1), contradicts tafamidis. Recommend dropping from evolution pool.

---

Ranker: Hypothesis Ranker v5.2 | Session 2026-03-28-scout-014 | Cycle 2 | 2026-03-28
