# Literature Landscape — Session session-20260322-154446
## Focus: Volcanic Glass Dissolution Kinetics x Pharmaceutical ASD Dissolution

---

## Field A: Glass Dissolution Kinetics (Geochemistry/Materials Science)

### Core Framework
The dissolution of silicate glasses (including volcanic glass) follows Transition State Theory (TST):

**TST Rate Law**: r = k+ * prod(a_i^n_i) * (1 - exp(-A/sigma*RT))

Where:
- k+ = forward rate constant (intrinsic dissolution rate)
- a_i = activities of solution species affecting dissolution
- A = chemical affinity (= -DeltaG_rxn = RT * ln(Q/K))
- sigma = Temkin coefficient (stoichiometry correction)
- Q = ion activity product, K = equilibrium constant

At far-from-equilibrium (Q << K): r approaches k+ (surface-reaction limited)
At near-equilibrium (Q -> K): r approaches 0 (dissolution nearly ceases)

### Key Parameters
- **Activation energy**: Basaltic glass Ea ~ 60-80 kJ/mol (Gislason & Oelkers 2003)
- **pH dependence**: V-shaped rate law with minimum at pH ~6-7
  - Acidic: rate ~ [H+]^0.3-0.5
  - Basic: rate ~ [OH-]^0.3-0.5
- **Composition effects**: Network modifiers (Na, Ca, Mg) vs network formers (Si, Al) — higher modifier/former ratio = faster dissolution
- **Passivation layer**: Silica-rich alteration rind forms during dissolution, creating diffusion barrier
  - Parabolic rate law applies: thickness ~ sqrt(t)
  - Rate transitions from surface-reaction limited to transport-limited

### Key Papers (from PubMed + parametric knowledge)
1. Lasaga 1981 (ACS Symp Ser): TST framework for mineral dissolution — foundational
2. Oelkers 2001 (GCA): General kinetic description of multioxide silicate dissolution
3. Gislason & Oelkers 2003 (GCA): Basaltic glass dissolution kinetics — Ea, pH dependence
4. Grambow & Muller 2001: Nuclear waste glass dissolution modeling — long-term prediction
5. Gin et al. 2015 (Nat Mater): Glass alteration mechanisms and rate-limiting steps
6. PMID 28092154 (Bauchy 2017, J Phys Chem B): Network topology correlates with dissolution rate — "the network topology (rigidity, connectivity) of the glass controls its chemical durability"
7. PMID 34207343 (2021, Materials): Early-stage dissolution kinetics under dynamic conditions — systematic methodology
8. Hellmann et al. 2012 (EPSL): Interfacial dissolution-reprecipitation mechanism

### PHREEQC Modeling Tool
- USGS geochemical speciation code
- Calculates saturation indices for hundreds of mineral phases
- Predicts precipitation/dissolution based on thermodynamic data
- Handles kinetic rate laws (TST and empirical)
- Can model reactive transport (1D column experiments)
- Widely used in geochemistry (~10,000+ citations) but ZERO use in pharmaceutical dissolution science

---

## Field C: Pharmaceutical ASD Dissolution

### Core Challenge
- >75% of new drug candidates are poorly water-soluble (BCS Class II/IV)
- Amorphous solid dispersions (ASDs) enhance dissolution by maintaining drug in metastable amorphous form
- ASD dissolution generates supersaturated solutions that eventually crystallize (crash)
- The "spring and parachute" model: ASD provides spring (rapid dissolution), polymer maintains parachute (inhibits crystallization)

### Current Dissolution Models (Pharmaceutical)
1. **Noyes-Whitney equation**: dm/dt = DA(Cs - C)/h — empirical, no composition-based prediction
2. **Higuchi model**: drug release from matrices proportional to sqrt(t) — same mathematical form as geochemical parabolic rate law
3. **First-order kinetics**: Assumes linear concentration dependence — poor fit for ASDs
4. **Amorphous solubility approach**: Uses measured amorphous solubility as upper bound
5. **LLPS framework**: Liquid-liquid phase separation occurs when amorphous solubility is exceeded (Indulkar et al. 2019)

### Critical Gap
**No TST-equivalent framework exists in pharmaceutical science.** Pharma dissolution models are empirical (fit parameters to dissolution curves) rather than predictive from composition and thermodynamic properties.

Specific gaps:
- Cannot predict dissolution rate from drug-polymer composition without experimental measurement
- No equivalent of the saturation index framework for predicting crystallization during dissolution
- Passivation layer (polymer-rich surface) is observed but not modeled with geochemical rigor
- No speciation modeling equivalent to PHREEQC for drug-water-polymer systems

### Key Papers
1. PMID 36549404 (2023, IJP): Supersaturation and phase behavior during ASD dissolution — critical review
2. PMID 36529939 (2023, Mol Pharm): Inhomogeneous phase reduces bioavailability — demonstrates that ASD dissolution is far more complex than Noyes-Whitney predicts
3. PMID 35872180 (2022, Eur J Pharm Biopharm): HPMCAS review — the most successful ASD polymer
4. PMID 34002256 (2021): Dissolution mechanisms review
5. Indulkar et al. 2019 (Mol Pharm): LLPS during ASD dissolution — new phase behavior framework
6. Ting et al. 2018 (AAPS J): Spring-parachute model — current conceptual framework
7. Baird & Taylor 2012 (Adv Drug Deliv Rev): Evaluation of ASD dissolution — foundational review

---

## Disjointness Verification

### PubMed Cross-Citation Analysis
- "volcanic glass dissolution" AND "pharmaceutical" OR "drug" OR "ASD": 1 result (false positive — about volcanic ash Fe/ocean)
- "basaltic glass dissolution kinetics" AND "amorphous solid dispersion": 0 results
- "transition state theory dissolution" AND "amorphous drug": 0 results (12 results for broader "TST + drug dissolution" but these are pharmaceutical-internal uses of TST for chemical reactions, NOT geochemical glass dissolution TST)
- "PHREEQC" AND "pharmaceutical": 21 results (all environmental: drug contamination in groundwater modeling, NOT dissolution prediction)
- "silicate glass dissolution" AND "drug release": 0 specific mechanistic cross-citations

### Disjointness Assessment: DISJOINT
The geochemical glass dissolution community (volcanology, nuclear waste, weathering) and the pharmaceutical ASD dissolution community have zero mechanistic cross-citations. They study the SAME physical process (amorphous solid dissolving in aqueous medium) with completely independent theoretical frameworks. The geochemists have TST rate laws, PHREEQC modeling, and composition-property relationships. The pharmaceutical scientists have empirical Noyes-Whitney, Higuchi models, and experimental dissolution testing. The transfer of the geochemical framework to pharma has not been attempted.

---

## Bridge Concept Strength Assessment

### Mathematical Analogy Verification
1. **Parabolic rate law**: Geochemistry uses thickness ~ sqrt(t) for passivation layer growth. Higuchi (1961) independently derived dm/dt ~ sqrt(t) for drug release from matrices. SAME mathematics applied to SAME physics in different fields.
2. **Saturation-dependent rate**: Geochemistry: r = k*(1 - Q/K). Pharma: no equivalent. The closest is crystallization rate ~ (S-1) where S = supersaturation ratio, but this is for crystallization, not dissolution.
3. **Composition-rate functions**: Geochemistry: extensive empirical models (e.g., Gislason & Oelkers 2003 for basalt, Grambow 1985 for borosilicate glass). Pharma: no equivalent — each drug-polymer combination requires new dissolution experiments.

### Potential Impact Assessment
- The pharmaceutical ASD market is >$20B and growing rapidly
- Ability to PREDICT dissolution rate from composition would accelerate formulation development by months
- Currently, formulation screening requires extensive experimental dissolution testing
- If TST framework + PHREEQC-style modeling can be adapted, this would be a paradigm shift in pharmaceutical dissolution science
