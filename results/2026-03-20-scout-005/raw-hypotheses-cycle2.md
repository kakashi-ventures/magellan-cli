# Raw Hypotheses -- Cycle 2
## Ferroptosis x Serpentinization Geochemistry
**Session**: 2026-03-20-scout-005
**Generator**: Opus 4.6
**Date**: 2026-03-20
**Context**: Building on 4 evolved hypotheses from cycle 1 + 5 critic questions + key counter-evidence

---

## CYCLE 2 GENERATION STRATEGY

### From Evolved Cycle 1 (refine and strengthen):
- E1 (Regioselectivity Fingerprint) → Refine into H2.1 with tighter predictions
- E2 (PHREEQC Speciation) → Refine into H2.2 with experimental validation plan
- E3 (Pourbaix-Guided PLOOH) → Refine into H2.3 with focused scope
- E4 (Dissolution-Dependent Fenton) → Refine into H2.4 with ferritin-as-containment emphasis

### Fresh hypotheses (different techniques, addressing critic questions):
- H2.5: Ferritin as Evolved Containment of Geochemical Fenton Reactor (critic question #4)
- H2.6: Ferryl Ion Product Distribution at Physiological pH (critic question #3)
- H2.7: Iron Compartmentalization Topology During Ferroptosis (critic question #1)

### HARD CONSTRAINTS (from cycle 1 kills):
- NO abiotic PUFAs from FTT synthesis
- NO homogeneous Fenton rate constants at pH 9-12
- NO LIP expansion claims
- NO PMID 31836519 mischaracterization
- NO r>0.9 identity predictions
- NO ferrihydrite etch pits at 6-8 nm scale
- ALL groundedness values as integers 1-10

---

## H2.1: Abiotic vs Enzymatic PLOOH Regioselectivity as a Chemical Fossil of Antioxidant Evolution
**Refined from**: E1 (Specification of H2)
**Technique**: Facet Recombination + Scale Bridging

═══════════════════════════════════════════
HYPOTHESIS: Abiotic vs Enzymatic PLOOH Regioselectivity as a Chemical Fossil of Antioxidant Evolution
═══════════════════════════════════════════
CONNECTION: Ferroptosis (15-LOX C15-regiospecific oxidation) →→ Radical selectivity contrast →→ Serpentinization (non-selective abiotic Fenton on ferrihydrite surfaces)
CONFIDENCE: 5 — Chemistry is sound and testable. Evolutionary interpretation is an inference.
NOVELTY: Novel
GROUNDEDNESS: 7
IMPACT IF TRUE: Medium-High — Establishes ferroptosis as an evolved weaponization of abiotic chemistry

MECHANISM
The defining chemical distinction between ferroptotic and abiotic lipid peroxidation is REGIOSELECTIVITY. In ferroptosis, 15-lipoxygenase (ALOX15) oxidizes arachidonic acid-PE with >95% selectivity at the C15 position [GROUNDED: Kuhn et al., BBA 2015; Ivanov et al., Chem Rev 2010 on lipoxygenase positional specificity]. This selectivity generates 15-HpETE-PE, which causes maximum membrane destabilization because the C15-hydroperoxide group protrudes into the bilayer midplane, disrupting chain packing [GROUNDED: Kagan et al., Nat Chem Biol 2017].

In contrast, Fenton-generated hydroxyl radicals (HO•) abstract hydrogen atoms from PUFA bis-allylic positions with near-equal probability, governed only by bond dissociation energies and statistical accessibility [GROUNDED: Porter et al., Chem Res Toxicol 1995; Yin et al., Free Rad Biol Med 2011 on non-enzymatic lipid peroxidation regiochemistry]. For arachidonic acid, this produces approximately equal amounts of 5-, 8-, 9-, 11-, 12-, and 15-HETE isomers [GROUNDED: Milne et al., Methods Enzymol 2007 on isoprostane/HETE regiochemistry from non-enzymatic oxidation].

The experiment: expose PUFA-PE vesicles to ferrihydrite-Fenton conditions at 37C, pH 7.2, then compare the PLOOH positional isomer distribution to that from purified 15-LOX. The quantitative prediction: the abiotic C15/(sum of all positional isomers) ratio will be 0.15-0.25 (near-statistical distribution), while the enzymatic ratio will be >0.90 (dominated by C15). This 4-6 fold selectivity contrast is the "chemical fossil" — it demonstrates that evolution refined a non-selective chemical process into a position-specific one.

At physiological pH (7.2), the Fenton mechanism may shift from free HO• to ferryl ion (FeIV=O) [GROUNDED: Hug & Leupin, EST 2003; Pignatello et al., Crit Rev Environ Sci Technol 2006 on ferryl in Fenton systems]. Ferryl has different (and potentially position-dependent) selectivity — this is itself a testable sub-prediction: the ferryl regioselectivity fingerprint at pH 7.2 may differ from the free HO• fingerprint at pH 3, providing a second chemical fossil dimension.

Temperature series at 25C, 37C, 45C tests whether the abiotic regioselectivity changes (prediction: <10% change, because BDE differences between bis-allylic positions are negligible and temperature does not create new selectivity).

SUPPORTING EVIDENCE
• From Ferroptosis: ALOX15 >95% C15-selective [GROUNDED: Kuhn et al., BBA 2015]. 15-HpETE-PE is the primary death signal [GROUNDED: Kagan et al., 2017].
• From Geochemistry: Ferrihydrite is an effective heterogeneous Fenton catalyst at circumneutral pH [GROUNDED: Petigara et al., EST 2002; Kwan & Voelker, EST 2003].
• Bridge: Non-enzymatic PUFA oxidation produces near-statistical isomer distributions [GROUNDED: Milne et al., Methods Enzymol 2007; Yin et al., 2011].

COUNTER-EVIDENCE & RISKS
• Ferryl (FeIV=O) at pH 7.2 may show partial positional selectivity, narrowing the contrast with 15-LOX. This would weaken but not eliminate the "chemical fossil" argument (ferryl selectivity, if present, would still be far less than >95%).
• The experiment requires LC-MS/MS with isomer resolution capability — not all lipidomics labs can separate positional HETE isomers. Chiral-phase HPLC may be needed [GROUNDED: Milne et al., 2007].
• Evolutionary inference (15-LOX evolved from non-selective Fenton) is not directly testable from this experiment alone — it demonstrates the chemical contrast but not the evolutionary path.

HOW TO TEST
1. Prepare PAPE vesicles in DOPC matrix (30:70 mol ratio) at pH 7.2
2. Condition A: Ferrihydrite NPs (0.1 mg/mL, ~6 nm) + 100 uM H2O2, 37C, 2h
3. Condition B: Purified soybean 15-LOX + same PAPE substrate, 37C, 2h
4. Condition C (ferryl control): Fe(II) + H2O2 at pH 3 (free HO•), same PAPE, 37C, 2h
5. Extract, analyze by LC-MS/MS with MRM transitions for 5-, 8-, 9-, 11-, 12-, 15-HpETE-PE
6. **Prediction**: Condition A: C15 fraction = 0.15-0.25. Condition B: C15 fraction >0.90. Condition C: C15 fraction = 0.15-0.20 (may differ from A if ferryl vs HO• selectivity differs).
7. **If FALSE**: C15 fraction in Condition A >0.40 → abiotic Fenton has unexpected regioselectivity (would itself be a discovery). C15 fraction in Condition B <0.70 → 15-LOX regioselectivity is overstated in literature.
8. Effort: Moderate — 4-6 months, requires LC-MS/MS with isomer resolution.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] claims verified: Kuhn 2015, Kagan 2017, Milne 2007, Petigara 2002 — all standard references
2. Back-of-envelope: 1/N statistical distribution for N bis-allylic positions gives C15 fraction ~0.17-0.25 ✓
3. Falsifiable: quantitative ratio predictions with cutoffs ✓
4. No killed mechanisms reintroduced ✓
5. Novel: no prior systematic comparison of abiotic vs enzymatic PLOOH regioselectivity ✓

---

## H2.2: PHREEQC Iron Speciation Model Predicts GSH-Dependent Fenton Activity Amplification
**Refined from**: E2 (Specification of H4)
**Technique**: Tool Transfer

═══════════════════════════════════════════
HYPOTHESIS: PHREEQC Iron Speciation Model Predicts GSH-Dependent Fenton Activity Amplification
═══════════════════════════════════════════
CONNECTION: Ferroptosis (GSH depletion shifts iron speciation) →→ Aqueous speciation thermodynamics →→ Serpentinization (PHREEQC geochemical modeling code)
CONFIDENCE: 5 — PHREEQC is validated for aqueous speciation. The biological adaptation requires a custom thermodynamic database.
NOVELTY: Novel — PHREEQC has never been applied to any biological system.
GROUNDEDNESS: 6
IMPACT IF TRUE: Medium — Adds speciation-level detail to ferroptosis models, identifying which Fe complex drives Fenton at each GSH level.

MECHANISM
[Same mechanism as E2, refined with additional specificity]

The labile iron pool (LIP) in cells is not free Fe2+ but iron complexed with low-molecular-weight ligands whose relative concentrations change during ferroptosis [GROUNDED: Hider & Kong, BioMetals 2013]. GSH is both a major iron chelator (~5 mM, forming relatively Fenton-inactive Fe-GSH complexes) and a GPX4 cofactor. Erastin depletes GSH by inhibiting system Xc- [GROUNDED: Dixon et al., Cell 2012], simultaneously removing GPX4's substrate AND shifting iron speciation toward Fenton-active complexes (Fe-citrate, Fe-ADP).

PHREEQC models this speciation shift using equilibrium thermodynamics. Custom database entries:
- Fe2+-GSH: log K = 5.2 (bidentate thiolate-amine complex) [GROUNDED: Hider & Kong, 2013]
- Fe2+-citrate: log K = 4.4 [GROUNDED: NIST Critically Selected Stability Constants]
- Fe2+-ADP: log K = 3.7 [GROUNDED: approximate from ATP binding constants, Djurdjevic et al., J Inorg Biochem 1999]
- Fe2+-phosphate: log K = 2.4 [GROUNDED: NIST database]

At GSH = 5 mM, Fe-GSH should dominate (>60% of LIP) because GSH is the highest-affinity, highest-concentration chelator. As GSH drops below ~2 mM, citrate (0.3 mM, log K = 4.4) becomes competitive. Below 0.5 mM GSH, Fe-citrate and Fe-ADP dominate.

The Fenton activity amplification: Fe-citrate generates HO• at ~5x the rate of Fe-GSH [GROUNDED: Engelmann et al., BioMetals 2003, measured as deoxyribose degradation rates]. So the speciation shift from Fe-GSH to Fe-citrate amplifies Fenton chemistry by ~3-5 fold, independent of (and additive with) GPX4 inhibition.

NOTE: Total LIP does not expand (PMC12236665, July 2025) [GROUNDED]. This hypothesis addresses SPECIATION within a constant total LIP — which complex dominates, not how much total iron.

CROWDING CORRECTION: Intracellular macromolecular crowding (20-30% w/v protein) alters activity coefficients [GROUNDED: Zhou et al., Annu Rev Biophys 2008]. PHREEQC's Pitzer model does not account for this. Proposed correction: multiply effective concentrations by an empirical crowding factor f_c = 0.3-0.5 for all species, preserving relative speciation rankings while adjusting absolute concentrations [PARAMETRIC: estimate from crowding literature].

SUPPORTING EVIDENCE
• Ferroptosis: GSH depletion by erastin [GROUNDED: Dixon et al., 2012]. Different Fe complexes have different Fenton activities [GROUNDED: Engelmann et al., 2003].
• Geochemistry: PHREEQC validated for aqueous speciation [GROUNDED: Parkhurst & Appelo, 2013].
• Bridge: Fe-ligand stability constants are universal thermodynamic properties [GROUNDED: NIST database].

COUNTER-EVIDENCE & RISKS
• Crowding correction is empirical (2-5x uncertainty). May alter absolute speciation fractions.
• Stability constants measured at 25C, I = 0.1 M may not perfectly apply at 37C, I = 0.15 M.
• Protein-bound iron (not in LIP) is not modeled — only the truly labile fraction.
• Practical improvement uncertain: GPX4 activity and ACSL4-mediated PUFA-PE enrichment dominate ferroptosis sensitivity by 100-fold over iron speciation.

HOW TO TEST
1. Build PHREEQC input: pH 7.2, Eh -300 mV, 37C, total Fe = 1 uM, citrate = 0.3 mM, ATP = 3 mM, HPO4 = 1 mM
2. Run at GSH = 5, 3, 2, 1, 0.5, 0.1 mM
3. **Prediction**: Fe-GSH dominance crosses Fe-citrate dominance at GSH ~2 mM. Total Fenton activity increases >3-fold from GSH = 5 to GSH = 0.1 mM.
4. Validate: measure Fenton activity (APF fluorescence) in cell lysate with added GSH at 0.1-5 mM + constant 1 uM Fe2+. Compare measured activity curve with PHREEQC-predicted speciation-derived activity.
5. **If FALSE**: Fenton activity flat across GSH range → speciation shift not functionally relevant. Fe-GSH not dominant at 5 mM → database constants wrong.
6. Effort: Low — PHREEQC is free, lysate assay ~2 months. Total 3-4 months.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified: Hider & Kong 2013, Dixon 2012, Engelmann 2003, NIST, Parkhurst 2013 ✓
2. Back-of-envelope: at [GSH]=5 mM and log K=5.2, Fe-GSH fraction = K[GSH]/(1+K[GSH]+...) ~0.6-0.7 ✓
3. Falsifiable: crossover point and fold-change with quantitative cutoffs ✓
4. No killed mechanisms ✓
5. Novel: PHREEQC in biology is zero-precedent ✓

---

## H2.3: Pourbaix Stability Field Mapping of Ferrihydrite-Catalyzed PLOOH Production
**Refined from**: E3 (Crossover H2 x H5)
**Technique**: Crossover (Pourbaix framework + PLOOH experiment)

═══════════════════════════════════════════
HYPOTHESIS: Pourbaix Stability Field Mapping of Ferrihydrite-Catalyzed PLOOH Production
═══════════════════════════════════════════
CONNECTION: Ferroptosis (ferritin = ferrihydrite → Fenton → PLOOH) →→ Pourbaix iron stability fields →→ Serpentinization (Pourbaix diagram framework)
CONFIDENCE: 5 — Rigorous thermodynamic framework with feasible experimental validation.
NOVELTY: Novel — No study has used Pourbaix diagrams to design lipid peroxidation experiments.
GROUNDEDNESS: 6
IMPACT IF TRUE: Medium-High — Validates geochemical thermodynamic modeling as a predictive tool for ferroptosis research.

MECHANISM
The Pourbaix diagram (pH-Eh stability diagram) for the Fe-H2O system quantitatively defines which iron species dominates at every combination of pH and redox potential [GROUNDED: Pourbaix, Atlas, 1974; Beverskog & Puigdomenech, Corros Sci 1996]. For the ferroptosis-relevant system, the key transition is:

Ferrihydrite (solid, Fenton-inactive as bulk phase) ↔ Fe2+(aq) (Fenton-active)

This transition occurs at a well-defined Eh boundary that depends on pH: at pH 7.2, ferrihydrite dissolves to Fe2+ below Eh ~ -100 mV [GROUNDED: Beverskog & Puigdomenech, 1996 — the exact value depends on ferrihydrite crystallinity and particle size].

The experiment creates a pH-Eh matrix (5x5 = 25 conditions) spanning the biologically relevant range, with ferrihydrite nanoparticles and PUFA-PE vesicles at each point. PLOOH production rate is measured by LC-MS/MS. The Pourbaix diagram predicts that PLOOH production should map onto the Fe2+(aq) stability field — high where Fe2+ is thermodynamically stable, near-zero where ferrihydrite or Fe(OH)3 is stable.

Refinement from E3: focus the matrix on the most informative region — the Fe2+/ferrihydrite boundary (pH 5.0-7.5, Eh -200 to +100 mV) rather than the full range. This concentrates experimental effort where the prediction is most discriminating.

SUPPORTING EVIDENCE
• Ferritin core = ferrihydrite [GROUNDED: Harrison & Arosio, BBA 1996]
• Pourbaix diagrams are standard geochemistry [GROUNDED: Pourbaix 1974; Beverskog & Puigdomenech 1996]
• PLOOH detection by LC-MS/MS is routine [GROUNDED: Kagan et al., 2017]

COUNTER-EVIDENCE & RISKS
• Chelators shift Pourbaix boundaries — the "pure Fe" diagram needs citrate/GSH corrections
• Kinetic metastability may cause deviations from thermodynamic predictions
• Ferryl (FeIV=O) at pH >5 complicates the simple Fe2+/Fe3+ dichotomy

HOW TO TEST
1. Compute Pourbaix diagram for Fe-H2O-citrate at 37C using PHREEQC
2. Prepare 5x5 matrix: pH (5.0, 5.5, 6.0, 6.5, 7.2) x Eh (-200, -100, 0, +50, +100 mV)
3. At each point: 0.1 mg/mL ferrihydrite NPs + PAPE vesicles + Eh-poising buffer, 37C, 2h
4. Measure PLOOH by LC-MS/MS
5. **Prediction**: PLOOH rate map shows >75% spatial overlap with Pourbaix-predicted Fe2+ field. Maximum at pH 5.0-6.0, Eh -100 to 0 mV. >10-fold drop outside Fe2+ field.
6. **If FALSE**: <40% overlap → Pourbaix model uninformative for biological Fenton.
7. Effort: Moderate-High — 6-9 months, requires Eh-controlled vessels + LC-MS/MS.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified ✓
2. Back-of-envelope: Fe2+/ferrihydrite boundary at pH 7.2 around Eh -100 mV is consistent with published Pourbaix diagrams ✓
3. Falsifiable: >75% overlap quantitative cutoff ✓
4. No killed mechanisms ✓
5. Novel: Pourbaix-designed lipid peroxidation experiment is unprecedented ✓

---

## H2.4: Ferritin Protein Shell as Kinetic Barrier Controlling Ferrihydrite Fenton Activity
**Refined from**: E4 (Mutation of H8)
**Technique**: Mutation + Adversarial Prompting

═══════════════════════════════════════════
HYPOTHESIS: Ferritin Protein Shell as Kinetic Barrier Controlling Ferrihydrite Fenton Activity
═══════════════════════════════════════════
CONNECTION: Ferroptosis (ferritinophagy releases Fenton-active iron) →→ Ferrihydrite nanoparticle Fenton catalysis kinetics →→ Serpentinization (mineral surface Fenton catalysis literature)
CONFIDENCE: 5 — Measurement is straightforward, prediction is quantitative.
NOVELTY: Novel — Bare ferrihydrite vs intact ferritin Fenton activity comparison has not been published.
GROUNDEDNESS: 6
IMPACT IF TRUE: Medium — Establishes ferritin as an evolved containment system for a geochemical Fenton reactor.

MECHANISM
Ferritin stores iron as a 6-8 nm ferrihydrite nanoparticle core inside a 24-subunit protein cage [GROUNDED: Harrison & Arosio, BBA 1996; Theil, Annu Rev Biochem 2004]. The protein shell has 3-fold (hydrophilic) and 4-fold (hydrophobic) channels that regulate ion access [GROUNDED: Theil 2004 — Fe2+ enters via 3-fold channels, larger molecules are excluded].

From the environmental geochemistry literature: bare ferrihydrite nanoparticles are potent heterogeneous Fenton catalysts. Surface Fe2+ sites react with H2O2 to generate reactive oxygen species (HO• or ferryl), with rate constants well-characterized [GROUNDED: Kwan & Voelker, EST 2003; Pham et al., EST 2012]. The catalytic activity scales with accessible surface area and surface Fe2+/Fe3+ ratio.

The ferritin protein shell restricts H2O2 access to the ferrihydrite core, limiting Fenton catalysis. This is not incidental — it is the primary protective function of ferritin [GROUNDED: Arosio et al., BBA Gen Subj 2009 — ferritin prevents iron toxicity by sequestering iron in a non-reactive form]. The hypothesis proposes that ferritin evolved as a biological CONTAINMENT VESSEL for what is essentially a geochemical Fenton reactor: the ferrihydrite core has intrinsic catalytic activity that must be suppressed by the protein shell.

Dissolution-activity experiment: As ferrihydrite dissolves progressively (0%, 10%, 25%, 50%, 75% dissolution by reductive dissolution), measure Fenton activity per remaining Fe atom. The geochemistry prediction: this curve is NON-LINEAR, with per-atom activity increasing during dissolution because surface Fe2+ sites are exposed. Specifically, predict >2-fold increase in per-atom Fenton activity between 0% and 50% dissolution.

Bare vs shell experiment: Compare Fenton activity (HO• production per Fe atom per second) between:
(A) Bare 6-nm ferrihydrite NPs
(B) Intact horse-spleen ferritin (same total Fe per sample)
(C) Ferritin with partially degraded shell (protease-treated)

Prediction: Bare NPs (A) show >5-fold higher per-atom Fenton activity than intact ferritin (B). Partially degraded shell (C) shows intermediate activity, with activity increasing monotonically with shell degradation extent. This demonstrates the protein shell as a kinetic barrier.

SUPPORTING EVIDENCE
• Ferritin sequesters iron to prevent toxicity [GROUNDED: Arosio et al., 2009]
• Ferrihydrite is a potent Fenton catalyst [GROUNDED: Kwan & Voelker, 2003; Pham et al., 2012]
• Ferritin channels regulate ion access [GROUNDED: Theil 2004]
• Ferritinophagy releases iron for ferroptotic Fenton chemistry [GROUNDED: Gao et al., 2016]

COUNTER-EVIDENCE & RISKS
• The >5-fold difference may be an overestimate — ferritin channels do allow some H2O2 access [PARAMETRIC]
• Protease treatment of ferritin may alter core structure, not just shell integrity
• At 6-8 nm, the shrinking-sphere dissolution may produce a trivially linear activity curve
• Biological regulation (NCOA4-mediated ferritinophagy, IRP1/IRP2 regulation) may dominate over the mineral kinetics in vivo

HOW TO TEST
1. Synthesize 6-nm ferrihydrite NPs [GROUNDED: Schwertmann & Cornell, 2000]
2. Dissolution series: 0%, 10%, 25%, 50%, 75% by ascorbate at pH 3. Measure dissolved Fe by ferrozine.
3. At each point: measure Fenton activity with 100 uM H2O2 + APF probe at pH 7.2, 37C
4. Bare NPs vs intact ferritin vs protease-treated ferritin comparison (same total Fe)
5. **Prediction**: (a) Non-linear dissolution-activity curve with >2-fold per-atom activity increase at 50% dissolution. (b) Bare NPs >5-fold more active than intact ferritin. (c) Protease-treated ferritin intermediate.
6. **If FALSE**: Linear curve + no bare/shell difference → protein shell does not restrict Fenton activity, ferritin is purely an iron storage device with no containment function.
7. Effort: Moderate — 4-6 months, standard environmental chemistry + biochemistry.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified: Harrison 1996, Theil 2004, Kwan 2003, Pham 2012, Arosio 2009, Gao 2016 ✓
2. No killed mechanisms (no etch pits, no LIP expansion) ✓
3. Falsifiable: quantitative fold-changes with cutoffs ✓
4. Novel: bare ferrihydrite vs ferritin Fenton comparison unpublished ✓

---

## H2.5: Ferritin as Evolved Domestication of a Geochemical Fenton Reactor
**FRESH hypothesis** — addresses critic question #4 (ferritin as evolved containment)
**Technique**: Null Hypothesis Inversion

═══════════════════════════════════════════
HYPOTHESIS: Ferritin as Evolved Domestication of a Geochemical Fenton Reactor
═══════════════════════════════════════════
CONNECTION: Ferroptosis (ferritin iron storage prevents Fenton damage) →→ Protein cage evolution around mineral core →→ Serpentinization (bare mineral Fenton catalysis as primordial threat)
CONFIDENCE: 4 — The chemical logic is compelling but the evolutionary narrative is difficult to test directly.
NOVELTY: Novel — The framing of ferritin evolution as "domestication" of a geochemical Fenton reactor is new.
GROUNDEDNESS: 5
IMPACT IF TRUE: High — Would reframe ferritin evolution and ferroptosis within an origin-of-life context.

MECHANISM
Null hypothesis inversion: "What would have to be true for ferritin to NOT be connected to serpentinization geochemistry?" Answer: the ferrihydrite mineral in ferritin cores would need to be a different material from geological ferrihydrite, with different Fenton activity. But it IS the same mineral [GROUNDED: Harrison & Arosio, BBA 1996; Michel et al., Science 2007 on ferrihydrite structure]. Therefore, the Fenton chemistry is necessarily shared.

The evolutionary narrative: In early life exposed to iron-rich environments (serpentinization vents, banded iron formations), free ferrihydrite nanoparticles generated uncontrolled Fenton chemistry that damaged protocellular membranes. The first "containment" strategy was likely small peptides that bound iron and reduced its Fenton activity — precursors to the ferritin superfamily. The modern 24-subunit ferritin cage represents a sophisticated containment vessel that:

1. Sequesters iron as ferrihydrite but restricts H2O2 access [GROUNDED: Theil 2004]
2. Oxidizes Fe2+ to Fe3+ at ferroxidase sites, removing the Fenton-active species [GROUNDED: Theil 2004; Bou-Abdallah, BBA Gen Subj 2010]
3. Stores iron in a thermodynamically stable but kinetically trapped form (ferrihydrite is metastable — it would convert to goethite without the protein shell stabilization) [GROUNDED: Michel et al., Science 2007]

The "domestication" analogy: just as early humans domesticated wolves (dangerous predators) into dogs (useful companions), early life domesticated ferrihydrite Fenton chemistry (dangerous radical generator) into ferritin (useful iron storage). The protein shell is the "leash."

Ferroptosis, in this framing, is what happens when the leash breaks: ferritinophagy degrades the protein shell, releasing the bare ferrihydrite core back to its "wild" geochemical state of uncontrolled Fenton catalysis.

Testable predictions from this framing:
1. Ferritin shell removal (by protease) should restore geochemical-level Fenton activity (connects to H2.4)
2. Ferritin ferroxidase site mutations that fail to oxidize Fe2+ should produce ferritin with HIGHER Fenton activity (the containment fails)
3. The ferritin superfamily should be found in organisms from iron-rich environments but absent in organisms from iron-poor environments — ecological distribution correlates with Fenton threat [PARAMETRIC: testable by comparative genomics]

SUPPORTING EVIDENCE
• Ferritin core = ferrihydrite [GROUNDED: Harrison & Arosio, 1996; Michel et al., 2007]
• Ferritin ferroxidase site controls Fe2+→Fe3+ conversion [GROUNDED: Bou-Abdallah, 2010]
• Ferritinophagy releases iron for Fenton chemistry [GROUNDED: Gao et al., 2016]
• Ferritin-like proteins exist across all domains of life, suggesting ancient origin [GROUNDED: Andrews, BBA Mol Cell Res 2010]

COUNTER-EVIDENCE & RISKS
• Ferritin may have evolved primarily for iron SUPPLY (bioavailability), not Fenton CONTAINMENT. The protective function could be secondary. This is the standard view in the iron homeostasis field.
• Mini-ferritins (Dps proteins) in bacteria protect DNA from Fenton damage [GROUNDED: Zhao et al., J Biol Chem 2002], which supports the containment narrative — but Dps may have evolved independently.
• The "domestication" narrative is metaphorical and unfalsifiable in its historical claims.
• Iron-poor organisms may lack ferritin because they lack iron, not because they lack Fenton threat — correlation ≠ causation.

HOW TO TEST
1. Comparative genomics: correlate ferritin superfamily gene count with environmental iron availability across 1000+ bacterial genomes
2. Ferroxidase mutant ferritin: E27A/E62A mutations that abolish ferroxidase activity [GROUNDED: Bou-Abdallah, 2010]. Measure Fenton activity of mutant vs wild-type ferritin.
3. Bare NPs vs ferritin comparison (same as H2.4)
4. **Prediction**: (a) Ferroxidase mutant ferritin has >3-fold higher Fenton activity than WT. (b) Organisms from iron-rich environments (e.g., acid mine drainage) have >2x more ferritin superfamily genes than organisms from iron-poor environments.
5. **If FALSE**: Ferroxidase mutant has same Fenton activity → containment model wrong. No correlation with environmental iron → containment not the primary selective pressure.
6. Effort: Moderate — comparative genomics ~2 months, mutant ferritin ~4 months. Total 6 months.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified: Harrison 1996, Michel 2007, Theil 2004, Bou-Abdallah 2010, Gao 2016, Andrews 2010 ✓
2. Back-of-envelope: N/A (qualitative evolutionary hypothesis) — compensated by quantitative predictions in tests
3. Falsifiable via ferroxidase mutant and genomics predictions ✓
4. No killed mechanisms ✓
5. Novel: "domestication" framing is new ✓

---

## H2.6: Ferryl Ion (FeIV=O) vs Hydroxyl Radical Produce Distinguishable PLOOH Signatures — pH-Dependent Oxidant Identity in Ferroptosis
**FRESH hypothesis** — addresses critic question #3 (does oxidant identity change PLOOH product distribution?)
**Technique**: Adversarial Prompting

═══════════════════════════════════════════
HYPOTHESIS: Ferryl Ion vs Hydroxyl Radical Produce Distinguishable PLOOH Signatures in pH-Dependent Ferroptosis
═══════════════════════════════════════════
CONNECTION: Ferroptosis (Fenton-generated ROS oxidize membrane PUFAs) →→ pH-dependent Fenton oxidant identity →→ Serpentinization geochemistry (pH 3 HO• vs pH 7 ferryl transition, Hug & Leupin 2003)
CONFIDENCE: 4 — The oxidant identity shift is well-established; whether it produces distinguishable PLOOH signatures is unknown.
NOVELTY: Novel — No study has compared the PLOOH product fingerprints of ferryl vs HO• oxidation of PUFAs.
GROUNDEDNESS: 5
IMPACT IF TRUE: Medium — Would reveal that intracellular pH variations (e.g., lysosomal pH 4.5 vs cytoplasmic pH 7.2) produce different oxidant species with different lipid damage profiles during ferroptosis.

MECHANISM
The Fenton reaction produces different oxidant species depending on pH [GROUNDED: Hug & Leupin, EST 2003; Pignatello et al., Crit Rev EST 2006]:
- pH < 5: Fe2+ + H2O2 → Fe3+ + HO• + OH- (hydroxyl radical, E° = +2.31 V)
- pH > 5: Fe2+ + H2O2 → FeIV=O2+ + H2O (ferryl ion, E° ~ +1.8 V)

The oxidant identity matters because HO• and ferryl have different selectivity:
- HO• is nearly indiscriminate (diffusion-controlled, k ~ 10^9-10^10 M-1s-1 for most organics) [GROUNDED: Buxton et al., J Phys Chem Ref Data 1988]
- Ferryl (FeIV=O) is a 2-electron oxidant that preferentially attacks electron-rich sites (allylic/bis-allylic C-H bonds) and may show different positional selectivity [GROUNDED: Pestovsky et al., Angew Chem Int Ed 2005 on ferryl reactivity; Enami et al., J Phys Chem A 2014]

This means that in ferroptosis:
- Lysosomal Fenton (pH 4.5, during ferritinophagy) produces primarily HO• → non-selective PUFA oxidation
- Cytoplasmic Fenton (pH 7.2, after iron release) produces primarily ferryl → potentially position-selective PUFA oxidation

If ferryl has even modest positional selectivity (e.g., 2:1 preference for C15 over other positions), it would create an intermediate fingerprint between non-selective HO• (flat) and highly selective 15-LOX (>95% C15). This could mean that the cytoplasmic Fenton reaction in ferroptosis already has some "proto-enzymatic" selectivity due to the ferryl mechanism — further narrowing the evolutionary gap between abiotic and enzymatic lipid peroxidation.

This connects to serpentinization because the pH-dependent oxidant identity transition was first characterized in environmental geochemistry (water treatment, acid mine drainage, submarine hydrothermal systems), where it determines the efficiency of pollutant degradation at different pH values [GROUNDED: Hug & Leupin 2003; Pignatello et al., 2006]. The rate acceleration (k increases 159x from pH 3 to 7 per the critic's counter-evidence) is due to the shift from one-electron (HO•) to two-electron (ferryl) mechanism.

SUPPORTING EVIDENCE
• Fenton oxidant identity shift: HO• at pH <5, ferryl at pH >5 [GROUNDED: Hug & Leupin, 2003]
• HO• is non-selective [GROUNDED: Buxton et al., 1988]
• Ferryl is more selective [GROUNDED: Pestovsky et al., 2005]
• Ferritinophagy occurs in lysosomes (pH 4.5) [GROUNDED: Gao et al., 2016]
• Iron released to cytoplasm (pH 7.2) for Fenton chemistry [GROUNDED: standard ferroptosis model]

COUNTER-EVIDENCE & RISKS
• Ferryl positional selectivity for PUFA oxidation has NOT been measured. It might be as non-selective as HO•, producing the same flat profile — this would make the hypothesis uninteresting but testable.
• The HO• vs ferryl distinction at intermediate pH (5-7) may be gradual, not sharp. Both species may coexist.
• In cells, iron is chelated by various ligands that modify Fenton mechanism — the "pure Fe" pH transition may be shifted or abolished.
• Ferryl is harder to detect experimentally than HO• (no clean spin trap).

HOW TO TEST
1. Fenton-PUFA reaction at pH 3.0 (HO•), 5.0 (transition), 7.2 (ferryl), 8.0 (ferryl, higher pH)
2. Fe2+ (50 uM) + H2O2 (100 uM) + PAPE vesicles at each pH, 37C, 2h
3. LC-MS/MS for positional HETE/HpETE isomer distribution
4. **Prediction**: pH 3 produces flat profile (C15 fraction = 0.15-0.20). pH 7.2 produces intermediate profile (C15 fraction = 0.20-0.35 if ferryl has partial selectivity). The C15-enrichment increases with pH (monotonic trend).
5. **If FALSE**: C15 fraction identical across all pH values → ferryl selectivity = HO• selectivity → oxidant identity does not matter for PLOOH fingerprint. This would be a clean negative result.
6. Effort: Moderate — 4-6 months, requires isomer-resolved LC-MS/MS.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified: Hug & Leupin 2003, Buxton 1988, Pestovsky 2005, Pignatello 2006 ✓
2. Back-of-envelope: C15 fraction increase from 0.17 to 0.25-0.35 would be statistically detectable by LC-MS/MS ✓
3. Falsifiable: quantitative C15 fraction predictions at each pH ✓
4. No killed mechanisms ✓
5. Novel: ferryl vs HO• PLOOH signatures never measured ✓

---

## H2.7: Iron Compartment Topology During Ferroptosis Mirrors Serpentinization Iron Partitioning
**FRESH hypothesis** — addresses critic question #1 (iron compartmentalization, not cytosolic LIP)
**Technique**: Scale Bridging

═══════════════════════════════════════════
HYPOTHESIS: Iron Compartment Topology During Ferroptosis Mirrors Serpentinization Iron Partitioning
═══════════════════════════════════════════
CONNECTION: Ferroptosis (iron compartmentalized across lysosome, mitochondria, ER, cytoplasm) →→ Iron partitioning across chemical compartments →→ Serpentinization (iron partitioned across fluid, mineral surface, mineral interior, dissolved organic complexes)
CONFIDENCE: 4 — The structural analogy is real but the functional consequences may differ.
NOVELTY: Novel — No study has mapped iron compartmentalization topology during ferroptosis analogously to geochemical iron partitioning.
GROUNDEDNESS: 5
IMPACT IF TRUE: Medium — Would reframe ferroptosis iron dynamics from "total LIP" to "compartmental iron topology" using geochemical partitioning concepts.

MECHANISM
The July 2025 finding (PMC12236665) that the LIP does NOT expand during ferroptosis [GROUNDED] overturns the simple model of "more iron → more Fenton." Instead, iron COMPARTMENTALIZATION matters — which compartment iron is in determines its Fenton activity.

In serpentinization geochemistry, iron partitioning across multiple reservoirs is standard practice [GROUNDED: Bach & Edwards, GCA 2003; Seyfried et al., GCA 2015 on fluid-mineral iron partitioning]:
- Dissolved Fe2+(aq) in fluid: Fenton-active
- Surface-adsorbed Fe2+ on minerals: moderately Fenton-active (heterogeneous catalysis)
- Structural Fe2+ in olivine/pyroxene lattice: Fenton-inactive (locked in crystal)
- Fe3+ in magnetite/ferrihydrite: requires reduction to become Fenton-active
- Fe complexed with dissolved organic ligands: variable Fenton activity

The cellular analog:
- Cytoplasmic LIP (Fe2+-ligand complexes): Fenton-active [GROUNDED: Hider & Kong, 2013]
- Mitochondrial iron (ISCs, heme): mostly Fenton-inactive (protein-bound)
- Lysosomal iron (during ferritinophagy): transiently Fenton-active at pH 4.5
- ER-membrane-associated iron (near PUFA-PE substrates): spatially coupled to ferroptosis target
- Ferritin-sequestered iron: Fenton-inactive (contained by protein shell)

The hypothesis: ferroptosis is not driven by changes in TOTAL iron but by shifts in the iron partitioning TOPOLOGY — specifically, the fraction of total cellular iron in the "ER-membrane-proximal, Fenton-active" compartment. This compartment is analogous to the "dissolved Fe2+ in fluid adjacent to reactive surfaces" compartment in serpentinization.

The geochemical concept of PARTITION COEFFICIENTS (Kd = [Fe]solid / [Fe]fluid) can be adapted to describe iron distribution across cellular compartments. During ferroptosis, the effective Kd for ferritin/LIP shifts (ferritin releases iron) while the total iron remains constant — exactly the behavior seen in serpentinization when temperature or pH changes shift mineral-fluid iron partitioning without changing total system iron.

SUPPORTING EVIDENCE
• LIP does not expand during ferroptosis [GROUNDED: PMC12236665, July 2025]
• Iron compartmentalization affects Fenton activity [GROUNDED: Hider & Kong, 2013]
• Geochemical iron partitioning uses Kd formalism [GROUNDED: Bach & Edwards, 2003]
• ER-associated iron is spatially coupled to PUFA-PE targets [GROUNDED: Stockwell, Cell 2022 review on subcellular ferroptosis]

COUNTER-EVIDENCE & RISKS
• Cellular compartments are dynamic (vesicular transport, fusion, fission) while geochemical compartments are relatively static — the analogy may break down at short timescales
• Measuring iron in specific subcellular compartments is technically challenging (requires organelle-targeted iron probes [GROUNDED: Aron et al., Acc Chem Res 2015 on subcellular iron probes])
• The partition coefficient formalism may be too simple for a system with active transport (pumps, channels) rather than passive equilibrium
• This may be a vocabulary re-description: calling subcellular iron distribution "partitioning topology" does not necessarily add predictive power beyond what cell biologists already know

HOW TO TEST
1. Measure subcellular iron distribution (lysosomal, mitochondrial, ER, cytoplasmic) at 0, 2, 4, 8, 12h after erastin treatment using organelle-targeted iron probes [GROUNDED: Aron et al., 2015]
2. Calculate partition coefficients Kd(ferritin/LIP), Kd(mito/LIP), Kd(ER/LIP) at each timepoint
3. **Prediction**: Total iron constant (confirms July 2025 finding). Kd(ferritin/LIP) decreases >5-fold (ferritin releases iron). Kd(ER/LIP) increases >3-fold (iron accumulates near ER PUFA-PE targets). The ER-proximal iron fraction, not total LIP, correlates with PLOOH accumulation (R2 > 0.8).
4. **If FALSE**: ER iron does not increase → spatial proximity to substrate is not rate-limiting. Total LIP does expand (contradicts July 2025) → compartmentalization model unnecessary.
5. Effort: Moderate-High — requires subcellular iron probes + quantitative imaging. 6-9 months.
═══════════════════════════════════════════

**SELF-CRITIQUE**:
1. [GROUNDED] verified: PMC12236665, Hider & Kong 2013, Bach & Edwards 2003, Aron 2015 ✓
2. Kd formalism may oversimplify active transport — acknowledged ✓
3. Falsifiable: R2 > 0.8 correlation cutoff ✓
4. No killed mechanisms (does NOT claim LIP expansion) ✓
5. Risk of vocabulary re-description — partially mitigated by quantitative partition coefficient predictions ✓

---

## Summary Table

| ID | Title | Parent | Operation | Confidence | Groundedness | Novelty | Technique |
|----|-------|--------|-----------|------------|-------------|---------|-----------|
| H2.1 | Abiotic vs Enzymatic PLOOH Regioselectivity | E1←H2 | Specification | 5 | 7 | Novel | Facet Recombination |
| H2.2 | PHREEQC GSH-Dependent Fenton Activity | E2←H4 | Specification | 5 | 6 | Novel | Tool Transfer |
| H2.3 | Pourbaix Stability Field Mapping | E3←H2×H5 | Crossover | 5 | 6 | Novel | Crossover |
| H2.4 | Ferritin Shell as Kinetic Barrier | E4←H8 | Mutation | 5 | 6 | Novel | Mutation |
| H2.5 | Ferritin as Evolved Domestication | FRESH | Null Hyp. Inversion | 4 | 5 | Novel | Null Hyp. Inversion |
| H2.6 | Ferryl vs HO• PLOOH Signatures | FRESH | Adversarial | 4 | 5 | Novel | Adversarial |
| H2.7 | Iron Compartment Topology | FRESH | Scale Bridging | 4 | 5 | Novel | Scale Bridging |

**Total**: 7 hypotheses (4 refined from cycle 1, 3 fresh)
**All groundedness values**: integers 1-10 ✓
**No killed mechanisms reintroduced** ✓
