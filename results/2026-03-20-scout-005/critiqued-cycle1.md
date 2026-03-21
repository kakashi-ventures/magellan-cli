# Critiqued Hypotheses -- Cycle 1
## Ferroptosis x Serpentinization Geochemistry
**Session**: 2026-03-20-scout-005
**Critic**: Opus 4.6
**Date**: 2026-03-20

---

## CRITICAL CROSS-CUTTING FINDING

Before individual hypothesis analysis, two systemic problems affect multiple hypotheses and must be stated upfront:

**1. Fischer-Tropsch-type (FTT) synthesis does NOT produce polyunsaturated fatty acids (PUFAs).**
Multiple searches confirm that abiotic FTT synthesis under hydrothermal conditions produces predominantly saturated fatty acids (n-alkanoic acids C5-C18+) with no polyunsaturated products. The Rushdi & Simoneit (2001) paper cited across multiple hypotheses reports n-alkanols, n-alkanoic acids, n-alkyl formates, n-alkanals, n-alkanones, n-alkanes, and n-alkenes -- all saturated or monounsaturated at most. There is no evidence for abiotic PUFA production via FTT synthesis. This is critical because PUFA substrates (with bis-allylic hydrogens) are required for the ferroptosis-relevant selectivity that H1, H2, H4, and H7 depend upon.

**2. The Fenton reaction is essentially non-functional at serpentinization pH (9-12).**
At pH > 9, Fe(II) and Fe(III) precipitate as iron hydroxides (Fe(OH)2, Fe(OH)3), removing the dissolved catalyst from solution. Heterogeneous mineral-surface Fenton catalysis can partially compensate, but operates at up to 100x lower turnover frequency than homogeneous Fenton at pH 3-5. The hypotheses acknowledge this but underestimate its severity. The rate calculations in H1, H2, and H4 that use homogeneous Fenton rate constants (~76 M-1s-1 at pH 3) are not valid at pH 9-12.

---

## H1: Serpentinization as an Abiotic Ferroptosis-Analog Selection Filter for Protocellular Membrane Composition

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty Kill**
- Search: "serpentinization ferroptosis lipid peroxidation prebiotic membrane selection" -- 0 results connecting these fields.
- Search: "prebiotic membrane selection PUFA saturated fatty acid oxidation early Earth vesicle" -- extensive prebiotic membrane literature but zero papers connecting ferroptosis-like selectivity to serpentinization.
- **Novelty holds.** No prior work.

**2. Mechanism Kill -- FATAL**
The entire hypothesis depends on PUFA-containing vesicles being selectively destroyed by Fenton chemistry in serpentinization environments. However:
- FTT synthesis does NOT produce PUFAs (see Cross-Cutting Finding #1). The lipid products are saturated and monounsaturated at best.
- Without PUFAs, there is no bis-allylic hydrogen abstraction selectivity (the 65x rate difference requires bis-allylic C-H bonds at ~75 kcal/mol BDE, which only exist in PUFAs with >=2 double bonds).
- Without PUFAs, there is no "ferroptosis-analog" selection pressure. All vesicles would be composed of saturated/monounsaturated lipids and would resist peroxidation roughly equally.
- The Fenton reaction rate constant of ~76 M-1s-1 cited is for pH 3; at serpentinization pH 9-12, dissolved Fe(II) precipitates and this rate is irrelevant.
- The "back-of-envelope" vesicle half-life calculation (minutes vs hours) is built on the false premise that PUFA-rich vesicles exist in this context.

**3. Logic Kill**
The hypothesis draws a structural analogy between ferroptotic PUFA selectivity and prebiotic selection, but this analogy breaks down because the substrate (PUFAs) does not exist in the prebiotic serpentinization context. This is a case of reasoning by analogy from biology to geology without verifying that the substrate basis of the analogy transfers.

**4. Falsifiability Kill**
PASSES -- the test protocol is sound (mix lipids, expose to Fenton conditions, measure survival). But the predicted result (PUFA-enriched vesicles destroyed faster) would test laboratory chemistry, not the prebiotic scenario, since PUFAs would need to be artificially added.

**5. Triviality Kill**
A prebiotic chemist would immediately flag that FTT synthesis does not produce PUFAs, making the "selection" scenario moot.

**6. Counter-Evidence Search**
- Search: "abiotic Fischer-Tropsch synthesis produce only saturated fatty acids no polyunsaturated" -- confirmed that FTT produces only saturated fatty acids.
- Search: "prebiotic membrane selection PUFA" -- prebiotic literature emphasizes saturated C10-C15 amphiphiles as the most prebiotically plausible membrane formers (Deamer & Dworkin 2005 confirms this).
- Search: "Fenton reaction pH 9 10 11 rate constant" -- Fenton essentially non-functional at pH > 9 due to iron precipitation.

**7. Groundedness Attack**
- Dixon et al., Cell 2012: VERIFIED -- real paper on ferroptosis.
- Kagan et al., Nat Chem Biol 2017: VERIFIED -- real paper on PUFA-PE selectivity.
- Porter et al., Lipids 1995: PARTIALLY VERIFIED -- Porter published on lipid peroxidation; the BDE values (~75 kcal/mol bis-allylic) are confirmed by other sources, though the specific 1995 Lipids citation could not be precisely verified.
- McCollom et al., 1999: VERIFIED -- real paper on FTT lipid synthesis.
- Rushdi & Simoneit, 2001: VERIFIED -- real paper.
- Deamer & Dworkin, Top Curr Chem 2005: VERIFIED -- real paper.
- PMID 31836519: **MISCHARACTERIZED** -- the paper studies ferrihydrite nanoparticle effects on membrane FLUIDITY, not "catalysis of lipid peroxidation." The hypothesis claims ferrihydrite nanoparticles "catalyze lipid peroxidation in model membranes" based on this PMID, but the actual paper measures membrane fluidity changes. This is a significant misrepresentation of the source.
- Fenton rate constant "~76 M-1s-1 at 25C": This is for pH 3; not stated in the hypothesis, leading to misleading application at serpentinization pH 9-12.
- Groundedness: ~55% -- mechanism is partly grounded in real chemistry but the critical prebiotic substrate claim (PUFAs from FTT) is FALSE.

**8. Hallucination-as-Novelty Check**
The novelty appears genuine -- no one has proposed this. But the reason no one has proposed it is because prebiotic chemists know FTT synthesis does not produce PUFAs. The hypothesis is novel because the bridge substrate (abiotic PUFAs) does not exist, not because the connection is unexplored.

**9. Claim-Level Fact Verification**
- CLAIM: "Fischer-Tropsch-type (FTT) synthesis during serpentinization produces a distribution of fatty acids including both saturated, monounsaturated, and polyunsaturated species" [GROUNDED: McCollom et al. 1999; Rushdi & Simoneit 2001]
  - **FALSE.** Both McCollom 1999 and Rushdi & Simoneit 2001 report saturated fatty acids. No PUFAs are produced. The hypothesis falsely adds "polyunsaturated" to the list of FTT products and attributes this claim to sources that do not support it. This is a fabricated substrate property grounded in a real citation -- a citation misrepresentation.
- CLAIM: "Ferrihydrite nanoparticles catalyze lipid peroxidation in model membranes [GROUNDED: PMID 31836519]"
  - **MISCHARACTERIZED.** PMID 31836519 measures ferrihydrite effects on membrane fluidity, not lipid peroxidation catalysis.
- CLAIM: "Fenton chemistry rate constants are thermodynamically identical in both contexts (k ~76 M-1s-1 at 25C for Fe2+ + H2O2)"
  - The rate constant value is real but applies at pH ~3. At serpentinization pH 9-12, dissolved iron precipitates and the homogeneous rate is irrelevant.

**REVISED CONFIDENCE**: 1/10
**REVISED GROUNDEDNESS**: 3/10
**KILL REASON**: Fatal mechanism failure -- the substrate (abiotic PUFAs) does not exist in serpentinization environments. FTT synthesis produces only saturated fatty acids. Without PUFAs, the entire selectivity argument collapses. Additionally, PMID 31836519 is mischaracterized and Fenton rates at serpentinization pH are drastically overestimated.

---

## H2: Quantitative Equivalence of Phospholipid Hydroperoxide Chemistry in Ferroptotic and Serpentinizing Systems

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty Kill**
- Search: "PLOOH phospholipid hydroperoxide serpentinization abiotic mineral surface" -- 0 results connecting PLOOH to serpentinization.
- **Novelty holds.** No prior work.

**2. Mechanism Kill -- FATAL (multiple issues)**
- **No PUFA substrate**: PLOOHs in ferroptosis are specifically 15-HpETE-PE and analogous species formed from PUFA-containing phospholipids. FTT synthesis does not produce PUFAs (Cross-Cutting Finding #1). Without PUFA substrates, the specific PLOOH species central to ferroptosis cannot form abiotically.
- **No phospholipids**: The hypothesis itself acknowledges "FTT synthesis primarily produces simple fatty acids, not phospholipids -- the 'PL' in PLOOH may not form abiotically in significant quantities." This is correct and fatal.
- **Thermal instability of PLOOHs**: At 300C (hydrothermal conditions claimed in the hypothesis), organic hydroperoxides decompose rapidly (exothermic peak at ~150C for polymer hydroperoxides). The "PLOOH steady-state" at 300C would be vanishingly small -- not a useful detection target.
- **pH problem**: Fenton chemistry at serpentinization pH 9-12 is drastically reduced (Cross-Cutting Finding #2). The 3700x volumetric production rate calculated by the hypothesis uses homogeneous Fenton constants that do not apply.
- **Propagation rate kp = 62 M-1s-1 at 37C**: This is for linoleate (a PUFA, C18:2). Saturated fatty acids have negligible propagation rates because they lack bis-allylic hydrogens.

**3. Logic Kill**
The hypothesis commits the fallacy of assuming chemical identity implies quantitative equivalence. Even if the same Fenton reaction operates in both systems (which is true in principle), the substrates, pH, temperature, and product stability are so different that claiming "quantitative PLOOH chemical equivalence" is misleading. The chemistry is formally identical but the operating conditions make the outcomes qualitatively different.

**4. Falsifiability Kill**
PASSES -- the test (LC-MS/MS detection of PLOOHs in serpentinization experiments) is well-defined. But the prediction is almost certainly NEGATIVE given the substrate and stability problems.

**5. Triviality Kill**
The statement "Fenton chemistry produces the same intermediates regardless of context" is trivially true for a named chemical reaction. The non-trivial claim is that the specific biological PLOOH species would appear in geology, which fails on substrate grounds.

**6. Counter-Evidence Search**
- Search: "lipid hydroperoxide thermal stability 100 200 300 degrees" -- hydroperoxides decompose rapidly above ~80C (exothermic peak at 150C). At 300C, PLOOH half-life would be seconds to minutes, making steady-state accumulation negligible.
- Search: "Fenton reaction alkaline pH 9 10 11 efficiency rate" -- at pH > 10, Fe2+-complexes cannot activate H2O2 to produce hydroxyl radicals; iron precipitates.

**7. Groundedness Attack**
- Kagan et al., 2017: VERIFIED.
- Stockwell et al., Cell 2017: VERIFIED.
- Howard & Ingold, 1967: VERIFIED (published in Can J Chem on hydrocarbon autoxidation rate constants).
- PMID 31836519: **MISCHARACTERIZED** (same issue as H1 -- membrane fluidity, not lipid peroxidation catalysis).
- Bach & Edwards, GCA 2003: PARTIALLY VERIFIED (Bach has published extensively on serpentinization in GCA; exact 2003 paper not independently confirmed but plausible).
- McCollom et al., 1999: VERIFIED.
- Groundedness: ~50% -- the ferroptosis chemistry is well-grounded, but the geological substrate claims are false and the bridge calculation uses inapplicable rate constants.

**8. Hallucination-as-Novelty Check**
The bridge mechanism (Fenton chemistry) exists independently. The novelty claim -- that PLOOH speciation should be identical -- is a logical deduction from shared chemistry. However, the deduction ignores that the substrates differ fundamentally (PUFAs vs. saturated FAs). The novelty is an artifact of ignoring substrate requirements.

**9. Claim-Level Fact Verification**
- CLAIM: "kp = 62 M-1s-1 at 37C for linoleate" -- Linoleate propagation rate constants are well-established in the lipid peroxidation literature. VERIFIED as a general claim, though the specific value may vary slightly by source.
- CLAIM: "Fenton rate ratio k(serp)/k(bio) = 2.8x net" -- This was from computational validation and applies only to the homogeneous Fenton step, not to the overall system at serpentinization pH. MISLEADING without pH correction.
- CLAIM: "volumetric PLOOH production rate in serpentinization could be ~3700x higher" -- **FALSE as stated.** The calculation (1333x Fe x 2.8x rate) ignores: (a) pH-dependent iron precipitation, (b) absence of PUFA substrate, (c) thermal decomposition of PLOOHs. The actual rate would be orders of magnitude lower.

**REVISED CONFIDENCE**: 2/10
**REVISED GROUNDEDNESS**: 3/10
**KILL REASON**: Fatal on multiple axes -- (1) no PUFA substrate from FTT, (2) no phospholipids from FTT, (3) PLOOH thermal instability at 300C, (4) Fenton rate calculation invalid at pH 9-12. The hypothesis correctly identifies shared chemistry in principle but fails catastrophically on substrate availability and reaction conditions.

---

## H3: Serpentinization-Derived H2 as a Primordial Anti-Peroxidation Reductant Preceding Biological Antioxidant Systems

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "hydrogen H2 serpentinization antioxidant lipid peroxidation primordial" -- no direct papers proposing H2 as a primordial anti-ferroptotic agent. Papers discuss serpentinization H2 as energy source for metabolism, not as a direct radical scavenger/reductant for lipid peroxidation.
- **Novelty holds.**

**2. Mechanism Kill -- SERIOUS CONCERNS but not fatal**
- The hypothesis correctly identifies the kinetic barrier: H2 + LOO is negligibly slow (<1 M-1s-1 at 37C). The hypothesis frames H2 as a "thermodynamic buffer" rather than kinetic scavenger, which is more defensible.
- However, thermodynamic buffering requires equilibrium. In an open serpentinization system with continuous radical generation, equilibrium may never be reached; the kinetically inert H2 would not reduce steady-state PLOOH levels.
- Metal-catalyzed H2 activation on Fe or Ni surfaces is plausible but adds an additional unverified step.
- The "redox sanctuary" concept is qualitatively reasonable but the quantitative impact is uncertain.
- This hypothesis has fewer substrate problems than H1/H2/H4 because it focuses on the reductant side (H2) rather than specific lipid substrates. The membrane peroxidation it discusses could involve saturated lipids too (at much lower rates), making the H2 protection relevant even without PUFAs.

**3. Logic Kill**
The evolutionary narrative (protocells migrate away from H2 source, become vulnerable, evolve enzymatic antioxidants) is a plausible just-so story but unfalsifiable in its historical claims. However, the chemical prediction (H2 reduces PLOOH accumulation in presence of mineral catalysts) is testable.

**4. Falsifiability Kill**
PASSES -- the test protocol (compare PLOOH accumulation in H2-saturated vs N2-purged conditions with mineral catalysts) is well-defined and would produce a clear positive or negative result.

**5. Triviality Kill**
Not trivial. The connection between serpentinization H2 and lipid peroxidation protection is not obvious to either field.

**6. Counter-Evidence Search**
- Search: "hydrogen H2 serpentinization antioxidant lipid peroxidation" -- no direct counter-evidence found. The general point that H2 is kinetically inert as a radical scavenger is well-known but the hypothesis already acknowledges this.
- The hypothesis's own counter-evidence section is honest and thorough.

**7. Groundedness Attack**
- Yang et al., Cell 2014: VERIFIED.
- Stockwell et al., Cell 2017: VERIFIED.
- Kelley et al., Science 2005: VERIFIED -- H2 concentrations at Lost City of 1-15 mM confirmed by multiple sources.
- McCollom & Bach, GCA 2009: VERIFIED (well-known serpentinization reference).
- Friedmann Angeli et al., Nat Cell Biol 2014: VERIFIED -- GPX4 knockout causes lethal ferroptosis.
- E(H2/H+) = -0.414 V: VERIFIED -- standard electrochemistry.
- H2 + OH rate ~4 x 10^7 M-1s-1: VERIFIED (well-established radical chemistry).
- Groundedness: ~75% -- most claims are well-grounded. The weakest claims are the quantitative "redox sanctuary" predictions and the mineral-catalyzed H2 activation step.

**8. Hallucination-as-Novelty Check**
Low hallucination risk. H2 production in serpentinization is real and well-quantified. The kinetic barrier is honestly acknowledged. The novelty lies in proposing H2 as a prebiotic protector against lipid peroxidation, which is genuinely unexplored.

**9. Claim-Level Fact Verification**
- CLAIM: "H2 concentrations at active serpentinization sites reach 1-16 mM [GROUNDED: Kelley et al., Science 2005]" -- VERIFIED (1-15 mM at Lost City).
- CLAIM: "E(H2/H+) = -0.414 V at pH 7" -- VERIFIED.
- CLAIM: "Rate constant for H2 + OH = ~4 x 10^7 M-1s-1 (fast)" -- VERIFIED.
- CLAIM: "GPX4 knockout is lethal in mice [GROUNDED: Friedmann Angeli et al., Nat Cell Biol 2014]" -- VERIFIED.
- All checked [GROUNDED] claims verify. No citation hallucinations detected.

**REVISED CONFIDENCE**: 3/10 (down from 4)
**REVISED GROUNDEDNESS**: 6/10 (up from 5)
**SURVIVAL NOTE**: Survives as WOUNDED because the chemical claims are honest and well-grounded, but the kinetic inertness of H2 as a radical scavenger is a serious problem. The hypothesis acknowledges this and proposes mineral-catalyzed H2 activation as a workaround, but this adds an unverified step. The evolutionary narrative is unfalsifiable but the core chemical prediction is testable. The weakest hypothesis to survive but the intellectual honesty earns it a pass.

---

## H4: Fenton-Driven LLPS as a Shared Membrane Reorganization Mechanism in Both Ferroptotic and Prebiotic Systems

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty Kill**
- Search: "Fenton LLPS liquid-liquid phase separation prebiotic membrane" -- LLPS in prebiotic contexts has been discussed (Zwicker et al., Nat Phys 2017), but not via Fenton-driven lipid peroxidation. No direct hit.
- Search: "Balakrishnan Kenworthy JACS 2024 Fenton lipid peroxidation LLPS" -- VERIFIED. The JACS 2024 paper is real (Balakrishnan & Kenworthy, JACS 146(2): 1374-1387, 2024). It shows Fenton-induced lipid peroxidation drives LLPS in giant plasma membrane vesicles.
- **Novelty partially holds.** The biological LLPS-Fenton connection is established (2024); the extension to prebiotic systems is novel.

**2. Mechanism Kill -- FATAL (substrate + temperature)**
- **No PUFA substrate in prebiotic context**: LLPS in the JACS 2024 study was observed in giant plasma membrane vesicles (GPMVs) containing biological lipids, including abundant PUFAs and cholesterol. Prebiotic vesicles from FTT synthesis would contain only saturated fatty acids -- fundamentally different composition.
- **Temperature kills phase separation**: The hypothesis proposes LLPS at serpentinization temperatures (100-300C). The critical mixing temperature for lipid membranes is typically 30-80C; above this, lipid mixtures are fully miscible. At 100-300C, there can be no liquid-ordered/liquid-disordered phase separation because the system is far above the miscibility boundary. The hypothesis itself acknowledges this risk.
- **Compositional complexity insufficient**: LLPS in membranes requires at least two lipid types with different miscibility behavior (typically saturated + unsaturated + cholesterol in biological membranes). FTT products are predominantly saturated, lacking the compositional asymmetry needed for phase separation.

**3. Logic Kill**
The hypothesis extrapolates from a biological membrane system (GPMVs with cholesterol, sphingomyelin, PUFAs) to a prebiotic system (simple fatty acid vesicles) without verifying that the physical prerequisites for LLPS transfer. This is analogy masquerading as mechanism.

**4. Falsifiability Kill**
PASSES -- the GUV fluorescence microscopy experiment is well-designed.

**5. Triviality Kill**
A membrane biophysicist would immediately object that LLPS requires compositional complexity and temperatures below the critical mixing point -- both absent in the prebiotic scenario.

**6. Counter-Evidence Search**
The Balakrishnan & Kenworthy JACS 2024 paper itself is conducted at biological temperatures (~37C) with biological membranes. Extrapolation to 100-300C with simple fatty acid vesicles is not supported by the paper's findings.

**7. Groundedness Attack**
- JACS 2024 (Balakrishnan & Kenworthy): VERIFIED.
- Agmon et al., Nat Chem Biol 2018: **CITATION ERROR.** Agmon et al. 2018 was published in Scientific Reports (Sci Rep 8:5155), NOT Nature Chemical Biology. This is a journal misattribution. The paper is real but the journal is wrong. Nature Chemical Biology published a 2017 paper by Kagan et al. on oxidized PEs -- these are different papers. This counts as a minor citation error (paper exists but journal is wrong).
- PMID 31836519: **MISCHARACTERIZED** (same issue as H1/H2).
- McCollom et al., 1999: VERIFIED.
- Flory-Huggins chi parameter discussion: correct physics in principle, but the specific values cited (area per headgroup ~0.65 nm2 to ~0.85 nm2 upon peroxidation, miscibility threshold ~15-25 mol%) appear to be parametric knowledge claims that could not be precisely verified. The general trend is correct but exact values are uncertain.
- Groundedness: ~50% -- biological side well-grounded, prebiotic extension poorly grounded. One citation journal error.

**8. Hallucination-as-Novelty Check**
The biological phenomenon (Fenton-driven LLPS) is real and verified. The novelty is in extending it to prebiotic systems. This extension fails because the prerequisites (PUFA substrates, cholesterol, temperatures below critical mixing) do not transfer.

**9. Claim-Level Fact Verification**
- CLAIM: "Fenton-induced lipid peroxidation drives LLPS in biological membranes [GROUNDED: JACS 2024]" -- VERIFIED.
- CLAIM: "Oxidized lipid domains have altered thickness, curvature, and permeability [GROUNDED: Agmon et al., Nat Chem Biol 2018]" -- Paper is REAL but published in **Scientific Reports**, not Nature Chemical Biology. JOURNAL MISATTRIBUTION.
- CLAIM: "Ferrihydrite catalyzes lipid peroxidation [GROUNDED: PMID 31836519]" -- MISCHARACTERIZED (measures fluidity, not peroxidation).
- CLAIM: "Area per headgroup increases from ~0.65 nm2 to ~0.85 nm2 upon peroxidation" -- UNVERIFIED specific values; the direction of the change is consistent with known physics but exact numbers could not be confirmed.

**REVISED CONFIDENCE**: 2/10
**REVISED GROUNDEDNESS**: 4/10
**KILL REASON**: Fatal mechanism failure on three axes -- (1) no PUFA substrate in prebiotic vesicles, (2) temperatures far above critical mixing point eliminate phase separation, (3) insufficient compositional complexity in FTT-derived lipids. Additionally, one journal misattribution (Agmon et al.) and one mischaracterized reference (PMID 31836519).

---

## H5: Serpentinite Mineral Phase Transition Sequences as a Thermodynamic Framework for Resolving Iron Speciation Dynamics in Ferroptosis

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "Pourbaix diagram intracellular iron speciation ferritin ferroptosis" -- no papers found applying Pourbaix diagrams to intracellular iron during ferroptosis. Ferroptosis literature treats iron speciation qualitatively, not with geochemical stability diagrams.
- **Novelty holds.**

**2. Mechanism Kill -- minor concerns**
- The analogy between ferritin-core ferrihydrite and geological ferrihydrite is chemically sound -- it IS the same mineral.
- Pourbaix diagrams are genuinely applicable to any aqueous Fe system, including intracellular environments -- the thermodynamics are universal.
- However, intracellular iron is heavily chelated by proteins, citrate, phosphate, GSH, etc. These chelators shift the stability fields dramatically. A Pourbaix diagram for "pure Fe in water" would not accurately predict speciation in cytoplasm with mM levels of chelators. This is a serious but not fatal limitation -- it means the geochemical framework would need significant modification for biological application.
- The ferritinophagy prediction (dissolution in acidic lysosomes, reduction upon cytoplasmic release) is qualitatively correct and could be quantitatively refined by Pourbaix analysis.

**3. Logic Kill**
No major logical fallacy. The hypothesis correctly identifies that Pourbaix diagrams are universal thermodynamic tools applicable to any aqueous iron system. The extension to intracellular iron is methodologically sound, with caveats about complexity.

**4. Falsifiability Kill**
PASSES strongly -- the test (compare Pourbaix predictions with Mossbauer/XAS measurements of iron speciation during ferroptosis) is clear, quantitative, and would decisively confirm or refute the hypothesis.

**5. Triviality Kill**
A geochemist might say "obviously Pourbaix diagrams apply to any Fe system." But the specific application to ferroptotic iron speciation dynamics has not been done, and ferroptosis researchers do not use these tools. The cross-pollination is non-trivial.

**6. Counter-Evidence Search**
- The hypothesis itself identifies the key counter-argument: intracellular chelators modify effective iron speciation away from the "pure Fe" Pourbaix diagram. This is honest and accurate.
- No published work was found explicitly arguing against applying Pourbaix diagrams to biological iron. The absence of such work likely reflects that no one has tried, not that it has been disproven.

**7. Groundedness Attack**
- Gao et al., Autophagy 2016: VERIFIED (ferritinophagy drives ferroptosis via NCOA4).
- Hou et al., Autophagy 2016: Exists in the ferritinophagy/ferroptosis literature. VERIFIED.
- Harrison & Arosio, BBA 1996: VERIFIED (landmark ferritin review, BBA 1275:161-203).
- Pourbaix, Atlas of Electrochemical Equilibria, 1974: VERIFIED (foundational reference).
- Frost & Beard, JGR 2007: **JOURNAL ERROR.** The paper was published in **Journal of Petrology** (J Petrol 48:1351-1368, 2007), NOT Journal of Geophysical Research (JGR). Paper is real; journal is wrong.
- Klein et al., Lithos 2013: VERIFIED (Klein, Bach & McCollom on compositional controls on H2 generation during serpentinization).
- Groundedness: ~70% -- most claims verified. One journal misattribution. The intracellular complexity caveat is honestly acknowledged.

**8. Hallucination-as-Novelty Check**
Low hallucination risk. Both components (Pourbaix diagrams, ferritin-as-ferrihydrite, ferritinophagy) exist independently and are well-documented. The novelty is in the connection, not in fabricated properties.

**9. Claim-Level Fact Verification**
- CLAIM: "Ferritin core IS ferrihydrite [GROUNDED: Harrison & Arosio, BBA 1996]" -- VERIFIED. This is a well-established fact in biomineralization.
- CLAIM: "Ferritinophagy releases iron from ferritin cores, feeding the LIP [GROUNDED: Gao et al., Autophagy 2016]" -- VERIFIED.
- CLAIM: "Mineral phase transitions: olivine Fe2+ -> dissolved Fe2+(aq) -> magnetite -> ferrihydrite -> goethite -> hematite [GROUNDED: Frost & Beard, JGR 2007]" -- The mineral sequence is correct and well-established in serpentinization geochemistry. JOURNAL WRONG (J Petrol, not JGR), but the content is verified.
- CLAIM: "Ferrihydrite should be thermodynamically unstable in the reducing cytoplasmic environment (Eh < -200 mV at pH 7.2)" -- This is a Pourbaix diagram prediction and is directionally correct: at pH 7.2 and Eh -300 mV, Fe2+(aq) is predicted to dominate over Fe(III) solid phases. VERIFIED by standard Pourbaix analysis.

**REVISED CONFIDENCE**: 5/10 (down from 6)
**REVISED GROUNDEDNESS**: 6/10 (same)
**SURVIVAL NOTE**: This is the strongest hypothesis because it transfers a validated analytical framework (Pourbaix diagrams) rather than claiming substrate equivalence. The ferritin=ferrihydrite connection is real. The main weakness is that intracellular chelators will modify the stability fields, requiring parameterization. One journal citation error (J Petrol, not JGR) is notable but does not invalidate the science. Strongest reason to kill: intracellular complexity may make the geochemical framework uninformative compared to more targeted biochemical models.

---

## H6: Geochemical Arrhenius Parameters for Fenton-Lipid Peroxidation Predict Therapeutic Temperature Windows in Ferroptosis

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill -- PARTIALLY COMPROMISED**
- Search: "Arrhenius Fenton reaction temperature ferroptosis therapeutic hypothermia" -- found multiple relevant papers:
  - "Targeted temperature management alleviates post-resuscitation myocardial dysfunction by inhibiting ferroptosis" (Cell Death Discovery, 2025) -- TTM at 33C inhibits ferroptosis via suppressing ferritinophagy.
  - "Cold resistance of mammalian hibernators -- a matter of ferroptosis?" (Front Physiol, 2024) -- cold-induced ferroptosis is an active research area.
  - "Photothermia at the nanoscale induces ferroptosis via nanoparticle degradation" (Nat Commun, 2023) -- temperature enhancement of Fenton reaction used therapeutically.
- The temperature-ferroptosis connection is NOT novel. Multiple groups have already shown that temperature modulates ferroptosis. The SPECIFIC claim that geochemical Arrhenius parameters provide quantitative predictions is more novel, but the general concept (temperature affects Fenton rate affects ferroptosis) is already being explored.
- **Novelty downgraded to "extension of partially explored territory."**

**2. Mechanism Kill -- moderate concerns**
- The Arrhenius calculation is mathematically correct: Ea ~42 kJ/mol gives ~4%/degree near 37C.
- However, the 4%/degree effect is SMALL compared to biological variability in ferroptosis sensitivity. The hypothesis acknowledges this: "small compared to biological variability in ferroptosis sensitivity (which varies >10x between cell types)."
- Temperature also affects GPX4 activity, ACSL4 activity, membrane fluidity, oxygen solubility, and dozens of other biological processes. Isolating the Fenton rate contribution from the confounding biological temperature effects is extremely difficult.
- The claim that geochemical data provides BETTER Arrhenius parameters than could be obtained from direct biological measurements is questionable. Why would you need serpentinization-derived rate constants when you can measure Fenton kinetics directly at 33-42C in the lab?

**3. Logic Kill**
The hypothesis implicitly argues that geochemical high-temperature data (25-400C) provides better Arrhenius fits than direct measurement at biological temperatures (33-42C). This is backwards -- if you want to know the Fenton rate at 37C, you measure it at 37C. Wide-temperature Arrhenius extrapolation is LESS accurate for a narrow window than direct measurement. The serpentinization connection adds no methodological value over standard chemistry.

**4. Falsifiability Kill**
PASSES -- the cell-free system test (compare measured vs. predicted temperature dependence) is well-designed.

**5. Triviality Kill**
A chemical kineticist would say "obviously Arrhenius kinetics apply to Fenton chemistry at any temperature." A clinical researcher would say "obviously hypothermia slows radical reactions." The hypothesis packages known facts (Arrhenius applies to Fenton; hypothermia is neuroprotective) with a serpentinization wrapper that adds no explanatory value.

**6. Counter-Evidence Search**
- Search: "targeted temperature management ferroptosis hypothermia 33 degrees" -- TTM at 33C already shown to inhibit ferroptosis (Cell Death Discovery, 2025). This is direct evidence that the temperature-ferroptosis link is already known.
- Search: "hibernation torpor hypothermia ferroptosis resistance cold" -- active field. GPX4 is identified as the key cold-resistance factor in hibernators (Front Physiol, 2024). Temperature-dependent ferroptosis is being studied without any geochemical framework.

**7. Groundedness Attack**
- De Laat & Gallard, EST 1999: VERIFIED (catalytic decomposition of H2O2 by Fe(III) in homogeneous solution, EST 33:2726-2732).
- Howard & Ingold, Can J Chem 1967: VERIFIED (autoxidation rate constants).
- Bernard et al., NEJM 2002: VERIFIED (therapeutic hypothermia after cardiac arrest).
- Tuo et al., ATVB 2017: **JOURNAL ERROR.** Tuo et al. 2017 was published in **Molecular Psychiatry** (Mol Psychiatry 22:1520-1530), NOT ATVB. The paper is about tau-mediated iron export preventing ferroptotic damage after ischemic stroke. Real paper, wrong journal.
- Ea ~40-50 kJ/mol for Fenton: VERIFIED as a reasonable range from the environmental chemistry literature.
- Groundedness: ~70% -- most claims verified. One journal misattribution (Tuo 2017).

**8. Hallucination-as-Novelty Check**
The bridge mechanism (Arrhenius kinetics) is real. The connection to ferroptosis is real. But the novelty is low because temperature-dependent ferroptosis is already being actively studied. The "serpentinization" framing adds rhetorical novelty but not scientific novelty.

**9. Claim-Level Fact Verification**
- CLAIM: "Ea = 40-50 kJ/mol for Fe2+ + H2O2 [GROUNDED: De Laat & Gallard, EST 1999]" -- VERIFIED range from environmental chemistry. Exact Ea may vary with conditions.
- CLAIM: "k(42C)/k(37C) = 1.22 (22% increase at fever temperature)" -- Mathematically correct given Ea = 42 kJ/mol. VERIFIED by Arrhenius calculation.
- CLAIM: "Ferroptosis contributes to ischemia-reperfusion injury [GROUNDED: Tuo et al., ATVB 2017]" -- Paper is real but in Molecular Psychiatry, NOT ATVB. JOURNAL MISATTRIBUTION. Content claim is verified.
- CLAIM: "Therapeutic hypothermia (33C) is neuroprotective after cardiac arrest [GROUNDED: Bernard et al., NEJM 2002]" -- VERIFIED.

**REVISED CONFIDENCE**: 4/10 (down from 6)
**REVISED GROUNDEDNESS**: 6/10 (down from 7)
**SURVIVAL NOTE**: The chemistry is correct but the hypothesis has low novelty (temperature-ferroptosis link already being studied), low added value (geochemical Arrhenius data does not improve on direct measurement), and a triviality problem (Arrhenius applies to everything). It survives as WOUNDED because the quantitative prediction (4%/degree) is testable and the specific framing of optimal hypothermia targets from Ea is somewhat novel, but the serpentinization connection is forced. One journal misattribution (Tuo 2017). Strongest reason to kill: this is essentially "Arrhenius kinetics apply to the Fenton reaction" dressed in geochemical clothing, and the temperature-ferroptosis link is already being explored without geochemistry.

---

## H7: Abiotic Lipid Peroxidation Products from Serpentinization as Confounding False Positives for Ferroptotic Biosignatures in Astrobiology

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "abiotic lipid peroxidation products biosignature astrobiology false positive" -- found related work on distinguishing biotic from abiotic organics on ocean worlds:
  - "Distinguishing Potential Organic Biosignatures on Ocean Worlds from Abiotic Geochemical Products using Thermodynamic Calculations" (ChemRxiv, 2024) -- uses thermodynamic approaches to distinguish biotic from abiotic organics on Enceladus. Does NOT specifically discuss lipid peroxidation products but establishes the general false-positive concern.
  - General abiotic-organic false positive concern is well-established in astrobiology.
- The SPECIFIC claim about ferroptosis biomarkers (4-HNE, MDA, isoprostanes) as false positives has NOT been published. **Novelty of the specific claim holds.**

**2. Mechanism Kill -- SERIOUS substrate problem**
- **FTT synthesis does not produce PUFAs** (Cross-Cutting Finding #1). 4-HNE requires omega-6 PUFA substrates (linoleic acid, arachidonic acid). MDA requires PUFAs with >=3 double bonds. F2-isoprostanes specifically require arachidonic acid (C20:4). None of these substrates are produced by FTT synthesis.
- However, the hypothesis is partially saved by an important distinction: some lipid peroxidation products (MDA-like short-chain aldehydes, simple epoxides) CAN form from monounsaturated or even saturated lipids at very high temperatures and radical fluxes, just at much lower rates and different product distributions.
- The isoprostane argument is the strongest specific claim -- isoprostanes are EXCLUSIVELY derived from PUFAs (specifically arachidonic acid) by free radical peroxidation. Without abiotic arachidonic acid, there are no abiotic isoprostanes on Enceladus. This eliminates the primary biosignature-confusion scenario.
- MDA and 4-HNE are the most specific ferroptosis markers, and both require PUFA precursors. Their absence from abiotic systems actually STRENGTHENS their value as biosignatures, the opposite of the hypothesis claim.

**3. Logic Kill**
The hypothesis argues that DETECTION of lipid peroxidation products on ocean worlds would be ambiguous between biotic and abiotic origins. But if the specific products (4-HNE, isoprostanes) require PUFA substrates that are only produced biologically, then their detection would be EVIDENCE FOR biology, not confused by abiotic chemistry. The hypothesis has the direction wrong for the most specific markers.

**4. Falsifiability Kill**
PASSES -- test is well-defined (run serpentinization experiments, analyze for 4-HNE/MDA/isoprostanes).

**5. Triviality Kill**
The general concept "abiotic chemistry can produce molecules that look biological" is well-established in astrobiology. The specific application to ferroptosis markers has some novelty.

**6. Counter-Evidence Search**
- Search: "Europa Enceladus lipid biosignature abiotic organic molecule false positive astrobiology 2024 2025" -- found ChemRxiv 2024 preprint on thermodynamic approaches to distinguish biotic from abiotic organics. Also found machine learning approaches (2025) for distinguishing biotic mimicry.
- The astrobiology community is already actively addressing the general false-positive problem, though not specifically for ferroptosis biomarkers.

**7. Groundedness Attack**
- Ayala et al., Oxid Med Cell Longev 2014: VERIFIED (review of lipid peroxidation products).
- Kagan et al., Nat Chem Biol 2017: VERIFIED.
- Morrow et al., PNAS 1990: VERIFIED (F2-isoprostanes as non-enzymatic products, PNAS 87:9383-9387). The paper specifically establishes that F2-isoprostanes form from arachidonic acid by non-cyclooxygenase, free radical-catalyzed mechanism. Key point: "non-enzymatic" does NOT mean "abiotic" -- these still require arachidonic acid (a PUFA), which is biologically derived.
- Esterbauer et al., Free Rad Biol Med 1991: VERIFIED (landmark review on 4-HNE).
- Hsu et al., Nature 2015: VERIFIED (Cassini silica nanoparticles, serpentinization on Enceladus).
- McCollom et al., 1999: VERIFIED.
- Groundedness: ~65% -- most citations verified, but the critical inference (FTT lipids can produce ferroptosis-specific products) is UNVERIFIED and likely incorrect.

**8. Hallucination-as-Novelty Check**
The individual components are all real. The novel claim -- that serpentinization would produce molecules indistinguishable from ferroptosis biomarkers -- fails because the specific biomarkers require PUFA precursors not available abiotically. The apparent novelty is partly an artifact of ignoring substrate requirements.

**9. Claim-Level Fact Verification**
- CLAIM: "F2-isoprostanes form by free radical-catalyzed peroxidation of arachidonic acid without enzymatic involvement [GROUNDED: Morrow et al., PNAS 1990]" -- VERIFIED. But "without enzymatic involvement" is not the same as "without biological precursors." Arachidonic acid itself is biogenic.
- CLAIM: "Fe2+ from olivine hydration [GROUNDED: Hsu et al., Nature 2015]" -- VERIFIED for Enceladus.
- CLAIM: "O2 or H2O2 from water radiolysis [GROUNDED: radiation processing of ice on Europa]" -- VERIFIED as a general radiation chemistry claim.
- CLAIM: "Lipids from Fischer-Tropsch-type synthesis [GROUNDED: McCollom et al., 1999]" -- VERIFIED that FTT produces SATURATED lipids. PUFAs are NOT produced. The hypothesis's inference that these lipids would produce 4-HNE, MDA, and isoprostanes is INCORRECT.

**REVISED CONFIDENCE**: 4/10 (down from 7)
**REVISED GROUNDEDNESS**: 5/10 (down from 7)
**SURVIVAL NOTE**: The hypothesis survives as WOUNDED because the CONCEPT of false-positive organic biosignatures is important and the cross-fertilization between ferroptosis detection methods and astrobiology is genuinely useful. However, the specific claim that ferroptosis biomarkers (4-HNE, MDA, isoprostanes) would be produced abiotically is undermined by the absence of PUFA substrates in FTT synthesis. The hypothesis could be RESCUED by refocusing on simpler lipid peroxidation products (short-chain aldehydes, epoxides) that CAN form from saturated lipids, though these are less specific to ferroptosis. The general warning ("abiotic Fenton chemistry produces SOME lipid oxidation products that missions should account for") retains value even if the specific ferroptosis-marker claims fail. Strongest reason to kill: the most specific ferroptosis biomarkers (isoprostanes, 4-HNE) require PUFAs not produced abiotically, actually strengthening their biosignature value rather than undermining it.

---

## H8: Iron Nanoparticle Surface-Area-to-Volume Scaling from Serpentinite Petrology Predicts Ferroptotic Chain Propagation Efficiency

**VERDICT: WOUNDED**

### ATTACKS:

**1. Novelty Kill**
- Search: "ferrihydrite nanoparticle surface area dissolution Fenton catalysis efficiency" -- found papers on ferrihydrite as heterogeneous Fenton catalyst (specific surface area ~297.5 m2/g reported for ferrihydrite). Found work on dissolution mechanisms and catalytic efficiency. But no papers applying mineral weathering dissolution models to ferritin-core Fenton catalysis.
- **Novelty holds.**

**2. Mechanism Kill -- moderate concerns**
- Ferrihydrite surface area dependence on Fenton catalysis is well-established in environmental chemistry. The transfer to ferritin cores is plausible because ferritin cores ARE ferrihydrite.
- The "Swiss cheese" dissolution model from mineral weathering is real (Luttge 2005 on etch pit coalescence and surface area).
- However, ferritin protein shell constrains the dissolution geometry. Lysosomal proteases first degrade the protein shell, then acidic pH dissolves the iron core. This is not analogous to geological weathering of exposed mineral surfaces. The ferritin shell acts as a rate-limiting membrane, and once breached, iron dissolution proceeds through different mechanisms than etch pit formation.
- The 3-4x enhancement prediction (150 m2/g intact to 400-600 m2/g at 50% dissolution) is reasonable for geological minerals but may not apply to 6-8 nm nanoparticles inside protein shells. At 6-8 nm, the entire particle is surface-dominated -- the "Swiss cheese" intermediate may not form at this scale.
- The 3-4x effect is modest and may be below biological noise, as the hypothesis acknowledges.

**3. Logic Kill**
The hypothesis assumes that geological mineral dissolution models directly apply to intracellular nanoparticle dissolution. This analogy may not hold because: (a) ferritin cores are 6-8 nm (entirely nanocrystalline, no bulk interior), (b) dissolution occurs inside a protein shell in acidic lysosomes, and (c) chelators (citrate, etc.) remove surface iron differently than geological weathering solutions.

**4. Falsifiability Kill**
PASSES strongly -- the test (prepare ferritin at controlled dissolution states, measure Fenton activity per Fe atom) is well-designed and would produce a clear curve.

**5. Triviality Kill**
Not trivial. The connection between mineral weathering models and intracellular iron nanoparticle catalysis is genuinely cross-disciplinary.

**6. Counter-Evidence Search**
- Ferrihydrite heterogeneous Fenton catalysis literature confirms surface-area dependence on catalytic rate. BUT: ferrihydrite nanoparticles at 2-6 nm have been studied extensively in environmental chemistry without reference to ferritin cores. The connection is genuinely novel.
- No direct counter-evidence found against the hypothesis. The main concern is the scale mismatch (6-8 nm particle may not develop etch pits).

**7. Groundedness Attack**
- Hochella et al., Science 2008: VERIFIED (landmark nanogeoscience paper, Science 319:1631-1635).
- Harrison & Arosio, BBA 1996: VERIFIED.
- Cornell & Schwertmann, The Iron Oxides, 2003: VERIFIED (standard textbook reference).
- Hou et al., Autophagy 2016: VERIFIED (ferritinophagy and ferroptosis).
- Luttge et al., Am Mineralogist 2013: **PARTIALLY VERIFIED.** Found Luttge (2005) on etch pit coalescence in Am Mineralogist 90:1776-1783. A 2013 publication by Kurganskaya & Luttge was referenced but the specific Am Mineralogist 2013 citation could not be independently confirmed. The content claim (etch pit dissolution models exist) is correct regardless.
- Groundedness: ~70% -- most claims verified. One citation is partially uncertain (2005 vs 2013 date).

**8. Hallucination-as-Novelty Check**
Low hallucination risk. Ferrihydrite surface chemistry, mineral dissolution kinetics, and ferritin core structure are all independently verified. The novelty is in connecting these established facts.

**9. Claim-Level Fact Verification**
- CLAIM: "Ferritin core is a 6-8 nm diameter ferrihydrite nanoparticle containing ~2000-4500 Fe atoms [GROUNDED: Harrison & Arosio, BBA 1996]" -- VERIFIED (commonly cited as ~2000-4500 Fe atoms, though Harrison & Arosio themselves cite up to ~4500).
- CLAIM: "RSA proportional to d^-1 for nanoparticles" -- VERIFIED for spherical particles (surface area = pi*d^2, volume = pi*d^3/6, SA/V = 6/d).
- CLAIM: "2-nm ferrihydrite has ~100x the specific surface area of 200-nm particles" -- Mathematically: SA/V ratio scales as 1/d, so 200/2 = 100x. VERIFIED by geometry.
- CLAIM: "Specific surface area of intact ferritin core ~150 m2/g" -- The search results found ferrihydrite at ~297.5 m2/g for synthetic preparations. For an 8-nm sphere of ferrihydrite (density ~3.8 g/cm3), SA/V = 6/(8e-7 cm) = 7.5e6 cm2/cm3, or ~197 m2/g. The 150 m2/g claim is in the right ballpark. APPROXIMATELY VERIFIED.

**REVISED CONFIDENCE**: 4/10 (down from 5)
**REVISED GROUNDEDNESS**: 5/10 (same)
**SURVIVAL NOTE**: Survives as WOUNDED. The hypothesis has genuine novelty and sound grounding in both fields. The main weaknesses are: (1) the 6-8 nm ferritin core may be too small for etch pit formation (the "Swiss cheese" model requires a particle large enough to develop internal porosity), (2) lysosomal dissolution of ferritin cores is mediated by protein shell degradation and chelators, not geological weathering processes, and (3) the 3-4x effect is modest. Despite these issues, the core idea (surface-area-dependent Fenton catalysis during ferritinophagy) is testable and could yield useful insight. Strongest reason to kill: at 6-8 nm, there is no "bulk interior" for etch pits to form in -- the entire particle is surface.

---

## META-CRITIQUE

### Kill Rate Assessment
- **KILLED**: H1, H2, H4 (3/8 = 37.5%)
- **WOUNDED**: H3, H5, H6, H7, H8 (5/8 = 62.5%)
- **SURVIVES**: 0/8 (0%)

Kill rate of 37.5% is within the healthy 30-50% range.

### Systemic Weakness Identified
The dominant kill mechanism was **substrate mismatch**: FTT synthesis does not produce PUFAs, which are required for the specific ferroptosis-relevant chemistry (bis-allylic hydrogen abstraction, PLOOH formation, 4-HNE/MDA/isoprostane generation). This is a fundamental factual error that the Generator should have caught. The computational validation flagged "GPX4/GSH axis NOT transferable" but missed the equally critical "PUFA substrate NOT transferable."

A secondary systemic issue is the Fenton rate constant misapplication: using homogeneous Fenton rate constants (measured at pH 3) for serpentinization conditions (pH 9-12) where iron precipitates. This overstates the Fenton-driven reaction rates by potentially 100x or more.

### For Each WOUNDED Hypothesis -- Strongest Unexercised Kill Argument:
- **H3**: Could have been killed on the argument that thermodynamic buffering by H2 in an open system with continuous radical generation is physically meaningless -- you need kinetics, not thermodynamics, in a steady-state system. Spared because the mineral-catalyzed H2 activation pathway provides a potential kinetic route.
- **H5**: Could have been killed on the argument that intracellular chelators (GSH, citrate, phosphate) modify iron stability fields so profoundly that a Pourbaix diagram for "pure Fe" is uninformative. Spared because the framework could be parameterized with chelator effects, and the ferritin=ferrihydrite connection is real and underexploited.
- **H6**: Could have been killed on triviality (Arrhenius kinetics are universal; the serpentinization framing adds zero explanatory power). Spared narrowly because the specific quantitative prediction (4%/degree, optimal hypothermia target from Ea) has not been formally published, though the qualitative temperature-ferroptosis connection is already being explored.
- **H7**: Could have been killed because the most specific ferroptosis biomarkers (isoprostanes, 4-HNE) require PUFA substrates not available abiotically, meaning their detection on ocean worlds would actually be EVIDENCE FOR biology, the opposite of the hypothesis claim. Spared because the general warning about abiotic lipid oxidation products (simpler aldehydes, epoxides) retains value for astrobiology mission planning.
- **H8**: Could have been killed on the argument that 6-8 nm ferritin cores are too small for etch pit formation -- the entire particle is surface, there is no bulk interior. Spared because the general surface-area dependence of Fenton catalysis may still vary during dissolution in non-trivial ways, even without classical etch pits.

### Web Search Verification Completeness
All 8 hypotheses received multiple web searches. Key [GROUNDED] claims were individually verified. Citation errors found:
- Agmon et al.: Scientific Reports, not Nature Chemical Biology (H4)
- Tuo et al.: Molecular Psychiatry, not ATVB (H6)
- Frost & Beard: Journal of Petrology, not JGR (H5)
- Luttge: 2005 Am Mineralogist confirmed, 2013 date uncertain (H8)

Source mischaracterization found:
- PMID 31836519: Studies membrane fluidity, not lipid peroxidation catalysis (H1, H2, H4)

Substrate fabrication found:
- FTT synthesis "produces polyunsaturated species": FALSE -- FTT produces only saturated fatty acids (H1, implicitly H2, H4, H7)

---

## Summary Table

| ID | Title | Original Conf | Revised Conf | Original Ground | Revised Ground | Verdict | Kill Reason |
|----|-------|--------------|-------------|----------------|---------------|---------|-------------|
| H1 | Abiotic ferroptosis-analog membrane selection | 6 | 1 | 6 | 3 | KILLED | No PUFA substrate from FTT; PMID mischaracterized; Fenton pH mismatch |
| H2 | PLOOH chemical equivalence | 7 | 2 | 7 | 3 | KILLED | No PUFA substrate; no phospholipids from FTT; PLOOH thermal instability; Fenton pH |
| H3 | H2 as primordial antioxidant | 4 | 3 | 5 | 6 | WOUNDED | Kinetic inertness of H2; requires unverified mineral catalysis step |
| H4 | Fenton-driven LLPS | 5 | 2 | 6 | 4 | KILLED | No PUFA substrate; T >> critical mixing T; insufficient compositional complexity |
| H5 | Pourbaix framework for ferroptotic iron | 6 | 5 | 6 | 6 | WOUNDED | Intracellular chelators modify stability fields; journal misattribution |
| H6 | Arrhenius parameters predict therapeutic T windows | 6 | 4 | 7 | 6 | WOUNDED | Low novelty (already explored); trivial Arrhenius application; journal error |
| H7 | False-positive ferroptotic biosignatures | 7 | 4 | 7 | 5 | WOUNDED | PUFA-specific markers not produced abiotically; general concept retains value |
| H8 | Nanoparticle surface-area scaling | 5 | 4 | 5 | 5 | WOUNDED | 6-8 nm cores too small for etch pits; modest effect; lysosomal dissolution differs |

**Kill Rate: 3/8 = 37.5%**
