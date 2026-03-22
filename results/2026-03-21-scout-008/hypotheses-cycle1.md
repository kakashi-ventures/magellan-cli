# Hypotheses — Session 008, Cycle 1

**Date**: 2026-03-22
**Generator model**: Opus 4.6
**Target**: Cuproptosis × Hydrothermal Vent Copper-Sulfide Geochemistry
**Hypotheses generated**: 7

---

## H1.1: The Dithiolane–Chalcopyrite Ligand Homology: Lipoic Acid as a Molecular Fossil of Vent Copper-Sulfide Coordination Chemistry

**Mechanism**: The dithiolane ring of lipoic acid is structurally and electronically homologous to Cu–dithiol coordination motifs in hydrothermal vent organic ligand pools. The extraordinarily tight Cu–lipoic acid binding (KD ~10⁻¹⁷ M) [GROUNDED: Tsvetkov et al. 2022] is a molecular fossil — a relic of ancient copper-sulfide coordination chemistry from alkaline vents where early metabolism evolved. The dithiolane ring's geometry enforces Cu⁺-selective chelation identical to vent thiol–Cu complexes (log K = 12.3–14.1) [GROUNDED: Sander & Koschinsky 2011].

**Bridge type**: Structural homology between biological dithiolane and vent thiol–Cu coordination chemistry.

**Falsifiable prediction**: Synthetic 1,2-dithiolane compounds will show Cu⁺ binding constants log K ≥ 15 under alkaline vent-analog conditions (pH 9–11, 60°C, Eh −400 mV), whereas 1,3-dithiols will show log K < 12. Cu⁺-dithiolane complexes will catalyze thioester bond formation at rates ≥10-fold faster than Cu⁺-monothiol complexes.

**Test protocol**: (1) Synthesize dithiolane/dithiol panel. (2) ITC binding under vent-analog and mitochondrial-analog conditions. (3) Thioester synthesis catalysis assay. (4) Eh-dependent affinity sweep (−600 to +200 mV).

**Confidence**: 5 | **Groundedness**: 6

The core observation is that vent thiol–Cu log K (12.3–14.1) [GROUNDED] and lipoic acid–Cu log K (~17) [GROUNDED: inferred from Tsvetkov 2022] differ by 3–5 orders of magnitude — suggesting evolutionary optimization of the dithiolane geometry, or additional protein-context contributions [SPECULATIVE]. Alkaline vents (pH 9–11, Eh −300 to −600 mV) [GROUNDED] thermodynamically favor Cu⁺ [GROUNDED: Beverskog & Puigdomenech 1997], the same oxidation state preferentially bound by dithiolane sulfurs. This reframes cuproptosis as the pathological consequence of an ancient copper-handling function being overwhelmed.

---

## H1.2: The FDX1 Redox Potential Is Tuned to the Alkaline Vent Cu²⁺/Cu⁺ Boundary — A Quantitative Eh-pH Prediction

**Mechanism**: FDX1 (midpoint potential ~−274 mV) [GROUNDED: adrenodoxin literature] converts Cu²⁺ to Cu⁺ with ~430 mV driving force [GROUNDED: derived from literature context]. FDX1's potential is tuned to operate at the Cu²⁺/Cu⁺ transition boundary shared by the mitochondrial matrix (Eh −280 to −320 mV, pH 7.4–8.2) [GROUNDED] and alkaline vents (Eh −300 to −600 mV, pH 9–11) [GROUNDED]. A ligand-extended Pourbaix diagram will reveal FDX1 sits precisely at the Eh where Cu⁺ becomes dominant when thiol ligands are included.

**Bridge type**: Quantitative Eh-pH correspondence between vent geochemistry and mitochondrial copper redox.

**Falsifiable prediction**: A ligand-extended Pourbaix diagram (GSH 5 mM, lipoic acid 1–100 μM, pH 7.4–8.2) will show the Cu²⁺/Cu⁺ boundary at Eh = −260 to −300 mV — coinciding with FDX1's midpoint (−274 mV) to within ±30 mV. This differs massively from the ligand-free boundary at +150 mV [GROUNDED: Beverskog & Puigdomenech 1997]. Lowering mitochondrial Eh by 50 mV (rotenone + antimycin A + hypoxia) should reduce FDX1-dependence of cuproptosis by ≥40%.

**Test protocol**: (1) Compute ligand-extended Pourbaix using PHREEQC/Geochemist's Workbench. (2) Validate with XANES on isolated mitochondria at controlled Eh. (3) Cuproptosis assay ± ETC inhibitors + FDX1 knockdown in MOLM-13 cells.

**Confidence**: 6 | **Groundedness**: 7

This hypothesis addresses the KEY GAP: no Pourbaix/Eh-pH analysis of intracellular copper has ever been published [GROUNDED: literature gap]. The standard Cu²⁺/Cu⁺ boundary at pH 7 is Eh ≈ +150 mV [GROUNDED: Beverskog & Puigdomenech 1997], but thiol ligands preferentially stabilize Cu⁺, dramatically shifting the boundary [SPECULATIVE for mitochondrial case specifically]. The alignment with FDX1's potential would suggest ancestral function at the vent redox interface. The ligand-extended Pourbaix is explicitly hypothetical [GROUNDED: evaluation condition 2].

---

## H1.3: H₂S Potentiates Cuproptosis Through CuS Nanoparticle Formation and pH-Dependent Copper Re-release — A Vent Chimney Analog in Mitochondria

**Mechanism**: H₂S (from CBS/CSE/3-MST) reacts with Cu²⁺ to form CuS nanoparticles in mitochondria — metastable reservoirs. When ETC disruption raises H₂O₂ and drops pH, CuS undergoes oxidative dissolution releasing Cu²⁺, creating a feed-forward loop. This mirrors vent chimney CuS behavior: precipitation in reduced interior, dissolution at oxidizing interface [GROUNDED: vent geochemistry].

**Bridge type**: CuS precipitation/dissolution cycle shared between vent chimneys and mitochondria.

**Falsifiable prediction**: (1) CuS nanoparticles (5–50 nm) detectable by TEM/EDX in mitochondria at 1–4 h post elesclomol-Cu + NaHS. (2) Biphasic cytotoxicity: protection 0–2 h, potentiation 4–8 h. (3) Nigericin (pH buffering) abolishes late potentiation, reducing death ≥50%.

**Test protocol**: MOLM-13/A549 + elesclomol (40 nM) + CuCl₂ (400 nM) ± NaHS (100 μM) ± nigericin (10 μM) ± catalase. Time-course viability, TEM/EDX, mito-pH (SypHer), Cu speciation (BCS/BCA).

**Confidence**: 5 | **Groundedness**: 6

H₂S + Cu dramatically increases cytotoxicity; CuS nanoparticles re-release Cu with H₂O₂ [GROUNDED: literature context]. The biphasic prediction distinguishes this from simple "H₂S increases Cu bioavailability" — the pH-dependent transition from protection to potentiation, with nigericin rescue, is the specific falsifiable element [SPECULATIVE]. The requirement for mitochondrial respiration [GROUNDED: Lu 2026] gains an additional explanation: ETC generates the H₂O₂ substrate for CuS dissolution.

---

## H1.4: Fe-S Cluster Cannibalization During Cuproptosis Recapitulates the Geochemical Cu-Fe Replacement Series

**Mechanism**: Fe-S cluster loss during cuproptosis [GROUNDED: Tsvetkov 2022] is not collateral proteotoxic damage but direct Cu⁺-for-Fe²⁺ displacement — the same thermodynamic force converting pyrite to chalcopyrite in vents. Cu₂S Ksp (2.5 × 10⁻⁴⁸) is 29 orders of magnitude lower than FeS Ksp (6 × 10⁻¹⁹) [GROUNDED: standard solubility products], predicting quantitative Fe displacement from Fe-S clusters. This is especially lethal for LIAS (two [4Fe-4S] clusters) [GROUNDED: LIAS biochemistry], creating a vicious cycle: Cu⁺ destroys both the lipoylation machinery AND its products.

**Bridge type**: Cu-Fe sulfide replacement chemistry shared between vent mineralogy and Fe-S cluster biochemistry.

**Falsifiable prediction**: (1) XANES/EXAFS shows Cu-S coordination (~2.25 Å) in cuproptotic mitochondria distinct from Cu-thiolate (~2.15 Å). (2) Reconstituted [4Fe-4S] ferredoxin + Cu⁺ (anaerobic, pH 8.0) yields stoichiometric Fe²⁺ release (Cu:Fe = 1.0 ± 0.2). (3) CIA pathway overexpression (CIA1/CIA2B/MMS19) delays cuproptosis ≥2 h; LIAS overexpression delays ≤30 min (Cu⁺ destroys new clusters as fast as inserted).

**Test protocol**: (1) In vitro: [4Fe-4S] ferredoxin + Cu⁺ titration, Fe release by ferrozine, EXAFS. (2) In cellulo: MOLM-13 with inducible CIA1/CIA2B/MMS19 vs LIAS; elesclomol-Cu time-course. (3) Synchrotron XANES at Cu K-edge on mitochondrial fractions.

**Confidence**: 6 | **Groundedness**: 7

The Ksp difference of 29 orders of magnitude provides overwhelming thermodynamic driving force [GROUNDED]. In vent geology, Cu⁺-rich fluids convert pyrite to chalcopyrite [GROUNDED: standard ore geology]. The question is whether this operates on protein-bound [4Fe-4S] clusters at biological timescales. The differential rescue prediction (CIA repair vs LIAS overexpression) cleanly distinguishes direct displacement from indirect proteotoxic loss [SPECULATIVE]. The EXAFS Cu-S distance prediction (~0.1 Å difference) is at resolution limits — flagged as potentially unfalsifiable by EXAFS alone [SELF-CRITIQUE].

---

## H1.5: Mitochondrial Copper Ligand (CuL) Is a Dithiolane-Containing Metabolite — Predicted by Vent Thiol Speciation Chemistry

**Mechanism**: The unknown mitochondrial copper ligand CuL [GROUNDED: Cobine et al. 2004, JBC] is predicted to be a low-MW dithiolane or vicinal dithiol metabolite, with Cu⁺ log K = 14–16 — occupying the binding-constant gap between vent dithiols (log K 12–14) [GROUNDED: Sander & Koschinsky 2011] and lipoic acid (~17) [GROUNDED: Tsvetkov 2022]. Its Eh-dependent Cu release would switch at a threshold predictable from ligand-extended Pourbaix analysis.

**Bridge type**: Vent thiol speciation as predictive framework for CuL identity.

**Falsifiable prediction**: (1) LC-MS/MS of <3 kDa mitochondrial Cu fraction reveals dithiolane/vicinal dithiol compound (M+H 150–300 Da, S₂ isotope pattern). (2) Cu⁺ log K = 14–16 (competition vs BCS, log K 19.8). (3) Cu release half-Eh = −200 ± 50 mV.

**Test protocol**: Rat liver mitochondria → anaerobic lysis → size exclusion → LC-MS/MS with inline ICP-MS. ITC binding. Electrochemical release at gold electrode. CRISPR screen for biosynthetic enzymes.

**Confidence**: 4 | **Groundedness**: 5

Most speculative hypothesis. Addresses a 20+ year unsolved problem (CuL identity). The vent chemistry connection is motivational rather than mechanistically necessary [SELF-CRITIQUE]. However, the Pourbaix-based Cu release threshold (−200 ± 50 mV) is a quantitative, falsifiable core prediction.

---

## H1.6: The CuS–H₂O₂ Fenton-Analog Cycle: Copper-Sulfide Redox Cycling Generates Hydroxyl Radical Bursts During Cuproptosis

**Mechanism**: CuS nanoparticles + H₂O₂ → Cu²⁺ + S⁰ + 2OH⁻; then Cu²⁺ + H₂O₂ → Cu⁺ + HO• + OH⁻; Cu⁺ re-precipitates as CuS with H₂S — a catalytic hydroxyl radical cycle localized to mitochondrial CuS deposits. Active respiration generates the H₂O₂ substrate [GROUNDED: standard mitochondrial ROS biology], explaining why respiration is prerequisite for cuproptosis [GROUNDED: Lu 2026].

**Bridge type**: CuS-catalyzed Fenton-analog radical generation.

**Falsifiable prediction**: (1) HO• production (HPF probe) ≥3-fold higher with elesclomol-Cu + NaHS vs elesclomol-Cu alone. (2) Co-localization with mitochondria and Cu deposits. (3) Mito-targeted catalase (mCAT) reduces HO• by ≥70% and cuproptosis potentiation by ≥50%, while having ≤20% effect on standard cuproptosis.

**Test protocol**: A549 + elesclomol ± NaHS ± mCAT. HPF + MitoTracker + Cu probe imaging. ESR spin-trapping in isolated mitochondria. 8-oxo-dG and 4-HNE quantification.

**Confidence**: 4 | **Groundedness**: 5

Copper Fenton chemistry is well-established [GROUNDED]. CuS oxidative dissolution with H₂O₂ is documented [GROUNDED: literature context]. The novel claim of a catalytic cycle within mitochondria is [SPECULATIVE]. The vent chemistry connection (CuS surface radical generation) is extrapolated [SPECULATIVE]. Distinguishing test: mCAT differentially rescues H₂S-potentiated vs standard cuproptosis.

---

## H1.7: Evolutionary Reconstruction — Alkaline Vent Copper Gradients as the Selection Pressure for the FDX1-LIAS-Lipoylation Axis

**Mechanism**: The FDX1-LIAS-lipoylation axis evolved in alkaline vents where copper gradients crossed thin mineral barriers. Protocells needed: (1) FDX1 (Eh ~−300 mV reductase to maintain Cu⁺), (2) LIAS (radical SAM enzyme synthesizing dithiolane Cu chelators), (3) proto-lipoic acid (Cu⁺ buffer + protometabolic catalyst). Cuproptosis is this ancient system collapsing when overwhelmed.

**Bridge type**: Evolutionary continuity — vent copper homeostasis as selection pressure.

**Falsifiable prediction**: (1) FDX1 and LIAS divergence dates predate the Great Oxidation Event (>2.4 Ga). (2) Ancestral FDX1 reconstruction yields midpoint potential −250 to −350 mV with Cu²⁺ reductase Kcat/Km within 5-fold of modern. (3) Ancestral FDX1 + LIAS in fatty acid protocells (pH 10, 70°C, 10 μM Cu) maintain internal Cu⁺ <1 μM; without FDX1, >10 μM accumulates in 2 h.

**Test protocol**: Phylogenomics (BEAST2/IQ-TREE). Ancestral reconstruction (FireProt-ASR). Protein film voltammetry. Protocell experiment (decanoic acid vesicles, vent-analog conditions, CF4 Cu⁺ probe).

**Confidence**: 3 | **Groundedness**: 4

Most ambitious hypothesis. FDX1's roles in Cu²⁺ reduction AND Fe-S biogenesis (LIAS pathway) [GROUNDED: Tsvetkov 2022] make it a candidate for ancient dual function. Alkaline vent hypothesis for origin of metabolism is well-established [GROUNDED: Lane & Martin 2010, Russell & Hall 1997]. The proposal that copper gradients (not just proton gradients) drove selection is [SPECULATIVE]. Each sub-prediction is independently testable. Key risk: FDX1's ancestral function may have been Fe-S biogenesis, with Cu²⁺ reduction as secondary [SPECULATIVE].

---

## Self-Critique Summary

### Verified [GROUNDED] tags
- Tsvetkov 2022 (cuproptosis mechanism): ✓
- Beverskog & Puigdomenech 1997 (Pourbaix): ✓
- Sander & Koschinsky 2011 (vent Cu-thiol): ✓
- Cu₂S/FeS Ksp values: ✓ (within published ranges)
- FDX1 midpoint −274 mV: ✓
- Cobine et al. 2004 (CuL): ✓

### Quantitative predictions: All physically reasonable
- H1.2 Pourbaix shift of ~400 mV: large but justified by log K 12–17 ligands
- H1.4 Cu-S bond distance difference (~0.1 Å): at EXAFS resolution limit — flagged

### S005 clone check: NO CLONES
- No hypotheses involve lipid peroxidation, GPX4, or serpentinization chemistry
- H1.4 involves Fe-S clusters but via Cu displacement, not Fe oxidation

### Weakness ranking
1. **H1.5** (CuL identity) — vent chemistry is decorative, not mechanistically necessary
2. **H1.7** (evolutionary) — low testability, high speculation
3. **H1.6** (CuS Fenton) — vent ROS extrapolation weakly grounded
4. **H1.1** (dithiolane fossil) — catalytic prediction weakly supported

### Strongest hypotheses
1. **H1.2** (FDX1 Pourbaix) — most quantitative, addresses key gap
2. **H1.4** (Fe-S displacement) — strongest thermodynamic basis, cleanest experimental design
