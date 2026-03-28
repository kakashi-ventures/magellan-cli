# Scout Targets — Session 015 (2026-03-28)

**Creativity constraint**: Bridge physical sciences and life sciences
**Strategy diversification**: 5 strategies across 6 targets; 3 under-tested (serendipity 0, failed_paradigm_recycling 0, scale_bridging 1)
**Banned strategies**: converging_vocabularies (S017), anomaly_hunting (S018)

---

## T1: Percolation Threshold Theory × T Cell Infiltration in Solid Tumors

**Strategy**: structural_isomorphism | **Score**: 8.5 | **Disjointness**: DISJOINT (verified S014, 0 PubMed cross-field papers)
**Disciplinary distance**: 2.5 (statistical mechanics → tumor immunology)

**Field A**: Statistical mechanics — bond percolation theory (physics)
**Field C**: Tumor immunology — ECM-mediated immune exclusion (medicine)

**Bridge concepts**:
- LOX-mediated collagen crosslink density as bond occupation probability p in a lattice percolation model
- Percolation threshold p_c as the critical ECM density above which T cells cannot form a connected infiltration path (immune exclusion threshold)
- Correlation length ξ ~ |p - p_c|^(-ν) predicts the spatial scale of T cell clustering near the exclusion threshold
- Finite-size scaling of T cell mean squared displacement (MSD) as a diagnostic for proximity to p_c
- Universality class predictions: critical exponents (ν ≈ 0.88 in 3D) are independent of collagen specifics — testable across tumor types

**Why this target**: Highest-priority item in deferred queue (Scout score 8, S014). Statistical physics provides exact quantitative predictions (threshold, exponents, scaling functions) that are directly measurable by multiplex IHC + spatial statistics on tumor sections. LOX is a druggable target (BAPN inhibitor), enabling experimental manipulation of the control parameter p.

**Kill vector pre-check**: No energy scale mismatch — percolation is geometric/topological, not force-dependent. Primary risk: biological complexity (T cell motility is active, not passive diffusion through a static lattice). Mitigation: use effective medium theory for active particles on disordered lattices.

**Source**: Deferred queue T1 from S014. Originally anomaly_hunting; reframed as structural_isomorphism (both fields use lattice connectivity mathematics independently).

---

## T2: Acoustic Filter-Bank Theory × Plant Bioacoustics

**Strategy**: serendipity (0 primary sessions — EXPLORATION SLOT) | **Score**: 7.0 | **Disjointness**: DISJOINT (est.)
**Disciplinary distance**: 2.5 (acoustic engineering → plant biology)

**Field A**: Acoustic engineering/physics — matched-filter detection, parallel filter-bank theory
**Field C**: Plant biology — ultrasonic emission detection, mechanosensitive channel biology

**Bridge concepts**:
- Trichome arrays as tuned mechanical resonators — individual trichomes have calculable resonance frequencies based on length/stiffness (Euler-Bernoulli beam theory)
- MSL (MscS-Like) and MCA (Mid1-Complementing Activity) channel gating thresholds could be frequency-selective if coupled to resonant structures
- Leaf surface microstructure (trichome spacing, density, height distribution) as a parallel filter-bank array — each trichome "tuned" to a different frequency band
- Acoustic impedance matching between air and plant tissue via trichome geometry (quarter-wave transformer analogy)
- Testable prediction: trichome-bearing species show frequency-selective responses to airborne vibrations; glabrous mutants lose selectivity

**Why this target**: Serendipity strategy is completely untested (0 sessions). Plant bioacoustics is a young, high-novelty field (Khait et al. 2023 Cell — plants emit ultrasonic clicks under stress). The acoustic engineering framework provides quantitative design principles for biological "receivers." High creativity value.

**Kill vector pre-check**: Primary risk — trichome resonance frequencies may not match biologically relevant acoustic signals (plant stress emissions are 20-100 kHz; trichome resonance depends on geometry). Need back-of-envelope calculation: f_res ~ (1/2π)√(EI/ρAL⁴) for cantilever beam. If f_res is orders of magnitude away from 20-100 kHz, bridge fails.

**Source**: Deferred queue T2 from S014.

---

## T3: Classical Nucleation Theory × Ferroptosis Labile Iron Pool Dynamics

**Strategy**: scale_bridging (1 primary session — exploration eligible) | **Score**: 7.0 | **Disjointness**: DISJOINT
**Disciplinary distance**: 2.0 (thermodynamics/kinetics → cell death biology)

**Field A**: Physics — classical nucleation theory (CNT), heterogeneous nucleation kinetics
**Field C**: Cell death biology — ferroptosis, labile iron pool (LIP) regulation

**Bridge concepts**:
- Ferritin iron core (ferrihydrite nanoparticle, ~6 nm, up to 4500 Fe atoms) dissolution as reverse heterogeneous nucleation — the core dissolves when the "dissolution nucleus" reaches critical size
- Critical nucleus size a* = 2γV_m/(kT·ln(S)) where S = supersaturation ratio of Fe²⁺ in the LIP relative to ferrihydrite solubility
- Nucleation rate J = A·exp(−ΔG*/kT) predicts THRESHOLD behavior: LIP burst is not gradual but switches on above a critical ferritin degradation rate
- Ferritinophagy (NCOA4-mediated) as the kinetic driver — autophagy rate controls the supersaturation parameter S
- Testable prediction: LIP accumulation shows a sharp nucleation-like threshold as ferritinophagy rate increases, not a linear dose-response

**Why this target**: CNT provides exact mathematical predictions for the threshold behavior of iron release from ferritin — a phenomenon currently modeled only phenomenologically. The framework explains WHY ferroptosis has a threshold (nucleation barrier) rather than being proportional to GPX4 inhibition.

**Kill vector pre-check**: Primary risk — ferritin dissolution may not proceed by classical nucleation (it could be enzymatic/reductive dissolution following different kinetics). Mitigation: CNT applies to ANY dissolution process with a free energy barrier; the mathematical form is general even if the molecular mechanism differs.

**Domain saturation flag**: 3rd ferroptosis session (S005, S006 prior). New bridge (nucleation physics) is distinct from previous bridges (serpentinization geochemistry in S005, quorum sensing metabolites in S006).

**Source**: Deferred queue from S012.

---

## T4: Linear Viscoelastic Creep Theory × Biofilm Antibiotic Tolerance

**Strategy**: failed_paradigm_recycling (0 primary sessions — EXPLORATION SLOT) | **Score**: 7.5 | **Disjointness**: DISJOINT (est.)
**Disciplinary distance**: 2.0 (materials science/rheology → microbiology)

**Field A**: Materials science — linear viscoelastic theory (Maxwell, Kelvin-Voigt, standard linear solid models)
**Field C**: Microbiology — biofilm antibiotic tolerance, persister cell formation

**Bridge concepts**:
- Creep compliance J(t) = J₀ + J₁(1 − e^(−t/τ)) + t/η as quantitative model for antibiotic penetration kinetics through biofilm EPS matrix
- Retardation time τ of the EPS polymer network determines the timescale over which antibiotic concentration equilibrates across the biofilm — predicts a "pharmacokinetic shadow" where inner bacteria experience delayed, attenuated drug exposure
- Stress relaxation modulus G(t) = G₀·e^(−t/τ) predicts post-antibiotic recovery rate — biofilms with shorter τ recover faster (more liquid-like EPS)
- Storage modulus G' (elastic) vs loss modulus G" (viscous) ratio at antibiotic-relevant timescales predicts whether the biofilm responds as solid-like barrier (G' >> G") or liquid-like permeable matrix (G" >> G')
- Testable prediction: MIC of biofilm-embedded bacteria correlates with EPS G'/G" crossover frequency, not with planktonic MIC

**Failed paradigm rationale**: Linear viscoelastic models were THE framework for biological cell mechanics (Fung 1981 "Biomechanics," Thoumine & Ott 1997). They were progressively ABANDONED for eukaryotic cells as evidence accumulated that cells are active matter — cytoskeletal motors, fluidization responses, and strain-stiffening make passive viscoelastic models fundamentally inadequate. However, biofilm EPS matrices are PASSIVE crosslinked polymer gels (polysaccharides, eDNA, proteins) WITHOUT molecular motors. The viscoelastic framework that failed for cells should be precisely correct for biofilms.

**Kill vector pre-check**: Primary risk — biofilm EPS may be nonlinear viscoelastic (strain-stiffening, shear-thinning) rather than linear. Mitigation: linear viscoelasticity is valid at small strains; antibiotic diffusion is a small-perturbation process that doesn't deform the matrix. Also risk of PARTIALLY_EXPLORED — biofilm rheology exists (Stoodley 1999, Peterson 2015). Must verify that SPECIFIC bridge (rheological parameters → MIC prediction) is novel.

**Source**: New target, not from deferred queue.

---

## T5: Griffith Fracture Mechanics × Bacterial Cell Wall Failure Under β-Lactam Stress

**Strategy**: structural_isomorphism | **Score**: 7.5 | **Disjointness**: DISJOINT (est.)
**Disciplinary distance**: 2.0 (engineering mechanics → microbiology)

**Field A**: Materials science/engineering — Griffith fracture mechanics, stress intensity factors, energy release rate
**Field C**: Microbiology — peptidoglycan mechanics, β-lactam mechanism of action, cell lysis

**Bridge concepts**:
- Peptidoglycan (PG) mesh as a pressurized thin-walled vessel (turgor pressure P = 2-5 atm, wall thickness t ~ 4-8 nm for Gram-negative)
- β-Lactam antibiotics inhibit transpeptidases (PBPs), creating crosslink defects = "cracks" in the PG mesh
- Griffith criterion: crack propagates when energy release rate G = πσ²a/E ≥ 2γ_s (surface energy of PG bond breakage)
- Stress intensity factor K_I = σ√(πa) where σ = PR/t (hoop stress from turgor), a = defect cluster size
- Critical defect size a_c = (K_Ic)²/(πσ²) — predicts the NUMBER of adjacent crosslink defects required for catastrophic lysis
- Subcritical crack growth (stress corrosion cracking analog): autolysins at crack tips accelerate local PG hydrolysis, extending defects below K_Ic — explains why lysis is delayed, not instantaneous, after β-lactam exposure
- Testable prediction: At fixed PBP inhibition fraction, cells lyse when they accumulate a critical-sized contiguous defect patch (not when total defect fraction exceeds a threshold). Predicts stochastic lysis timing distributed as extreme value (weakest link) rather than normal distribution.

**Why this target**: Existing cell wall mechanical models (Furchtgott 2011, Huang 2008) use continuum elasticity — they predict uniform thinning and gradual weakening. Fracture mechanics predicts a QUALITATIVELY DIFFERENT failure mode: crack nucleation, propagation, and catastrophic rupture from the weakest point. These make different experimental predictions about lysis dynamics (gradual vs sudden), spatial pattern (uniform vs localized), and statistics (normal vs extreme value).

**Kill vector pre-check**: Primary risk — PG mesh (~2 nm glycan strand spacing) may be too small for continuum fracture mechanics to apply (discrete lattice effects dominate). Mitigation: lattice fracture models exist (discrete counterpart of Griffith). The mathematical predictions (critical defect size, weakest-link statistics) hold for lattice fracture too.

**Source**: New target, not from deferred queue.

---

## T6: Electrochemical Impedance Spectroscopy × Gut Microbiome Metabolic State

**Strategy**: tool_repurposing | **Score**: 7.0 | **Disjointness**: DISJOINT (est.)
**Disciplinary distance**: 2.0 (electrochemistry → gut microbiology)

**Field A**: Electrochemistry (chemistry/physics) — electrochemical impedance spectroscopy (EIS), equivalent circuit modeling
**Field C**: Gut microbiology — microbiome metabolic activity, dysbiosis detection

**Bridge concepts**:
- EIS frequency sweep (mHz to MHz) as real-time metabolic fingerprint of microbial communities — each metabolic pathway has a characteristic charge transfer timescale
- Charge transfer resistance R_ct reflects the rate of microbial extracellular electron transfer (EET) — anaerobes (Bacteroidetes, Firmicutes) produce different redox-active metabolites (SCFAs, H₂S, indoles) with distinct electrochemical signatures
- Nyquist plot topology (semicircle diameter, Warburg tail slope) changes as community composition shifts — healthy vs dysbiotic communities should have distinct impedance spectra
- Warburg impedance element captures diffusion-limited metabolite transport in the mucus layer — mucus degradation (dysbiosis marker) would shift the Warburg coefficient
- Testable prediction: EIS equivalent circuit parameters (R_ct, C_dl, Z_W) measured in a colonic environment change systematically with known dysbiosis inducers (antibiotics, dietary changes) before 16S rRNA composition changes are detectable

**Why this target**: No real-time functional monitoring tool exists for gut microbiome metabolic state. Current methods (16S, metagenomics, metabolomics) are snapshot-based and compositional, not functional. EIS provides continuous, real-time electrochemical readout. Same-class tool transfer (electrochemistry used in both corrosion science and biological sensing).

**Kill vector pre-check**: Primary risk — practical feasibility of EIS electrodes in gut environment (biofouling, reference electrode stability, mucosal adhesion). Mitigation: implantable EIS sensors exist for glucose monitoring (CGMs use related technology). The physics is sound; engineering challenges are addressable.

**Source**: Deferred queue from S013.

---

## Summary Table

| # | Target | Strategy | Score | Disjointness | Distance | Source |
|---|--------|----------|-------|-------------|----------|--------|
| T1 | Percolation × T cell infiltration | structural_isomorphism | 8.5 | DISJOINT (verified) | 2.5 | Deferred (S014) |
| T2 | Acoustic filter-bank × Plant bioacoustics | serendipity (0 sessions) | 7.0 | DISJOINT (est.) | 2.5 | Deferred (S014) |
| T3 | CNT × Ferroptosis LIP | scale_bridging (1 session) | 7.0 | DISJOINT | 2.0 | Deferred (S012) |
| T4 | Viscoelastic creep × Biofilm tolerance | failed_paradigm_recycling (0 sessions) | 7.5 | DISJOINT (est.) | 2.0 | New |
| T5 | Griffith fracture × PG wall failure | structural_isomorphism | 7.5 | DISJOINT (est.) | 2.0 | New |
| T6 | EIS × Gut microbiome metabolic state | tool_repurposing | 7.0 | DISJOINT (est.) | 2.0 | Deferred (S013) |

**Strategy distribution**: 5 strategies, 3 under-tested (serendipity, failed_paradigm_recycling, scale_bridging)
**Recommendation**: T1 (Percolation) for highest expected quality; T2 (Acoustic) or T4 (Viscoelastic) for exploration slot value.
