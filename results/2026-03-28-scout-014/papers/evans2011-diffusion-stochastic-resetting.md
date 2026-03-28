# Diffusion with Stochastic Resetting

**Authors:** Martin R. Evans, Satya N. Majumdar
**Year:** 2011
**Journal:** Physical Review Letters, Vol. 106, Article 160601
**DOI:** 10.1103/PhysRevLett.106.160601
**arXiv:** 1102.2704

## Abstract Summary
Foundational paper establishing stochastic resetting as a framework for optimizing diffusive search. A particle diffuses and resets to its initial position at constant rate r. Key result: mean first passage time to a target is minimized at an optimal resetting rate r*.

## Key Findings

**Non-equilibrium stationary state:** Finite resetting rate r → non-equilibrium stationary state with non-Gaussian position fluctuations.

**Optimal resetting rate r*:** Mean first passage time to a stationary target has a minimum at r* — the fundamental result exploited in all downstream applications.

**Multi-searcher survival:** With multiple searchers, typical survival probability decays exponentially, average decays as power law (density-dependent exponent) — distinction between typical/average absent in standard diffusion.

**Mathematical framework:** Renewal process formalism for computing mean first passage times with resetting. Renewal equation: MFPT(r) = [1 - e^(-r·T₀)]/(r·e^(-r·T₀)) where T₀ = resetting-free MFPT.

## Relevance to MAGELLAN Pipeline
- Anchor theory paper for Candidate 5 (Resetting × Persister)
- Bridge concept: dosing event = resetting event; bacterial population state = particle position; extinction = target
- Critical gap: Evans & Majumdar framework has NEVER been applied to antibiotic dosing or persister bacteria
- The optimal r* formula maps directly onto optimal dosing interval concept
