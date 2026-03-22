# Cross-Model Validation Consensus — Session 2026-03-21-scout-008

**Target**: Cuproptosis x Hydrothermal Vent Copper-Sulfide Geochemistry
**Hypotheses validated**: E1.1 (PASS, rubric 8.1) and E1.4 (CONDITIONAL_PASS, rubric 7.3)
**Note**: E1.3 was included in the export prompts as a third hypothesis (scored 6.45, CONDITIONAL_PASS by QG). Validation results for all three are included below; E1.1 and E1.4 are the primary candidates.

---

## Methodology

- **GPT-5.4 Pro** (reasoning_effort: high, ~880s): Empirical validation — novelty assessment, counter-evidence search, mechanism plausibility, experimental design critique
- **Gemini 3.1 Pro** (thinkingLevel: HIGH, ~32s): Structural analysis — mathematical mappings, formal isomorphisms, quantitative predictions, symmetry analysis

---

## Per-Hypothesis Consensus

### E1.1 — Pourbaix-Quantified Fe-S Cluster Displacement

| Dimension | GPT-5.4 Pro | Gemini 3.1 Pro | Consensus |
|-----------|-------------|----------------|-----------|
| Novelty | PARTLY NOVEL — quantitative Pourbaix framing new; Cu-Fe-S displacement itself established | Formal isomorphism confirmed — Nernst/mass-action equations identical across geo and bio | **Agree: novel framing, established substrate** |
| Confidence | 6/10 | 9/10 (structural) | **Range 6-9; divergence on mechanism certainty** |
| Mechanism | 6.5/10 plausibility — chemistry real but Fe-S damage may be secondary to lipoyl aggregation | Formal isomorphism — Gibbs free energy minimization, Irving-Williams invariant; LIAS destruction pseudo-first-order by solvent accessibility | **Agree on thermodynamic validity; diverge on whether primary lethal event** |
| Testability | MVE: anaerobic [4Fe-4S] target + Cu(I)-GSH + ferrozine; time-resolve vs DLAT aggregation; CIA should be ISC | Ligand-extended Pourbaix + EPR threshold mapping; independently perturb Eh and pH with redox cyclers + ionophores | **Complementary: GPT prioritizes temporal ordering; Gemini phase-boundary mapping** |

**Agreement areas**: Both models confirm the thermodynamic calculation is sound (K = 10^7.5, ΔG = -44.5 kJ/mol direction is correct). Both agree that the LIAS double-cluster architecture creates genuine vulnerability. Both identify the CIA/ISC naming confusion as a design flaw needing correction.

**Divergence areas**: GPT-5.4 Pro (6/10 confidence) raises a fundamental mechanistic challenge — cuproptosis genetics fingerprint lipoylated TCA proteins, not ISC assembly factors, suggesting Fe-S displacement is an amplifier not the primary lesion. Gemini (9/10 structural) treats the Nernst/Ksp isomorphism as near-definitive but does not assess primary-vs-secondary event ordering. The Irving-Williams series citation is critiqued by GPT as inapplicable to Cu(I) exchange into multi-metal sulfide clusters (series is for divalent M(II) complexes only).

**Combined recommendation**: HIGH PRIORITY with reframing. The thermodynamics are solid and the geochemical/biological isomorphism is formally valid. The critical unresolved question is temporal: does Fe-S cluster attack precede or follow lipoylated DLAT oligomerization? This must be the first experiment (time-resolved aconitase activity vs. anti-lipoyl crosslinking). CIA must be corrected to ISC throughout the protocol.

---

### E1.4 — FDX1 as Calibrated Kinetic Gate with Elesclomol Speciation

| Dimension | GPT-5.4 Pro | Gemini 3.1 Pro | Consensus |
|-----------|-------------|----------------|-----------|
| Novelty | MODERATELY NOVEL — FDX1-elesclomol dependency established; kinetic-gate framing and sigmoidal E0' prediction are new | Structural analogy (Marcus-Hush) — homomorphism between FDX1 active site and mineral surface catalysis; isoenergetic resonance mapping confirmed | **Agree: quantitative kinetic-gate framing is new** |
| Confidence | 5/10 | 8/10 (structural) | **Range 5-8; widest divergence** |
| Mechanism | 5.5/10 — FDX1 lipoylation role is dominant confound; redox-gating conflated with lipoylation; lipoyl oxidation state unspecified | Marcus theory predicts FDX1 lowers reorganization energy (lambda); near-isoenergetic transfer (ΔG ≈ 0) means rate entirely governed by lambda minimization | **Agree on Marcus framework; diverge on whether FDX1 mutant library tests reduction vs lipoylation** |
| Testability | Must uncouple FDX1 redox role from lipoylation role; use protein-bound lipoyl-lysine not free lipoamide; LplA bypass to rescue lipoylation independently | ITC to verify ΔG ≈ 0 transfer; stopped-flow kinetics; FDX1 mutants should show exponential cuproptosis drop as E0' deviates from -274 mV | **Complementary: GPT identifies the confound; Gemini provides the formal prediction to test** |

**Agreement areas**: Both models confirm elesclomol-to-lipoyl Cu transfer thermodynamics are near-isoenergetic, making the system kinetically controlled. Both predict FDX1 mutant library as the key experiment. Both confirm absolute novelty of applying Pourbaix/Marcus framework to intracellular copper speciation.

**Divergence areas**: GPT (5/10) identifies the critical confound — FDX1 knockout reduces protein lipoylation (established in Tsvetkov et al. 2022), so cuproptosis resistance in FDX1-KO may reflect fewer lipoylated targets, not slower Cu reduction. Gemini (8/10 structural) does not assess this confound, focusing instead on the formal Marcus mapping. GPT also raises that free lipoamide has different Cu affinity from protein-bound reduced dihydrolipoyl-lysine — making the Ka ratio of 1.26 underspecified unless redox state is explicit.

**Combined recommendation**: PROMISING — but requires biochemical decoupling experiment before cell work. The Marcus-theory prediction (exponential cuproptosis drop as FDX1 E0' deviates from -274 mV) is testable and would distinguish kinetic-gate from lipoylation-maintenance models. LplA-mediated lipoate ligation bypass is the key experimental innovation. Without it, FDX1 mutant library results will be uninterpretable.

---

### E1.3 — Evolutionary Cu-Driven FDX1-LIAS Co-Selection (supplemental)

| Dimension | GPT-5.4 Pro | Gemini 3.1 Pro | Consensus |
|-----------|-------------|----------------|-----------|
| Novelty | GENUINELY NOVEL — no published FDX1-LIAS co-selection driven by copper pressure | Formal homomorphism — information-theoretic fitness mapping from Pourbaix state space to FDX1 sequence space | **Agree: novel** |
| Confidence | 3/10 | 6.8/10 (structural) | **Widest divergence; lowest experimental support** |
| Mechanism | 3.5/10 — biochemical necessity (LIAS needs electron donors) explains co-occurrence more parsimoniously; sulfide precipitation negates "Cu-rich = Cu stress" | Shannon entropy conservation; mutual information I(E;S) between paleo-Pourbaix state and FDX1 D136/D139 sequence motifs | **Agree on information-theoretic framing; diverge on whether signal exceeds neutral drift** |
| Testability | Phylogenetically corrected logistic regression; model labile dissolved Cu (not bulk mineral) from pH/Eh/sulfide; ancestral FDX1 Cu reduction + LIAS support assays | ASR of FDX1 nodes at Great Oxidation Event; regress synthesized protein E0' against isotope-derived paleo-Pourbaix data | **Complementary: GPT corrects the "Cu-rich" confound; Gemini provides the regression target** |

**Agreement areas**: Both models agree the hypothesis is genuinely novel. Both suggest ancestral sequence reconstruction as the credible experimental route.

**Divergence areas**: GPT gives 3/10 confidence because vent sulfide chemistry buffers free Cu (Cu precipitates as CuS/chalcopyrite), meaning "Cu-rich environment" does not equal intracellular Cu stress. Copper stress more commonly selects for export/sequestration than for stronger Cu reductases. Gemini is more optimistic (6.8/10) on the formal mapping but acknowledges historical contingency and pleiotropy degrade the signal.

**Combined recommendation**: LOWER PRIORITY — interesting as evolutionary speculation; requires preliminary phylogenetic signal test before any wet-lab investment. Critical first step: model bioavailable dissolved Cu (not bulk mineralogy) for vent vs. non-vent taxa using CHESS/GEMS speciation calculations. Raw co-occurrence will be uninterpretable without this correction.

---

## Cross-Cutting Issue Identified by GPT-5.4 Pro

Both E1.1 and E1.4 apply equilibrium Pourbaix logic to the mitochondrial matrix. GPT raises an important caution: vent geochemistry uses relatively simple ligand sets; mitochondria are dominated by protein thiolates, lipoyl-lysines, GSH/GSSG, and Cu chaperones. Free Cu(I) in the matrix is expected at sub-attomolar concentrations (fully protein/thiol-buffered), meaning **bulk thermodynamic favorability does not imply freely exchangeable Cu attack**. The Pourbaix framework remains valuable as a heuristic, but quantitative window claims (e.g., Eh = -250 to -320 mV ± 30 mV) require conditional potentials derived from the actual biological ligand mixture, not free-ion standard potentials.

Gemini's formal isomorphism analysis does not dispute the thermodynamic logic but independently arrives at the same conclusion: in vitro validation must use the actual protein-embedded ligand context, not free lipoic acid at 5 mM.

---

## Summary

### High-Priority Candidates

**E1.1 — Pourbaix-Quantified Fe-S Cluster Displacement**
Both models confirm formal validity of the thermodynamic isomorphism. GPT confidence: 6/10. Gemini structural confidence: 9/10. The key open question GPT identifies is primary-vs-secondary event ordering (Fe-S damage before or after lipoyl aggregation). Recommend executing the time-resolved experiment before any mechanistic investment: anaerobic [4Fe-4S] target (mitochondrial aconitase or ISCA) + Cu(I)-GSH + simultaneous readout of Fe2+ release (ferrozine), aconitase activity, and lipoyl-DLAT crosslinking at t = 15, 30, 60, 120 min. ISC overexpression (not CIA) as protective arm.

**E1.4 — FDX1 Kinetic Gate + Elesclomol Speciation**
Promising but requires decoupling. GPT confidence: 5/10. Gemini structural confidence: 8/10. The Marcus-theory prediction is testable and formally clean: FDX1 mutant library should show exponential sensitivity drop as E0' shifts from -274 mV. But this is uninterpretable without an independent lipoylation rescue (LplA bypass or equivalent). Recommend biochemical gate experiment first: NADPH/FDXR/FDX1 + elesclomol-Cu(II) + lipoylated DLAT E2 domain, anaerobic, stopped-flow, measuring Cu(I) generation rate and protein-Cu transfer.

### Needs Investigation

**E1.3 — Evolutionary Co-Selection**
Genuinely novel but lowest confidence (GPT 3/10, Gemini 6.8/10). GPT's sulfide-buffering counter-argument is strong — "Cu-rich vent" may not equal intracellular Cu stress. Do not invest wet-lab resources until a phylogenetically corrected signal test is completed with bioavailable (not total) Cu as the environmental variable.

### Key Experimental Priorities

1. **Temporal ordering experiment for E1.1**: Is Fe-S cluster attack before or after DLAT oligomerization? This resolves primary-vs-amplifier status with a single time-course.
2. **LplA bypass cell line for E1.4**: Rescuing lipoylation independently of FDX1 is the enabling experiment for the entire kinetic-gate mutant library.
3. **Conditional Cu potential measurement**: Measure E0' of Cu2+/Cu+ in a mitochondrial-mimetic buffer (5 mM GSH, physiological protein thiolates, pH 7.8) by potentiometric titration — this is the input the Pourbaix model actually needs.
4. **E1.3 phylogenetic pre-screen**: Model dissolved labile Cu for vent genomes from GTDB r220 metadata before any ancestral reconstruction investment.

---

## Models Used

| Model | Role | Duration | Reasoning |
|-------|------|----------|-----------|
| GPT-5.4 Pro | Empirical validation | 880s | High reasoning effort |
| Gemini 3.1 Pro | Structural analysis | 32s | Thinking: HIGH |
