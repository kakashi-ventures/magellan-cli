# Ranking — Cycle 1
## Session: 2026-03-20-scout-005
## Survivors: 2 of 5 (40% survival rate)

---

## Scoring Dimensions (weighted)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Testability | 20% | Feasibility and clarity of test protocol |
| Groundedness | 20% | Claims verifiable in existing literature |
| Mechanistic Specificity | 20% | How specific and detailed is the mechanism |
| Novelty | 15% | Genuinely new connection |
| Cross-disciplinary Insight | 15% | Reveals something neither field alone would see |
| Potential Impact | 10% | Significance if confirmed |

---

## H2: Ferrihydrite PLOOH Fingerprinting in Protocells

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Testability | 7 | Well-defined wet-lab protocol: GUVs + ferrihydrite + H₂O₂ + LC-MS/MS. Feasible with standard equipment. Must drop 80°C step (ferrihydrite unstable >50°C). 37°C experiment is clean. |
| Groundedness | 5 | Ferrihydrite Fenton catalysis well-characterized. But PMID 31836519 precedent overstated (fluidity study, not peroxidation). Original r > 0.9 prediction invalidated by 15-LOX regioselectivity issue. |
| Mechanistic Specificity | 5 | Fenton → •OH → bis-allylic H-abstraction → PLOOH is specific chemistry. But the critical distinction (15-LOX C15-specific vs Fenton random across all 4 bis-allylic positions) weakens the "identity" claim. Revised prediction (superset containing ferroptosis species) is less mechanistically precise. |
| Novelty | 8 | No ferrihydrite-PLOOH lipidomics experiment exists anywhere in the literature. Confirmed by exhaustive search. Genuinely novel experimental concept. |
| Cross-disciplinary Insight | 7 | Demonstrates abiotic Fenton chemistry generates the chemical species that kill mammalian cells — a deep insight connecting geochemistry to cell death. The non-specificity of abiotic production vs enzymatic specificity of 15-LOX is itself an insight about evolutionary refinement. |
| Potential Impact | 6 | Establishes "primordial ferroptosis" concept. Origin-of-life implications: if prebiotic membranes were vulnerable to iron-catalyzed peroxidation, anti-peroxidation defenses may have been among the earliest evolved. |

**Weighted composite: 0.20×7 + 0.20×5 + 0.20×5 + 0.15×8 + 0.15×7 + 0.10×6 = 6.25/10**

### Strengths
- Genuinely novel experiment (no precedent)
- Clear wet-lab protocol with standard techniques
- Deep evolutionary insight potential

### Weaknesses (from critique)
- Original falsifiable prediction (r > 0.9 isomer match) guaranteed to fail — must revise
- 80°C step invalid — ferrihydrite transforms above 50°C
- PMID 31836519 precedent was overstated
- Weaker than claimed: abiotic Fenton produces ALL isomers non-specifically; 15-LOX is C15-specific

### Required revisions for cycle 2
1. Change prediction: "ferrihydrite-Fenton produces a superset containing PE(18:0/20:4)-15-OOH among broader isomer mixture" (not "identical distribution")
2. Drop 80°C Arrhenius step; use 37°C and <50°C temperature series only
3. The non-specificity is the FEATURE: abiotic systems produce all isomers; evolution selected 15-LOX to concentrate at the most membrane-destabilizing position

---

## H4: PHREEQC Geochemical Code for Iron Speciation

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Testability | 5 | PHREEQC is freely available (USGS). But requires custom database adaptation for cytoplasmic conditions, crowding corrections not standard, and benchmarking against existing ODE models is ambiguous (how to define "better"?). Less straightforward than a wet-lab experiment. |
| Groundedness | 5 | Ferritin-ferrihydrite structural analogy confirmed (EXAFS). PHREEQC speciation capability well-validated in geochemistry. But: ferritin dissolution kinetics NOT transferable (protein cage ≠ open mineral surface), macromolecular crowding introduces 2-5× systematic error, July 2025 LIP non-expansion undermines dynamics framing. |
| Mechanistic Specificity | 4 | The speciation concept is clear (which Fe-ligand complex dominates at each GSH level), but the original framing as LIP dynamics modeling is undermined by July 2025 paper. Must pivot to speciation snapshots. Prediction #3 (ferrihydrite saturation index → ferritin release) is wrong. |
| Novelty | 9 | PHREEQC has NEVER been applied to any biological context. Absolute confirmed novelty. This is a true tool transfer with zero precedent. |
| Cross-disciplinary Insight | 8 | Exactly what MAGELLAN seeks: taking a mature computational tool from geochemistry and applying it to a completely different domain. The insight is that cellular iron speciation IS geochemistry — cells maintain aqueous iron solutions, and the same thermodynamics applies (with crowding corrections). |
| Potential Impact | 5 | If it works, adds speciation detail no current ferroptosis model captures (which Fe complex dominates). But practical improvement over existing models uncertain given that biological variables (GPX4, ACSL4) dominate sensitivity by 100-fold. |

**Weighted composite: 0.20×5 + 0.20×5 + 0.20×4 + 0.15×9 + 0.15×8 + 0.10×5 = 5.85/10**

### Strengths
- Absolute novelty (zero precedent for PHREEQC in biology)
- True tool transfer — the core MAGELLAN value proposition
- Speciation detail genuinely absent from all existing ferroptosis models

### Weaknesses (from critique)
- LIP doesn't expand during ferroptosis (July 2025) — dynamics framing broken
- Macromolecular crowding: 2-5× systematic error with no standard correction
- Ferritin dissolution ≠ ferrihydrite dissolution — protein cage dominates
- Practical improvement uncertain given biological variable dominance

### Required revisions for cycle 2
1. Pivot from "LIP dynamics modeling" to "iron speciation snapshots at discrete GSH depletion states"
2. Drop prediction #3 (ferrihydrite saturation → ferritin release)
3. Focus on: which Fe-ligand complex (Fe-GSH, Fe-citrate, Fe-ADP) dominates BEFORE vs AFTER GSH depletion, and whether the dominant complex determines Fenton activity
4. Acknowledge crowding limitation explicitly; propose correction factor

---

## Final Ranking

| Rank | ID | Title | Composite | Verdict |
|------|-----|-------|-----------|---------|
| 1 | H2 | Ferrihydrite PLOOH Fingerprinting | **6.25** | CONDITIONAL — proceed to evolution with required revisions |
| 2 | H4 | PHREEQC Iron Speciation | **5.85** | CONDITIONAL — proceed to evolution with required revisions |

---

## Elo Tournament Sanity Check (1 pairwise comparison)

**H2 vs H4**: H2 wins. H2 has a clearer, more executable test protocol (wet-lab LC-MS/MS vs computational modeling with uncertain benchmarking), stronger mechanistic specificity (specific chemistry prediction vs vague "better modeling" claim), and more direct cross-disciplinary insight (chemical species identity vs computational tool transfer). H4 has higher novelty (9 vs 8) and cross-disciplinary conceptual value, but testability gap is decisive.

**Elo result**: H2 > H4. Consistent with composite ranking. ✓

---

## Diversity Check

- H2: Experimental chemistry (wet-lab PLOOH lipidomics)
- H4: Computational tool transfer (geochemical modeling software)

Two distinct approaches. No convergence. ✓

---

## Cycle Decision

- **Top-3 average ≥ 7.0?** No (only 2 survivors, both < 7.0). Cannot early-complete.
- **Survival rate < 30%?** No (40%). Does not trigger mandatory cycle 3 extension.
- **Both survivors are CONDITIONAL**, requiring significant revision before quality gate.

**Decision: PROCEED TO CYCLE 2.** Both hypotheses need evolution to address critique. The 5 critic_questions provide specific directions for the Generator in cycle 2. The 60% kill rate and low composite scores (6.25, 5.85) indicate this target pairing is harder than expected — the Fenton chemistry bridge is real but the biological dominance of GPX4/ACSL4 and the July 2025 LIP non-expansion finding significantly constrain hypothesis space.
