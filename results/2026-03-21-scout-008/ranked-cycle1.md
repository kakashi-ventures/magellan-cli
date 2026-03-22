# MAGELLAN Ranker — Session 008, Cycle 1
## Cuproptosis x Hydrothermal Vent Copper-Sulfide Geochemistry

**Session:** 2026-03-21-scout-008
**Cycle:** 1 (post-critique)
**Ranked at:** 2026-03-22
**Hypotheses scored:** 6 survivors (H1.1, H1.2, H1.3, H1.4, H1.6, H1.7)
**Killed before ranking:** H1.5 (NMR counter-evidence: CuL is aromatic, not dithiolane)

**Dimension weights (life-sciences optimized):**
Novelty 15% | Mechanistic Specificity 20% | Testability 20% | Groundedness 20% | Cross-Domain Bridge Quality 10% | Potential Impact 15%

---

## Per-Hypothesis Scoring Tables

### Hypothesis H1.4: Fe-S Cluster Cu-Fe Replacement Series

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 7 | Macomber and Imlay 2009 established that Cu+ attacks bacterial [4Fe-4S] clusters, so the biology of Cu-Fe displacement is not new. However, the explicit framing as a recapitulation of the pyrite-to-chalcopyrite geochemical substitution series applied specifically to cuproptosis appears unpublished, and the Critic awarded a clean PASS with no prior publication found connecting these two bodies of work at this mechanistic level. |
| Mechanistic Specificity | 20% | 9 | Exceptionally specific: names a 29-order-of-magnitude Ksp thermodynamic driving force, a predicted stoichiometric ratio (Cu:Fe = 1.0 +/- 0.2 in reconstituted ferredoxin), and a differential timing test (CIA overexpression delays cuproptosis >= 2h; LIAS overexpression <= 30 min). Both directions of the bridge have named molecules and quantitative parameters. The only gap is that the Ksp argument relies on a CuS vs FeS solubility product comparison that should be stated explicitly in the experimental methods. |
| Testability | 20% | 9 | CIA/LIAS differential overexpression experiment can be done in standard cell culture with commercially available constructs; ferredoxin reconstitution plus ICP-MS or EPR is standard biochemistry. A PhD student could design and run the core experiment within 3 months. The timing prediction (>= 2h vs <= 30 min) is a sharp, quantitative, falsifiable boundary where counter-evidence would be definitive rather than merely weakening. |
| Groundedness | 20% | 8 | Critic awarded PASS — the strongest verdict in the set. Macomber and Imlay 2009 directly supports bacterial Fe-S vulnerability to Cu+. CIA complex biology is textbook. The Ksp thermodynamic argument is grounded in published solubility products. The main speculative element is projecting the bacterial mechanism to cuproptosis specifically and whether CIA overexpression is cytoprotective at the predicted timescale — both unverified but plausible and verifiable. |
| Cross-Domain Bridge Quality | 10% | 8 | The bridge is load-bearing: removing the geochemical analogy (pyrite-to-chalcopyrite) changes the mechanistic logic. The Ksp argument is the same thermodynamic framework geochemists use; applying it to Fe-S cluster stability is a genuine cross-domain import. The prediction of a 29-order driving force comes directly from mineral chemistry, not from the cellular biology literature alone. |
| Potential Impact | 15% | 8 | If the primary cuproptosis mechanism is Fe-S cluster destruction rather than DLAT oligomerization (the current consensus from Tsvetkov 2022), this reframes a 3-year-old major discovery. It would redirect therapeutic targeting from lipoylation pathways to Fe-S assembly machinery (CIA/LIAS differential), with direct implications for cancer cell killing strategies and copper ionophore design. |
| **Composite** | | **8.25** | (0.15x7)+(0.20x9)+(0.20x9)+(0.20x8)+(0.10x8)+(0.15x8) = 1.05+1.80+1.80+1.60+0.80+1.20 = 8.25 |

---

### Hypothesis H1.2: FDX1 Redox Potential Tuned to Vent Cu2+/Cu+ Boundary

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 7 | FDX1 redox potential (-274 mV) is published in Tsvetkov 2022 and prior ferredoxin literature. Pourbaix diagram methodology is standard geochemistry. The specific claim that FDX1's midpoint potential is evolutionarily tuned to the ligand-extended Cu2+/Cu+ Pourbaix boundary in sulfide-rich environments appears unexplored, though Eh/speciation coupling in biological systems has precedent in the iron literature. CONDITIONAL_PASS implies partial prior exploration. |
| Mechanistic Specificity | 20% | 7 | Names specific molecules (FDX1, Cu2+/Cu+ couple), a quantitative Eh value (-274 mV), and a prediction (ligand-extended Pourbaix boundary at -260 to -300 mV). However, the mechanism connecting evolutionary tuning to the Pourbaix boundary remains underspecified — what selective pressure would have tuned FDX1 redox potential to this specific value? The "ligand-extended" qualifier is important but the specific ligand complex is not named. |
| Testability | 20% | 7 | Computing the Pourbaix diagram for Cu-S-N-O systems at mitochondrial pH and checking the Cu2+/Cu+ boundary is a theoretical task doable in weeks. The confound identified by the Critic (ETC inhibitors abolish respiration AND lower Eh simultaneously) requires a designed experiment separating these effects — feasible but adds complexity, pushing clean experimental validation to 6-12 months rather than 3. |
| Groundedness | 20% | 7 | FDX1 midpoint potential -274 mV is verifiable in published literature. Pourbaix diagram methodology for Cu-S systems is established geochemistry. The Critic flagged the Eh/respiration confound but did not find the core quantitative claim to be wrong — only that the experiment to test it is complicated. Cu+ disproportionation at pH 7 is a real concern affecting the vent analogy but not the cellular mechanism directly. |
| Cross-Domain Bridge Quality | 10% | 8 | The bridge is quantitatively tight: the same Eh value (-274 mV for FDX1; -260 to -300 mV predicted Pourbaix boundary) appears in both the cellular biology and geochemical framework. This numerical coincidence demands mechanistic explanation, and removing the vent geochemistry removes the predictive framework for why FDX1 sits at exactly this potential. Strong load-bearing bridge. |
| Potential Impact | 15% | 7 | Would reframe FDX1 not merely as a reductase in the cuproptosis pathway but as an Eh sensor evolved under primordial copper-sulfide conditions. Has implications for elesclomol efficacy (dependent on mitochondrial Eh state) and for understanding why FDX1 specifically — not other ferredoxins — mediates cuproptosis. |
| **Composite** | | **7.10** | (0.15x7)+(0.20x7)+(0.20x7)+(0.20x7)+(0.10x8)+(0.15x7) = 1.05+1.40+1.40+1.40+0.80+1.05 = 7.10 |

---

### Hypothesis H1.3: H2S-CuS Nanoparticle Feed-Forward Loop

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 8 | The specific framing of CuS nanoparticle formation inside mitochondria creating a pH-dependent dissolution feed-forward loop is not found in the cuproptosis literature, which focuses on DLAT oligomerization and FDX1. H2S biology in mitochondria is active, but the CuS nanoparticle precipitation step as a mechanistic intermediate appears genuinely novel. Even if nanoparticle feasibility is challenged, the feed-forward framing itself is new and distinct. |
| Mechanistic Specificity | 20% | 6 | Names specific reagents (NaHS, nigericin, elesclomol-Cu), a biphasic timeline (protection 0-2h, potentiation 4-8h), and a rescue condition (nigericin). However, the core mechanistic step — CuS nanoparticle formation in a single mitochondrion — is quantitatively challenged (3x10^4 Cu atoms is insufficient for stable nanoparticles by standard nucleation criteria). The prediction might be observable even if the nanoparticle mechanism is wrong, so the hypothesis cannot cleanly distinguish nanoparticle-mediated from direct H2S-Cu coordination effects. |
| Testability | 20% | 7 | Biphasic cytotoxicity is directly measurable with time-resolved cell viability assays. Nigericin rescue experiment is feasible and interpretable. TEM/EELS for CuS nanoparticle detection in mitochondria is technically demanding but possible at EM core facilities. The fact that the biphasic prediction may survive without the nanoparticle mechanism is a testability asset: the observable prediction partially decouples from the mechanistic claim, allowing staged validation. |
| Groundedness | 20% | 5 | The Critic identified a quantitative problem: a single mitochondrion at cuproptosis-inducing Cu concentrations contains approximately 3x10^4 Cu atoms — insufficient to form stable CuS nanoparticles (which require roughly 10^5-10^6 atoms per particle by typical nucleation thresholds). H2S presence in mitochondria is grounded. CuS nanoparticle formation in bulk solution is grounded. The mitochondria-scale nanoparticle step is not grounded and may be physically impossible. Generator confidence was only 5/10. |
| Cross-Domain Bridge Quality | 10% | 7 | The vent geochemistry analogy (CuS precipitation in sulfide-rich fluid, pH-dependent dissolution of covellite) is load-bearing: it provides the quantitative framework for the biphasic dissolution kinetics. Removing the vent analogy loses the theoretical basis for the pH-dependent timing prediction. The bridge is genuine, though the scale mismatch (vent fluids vs single organelle) weakens its direct mechanistic applicability. |
| Potential Impact | 15% | 6 | If a feed-forward loop between H2S and Cu toxicity exists in mitochondria — even without nanoparticles — it would have implications for cancer cell H2S metabolism (CBS/CSE/3MST pathway) and cuproptosis sensitivity prediction. Nanoparticle mechanism failure would reduce impact to a secondary pharmacological observation about H2S modulation of copper cytotoxicity. |
| **Composite** | | **6.40** | (0.15x8)+(0.20x6)+(0.20x7)+(0.20x5)+(0.10x7)+(0.15x6) = 1.20+1.20+1.40+1.00+0.70+0.90 = 6.40 |

---

### Hypothesis H1.6: CuS-H2O2 Fenton-Analog Radical Cycle

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 7 | CuS nanoparticles as a Fenton-analog catalyst producing hydroxyl radical in mitochondria is a novel framing. The vent geochemistry connection (CuS mineral surfaces as Fenton-analog catalysts in hydrothermal systems) is established in geochemistry but has not been applied to cuproptosis. The specific prediction of mCAT-rescuable HO• generation during elesclomol-Cu plus NaHS treatment is not published. |
| Mechanistic Specificity | 20% | 6 | Names specific reagents (elesclomol-Cu, NaHS, HPF probe, mCAT), quantitative thresholds (HO• >= 3-fold higher, mCAT reduction >= 70%), and a molecular mechanism (CuS + H2O2 yields Cu2+ + OH- + HO•). The mechanism is borrowed from established Fenton/Haber-Weiss chemistry applied to CuS. However, the substrate H2O2 self-terminates under the same conditions (ETC disruption) that produce CuS — a mechanistic contradiction flagged by the Critic that undermines the loop's feasibility. |
| Testability | 20% | 7 | HO• detection with mitochondria-targeted HPF probe is established methodology. mCAT overexpression is widely used in the field. The experimental design is clean and the prediction quantitatively sharp. The ETC/H2O2 confound could be addressed by providing exogenous H2O2 or using a mitochondria-targeted H2O2-generating system as a co-treatment arm, adding 6-12 months to the clean validation timeline. |
| Groundedness | 20% | 4 | Two compounding ungrounded steps: (1) inherits the CuS nanoparticle formation problem from H1.3 — single-mitochondrion Cu concentrations are likely insufficient for nanoparticle nucleation; (2) ETC disruption during cuproptosis would reduce, not increase, mitochondrial H2O2 — the radical cycle's substrate is depleted by the same event that triggers it. Both were flagged by the Critic as mechanistic contradictions rather than minor calibration issues. Generator confidence was only 4/10. |
| Cross-Domain Bridge Quality | 10% | 6 | The vent-to-cell bridge (CuS mineral Fenton activity in hydrothermal chemistry applied to CuS nanoparticle Fenton activity in mitochondria) is conceptually coherent and load-bearing for the mechanism. Removing the vent analogy removes the chemical precedent for CuS as a Fenton catalyst. The scale and temperature differences (bulk mineral at 300 degrees C in vent fluid vs nanoscale particle at 37 degrees C in a mitochondrion) reduce bridge quality. |
| Potential Impact | 15% | 6 | If ROS generation via CuS Fenton chemistry contributes to cuproptosis, it would add an oxidative stress mechanism to a field that currently emphasizes proteotoxicity (DLAT oligomerization) and Fe-S destruction. Has implications for combination therapy with antioxidants in copper ionophore cancer treatment. Moderate impact because ROS in copper toxicity is not conceptually new, but the CuS-specific Fenton mechanism with a defined mineral chemistry precedent would be. |
| **Composite** | | **5.95** | (0.15x7)+(0.20x6)+(0.20x7)+(0.20x4)+(0.10x6)+(0.15x6) = 1.05+1.20+1.40+0.80+0.60+0.90 = 5.95 |

---

### Hypothesis H1.7: Evolutionary FDX1-LIAS Vent Copper Selection

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 8 | The evolutionary hypothesis that FDX1 and LIAS co-evolved specifically under copper pressure at alkaline hydrothermal vents appears unpublished. Evolutionary analyses of FDX1 exist in the context of Fe-S biogenesis and electron transfer, but copper-driven selection pressure on this axis is not a framing found in the cuproptosis or prebiotic chemistry literature. High novelty precisely because it is unexplored territory. |
| Mechanistic Specificity | 20% | 4 | The mechanism of selection under vent copper pressure is underspecified. The prediction (FDX1/LIAS divergence > 2.4 Ga; ancestral FDX1 has Cu2+ reductase activity within 5-fold of modern) names a date and a functional assay, but the intermediate mechanism — how copper pressure at alkaline vents would select for the specific FDX1 redox potential — is not articulated. The specific phylogenetic tree, outgroups, and molecular clock calibration points are not named. |
| Testability | 20% | 4 | Ancestral protein reconstruction is a real technique that has been applied to ferredoxins. However, getting to a 2.4 Ga divergence date requires a molecular clock with well-calibrated fossil constraints that are absent for FDX1. The Cu2+ reductase activity assay for ancestral FDX1 is feasible but represents 2-3 years of work minimum. The Critic noted the protocell Cu-uptake experiment is infeasible with current technology. |
| Groundedness | 20% | 4 | The 2.4 Ga date (Great Oxidation Event context) is plausible as a framework but not grounded in published FDX1 phylogenetics. The Critic's concern that Cu interaction with FDX1 may be incidental to Fe-S biogenesis is well-founded: FDX1's primary role is Fe-S cluster assembly electron donation, and Cu sensitivity may be a side effect of the Fe-S cluster rather than a selected property. Generator confidence was only 3/10 — the lowest in the surviving set. |
| Cross-Domain Bridge Quality | 10% | 7 | This is the deepest cross-domain bridge in the set: it proposes that modern cellular biochemistry (cuproptosis via FDX1-LIAS) is a direct evolutionary product of Archaean vent geochemistry. If true, the bridge is maximally load-bearing — the vent connection would explain the existence of the cuproptosis pathway rather than merely analogizing to it. Bridge quality is high in conceptual ambition even if mechanistic grounding is low. |
| Potential Impact | 15% | 7 | If confirmed, this would establish cuproptosis as an evolutionary adaptation of Archaean copper-sulfide geochemistry — connecting a 2022 cell death discovery to the origin of eukaryotic life. High-impact conceptual contribution crossing cancer biology, evolutionary cell biology, and geochemistry. The risk is that the hypothesis approaches unfalsifiability in practice, which caps its scientific utility. |
| **Composite** | | **5.35** | (0.15x8)+(0.20x4)+(0.20x4)+(0.20x4)+(0.10x7)+(0.15x7) = 1.20+0.80+0.80+0.80+0.70+1.05 = 5.35 |

---

### Hypothesis H1.1: Dithiolane-Chalcopyrite Ligand Homology

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 6 | The molecular fossil framing of lipoic acid's dithiolane ring as a relic of vent Cu-S coordination chemistry sits at the intersection of origin-of-life chemistry and cofactor evolution — a partially explored area. Convergent chemistry between organic dithiolanes and mineral sulfide coordination is discussed in prebiotic chemistry literature. The specific claim linking dithiolane geometry to chalcopyrite coordination in the cuproptosis context appears not directly published, but the framing is not distant from existing convergent-chemistry arguments. |
| Mechanistic Specificity | 20% | 5 | The log K claim (originally ~17, revised by Critic to likely 14-16) is the core quantitative anchor and is disputed. The molecular fossil claim lacks a specified inheritance mechanism — it requires either lateral gene transfer or descent with modification of a lipoic acid synthase ancestor, neither of which is named. The testable prediction (synthetic dithiolanes show Cu+ log K >= 15 under vent conditions) tests convergent chemistry rather than inheritance, leaving the core claim unaddressed by the proposed experiment. |
| Testability | 20% | 6 | Measuring Cu+ binding affinity for synthetic dithiolane compounds under vent-mimic conditions is technically feasible with ITC or competition assays. However, the test cannot distinguish convergent chemistry from molecular inheritance — a positive result would not confirm the hypothesis's distinctive claim. The prediction is testable but underdetermines the hypothesis, a significant weakness relative to hypotheses whose predictions are uniquely diagnostic. |
| Groundedness | 20% | 4 | The Critic explicitly found the KD value (log K ~17) was misattributed to Tsvetkov 2022 — Tsvetkov 2022 does not report this value, and the corrected range (14-16) is a significant downward revision. The molecular fossil claim is the type of untestable evolutionary narrative common in prebiotic chemistry speculation. Convergent chemistry between dithiolanes and metal-sulfide minerals is plausible but weakly grounded without specific coordination chemistry studies linking these two systems. |
| Cross-Domain Bridge Quality | 10% | 5 | The bridge is analogical rather than causal. Dithiolane rings resemble Cu-S coordination geometries in chalcopyrite, but this resemblance does not mechanistically connect cuproptosis to vent geochemistry via a causal pathway. Removing the bridge (dithiolane is simply an ancient cofactor with no vent connection) leaves the cuproptosis mechanism unchanged. The bridge is decorative for the biology even if the chemical analogy is interesting. |
| Potential Impact | 15% | 5 | If the molecular fossil claim were confirmed, it would reshape the origin-of-life narrative for lipoic acid and connect cuproptosis to prebiotic chemistry. However, even confirmation would not change cuproptosis therapeutics or mechanistic understanding of the cell death pathway. Impact is primarily conceptual with limited translational or mechanistic consequence for either constituent field. |
| **Composite** | | **5.15** | (0.15x6)+(0.20x5)+(0.20x6)+(0.20x4)+(0.10x5)+(0.15x5) = 0.90+1.00+1.20+0.80+0.50+0.75 = 5.15 |

---

## Final Ranking Table

| Rank | ID | Composite | Novelty (15%) | Mech Spec (20%) | Testability (20%) | Groundedness (20%) | Bridge Quality (10%) | Impact (15%) | Critic Verdict |
|------|-----|-----------|--------------|-----------------|-------------------|--------------------|----------------------|--------------|----------------|
| 1 | H1.4 | **8.25** | 7 | 9 | 9 | 8 | 8 | 8 | PASS |
| 2 | H1.2 | **7.10** | 7 | 7 | 7 | 7 | 8 | 7 | CONDITIONAL_PASS |
| 3 | H1.3 | **6.40** | 8 | 6 | 7 | 5 | 7 | 6 | CONDITIONAL_PASS |
| 4 | H1.6 | **5.95** | 7 | 6 | 7 | 4 | 6 | 6 | CONDITIONAL_PASS |
| 5 | H1.7 | **5.35** | 8 | 4 | 4 | 4 | 7 | 7 | CONDITIONAL_PASS |
| 6 | H1.1 | **5.15** | 6 | 5 | 6 | 4 | 5 | 5 | CONDITIONAL_PASS |

**Top-3 composite average: (8.25 + 7.10 + 6.40) / 3 = 7.25**

Note: This ranking diverges from the Critic's post-critique ordering (H1.4 > H1.2 > H1.3 > H1.1 > H1.7 > H1.6) at positions 4-6. The Ranker promotes H1.6 above H1.7 and H1.1 because H1.6's experimental readout (HO• probe, mCAT overexpression) is more immediately executable than H1.7's ancestral protein reconstruction (2-3 year minimum) or H1.1's underdetermining ligand-binding test. The 20% Testability weight drives this separation.

---

## Diversity Check

Examining the top 5 hypotheses (H1.4, H1.2, H1.3, H1.6, H1.7):

**Convergence assessment:**
- H1.3 and H1.6 share a bridge mechanism (CuS nanoparticle formation as a mechanistic intermediate). This is the only convergent pair in the top 5. Their downstream predictions differ cleanly: H1.3 predicts biphasic cytotoxicity + nigericin rescue; H1.6 predicts HO• generation + mCAT rescue. They test different downstream consequences.
- All other pairs span distinct mechanisms, experimental approaches, and bridge logic.
- The 3-pair convergence threshold (required to trigger diversity adjustment) is not reached.

**Top-3 diversity:**
- H1.4: Thermodynamic displacement — Fe-S cluster reconstitution, ICP-MS, CIA/LIAS differential overexpression
- H1.2: Redox potential alignment — Pourbaix diagram calculation, Eh manipulation, spectroelectrochemistry
- H1.3: Nanoparticle kinetics — biphasic viability assay, nigericin rescue, TEM/EELS

These span different mechanism types, different experimental platforms, and different bridge logic (thermodynamic solubility product vs Eh alignment vs nanoparticle dissolution kinetics).

**Diversity check result: PASS.** No re-ranking adjustment needed.

---

## Elo Tournament Sanity Check

All 6 survivors participate. 15 pairwise comparisons. Question per matchup: "Which hypothesis would a domain researcher want to test FIRST?"

| # | Matchup | Winner | Reasoning |
|---|---------|--------|-----------|
| 1 | H1.4 vs H1.2 | H1.4 | CIA/LIAS differential rescue is more definitive and less confounded than the Eh/respiration-entangled Pourbaix test. |
| 2 | H1.4 vs H1.3 | H1.4 | H1.4 has no quantitative impossibility in its mechanism; H1.3 carries the nanoparticle nucleation problem. |
| 3 | H1.4 vs H1.6 | H1.4 | H1.6 has two compounding contradictions (nanoparticle + ETC H2O2 depletion); H1.4 has none flagged by Critic. |
| 4 | H1.4 vs H1.7 | H1.4 | H1.4 testable in 3 months; H1.7 requires ancestral protein reconstruction at minimum 2-3 years. |
| 5 | H1.4 vs H1.1 | H1.4 | H1.1 has a misattributed KD and a test that cannot distinguish convergent from inherited chemistry. |
| 6 | H1.2 vs H1.3 | H1.2 | Pourbaix calculation takes weeks as first step; H1.3's core mechanism is physically challenged at the mitochondrial scale. |
| 7 | H1.2 vs H1.6 | H1.2 | H1.6 has two mechanistic contradictions; H1.2's Eh/respiration confound is a solvable experimental design problem. |
| 8 | H1.2 vs H1.7 | H1.2 | H1.2 testable in 6-12 months with proper controls; H1.7 at minimum 2-3 years for ASR. |
| 9 | H1.2 vs H1.1 | H1.2 | H1.2 has a quantitatively grounded bridge; H1.1 has a misattributed citation and an underdetermining test design. |
| 10 | H1.3 vs H1.6 | H1.3 | Both share the nanoparticle problem, but H1.3's biphasic prediction is partially testable without nanoparticle confirmation; H1.6 additionally faces H2O2 self-termination. |
| 11 | H1.3 vs H1.7 | H1.3 | H1.3 testable in 6-12 months; H1.7 requires ASR with no reliable molecular clock calibration for FDX1. |
| 12 | H1.3 vs H1.1 | H1.3 | H1.3 has a clean falsifiable prediction (biphasic viability curve); H1.1's test is inconclusive by design. |
| 13 | H1.6 vs H1.7 | H1.6 | Despite dual mechanistic contradictions, the HO• probe experiment is straightforward; H1.7 lacks near-term testability. |
| 14 | H1.6 vs H1.1 | H1.6 | H1.6's predictions are directly falsifiable with standard assays; H1.1's ligand-binding test cannot confirm the inheritance claim even if positive. |
| 15 | H1.7 vs H1.1 | H1.7 | H1.7's ancestral reconstruction, despite being long, stakes a definitive functional claim; H1.1's test underdetermines its core hypothesis regardless of outcome. |

**Win tally:**

| Hypothesis | Wins (out of 5) | Win Rate | Elo Rank |
|------------|-----------------|----------|----------|
| H1.4 | 5 | 100% | 1 |
| H1.2 | 4 | 80% | 2 |
| H1.3 | 3 | 60% | 3 |
| H1.6 | 2 | 40% | 4 |
| H1.7 | 1 | 20% | 5 |
| H1.1 | 0 | 0% | 6 |

**Elo ranking: H1.4 > H1.2 > H1.3 > H1.6 > H1.7 > H1.1**
**Linear composite ranking: H1.4 > H1.2 > H1.3 > H1.6 > H1.7 > H1.1**

**Result: Elo confirms linear ranking.** Rankings are identical across all 6 positions. No divergence to report.

The Critic's post-critique ordering differed at positions 4-6 (Critic: H1.1 > H1.7 > H1.6). Both Elo and linear composite agree that H1.6 should rank 4th over H1.7 and H1.1 because 20% Testability weight systematically penalizes hypotheses whose tests are inconclusive by design (H1.1) or require multi-year timelines (H1.7).

---

## Evolution Selection (Post-Diversity Check)

**Top-3 composite average: 7.25 — exceeds the 6.5 Evolver-skip threshold.**

Per adaptive cycle rules, the Evolver may be skipped if top-3 average >= 6.5. However, evolution is still recommended for hypotheses 2-4 to address Critic-identified mechanistic problems before Quality Gate.

**Selected for evolution: H1.4, H1.2, H1.3, H1.6**

| ID | Priority | Evolution task |
|----|----------|----------------|
| H1.4 | Strengthen | Add explicit Ksp calculation (CuS vs FeS2 solubility products) to experimental methods; add Fe2+ release stoichiometry as a second falsifiable prediction alongside CIA/LIAS timing differential. |
| H1.2 | Fix confound | Design explicit Eh-manipulation protocol that separates Eh from respiration (chemical Eh clamps, reconstituted systems, or anaerobic decoupled assay per Critic's suggestion). |
| H1.3 | Mechanistic surgery | Remove or heavily qualify the nanoparticle nucleation step; re-anchor on H2S-Cu coordination chemistry and biphasic kinetics directly, treating nanoparticle as a theoretical upper-bound scenario rather than the mechanism. |
| H1.6 | Fix H2O2 paradox | Add exogenous H2O2 co-treatment arm to decouple substrate supply from ETC disruption; alternatively identify an alternative matrix ROS source not dependent on ETC activity. |

**Excluded from evolution:**
- H1.7: Groundedness 4, Testability 4, Generator confidence 3/10. Too speculative with a 2-3 year minimum timeline. Not worth an evolution cycle; return to if cycle 2 produces insufficient survivors.
- H1.1: Misattributed foundational citation (log K value), analogical-only bridge, test underdetermines the core inheritance claim regardless of outcome. Not salvageable in one evolution cycle.
