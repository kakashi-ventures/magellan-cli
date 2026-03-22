# Final Hypotheses — Session session-20260322-154446
## Volcanic Glass Dissolution Kinetics x Pharmaceutical ASD Dissolution
## Quality Gate: 5 CONDITIONAL_PASS, 1 FAIL

---

## H1.1-E: TST Dissolution Kinetics in the Surface-Reaction-Limited Regime of Low Drug-Loading ASDs

VERDICT: CONDITIONAL_PASS | Rubric: 8/10 | Groundedness: 7/10

CONNECTION: Geochemical TST rate law >> Damkohler regime criterion >> ASD dissolution kinetic model
CONFIDENCE: 5/10 -- Novel cross-field application with no direct experimental precedent
NOVELTY: Novel -- 0 prior applications of TST to pharmaceutical ASD dissolution (web-verified)
GROUNDEDNESS: 7 -- Strong overall with one Ea misattribution requiring correction
IMPACT IF TRUE: Transformative -- first composition-based predictive dissolution model for ASDs

### MECHANISM

The Transition State Theory (TST) dissolution rate law from geochemistry (Lasaga 1981) provides a quantitative, predictive framework for ASD dissolution in the surface-reaction-limited regime:

r = k+ * exp(-Ea/RT) * (1 - exp(-DeltaG_r / sigma*RT))

The key advance: a Damkohler number criterion (Da = k+ * h_diff / D_drug) identifies WHEN TST applies:
- Da << 1: Surface-reaction-limited (TST applicable). Occurs in low drug-loading ASDs (<20 wt%) where the rate-limiting step is drug-polymer H-bond disruption at the ASD-water interface.
- Da >> 1: Diffusion-limited (Noyes-Whitney applicable). Occurs at high drug loadings (>30 wt%).

The rate-limiting molecular event: disruption of drug-polymer H-bond network at the solid-liquid interface. Estimated Ea = 65-85 kJ/mol (analogous to Si-O hydrolysis activation energy scale). The Temkin coefficient sigma = 0.30-0.40 for indomethacin-HPMCAS, derived from ~3 H-bonds per drug molecule. [GROUNDED: TST framework (Lasaga 1981), basaltic glass validation (Gislason & Oelkers 2003 GCA 67:3817), Damkohler number criterion standard chemical engineering]

### KEY PREDICTIONS
- 10 wt% indomethacin-HPMCAS: Ea = 65-80 kJ/mol (surface-reaction-limited)
- 40 wt% indomethacin-HPMCAS: Ea = 15-30 kJ/mol (diffusion-limited)
- Crossover at ~25 wt% drug loading (Da approximately 1)
- sigma = 0.30-0.40 for indomethacin-HPMCAS
- TST curve fit R2 > 0.95 for 10% loading at varied C_drug/C_am ratios

### HARD FALSIFICATION
Ea < 35 kJ/mol at 10% drug loading conclusively kills the hypothesis.

### HOW TO TEST
1. Prepare indomethacin-HPMCAS ASDs at 10%, 20%, 40% drug loading by spray drying
2. Measure initial dissolution rate at 25C, 30C, 37C using USP Apparatus II
3. Extract Ea from Arrhenius plot (ln(k+) vs 1/T)
4. At confirmed surface-reaction-limited loading: fit TST profile with sigma as single parameter
5. Effort: 2-3 months, ~$20K

### CORRECTION NEEDED
Ea = 60-80 kJ/mol must be reattributed from Gislason & Oelkers 2003 (which reports 25.5 kJ/mol) to ab initio Si-O hydrolysis studies (Criscenti et al. 2006).

---

## H1.2-E: Grambow Rate Law 2 Predicts Competitive Passivation-Erosion Kinetics and Regime Switching in ASD Dissolution

VERDICT: CONDITIONAL_PASS | Rubric: 8/10 | Groundedness: 7/10

CONNECTION: Nuclear waste glass Rate Law 2 >> competitive passivation-erosion ODE >> ASD dissolution regime switching
CONFIDENCE: 4/10 -- Novel framework, citation error corrected, polymer transport physics differ
NOVELTY: Novel -- Grambow-Muller 2001 RL-2 never applied to pharmaceutical systems (web-verified)
GROUNDEDNESS: 7 -- All major citations verified (Gin et al. 2015 Nature Communications, Grambow-Muller 2001)
IMPACT IF TRUE: High -- would explain poorly-understood transition from congruent to incongruent ASD dissolution

### MECHANISM

The competitive passivation-erosion ODE from nuclear waste borosilicate glass dissolution:

dh/dt = alpha * D_drug / h - beta * k_erase

predicts three dissolution regimes based on polymer molecular weight:
1. Parabolic (high MW, G << 1): passivation dominates, sqrt(t) kinetics
2. Zero-order (intermediate MW, G approximately 1): steady-state layer thickness
3. Erosion-controlled (low MW, G >> 1): faster-than-linear release

Where k_erase = k0 * MW^(-3.4) from reptation theory (Doi-Edwards). The dimensionless ratio G = beta*k_erase*h_ss / (alpha*D_drug) determines the regime.

### KEY PREDICTIONS
- HPMCAS-H (330 kDa): parabolic release (R2 > 0.92 for sqrt(t) fit)
- HPMCAS-M (78 kDa): zero-order release after initial burst
- HPMCAS-L (11 kDa): erosion-controlled, faster-than-linear
- k_erase scales as MW^(-3.4) across three HPMCAS grades (within factor of 3)
- PVP-VA negative control: no MW-dependent regime switching

### HOW TO TEST
1. Prepare indomethacin ASDs with HPMCAS-H, -M, -L and PVP-VA control
2. Measure dissolution profiles and surface layer thickness (confocal Raman)
3. Independently measure k_erase via QCM-D
4. Effort: 4-6 months, ~$40K

---

## H1.6-E: Dual Saturation Index Competition Predicts LLPS vs. Crystallization Pathway Switching in Ionizable Drug ASD Dissolution

VERDICT: CONDITIONAL_PASS | Rubric: 8/10 | Groundedness: 7/10

CONNECTION: Geochemical multi-phase speciation >> simultaneous SI computation >> ASD precipitation pathway prediction
CONFIDENCE: 4/10 -- Novel dual-SI approach, partially explored prior art (MFAD 2019)
NOVELTY: Novel -- dual-SI simultaneous computation for LLPS vs crystallization sequence prediction is new
GROUNDEDNESS: 7 -- Geochemical SI framework, LLPS (Indulkar et al. 2019), Ostwald Rule all verified
IMPACT IF TRUE: High -- would enable rational design of ionizable drug ASDs with optimized LLPS/crystallization behavior

### MECHANISM

Unlike MFAD (Schall, Capellades & Myerson, CrystEngComm 2019), which tracks only crystalline supersaturation, the dual-SI framework computes:
- SI_LLPS = log(a_drug / a_LLPS,eq) -- saturation with respect to amorphous drug-rich nanodroplets
- SI_cryst = log(a_drug / a_cryst,eq) -- saturation with respect to crystalline drug

Using Ostwald Rule of Stages: the phase with HIGHEST SI nucleates first. For ionizable drugs, the relative SI values are pH-dependent because ionization changes activity coefficients differently for LLPS and crystalline phases.

Activity coefficients computed via PC-SAFT (Perturbed-Chain Statistical Associating Fluid Theory).

### KEY PREDICTIONS
- Posaconazole pH 6.8: LLPS precedes crystallization by >=15 min
- Posaconazole pH 1.2: neither LLPS nor crystallization at therapeutic concentrations
- Posaconazole pH 4-5: LLPS and crystallization concurrent (<5 min lag)
- Correct sequence prediction in >=9/12 conditions (3 drugs x 4 pH values)

### HOW TO TEST
1. Prepare supersaturated solutions of 3 ionizable drugs at 4 pH values
2. Monitor with simultaneous DLS (LLPS) and PXRD/Raman (crystallization)
3. Record onset times for both events
4. Compare with PC-SAFT-predicted SI values
5. Effort: 6-8 months, ~$50K

---

## H2.4-E: Nucleation-Controlled Ostwald Ripening with Polymer Inhibition Predicts ASD Phase Evolution Trajectories

VERDICT: CONDITIONAL_PASS | Rubric: 7/10 | Groundedness: 7/10

CONNECTION: Geochemical competitive nucleation-growth >> selective polymer crystallization inhibition >> ASD long-term stability
CONFIDENCE: 6/10 -- Novel framework, key bridge claim unverified
NOVELTY: Novel -- competitive nucleation-growth with selective polymer inhibition not modeled for ASD systems
GROUNDEDNESS: 7 -- Classical nucleation theory and Ostwald ripening well-established; selective inhibition claim unverified
IMPACT IF TRUE: Transformative -- would enable prediction of long-term ASD shelf-life from short-term measurements

### MECHANISM

Polymer molecules preferentially adsorb to crystalline nuclei surfaces (via H-bonding to lattice planes) but not to LLPS droplet surfaces (due to conformational entropy penalty at liquid-liquid interface). This creates selective nucleation inhibition:

J_cryst = A_cryst * exp(-DeltaG*_cryst / kT) * (1 - I_polymer)

Three phase evolution regimes:
1. LLPS-dominated (high polymer, low supersaturation)
2. Competition zone (intermediate)
3. Crystallization-dominated (low polymer, high supersaturation)

### HOW TO TEST
1. Time-resolved DLS + optical microscopy at varying polymer concentrations
2. Measure k_ads via crystallization inhibition assays
3. Effort: 6+ months, ~$50K
4. NOTE: Overlap with H1.6-E; consider testing both frameworks simultaneously

---

## H2.1-E: Pressure-Fracture Competition Regime Map for ASD Manufacturing Optimization

VERDICT: CONDITIONAL_PASS | Rubric: 6/10 | Groundedness: 5/10

CONNECTION: Geochemical activation volume >> pressure-dependent dissolution kinetics >> ASD manufacturing optimization
CONFIDENCE: 6/10 -- Novel but quantitatively marginal at pharmaceutical pressures
NOVELTY: Novel -- activation volume framework never applied to pharmaceutical manufacturing
GROUNDEDNESS: 5 -- Activation volume theory solid but practical effect size questionable
IMPACT IF TRUE: High -- would optimize ASD tablet compression conditions

### MECHANISM

Dimensionless pressure competition number Pc predicts regime:
- Pc << 1: Activation volume kinetics dominate (pressure speeds dissolution via TST)
- Pc >> 1: Fracture mechanics dominate (pressure creates new surface area)
- Pc approximately 1: Competition zone (both effects contribute)

### CAUTION
Activation volume effect at pharmaceutical pressures (10-200 MPa) is only ~17%, potentially overwhelmed by mechanical effects. Pharmaceutical literature shows IDR unchanged below 125 MPa. This hypothesis has the weakest practical impact of the five.

### HOW TO TEST
1. Compress ASDs at 10, 50, 100, 200, 300 MPa
2. Measure dissolution rate and particle size distribution
3. Determine Pc crossover
4. Effort: 3-4 months, ~$30K
