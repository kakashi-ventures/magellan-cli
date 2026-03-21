# Hypotheses -- Cycle 1
## Session: 2026-03-20-scout-005
## Target: Ferroptosis x Serpentinization Geochemistry
## Generator: Opus 4.6 (Generator agent)
## Date: 2026-03-20

---

## Relationship Maps

### Field A (Ferroptosis) -- Key Relationships
1. System Xc- imports cystine -> GSH synthesis -> GPX4 reduces PLOOHs
2. Fe(II) + H2O2 -> Fe(III) + OH* (Fenton) -> H-abstraction from PUFA-PE -> PLOOH chain reaction
3. ACSL4 incorporates AA/AdA into PE -> creates ferroptosis-sensitive substrate
4. 15-LOX/PEBP1 complex -> enzymatic PLOOH generation (PE-AA-OOH, PE-AdA-OOH)
5. Labile iron pool (LIP) ~0.5-1 uM Fe(II), tightly regulated by ferritin/transferrin/ferroportin/IRP1/IRP2
6. NCOA4-mediated ferritinophagy -> LIP expansion -> ferroptosis sensitization
7. FSP1/CoQ10 -> membrane-localized radical trapping (GPX4-independent defense)
8. Fenton-induced peroxidation -> LLPS disruption, raft protein redistribution (JACS 2024)
9. GPX4 rate ~10^8 M-1s-1 via selenocysteine -> kinetically dominant at biological [Fe]
10. GPX1-OSBPL8 axis -> natural ferroptosis via PA peroxidation at ER (Xia et al. 2026 Cell)

### Field C (Serpentinization) -- Key Relationships
1. 3FeO(olivine) + H2O -> Fe3O4(magnetite) + H2
2. Fe(II) -> Fe(III) oxidation at 200-315C generates H2 (0.5-26.5 mM)
3. pH 9-12 alkaline (Lost City vents up to 91C; lab experiments 200-315C)
4. Fischer-Tropsch type (FTT) synthesis: CO/CO2 + H2 -> fatty acids C6-C34
5. Awaruite (Ni3Fe) catalyzes CO2 -> formate (0.3M), acetate (560 uM), pyruvate (10 uM)
6. Ferrihydrite: high surface area Fe(III) oxyhydroxide, heterogeneous Fenton catalyst
7. Green rust: mixed Fe(II)/Fe(III) layered hydroxide, Fenton-like at near-neutral pH
8. Redox gradients: >750 mV over ~400m at serpentinite-seawater interface
9. Fenton chemistry delocalized from serpentinization sites (Nature Comms 2023)
10. Lab serpentinization: olivine flow injection at 245C -> 76-89 mol% H2 (Ross et al. 2025 GRL)

### Bridge Points
- **Fe(II)/Fe(III) cycling**: Identical Fenton chemistry in both contexts
- **Lipid peroxidation substrates**: FTT produces fatty acids; ferroptosis peroxidizes membrane PLs
- **Ferrihydrite**: Known mineral catalyst in geochemistry; studied with lipid membranes (PMID 31836519)
- **PLOOH intermediates**: Same chemical species regardless of origin
- **Defense asymmetry**: Biology has GPX4/GSH/FSP1/CoQ10; abiotic systems have NO defense

---

## Hypothesis 1: Serpentinization-Condition Fenton Chemistry Generates the Same Specific PLOOHs Found in Ferroptosis

**Claim**: The phospholipid hydroperoxides PE-AA-OOH and PE-AdA-OOH that serve as specific death signals in ferroptosis can be generated abiotically when AA-PE or AdA-PE vesicles are exposed to Fe(II)/Fe(III) Fenton cycling at serpentinization-relevant conditions (150-250C, pH 9-11, 1 mM Fe(II)), with the same positional isomer distribution as the non-enzymatic ferroptotic pathway.

**Connection**: Ferroptosis (specific PLOOH death signals) -> Fe(II)/Fe(III) Fenton cycling kinetics -> Serpentinization geochemistry (abiotic radical chemistry)

**Mechanism**: In mammalian ferroptosis, four specific phospholipid hydroperoxides have been identified as the executioner molecules: PE-AA-OOH and PE-AdA-OOH (generated non-enzymatically via Fenton-initiated radical chain propagation) and 15-HpETE-AA-PE and 17-HOO-AdA-PE (generated enzymatically by the 15-LOX/PEBP1 complex) [GROUNDED: Kagan et al. 2017 Cell Chem Biol]. The non-enzymatic pathway operates via Fe(II) + H2O2 -> OH* -> H-abstraction at bis-allylic positions of AA (C-7, C-10, C-13) and AdA (C-7, C-10, C-13, C-16), followed by O2 addition and radical chain propagation [GROUNDED: standard lipid peroxidation chemistry]. The enzymatic pathway produces regiospecific products (15-position for AA, 17-position for AdA) requiring the LOX active site [GROUNDED: Kagan et al. 2017].

The bridge hypothesis is that the NON-ENZYMATIC Fenton pathway, which requires only Fe(II), H2O2 (or LOOH for propagation via Fe(II) + LOOH -> LO* + Fe(III) + OH-), and PUFA-containing phospholipids, would produce the same PE-AA-OOH and PE-AdA-OOH species under serpentinization-relevant conditions. At serpentinization temperatures (200-300C), the propagation rate constant increases approximately 3000x [COMPUTED: Arrhenius with Ea ~33 kJ/mol], and Fe(II) concentrations are approximately 1333x higher than the biological labile iron pool [COMPUTED: 1 mM vs 0.75 uM]. The bis-allylic C-H bonds in AA (BDE ~75 kcal/mol) remain the weakest positions at any temperature [GROUNDED: PUFA radical chemistry]. The key prediction is whether the POSITIONAL ISOMER DISTRIBUTION of hydroperoxides from abiotic Fenton chemistry at serpentinization conditions matches the non-enzymatic ferroptotic PLOOH profile. If it does, this demonstrates that ferroptosis exploits a fundamentally geochemical vulnerability -- the intrinsic reactivity of specific lipid structures to iron-mediated radical chemistry.

**Bridge type**: Fe(II)/Fe(III) Fenton cycling kinetics + PLOOH intermediate chemistry

**Falsifiable prediction**: When AA-PE or AdA-PE vesicles are exposed to 1 mM FeSO4 + 10 uM H2O2 at 200C, pH 10, for 24-48h (lab serpentinization conditions), LC-MS/MS will detect PE-AA-OOH and PE-AdA-OOH with a positional isomer distribution matching the non-enzymatic ferroptotic PLOOH profile within 2-fold. The 15-HpETE-AA-PE and 17-HOO-AdA-PE (enzymatic products) should NOT appear as dominant products, confirming these require 15-LOX regioselectivity absent in abiotic systems.

**Test protocol**:
1. Prepare SUVs of DOPE:DOPC:AA-PE (60:30:10 mol%) and DOPE:DOPC:AdA-PE (60:30:10 mol%)
2. Expose to Fenton conditions: 1 mM FeSO4, 10 uM H2O2, pH 10, 200C in sealed pressure vessels under N2/O2 (1% O2)
3. Sample at 2h, 6h, 24h, 48h
4. Extract lipids via Bligh-Dyer; analyze by LC-MS/MS with positional isomer resolution
5. Compare isomer distribution to published ferroptotic PLOOH profiles (Kagan et al. 2017)
6. Control: same vesicles at 37C, pH 7.4, 0.75 uM Fe(II) -- biological ferroptosis conditions
7. Control: free AA (not esterified) under same serpentinization conditions -- tests PE ester survival

**Counter-evidence**:
- At 200C and pH 10, AA-PE ester bonds may hydrolyze before significant peroxidation occurs, destroying PE-linked species. This is the largest experimental risk.
- The positional isomer distribution may be thermodynamically controlled at high T vs kinetically controlled at 37C, producing a different profile.
- At 1333x [Fe] and 3000x k_prop, over-oxidation (chain cleavage to MDA, 4-HNE) may dominate rather than stable PLOOH accumulation.

**Confidence**: 5/10 -- Chemistry is sound (Fenton + PUFA = PLOOH is universal). PE ester hydrolysis at 200C/pH 10 is a serious practical concern.

**Groundedness**: 6/10
- [GROUNDED: Kagan et al. 2017 Cell Chem Biol] Four specific PLOOHs as ferroptotic signals; 15-LOX/PEBP1 regioselectivity
- [GROUNDED: standard organic chemistry] Bis-allylic C-H bonds (~75 kcal/mol BDE) are weakest in PUFA chains
- [COMPUTED: computational validation phase] ~3000x propagation rate increase; 1333x Fe(II) concentration difference
- [SPECULATIVE] Whether PE-ester bonds survive 200C/pH 10
- [SPECULATIVE] Whether positional isomer distributions match across such different conditions

**Literature gap it fills**: No study has compared the specific PLOOH species profile between ferroptotic cells and abiotic Fenton-peroxidized lipids at any condition. The ferroptosis field treats PLOOHs as biological signals; the geochemistry field treats lipid oxidation as degradation. Neither asks whether the SAME specific molecules appear in both contexts.

---

## Hypothesis 2: The Labile Iron Pool Set-Point (~0.5-1 uM) Reflects the Fenton-PLOOH/GPX4 Kinetic Crossover Calibrated Against Ancestral Serpentinization Fe(II) Levels

**Claim**: The tightly regulated LIP of 0.5-1.0 uM Fe(II) in eukaryotic cells represents the maximum Fe(II) concentration at which Fenton-generated PLOOH accumulation rate remains below GPX4 clearance rate. This kinetic crossover was evolutionarily calibrated starting from the ~1 mM unregulated Fe(II) of serpentinization environments.

**Connection**: Ferroptosis (LIP regulation by ferritin/transferrin/IRP system) -> Fe(II)/Fe(III) Fenton cycling kinetics -> Serpentinization geochemistry (unregulated mM-level Fe(II))

**Mechanism**: In mammalian cells, the labile iron pool is maintained at approximately 0.5-1.0 uM Fe(II) through ferritin (sequestration into 4500-Fe(III) mineral core), transferrin/TFRC (controlled uptake), ferroportin/SLC40A1 (export), and IRP1/IRP2 (post-transcriptional regulation) [GROUNDED: Stockwell et al. 2017 Cell]. When LIP exceeds this range -- via NCOA4-mediated ferritinophagy, TFRC upregulation, or oncogenic signaling -- cells become sensitized to ferroptosis [GROUNDED: Stockwell et al. 2017]. The critical question: why 0.5-1 uM specifically? GPX4 operates at approximately 10^8 M-1 s-1 via selenocysteine [PARAMETRIC: selenoenzyme kinetics, specific citation uncertain], and at GSH 2-10 mM [GROUNDED: standard biochemistry], the PLOOH clearance rate is GPX4-limited. The Fenton-initiated PLOOH generation rate scales as k_Fenton * [Fe(II)] * [H2O2] * P_propagation.

The hypothesis proposes that the LIP set-point exists at the crossover where Fenton-PLOOH generation rate equals GPX4 clearance capacity. Below this [Fe(II)], GPX4 maintains steady-state PLOOH at negligible levels; above it, PLOOHs accumulate and membrane permeabilization ensues. Model membrane data supports the threshold concept: at 0.8 mM FeSO4, permeabilization onset occurs within ~20 min [GROUNDED: Langmuir 2024]. In serpentinization environments, Fe(II) was ~1 mM -- 1333x above the biological LIP [COMPUTED]. Early cells near such environments faced immediate membrane destruction via unchecked Fenton-PLOOH chemistry. The evolutionary trajectory: (1) proto-cells acquire Fe(II) sequestration, lowering intracellular Fe(II) from mM to uM; (2) selenoprotein GPX4 ancestors evolve to clear residual PLOOHs; (3) the two systems co-optimize to the present set-point.

**Bridge type**: Fe(II)/Fe(III) Fenton cycling kinetics

**Falsifiable prediction**: In a reconstituted system (AA-PE GUVs with ~1 uM reconstituted GPX4 and 5 mM GSH), plotting PLOOH accumulation rate vs [Fe(II)] at physiological [H2O2] = 50 nM, 37C, pH 7.4 will reveal a critical threshold [Fe(II)]_crit for runaway PLOOH accumulation falling within 0.3-3.0 uM -- coinciding with the biological LIP range. A 10-fold series (0.1, 0.3, 0.5, 1.0, 3.0, 10 uM Fe(II)) should show a sharp sigmoidal transition.

**Test protocol**:
1. Prepare GUVs of DOPC:AA-PE (80:20) with recombinant GPX4 at ~1 uM and 5 mM GSH encapsulated
2. Add Fe(II) externally at 0.1, 0.3, 0.5, 1.0, 3.0, 10 uM with steady-state 50 nM H2O2 (glucose/GOx/catalase system)
3. Monitor PLOOH by C11-BODIPY 581/591 fluorescence ratio
4. Monitor membrane integrity by calcein leakage
5. Identify [Fe(II)]_crit: transition from steady-state to runaway accumulation
6. Repeat with varying [GPX4] (0.1, 1, 10 uM) to test whether [Fe(II)]_crit scales with [GPX4]

**Counter-evidence**:
- LIP is likely determined by MULTIPLE constraints: iron is needed for hundreds of enzymes (RNR, CcO, aconitase, PHDs). The set-point is probably multi-constraint optimization, not purely anti-Fenton.
- GPX4 expression varies 10-100x across cell types (hepatocytes >> neurons), so no single universal crossover exists.
- The evolutionary argument is inherently difficult to falsify directly.

**Confidence**: 4/10 -- The in vitro crossover experiment is clean and feasible. The evolutionary claim is speculative.

**Groundedness**: 5/10
- [GROUNDED: Stockwell et al. 2017 Cell] LIP ~0.5-1 uM; ferroptosis sensitization upon LIP expansion
- [PARAMETRIC] GPX4 selenocysteine rate ~10^8 M-1s-1 -- widely cited, specific source uncertain
- [GROUNDED: Langmuir 2024] Membrane permeabilization onset at 0.8 mM FeSO4 in ~20 min
- [COMPUTED] 1333x Fe(II) ratio
- [SPECULATIVE] LIP set-point is specifically Fenton-PLOOH crossover tuned
- [SPECULATIVE] Evolutionary trajectory from serpentinization Fe(II) to regulated LIP

**Literature gap it fills**: The ferroptosis field documents the LIP as "tightly regulated" without explaining why 0.5-1 uM specifically. No paper asks whether the biological LIP represents a kinetic crossover point calibrated to Fenton-PLOOH chemistry from geochemical ancestral conditions.

---

## Hypothesis 3: Ferrihydrite Mineral Surfaces Exhibit Partial Positional Selectivity in PUFA Oxidation -- A Mineral Proto-Lipoxygenase

**Claim**: Ferrihydrite nanoparticle surfaces catalyze lipid peroxidation with partial positional selectivity (enrichment of certain hydroperoxide isomers) because Fe(III) octahedral site spacing (~2.96 Angstrom Fe-Fe) constrains which bis-allylic positions of surface-adsorbed PUFA chains access catalytic sites.

**Connection**: Ferroptosis (15-LOX/PEBP1 regioselectivity) -> Ferrihydrite surface-catalyzed lipid peroxidation -> Serpentinization geochemistry (ferrihydrite as abundant mineral)

**Mechanism**: In ferroptosis, the 15-LOX/PEBP1 complex generates regiospecific hydroperoxides: 15-HpETE from AA [GROUNDED: Kagan et al. 2017]. This regioselectivity arises from the enzyme's substrate-binding channel positioning specific carbons near the non-heme Fe(III) active site. In solution-phase Fenton chemistry, OH* attacks randomly at accessible bis-allylic positions, producing near-statistical isomer distributions [GROUNDED: free radical chemistry].

Ferrihydrite (approximate formula Fe10O14(OH)2) is a poorly crystalline Fe(III) oxyhydroxide with surface area 200-600 m^2/g and abundant surface Fe(III)-OH sites [GROUNDED: mineral chemistry]. The ferrihydrite structure contains Fe(III) in octahedral sites with Fe-Fe nearest-neighbor distances of approximately 2.96 Angstrom (edge-sharing) and 3.44 Angstrom (corner-sharing) [PARAMETRIC: ferrihydrite structure, Michel et al. ~2007-2010]. When a PUFA chain adsorbs via its carboxylate (inner-sphere complex with surface Fe), [SPECULATIVE] the positions of bis-allylic hydrogens relative to neighboring surface Fe(III) sites become geometrically constrained. If certain positions preferentially access surface Fe(III), those would be oxidized more frequently than solution-phase statistics predict -- perhaps 2-3 fold enrichment, not true enzymatic regioselectivity, but a PARTIAL enrichment constituting a mineral "proto-lipoxygenase."

**Bridge type**: Ferrihydrite surface-catalyzed lipid peroxidation

**Falsifiable prediction**: Free arachidonic acid adsorbed onto ferrihydrite NPs (5 nm, ~300 m^2/g) and oxidized at 60C, pH 8, aerobic, 48h will show positional isomer ratios (C-5, C-8, C-9, C-11, C-12, C-15 hydroperoxides) deviating from the statistical 1:1:1:1 distribution of homogeneous Fenton. At least 2 of 4 bis-allylic positions should show >1.5-fold enrichment or depletion relative to solution controls.

**Test protocol**:
1. Synthesize 2-line ferrihydrite NPs by rapid FeCl3 hydrolysis at pH 7-8; characterize by XRD, TEM, BET
2. Adsorb free AA at ~1 molecule/nm^2 surface coverage
3. Condition A: 60C, pH 8, aerobic, 48h (surface-mediated autoxidation)
4. Condition B: 60C, pH 8, 0.5 mM FeSO4, 10 uM H2O2, 24h (heterogeneous Fenton)
5. Control: 0.5 mM FeSO4 in solution, no ferrihydrite (homogeneous Fenton)
6. Analyze by chiral-phase HPLC-MS/MS for positional isomer ratios
7. Benchmark: purified soybean 15-LOX with AA for true regioselectivity comparison

**Counter-evidence**:
- AA has 20+ rotatable bonds. At 60C (kT ~28 meV), thermal motion randomizes conformation on nanosecond timescales, far faster than oxidation. Geometric selectivity would be thermally averaged out.
- Ferrihydrite surface Fe(III) sites are HIGHLY heterogeneous (defects, steps, kinks). The 2.96 Angstrom spacing is an average, not a uniform template.
- Carboxylate anchoring does not fix conformation of carbons 7-20 Angstrom away.
- Any enrichment may fall within HPLC-MS/MS measurement error.

**Confidence**: 3/10 -- Creative but physically weak. Thermal fluctuations, surface heterogeneity, and chain flexibility all work against selectivity. The experiment would give a clear answer regardless.

**Groundedness**: 4/10
- [GROUNDED: Kagan et al. 2017] 15-LOX regioselectivity for C-15 of AA
- [GROUNDED: mineral chemistry] Ferrihydrite surface area 200-600 m^2/g
- [PARAMETRIC] Fe-Fe distances ~2.96 and 3.44 Angstrom -- from Michel et al. ~2007-2010, exact journal uncertain
- [GROUNDED: PMID 31836519] Ferrihydrite nanoparticle-lipid membrane interactions
- [SPECULATIVE] Geometric matching between Fe-Fe spacing and adsorbed chain conformation
- [SPECULATIVE] That any selectivity survives thermal averaging at 60C

**Literature gap it fills**: No study has measured positional isomer distribution of lipid hydroperoxides from heterogeneous mineral-surface Fenton chemistry vs homogeneous solution Fenton. Environmental chemistry measures total hydroperoxide, not positional isomers. The comparison has never been made.

---

## Hypothesis 4: "Prebiotic Ferroptosis" -- Ferrihydrite Fenton Destruction of Unsaturated Vesicles Created Selection Pressure Favoring Saturated Lipid Membranes

**Claim**: In prebiotic serpentinization environments, ferrihydrite-catalyzed Fenton chemistry preferentially destroyed vesicles containing unsaturated fatty acids while sparing saturated ones, creating chemical selection pressure that shaped early membrane composition. GPX4-like antioxidant evolution later permitted PUFA reincorporation.

**Connection**: Ferroptosis (PUFA-dependent membrane vulnerability) -> Ferrihydrite surface-catalyzed lipid peroxidation -> Serpentinization geochemistry (co-production of fatty acids + ferrihydrite via FTT synthesis)

**Mechanism**: Fischer-Tropsch type synthesis in serpentinization environments produces fatty acids C6-C34 including saturated and unsaturated species [GROUNDED: McCollom & Seewald 2018 Life]. These can spontaneously form vesicles above their CMC [GROUNDED: prebiotic membrane literature]. The same environment generates ferrihydrite through partial Fe(II)->Fe(III) oxidation at redox interfaces [GROUNDED: serpentinization mineralogy]. Ferrihydrite NPs adsorb onto lipid membranes [GROUNDED: PMID 31836519]. With residual Fe(II) and H2O2, ferrihydrite catalyzes Fenton chemistry at the membrane-mineral interface.

This creates DIFFERENTIAL DESTRUCTION: vesicles with unsaturated fatty acids (bis-allylic C-H BDE ~75 kcal/mol for PUFAs; allylic ~88 for monounsaturated) undergo radical chain peroxidation and membrane permeabilization [GROUNDED: JACS 2024, Langmuir 2024], while saturated vesicles (C-H BDE ~100 kcal/mol) resist radical initiation. The rate of H-abstraction by OH* is approximately 10^4x slower at the stronger C-H bonds [GROUNDED: organic chemistry]. This is "prebiotic ferroptosis" -- iron-dependent lipid-peroxidation-mediated vesicle destruction chemically identical to ferroptosis but operating on prebiotic assemblies without regulation. The evolutionary implication: earliest membranes were forced to be saturated-enriched (explaining archaeal isoprenoid lipid dominance), and PUFA incorporation became possible only after GPX4/catalase/SOD evolution. Ferroptosis is the re-emergence of an ancient geochemical vulnerability suppressed but never eliminated.

**Bridge type**: Ferrihydrite surface-catalyzed lipid peroxidation + Evolutionary selection pressure

**Falsifiable prediction**: Mixed vesicle populations -- 50% oleic acid (C18:1) and 50% palmitic acid (C16:0), distinguishable by fluorescent labels -- exposed to ferrihydrite (5 mg/mL) + 0.5 mM Fe(II) + 10 uM H2O2 at 70C, pH 8.5, 48h will show >5-fold differential survival, with population shifting from 50:50 to >80:20 (saturated:unsaturated). With AA vesicles (C20:4), destruction should reach >95% within 12h.

**Test protocol**:
1. Prepare oleic acid vesicles (rhodamine-DHPE labeled) and palmitic acid vesicles (NBD-PE labeled)
2. Mix 50:50 by NTA count
3. Add ferrihydrite (5 mg/mL) + 0.5 mM FeSO4 + 10 uM H2O2, 70C, pH 8.5 (bicine buffer)
4. Sample at 0, 6, 12, 24, 48h; quantify by dual-channel fluorescence
5. Confirm by DLS and cryo-TEM
6. Control A: no ferrihydrite, only dissolved Fe
7. Control B: saturated-only vesicles (no destruction expected)
8. Control C: +GSH (5 mM) + selenocysteine (50 uM) as crude abiotic antioxidant
9. Extended: repeat with AA (C20:4) vesicles for accelerated destruction

**Counter-evidence**:
- Single-chain fatty acid vesicles are inherently less stable than phospholipid bilayers. At 70C/pH 8.5, differential survival may reflect PHYSICAL stability (CMC, Krafft T) rather than oxidative resistance.
- Oleic acid has only ONE double bond (allylic, not bis-allylic). Rate difference vs palmitic may be only 10-100x, not enough for 5-fold differential in 48h. Linolenic acid (C18:3) would be a better substrate.
- UV photolysis from the young Sun may have been a larger membrane destruction source than Fenton.
- Evolutionary inference requires demonstrating GPX4 ancestors appeared AFTER membrane saturation.

**Confidence**: 5/10 -- Differential oxidation chemistry is well-established. Prebiotic vesicle experiment is feasible. Evolutionary inference is speculative but in vitro test is clean.

**Groundedness**: 6/10
- [GROUNDED: McCollom & Seewald 2018 Life] FTT fatty acid synthesis C6-C34
- [GROUNDED: PMID 31836519] Ferrihydrite-lipid membrane interactions
- [GROUNDED: JACS 2024] Fenton-mediated membrane permeabilization
- [GROUNDED: Langmuir 2024] Fe-mediated Fenton reduces membrane integrity
- [GROUNDED: organic chemistry] BDE hierarchy: bis-allylic (~75) < allylic (~88) < methylenic (~100) kcal/mol
- [SPECULATIVE] Differential destruction as meaningful prebiotic selection
- [SPECULATIVE] Archaeal membrane saturation as consequence of iron selection
- [SPECULATIVE] GPX4 evolution permitted PUFA reincorporation

**Literature gap it fills**: Origin-of-life research studies vesicle FORMATION from FTT fatty acids but not vesicle DESTRUCTION by the same environment's iron mineralogy. No study has performed differential vesicle survival under serpentinization Fenton conditions.

---

## Hypothesis 5: GPX4 Selenocysteine Catalysis Recapitulates an Abiotic PLOOH-Reduction Reaction First Performed by Iron-Selenium Minerals

**Claim**: GPX4's selenocysteine-mediated PLOOH reduction recapitulates an abiotic reaction first catalyzed by Se(-II) released from iron-selenide mineral phases in serpentinization environments. The Se atom was initially recruited from mineral dissolution rather than de novo synthesis.

**Connection**: Ferroptosis (GPX4 selenocysteine as master defense) -> Se-Fe mineral chemistry -> Serpentinization geochemistry (trace element mineralogy at hydrothermal vents)

**Mechanism**: GPX4 requires selenocysteine (Sec) at position 46; Cys substitution reduces activity approximately 1000-fold [GROUNDED: Ingold et al. 2018 Cell]. The catalytic cycle: (1) E-Se-H + PLOOH -> E-Se-OH + PLOH; (2) E-Se-OH + GSH -> E-Se-SG + H2O; (3) E-Se-SG + GSH -> E-Se-H + GSSG [GROUNDED: GPX catalytic mechanism]. The rate enhancement derives from selenium's lower pKa (~5.2 for Sec vs ~8.3 for Cys), meaning the selenolate form (more nucleophilic) predominates at physiological pH [GROUNDED: selenium biochemistry].

In serpentinization systems, Se is present as Se(-II) substituted for S(-II) in iron sulfide minerals (pyrite, pyrrhotite, mackinawite). Discrete ferroselite (FeSe2) can occur in some hydrothermal settings [PARAMETRIC: hydrothermal mineralogy]. The hypothesis proposes that dissolved selenide (HSe-) from mineral dissolution could react with Fenton-generated PLOOHs: HSe- + ROOH -> ROH + SeOH- (or Se(0) + ROH + OH-). This is thermodynamically favorable: Se(-II)->Se(0) with concomitant peroxide reduction has delta-E approximately +0.5V [COMPUTED: standard reduction potentials]. This abiotic reaction provided primitive PLOOH detoxification. The evolutionary step was incorporating Se into a thioredoxin-fold protein scaffold for recyclable catalysis. The complex SECIS/UGA machinery was worth the cost because Se-based PLOOH reduction was already performing a critical function in the geochemical milieu.

**Bridge type**: Evolutionary Se mineral chemistry (origin-of-life)

**Falsifiable prediction**: Na2Se (10-100 uM, as soluble Se(-II)) added to AA-PE vesicles undergoing Fenton peroxidation (0.5 mM Fe(II), 10 uM H2O2, pH 9, 80C) will reduce PLOOH accumulation rate by >50% vs Se-free controls (FOX assay). Se speciation will shift from Se(-II) to Se(0)/Se(IV) during the reaction (detectable by Se K-edge XANES at synchrotron).

**Test protocol**:
1. Prepare AA-PE vesicles (DOPC:AA-PE 80:20, 1 mM total lipid)
2. Initiate Fenton: 0.5 mM FeSO4 + 10 uM H2O2, pH 9 (borate buffer), 80C, sealed anaerobic
3. Conditions: (a) +Na2Se 100 uM, (b) 50 uM, (c) 10 uM, (d) +FeS1.9Se0.1 powder 1 mg/mL, (e) Se-free control
4. Monitor PLOOH by FOX assay at 0, 1, 2, 6, 12, 24h
5. Monitor membrane integrity by calcein leakage
6. Se speciation by Se K-edge XANES (12.6 keV)
7. If confirmed, determine IC50 and compare to recombinant GPX4 (1 uM + 5 mM GSH)
8. Test whether added thiol (GSH/Cys) enables catalytic Se turnover (regenerating Se(-II))

**Counter-evidence**:
- At 80C/pH 9 with Fenton reagents, Se(-II) may be rapidly oxidized to Se(0) or Se(IV) by OH* BEFORE reacting with PLOOHs. Kinetic competition between Se oxidation by radicals and PLOOH reduction needs to favor the latter.
- Se is a trace element (crustal abundance ~0.05 ppm). Dissolved Se(-II) in serpentinization fluids may be <1 nM, too low for meaningful PLOOH detoxification.
- SECIS/UGA machinery may have evolved for other selenoproteins (TrxR, DIO) unrelated to PLOOH detoxification.

**Confidence**: 3/10 -- Highly creative, multiple uncertain steps. The Na2Se + PLOOH experiment is straightforward and would give a clear chemical answer even if evolutionary inference remains speculative.

**Groundedness**: 3/10
- [GROUNDED: Ingold et al. 2018 Cell] Sec->Cys GPX4 reduces activity ~1000-fold
- [GROUNDED: selenium chemistry] Se pKa ~5.2 vs Cys ~8.3; selenolate more nucleophilic
- [GROUNDED: GPX catalytic cycle] Three-step mechanism well established
- [COMPUTED] Thermodynamic favorability of HSe- + ROOH from standard potentials
- [PARAMETRIC] Se-substituted sulfides in serpentinization -- plausible but concentration data sparse
- [SPECULATIVE] Se(-II) reduces PLOOHs at meaningful rates vs OH* oxidation
- [SPECULATIVE] Evolutionary trajectory from mineral Se to GPX4 selenocysteine

**Literature gap it fills**: Selenoprotein evolution is studied without connection to PLOOH detoxification in serpentinization. Se biochemistry community focuses on SECIS element and UGA capture. Serpentinization community discusses Se as trace mineral element but not as prebiotic antioxidant. Ferroptosis field takes GPX4's Se as given without asking where the requirement originated.

---

## Hypothesis 6: The ER as Intracellular "Serpentinization Redox Interface" -- Fe(II)/H2O2 Overlap Zone Determines Ferroptosis Initiation Site

**Claim**: The ER membrane is the primary ferroptosis initiation site because it occupies a unique intracellular REDOX INTERFACE -- where cytoplasmic labile Fe(II) (from lysosomal ferritinophagy) meets ER-luminal H2O2 (from Ero1alpha oxidative protein folding) -- analogous to the Fenton-active mixing zone at serpentinite-seawater redox interfaces.

**Connection**: Ferroptosis (organelle-specific PLOOH initiation at ER) -> Redox gradient-dependent Fenton reaction zone -> Serpentinization geochemistry (Fenton-active redox interfaces)

**Mechanism**: In serpentinization systems, the steepest gradients occur at the interface between reducing serpentinizing rock (Eh -500 to -800 mV, rich in Fe(II), no O2) and oxidized seawater (Eh +350 mV, rich in O2/H2O2, no Fe(II)). Fenton chemistry peaks precisely at the narrow mixing zone where BOTH reactants coexist [GROUNDED: serpentinization redox literature; Nature Comms 2023]. This geochemical principle -- Fenton activity maximized at REDOX INTERFACES -- is fundamental.

The hypothesis transfers this spatial logic intracellularly. Within a eukaryotic cell, different organelles maintain distinct redox states: lysosomes contain Fe(II) from NCOA4-mediated ferritinophagy [GROUNDED: ferritinophagy literature]; the ER lumen is relatively oxidizing due to Ero1alpha generating H2O2 during disulfide bond formation [GROUNDED: Ero1 biochemistry]. [SPECULATIVE] The ER outer membrane represents the intracellular serpentinization mixing zone: cytoplasmic Fe(II) on one face, luminal H2O2 on the other. PLOOH initiation peaks at this interface. This is consistent with Xia et al. 2026 Cell, which identified the ER as the primary site of natural ferroptosis [GROUNDED: Xia et al. 2026]. The mechanistic addition: the ER is ferroptosis-vulnerable not solely because of ACSL4, but because of its position as a REDOX INTERFACE.

**Bridge type**: Redox gradient spatial patterning of Fenton activity

**Falsifiable prediction**: In HT-1080 cells, simultaneous imaging of (a) labile Fe(II) (FerroOrange) and (b) ER-luminal H2O2 (HyPer7-KDEL) will show spatial colocalization at ER membranes. During erastin-induced ferroptosis, PLOOH (C11-BODIPY) initiation will begin at ER membranes marked by Fe(II)/H2O2 overlap. Pre-treating with Ero1alpha inhibitor EN460 (reducing ER H2O2) should delay ferroptosis onset by >2-fold.

**Test protocol**:
1. HT-1080 cells expressing ER-targeted HyPer7 (HyPer7-KDEL) for ER luminal H2O2
2. Stain with FerroOrange (1 uM, cytoplasmic labile Fe(II))
3. Stain with C11-BODIPY 581/591 (membrane PLOOH reporter)
4. Induce ferroptosis with erastin (10 uM) or RSL3 (0.5 uM)
5. Live-cell confocal at 5 min intervals for 6h: three channels
6. Colocalization: Pearson coefficient for Fe(II) vs H2O2 vs PLOOH at ER (calnexin-BFP marker) vs other organelles
7. Intervention: EN460 (Ero1alpha inhibitor, 10 uM, 2h pre-treatment)
8. Intervention: DFO (100 uM, 6h) -- positive control eliminating Fe(II)
9. Quantify: time to first PLOOH signal; organelle of origin; EN460 effect on onset

**Counter-evidence**:
- Macroscale geochemical gradient (hundreds of meters) vs intracellular (micrometers) may be analogy without mechanistic substance. Diffusion physics differ fundamentally.
- ER vulnerability may be fully explained by high ACSL4 + low GPX4, without needing redox interface. If EN460 has no effect, the model is wrong.
- Ero1alpha H2O2 is generated in ER LUMEN; Fenton needs Fe(II) and H2O2 in SAME compartment. H2O2 trans-membrane diffusion may be limiting (may require aquaporins).
- FerroOrange/HyPer7 spatial resolution may be insufficient to distinguish "ER membrane" from "near-ER cytoplasm."

**Confidence**: 4/10 -- Conceptually elegant; the Xia 2026 ER finding provides partial support. But the geochemistry-to-cell leap is large and the ACSL4 alternative is strong.

**Groundedness**: 5/10
- [GROUNDED: serpentinization literature; Nature Comms 2023] Fenton peaks at redox interfaces
- [GROUNDED: Xia et al. 2026 Cell] ER is primary site of natural ferroptosis
- [GROUNDED: Ero1 biochemistry] Ero1alpha generates H2O2 in ER lumen during oxidative protein folding
- [GROUNDED: ferritinophagy literature] NCOA4 releases Fe(II) from lysosomes
- [PARAMETRIC] ER luminal redox potential values vary in literature
- [SPECULATIVE] Fe(II)/H2O2 overlap at ER membrane is CAUSAL for ER-initiated ferroptosis
- [SPECULATIVE] Geochemical redox interface analogy has predictive power at cellular scale

**Literature gap it fills**: Ferroptosis field identifies ER as key site (Xia 2026) but attributes it to ACSL4/OSBPL8, not redox interface positioning. Geochemistry has developed Fenton-at-redox-interface models never mapped to intracellular organelle geography. No paper proposes the ER as the "serpentinization mixing zone" of the cell.

---

## Hypothesis 7: Fenton Peroxidation of Prebiotic Fatty Acid Vesicles Induces Phase Separation Creating Functionally Distinct Membrane Domains

**Claim**: Fenton-induced lipid peroxidation (documented for modern phospholipid systems, JACS 2024) would similarly drive phase separation in simpler prebiotic fatty acid vesicles under serpentinization conditions, generating oxidized-enriched high-permeability domains coexisting with intact low-permeability domains -- a chemical route to primitive compartmentalization.

**Connection**: Ferroptosis (PLOOH-driven membrane LLPS and raft disruption) -> Fenton-mediated membrane phase reorganization -> Serpentinization geochemistry (iron-rich prebiotic environment with FTT fatty acids)

**Mechanism**: The JACS 2024 study (DOI: 10.1021/jacs.3c10132) demonstrated Fenton-induced peroxidation dramatically enhances Lo/Ld phase separation in DPPC/DOPC/cholesterol membranes, with peroxidized lipids accumulating in the disordered phase and GPI-anchored proteins displaced from raft domains [GROUNDED: JACS 2024]. The Langmuir 2024 study showed this reduces line tension at domain boundaries and decreases membrane integrity [GROUNDED: Langmuir 2024]. In ferroptosis this is pathological. In prebiotic context it could be CONSTRUCTIVE.

Prebiotic FTT fatty acid vesicles would contain heterogeneous saturated and unsaturated species of varying chain lengths [GROUNDED: McCollom & Seewald 2018]. Unlike modern Lo/Ld (requiring cholesterol), fatty acid membranes can exhibit solid-ordered/liquid-disordered (So/Ld) phase coexistence based on chain length and saturation differences alone [GROUNDED: fatty acid phase behavior]. When ferrihydrite-catalyzed Fenton chemistry selectively peroxidizes the unsaturated fraction, oxidized products (hydroperoxy, keto, chain-cleaved) have dramatically altered packing: -OOH groups increase headgroup area, truncated chains reduce hydrophobic volume [GROUNDED: lipid biophysics]. This AMPLIFIES existing phase separation, creating: (a) ordered domains enriched in intact saturated chains (low permeability) and (b) disordered domains enriched in oxidized species (high permeability). [SPECULATIVE] If these differentially permeable domains operate on metabolically relevant small molecules, they create primitive selectivity -- ordered domains retain encapsulated molecules while disordered domains permit exchange. This is a purely chemical route to compartmentalization without proteins or genetic material.

**Bridge type**: Membrane phase behavior under Fenton-mediated peroxidation

**Falsifiable prediction**: Mixed fatty acid GUVs (palmitic acid C16:0 / oleic acid C18:1, 50:50 mol%, pH 8.5, 60C) exposed to ferrihydrite Fenton conditions (5 mg/mL, 0.5 mM FeSO4, 10 uM H2O2, 24h) will show >3-fold increase in Laurdan GP spatial heterogeneity vs t=0, indicating domain formation. Simultaneously, encapsulated calcein should show PATCHY leakage (from disordered domains, retained in ordered domains).

**Test protocol**:
1. Form GUVs from palmitic:oleic acid (50:50) in bicine buffer pH 8.5, 60C. Include 0.5 mol% Laurdan.
2. Encapsulate 50 mM calcein (self-quenching) during formation
3. Add 5 mg/mL ferrihydrite + 0.5 mM FeSO4 + 10 uM H2O2 externally
4. Confocal imaging at 0, 2, 6, 12, 24h: Laurdan GP mapping + calcein fluorescence
5. Quantify GP standard deviation across individual vesicles (domain formation metric)
6. LUV parallel for SAXS/WAXS: detect second d-spacing peak from oxidized domain
7. Controls: (a) no Fe/ferrihydrite, (b) palmitic only, (c) oleic only
8. Molecular permeability: separate experiments with carboxyfluorescein (MW 376) and FITC-dextran (MW 4000) for size-selective leakage test

**Counter-evidence**:
- Single-chain fatty acid vesicles are in DYNAMIC EQUILIBRIUM with monomers (unlike kinetically trapped phospholipid bilayers). At 60C/pH 8.5, oleic acid CMC ~50-200 uM -- oxidized oleic acid monomers may desorb into solution rather than accumulate as membrane domains.
- JACS 2024 used DPPC/DOPC/cholesterol with Lo/Ld coexistence. Fatty acid binaries lack Lo phases (no cholesterol). Phase behavior mechanism may not transfer.
- Oxidized fatty acids (hydroperoxides, aldehydes) are highly reactive; further reactions (cross-linking, fragmentation) may destroy membrane rather than create stable domains.
- Thermal motion at 60C may homogenize domains faster than Fenton creates them.

**Confidence**: 4/10 -- Fenton-LLPS in phospholipids is established (JACS 2024). Extension to prebiotic fatty acid vesicles is creative and testable but physically uncertain.

**Groundedness**: 5/10
- [GROUNDED: JACS 2024 (10.1021/jacs.3c10132)] Fenton-induced LLPS in Lo/Ld model membranes
- [GROUNDED: Langmuir 2024] Fe-mediated Fenton reduces line tension, membrane integrity
- [GROUNDED: McCollom & Seewald 2018 Life] FTT fatty acid synthesis C6-C34
- [GROUNDED: lipid biophysics] Oxidized lipids have altered packing parameters
- [GROUNDED: fatty acid membrane science] Fatty acid mixtures exhibit So/Ld phase coexistence
- [SPECULATIVE] Fatty acid membranes undergo analogous Fenton-induced phase separation
- [SPECULATIVE] Resulting domains create functionally relevant differential permeability
- [SPECULATIVE] This constitutes "primitive compartmentalization"

**Literature gap it fills**: JACS 2024 used modern model membranes and interpreted in cell death context. No study applies Fenton-LLPS to prebiotic fatty acid vesicles. Origin-of-life community studies vesicle formation/growth/division but NOT oxidation-induced phase separation as compartmentalization route.

---

## SELF-CRITIQUE

### 1. [GROUNDED] Tag Verification

| Claim | Status | Notes |
|---|---|---|
| Kagan et al. 2017 -- four PLOOHs | VERIFIED | Cell Chemical Biology (not Cell). Content correct. |
| Stockwell et al. 2017 Cell | VERIFIED | Major ferroptosis review. |
| Ingold et al. 2018 Cell -- Sec->Cys GPX4 | VERIFIED | Cell paper, GPX4 knockin mice. Moderate confidence on exact activity ratio. |
| JACS 2024 (10.1021/jacs.3c10132) | VERIFIED | DOI from literature context. |
| Langmuir 2024 | VERIFIED | From literature context. |
| Xia et al. 2026 Cell | VERIFIED | Feb 2026 per literature context. |
| McCollom & Seewald 2018 Life | VERIFIED | From literature context. |
| PMID 31836519 ferrihydrite-lipid | VERIFIED | From computational validation. |
| GPX4 rate ~10^8 M-1s-1 | PARAMETRIC | Widely cited, cannot name specific author/year/journal. |
| Michel et al. ferrihydrite structure | PARAMETRIC | Cannot confidently assign year/journal (~2007-2010). |
| Organelle redox potentials | PARAMETRIC | Standard values, no specific citation. |
| Ero1alpha H2O2 generation | GROUNDED | Established in oxidative protein folding literature. |

### 2. Thermodynamic Plausibility
- H1: PE ester hydrolysis at 200C/pH 10 is genuine concern. FLAGGED.
- H2: Kinetic crossover model is sound. PASS.
- H3: Geometric selectivity at 60C is physically weak. FLAGGED (confidence = 3).
- H4: BDE difference (75 vs 100 kcal/mol) is robust. PASS.
- H5: HSe- + ROOH thermodynamically favorable by ~0.5V. PASS. Kinetic competition is the concern.
- H6: No thermodynamic claims. PASS.
- H7: Palmitic acid Tm = 63C; So/Ld coexistence possible at 60C. PASS.

### 3. GPX4 Equivalents in Abiotic Systems
- H1-H4, H6-H7: No GPX4 equivalent claimed. PASS.
- H5: Claims mineral Se as evolutionary PRECURSOR to GPX4. Correctly framed as ancestral chemistry. PASS.

### 4. Confidence Calibration
- Mean: (5+4+3+5+3+4+4)/7 = 4.0. Appropriate for genuinely novel cross-domain bridge with zero prior citations.
- No hypothesis at 7+ (would require strong literature support, impossible for truly novel connections).
- Lowest (H3, H5 at 3) are most speculative. Highest (H1, H4 at 5) have most testable chemistry.

### 5. Bridge Mechanism Diversity
- Fenton cycling kinetics: H1, H2 (2 -- within limit)
- Ferrihydrite surface catalysis: H3, H4 (2 -- within limit)
- Evolutionary Se mineral chemistry: H5 (unique)
- Redox gradient spatial patterning: H6 (unique)
- Membrane phase behavior: H7 (unique)
- Total: 5 DISTINCT bridge mechanisms. PASS.

### 6. Constraint Compliance
- 7 hypotheses (within 5-7)
- 5 distinct bridge mechanisms (exceeds minimum 3)
- 3+ hypotheses with named molecular species (H1: PE-AA-OOH; H3: ferrihydrite/AA; H5: FeSe2/selenocysteine)
- 2 origin-of-life hypotheses (H4, H5)
- All groundedness scores integer 1-10
- No "ferroptosis happens in rocks" framing
- Self-critique completed with claim-level verification

### Self-Critique Issues
1. Two citations downgraded GROUNDED->PARAMETRIC (Michel ferrihydrite, GPX4 rate constant)
2. PE ester hydrolysis at 200C/pH 10 threatens H1 -- mitigated by free-AA control
3. Geometric matching in H3 is weakest physical claim -- confidence at 3
4. Se availability in serpentinization fluids (H5) poorly constrained
5. Scale mismatch in H6 (geochemical km vs intracellular um)
6. Fatty acid vesicle dynamics may undermine H7
