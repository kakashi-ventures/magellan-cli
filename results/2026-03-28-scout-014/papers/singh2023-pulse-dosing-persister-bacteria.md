# Systematic Design of Pulse Dosing to Eradicate Persister Bacteria

**Authors:** Garima Singh, Mehmet A. Orman, Jacinta C. Conrad, Michael Nikolaou
**Year:** 2023
**Journal:** PLOS Computational Biology
**DOI:** 10.1371/journal.pcbi.1010243
**PMC:** 9882918

## Abstract Summary
Develops a systematic methodology for designing optimal periodic antibiotic pulse dosing to eliminate persister bacteria. Uses two-state ODE model (normal + persister populations) and derives critical on/off duration ratios for eradication.

## Key Findings

**Critical ratio:** Bacterial eradication requires (t_off/t_on) < critical value (≈2.8 for their experimental system).

**Optimal ratio:** (t_off/t_on)_opt ≈ √(Rₚ/Rₙ) maximizes peak-to-peak decline rate.

**Mathematical framework:** Two-state differential equations with matrix exponential analysis of successive bacterial population peaks — eigenvalue analysis of the transition matrix.

**NOT stochastic resetting:** The framework is deterministic population dynamics. No use of Evans-Majumdar stochastic resetting theory, renewal processes, or first-passage analysis under resetting.

**Key gap:** The optimal resetting rate r* from Evans-Majumdar gives a clean analytical solution for the optimal dosing interval from first principles — this deterministic model lacks that principled derivation.

## Relevance to MAGELLAN Pipeline
- Field C anchor paper for Candidate 5 (Resetting × Persister)
- Confirms pulse dosing IS effective and that an optimal ratio exists (consistent with r* prediction)
- The mathematical gap: Singh et al. solve the problem deterministically with ad hoc ODEs; resetting framework would derive the optimum from first principles with a cleaner, universal formula
- Establishes: literature knows optimal pulse dosing works, but does NOT use resetting formalism
