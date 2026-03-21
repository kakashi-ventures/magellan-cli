# Ranking — Cycle 2
## Session: 2026-03-20-scout-005
## Survivors: 6 of 7 (86% survival rate, 1 killed: H2.7)
## Forwarded to Quality Gate: 4 of 6

---

## Scoring Dimensions (fixed weights)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Novelty | 20% | Has this connection been explored? (10=completely unexplored) |
| Mechanistic Specificity | 20% | How concrete is the mechanism? (10=names specific molecules/equations) |
| Cross-field Distance | 10% | How far apart are the domains? (10=completely different disciplines) |
| Testability | 20% | Validatable with existing methods/data? (10=PhD student, 3 months) |
| Impact | 10% | If true, how much does it change understanding? (10=new field) |
| Groundedness | 20% | Are claims supported by verifiable evidence? (10=every claim traceable) |

---

## H2.1: Abiotic vs Enzymatic PLOOH Regioselectivity as Chemical Fossil of Antioxidant Evolution
**Parent**: E1 (from H2) | **Bridge**: radical_regioselectivity | **Technique**: facet_recombination + scale_bridging

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 8 | Specific comparison of abiotic Fenton vs enzymatic 15-LOX regioselectivity fingerprints on same PUFA substrate has never been published. "Chemical fossil" framing confirmed novel by Critic. Isoprostane literature (Milne 2007) exists but not as deliberate evolutionary comparison. |
| Mechanistic Specificity | 8 | Textbook chemistry with sharp quantitative predictions: C15 fraction 0.15-0.25 (abiotic, near-statistical across 4 bis-allylic positions) vs >0.90 (enzymatic 15-LOX). Ferryl sub-prediction at pH>5 adds mechanistic depth. Names specific molecules (PE(18:0/20:4)-OOH), specific enzymes (ALOX15), specific oxidants (HO•, FeIV=O). |
| Cross-field Distance | 7 | Connects environmental Fenton chemistry (geochemistry) to ferroptosis enzymology (cell biology) through evolutionary biology. Three fields, but both share iron chemistry as common language. |
| Testability | 8 | GUVs + ferrihydrite + H2O2 + LC-MS/MS is a clear protocol with standard equipment. Sharp falsification: if abiotic C15 >0.40, hypothesis fails. Temperature independence testable. PhD student: 3-6 months. |
| Impact | 6 | Establishes "primordial ferroptosis" / "chemical fossil" concept. Would be published in chemistry or origins-of-life journal. Significant but does not open a new field. |
| Groundedness | 7 | All citations verified across both cycles: Kuhn 2015 (ALOX15 >95% C15), Kagan 2017, Milne 2007, Petigara 2002, Kwan & Voelker 2003. Chemistry well-established on both sides. Strongest groundedness in cohort. |

**Weighted composite: 0.20(8) + 0.20(8) + 0.10(7) + 0.20(8) + 0.10(6) + 0.20(7) = 7.50/10**

### Strengths
- Strongest cycle 2 hypothesis by a clear margin
- Sharp quantitative falsification cutoffs
- All chemistry textbook-verified; no speculative claims in the mechanism
- Novel "chemical fossil" framing with evolutionary depth
- Feasible experiment with standard analytical equipment

### Weaknesses
- Evolutionary inference (non-selective → selective) is suggestive, not deductive
- Ferryl selectivity at pH>5 could complicate the "flat abiotic profile" prediction
- Impact limited to a niche at the intersection of origins-of-life and lipid chemistry

---

## H2.4: Ferritin Protein Shell as Kinetic Barrier Controlling Ferrihydrite Fenton Activity
**Parent**: E4 (from H8) | **Bridge**: nanoparticle_dissolution_kinetics | **Technique**: mutation + adversarial

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 7 | Direct quantitative comparison of bare ferrihydrite NPs vs intact ferritin Fenton activity confirmed unpublished. Individual components known in separate literatures but the head-to-head comparison is new. Slightly lower than H2.1 because the qualitative fact (ferritin is protective) is widely assumed. |
| Mechanistic Specificity | 7 | Specific structural mechanism: H2O2 (2.8Å) restricted by 3-4Å 3-fold channels (Theil 2004). Shrinking-sphere dissolution model correct at 6nm. Quantitative: >5-fold difference bare vs ferritin, >2-fold per-atom increase at 50% dissolution. |
| Cross-field Distance | 6 | Mineral dissolution kinetics (environmental chemistry) → protein biochemistry (ferritin biology). Both involve iron chemistry — moderate distance. Same redox chemistry, different containers. |
| Testability | 8 | Clean experimental comparison: synthesize 6nm ferrihydrite NPs, protease-strip ferritin, compare Fenton activity. Standard assays (deoxyribose degradation or fluorescent probe). Protease confounding manageable with controls. PhD student: 3-6 months. |
| Impact | 5 | Quantifies what biochemists qualitatively assume. The number matters for ferroptosis modeling but doesn't change conceptual understanding. Moderate contribution to both fields. |
| Groundedness | 6 | Harrison & Arosio 1996, Theil 2004, Kwan & Voelker 2003, Pham 2012, Arosio 2009, Gao 2016 — all verified. Channel dimensions from crystal structure. Risk: H2O2 may enter channels faster than predicted. |

**Weighted composite: 0.20(7) + 0.20(7) + 0.10(6) + 0.20(8) + 0.10(5) + 0.20(6) = 6.70/10**

### Strengths
- Cleanest experimental design in the cohort — simple A/B comparison
- Quantitative prediction with sharp threshold (>5-fold)
- Genuine insight from geochemistry (dissolution kinetics framework)
- High testability with standard equipment

### Weaknesses
- Impact ceiling — quantifies a qualitatively known effect
- >5-fold prediction may be too generous given 2.8Å vs 3-4Å channel geometry
- Cross-field distance moderate — both fields study iron

---

## H2.2: PHREEQC Iron Speciation Model Predicts GSH-Dependent Fenton Activity Amplification
**Parent**: E2 (from H4) | **Bridge**: speciation_thermodynamics | **Technique**: tool_transfer

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 9 | PHREEQC has NEVER been applied to any biological context — absolute confirmed novelty. Zero precedent in PubMed or Google Scholar. True tool transfer from USGS geochemistry to cell biology. Highest novelty in the cohort. |
| Mechanistic Specificity | 5 | Speciation shift Fe-GSH → Fe-citrate is specific with log K values cited. Crossover at ~2mM GSH, >3-fold activity increase are quantitative. But: crowding correction (0.3-0.5) introduces 2-5x systematic uncertainty. Deoxyribose assay rates may not translate to membrane PUFA-PE peroxidation. |
| Cross-field Distance | 9 | USGS geochemistry computational tool → cellular biochemistry. Different communities, journals, training programs. Near-maximum field distance for an applicable tool transfer. |
| Testability | 5 | PHREEQC is free (USGS). But: custom database adaptation needed, crowding corrections non-standard, benchmarking against ODE models ambiguous. Cell lysate validation adds 3+ months. Total: 6-9 months. |
| Impact | 5 | Demonstrates geochemistry codes applicable to biology — conceptually exciting. But if 3-5x speciation effect dwarfed by 100x GPX4/ACSL4 biological variables, practical improvement minimal. |
| Groundedness | 6 | Hider & Kong 2013, Dixon 2012, Engelmann 2003, NIST, Parkhurst 2013 — verified. Log K values approximate and condition-dependent. Crowding correction empirical with no standard methodology. |

**Weighted composite: 0.20(9) + 0.20(5) + 0.10(9) + 0.20(5) + 0.10(5) + 0.20(6) = 6.40/10**

### Strengths
- Highest novelty in the entire session (9/10) — zero precedent
- Maximum cross-field distance (9/10) — true tool transfer
- Exact MAGELLAN value proposition: connecting disconnected fields via shared chemistry

### Weaknesses
- Practical relevance uncertain — speciation effect may be minor vs biological variables
- Crowding corrections introduce large systematic error
- Benchmarking against existing models lacks clear success criterion

---

## H2.3: Pourbaix Stability Field Mapping of Ferrihydrite-Catalyzed PLOOH Production
**Parent**: E3 (from H2 x H5) | **Bridge**: pourbaix_thermodynamics | **Technique**: crossover

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 8 | Using Pourbaix diagrams to design and interpret lipid peroxidation experiments — no precedent confirmed. Novel application of a well-established geochemistry visualization framework to biochemistry. |
| Mechanistic Specificity | 6 | Thermodynamically rigorous pH-Eh framework. Maps Fe2+/Fe3+/ferrihydrite stability fields to PLOOH production zones. But chelators shift boundaries substantially and ferryl transition at pH>5 adds unquantified complexity. Predictions may be inaccurate without chelator corrections. |
| Cross-field Distance | 8 | Pourbaix diagrams (standard in corrosion science and mineralogy) → biochemistry (lipid peroxidation). Strong cross-field transfer — different textbooks, communities. |
| Testability | 5 | 5×5 = 25 conditions with pH-Eh control + LC-MS/MS. Eh control at low pH requires electrochemical cell or redox buffers. 6-9 months, well-equipped lab. Large but doable. >75% spatial overlap prediction is quantitative. |
| Impact | 6 | Would create the first thermodynamic phase diagram for biological lipid peroxidation — a genuinely new type of figure. Niche but novel and citable. |
| Groundedness | 6 | Pourbaix thermodynamics textbook-established (Stumm & Morgan). Ferrihydrite stability field data well-characterized. But biological relevance of pure-Fe boundaries uncertain — chelator corrections could shift by 1+ pH unit. |

**Weighted composite: 0.20(8) + 0.20(6) + 0.10(8) + 0.20(5) + 0.10(6) + 0.20(6) = 6.40/10**

### Strengths
- Elegant thermodynamic framework with visual clarity (Pourbaix diagram)
- Novel type of output — no one has mapped PLOOH production to stability fields
- Strong cross-field transfer from corrosion science to biochemistry

### Weaknesses
- Large experimental matrix (25 conditions × LC-MS/MS) — expensive and time-consuming
- Chelator corrections may invalidate pure-Fe boundary predictions
- Ferryl transition adds complexity not captured in standard Pourbaix diagrams

---

## H2.6: Ferryl Ion vs Hydroxyl Radical Produce Distinguishable PLOOH Signatures (NOT FORWARDED)
**Parent**: FRESH | **Bridge**: oxidant_identity | **Technique**: adversarial

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 7 | Whether ferryl vs HO• produces different PLOOH positional isomer distributions on PUFAs has never been measured. Genuinely unknown question. |
| Mechanistic Specificity | 5 | HO• vs ferryl transition at pH ~5 is well-established. But core prediction (ferryl selectivity for PUFAs) is genuinely unknown — exploratory rather than predictive. Effect size (C15 0.15→0.20-0.35) is an honest guess. |
| Cross-field Distance | 6 | Environmental chemistry oxidant speciation → biochemical lipid peroxidation. Moderate distance. |
| Testability | 5 | pH-dependent LC-MS/MS experiment is clear. But predicted effect size (C15 shift of 0.05-0.20) may be within experimental noise. Risk of indeterminate null result. |
| Impact | 4 | Narrow audience regardless of outcome. Neither positive nor negative result reshapes understanding significantly. |
| Groundedness | 5 | Hug & Leupin 2003 verified for oxidant transition. Core prediction has no evidentiary basis — hypothesis about a genuinely unknown phenomenon. |

**Weighted composite: 0.20(7) + 0.20(5) + 0.10(6) + 0.20(5) + 0.10(4) + 0.20(5) = 5.40/10**

**NOT FORWARDED**: Redundant with H2.1 (both use LC-MS/MS for PLOOH isomers). Could be absorbed as a pH-dependent sub-experiment of H2.1. Effect size may be undetectable. Recommend noting ferryl extension in H2.1's Quality Gate card.

---

## H2.5: Ferritin as Evolved Domestication of a Geochemical Fenton Reactor (NOT FORWARDED)
**Parent**: FRESH | **Bridge**: evolutionary_containment | **Technique**: null_hypothesis_inversion

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 6 | "Domestication" framing is a novel metaphor. Individual facts (ferritin = ferrihydrite, ferritin prevents Fenton) are all known. Novelty is in narrative synthesis, not underlying claims. |
| Mechanistic Specificity | 4 | Evolutionary narrative is qualitative and non-mechanistic. Ferroxidase mutant prediction (>3-fold) is specific but borrowed from H2.4. Comparative genomics is correlational. No molecular mechanism for "domestication." |
| Cross-field Distance | 7 | Geochemistry + evolutionary biology + cell biology — three fields. But connections are narrative rather than mechanistic. |
| Testability | 5 | Ferroxidase mutant testable (shared with H2.4). Comparative genomics correlational. Historical evolutionary narrative unfalsifiable in principle. |
| Impact | 6 | If accepted, reframes ferritin evolution. Deep conceptual insight but hard to prove definitively. |
| Groundedness | 5 | Individual facts verified. Evolutionary narrative has no direct evidence. Comparative genomics prediction speculative. |

**Weighted composite: 0.20(6) + 0.20(4) + 0.10(7) + 0.20(5) + 0.10(6) + 0.20(5) = 5.30/10**

**NOT FORWARDED**: Redundant with H2.4 (shares bare vs ferritin comparison). Narrative core unfalsifiable. Recommend noting ferroxidase mutant extension and domestication framing in H2.4's Quality Gate card.

---

## Final Ranking Table

| Rank | ID | Title | Nov | Mech | XField | Test | Impact | Ground | Composite | Verdict | Forward? |
|------|-----|-------|-----|------|--------|------|--------|--------|-----------|---------|----------|
| 1 | H2.1 | PLOOH Regioselectivity Chemical Fossil | 8 | 8 | 7 | 8 | 6 | 7 | **7.50** | PASS | YES |
| 2 | H2.4 | Ferritin Shell Kinetic Barrier | 7 | 7 | 6 | 8 | 5 | 6 | **6.70** | PASS | YES |
| 3 | H2.2 | PHREEQC GSH-Dependent Speciation | 9 | 5 | 9 | 5 | 5 | 6 | **6.40** | COND_PASS | YES |
| 4 | H2.3 | Pourbaix Stability Field Mapping | 8 | 6 | 8 | 5 | 6 | 6 | **6.40** | COND_PASS | YES |
| 5 | H2.6 | Ferryl vs HO• PLOOH Signatures | 7 | 5 | 6 | 5 | 4 | 5 | **5.40** | COND_PASS | NO (redundant w/ H2.1) |
| 6 | H2.5 | Ferritin Evolved Domestication | 6 | 4 | 7 | 5 | 6 | 5 | **5.30** | COND_PASS | NO (redundant w/ H2.4) |

---

## Elo Tournament Sanity Check (15 pairwise comparisons)

| Match | Winner | Key Reason |
|-------|--------|------------|
| H2.1 vs H2.2 | **H2.1** | Superior mechanism (+3), testability (+3), groundedness (+1) outweigh novelty/distance advantage |
| H2.1 vs H2.3 | **H2.1** | Sharper predictions, faster experiment, stronger groundedness |
| H2.1 vs H2.4 | **H2.1** | More novel framing, tighter mechanism, higher groundedness; close match |
| H2.1 vs H2.5 | **H2.1** | H2.5's narrative unfalsifiable; H2.1 dominates mechanism/testability/groundedness |
| H2.1 vs H2.6 | **H2.1** | H2.6 is a potential sub-experiment of H2.1; effect size risk decisive |
| H2.2 vs H2.3 | **H2.2** | Marginally — absolute tool-transfer novelty (9 vs 8), higher cross-field distance |
| H2.2 vs H2.4 | **H2.4** | Testability (+3) and mechanism (+2) overcome novelty (+2) and distance (+3) |
| H2.2 vs H2.5 | **H2.2** | Higher novelty, better mechanism, stronger cross-field insight across the board |
| H2.2 vs H2.6 | **H2.2** | Exceptional novelty and distance dominate; H2.6 effect size uncertainty |
| H2.3 vs H2.4 | **H2.4** | Simpler experiment, better testability (8 vs 5); 25-condition burden decisive |
| H2.3 vs H2.5 | **H2.3** | More rigorous framework, higher novelty, better mechanism |
| H2.3 vs H2.6 | **H2.3** | Larger scope, higher novelty, more impact; H2.6 may produce null |
| H2.4 vs H2.5 | **H2.4** | H2.5 partially redundant; H2.4 sharper on mechanism (+3), testability (+3) |
| H2.4 vs H2.6 | **H2.4** | Cleaner comparison, stronger predictions, higher mechanism specificity |
| H2.5 vs H2.6 | **H2.6** | Marginal — H2.6 asks genuinely unknown empirical question; H2.5 narrative unfalsifiable |

### Elo W-L Records

| ID | W | L | Elo Rank |
|----|---|---|----------|
| H2.1 | 5 | 0 | 1st |
| H2.4 | 4 | 1 | 2nd |
| H2.2 | 3 | 2 | 3rd |
| H2.3 | 2 | 3 | 4th |
| H2.6 | 1 | 4 | 5th |
| H2.5 | 0 | 5 | 6th |

**Consistency check**: Elo ranking perfectly matches composite ranking. H2.2/H2.3 tied on composite (6.40) but H2.2 wins the Elo head-to-head — PHREEQC's exceptional novelty is the tiebreaker. **CONSISTENT. ✓**

---

## Diversity Check

### Methodology Distribution (Top 4)

| ID | Approach Type | Methods | Distinct? |
|----|---------------|---------|-----------|
| H2.1 | Wet-lab: isomer fingerprinting | GUVs + ferrihydrite + LC-MS/MS | ✓ |
| H2.4 | Wet-lab: kinetic barrier comparison | Bare NPs vs ferritin + Fenton assay | ✓ |
| H2.2 | Computational: tool transfer | PHREEQC speciation modeling | ✓ |
| H2.3 | Thermodynamic mapping | Pourbaix framework + 25-point matrix | ✓ |

**4 distinct approaches. No convergence. DIVERSITY PASS. ✓**

### Redundancy in Ranks 5-6 (dropped)

- H2.6 ↔ H2.1: Both use LC-MS/MS for PLOOH positional isomers. H2.6 is a pH-dependent sub-experiment of H2.1.
- H2.5 ↔ H2.4: Both involve bare ferrihydrite vs intact ferritin comparison. H2.5 adds evolutionary narrative.
- Neither substitution would add diversity to the top 4.
- **Recommendation to Quality Gate**: Incorporate H2.6's ferryl sub-experiment as extension of H2.1. Incorporate H2.5's ferroxidase mutant prediction and domestication framing as extension of H2.4.

---

## Cycle 2 vs Cycle 1 Comparison

| Metric | Cycle 1 | Cycle 2 |
|--------|---------|---------|
| Hypotheses critiqued | 5 | 7 |
| Survived critique | 2 (40%) | 6 (86%) |
| Top composite | 6.25 | 7.50 |
| 2nd composite | 5.85 | 6.70 |
| Top-4 average | N/A | 6.75 |
| Forwarded to QG | 0 (→ evolution) | 4 |

Cycle 2 shows substantial improvement: higher survival rate (critique feedback incorporated), higher composite scores (evolved hypotheses sharper), and enough quality mass to forward 4 diverse candidates to Quality Gate. The evolution step and cycle 2 generation successfully addressed the systemic problems (no abiotic PUFAs, Fenton pH constraints, LIP non-expansion) that weakened cycle 1 hypotheses.

---

## Quality Gate Selection Summary

**Forward 4 hypotheses to Quality Gate:**

1. **H2.1** (7.50) — Strongest overall. Sharp falsification, verified chemistry, novel framing.
2. **H2.4** (6.70) — Cleanest experiment. Simple A/B comparison, genuine geochemical insight.
3. **H2.2** (6.40) — Highest novelty (9). True tool transfer. Practical utility is the key question.
4. **H2.3** (6.40) — Novel thermodynamic framework. Expensive but rigorous. New type of figure.

**Drop 2 hypotheses (redundancy + low scores):**

5. H2.6 (5.40) — Absorb ferryl sub-experiment into H2.1.
6. H2.5 (5.30) — Absorb ferroxidase mutant and domestication framing into H2.4.
