# Evolution Report — Session 008, Cycle 1→2

**Date**: 2026-03-22
**Evolver model**: Sonnet 4.6
**Input**: 6 surviving hypotheses | **Output**: 6 evolved hypotheses | **Dropped**: H1.6, H1.7

## Evolved Hypotheses

| ID | Parent | Operation | Improvement | Bridge Type |
|---|---|---|---|---|
| **H2.1** | H1.4 | Specification | 8/10 | Kinetic accessibility gradient (CIA vs ISC) |
| **H2.2** | H1.2 | Mutation | 9/10 | Thermodynamic framework (ligand-extended Pourbaix + ΔΨm) |
| **H2.3** | H1.3 | Pruning+Spec | 7/10 | Mass-balance geochemical (CuS oligomers) |
| **H2.4** | H1.1 | Mutation+Spec | 8/10 | Enzymatic competitive inhibition (Cu⁺-dithiolane LIAS trap) |
| **H2.5** | H1.4×H1.2 | Crossover | 7/10 | Two-hit mechanistic architecture |
| **H2.6** | H1.3 | Generalization | 6/10 | Scavenging budget + tissue vulnerability map |

## H2.1: CIA vs ISC Cu-Accessibility Gating (from H1.4 via SPECIFICATION)
CIA-assembled cytoplasmic clusters attacked before ISC/LIAS mitochondrial clusters. Pyrite→chalcopyrite surface-in replacement parallel. Test: native gel ABCE1 loss precedes DLAT lipoylation decrease by 30-60 min.

## H2.2: Ligand-Extended Pourbaix with Decoupled Eh (from H1.2 via MUTATION)
Eliminates both Critic flaws: uses ΔΨm (JC-1/TMRM) instead of rotenone; repositions to elesclomol-Cu²⁺ speciation (log K ~8-9, Cen 2021) not free Cu. Predicts ΔΨm threshold ~−150 mV for cuproptosis commitment. Oligomycin (hyperpolarizes) should delay cuproptosis.

## H2.3: CSE-H₂S Modulates Cuproptosis via CuS Oligomers (from H1.3 via PRUNING)
Drops infeasible nanoparticles → CuS oligomers (binuclear/tetranuclear, n=2-8). Mass-balance valid: 3×10⁴ Cu atoms → ~10⁴ (CuS)₂ dimers. Detectable by Raman (Cu-S stretch 270 cm⁻¹). Biphasic NaHS curve: 50 μM accelerates, 500 μM protects.

## H2.4: Dithiolane as Kinetic Trap During LIAS Catalysis (from H1.1 via MUTATION)
Drops unfalsifiable "molecular fossil." Cu⁺ competes for nascent dithiolane during LIAS S-insertion (log K ~16.1, Smirnova 2018). Second pathway to lipoylation failure independent of cluster destruction. Test: aconitase stays high while DLAT lipoylation drops in early cuproptosis.

## H2.5: Two-Hit Cuproptosis Model (CROSSOVER H1.4 × H1.2)
Hit 1: ΔΨm threshold for FDX1-mediated Cu²⁺→Cu⁺. Hit 2: Cu⁺ attacks CIA clusters first, then ISC/LIAS. Two-hit model predicts irreversibility threshold and time-ordered cascade.

## H2.6: CBS/CSE H₂S as Tissue Cuproptosis Rheostat (from H1.3 via GENERALIZATION)
CBS/CSE expression sets tissue cuproptosis sensitivity via H₂S-Cu buffering. Neurons (low CBS/CSE) 5-10× more sensitive than hepatocytes. CBS polymorphisms predict Wilson's disease severity.

## Diversity Check: 6 DISTINCT bridge types ✓
## Dropped: H1.6 (self-terminating loop), H1.7 (near-trivially true, infeasible test)
