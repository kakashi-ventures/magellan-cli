# Critique — Cycle 1
## Session: 2026-03-20-scout-005
## Target: Ferroptosis × Serpentinization Geochemistry

---

## Hypothesis 1: Geochemical Peroxidation Potential Index

### Attack Vector 1: Claim-Level Fact Verification
- **k_Fenton = 63 M⁻¹s⁻¹ at pH 7**: **REFUTED.** 63 M⁻¹s⁻¹ is the acidic Fenton rate constant (~pH 3). At pH 7, k ≈ 1.0 × 10⁴ M⁻¹s⁻¹ — a **159× underestimate**. Above pH 5, the mechanism shifts from HO• generation to ferryl/oxidoiron(2+) pathway ([RSC Dalton Trans. 2022, "Ferryl for real"]). ALL downstream calculations in the hypothesis using k=63 are wrong by 2-3 orders of magnitude.
- **DepMap/PRISM RSL3 EC50 for >100 cell lines**: **PARTIALLY REFUTED.** RSL3 is a tool compound, not in PRISM's standard repurposing library. CTRP has ~860-line data but RSL3-specific coverage unconfirmed. The claim should cite CTRP, not PRISM.

### Attack Vector 2: Biological Variable Dominance (Counter-Evidence)
- **Critical 2025 finding**: Ye et al. (PMC12236665, July 2025) — "Labile iron pool dynamics do not drive ferroptosis potentiation in colorectal cancer cells." Using TRX-PURO probe (more specific than calcein-AM), the LIP does NOT measurably increase during RSL3/JKE1674/IKE treatment. Iron compartmentalization (lysosomal, mitochondrial), not cytosolic LIP dynamics, determines sensitivity.
- **Variable dominance**: GPX4 expression varies ~100-fold across cell lines. ACSL4 varies ~100-fold. Labile Fe(II) varies ~10-fold. k_Fenton precision from geochemistry: ~2-fold. **k_Fenton contributes <1% of variance in sensitivity.**
- **GPX4 catalytic rate dwarfs Fenton**: GPX4 suppression ~5×10⁻⁴ M/s vs Fenton rate ~3.75×10⁻¹⁰ M/s at physiological conditions = 1.3 million-fold difference. Ferroptosis occurs only when GPX4 is inhibited, not when iron kinetics change.

### Attack Vector 3: Novelty Check
- **CONFIRMED NOVEL**: No existing model uses geochemical/abiotic iron rate constants for ferroptosis prediction. All models use gene expression or omics inputs. The approach is genuinely new.

### Verdict: FAIL
The hypothesis has genuine novelty but fatal quantitative problems: (1) k_Fenton value is wrong by 159×, (2) July 2025 evidence shows LIP doesn't expand during ferroptosis, (3) biological variables dominate by orders of magnitude over any iron kinetics precision. The GPP index cannot be the primary predictor — at best a secondary modifier in GPX4-low contexts.

**Salvageable if**: Reframed as "geochemical rate constants define the physical chemistry substrate that becomes rate-limiting ONLY after GPX4 suppression." This is a much weaker but defensible claim.

---

## Hypothesis 2: Ferrihydrite PLOOH Fingerprinting in Protocells

### Attack Vector 1: Claim-Level Fact Verification
- **PE(18:1/20:4)-OOH attributed to Kagan 2017**: **REFUTED.** Kagan 2017 identifies PE(18:0/20:4)-OOH and PE(18:0/22:4)-OOH (stearoyl sn-1). PE(18:1/20:4)-OOH (oleoyl sn-1) appears in later lipidomics studies, not the original paper. Citation error.
- **PMID 31836519 as "ferrihydrite-PLOOH precedent"**: **REFUTED.** This paper studies membrane fluidity (Laurdan, DPH probes), NOT lipid peroxidation products. No H₂O₂ added, no LC-MS/MS, no PLOOH analysis. The "partial precedent" claim from computational validation is overstated.
- **Ferrihydrite stability at 80°C**: **REFUTED.** Transformation to goethite/hematite begins above ~50°C, not 80°C. At 80°C and pH 10, ferrihydrite half-life ≈ 45 hours. A 2-24h experiment would see 10-50% mineral transformation, confounding results.

### Attack Vector 2: Regioselectivity Mismatch (FATAL)
- **Ferroptosis PLOOHs are 15-LOX products, not random Fenton products.** ALOX15 abstracts H specifically from C13 of arachidonic acid, inserting O₂ at C15, producing >95% 15-HPETE.
- **Fenton-•OH attacks ALL four bis-allylic positions** (C7, C10, C13, C16) with roughly equal probability, producing a mixture of 5-, 8-, 9-, 11-, 12-, and 15-HPETE isomers. The 15-position isomer would be ~10-20% of the mixture, not >80%.
- **The falsifiable prediction "r > 0.9 for positional isomer ratios" is almost certainly false** — it compares an enzyme-specific product to a random radical product. This isn't a test of the hypothesis; it's a guaranteed negative result.

### Attack Vector 3: Novelty Check
- **CONFIRMED NOVEL**: No ferrihydrite-PLOOH lipidomics experiment exists. The experimental concept is genuinely new.

### Verdict: CONDITIONAL PASS
The experiment is novel and the Fenton-protocell concept is interesting, but the falsifiable prediction guarantees failure. Saveable if the prediction is revised to: "Ferrihydrite-Fenton produces a superset of PLOOH species CONTAINING the ferroptosis signature species (PE-15-HPETE) among a broader isomer mixture — proving abiotic Fenton can generate all species that 15-LOX produces, though without enzymatic selectivity." Also must drop the 80°C step or use <50°C temperature series.

---

## Hypothesis 3: GPX4 Selenocysteine Evolved Against Alkaline Fenton

### Attack Vector 1: Claim-Level Fact Verification — FATAL FLAW
- **Selenocysteine pKa ≈ 5.2**: **CORRECT.**
- **The pH-dependent advantage prediction is INVERTED.** The hypothesis claims "Sec/Cys advantage increases from ~100× at pH 7 to >500× at pH 10." First-principles ionization calculation:

| pH | Sec ionized | Cys ionized | Sec/Cys ratio |
|----|------------|------------|---------------|
| 7.4 | 99.4% | 11.2% | **8.9×** |
| 9.0 | 100% | 83.4% | **1.2×** |
| 10.0 | 100% | 98.0% | **1.0×** |

**At serpentinization pH (10), BOTH Sec and Cys are fully deprotonated. The pKa advantage DISAPPEARS.** The hypothesis predicts the exact opposite of what the chemistry shows. The Sec/Cys advantage is MAXIMAL at physiological pH (8.9×) and collapses to 1.0× at alkaline pH.

### Attack Vector 2: Competing Explanations
- **Ingold et al. Cell 2018 mechanism**: GPX4 requires Sec for **overoxidation resistance** — Sec forms a protective selenylamide intermediate under low-GSH/high-peroxide conditions that Cys cannot form. This is a qualitative mechanistic difference, completely independent of pH.
- **GPX4(Cys) knockin mice**: Did NOT survive to adulthood — died by P18 from spontaneous epileptic seizures due to PV+ interneuron loss. The hypothesis mischaracterizes the Ingold paper.
- **Sec evolved ~2 billion years before GPX4**: Sec incorporation machinery is pan-domain (Bacteria, Archaea, Eukaryotes). GPX4 is eukaryote-specific. Sec was RECRUITED into GPX4, not invented for anti-Fenton defense.

### Attack Vector 3: No Supporting Data Exists
- **No study measures GPX4 at pH > 9.** pH 8 is the empirical assay optimum. The pH conditions the hypothesis requires have never been tested because they are not physiologically relevant.

### Verdict: KILL
The core mechanism is inverted — the pKa advantage disappears at exactly the alkaline pH the hypothesis requires. This is not a soft failure; it's a physics contradiction. The overoxidation resistance explanation (Ingold 2018) is better supported and does not invoke alkaline pH. The evolutionary narrative has appeal but the proposed mechanism is wrong.

---

## Hypothesis 4: PHREEQC for Labile Iron Pool Modeling

### Attack Vector 1: Claim-Level Fact Verification
- **PHREEQC never used in biological context**: **CONFIRMED.** Genuinely novel cross-domain application.
- **Ferritin core ≈ ferrihydrite structurally**: **CONFIRMED** (EXAFS, multiple studies).
- **Ferritin dissolution kinetics ≈ ferrihydrite dissolution**: **REFUTED.** The protein cage controls release kinetics (reductant access through 3-fold channels, Fe(III)→Fe(II) reduction, diffusion through channels). Geological ferrihydrite dissolves at open mineral-water interfaces. Mechanistically distinct processes. Prediction #3 (mineral saturation index predicts ferritin release) is the weakest claim.

### Attack Vector 2: LIP Non-Expansion (Counter-Evidence)
- **July 2025 (PMC12236665)**: LIP does NOT expand during ferroptosis induction. If the LIP is static during RSL3 treatment, there is nothing for PHREEQC to model dynamically. The entire premise — modeling LIP DYNAMICS during ferroptosis — may be modeling the wrong variable.

### Attack Vector 3: Systematic Error from Crowding
- **WATEQ4F at 37°C**: Valid temperature range but calibrated at 25°C. Individual species concentrations off by 1.5-4.5× from temperature correction alone.
- **Macromolecular crowding (~300-400 mg/mL protein)**: Occupies 20-30% of volume, increases activity coefficients 20-50%, shifts equilibria 2-5×. No geochemical code corrects for this. The systematic error from crowding alone may EXCEED the improvement over simple ODE models.

### Verdict: CONDITIONAL PASS
PHREEQC speciation genuinely adds something no existing ferroptosis model has: prediction of which iron coordination complexes dominate (Fe-GSH vs Fe-citrate vs Fe-ADP) as GSH is depleted. But three specific claims need revision: (1) drop ferritin dissolution prediction, (2) acknowledge crowding systematic error, (3) frame as speciation snapshot modeling, not dynamic LIP tracking (given July 2025 non-expansion finding).

---

## Hypothesis 5: Fe(II)/Fe(III) ≈ 1 Universal Tipping Point

### Attack Vector 1: Claim-Level Fact Verification
- **Pignatello et al. 2006**: **EXISTS** but is an environmental engineering review, not lipid peroxidation biology. Does not argue for a biological 1:1 tipping point.
- **Halliwell-Gutteridge**: Original work reports optimal Fe³⁺:Fe²⁺ = 1:1 to 7:1 — a much wider range than "≈1". The optimum is also model-dependent: simple product [Fe²⁺]×[Fe³⁺] peaks at 1:1, but Halliwell initiation model gives ~2:1.
- **One study explicitly contests the 1:1 hypothesis** in emulsified lipid systems.

### Attack Vector 2: Free Ion Speciation Problem (FATAL)
At pH 7.4: free Fe³⁺ ≈ 1.26 × 10⁻¹⁹ M from 1 μM total iron. That is 0.000000013% of total iron as free Fe³⁺. **At physiological pH, essentially ALL Fe³⁺ is precipitated as Fe(OH)₃ or tightly complexed.** A "total iron ratio = 1:1" at pH 7.4 is physically meaningless for Fenton chemistry — the active species are chelated complexes (Fe²⁺-GSH, Fe²⁺-citrate), not free ions.

At serpentinization pH (9-11), Fe³⁺ is EVEN LESS soluble. The "universal ratio" across biology and geology compares physically incomparable quantities measured in physically incomparable ways.

### Attack Vector 3: LIP Non-Expansion (Counter-Evidence)
- **July 2025**: Fe(II) pool is static during ferroptosis induction. If Fe(II) doesn't change, the Fe(II)/Fe(III) ratio doesn't dynamically approach any tipping point. The proposed mechanism (ratio change → peroxidation onset) has no experimental support.

### Attack Vector 4: Measurement Infeasibility
- **Fe(II)/Fe(III) ratio during ferroptosis has NEVER been measured.** Mössbauer requires frozen pellets (non-physiological). FerroOrange measures only Fe(II). No method currently measures the ratio in live cells during ferroptosis.
- The falsifiable prediction requires a measurement that no existing technique can provide cleanly.

### Verdict: FAIL
The mathematical optimum ([Fe²⁺]×[Fe³⁺] maximized at 1:1) is correct in pure solution. But at physiological pH, free Fe³⁺ is essentially zero — the "ratio" that matters is the chelated-complex ratio, which nobody measures. The "universal" claim across pH 3 (where it was established), pH 7.4 (biology), and pH 10 (geology) compares physically incomparable quantities. Combined with the July 2025 LIP non-expansion finding, this hypothesis lacks both theoretical and experimental support.

---

## Summary

| Hypothesis | Key Attack | Verdict | Score |
|-----------|-----------|---------|-------|
| H1: GPP Index | k_Fenton wrong by 159×; LIP static; bio variables dominate | **FAIL** | 3/10 |
| H2: PLOOH Fingerprint | 15-LOX ≠ random Fenton regioselectivity; 80°C invalid | **CONDITIONAL** | 5/10 |
| H3: Selenocysteine Evolution | pKa advantage DISAPPEARS at alkaline pH (inverted prediction) | **KILL** | 1/10 |
| H4: PHREEQC Tool Transfer | Novel but LIP static + crowding error + ferritin ≠ ferrihydrite kinetically | **CONDITIONAL** | 5/10 |
| H5: Fe Ratio Tipping Point | Free Fe³⁺ ≈ 0 at pH 7.4; "universal" compares incomparables | **FAIL** | 2/10 |

**Survived critique**: H2 (conditional), H4 (conditional) — 2 of 5
**Killed**: H3 (physics contradiction)
**Failed**: H1 (quantitative dominance), H5 (speciation problem)

---

## Critic Questions for Cycle 2 Generator

1. **The July 2025 LIP non-expansion finding (PMC12236665) undermines ALL iron-kinetics hypotheses.** If the cytosolic labile iron pool does NOT change during ferroptosis induction, what IS the geochemical bridge actually modeling? Can you reformulate around iron COMPARTMENTALIZATION (lysosomal, mitochondrial) rather than cytosolic LIP dynamics?

2. **The 15-LOX regioselectivity problem is central.** Ferroptosis PLOOHs are enzyme-directed (C15-specific). Fenton-•OH is non-specific. Can you find a hypothesis where the non-specificity of abiotic Fenton is the FEATURE, not the bug? (e.g., abiotic systems produce ALL isomers; evolution selected 15-LOX to concentrate production at the most membrane-destabilizing position)

3. **The k_Fenton pH dependence was wrong but reveals something interesting.** The shift from HO• to ferryl/oxidoiron at neutral pH means the ACTIVE OXIDANT is different in cells (ferryl) vs acidic geochemical systems (HO•). This mechanistic divergence is itself a hypothesis target — does the oxidant identity change the PLOOH product distribution?

4. **Ferritin as a "biological mineral" is the strongest surviving bridge.** The structural analogy is confirmed; the kinetic difference (protein cage vs open surface) is the interesting biology. Can you build a hypothesis around ferritin as an evolved containment vessel for what would otherwise be a geochemical Fenton reactor?

5. **PHREEQC's real value is speciation, not dynamics.** Instead of modeling LIP time-courses, can you use PHREEQC to predict which iron-ligand complex DOMINATES at each stage of GSH depletion — and whether the dominant complex determines which PLOOH species are produced?
