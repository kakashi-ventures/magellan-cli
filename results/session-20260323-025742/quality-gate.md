# Quality Gate — Session 011
## Target: Cartilage Biphasic Theory x Biofilm Matrix Mechanics
## Date: 2026-03-23

---

## 10-Point Rubric Applied to Each Hypothesis

### Rubric Criteria:
1. Specific mechanism with named molecules/equations/pathways
2. Falsifiable prediction with stated outcome for TRUE and FALSE
3. Literature-verified novelty (not already published)
4. Counter-evidence explicitly addressed
5. Test protocol with effort estimate
6. Calibrated confidence (not overconfident)
7. Groundedness: factual claims verified, speculation clearly marked
8. Impact assessment is realistic
9. Cross-domain connection is genuine (not vocabulary re-description)
10. Bridge concept is specific enough to distinguish from trivial analogy

---

## H1.2: Aggregate Modulus H_a from Confined Compression

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 9/10 | Biphasic theory equation given. H_a, k, nu_s all defined. |
| 2 | Falsifiable prediction | 9/10 | If H_a ~ G', hypothesis fails. If H_a doesn't correlate with debridement, fails. |
| 3 | Novelty verified | 9/10 | H_a has never been measured in biofilm. Confirmed by S008 evaluation and parametric search. No paper applies confined compression to biofilm. |
| 4 | Counter-evidence addressed | 7/10 | Technical feasibility acknowledged. Heterogeneity concern raised. Does not fully address whether debridement is purely mechanical. |
| 5 | Test protocol | 8/10 | Clear protocol with equipment specs. Effort estimate provided ($30K, 4-6 months). |
| 6 | Calibrated confidence | 8/10 | 6/10 confidence is appropriate — the framework is sound but application to biofilm is untested. |
| 7 | Groundedness | 8/10 | Mow 1980 [GROUNDED], biofilm G' values [GROUNDED], prediction that H_a << G' is [PARAMETRIC but physically reasoned]. No fabricated claims. |
| 8 | Impact realistic | 8/10 | Would genuinely change biofilm characterization paradigm if validated. Not overstated. |
| 9 | Genuine cross-domain | 9/10 | Not a vocabulary re-description. Introduces a measurement paradigm (drained vs undrained) that fundamentally changes interpretation of biofilm stiffness. |
| 10 | Bridge specificity | 9/10 | The bridge is the specific mathematical framework (biphasic theory) with named equations and parameters. Not a vague analogy. |

**Per-claim grounding verification:**
- "Mow 1980 establishes confined compression and biphasic theory" → [GROUNDED] Standard textbook reference.
- "Biofilm G' ranges 1-1000 Pa" → [GROUNDED] Multiple published measurements (Peterson 2015, Stoodley 2002).
- "H_a = E_s*(1-nu)/((1+nu)(1-2nu))" → [GROUNDED] Standard elasticity relation.
- "Fluid pressurization dominates undrained response" → [GROUNDED] Soltz & Ateshian 1998.
- "H_a will be 10-100x lower than G'" → [PARAMETRIC] No data for biofilm. The 100x upper bound may be overestimated; 5-30x more realistic based on cartilage analogy.

**QG Score**: 8.4/10

**VERDICT: PASS**
Reason: Foundational measurement hypothesis with strong theoretical backing, genuine novelty, specific falsifiable predictions, and clear experimental protocol. The core insight (undrained biofilm rheology conflates solid and fluid contributions) is physically correct and never previously applied. Minor weakness: the 10-100x prediction range should be narrowed.

---

## H1.1: FCD Predicts Donnan-Mediated Cationic Antibiotic Partitioning

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 8/10 | Donnan factor equation, specific antibiotics (tobramycin z=+5, gentamicin z=+4.5), specific ionic strengths. |
| 2 | Falsifiable prediction | 8/10 | Partition coefficient matches Donnan prediction across ionic strength range, or doesn't. |
| 3 | Novelty verified | 7/10 | FCD never measured in biofilm (novel). But tobramycin-alginate interaction is studied. The Donnan framework is the novel angle. |
| 4 | Counter-evidence addressed | 7/10 | Specific binding vs Donnan discussed. Multifactorial resistance acknowledged. |
| 5 | Test protocol | 8/10 | ICP-MS for FCD, fluorescent antibiotics for partitioning, confocal for spatial distribution. |
| 6 | Calibrated confidence | 8/10 | Revised to 5/10 after critique, appropriately reflecting the weakness at physiological ionic strength. |
| 7 | Groundedness | 7/10 | All factual claims verified. The key limitation (Donnan negligible at 150 mM) honestly presented. |
| 8 | Impact realistic | 6/10 | Impact limited to low-ionic-strength environments. Not transformative across all biofilm contexts. |
| 9 | Genuine cross-domain | 8/10 | Genuine framework transfer. The Donnan partitioning concept from cartilage provides quantitative predictions for biofilm. |
| 10 | Bridge specificity | 8/10 | Specific equation (Donnan factor), specific predictions (K=1.02 at 150 mM, K=3.0 at 10 mM). |

**Per-claim grounding verification:**
- "Lai et al. 1991 establishes triphasic theory with Donnan partitioning" → [GROUNDED]
- "Alginate has ~1 carboxylate per 200 Da disaccharide" → [GROUNDED] Standard alginate chemistry.
- "Tobramycin has z=+5 at pH 7.4" → [GROUNDED] Well-known aminoglycoside chemistry (5 amine groups).
- "Donnan factor at 150 mM NaCl gives K~1.02" → [GROUNDED] Correct calculation from equation.
- "Donnan factor at 10 mM gives K~3.0 for z=+5" → [PARAMETRIC] Depends on assumed FCD. Back-of-envelope calculation is correct for assumed FCD range.
- "Kundukad 2025 invokes Donnan equilibrium qualitatively" → [GROUNDED] Confirmed in S008 evaluation.

**QG Score**: 7.5/10

**VERDICT: PASS**
Reason: The hypothesis provides a genuinely novel quantitative framework (Donnan partitioning for biofilm antibiotic penetration) with specific, testable predictions. The key limitation (negligible at physiological ionic strength) is honestly acknowledged. The FCD measurement itself is the most novel contribution — the first quantitative measurement of fixed charge density in any biofilm. This measurement has value beyond the antibiotic partitioning application.

---

## H1.8: Net FCD Transitions During Maturation with Ionic Sensitivity Reversal

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 7/10 | Pel(+)→alginate(-) shift documented. FCD transition is a logical consequence. But the "charge reversal window" mechanism is vague. |
| 2 | Falsifiable prediction | 7/10 | FCD vs time curve should show sign change. Antibiotic efficacy should peak near zero-crossing. |
| 3 | Novelty verified | 8/10 | No paper predicts or measures FCD during biofilm maturation. The concept of a charge reversal window is novel. |
| 4 | Counter-evidence addressed | 6/10 | Spatial heterogeneity concern raised but not fully resolved. Timing variability acknowledged but not quantified. |
| 5 | Test protocol | 7/10 | Daily FCD measurement feasible. But timing the therapeutic window requires knowing the transition in advance — circular. |
| 6 | Calibrated confidence | 7/10 | 5/10 is appropriate given the speculative therapeutic implications. |
| 7 | Groundedness | 6/10 | Pel→alginate shift [GROUNDED for CF]. Net FCD zero-crossing [PARAMETRIC but thermodynamically necessary]. Therapeutic window [SPECULATIVE]. |
| 8 | Impact realistic | 6/10 | Transformative if the window is exploitable. But practical clinical translation is distant. |
| 9 | Genuine cross-domain | 7/10 | Temporal FCD tracking from developmental cartilage biology → biofilm maturation. Genuine but less surprising. |
| 10 | Bridge specificity | 7/10 | FCD measurement methodology transfers directly. The temporal tracking concept is specific. |

**Per-claim grounding verification:**
- "Pel is cationic (partially deacetylated GalNAc)" → [GROUNDED] Jennings et al. 2015 PNAS.
- "Alginate is anionic (carboxylate groups)" → [GROUNDED] Standard chemistry.
- "Pel→alginate shift in chronic CF infection" → [GROUNDED] Wozniak et al. 2003, mucA mutation.
- "Net FCD must transition through zero" → [GROUNDED] Mathematically necessary if sign changes and the transition is continuous.
- "Charge reversal window creates vulnerability" → [SPECULATIVE] No evidence that FCD=0 creates exploitable weakness. The osmotic pressure at FCD=0 IS minimal, but whether this translates to mechanical vulnerability is unproven.

**QG Score**: 6.7/10

**VERDICT: CONDITIONAL_PASS**
Reason: The core prediction (FCD transitions from positive to negative) is thermodynamically sound and testable. The FCD measurement over maturation time would be genuinely novel and informative. However, the therapeutic "charge reversal window" claim is speculative and the practical utility is unclear. CONDITIONAL on: (1) demonstrating the FCD transition in vitro first, (2) showing that mechanical or antibiotic vulnerability correlates with FCD ≈ 0.

---

## H1.6: Streaming Potential Reveals Spatial FCD Heterogeneity

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 7/10 | Streaming potential equation given. Microelectrode array specified. |
| 2 | Falsifiable prediction | 7/10 | Alginate-only = negative, Pel-only = positive, Psl-only ≈ zero. Clear sign predictions for mutants. |
| 3 | Novelty verified | 8/10 | Streaming potential never applied to biofilm. Novel technique transfer. |
| 4 | Counter-evidence addressed | 6/10 | Biological noise concern raised but solution (dead biofilm) may alter FCD. Not fully resolved. |
| 5 | Test protocol | 5/10 | Technically demanding. Signal-to-noise uncertain. May require custom apparatus beyond typical lab capability. |
| 6 | Calibrated confidence | 7/10 | 4/10 after critique is appropriate given technical risks. |
| 7 | Groundedness | 6/10 | Streaming potential for cartilage [GROUNDED]. Adaptation to biofilm [PARAMETRIC/SPECULATIVE]. Signal magnitude [UNCERTAIN]. |
| 8 | Impact realistic | 7/10 | First spatial FCD map of biofilm would be high impact. IF it works. |
| 9 | Genuine cross-domain | 8/10 | Genuine technique transfer from cartilage biophysics. |
| 10 | Bridge specificity | 7/10 | Specific measurement technique with named equipment and protocol. |

**Per-claim grounding verification:**
- "Grodzinsky 1981 establishes streaming potential for cartilage" → [GROUNDED]
- "Mixed Pel/alginate/Psl spatial heterogeneity documented" → [GROUNDED] Colvin et al. 2012.
- "Streaming potential scales with FCD * k * delta_P" → [GROUNDED] Standard electrokinetic theory.
- "Expected signal ~0.01-0.1 mV at 100 Pa" → [PARAMETRIC] Order-of-magnitude estimate. May be detectable or may be below noise floor.

**QG Score**: 6.5/10

**VERDICT: CONDITIONAL_PASS**
Reason: Novel technique transfer with clear validation strategy (deletion mutant controls). However, the technical feasibility is the primary concern — the signal may be below detection limits. CONDITIONAL on: (1) demonstrating detectable streaming potential in alginate-only biofilm (simplest case) before attempting spatial mapping, (2) using glutaraldehyde-fixed biofilm to test whether killing bacteria eliminates noise without destroying FCD.

---

## H1.3: Pel vs Alginate Differential Swelling (Ca2+ effect)

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 6/10 | Ca2+-alginate egg-box model known. The "internal mechanical stress" from differential response is the novel element but is vaguely specified. |
| 2 | Falsifiable prediction | 7/10 | CaCl2 should compact alginate zones while not affecting Pel zones. Visible in confocal with deletion mutants. |
| 3 | Novelty verified | 5/10 | Ca2+-alginate interaction well-studied. EDTA disruption known. The differential Pel-alginate response to Ca2+ is modestly novel. |
| 4 | Counter-evidence addressed | 5/10 | Sign error in original Donnan mechanism not fully corrected. The mechanism was re-attributed to Ca2+ chemistry rather than Donnan theory. |
| 5 | Test protocol | 7/10 | Flow cell confocal with deletion mutants is feasible and well-designed. |
| 6 | Calibrated confidence | 6/10 | 4/10 after critique is appropriate. |
| 7 | Groundedness | 5/10 | Core Donnan claim had a sign error, reducing trust in the theoretical framework. Ca2+ chemistry is well-grounded but not novel. |
| 8 | Impact realistic | 5/10 | Incremental advance over existing Ca2+-biofilm understanding. |
| 9 | Genuine cross-domain | 5/10 | The Donnan framework (cartilage contribution) was weakened. What remains is primarily Ca2+-alginate chemistry already studied in biofilm. |
| 10 | Bridge specificity | 5/10 | Bridge was weakened by the sign error. The remaining bridge (cartilage triphasic perspective on biofilm charge) is less specific. |

**QG Score**: 5.6/10

**VERDICT: FAIL**
Reason: The sign error in the core Donnan mechanism undermines the theoretical bridge. The remaining testable prediction (Ca2+ differential effect on Pel vs alginate) is real but is better explained by existing Ca2+-alginate binding chemistry (egg-box model) than by cartilage triphasic theory. The cross-domain contribution is too weak — the hypothesis does not demonstrate that cartilage theory adds predictive power beyond what biofilm chemistry already provides. The novelty is insufficient.

---

## H1.4: Creep Time Constant Predicts Convective Penetration Timescale

### Rubric Assessment

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1 | Specific mechanism | 6/10 | Equation given but parameter values span 4+ orders of magnitude. t_c estimate ranges from 0.1 s to 1000 s. |
| 2 | Falsifiable prediction | 5/10 | The prediction is "pulsatile shear at t_c frequency enhances transport" but t_c is unknown, making the prediction untestable until H1.2 is completed. |
| 3 | Novelty verified | 7/10 | Poroelastic transport in biofilm not previously proposed. |
| 4 | Counter-evidence addressed | 5/10 | Shear vs compression loading mode mismatch not resolved. Alternative transport mechanisms (convective mixing, channel flow) not adequately distinguished. |
| 5 | Test protocol | 4/10 | Depends on H1.2 measurements first. Cannot be independently tested. |
| 6 | Calibrated confidence | 7/10 | 4/10 after critique is appropriate. |
| 7 | Groundedness | 5/10 | Core physics [GROUNDED]. Biofilm parameter values [HIGHLY UNCERTAIN]. Coupling between shear and interstitial pressure [SPECULATIVE]. |
| 8 | Impact realistic | 5/10 | Would be interesting if validated but impact is limited by the derivation dependence on H1.2. |
| 9 | Genuine cross-domain | 6/10 | Genuine physics transfer but the connection is more of a "derived corollary" of H1.2 than an independent insight. |
| 10 | Bridge specificity | 5/10 | The bridge (poroelastic time constant) is specific but the application (shear-driven transport) has a loading mode mismatch. |

**QG Score**: 5.5/10

**VERDICT: FAIL**
Reason: The hypothesis is not independently testable — it depends on H1.2 parameter measurements. The 4-order-of-magnitude parameter uncertainty renders the prediction useless without prior data. The shear vs compression loading mode mismatch was flagged by the critic and not resolved. This is better considered as a future extension of H1.2 rather than a standalone hypothesis.

---

## Quality Gate Summary

| Hypothesis | QG Score | Verdict | Key Reason |
|---|---|---|---|
| H1.2 Aggregate modulus H_a | 8.4 | **PASS** | Foundational measurement, genuine novelty, strong theory |
| H1.1 FCD-Donnan antibiotic | 7.5 | **PASS** | Novel FCD measurement + quantitative framework |
| H1.8 FCD maturation transition | 6.7 | **CONDITIONAL_PASS** | Sound prediction, speculative therapeutic claim |
| H1.6 Streaming potential FCD | 6.5 | **CONDITIONAL_PASS** | Novel technique, technical feasibility uncertain |
| H1.3 Pel/alginate Ca2+ swelling | 5.6 | **FAIL** | Sign error, novelty insufficient, weak cross-domain bridge |
| H1.4 Creep time constant | 5.5 | **FAIL** | Not independently testable, parameter uncertainty too wide |

**PASS**: 2
**CONDITIONAL_PASS**: 2
**FAIL**: 2

**Total passed + conditional**: 4 of 6 survived (67%)
