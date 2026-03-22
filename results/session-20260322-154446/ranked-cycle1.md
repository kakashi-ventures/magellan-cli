# Ranked Hypotheses — Cycle 1
**Session**: session-20260322-154446
**Fields**: Volcanic glass dissolution kinetics × Pharmaceutical amorphous solid dispersion dissolution
**Hypotheses scored**: 4 survivors from 7 generated (kill rate: 42.9%)
**Ranker**: Hypothesis Ranker v5.2

---

## Per-Hypothesis Scoring Tables

---

### H1.1: TST Affinity-Based Dissolution Model for Amorphous Solid Dispersions

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | Critic's web search confirmed zero prior applications of Transition State Theory to pharmaceutical ASD dissolution — a complete blank in the literature. The geochemistry→pharma direction is unexplored, and no QSPR or mechanistic ASD model uses activation-energy-based rate expressions derived from TST frameworks. |
| Mechanistic Specificity | 20% | 7 | Hypothesis names a specific theoretical framework (TST/Eyring equation), invokes activation energies and pre-exponential factors, and draws on verified geochemical precedent (Dove 2008 Si-O bond hydrolysis). Loses points because the precise rate-limiting molecular event in ASD systems (which bond/interface controls k?) is not yet specified — the Critic correctly flagged that polymer dissolution is often diffusion-controlled, meaning TST's applicability hinges on an unresolved mechanism question. |
| Cross-field Distance | 10% | 7 | Volcanic glass geochemistry (Geochimica et Cosmochimica Acta territory, Si-O network hydrolysis, aqueous geochemistry) → pharmaceutical formulation science (J. Pharm. Sci., ASD polymer matrices, biopharmaceutics). Different primary communities, different empirical traditions, and different language — the bridge is genuine. Score is 7 rather than 9 because both are ultimately dissolution-of-solid-in-aqueous-media problems, so the underlying physics is related. |
| Testability | 20% | 8 | The Arrhenius temperature dependence predicted by TST is directly measurable with standard USP Apparatus II: run dissolution experiments at 25°C, 32°C, and 37°C (physiologically relevant range), extract rate constants, plot ln(k) vs 1/T, and compare activation energy to TST predictions for amorphous silica (~60–80 kJ/mol). All equipment exists in any pharmaceutical lab. Achievable in 3 months. Clear falsification: if activation energy is not linearly correlated with temperature via Arrhenius or if diffusion governs over surface reaction, TST is inapplicable. |
| Impact | 10% | 7 | ASD formulation is a multi-billion-dollar pharmaceutical problem; empirical trial-and-error currently dominates because no first-principles dissolution model exists. A TST-based predictive model could fundamentally shift ASD screening from empirical DoE to mechanistic simulation, reducing development timelines. Score is 7 (not 9–10) because it would advance a subfield rather than open a new one, and applicability may be restricted to specific dissolution regimes. |
| Groundedness | 20% | 7 | Critic assigned revised groundedness 7. TST foundation grounded in Dove 2008 (amorphous silica), Icenhower & Dove 2000 (surface area normalization), and Lasaga 1998 (geochemical kinetics textbook) — all cited and verified. Minor citation issue: spring-parachute attributed to Ting 2018, but correctly belongs to Guzmán 2007. The pharma-side transfer is logical extrapolation, not fabricated — the existing ASD literature lacks TST models rather than contradicting them. ~70% of claims are grounded. |
| **Composite** | | **7.6** | Weighted: (0.20×9)+(0.20×7)+(0.10×7)+(0.20×8)+(0.10×7)+(0.20×7) = 1.80+1.40+0.70+1.60+0.70+1.40 |

---

### H1.2: Passivation Layer Kinetics Unify Glass Alteration Rinds and ASD Polymer-Rich Surface Layers

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | Critic confirmed novel — no published work explicitly frames ASD polymer-rich surface layer formation as analogous to glass alteration rind (passivation layer) kinetics. The √t diffusion-based unification has not appeared in pharma literature. Score is 8 rather than 10 because the √t form is so generic (Higuchi 1961 predates both modern ASD and glass geochemistry work) that it is arguably not a "discovered connection" so much as a shared mathematical coincidence waiting to be noticed. |
| Mechanistic Specificity | 20% | 4 | The proposed "mechanism" is the shared √t parabolic diffusion scaling — a generic consequence of Fick's second law under a diffusion-limited regime. No specific diffusing species are named for the ASD context, no effective diffusivity (D_eff) is estimated for polymer layers, and no molecular model explains why transient viscoelastic polymer layers should exhibit the same kinetics as permanent microporous silica rinds. Critic diagnosed this as generic diffusion physics, not a specific mechanistic bridge. |
| Cross-field Distance | 10% | 7 | Same geochemistry→pharma axis as H1.1. The specific sub-domain (glass alteration rind kinetics from Gin et al., Hellmann et al.) is even more specialized within geochemistry, widening the perceived distance. Score unchanged at 7 for the same reasons as H1.1. |
| Testability | 20% | 6 | Individual components are testable: ASD surface layer thickness vs. time can be measured by AFM height mapping, XPS depth profiling, or confocal Raman imaging. Testing whether the kinetics follow √t is straightforward. However, proving mechanistic unification (vs. trivial mathematical coincidence of two diffusion-limited systems) requires ruling out alternative rate laws and demonstrating causal equivalence — a substantially harder experimental challenge not achievable in 3 months. |
| Impact | 10% | 5 | If validated within its narrow scope, this provides a useful engineering framework for predicting ASD surface layer formation times — helpful for shelf-life and dissolution testing. But the Critic's observation that polymer layer transience breaks the glass rind model limits the conceptual impact to a useful analogy at best, not a mechanistic breakthrough. Would not shift the field's understanding of ASD dissolution. |
| Groundedness | 20% | 5 | Revised groundedness 6 from Critic, adjusted down to 5 here due to the citation error on the hypothesis's flagship reference: Gin et al. 2015 published in Nature Communications, not Nature Materials as cited — a meaningful error on the most prominent supporting paper. Glass rind literature is well-grounded; ASD surface layer literature is partially grounded; the mechanistic connection is speculative. ~50–55% of claims traceable to literature. |
| **Composite** | | **5.8** | Weighted: (0.20×8)+(0.20×4)+(0.10×7)+(0.20×6)+(0.10×5)+(0.20×5) = 1.60+0.80+0.70+1.20+0.50+1.00 |

---

### H1.4: Composition-Dissolution Rate Functions Enable Predictive ASD Formulation Screening

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 6 | Critic confirmed the specific TST-based composition-rate formalism from geochemistry has not been applied to ASDs. However, the underlying concept — correlate molecular descriptors of drug/polymer with dissolution rate — is the core premise of QSPR (Quantitative Structure-Property Relationships), which is mature in pharmaceutical science. The novelty is terminological and the framework is less novel than it appears. Score 6 reflects genuine novelty of geochemical framing but not of concept. |
| Mechanistic Specificity | 20% | 4 | No specific molecular descriptors, bond types, or rate-limiting chemical events are named for the ASD context. The formalism proposes a regression framework with unspecified parameters. The severe dimensionality problem identified by the Critic (drug structural diversity requires 10–20+ descriptors vs. ~10 oxides for silicate glass) means the mechanism is buried under an underdetermined parameter space. Effectively an empirical fit with a theoretical label. |
| Cross-field Distance | 10% | 7 | Same geochemistry→pharma gap as other hypotheses. The compositional modeling angle (linear free energy relationships in geochemistry) is a specific sub-tradition within geochemical kinetics, maintaining the genuine cross-field distance. |
| Testability | 20% | 6 | Within a narrow, controlled scope — varying the ratio of a single drug to a single polymer across 5–10 compositions and measuring dissolution rates — the hypothesis is testable and could yield a composition-rate function. Generalization across drugs is impractical without enormous experimental investment. The narrow-scope version is testable; the broad formulation-screening claim is not within a PhD timeframe. Score reflects partial testability. |
| Impact | 10% | 4 | Within its viable narrow scope (single drug-polymer system), this adds marginally to QSPR capability with an unusual geochemical vocabulary. It does not address the dimensionality problem, does not generalize across drug classes, and does not provide insight beyond what standard factorial DoE already provides for formulation optimization. The Critic's judgment that it "reduces to QSPR with extra steps" limits the projected impact. |
| Groundedness | 20% | 5 | Revised groundedness 5 from Critic; all citations verified. Geochemical side (TST compositional models) grounded. Drug-polymer transfer is speculative. The hypothesis makes no factually false claims — it simply applies a framework in a new context without resolving whether the application is physically justified. ~50% grounded in verifiable literature. |
| **Composite** | | **5.3** | Weighted: (0.20×6)+(0.20×4)+(0.10×7)+(0.20×6)+(0.10×4)+(0.20×5) = 1.20+0.80+0.70+1.20+0.40+1.00 |

---

### H1.6: Saturation Index-Guided Crystallization Risk Assessment for Supersaturated Drug Solutions

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 3 | Critic found material prior art: the MFAD (Maximum Free Energy Advantage of Dissolution) supersaturation expression (2019) already incorporates activity coefficients in pharmaceutical crystallization modeling. The geochemical Saturation Index (SI = log[a/a_eq]) is mathematically identical to log(S_corrected) already used in pharma. The novelty claim rests on systematic adoption of geochemical vocabulary, not on a new concept. Score 3 reflects prior art that substantially undermines the core contribution. |
| Mechanistic Specificity | 20% | 6 | SI = log(IAP/Ksp) is precisely defined; the application to drug systems as SI = log(a_drug/a_drug,eq) is specific and requires specifying an activity coefficient model (e.g., Flory-Huggins for polymer environments). The hypothesis is more mechanistically specified than H1.2 or H1.4 because it names a concrete thermodynamic quantity and its relationship to crystallization driving force. Score limited because the stochastic/kinetic nature of nucleation means the thermodynamic SI does not fully specify crystallization risk. |
| Cross-field Distance | 10% | 7 | Geochemical mineralogy (carbonate/silicate mineral saturation, Langelier index) → pharmaceutical supersaturation management. Both involve aqueous solubility, but the geochemical community has developed analytical frameworks (PHREEQC, MINTEQ) that pharma has not adopted. Same cross-field gap as other hypotheses in this session. |
| Testability | 20% | 8 | Highly testable: prepare supersaturated ASD solutions at controlled drug loadings, calculate activity-corrected SI using available Flory-Huggins or UNIQUAC models, monitor crystallization onset by UV-Vis turbidimetry or light scattering, correlate SI at induction time. All equipment is standard. The protocol is cleaner than H1.1 or H1.2 because SI is a single thermodynamic variable. A 3-month PhD study comparing SI-threshold predictions to observed crystallization times across 4–6 drug-polymer pairs is entirely feasible. |
| Impact | 10% | 3 | Prior art severely limits impact. MFAD already provides activity-corrected supersaturation in pharma. Systematic adoption of SI notation would standardize language across geochemistry and pharma but would not change fundamental understanding. Score 3 reflects that this is a terminological and workflow improvement, not a conceptual advance. |
| Groundedness | 20% | 5 | Revised groundedness 5 from Critic; citations verified. Geochemical SI literature (Langelier 1936, PHREEQC documentation) is well-grounded. Pharma supersaturation literature is well-grounded. The specific claim that geochemical SI adds beyond MFAD is speculative and arguably false given the prior art. ~50% of the novelty-relevant claims are grounded. |
| **Composite** | | **5.4** | Weighted: (0.20×3)+(0.20×6)+(0.10×7)+(0.20×8)+(0.10×3)+(0.20×5) = 0.60+1.20+0.70+1.60+0.30+1.00 |

---

## Final Ranking Table

| Rank | ID | Title (abbreviated) | Novelty | Mech. Spec. | Cross-field | Testability | Impact | Groundedness | **Composite** |
|------|----|---------------------|---------|-------------|-------------|-------------|--------|--------------|--------------|
| 1 | H1.1 | TST Affinity-Based Dissolution Model | 9 | 7 | 7 | 8 | 7 | 7 | **7.6** |
| 2 | H1.2 | Passivation Layer Kinetics | 8 | 4 | 7 | 6 | 5 | 5 | **5.8** |
| 3 | H1.6 | Saturation Index-Guided Crystallization Risk | 3 | 6 | 7 | 8 | 3 | 5 | **5.4** |
| 4 | H1.4 | Composition-Dissolution Rate Functions | 6 | 4 | 7 | 6 | 4 | 5 | **5.3** |

**Score spread**: 7.6 → 5.3 (range: 2.3). H1.1 is a clear leader; H1.2, H1.6, H1.4 cluster tightly between 5.3–5.8. Note that all four share identical Cross-field Distance scores (7/10) — inherent to this session's single geochemistry→pharma axis; this dimension does not differentiate within-session.

---

## Diversity Check

**Top 4 analysis** (all 4 survivors evaluated):

| Pair | Share bridge mechanism? | Share subfields? | Same prediction type? | Verdict |
|------|------------------------|------------------|-----------------------|---------|
| H1.1 + H1.4 | Partial — both TST-based | Both: glass kinetics → ASD | H1.1: rate constants; H1.4: composition regression | SIMILAR (TST framing) |
| H1.1 + H1.2 | No — TST vs. diffusion | Both: glass → ASD | Kinetic rates vs. surface morphology | DISTINCT |
| H1.1 + H1.6 | No — TST vs. thermodynamics | Both: glass → ASD | Kinetic prediction vs. thermodynamic risk | DISTINCT |
| H1.2 + H1.4 | No — diffusion vs. regression | Both: glass → ASD | Surface layer vs. composition-rate | DISTINCT |
| H1.2 + H1.6 | No — diffusion vs. saturation | Both: glass → ASD | Layer kinetics vs. crystallization threshold | DISTINCT |
| H1.4 + H1.6 | No — regression vs. thermodynamics | Both: glass → ASD | QSPR-style vs. saturation-driven | DISTINCT |

**Assessment**: Only 1 conceptually similar pair (H1.1 + H1.4 share TST-based tool transfer). The three conceptual clusters represented are:
- **Kinetic/TST** (H1.1, H1.4): surface reaction rate prediction via activation energy
- **Structural/Diffusion** (H1.2): passivation layer formation kinetics
- **Thermodynamic** (H1.6): free energy / saturation driving force

Threshold for adjustment: 3+ of top 5 conceptually similar. With only 1/4 similar pairs — **PASSED. No diversity adjustments required.** The 4 survivors naturally span kinetic, structural, and thermodynamic dimensions of the dissolution problem.

*Note*: H1.1 and H1.4 share a TST bridge but are functionally distinct — H1.1 targets mechanistic rate prediction for a single ASD system; H1.4 targets multi-composition screening via regression. Their evolutionary paths would diverge.

---

## Elo Tournament Sanity Check

**6 pairwise comparisons (4 hypotheses: 4×3/2 = 6)**

| Match | Winner | Reasoning |
|-------|--------|-----------|
| H1.1 vs H1.2 | **H1.1** | A researcher would test H1.1 first: it proposes a specific, falsifiable mechanistic framework (Arrhenius plot, activation energy comparison), while H1.2's √t analogy requires ruling out generic diffusion before it says anything mechanistically interesting. H1.1's testability is also cleaner. |
| H1.1 vs H1.4 | **H1.1** | H1.4 effectively reduces to QSPR with a dimensionality problem that grows with drug structural diversity. H1.1 has a defined theoretical ceiling and falsifiable prediction. A researcher would prioritize the mechanism over the regression. |
| H1.1 vs H1.6 | **H1.1** | H1.6's core insight (activity-corrected supersaturation) is already present in MFAD 2019. H1.1 is genuinely novel with no prior art conflict. A researcher would invest in the novel mechanistic hypothesis before refining existing notation. |
| H1.2 vs H1.4 | **H1.2** | Both are wounded, but H1.2's mathematical framing is more intellectually interesting and its novelty is higher (8 vs. 6). H1.4's dimensionality problem is a more fundamental barrier to progress than H1.2's genericity problem. H1.2 could be evolved toward a more specific mechanism. |
| H1.2 vs H1.6 | **H1.2** | H1.6's prior art conflict (MFAD 2019) substantially undercuts its experimental value — a researcher would know the result is likely explained by existing frameworks. H1.2, despite its shallow analogy, at least poses a question not yet answered in the literature. |
| H1.4 vs H1.6 | **H1.6** | Despite H1.6's prior art issue, its experimental protocol is cleaner and more directly testable than H1.4's underdetermined regression. H1.6 could be evolved to differentiate itself from MFAD; H1.4's dimensionality problem has no clean experimental workaround. |

**Elo win tallies**:

| Hypothesis | Wins | Losses | Win Rate | Linear Rank |
|-----------|------|--------|----------|-------------|
| H1.1 | 3 | 0 | 3/3 (100%) | 1 |
| H1.2 | 2 | 1 | 2/3 (67%) | 2 |
| H1.6 | 1 | 2 | 1/3 (33%) | 3 |
| H1.4 | 0 | 3 | 0/3 (0%) | 4 |

**Verdict**: Elo ranking (H1.1 > H1.2 > H1.6 > H1.4) **exactly matches the linear composite ranking**.

**Elo confirms linear ranking.**

*Diagnostic note*: The perfect agreement is notable because H1.6 and H1.4 are only 0.1 composite points apart (5.4 vs. 5.3), yet the Elo tournament cleanly separates them. The pairwise comparison captures H1.6's superior testability and evolutionary potential (differentiating from MFAD) vs. H1.4's structurally intractable dimensionality problem — a qualitative judgment the linear scores almost but not quite express. This validates the linear ranking in the most uncertain region (3rd vs. 4th place).

---

## Evolution Selection

**Selected for evolution (3/4 hypotheses):**

| # | ID | Score | Rationale |
|---|----|-------|-----------|
| 1 | **H1.1** | 7.6 | Clear leader. Genuinely novel, mechanistically specific enough to evolve. Priority evolution target: resolve which ASD dissolution regime is surface-reaction-limited (Critic question), and specify the rate-limiting molecular event. |
| 2 | **H1.2** | 5.8 | Best-scoring wounded hypothesis. High novelty compensates for shallow mechanism. Evolution target: deepen the mechanistic analogy beyond generic √t — identify specific diffusing species in both glass rind and polymer layer; account for polymer layer transience by introducing a termination term. |
| 3 | **H1.6** | 5.4 | Selected over H1.4 for testability advantage and evolutionary potential. Evolution target: differentiate from MFAD 2019 by specifying what the geochemical SI framework adds — e.g., multi-ion activity products, pH-coupled crystallization equilibria, or kinetic saturation index trajectories not captured by scalar S. |

**Excluded from evolution:**

| ID | Score | Reason |
|----|-------|--------|
| H1.4 | 5.3 | Reduces to QSPR with extra steps. The dimensionality problem (drug structural space >> silicate oxide space) has no evolutionary solution that doesn't already exist as standard QSPR methodology. Limited evolutionary potential; marginal score advantage for H1.6. |

---

*Ranked by Hypothesis Ranker v5.2 | Session session-20260322-154446 | Cycle 1 | 2026-03-22*
