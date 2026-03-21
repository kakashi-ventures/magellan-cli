# Critiqued Hypotheses -- Cycle 2
## Ferroptosis x Serpentinization Geochemistry
**Session**: 2026-03-20-scout-005
**Critic**: Opus 4.6
**Date**: 2026-03-20

---

## CYCLE 2 CRITIQUE OVERVIEW

Cycle 2 hypotheses benefit from incorporating cycle 1 critique feedback. The systemic substrate problem (no abiotic PUFAs from FTT) has been addressed — all hypotheses either supply PUFAs experimentally or avoid requiring them. The Fenton pH problem has been addressed — no hypotheses use homogeneous Fenton at pH 9-12. The LIP expansion problem has been addressed — E2.2 and H2.7 explicitly disclaim it.

Remaining attack surfaces: (1) triviality/vocabulary re-description, (2) practical utility, (3) evolutionary narrative unfalsifiability, (4) measurement feasibility, (5) quantitative prediction accuracy.

---

## H2.1: Abiotic vs Enzymatic PLOOH Regioselectivity as Chemical Fossil of Antioxidant Evolution

**VERDICT: PASS**

### ATTACKS:

**1. Novelty**
- The specific comparison of abiotic Fenton vs enzymatic 15-LOX regioselectivity fingerprints on the SAME PUFA substrate has not been published. Non-enzymatic lipid peroxidation products have been characterized (isoprostanes, Milne et al. 2007), but not as a deliberate COMPARISON with enzymatic products for evolutionary inference.
- The "chemical fossil" framing is novel.
- **Novelty: HOLDS.**

**2. Mechanism**
- The chemistry is textbook. HO• non-selectivity for bis-allylic positions is well-established. 15-LOX C15 selectivity is well-established. The prediction of a flat vs peaked profile follows directly.
- At pH 7.2, ferryl (FeIV=O) may show partial selectivity — acknowledged and included as a sub-prediction. This is a STRENGTH, not a weakness.
- The experiment supplies PUFAs externally (PAPE in GUVs) — no abiotic PUFA problem.
- **Mechanism: SOUND.**

**3. Logic**
- The evolutionary inference (15-LOX evolved regioselectivity from non-selective chemistry) does not follow deductively from the experiment. Demonstrating that abiotic is non-selective and enzymatic is selective shows a CONTRAST, not an evolutionary pathway. However, the hypothesis explicitly acknowledges this limitation and frames the experiment as demonstrating the "chemical fossil" contrast, not proving evolutionary descent.
- This is an acceptable level of speculative inference for a hypothesis.
- **Logic: ACCEPTABLE with caveat.**

**4. Falsifiability**
- STRONG. C15 fraction = 0.15-0.25 (abiotic) vs >0.90 (enzymatic) with clear cutoffs. Temperature independence prediction (<10% change). If abiotic shows >0.40 C15, hypothesis fails.
- **Falsifiability: STRONG.**

**5. Triviality**
- A lipid chemist might say "of course radical chemistry is non-selective and enzymes are selective — this is known." But the QUANTITATIVE comparison on the same substrate in a single experiment, framed as evolutionary evidence, has not been done. The experimental result would be citable and informative, not trivial.
- **Triviality: NOT TRIVIAL.**

**6. Counter-Evidence**
- Ferryl selectivity is the main risk. If FeIV=O shows strong positional preference (>3:1), the "flat abiotic profile" prediction fails at physiological pH. This would itself be interesting but would weaken the evolutionary argument.
- No direct counter-evidence against the core chemistry predictions.

**7. Groundedness**
- All citations verified in cycle 1 (Kuhn 2015, Kagan 2017, Howard & Ingold 1967, Porter 1995). New additions (Milne 2007, Petigara 2002, Kwan & Voelker 2003) are standard environmental chemistry references.
- Groundedness: 7/10 — strong.

**8. Hallucination-as-Novelty**
- Low risk. Both components (non-selective Fenton, selective 15-LOX) are well-documented independently. Novelty lies in the comparison and framing.

**9. Claim-Level Verification**
- ALOX15 >95% C15 selectivity: VERIFIED (Kuhn et al., BBA 2015)
- Non-enzymatic gives near-statistical distribution: VERIFIED (Milne et al., 2007; Yin et al., 2011)
- Ferrihydrite Fenton at circumneutral pH: VERIFIED (Petigara 2002, Kwan & Voelker 2003)

**REVISED CONFIDENCE**: 5/10 (maintained)
**REVISED GROUNDEDNESS**: 7/10 (maintained)
**SURVIVAL NOTE**: Strongest hypothesis in cycle 2. Clean experimental design, quantitative predictions, novel framing. The evolutionary inference is speculative but the chemistry is solid.

---

## H2.2: PHREEQC Iron Speciation Model Predicts GSH-Dependent Fenton Activity Amplification

**VERDICT: CONDITIONAL_PASS**

### ATTACKS:

**1. Novelty**
- PHREEQC has genuinely never been applied to biology. Confirmed.
- **Novelty: HOLDS.**

**2. Mechanism**
- The speciation shift from Fe-GSH to Fe-citrate during GSH depletion is chemically plausible. The stability constants cited (log K values) are reasonable.
- However: the 5x differential Fenton activity between Fe-citrate and Fe-GSH (from Engelmann et al. 2003) was measured in a deoxyribose degradation assay, which may not translate to PUFA-PE peroxidation in membranes. Different substrates, different geometry.
- The crowding correction (factor 0.3-0.5) is an acknowledged approximation that could alter results by 2-5x.
- **Mechanism: PLAUSIBLE but with quantitative uncertainty.**

**3. Logic**
- The hypothesis correctly distinguishes between "total iron" (constant per July 2025) and "iron speciation" (changes with GSH). This is a genuine advance over the cycle 1 framing.
- However: the practical utility is questionable. If GPX4 activity and ACSL4-mediated PUFA-PE enrichment dominate ferroptosis sensitivity by 100-fold (as stated in counter-evidence), then a 3-5 fold speciation effect is a minor contributor. PHREEQC would be modeling a secondary effect.
- **Logic: SOUND but practical relevance uncertain.**

**4. Falsifiability**
- The crossover point (GSH ~2 mM) and >3-fold activity increase are specific and testable.
- **Falsifiability: GOOD.**

**5. Triviality**
- A bioinorganic chemist would say "of course GSH chelates iron and citrate chelates iron with different affinities." The non-trivial part is (a) the quantitative prediction of the crossover point, and (b) the demonstration that a geochemistry code (PHREEQC) can model it.
- **Triviality: BORDERLINE — the tool transfer is non-trivial but the chemistry it models is somewhat known.**

**6. Groundedness**
- Hider & Kong 2013, Dixon 2012, Engelmann 2003, NIST database — all verified.
- log K values are approximate and may vary with measurement conditions.
- Groundedness: 6/10.

**REVISED CONFIDENCE**: 4/10 (down from 5 — practical relevance concern)
**REVISED GROUNDEDNESS**: 6/10 (maintained)
**SURVIVAL NOTE**: Passes conditionally. The tool transfer novelty is high but the practical utility is uncertain — if iron speciation is a 3-5x effect in a system dominated by 100x biological variables, the PHREEQC model may be correct but uninteresting. The experiment (cell lysate Fenton assay) would test this directly.

---

## H2.3: Pourbaix Stability Field Mapping of Ferrihydrite-Catalyzed PLOOH Production

**VERDICT: CONDITIONAL_PASS**

### ATTACKS:

**1. Novelty**
- Using Pourbaix diagrams to design lipid peroxidation experiments is novel. No precedent.
- **Novelty: HOLDS.**

**2. Mechanism**
- The Pourbaix framework is thermodynamically rigorous.
- Concern: at pH 5.0-7.2, the Fe2+/ferrihydrite boundary is well-defined in pure water but shifts substantially with chelators (citrate, phosphate). The "pure Fe" Pourbaix diagram may not accurately predict the PLOOH map in a chelator-containing buffer.
- The ferryl transition at pH >5 adds complexity: even within the "Fe2+ field," the oxidant species changes, potentially affecting PLOOH production non-thermodynamically.
- **Mechanism: SOUND in principle, boundary predictions may be inaccurate without chelator corrections.**

**3. Falsifiability**
- >75% spatial overlap with >10-fold drop is quantitative and testable.
- **Falsifiability: GOOD.**

**4. Overlap with H2.1**
- H2.3 uses PLOOH detection by LC-MS/MS at varying pH-Eh. H2.1 uses the same detection at fixed pH-Eh but varying conditions. They share methodology but address different questions (spatial mapping vs regioselectivity). Sufficient distinction.

**5. Practical Feasibility**
- Eh-controlled experiments at 25 conditions with LC-MS/MS at each point is a large experimental matrix. This is doable but expensive. May require 6-9 months and a well-equipped lab.

**REVISED CONFIDENCE**: 5/10 (maintained)
**REVISED GROUNDEDNESS**: 6/10 (maintained)
**SURVIVAL NOTE**: Passes conditionally. Strong thermodynamic foundation, but the chelator-modified Pourbaix boundary may deviate from pure-Fe predictions. The experiment is large but well-designed.

---

## H2.4: Ferritin Protein Shell as Kinetic Barrier Controlling Ferrihydrite Fenton Activity

**VERDICT: PASS**

### ATTACKS:

**1. Novelty**
- The bare ferrihydrite NPs vs intact ferritin Fenton activity comparison — confirmed no publication found with this direct comparison. Individual components exist (ferrihydrite Fenton catalysis in environmental chemistry; ferritin iron sequestration in biology) but the direct comparison is unpublished.
- **Novelty: HOLDS.**

**2. Mechanism**
- The hypothesis that ferritin's protein shell restricts H2O2 access to the ferrihydrite core is supported by structural data [GROUNDED: Theil 2004 — channels are 3-4 Angstrom, H2O2 is ~2.8 Angstrom, so it can enter but at restricted rate].
- The 6-nm particle shrinking-sphere model is the correct dissolution model at this scale — the concern about etch pits has been properly addressed (dropped).
- The ferroxidase site mutation (H2.5) provides a complementary test.
- **Mechanism: SOUND.**

**3. Falsifiability**
- >5-fold difference (bare vs ferritin) and >2-fold per-atom increase at 50% dissolution are specific, quantitative predictions.
- **Falsifiability: STRONG.**

**4. Triviality**
- A biochemist might say "obviously ferritin protects against Fenton — that's its function." But the QUANTITATIVE comparison with bare mineral of the same composition is new and the exact fold-difference has predictive value.
- **Triviality: NOT TRIVIAL — the quantification is the contribution.**

**5. Counter-Evidence**
- H2O2 (2.8 Angstrom) fits through ferritin 3-fold channels (3-4 Angstrom), so some Fenton activity may occur even in intact ferritin. The >5-fold prediction might be too generous. A 2-3 fold difference is more conservative.
- Protease treatment may partially aggregate or denature the ferrihydrite core, confounding the comparison.

**REVISED CONFIDENCE**: 5/10 (maintained)
**REVISED GROUNDEDNESS**: 6/10 (maintained)
**SURVIVAL NOTE**: Strong hypothesis with clean experimental design. The geochemical insight (ferrihydrite Fenton catalysis literature) provides the quantitative framework that the biology field lacks. The bare vs shell comparison would be a genuine contribution.

---

## H2.5: Ferritin as Evolved Domestication of a Geochemical Fenton Reactor

**VERDICT: CONDITIONAL_PASS**

### ATTACKS:

**1. Novelty**
- The "domestication" framing is novel. The individual facts (ferritin = ferrihydrite, ferritin prevents Fenton) are known.
- **Novelty: PARTIALLY — framing is new, individual facts are known.**

**2. Mechanism**
- The evolutionary narrative is compelling but unfalsifiable in its historical claims. We cannot observe ferritin evolution.
- However, the testable predictions (ferroxidase mutant, comparative genomics, bare vs shell) provide indirect tests.
- **Mechanism: QUALITATIVE — the narrative is not mechanistic but the predictions are.**

**3. Logic**
- The "domestication" metaphor is useful for framing but risks anthropomorphizing evolution. Ferritin may have evolved for iron supply (homeostasis) rather than Fenton containment. The containment function could be a side effect of iron sequestration.
- This is a classic "chicken and egg" problem — was ferritin selected for storage or protection?

**4. Falsifiability**
- Ferroxidase mutant: >3-fold higher Fenton activity is testable.
- Comparative genomics: correlation with environmental iron is testable but correlation ≠ causation.
- **Falsifiability: MODERATE — individual predictions are testable but the overall narrative is not.**

**5. Overlap with H2.4**
- H2.5 shares the bare vs ferritin comparison with H2.4. If both survive, they should be merged or one should be the "experimental" hypothesis and the other the "interpretive" hypothesis.
- **Redundancy risk: MODERATE.**

**REVISED CONFIDENCE**: 4/10 (maintained)
**REVISED GROUNDEDNESS**: 5/10 (maintained)
**SURVIVAL NOTE**: Passes conditionally. The evolutionary framing is intellectually stimulating and the ferroxidase mutant prediction is strong. But the overlap with H2.4 and the unfalsifiable narrative core are concerns. Consider merging with H2.4 for the quality gate.

---

## H2.6: Ferryl Ion vs Hydroxyl Radical Produce Distinguishable PLOOH Signatures

**VERDICT: CONDITIONAL_PASS**

### ATTACKS:

**1. Novelty**
- The specific question "does ferryl vs HO• produce different PLOOH positional isomer distributions?" has not been addressed. Ferryl reactivity has been studied with small molecules (Pestovsky 2005) but not with PUFA-PE.
- **Novelty: HOLDS.**

**2. Mechanism**
- The HO• vs ferryl transition at pH ~5 is well-established (Hug & Leupin 2003).
- Whether ferryl shows positional selectivity for PUFA oxidation is genuinely unknown. The hypothesis acknowledges this uncertainty and frames it as the question to answer.
- **Mechanism: HONEST about uncertainty.**

**3. Falsifiability**
- The prediction (C15 fraction increases monotonically with pH) is testable. But the predicted effect size (0.15 → 0.20-0.35) is modest and may be within experimental error for LC-MS/MS.
- **Falsifiability: MODERATE — the effect may be too small to detect reliably.**

**4. Overlap with H2.1**
- H2.6 shares experimental methodology with H2.1 (LC-MS/MS for positional HETE isomers). However, H2.6 varies pH (to probe oxidant identity) while H2.1 compares abiotic vs enzymatic at fixed pH. They could be combined into a single experimental paper.
- **Redundancy: MODERATE — could be a sub-experiment of H2.1.**

**5. Counter-Evidence**
- Ferryl selectivity for PUFA oxidation may be negligible — many ferryl studies on small molecules show that ferryl and HO• produce similar product distributions, just at different rates. If so, this would be a clean negative result.

**REVISED CONFIDENCE**: 4/10 (maintained)
**REVISED GROUNDEDNESS**: 5/10 (maintained)
**SURVIVAL NOTE**: Passes conditionally. Genuinely unknown question, but the effect size may be too small to detect. Could be merged with H2.1 as a pH-dependent sub-experiment.

---

## H2.7: Iron Compartment Topology During Ferroptosis Mirrors Serpentinization Iron Partitioning

**VERDICT: KILLED**

### ATTACKS:

**1. Novelty**
- The concept of iron compartmentalization in ferroptosis is already being actively studied. The July 2025 paper (PMC12236665) itself addresses compartmentalization.
- The "partition coefficient Kd" framing from geochemistry is novel as applied to subcellular compartments, but...

**2. Triviality — FATAL**
- This hypothesis commits the vocabulary re-description fallacy. Calling subcellular iron distribution "partitioning topology" and applying Kd notation does NOT add predictive power. Cell biologists already measure iron in subcellular compartments using organelle-targeted probes. They call it "subcellular iron distribution," not "partitioning topology."
- The Kd(ferritin/LIP), Kd(mito/LIP), Kd(ER/LIP) notation is a geochemical vocabulary overlay on existing cell biology measurements. No new prediction is generated that a cell biologist couldn't make without the geochemical framing.
- The R2 > 0.8 correlation between ER iron and PLOOH accumulation is a prediction that cell biologists would test regardless of the geochemical framework — it's a direct spatial coupling hypothesis.

**3. Logic — SERIOUS CONCERN**
- Geochemical partition coefficients assume equilibrium between phases. Subcellular iron distribution is dominated by ACTIVE TRANSPORT (ferroportin, NRAMP2, mitoferrin, NCOA4-mediated ferritinophagy) — not equilibrium. The Kd formalism is fundamentally inappropriate for a system driven by ATP-dependent transporters.

**4. Analogy quality**
- The analogy between subcellular compartments and geochemical reservoirs is superficial. Geological reservoirs exchange iron by diffusion and thermodynamic equilibrium. Cellular compartments exchange iron by protein-mediated active transport with regulatory feedback (IRP1/IRP2, FBXL5). The physics is fundamentally different.

**REVISED CONFIDENCE**: 2/10 (down from 4)
**REVISED GROUNDEDNESS**: 4/10 (down from 5)
**KILL REASON**: Vocabulary re-description of existing cell biology concepts in geochemical notation without added predictive power. Kd formalism inappropriate for active transport-dominated system. Cell biologists already study subcellular iron distribution without needing partition coefficients from geochemistry.

---

## META-CRITIQUE

### Kill Rate Assessment
- **PASS**: H2.1, H2.4 (2/7 = 29%)
- **CONDITIONAL_PASS**: H2.2, H2.3, H2.5, H2.6 (4/7 = 57%)
- **KILLED**: H2.7 (1/7 = 14%)

Total survival: 6/7 = 86%. This is a HIGH survival rate for cycle 2, reflecting that cycle 1 critique feedback was effectively incorporated. The cycle 2 hypotheses avoid the systemic substrate and pH problems that killed cycle 1 hypotheses.

### Redundancy Assessment
Three pairs have overlap:
1. H2.1 + H2.6: Both use LC-MS/MS for HETE isomer analysis. H2.6 could be a sub-experiment of H2.1.
2. H2.4 + H2.5: Both involve bare ferrihydrite vs ferritin comparison. H2.5 adds evolutionary framing and genomics.
3. H2.2 + H2.3: Both use thermodynamic frameworks for iron speciation. H2.2 uses PHREEQC at fixed pH; H2.3 maps the full pH-Eh space.

Recommendation for ranking: Consider merging H2.1+H2.6 and H2.4+H2.5 into stronger combined hypotheses.

### Strongest Hypotheses
1. **H2.1** — Clearest prediction, strongest groundedness, novel experiment
2. **H2.4** — Clean comparison, quantitative prediction, genuine geochemical insight
3. **H2.2** — Highest tool-transfer novelty, but practical relevance uncertain

### Weakest Survivors
1. **H2.6** — Effect size may be too small; could be absorbed into H2.1
2. **H2.5** — Evolutionary narrative unfalsifiable; redundant with H2.4

---

## Summary Table

| ID | Title | Confidence | Groundedness | Verdict | Key Issue |
|----|-------|-----------|-------------|---------|-----------|
| H2.1 | PLOOH Regioselectivity Chemical Fossil | 5 | 7 | PASS | Strongest cycle 2 hypothesis |
| H2.2 | PHREEQC GSH-Dependent Speciation | 4 | 6 | CONDITIONAL_PASS | Practical relevance uncertain |
| H2.3 | Pourbaix Stability Field Mapping | 5 | 6 | CONDITIONAL_PASS | Large experiment, chelator corrections needed |
| H2.4 | Ferritin Shell Kinetic Barrier | 5 | 6 | PASS | Clean comparison, genuine insight |
| H2.5 | Ferritin Evolved Domestication | 4 | 5 | CONDITIONAL_PASS | Redundant with H2.4, narrative unfalsifiable |
| H2.6 | Ferryl vs HO• PLOOH Signatures | 4 | 5 | CONDITIONAL_PASS | Effect may be too small, absorb into H2.1 |
| H2.7 | Iron Compartment Topology | 2 | 4 | KILLED | Vocabulary re-description, Kd inappropriate |
