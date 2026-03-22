# Evolved Hypotheses — Session 008, Cycle 1

**Date**: 2026-03-22
**Evolver model**: Opus 4.6
**Parent hypotheses**: H1.4 (7.90), H1.2 (7.15), H1.3 (5.80), H1.7 (4.25)
**Operations**: 2 crossovers, 2 mutations
**Killed during evolution**: 0
**Diversity check**: PASSED (3 distinct bridge mechanisms)

---

## E1.1: Pourbaix-Quantified Fe-S Cluster Displacement — Predicting the Eh Window of Cuproptotic Lethality

**Parents**: H1.4 (Fe-S Cluster Cannibalization) × H1.2 (FDX1 Redox Pourbaix)
**Operation**: CROSSOVER

**Mechanism**: Cu⁺ displaces Fe²⁺ from [4Fe-4S] clusters with K(displacement) = 10⁷·⁵ (ΔG = −44.5 kJ/mol) [GROUNDED: computed from Cu₂S Ksp 2.5×10⁻⁴⁸ vs FeS Ksp 6×10⁻¹⁹; experimentally validated by Macomber & Imlay 2009, PMID 19416816]. A ligand-extended Pourbaix diagram — incorporating GSH (5 mM), lipoic acid (1–100 μM), and Fe-S cluster sulfide ligands — will reveal a critical Eh window (−250 to −320 mV) where Cu⁺ is thermodynamically stable AND kinetically competent to attack protein-bound Fe-S clusters. FDX1 (E₀' = −274 mV) [GROUNDED: adrenodoxin literature] operates as a kinetic facilitator — not a thermodynamic driver [GROUNDED: computational validator] — accelerating Cu²⁺→Cu⁺ conversion to produce the displacing species at rates exceeding cluster repair by CIA/LIAS pathways.

**What's new vs parents**: H1.4 established the displacement thermodynamics; H1.2 proposed the Pourbaix framework. This crossover (1) embeds displacement in a Pourbaix Eh-pH map to predict the lethal window, (2) resolves H1.2's fatal confound (FDX1 as kinetic, not thermodynamic), (3) adds cluster-type kinetic accessibility prediction addressing H1.4's Critic question, and (4) replaces H1.2's problematic ETC inhibitor test with a genetic approach.

**Bridge type**: Cu-Fe sulfide replacement chemistry mapped onto Eh-pH speciation space.

**Falsifiable predictions**:
1. **Pourbaix-displacement map**: Ligand-extended Pourbaix diagram (PHREEQC/Geochemist's Workbench, including Fe-S cluster ligand fields) predicts Cu⁺→Fe²⁺ displacement onset at Eh = −240 ± 30 mV at pH 7.4–8.2. Below Eh −350 mV, displacement rate saturates (all Cu already Cu⁺). Above Eh −200 mV, Cu²⁺ dominates and displacement rate drops ≥10-fold.
2. **In vitro stoichiometry**: Reconstituted [4Fe-4S] ferredoxin + Cu⁺ (anaerobic, pH 8.0, Eh −300 mV) yields stoichiometric Fe²⁺ release at Cu:Fe = 1.0 ± 0.2. Rate constant k(displacement) ≥ 10³ M⁻¹s⁻¹ at pH 8.0, dropping ≤10² M⁻¹s⁻¹ at pH 6.5 (protonation of bridging sulfides).
3. **CIA vs LIAS differential**: CIA pathway overexpression (CIA1/CIA2B/MMS19) delays cuproptosis onset ≥2 h in MOLM-13 cells because CIA repairs cytosolic clusters faster than Cu⁺ destroys them. LIAS overexpression delays ≤30 min because Cu⁺ destroys mitochondrial [4Fe-4S] clusters at the LIAS active site faster than new clusters are inserted — the pathway substrate is also its vulnerability.
4. **FDX1 kinetic role**: FDX1 point mutants with E₀' shifted to −200 mV (less reducing) reduce cuproptosis sensitivity by ≥40% without changing Fe-S biogenesis capacity, confirming kinetic Cu²⁺ reduction, not structural scaffolding, is the lethal function.

**Test protocol**:
(1) Computational: Ligand-extended Pourbaix including Fe-S cluster sulfide fields (PHREEQC + MINTEQ database supplemented with Cu-thiol stability constants from Sander & Koschinsky 2011).
(2) In vitro: [4Fe-4S] ferredoxin reconstitution + Cu⁺ titration under potentiostat Eh control (−400 to −100 mV). Fe release by ferrozine assay. Cu coordination by EXAFS at Cu K-edge.
(3) In cellulo: MOLM-13 with dox-inducible CIA1+CIA2B+MMS19 vs LIAS; elesclomol-Cu time-course (0–8 h). Viability (CellTiter-Glo), DLAT aggregation (BN-PAGE), Fe-S cluster status (aconitase activity).
(4) Genetic: FDX1 E₀' mutant library (site-saturation at C46, C52, C55, H56 — iron ligands) screened for cuproptosis resistance in FDX1-KO MOLM-13 rescue.

**Confidence**: 7 | **Groundedness**: 8

The crossover is synergistic: H1.4's thermodynamic rigor (Ksp-based, experimentally validated in E. coli) gains H1.2's quantitative prediction framework (Pourbaix). The ligand-extended Pourbaix remains hypothetical [GROUNDED: evaluation condition 2], but the displacement itself is established [GROUNDED: Macomber & Imlay 2009]. The CIA vs LIAS differential is the cleanest test — it distinguishes direct Cu⁺ displacement from indirect proteotoxic damage with no pharmacological confounds. The FDX1 mutant test eliminates H1.2's ETC inhibitor confound (respiratory cessation independently kills cuproptosis).

---

## E1.2: CuS Oligomer Buffering — Sub-Nanoparticle Copper-Sulfide Coordination Polymers as Mitochondrial Copper Reservoirs

**Parent**: H1.3 (H₂S Potentiates Cuproptosis Through CuS Nanoparticle Formation)
**Operation**: MUTATION (downscale from nanoparticles to oligomers)

**Mechanism**: At biological concentrations (~3×10⁴ Cu atoms per mitochondrion [GROUNDED: Cobine et al. 2004], H₂S 10–100 nM [GROUNDED: Kabil & Banerjee 2014]), CuS does not form crystalline nanoparticles but instead forms amorphous CuS oligomers (Cu₂S₃, Cu₃S₄, Cu₄–₆Sₙ clusters of 0.5–2 nm) — coordination polymers below the nucleation threshold for crystalline covellite. These oligomers are metastable copper reservoirs: thermodynamically stable at basal Eh (−300 mV) and pH (8.0) [GROUNDED: CuS Ksp = 6×10⁻³⁶], but susceptible to oxidative dissolution when H₂O₂ rises during early cuproptosis, releasing Cu⁺ in a burst that overwhelms lipoylation targets.

**What's new vs parent**: Replaces the physically impossible nanoparticle claim (Critic: 3×10⁴ Cu insufficient for 10 nm particle requiring ~10⁵ atoms) with sub-nanoparticle oligomers consistent with copper atom counts. Replaces TEM/EDX (cannot distinguish CuS from Cu-DLAT) with XAS/EXAFS, which detects Cu-S coordination geometry regardless of crystallinity.

**Bridge type**: Sub-nanoparticle CuS phase chemistry in mitochondria mirroring vent CuS precipitation/dissolution.

**Falsifiable predictions**:
1. **Cu-S coordination by XAS**: Cu K-edge XANES of mitochondria from NaHS-pretreated cells (100 μM, 2 h) + elesclomol-Cu shows CuS-like nearest-neighbor shell (Cu-S at 2.19–2.23 Å, coordination number 3–4) distinct from Cu-thiolate protein binding (Cu-S at 2.13–2.16 Å, coordination number 2) [GROUNDED: standard EXAFS distances]. This signal appears at 1–2 h and diminishes by 6 h (dissolution).
2. **Biphasic cytotoxicity**: NaHS (100 μM) + elesclomol-Cu (40 nM + 400 nM CuCl₂) shows protection at 0–2 h (CuS oligomers sequester Cu) then potentiation at 4–8 h (H₂O₂-driven release). EC₅₀ at 6 h is ≥2-fold lower with NaHS than without.
3. **pH-dependent release**: Nigericin (10 μM, collapses ΔpH) abolishes late-phase potentiation (≥50% rescue at 6 h) by preventing the pH drop that accelerates CuS dissolution.
4. **Oligomer size**: Cryo-EM of isolated mitochondria (NaHS + elesclomol-Cu, 2 h) may show electron-dense puncta <2 nm colocalizing with cristae. (Exploratory — absence does not falsify if XAS confirms Cu-S coordination.)

**Test protocol**:
(1) MOLM-13/A549 + elesclomol (40 nM) + CuCl₂ (400 nM) ± NaHS (100 μM) ± nigericin (10 μM). Time-course viability (0, 2, 4, 6, 8 h).
(2) Synchrotron XAS at Cu K-edge on mitochondrial fractions at 2 h and 6 h time points. EXAFS shell fitting for Cu-S coordination.
(3) Mito-pH monitoring (SypHer3s) to correlate pH drop with CuS dissolution window.
(4) Cu speciation control: BCS (Cu⁺ chelator) added at 3 h should block late-phase potentiation if released Cu⁺ is the effector.

**Confidence**: 5 | **Groundedness**: 6

The mutation resolves H1.3's central physical impossibility while preserving its testable biphasic prediction. CuS oligomers at sub-nanoparticle scale are thermodynamically expected (Ksp drives precipitation even at low concentrations) [GROUNDED] but have never been characterized in mitochondria [SPECULATIVE]. The XAS approach can detect Cu-S coordination regardless of crystallinity — a critical methodological upgrade. The vent connection is preserved: sub-nanoparticle CuS clusters form in vent mixing zones before growing to covellite [GROUNDED: Luther et al. 2002, metal sulfide nanoparticle nucleation at vents].

---

## E1.3: Cuproptosis as Evolutionary Relic — Fe-S Displacement as Selection Pressure for FDX1-LIAS Co-Evolution in High-Cu Vent Environments

**Parents**: H1.4 (Fe-S Cluster Cannibalization) × H1.7 (Evolutionary Reconstruction)
**Operation**: CROSSOVER (displacement mechanism + evolutionary genomics, replacing infeasible protocell)

**Mechanism**: The Fe-S displacement mechanism (Cu⁺ replacing Fe²⁺ in [4Fe-4S] clusters, K = 10⁷·⁵) [GROUNDED: Macomber & Imlay 2009] was the ancient selection pressure that drove co-evolution of FDX1 (Cu²⁺→Cu⁺ kinetic control) and LIAS (Fe-S cluster-dependent lipoylation). In high-Cu vent environments, organisms that coupled a reductase (proto-FDX1) to a robust Fe-S repair/utilization pathway (proto-LIAS) survived Cu⁺ assault on their Fe-S clusters. Cuproptosis is this ancient defense failing when copper overwhelms the FDX1-LIAS axis.

**What's new vs parents**: H1.7's evolutionary narrative gains H1.4's specific mechanism (displacement, not vague "copper stress"). The infeasible protocell experiment (Critic: ~6 simultaneous parameters) is replaced with comparative genomics of extant Cu-tolerant organisms — an approach that is tractable with existing databases and tools.

**Bridge type**: Evolutionary co-selection driven by Cu-Fe sulfide displacement chemistry.

**Falsifiable predictions**:
1. **FDX1-LIAS genomic co-occurrence**: In a panel of ≥200 prokaryotic genomes spanning Cu-rich (acid mine drainage, hydrothermal) and Cu-poor (deep ocean sediment, freshwater) environments, FDX1 homolog and LIAS homolog genomic co-occurrence is significantly higher in Cu-rich habitat organisms (Fisher exact p < 0.01), and the genetic distance between them (operon proximity or regulatory linkage) is shorter.
2. **FDX1 Cu-resistance signatures**: FDX1 orthologs from Cu-tolerant organisms (e.g., Acidithiobacillus, Sulfolobus, vent-associated archaea) show convergent substitutions at positions contacting Fe-S clusters — specifically, residues that modulate the accessibility of the [2Fe-2S] cluster to Cu⁺. These positions will overlap with cuproptosis-sensitizing mutations in human FDX1.
3. **Ancestral FDX1 reconstruction**: Ancestral FDX1 (reconstructed by FireProt-ASR, targeting LUCA node) retains Cu²⁺ reductase activity (kcat/Km within 10-fold of human FDX1) AND shows higher tolerance to Cu⁺-mediated inactivation than human FDX1 (IC₅₀ ≥3-fold higher), consistent with selection for Cu resistance.
4. **Pre-GOE divergence**: Molecular clock analysis (BEAST2, calibrated by geochemical events) places FDX1-LIAS pathway divergence at >2.4 Ga, with the Cu-binding interface more conserved than the steroidogenic interface across archaea and bacteria.

**Test protocol**:
(1) Comparative genomics: Download curated prokaryotic genomes from GTDB (≥200, stratified by environment Cu concentration). Quantify FDX1/LIAS co-occurrence, operon distance, and regulatory linkage. Statistical test: Fisher exact + Bonferroni.
(2) Phylogenomics: IQ-TREE maximum likelihood tree of FDX1 across all domains. dN/dS at Cu-interacting vs non-interacting residues. BEAST2 molecular clock.
(3) Ancestral reconstruction: FireProt-ASR for LUCA-node FDX1. Express in E. coli. Protein film voltammetry for E₀'. Cu²⁺ reductase kinetics. Cu⁺ inactivation assay (IC₅₀).
(4) Cross-reference: Map FDX1 positions that (a) show convergent evolution in Cu-tolerant organisms AND (b) modulate cuproptosis sensitivity in human cell CRISPR screens [GROUNDED: Tsvetkov 2022 screen data].

**Confidence**: 5 | **Groundedness**: 6

This crossover transforms H1.7's untestable evolutionary narrative into a data-driven hypothesis grounded in H1.4's mechanistic specificity. Every prediction is testable with existing databases and standard techniques (no protocells required). The key evolutionary insight: if Cu⁺ displacement of Fe-S clusters was the selection pressure, then FDX1 variants in Cu-rich environments should show specific adaptations at the Cu-interaction interface — and those same positions should matter for cuproptosis in human cells. Weakness: genomic co-occurrence could reflect shared metabolic need for Fe-S clusters rather than Cu-specific selection [SELF-CRITIQUE]. The dN/dS analysis at Cu-interacting residues specifically tests for Cu-driven selection.

---

## E1.4: FDX1 as Calibrated Kinetic Gate — Ligand-Extended Pourbaix With Elesclomol Speciation and Genetic Test

**Parent**: H1.2 (FDX1 Redox Potential Tuned to Vent Cu²⁺/Cu⁺ Boundary)
**Operation**: MUTATION (fix 3 Critic-identified confounds)

**Mechanism**: FDX1 (E₀' = −274 mV) [GROUNDED] serves as a calibrated kinetic gate for Cu²⁺→Cu⁺ conversion in the mitochondrial matrix. Its midpoint potential falls within the Cu²⁺/Cu⁺ transition zone of a ligand-extended Pourbaix diagram that includes GSH (5 mM), lipoic acid (1–100 μM), and — critically — the elesclomol carrier ligand (Ka = 10¹⁷·¹) [GROUNDED: computational validator]. When FDX1 reduces Cu²⁺ from the elesclomol complex (near-isoenergetic transfer, ΔKa ≈ 1.26) [GROUNDED: computational validator], the liberated Cu⁺ enters a thermodynamic landscape that favors lipoyl-thiol binding over all other available ligands.

**What's new vs parent**: (1) Adds elesclomol speciation to the Pourbaix framework — H1.2 ignored the carrier molecule. (2) Replaces ETC inhibitor test (fatal confound: respiratory cessation independently blocks cuproptosis) with FDX1 E₀' mutant library. (3) Restricts Cu⁺ stability analysis to ligand-extended domain, sidestepping Critic's Cu⁺ disproportionation concern (Cu⁺ disproportionation is suppressed by thiol ligands that stabilize Cu⁺ complexes) [GROUNDED: standard Cu⁺ coordination chemistry]. (4) Adds explicit anti-post-hoc-fitting test: predict THEN measure.

**Bridge type**: Quantitative Eh-pH correspondence between vent geochemistry and mitochondrial copper redox kinetics.

**Falsifiable predictions**:
1. **Ligand-extended Pourbaix**: The Cu²⁺/Cu⁺ boundary shifts from Eh = +150 mV (ligand-free) [GROUNDED: Beverskog & Puigdomenech 1997] to Eh = −260 ± 30 mV when GSH (5 mM) + lipoic acid (50 μM) are included. This must be computed BEFORE experimental validation (anti-post-hoc fitting).
2. **FDX1 E₀' mutant series**: A library of FDX1 mutants spanning E₀' from −200 to −350 mV (constructed by systematic substitution at C46, C52, C55, H56) shows a sigmoidal cuproptosis sensitivity curve with inflection at E₀' = −260 ± 20 mV — matching the predicted Pourbaix boundary. Mutants with E₀' > −220 mV reduce cuproptosis sensitivity ≥50% without impairing steroidogenesis (11β-hydroxylase activity).
3. **Elesclomol-to-lipoyl transfer**: In vitro transfer of Cu from elesclomol to lipoamide reaches equilibrium Ktransfer = 0.8 ± 0.3 (near-isoenergetic), measured by competition ITC at pH 7.4, 37°C. Transfer rate is FDX1-dependent: ≥10-fold acceleration with catalytic FDX1 vs spontaneous.
4. **Vent-analog validation**: Under alkaline vent conditions (pH 10, 70°C, Eh −500 mV), the Cu²⁺/Cu⁺ boundary collapses entirely to Cu⁺ — matching the Pourbaix prediction. FDX1 ancestral homolog (from E1.3 reconstruction) retains Cu²⁺ reductase activity under these conditions.

**Test protocol**:
(1) Computational: PHREEQC ligand-extended Pourbaix using Cu-thiol stability constants (Sander & Koschinsky 2011 + NIST Critical Stability Constants). Publish prediction BEFORE experimental validation.
(2) FDX1 mutants: Site-saturation mutagenesis at Fe-S ligand positions. Express in FDX1-KO MOLM-13. Screen cuproptosis EC₅₀ + steroidogenesis activity. Plot EC₅₀ vs measured E₀' (protein film voltammetry).
(3) Transfer kinetics: ITC with elesclomol-Cu²⁺ + lipoamide ± catalytic FDX1 (10 nM). Stopped-flow UV-vis to track elesclomol release.
(4) XANES validation: Cu K-edge XANES on isolated mitochondria at controlled Eh (potentiostat in anaerobic chamber) to confirm Cu⁺/Cu²⁺ ratio matches Pourbaix prediction at −300 mV.

**Confidence**: 6 | **Groundedness**: 7

This mutation preserves H1.2's core strength (quantitative Pourbaix framework filling a genuine literature gap) while eliminating all three Critic-identified confounds. The FDX1 mutant library is the strongest test: it decouples redox potential from respiratory function, directly addressing the Critic's fatal ETC inhibitor confound. The elesclomol speciation addition is non-trivial — it explains WHY cuproptosis requires an ionophore (near-isoenergetic transfer to lipoyl targets) and WHY FDX1 is needed (kinetic acceleration of what thermodynamics already favors). The predict-THEN-measure protocol explicitly addresses post-hoc fitting concerns.

---

## Evolution Quality Check

### Diversity Assessment
| Bridge Mechanism | Hypotheses | Status |
|---|---|---|
| Cu-Fe sulfide displacement in Eh-pH space | E1.1, E1.3 | DISTINCT: E1.1 = quantitative biophysics, E1.3 = evolutionary genomics |
| CuS oligomer phase chemistry | E1.2 | UNIQUE |
| FDX1 redox potential as kinetic gate | E1.4 | UNIQUE (overlaps E1.1 in Pourbaix but core mechanism differs) |

**3 distinct bridge mechanisms survive** ✓

### Critic Question Resolution
| Critic Question | Resolved By |
|---|---|
| Which cluster type kinetically accessible first? (H1.4) | E1.1 prediction 3: CIA vs LIAS differential test |
| How to separate Eh from respiration? (H1.2) | E1.4: FDX1 E₀' mutant library replaces ETC inhibitor |
| How to avoid post-hoc fitting? (H1.2) | E1.4: Explicit predict-THEN-measure protocol |
| Cu⁺ disproportionation at pH 7? (H1.2) | E1.4: Ligand stabilization suppresses disproportionation |
| Min Cu for CuS? (H1.3) | E1.2: Reframed as sub-nanoparticle oligomers |
| Distinguish CuS from Cu-DLAT? (H1.3) | E1.2: XAS/EXAFS replaces TEM/EDX |
| Can biphasic work without nanoparticles? (H1.3) | E1.2: Yes, via oligomer buffering |
| Simpler evolutionary test? (H1.7) | E1.3: Comparative genomics replaces protocells |

### Self-Critique of Evolved Set
1. **E1.1 risk**: Ligand-extended Pourbaix with Fe-S cluster sulfide fields is unprecedented — thermodynamic databases may lack required constants. Mitigation: sensitivity analysis on missing constants.
2. **E1.2 risk**: Sub-nanoparticle CuS oligomers may be transient (picosecond lifetime) — too short to function as reservoirs. Mitigation: XAS time-resolved measurement at synchrotron.
3. **E1.3 risk**: FDX1-LIAS co-occurrence in Cu-rich environments could reflect shared Fe-S metabolism, not Cu-specific selection. Mitigation: dN/dS at Cu-specific vs general Fe-S residues.
4. **E1.4 risk**: FDX1 E₀' mutants may also alter Fe-S biogenesis, confounding the cuproptosis test. Mitigation: steroidogenesis activity as orthogonal readout.

### Improvement Assessment
| Parent | Evolved | Δ Score (estimated) | Key Improvement |
|---|---|---|---|
| H1.4 (7.90) + H1.2 (7.15) | E1.1 | +0.5–1.0 | Quantitative Pourbaix framework + mechanism-specific tests |
| H1.3 (5.80) | E1.2 | +0.5–1.0 | Physical feasibility restored, XAS methodology |
| H1.4 (7.90) + H1.7 (4.25) | E1.3 | +1.0–1.5 | Tractable genomics replaces infeasible protocells |
| H1.2 (7.15) | E1.4 | +0.5–1.0 | Three confounds eliminated, elesclomol added |
