# Final Hypotheses — Session 014

**Session:** 2026-03-28-scout-014
**Target:** Mpemba Spectral Relaxation Theory x Amyloid Aggregation Vulnerability
**Quality Gate:** 1 PASS | 5 CONDITIONAL_PASS | 2 FAIL
**Novelty:** CONFIRMED NOVEL — zero published connections across 6 independent web searches

---

## PASS: H7 — Cooling-Rate-Dependent Fibril Polymorph Selection in Insulin

**QG Score: 7.5 | Confidence: 5/10 | Groundedness: 8/10**

### The Idea

Different cooling rates from elevated temperature produce different amyloid fibril polymorphs because thermal history determines which slow eigenmodes of the protein's conformational landscape are selectively populated. A three-arm experiment — fast quench, slow cool, intermediate rate — can distinguish this eigenmode mechanism from simple stochastic nucleation.

### Why It Matters

Fibril polymorphism is a fundamental open question in amyloid biology with direct implications for disease strain diversity and drug targeting. If cooling-rate-dependent polymorph selection is mediated by eigenmode branching, it provides the first quantitative, predictive framework for controlling polymorph outcomes.

### The Mechanism

The Mpemba effect in Markov chains (Klich et al. 2019) shows that different initial conditions produce different overlaps with the slowest-decaying eigenmodes. In an amyloidogenic protein MSM, if the two slowest eigenmodes (v_2, v_3) encode distinct polymorph precursor basins, then different cooling rates produce different overlap ratios a_2/a_3, directing monomer flux toward different polymorphs.

The key innovation is the **three-arm discriminant**: at intermediate cooling rates, stochastic nucleation predicts MIXED polymorphs, while eigenmode branching predicts a SPECIFIC polymorph. This cleanly separates the two mechanisms.

### The Prediction

- **T_cross = 45-55C (+/-5C):** A crossover temperature where the dominant polymorph switches, predictable from the MSM eigenspectrum before experiment.
- **Total fibril mass within 25%** across cooling rates (not a yield effect), but **polymorph fractions shift by >20%** (a structural effect).
- **Three-arm test:** Fast quench -> Type A; slow cool -> Type B; intermediate -> specific (eigenmode) or mixed (stochastic).

### How To Test It

1. Insulin at pH 2, 0.5 mg/mL, 20 mM HCl/KCl
2. Three cooling protocols from 65C to 37C: rapid quench (<2 min), slow cool (0.1C/min), intermediate (3C/min)
3. ThT fluorescence kinetics for 72h
4. Cryo-EM 2D classification for polymorph identification
5. FTIR amide I band decomposition and/or solid-state NMR for structural confirmation
6. n >= 10 replicates per arm; chi-squared test on polymorph frequencies
7. **Timeline: 2-3 months wet lab**

### Grounding

All 3 GROUNDED citations verified: Jimenez et al. 2002 (insulin fibril cryo-EM), Nielsen et al. 2001 (insulin fibrillation kinetics), Klich et al. 2019 (Mpemba eigenmode overlap). Zero citation errors.

### Counter-Evidence

- Polymorph selection may be determined by elongation-phase templating, not initial monomer ensemble
- Nucleation stochasticity may mask deterministic eigenmode effects
- pH, salt, and agitation are stronger polymorph determinants
- Only 1-2 dominant morphologies may be detectable in vitro

---

## CONDITIONAL PASS: H4 — Spectral Entropy Production Rate as Misfolding Diagnostic

**QG Score: 7.3 | Confidence: 4/10 | Groundedness: 7/10**

### The Idea

The Schnakenberg entropy production rate, computed along MSM trajectories, shows characteristic transient spikes when a protein visits misfolding intermediates. These "sigma-spikes" arise from the roughness asymmetry between folding and misfolding landscapes and can serve as a novel diagnostic to classify individual trajectories as folding or misfolding.

### Why It Matters

Current methods identify misfolded states after the fact (structural analysis). Sigma-spikes would provide an early-warning signal detectable along individual trajectories, enabling real-time classification of protein dynamics as normal folding vs. pathological misfolding.

### The Prediction

- **70% of trajectories reaching A* (aggregation-competent) states show sigma-spikes >3x baseline**
- **80% of native-folding trajectories are sigma-monotonic**
- Mann-Whitney U test distinguishes the two populations
- K(Abeta42) > K(Abeta40) for the Kreiss constant

### Conditions for Full PASS

1. Develop noise model distinguishing genuine sigma-spikes from MSM estimation artifacts
2. Clarify discrete-time to continuous-time conversion
3. Provide derivation for the 70%/80% thresholds

### Grounding

All 4 citations verified with zero errors: Schnakenberg 1976, Seifert 2012, Yu 2015, Zwanzig 1988. Best citation integrity among fresh cycle 2 hypotheses.

---

## CONDITIONAL PASS: H5 — Hierarchical Spectral Scoring with Zwanzig Roughness Calibration

**QG Score: 7.2 | Confidence: 5/10 | Groundedness: 8/10**

### The Idea

A three-level framework predicts amyloid aggregation vulnerability: (1) Zwanzig roughness epsilon predicts whether the MSM eigenspectrum is bimodal; (2) bimodality enables the Mpemba index to be defined; (3) the Mpemba index predicts aggregation propensity. The key innovation is calibration against Yu et al. 2015 experimentally measured D_misfold/D_fold ratio (~1000x) for PrP, yielding epsilon_misfold ~ 3.3 kT.

### Why It Matters

This is the most complete causal chain in the session, providing not just a predictor but a mechanistic explanation for why the predictor works. Cross-validation against existing tools (TANGO, CamSol) makes it scientifically productive even if only partially correct.

### The Prediction

- **Self-refuting range: rho = 0.4-0.7** between M_eff and experimental ThT half-times
- If rho > 0.9 (TANGO already captures everything) or rho < 0.4 (M_eff fails), hypothesis is refuted
- Where M_eff and TANGO disagree (>= 2/8 proteins), M_eff better matches ThT data

### Conditions for Full PASS

1. Correct Cohen citation metadata
2. Address force-spectroscopy-to-free-diffusion D ratio transferability
3. Define D_fold operationally for IDPs or restrict to structured proteins

### Grounding

Highest groundedness in the session. Core experimental anchor (Yu et al. 2015 measured D ratio) fully verified. Cohen citation metadata errors are documentation issues, not content fabrication.

---

## CONDITIONAL PASS: H2 — Mpemba-Guided Aggregation Inhibitor Design

**QG Score: 6.8 | Confidence: 4/10 | Groundedness: 7/10**

### The Idea

Small molecules that maximally reduce the overlap coefficient between the drug-bound conformational ensemble and the slowest misfolding eigenmode are optimal aggregation inhibitors. Tafamidis (approved TTR stabilizer) should retrospectively satisfy this criterion.

### Why It Matters

No existing drug design framework uses eigenmode overlap as a screening criterion. If validated, this provides a genuinely new computational drug design paradigm for amyloid diseases.

### The Prediction

- Retrospective: tafamidis reduces TTR eigenmode overlap more than non-inhibitor controls (enrichment >2)
- Known inhibitors cluster at high eigenmode-overlap-disruption values
- If overlap disruption does not correlate with inhibitory activity (rho < 0.3), hypothesis refuted

### Conditions for Full PASS

1. Pivot primary system from Abeta42 (IDP, no pockets) to TTR (structured, known binding site)
2. Address eigenmode landscape change upon ligand binding
3. Replace dissimilar negative controls with matched non-inhibitors

### Grounding

Perfect citation accuracy: 4/4 verified with zero errors (Klich 2019, Bowman & Geissler 2012, Bulawa 2012, Husic & Pande 2018).

---

## CONDITIONAL PASS: H8 — Chaperone-Modulated Mpemba Index (Hsp70 as Biological Mpemba Protocol)

**QG Score: 6.5 | Confidence: 4/10 | Groundedness: 6/10**

### The Idea

Hsp70 chaperone binding sites on amyloidogenic proteins preferentially overlap with high-|v_slow| microstates, constituting a biological Mpemba protocol. Age-dependent decline in chaperone capacity is a "weakening Mpemba protocol" that explains late-onset aggregation diseases.

### Why It Matters

This reframes chaperone biology through the lens of non-equilibrium statistical mechanics. If the co-localization prediction holds, it provides a quantitative link between chaperone function and spectral protein dynamics.

### The Prediction

- >70% of Hsp70 binding sites co-localize with high-|v_slow| microstates
- Mpemba index decreases 3-fold in holo vs apo MSM
- If co-localization <30%, hypothesis refuted

### Conditions for Full PASS

1. Redirect from Abeta42 to tau/alpha-synuclein (documented Hsp70 monomer interaction)
2. Address holo MSM mathematical limitations
3. Clarify monomer vs. oligomer targeting

### Grounding

All 4 citations verified with zero errors (Rudiger 1997, Powers 2009, Taipale 2010, Mayer & Bukau 2005).

---

## CONDITIONAL PASS: H3 — Evolutionary Mpemba Tradeoff

**QG Score: 5.6 | Confidence: 3/10 | Groundedness: 6/10**

### The Idea

Amyloidogenic sequences persist evolutionarily because high Mpemba index enables rapid native folding (fitness advantage) at the cost of deep misfolding traps (disease vulnerability). This dual-use metric explains why aggregation-prone proteins are often highly expressed.

### Why It Matters

If correct, this connects non-equilibrium physics to evolutionary biology, providing a mechanistic explanation for the evolutionary persistence of disease-associated proteins.

### Critical Limitation

**MUST be restricted to non-IDP amyloid proteins** (TTR, lysozyme, beta-2-microglobulin). IDP folding rate is undefined, making the prediction untestable for Abeta42, alpha-synuclein, and tau — the most clinically relevant amyloidogenic proteins.

### Conditions for Full PASS

1. Restrict scope to non-IDP amyloid proteins
2. Add partial correlation controlling for contact order (Plaxco 1998)
3. Acknowledge exclusion of IDP-mediated diseases

### Grounding

All 3 citations verified. No errors (Drummond & Wilke 2008, Tartaglia 2007, Ciryam 2017).

---

## FAILED Hypotheses (not included in final set)

### H1: Resource-Theoretic Mpemba Vulnerability Score — FAIL
**Reason:** Fabricated citation. "Avanzini et al. 2026 PRX 16:011065" — the paper exists but authors are Summer, Moroder, Bettmann, Turkeshi, Marvian, Goold. Avanzini does not appear on the paper. Additionally, D_KL formula is mathematically wrong (chi-squared divergence, not KL divergence far from equilibrium). Concept is powerful and can be rebuilt on correct foundations.

### H6: Tau PTM Biomarker — FAIL
**Reason:** Two fatal flaws: (1) Citation misattribution (Wesseling vs Arakhamia at Cell 180:633); (2) T217 at position 217 is OUTSIDE the K18 fragment (residues 244-372) — the PTM site cannot perturb the simulated domain. Anatomically impossible mechanism.

---

## Session Summary

This session produced **6 quality-cleared hypotheses** from a genuinely novel cross-domain bridge (Mpemba spectral relaxation theory x amyloid aggregation vulnerability). The bridge is confirmed novel across 6 independent web searches with zero prior publications.

**Top 3 framework:**
1. **H7 (PASS):** Experimental validation via polymorph selection — near-term testable
2. **H4 (CONDITIONAL):** Diagnostic tool via entropy production signatures — computational
3. **H5 (CONDITIONAL):** Quantitative prediction framework — most complete causal chain

These three hypotheses are complementary: H7 provides the fastest path to experimental data, H4 provides a novel diagnostic method, and H5 provides the theoretical calibration framework. Together they form a coherent research program for the Mpemba-amyloid bridge.
