# Statistical Models for Earthquake Occurrences and Residual Analysis for Point Processes (ETAS Original)

**Authors:** Yosihiko Ogata
**Year:** 1988
**Journal:** Journal of the American Statistical Association, 83(401): 9-27
**DOI:** 10.2307/2288914

## Abstract Summary
Introduces the Epidemic Type Aftershock Sequence (ETAS) model — a branching Hawkes process for earthquake temporal clustering. Each earthquake triggers aftershocks according to a modified Omori law, and each aftershock triggers further aftershocks in cascade.

## Key Findings

**Conditional intensity function:**
λ(t) = μ + Σᵢ K₀·exp(α(Mᵢ - Mc)) / (t - tᵢ + c)^p
where μ = background rate, K₀ = aftershock productivity, α = magnitude scaling, Omori exponent p ≈ 1.

**Branching ratio n:** Average daughters per event = Σ direct aftershocks per mainshock.
- n < 1: subcritical (sequence dies out) = "dormant" analog
- n > 1: supercritical (explosive growth) = "recurrence" analog
- n ≈ 1: near-critical (long-lived, power-law distributed sequence lengths)

**Omori law:** Rate of aftershocks decays as ~(t+c)^{-p} — power law in time.

**Space-time extension:** Ogata (1998) added spatial spread.

## Relevance to MAGELLAN Pipeline
- Field A anchor paper for Candidate 4 (ETAS × Dormancy)
- Bridge concept: tumor microenvironment paracrine signaling as conditional intensity λ(t) — each awakened tumor cell emits growth factors that trigger neighbors (aftershocks)
- n < 1 (subcritical ETAS) = dormancy; n > 1 (supercritical) = recurrence/metastatic growth
- Omori law analog: paracrine signal decay after each "recurrence event"
