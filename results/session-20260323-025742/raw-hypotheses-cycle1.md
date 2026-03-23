# Raw Hypotheses — Cycle 1
## Target: Cartilage Biphasic Theory x Biofilm Matrix Mechanics
## Session 011 | Date: 2026-03-23

---

## Hypothesis H1.1: Fixed Charge Density (FCD) of P. aeruginosa Alginate Biofilm Predicts Donnan-Mediated Cationic Antibiotic Partitioning

CONNECTION: Cartilage triphasic theory (Lai 1991) -->  Fixed charge density & Donnan equilibrium -->  Biofilm antibiotic penetration

CONFIDENCE: 7/10 — Triphasic theory is well-validated in cartilage. Alginate carboxylates create a measurable FCD. Donnan partitioning of cationic antibiotics is a direct thermodynamic consequence.

NOVELTY: Novel — FCD has never been measured in biofilm. No paper applies Donnan partitioning theory to antibiotic uptake in biofilm.

GROUNDEDNESS: 7/10 — Mow 1980 and Lai 1991 are well-established [GROUNDED]. Alginate charge chemistry well-characterized [GROUNDED]. Donnan partitioning coefficient calculable from standard thermodynamics [GROUNDED]. Specific FCD values for biofilm are PREDICTED, not measured [PARAMETRIC].

IMPACT IF TRUE: High — Would provide a quantitative framework for predicting which antibiotics concentrate or are excluded from biofilms based on charge, and how to manipulate ionic strength to enhance penetration.

### MECHANISM

The triphasic theory of charged hydrated soft tissues (Lai et al. 1991, J Biomech Eng) describes how fixed charges in cartilage create a Donnan potential that concentrates cations and excludes anions within the tissue. The key equation is:

Donnan factor: r_D = sqrt(c_0^2 + (FCD/2)^2) / c_0

Where c_0 is the external ion concentration and FCD is the fixed charge density. For a cationic solute with valence z+, the partition coefficient K = r_D^z.

P. aeruginosa alginate contains mannuronate (M) and guluronate (G) blocks, each with one carboxylate (pKa ~3.5), yielding approximately one negative charge per ~200 Da disaccharide. At typical biofilm alginate concentrations (1-5% w/v), we predict FCD in the range of -0.05 to -0.25 mEq/mL.

For cationic antibiotics like tobramycin (z = +5 at pH 7.4) or gentamicin (z = +4.5), the Donnan partitioning creates CONCENTRATION of these drugs within the negatively charged biofilm matrix. At external [NaCl] = 10 mM (relevant for some mucosal surfaces): K_tobramycin ~ r_D^5 ~ 3.0-fold concentration. At physiological 150 mM NaCl: K ~ 1.02-fold (negligible).

This predicts that cationic aminoglycoside efficacy against biofilm should be STRONGLY ionic-strength-dependent — more effective at low ionic strength where Donnan concentration is maximal. Conversely, anionic antibiotics (e.g., ceftazidime, z ~ -1) would be EXCLUDED from the biofilm matrix at low ionic strength.

The critical prediction is that mixed-charge biofilms (with both cationic Pel and anionic alginate zones) would create INTERNAL concentration gradients — anionic antibiotics concentrated in Pel zones, cationic in alginate zones — producing heterogeneous killing patterns visible in confocal microscopy.

### SUPPORTING EVIDENCE
- From Field A (Cartilage): Lai et al. 1991 establishes triphasic theory with Donnan partitioning. Lu & Mow 2008 demonstrate FCD controls Na+ and Cl- partitioning in articular cartilage. Maroudas 1968 measured FCD of human cartilage (-0.05 to -0.30 mEq/mL). [GROUNDED]
- From Field C (Biofilm): Kundukad et al. 2025 (NPJ Biofilms) invoke Donnan equilibrium qualitatively for alginate biofilms but never quantify FCD. Tseng et al. 2013 show that alginate overproduction in mucoid P. aeruginosa correlates with aminoglycoside resistance. [GROUNDED]
- Bridge: Donnan partitioning coefficient is calculable from first principles given FCD and ionic strength. No published paper calculates it for biofilm. [NOVEL]

### COUNTER-EVIDENCE & RISKS
- Aminoglycoside resistance in biofilms is attributed to multiple mechanisms: efflux pumps (MexXY-OprM), enzymatic modification (AAC, ANT, APH), reduced growth rate/metabolic activity of biofilm cells, and persister cell formation. Donnan partitioning is ONE of many factors.
- Alginate is not the only barrier — Psl and Pel also contribute to matrix density, and their interactions with antibiotics are not purely charge-based.
- Biofilm interior ionic strength may differ from bulk medium, making the prediction dependent on local ionic environment which is hard to measure.
- Tobramycin binding to alginate may be driven by specific coordination chemistry (Ca2+ displacement), not just Donnan equilibrium.

### HOW TO TEST
1. **Measure biofilm FCD**: Equilibrate P. aeruginosa PAO1 biofilm with solutions of known [Na+] at varying ionic strengths (5, 10, 50, 150 mM NaCl). Measure Na+ partition coefficient by ICP-MS of digested biofilm vs. supernatant. Calculate FCD from Donnan theory.
2. **Predict antibiotic partitioning**: Using measured FCD, calculate predicted partition coefficients for tobramycin (+5), gentamicin (+4.5), ciprofloxacin (zwitterionic), and ceftazidime (-1).
3. **Measure actual antibiotic partitioning**: Incubate biofilms with fluorescently-labeled antibiotics at varying ionic strengths. Measure spatial distribution by confocal microscopy.
4. **If TRUE**: Measured antibiotic partition coefficients match Donnan predictions within 2-fold across ionic strength range. Cationic antibiotics show higher biofilm concentration at low ionic strength; anionic antibiotics show exclusion.
5. **If FALSE**: Antibiotic distribution is independent of ionic strength, or specific binding dominates over electrostatic effects.
6. **Effort**: 3-4 months wet lab. Standard microbiology + biophysics equipment. ~$20K materials.

---

## Hypothesis H1.2: Biofilm Aggregate Modulus (H_a) from Confined Compression Predicts Mechanical Resistance to Debridement Better Than G'/G''

CONNECTION: Cartilage confined compression (Mow 1980) -->  Aggregate modulus H_a -->  Biofilm mechanical resistance

CONFIDENCE: 6/10 — The biphasic framework is sound. Whether H_a is more predictive than current rheological measures is a testable empirical claim.

NOVELTY: Novel — H_a has never been measured in biofilm. Current biofilm mechanics uses oscillatory rheology (G'/G'') which is an UNDRAINED measure and does not separate solid and fluid contributions.

GROUNDEDNESS: 7/10 — Confined compression methodology for cartilage is well-established (Mow et al. 1980) [GROUNDED]. Current biofilm rheology methods documented [GROUNDED]. The claim that H_a is more predictive is PARAMETRIC — requires experimental validation.

IMPACT IF TRUE: High — Would replace the current biofilm mechanical characterization paradigm (oscillatory rheology giving G'/G'') with a framework that separates solid and fluid mechanical contributions, enabling better prediction of debridement outcomes.

### MECHANISM

Current biofilm mechanical characterization relies on oscillatory rheology to measure storage modulus G' and loss modulus G''. These are UNDRAINED properties — they measure the combined response of solid matrix + trapped fluid at the oscillation frequency. In cartilage biomechanics, the foundational insight of Mow 1980 was that undrained properties poorly predict tissue behavior under sustained loading because they conflate the solid matrix response with fluid pressurization.

The aggregate modulus H_a, measured by confined compression creep, isolates the drained solid matrix stiffness. In cartilage, H_a is the gold standard for predicting long-term load-bearing capacity because it represents the equilibrium solid response after all fluid has exited.

For biofilms, which are >90% water, the distinction between drained and undrained behavior should be EVEN MORE dramatic than in cartilage (~70% water). Current G'/G'' measurements at standard rheology frequencies (0.1-10 Hz) may dramatically overestimate biofilm resistance to sustained mechanical challenge (debridement, irrigation, shear stress) because they include fluid pressurization that dissipates in seconds.

We predict that confined compression of biofilm will yield H_a values 10-100x lower than G' values measured by oscillatory rheology, because removing the fluid contribution reveals the true solid matrix stiffness. Furthermore, H_a should be a better predictor of debridement outcomes (mechanical biofilm removal success) than G'/G''.

### SUPPORTING EVIDENCE
- From Field A: Mow et al. 1980 (J Biomech Eng) establishes confined compression and biphasic theory. Armstrong & Mow 1982 show H_a of cartilage ranges 0.5-0.9 MPa and correlates with load-bearing. Soltz & Ateshian 1998 demonstrate fluid pressurization dominates undrained cartilage response. [GROUNDED]
- From Field C: Biofilm G' ranges from ~1 Pa to ~1000 Pa (Peterson et al. 2015). Debridement outcomes are poorly predicted by current mechanical measures (Flemming & Wingender 2010 review). No confined compression data exists for biofilm. [GROUNDED]
- Bridge: Biphasic theory predicts that H_a = E_s * (1-nu_s) / ((1+nu_s)(1-2*nu_s)) where E_s and nu_s are the solid phase properties — directly transferable framework. [GROUNDED]

### COUNTER-EVIDENCE & RISKS
- Biofilms may be too soft for reliable confined compression. At 1-1000 Pa, measuring equilibrium confined compression requires extremely sensitive load cells and minimal friction.
- Biofilm architecture is heterogeneous (mushroom structures, channels, base layer vs. canopy) — a single H_a value may not capture this.
- Debridement is not purely mechanical — it involves chemical and biological factors (dispersal enzymes, quorum sensing).
- Biofilm under compression may exhibit nonlinear solid mechanics (strain-stiffening or -softening) not captured by linear biphasic theory.

### HOW TO TEST
1. **Confined compression setup**: Grow PAO1 biofilm in a custom confined compression chamber (porous indenter, impermeable sidewalls). Apply constant stress (0.01-10 Pa range), measure time-dependent deformation.
2. **Extract H_a and k**: Fit creep curve to biphasic theory solution to extract H_a (aggregate modulus) and k (hydraulic permeability).
3. **Compare with rheology**: On the same biofilm samples, measure G'/G'' by oscillatory rheology at 0.1-10 Hz.
4. **Debridement correlation**: Subject biofilms of varying maturity (1, 3, 5, 7 day) to standardized mechanical challenge (controlled shear). Correlate removal fraction with H_a vs. G'/G''.
5. **If TRUE**: H_a/G' ratio << 1 (fluid pressurization inflates apparent stiffness), and H_a correlates with debridement outcomes (R^2 > 0.7) better than G' (R^2 < 0.5).
6. **If FALSE**: H_a ≈ G' (biofilm behaves as an elastic solid at debridement timescales), or debridement is unrelated to mechanical properties.
7. **Effort**: 4-6 months. Requires custom compression apparatus. ~$30K.

---

## Hypothesis H1.3: Triphasic Theory Predicts That Pel-Dominated Biofilms and Alginate-Dominated Biofilms Have Opposite Donnan Swelling Responses to Ionic Strength Changes

CONNECTION: Cartilage triphasic theory (Lai 1991) -->  FCD-dependent Donnan swelling -->  Biofilm EPS composition determines swelling behavior

CONFIDENCE: 7/10 — Direct thermodynamic prediction from charge chemistry. Pel is cationic, alginate is anionic — their Donnan responses must be opposite.

NOVELTY: Novel — No paper predicts or measures opposite swelling responses for different EPS types. Biofilm swelling literature treats biofilm as a uniform material.

GROUNDEDNESS: 8/10 — Pel charge chemistry (cationic, deacetylated GalNAc) well-characterized [GROUNDED]. Alginate charge chemistry (anionic, carboxylate) well-characterized [GROUNDED]. Donnan swelling theory well-validated in cartilage [GROUNDED]. The specific prediction of OPPOSITE responses is a direct thermodynamic consequence [PARAMETRIC but thermodynamically necessary].

IMPACT IF TRUE: Transformative — Would establish that biofilm mechanical properties are not a single phenotype but depend fundamentally on EPS composition. Would predict that ionic manipulation (NaCl concentration changes) could selectively destabilize specific biofilm types.

### MECHANISM

In cartilage triphasic theory, Donnan osmotic pressure drives tissue swelling: FCD creates an excess of mobile ions inside the tissue relative to the bath, generating osmotic pressure pi_D = RT * (sqrt(FCD^2 + 4c_0^2) - 2c_0) where c_0 is external electrolyte concentration.

For ANIONIC matrices (negative FCD, like alginate or cartilage GAGs):
- Lowering external ionic strength INCREASES Donnan swelling (more osmotic pressure drives water in)
- Increasing ionic strength DECREASES swelling (screens charges, reduces osmotic gradient)

For CATIONIC matrices (positive FCD, like Pel):
- The mathematics is IDENTICAL but with reversed counterion species (Cl- instead of Na+)
- Lowering external ionic strength also INCREASES swelling for positive FCD

HOWEVER, the critical prediction emerges when considering MIXED ionic environments with divalent ions:
- Ca2+ cross-links alginate (egg-box model, specific to guluronate blocks) → CONTRACTS anionic matrix
- Ca2+ does NOT cross-link Pel (cationic, repels Ca2+) → Pel remains swollen
- Therefore: Adding CaCl2 should SELECTIVELY COMPACT alginate zones while SWELLING Pel zones (Donnan + osmotic from increased ionic strength)

This predicts that in mixed-EPS biofilms (like mature P. aeruginosa that produce both Pel and alginate), CaCl2 treatment creates INTERNAL mechanical stress between compacting alginate zones and swelling Pel zones — potentially causing mechanical disruption of the biofilm architecture.

### SUPPORTING EVIDENCE
- From Field A: Lai et al. 1991 triphasic theory predicts swelling as function of FCD and ionic strength. Urban et al. 1979 demonstrate cartilage swelling pressure increases ~4-fold as NaCl decreases from 1M to 0.01M. [GROUNDED]
- From Field C: Pel is cationic (Jennings et al. 2015 PNAS, partially deacetylated poly-GlcNAc/GalNAc). Alginate is anionic. Ca2+ cross-links alginate via egg-box model (Grant et al. 1973). Biofilm treated with EDTA (removes Ca2+) shows matrix disruption (Banin et al. 2006 PNAS). [GROUNDED]
- Bridge: Triphasic theory applied to heterogeneous charge system predicts internal stress at EPS boundaries. [NOVEL]

### COUNTER-EVIDENCE & RISKS
- The "internal mechanical stress" prediction assumes that Pel and alginate zones are spatially distinct and mechanically coupled. If they are interpenetrating networks, stress relaxation may prevent disruption.
- Ca2+ effects on biofilm are already studied (EDTA disruption) but through the lens of cross-linking chemistry, not Donnan theory. The Donnan framework may not add predictive power beyond what cross-linking chemistry already explains.
- Biofilm is living — bacteria can respond to ionic changes by altering EPS production, potentially compensating for mechanical stress.

### HOW TO TEST
1. **Prepare single-EPS biofilms**: Use Pel-only (pslBCD deletion mutant) and alginate-only (pelA deletion mutant) P. aeruginosa strains.
2. **Swelling measurement**: Grow biofilms in flow cell, then subject to step changes in NaCl concentration (150→10 mM, 10→150 mM). Measure thickness change by confocal z-stack in real time.
3. **Mixed-EPS biofilm**: Use wild-type PAO1 with fluorescent labeling of Pel (WFL lectin) and alginate (anti-alginate antibody). Subject to CaCl2 step (0→10 mM) and image spatial redistribution.
4. **If TRUE**: Alginate biofilm swells at low ionic strength, Pel biofilm swells at low ionic strength (same direction due to absolute FCD), but CaCl2 selectively compacts alginate zones while maintaining/swelling Pel zones, visible as differential spatial deformation.
5. **If FALSE**: Both EPS types show identical swelling response, or Ca2+ effects are dominated by specific binding rather than Donnan.
6. **Effort**: 3-4 months. Requires deletion mutants and confocal microscopy. ~$25K.

---

## Hypothesis H1.4: Biphasic Creep Time Constant of Biofilm Predicts the Timescale of Convective Antibiotic Penetration Under Shear Stress

CONNECTION: Cartilage biphasic poroelasticity -->  Characteristic diffusion time t_c = h^2/(H_a * k) -->  Biofilm transport timescale under mechanical loading

CONFIDENCE: 6/10 — The physics is correct for poroelastic materials. Whether biofilm behaves as a poroelastic material under shear is the key assumption.

NOVELTY: Novel — No biofilm transport model includes poroelastic coupling between mechanical deformation and fluid transport. Current models are pure diffusion-reaction.

GROUNDEDNESS: 6/10 — Biphasic creep time constant formula is standard (Mow 1980) [GROUNDED]. Biofilm antibiotic transport is well-studied by diffusion models [GROUNDED]. The coupling between mechanics and transport in biofilm is PARAMETRIC.

IMPACT IF TRUE: High — Would provide a quantitative prediction for how long shear stress must be applied to drive antibiotics into biofilm by convection, replacing the current purely diffusive model.

### MECHANISM

In biphasic theory, when a load is applied to a poroelastic material, it creates a pressure gradient that drives interstitial fluid flow. This fluid flow carries dissolved solutes (convective transport) in addition to diffusion. The characteristic time for this poroelastic transport is:

t_c = h^2 / (H_a * k)

where h is the layer thickness, H_a is the aggregate modulus, and k is the hydraulic permeability.

For cartilage (h = 2 mm, H_a = 0.5 MPa, k = 10^-15 m^4/N*s), t_c ~ 8000 s (~2 hours), explaining why sustained loading is needed for nutrient transport into cartilage.

For biofilm (estimated h = 100 um, H_a = 10-100 Pa, k = 10^-12 to 10^-10 m^4/N*s):
t_c = (10^-4)^2 / (100 * 10^-11) = 10^-8 / 10^-9 = ~10 seconds

This predicts that poroelastic transport in biofilm operates on a ~10-second timescale — meaning that applied shear stress for >10 seconds should drive convective transport of antibiotics into the biofilm matrix.

This makes a specific, falsifiable prediction: pulsatile shear (cycles of 10+ seconds of flow) should enhance antibiotic penetration compared to constant low flow, because each pulse drives a bolus of drug-laden fluid into the matrix. Short pulses (<1 s) should be ineffective because they are too brief for poroelastic coupling.

### SUPPORTING EVIDENCE
- From Field A: Mauck et al. 2003 demonstrate that dynamic compression enhances solute transport in cartilage through poroelastic pumping. Albro et al. 2008 quantify convective transport enhancement in cartilage under loading. [GROUNDED]
- From Field C: Stewart 2003 reviews antibiotic penetration in biofilm — all models are diffusion-based. Davit et al. 2013 measure biofilm permeability. Stoodley et al. 2002 show biofilm deformation under flow. [GROUNDED]
- Bridge: t_c formula is universal for poroelastic materials. Applying it to biofilm parameters gives ~10 s prediction. [PARAMETRIC]

### COUNTER-EVIDENCE & RISKS
- Biofilm may not behave as a poroelastic material — it could be viscoelastic with negligible solid-fluid coupling.
- The 10-second estimate depends on assumed k and H_a values. If k is higher (biofilm is more porous), t_c could be <1 second, making the effect irrelevant.
- Shear-enhanced transport in biofilm has been observed but attributed to convective mixing of the bulk fluid above the biofilm, not poroelastic pumping within the matrix.
- Biofilm channels (water-filled voids) provide bulk convective transport that may dominate over poroelastic transport through the EPS matrix.

### HOW TO TEST
1. **Measure H_a and k**: Confined compression of PAO1 biofilm to extract biphasic parameters (as in H1.2 protocol).
2. **Calculate predicted t_c**: From measured H_a, k, and biofilm thickness h.
3. **Pulsatile vs steady shear**: Expose biofilm to fluorescent dextran (antibiotic surrogate) under: (a) steady low shear, (b) pulsatile shear with period = t_c, (c) pulsatile shear with period = 0.1 * t_c.
4. **Image penetration depth**: Confocal microscopy of dextran penetration over time.
5. **If TRUE**: Pulsatile shear at t_c frequency shows 2-5x greater penetration depth than steady shear or high-frequency pulsation. Penetration kinetics match poroelastic model prediction.
6. **If FALSE**: All shear patterns give similar penetration, or steady shear is optimal.
7. **Effort**: 4-6 months. Requires flow cell with programmable shear and confocal. ~$30K.

---

## Hypothesis H1.5: The Hydraulic Permeability (k) of Biofilm EPS Network Can Be Predicted from Cartilage-Derived Structure-Function Relationships Using EPS Fiber Radius and Volume Fraction

CONNECTION: Cartilage permeability models (fiber-reinforced) -->  Kozeny-Carman / fiber matrix models -->  Biofilm permeability prediction

CONFIDENCE: 5/10 — The structure-function models are well-validated in cartilage. Whether EPS fiber geometry is sufficiently characterized for prediction is uncertain.

NOVELTY: Partially novel — Biofilm permeability has been measured, but never predicted from structural parameters using cartilage-derived models.

GROUNDEDNESS: 6/10 — Cartilage permeability models well-validated [GROUNDED]. EPS fiber dimensions partially characterized [GROUNDED]. Quantitative prediction from structure is PARAMETRIC.

IMPACT IF TRUE: Medium-High — Would enable prediction of biofilm permeability (and thus antibiotic transport rate) from microstructural imaging alone, without direct permeation measurement.

### MECHANISM

Cartilage hydraulic permeability is predicted from microstructural parameters using fiber matrix theory (Levick 1987, adapted by Quinn et al. 2001):

k = (a^2 / 16) * f(phi)

where a is the fiber radius, phi is the solid volume fraction, and f(phi) is a porosity function. For the Happel model: f(phi) = (1/phi) * [-ln(phi) - 0.5 * (1 - phi^2)/(1 + phi^2)].

In cartilage, a ~ 20 nm (collagen fibrils + GAG chains), phi ~ 0.15-0.30, giving k ~ 10^-15 to 10^-14 m^4/N*s. These model predictions match experimental measurements within ~2-fold.

For P. aeruginosa biofilm EPS:
- Alginate fibers: a ~ 5-10 nm (individual chains), phi ~ 0.01-0.05 (biofilm is >95% water)
- Predicted k = (7.5*10^-9)^2 / 16 * f(0.03) ~ 10^-12 to 10^-11 m^4/N*s

This is 3-4 orders of magnitude higher than cartilage permeability, consistent with the much higher water content. Published biofilm permeability measurements range from 10^-13 to 10^-10 m^4/N*s (variable, depending on biofilm type and maturity), bracketing our prediction.

The predictive power lies in relating permeability to fiber radius and volume fraction — meaning that changes in EPS composition (alginate overproduction in mucoid strains) could be PREDICTED to decrease permeability by increasing phi, providing a quantitative model for why mucoid biofilms are more resistant to antibiotic penetration.

### SUPPORTING EVIDENCE
- From Field A: Quinn et al. 2001 validate fiber matrix permeability model for cartilage. Levick 1987 establishes the theoretical foundation. [GROUNDED]
- From Field C: Biofilm permeability measured by multiple groups (Davit 2013, de Beer 1994). EPS fiber dimensions from electron microscopy. Mucoid (alginate-overproducing) biofilms are known to be more resistant to antibiotics. [GROUNDED]
- Bridge: Fiber matrix model is generic (applies to any fibrous hydrogel). Transfer to biofilm EPS requires knowing a and phi. [PARAMETRIC]

### COUNTER-EVIDENCE & RISKS
- EPS network structure is much more heterogeneous than cartilage collagen network — non-uniform fiber spacing may violate model assumptions.
- Biofilm permeability is affected by biofilm channels (water-filled voids) that are not captured by fiber matrix models (which assume uniform porous medium).
- The model may predict average permeability but miss the critical heterogeneity (channels vs. dense clusters) that determines actual transport.
- EPS fibers interact with each other (Pel-alginate cross-linking) in ways not captured by the independent-fiber assumption.

### HOW TO TEST
1. **Image EPS ultrastructure**: Cryo-SEM or cryo-TEM of PAO1 biofilm to measure fiber radius (a) and volume fraction (phi) in different regions.
2. **Predict k**: Apply Happel fiber matrix model to measured a and phi.
3. **Measure k**: Direct permeation test on the same biofilm samples (apply pressure gradient, measure flow rate).
4. **If TRUE**: Predicted k matches measured k within 3-fold for bulk biofilm. Mucoid mutant has lower k predictable from increased phi.
5. **If FALSE**: Predicted k is off by >10-fold, indicating that fiber matrix model is inappropriate for biofilm structure.
6. **Effort**: 6 months. Requires cryo-EM facility access and custom permeation apparatus. ~$40K.

---

## Hypothesis H1.6: Cartilage-Inspired Streaming Potential Measurement Reveals Spatial FCD Heterogeneity in Mixed-EPS Biofilm That Correlates with Antibiotic Killing Patterns

CONNECTION: Cartilage streaming potential measurement -->  Spatial FCD mapping -->  Biofilm EPS charge heterogeneity mapping

CONFIDENCE: 6/10 — Streaming potential is well-established for cartilage. Adapting to biofilm's much lower FCD and softer matrix is technically challenging.

NOVELTY: Novel — Streaming potential has never been applied to biofilm. No spatial FCD map of any biofilm exists.

GROUNDEDNESS: 6/10 — Streaming potential methodology well-established (Grodzinsky et al. 1981) [GROUNDED]. Biofilm EPS charge heterogeneity documented [GROUNDED]. Correlation with antibiotic killing is PARAMETRIC.

IMPACT IF TRUE: High — Would provide the first spatial FCD map of biofilm, revealing the charge landscape that determines ion and drug partitioning throughout the biofilm.

### MECHANISM

In cartilage, streaming potential measurements work by applying a pressure gradient across the tissue and measuring the resulting electrical potential. Mobile counterions are swept along with the fluid flow, creating a current. The streaming potential is proportional to FCD and inversely related to bulk conductivity:

V_stream = (FCD * k * delta_P) / (sigma_0 * mu * L)

where k is permeability, delta_P is applied pressure, sigma_0 is solution conductivity, mu is viscosity, L is sample thickness.

For biofilm, this measurement could be performed on a biofilm grown on a porous membrane support. Applying a small pressure difference (0.01-1 kPa — much less than for cartilage) across the membrane would drive fluid through the biofilm, and electrodes placed on either side would measure the streaming potential.

By scanning a microelectrode array across the biofilm surface, a spatial map of streaming potential (and thus FCD) could be constructed. In a mixed-EPS biofilm, this would reveal:
- Alginate-rich zones: negative FCD → negative streaming potential
- Pel-rich zones: positive FCD → positive streaming potential
- Psl-rich zones: near-zero FCD → near-zero streaming potential

Overlaying this FCD map with antibiotic killing patterns (from live/dead staining after antibiotic treatment) would test whether charge-based Donnan partitioning explains spatial heterogeneity in antibiotic efficacy within a single biofilm.

### SUPPORTING EVIDENCE
- From Field A: Grodzinsky et al. 1981 establish streaming potential for cartilage FCD measurement. Buschmann & Grodzinsky 1995 use streaming potential to map spatial FCD changes during cartilage compression. [GROUNDED]
- From Field C: Mixed Pel/alginate/Psl biofilms documented (Colvin et al. 2012, Mann & Wozniak 2012). Spatial heterogeneity of EPS known from confocal with lectins. No electrokinetic measurement of biofilm. [GROUNDED]
- Bridge: Streaming potential theory is material-independent — requires only charged porous medium with fluid flow. [GROUNDED]

### COUNTER-EVIDENCE & RISKS
- Biofilm FCD may be too low (~0.05 mEq/mL) to generate measurable streaming potentials at practical pressure differences.
- Biofilm is very soft — applied pressure may deform the biofilm rather than drive fluid through it.
- Live bacteria in biofilm produce their own electrochemical gradients (proton motive force) that could confound streaming potential measurements.
- Microelectrode resolution (~50-100 um) may be too coarse to resolve EPS-specific charge zones.

### HOW TO TEST
1. **Streaming potential setup**: Grow PAO1 biofilm on 0.2 um pore PCTE membrane in custom chamber. Place Ag/AgCl electrodes on both sides.
2. **Apply pressure steps**: 0.01, 0.1, 1 kPa. Measure voltage difference.
3. **Validation**: Compare streaming potential of alginate-only mutant (should be negative) vs Pel-only mutant (should be positive) vs Psl-only mutant (should be ~zero).
4. **Spatial mapping**: Use Pt microelectrode array (8x8, 100 um spacing) on biofilm surface. Scan streaming potential under flow.
5. **If TRUE**: Alginate-only and Pel-only mutants show opposite-sign streaming potentials. Wild-type shows spatial heterogeneity. FCD map correlates with antibiotic killing pattern (R^2 > 0.5).
6. **If FALSE**: Streaming potential undetectable or dominated by bacterial electrochemical noise.
7. **Effort**: 6-8 months. Requires custom electrochemical apparatus and microelectrode fabrication. ~$50K.

---

## Hypothesis H1.7: Biofilm Under Cyclic Compression Exhibits Poroelastic Pumping That Enhances Nutrient Transport, Analogous to Cartilage Under Joint Loading

CONNECTION: Cartilage dynamic loading benefit -->  Poroelastic pumping cycle -->  Biofilm nutrient transport under mechanical perturbation

CONFIDENCE: 5/10 — The physics is well-established in cartilage. Whether biofilm experiences and benefits from cyclic mechanical loading in vivo is the key question.

NOVELTY: Novel — Poroelastic pumping has never been proposed for biofilm nutrient transport. Current biofilm transport models ignore mechanical pumping.

GROUNDEDNESS: 5/10 — Cartilage poroelastic pumping well-documented [GROUNDED]. Biofilm experiences mechanical forces in vivo [GROUNDED]. The pumping benefit for biofilm is purely SPECULATIVE.

IMPACT IF TRUE: High — Would reveal that biofilms in mechanically active environments (heart valves, urinary catheters, joint prostheses) actively exploit mechanical forces to enhance their growth, suggesting that mechanical rest periods could be a biofilm control strategy.

### MECHANISM

In articular cartilage, cyclic compressive loading creates oscillating fluid flow through the poroelastic matrix. This "poroelastic pumping" enhances solute transport by 2-10x compared to diffusion alone (Mauck 2003, O'Hara 1990). The enhancement depends on the ratio of loading frequency to the characteristic poroelastic frequency f_c = 1/t_c.

Biofilms in clinical settings experience cyclic mechanical forces:
- Heart valve endocarditis biofilm: cardiac cycle at ~1 Hz, shear stress 1-10 Pa
- Urinary catheter biofilm: peristaltic flow, cyclic compression
- Orthopedic implant biofilm: joint loading at ~1 Hz during walking

If biofilm acts as a poroelastic material with t_c ~ 10 s (from H1.4), then cardiac-frequency loading (1 Hz >> 1/t_c = 0.1 Hz) would produce UNDRAINED response (no pumping benefit). But lower-frequency perturbations (breathing at ~0.25 Hz, postural changes, peristalsis) would be closer to the poroelastic frequency and could drive significant pumping.

The prediction: biofilms on mechanically active medical devices in slow-cycle environments (ventilator breathing, gastrointestinal peristalsis) grow faster than biofilms on static surfaces in otherwise identical conditions, because poroelastic pumping enhances nutrient transport to the biofilm interior.

### SUPPORTING EVIDENCE
- From Field A: O'Hara et al. 1990 and Mauck et al. 2003 demonstrate 2-10x transport enhancement in cartilage under dynamic loading. Soltz & Ateshian 2000 validate poroelastic model for cartilage under cyclic load. [GROUNDED]
- From Field C: Biofilms on medical devices experience mechanical forces (endocarditis, catheter, prosthetic joint). Stoodley et al. 1999 show biofilm deformation under flow. Growth differences between static and flow conditions observed (Purevdorj et al. 2002). [GROUNDED]
- Bridge: Poroelastic pumping enhancement factor depends on f/f_c ratio — calculable once t_c is known. [PARAMETRIC]

### COUNTER-EVIDENCE & RISKS
- Growth rate differences in flow vs static biofilm are currently explained by nutrient supply from bulk medium, not poroelastic pumping within the matrix.
- If t_c is <<1 s (biofilm is very permeable), then ALL physiologically relevant frequencies would be undrained and pumping would be negligible.
- Biofilm interior may be nutrient-limited by metabolic consumption (reaction) rather than transport — enhancing transport may not help if consumption rate is the bottleneck.
- The analogy breaks down if biofilm does not have a continuous solid matrix (it has channels and voids).

### HOW TO TEST
1. **Measure t_c**: From H1.2/H1.4 experiments, determine the poroelastic time constant.
2. **Cyclic loading**: Subject biofilm in flow cell to cyclic compression (frequency sweep: 0.01, 0.1, 1, 10 Hz) with fluorescent nutrient tracer.
3. **Measure transport**: Compare penetration depth and rate of tracer under cyclic loading vs static.
4. **Growth assay**: Grow biofilms under matched nutrient but different mechanical conditions: (a) static, (b) cyclic at f_c frequency, (c) cyclic at 10x f_c. Compare biomass after 48h.
5. **If TRUE**: Cyclic loading at f ~ f_c enhances tracer penetration 2-5x and biofilm growth 1.5-3x vs static.
6. **If FALSE**: No transport or growth enhancement from cyclic loading.
7. **Effort**: 4-6 months. ~$30K.

---

## Hypothesis H1.8: Net Fixed Charge Density (FCD) of P. aeruginosa Biofilm Transitions from Positive to Negative During Maturation Due to Temporal EPS Composition Shift, with Predictable Ionic Sensitivity Reversal

CONNECTION: Cartilage FCD measurement technology -->  Temporal FCD tracking -->  Biofilm maturation-dependent charge transition

CONFIDENCE: 6/10 — The temporal EPS shift is documented. The FCD transition prediction is a direct consequence. Whether it creates a therapeutically exploitable "charge reversal window" is speculative.

NOVELTY: Novel — No paper predicts or measures FCD changes during biofilm maturation. No concept of a "charge reversal point" in biofilm exists.

GROUNDEDNESS: 6/10 — Temporal EPS shift well-documented (Pel early → alginate late in chronic infection) [GROUNDED]. Triphasic theory for predicting charge consequences [GROUNDED]. Specific FCD values and transition timing PARAMETRIC.

IMPACT IF TRUE: Transformative — Would identify a "charge reversal window" during biofilm maturation when the matrix transitions through net-zero charge, creating a transient vulnerability to ionic perturbation.

### MECHANISM

P. aeruginosa biofilm maturation involves a well-documented shift in EPS composition:
- Early biofilm (1-3 days): Pel-dominated (Pel is the primary attachment and structural polysaccharide)
- Intermediate biofilm (3-5 days): Mixed Pel + alginate (alginate production begins)
- Mature/mucoid biofilm (>5 days, especially under selective pressure): Alginate-dominated

Since Pel is cationic (positive FCD) and alginate is anionic (negative FCD), the net FCD of the biofilm should transition from POSITIVE to NEGATIVE during maturation. At some intermediate timepoint, the net FCD passes through ZERO.

At net FCD = 0, the Donnan osmotic pressure is minimal, meaning the biofilm matrix has minimal osmotic resistance to mechanical challenge. This "charge reversal window" represents a transient vulnerability:
- Before reversal (Pel-dominated, FCD > 0): Biofilm is osmotically stabilized by positive Donnan pressure. Cationic antibiotics are repelled.
- At reversal (FCD ~ 0): Minimal osmotic stabilization. Neither cationic nor anionic antibiotics are electrostatically favored/disfavored.
- After reversal (alginate-dominated, FCD < 0): Biofilm is osmotically stabilized by negative Donnan pressure. Cationic antibiotics are concentrated but matrix is dense and mucoid.

### SUPPORTING EVIDENCE
- From Field A: Cartilage FCD changes with development and disease (osteoarthritis reduces FCD as GAGs are degraded). Temporal FCD tracking is standard in cartilage research (Bashir 1999, dGEMRIC MRI technique). [GROUNDED]
- From Field C: Pel → alginate temporal shift documented in chronic P. aeruginosa infection (Wozniak et al. 2003, Colvin et al. 2012). Mucoid conversion is a hallmark of CF lung adaptation. [GROUNDED]
- Bridge: Net FCD = Pel_FCD * phi_Pel + alginate_FCD * phi_alginate + Psl_FCD * phi_Psl (additive). Transition through zero is mathematically inevitable if sign changes. [PARAMETRIC but thermodynamically necessary]

### COUNTER-EVIDENCE & RISKS
- The EPS transition may not be uniform across the biofilm — different regions may have different compositions simultaneously.
- The "charge reversal window" may be very brief (~hours) or very gradual (~days), affecting its therapeutic utility.
- The FCD at the zero point may never truly reach zero if both EPS types coexist in the same microenvironment.
- Other factors (biofilm thickness, cell density, enzymatic defenses) may dominate over FCD-dependent vulnerability.

### HOW TO TEST
1. **Temporal FCD measurement**: Grow PAO1 biofilm, sample daily (days 1-7). Measure net FCD by tracer ion equilibrium (see H1.1 protocol).
2. **EPS quantification**: Parallel samples for Pel (congo red binding, Jennings method) and alginate (carbazole assay) quantification.
3. **Identify charge reversal timepoint**: Plot net FCD vs time. Find zero-crossing.
4. **Vulnerability test**: Challenge biofilms at pre-reversal, reversal, and post-reversal timepoints with standardized antibiotic (tobramycin 4x MIC) + mechanical shear. Compare killing efficacy.
5. **If TRUE**: Net FCD transitions from positive to negative. Killing efficacy peaks near the charge reversal timepoint (>2-fold improvement vs other timepoints).
6. **If FALSE**: FCD does not show a clear transition, or killing efficacy is unrelated to net FCD.
7. **Effort**: 4-6 months. Standard microbiology + ion chromatography. ~$25K.
