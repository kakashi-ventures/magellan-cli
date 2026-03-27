# Structural and Mathematical Analysis — Extreme Value Statistics × Protein Thermal Stability

You are asked to analyze three hypotheses that apply mathematical frameworks from extreme value statistics to protein thermal stability biology. Your role is to find and formally verify the mathematical structures underlying each hypothesis, assess whether the proposed connections are formal isomorphisms, structural analogies, or merely surface analogies, and computationally verify the key mathematical claims.

You have **code execution** and **web search** tools. Use code execution to verify mathematical claims — do not just describe formal mappings, compute them.

It is currently 2026. Use recent mathematical and physical frameworks when relevant.

---

## Behavioral Constraints

- Classify every connection as: **Formal identity** / **Structural analogy** / **Metaphorical similarity**
- Only formal identities and structural analogies are scientifically productive; flag metaphorical similarities as such
- For every proposed formal mapping, write and run Python code to verify:
  - Dimensional consistency of equations
  - Numerical predictions (plug in stated values, confirm outputs match claims)
  - Whether mathematical relationships hold for simple test cases
  - Order-of-magnitude plausibility of quantitative predictions
- Report discrepancies between stated and computed values
- Only assert formal mappings you can explicitly write down and verify

---

## Background on the Two Domains

**Extreme Value Theory (EVT)**: A branch of probability theory governing the behavior of sample maxima and minima. Foundational result — the Fisher-Tippett-Gnedenko theorem (1928/1943): if properly normalized block maxima of a sequence converge to a limit distribution, that limit must be a Generalized Extreme Value (GEV) distribution with CDF:

```
G(x; μ, σ, ξ) = exp{-[1 + ξ((x-μ)/σ)]^(-1/ξ)}
```

where:
- μ = location (shifts the distribution)
- σ > 0 = scale (spreads the distribution)
- ξ = shape (tail index):
  - ξ < 0: Weibull domain — bounded tail, finite endpoint
  - ξ = 0: Gumbel domain — exponential tail (take limit as ξ → 0)
  - ξ > 0: Fréchet domain — heavy polynomial tail

For the Peaks-over-Threshold approach, exceedances above threshold u follow a Generalized Pareto Distribution (GPD):

```
H(y; σ, ξ) = 1 - (1 + ξy/σ)^(-1/ξ),  y > 0
```

Return levels: the p-return level is the value exceeded with probability p. For GEV:
```
x_p = μ - (σ/ξ)[1 - (-log(1-p))^(-ξ)]
```

**Protein Thermal Stability (Meltome Atlas)**: Thermal Proteome Profiling (TPP) measures protein melting temperatures (Tm) across the proteome. The Meltome Atlas (Jarzab et al. 2020, Nature Methods) measured ~48,000 proteins across 13 species, covering Tm ≈ 30–90°C. Protein complexes (multi-subunit assemblies) show correlated melting (Thermal Proximity Co-aggregation, r = 0.75–0.83 within complexes; Tan et al. 2018, Science). Optimal growth temperature (OGT) varies from ~4°C (psychrophiles) to ~80°C (thermophiles) across the 13 species.

---

## HYPOTHESIS 1: GEV Shape Parameter Encodes Thermal Adaptation Strategy

### Formal Statement

For each species s, define the block-minimum Tm: sort proteins into ~300 KEGG pathway blocks, take the minimum Tm per block, yielding a sample of ~300 block minima. Fit the GEV distribution to the negated block minima (converting minima to maxima for standard GEV fitting). Extract ξ_s (the shape parameter). The hypothesis predicts:

**ξ_s is negatively correlated with OGT_s across the 13 Meltome Atlas species** (thermophiles: more negative ξ; psychrophiles: ξ closer to 0).

Proposed mechanistic interpretation:
- Thermophiles eliminated low-Tm proteins (tail truncation) → distribution has a harder lower bound → more negative ξ
- Psychrophiles shifted the whole distribution leftward without truncating the tail → relative tail shape preserved → ξ ≈ 0

### Mathematical Questions to Investigate

1. **FTG applicability**: The FTG theorem guarantees GEV convergence as block size → ∞. For blocks of ~15–30 proteins per KEGG pathway, is convergence sufficient? Compute the rate of convergence of block minima to the GEV for a distribution similar to the expected protein Tm distribution (approximately normal with μ ≈ 52°C, σ ≈ 10°C). How many blocks are needed before ξ estimates become reliable?

2. **SE(ξ) verification**: The hypothesis claims SE(ξ) ≈ 0.029 at n = 5,000–7,000 observations. Verify this claim using Fisher information theory for GEV MLE, or simulate: generate 5,000 samples from a GEV(μ=50, σ=8, ξ=-0.2), fit GEV 1,000 times, report SE(ξ). Does 0.029 match?

3. **Effect size plausibility**: The predicted ξ difference between thermophiles and psychrophiles is 0.3–0.5. Is this large relative to SE(ξ) ≈ 0.029? What power does a 13-species regression have to detect a correlation if the true effect maps to ξ differences of 0.3–0.5 over a 4–80°C OGT range?

4. **Tail truncation formal mapping**:
   - In EVT: a distribution with a hard lower bound b has ξ < 0 in the GEV for its minima; a distribution without a hard lower bound has ξ ≥ 0.
   - In biology: thermophile tail truncation means the distribution has a higher minimum Tm floor.
   - Is this a **formal identity** (the mathematical definition of bounded support maps exactly onto the biological truncation), or a **structural analogy** (same qualitative behavior, different generative mechanism)?

---

## HYPOTHESIS 2: Return Levels of Complex-Minimum Tm Predict Process Thermal Failure

### Formal Statement

For a cellular process P consisting of N_P protein complexes, define Tm_min,i as the minimum melting temperature among essential subunits of complex i. Fit a GPD to the lower tail of {Tm_min,i}: let the threshold u = 45°C. The p-return level R_p gives the temperature at which proportion p of the complexes have Tm_min below R_p. The hypothesis maps:

**R_p ↔ temperature at which fraction p of process P fails**

Specifically: R_{0.01} for ribosomal complexes should equal the temperature at which 90% of translation capacity is lost (measurable as puromycin incorporation drop).

Return level formula (GPD-based):
```
R_p = u + (σ/ξ)[(p/ζ_u)^(-ξ) - 1]
```
where ζ_u = P(X > u) is the fraction of complexes exceeding the threshold.

### Mathematical Questions to Investigate

1. **Formal mapping verification**:
   - In hydrology: return level R_p = flood level exceeded once in 1/p years on average
   - In this hypothesis: R_p = temperature at which fraction p of complexes have failed
   - Is this a **formal identity** (same mathematical structure), **structural analogy** (same formula, different interpretation), or something weaker?
   - Key difference to investigate: in hydrology, return levels extrapolate *above* the observed data (rare large floods). Here, R_{0.01} extrapolates into the bulk of the distribution (most complexes fail well before this temperature). Does this invert the usual interpretation?

2. **Numerical verification**:
   Using plausible parameter values for human ribosomal complex Tm distribution:
   - Suppose ribosomal complex-minimum Tm values have median ≈ 48°C, with ~15% of complexes having Tm_min < 45°C
   - Fit GPD parameters (σ ≈ 4°C, ξ ≈ -0.3 as an estimate)
   - Compute R_p for p = 0.01, 0.05, 0.10, 0.50
   - Are the resulting temperatures biologically plausible (near the 42–55°C range where heat stress effects are documented)?
   - Run this calculation in Python and report the values.

3. **Confidence interval propagation**:
   What are typical confidence intervals on return levels for small samples (n ≈ 50–200 complexes per pathway)? Compute profile likelihood confidence intervals for R_{0.01} with sample size n = 100. Is the ±2°C precision claim achievable?

4. **Bottleneck assumption formalization**:
   The hypothesis treats the minimum-Tm subunit as the thermal bottleneck. In engineering reliability theory, this is a series system: system fails when ANY component fails. The formal model is:
   ```
   P(complex fails at T) = 1 - P(all subunits survive at T) = 1 - Π_i P(subunit i survives at T)
   ```
   Is the "minimum-Tm subunit as bottleneck" assumption equivalent to assuming binary (all-or-nothing) subunit failure at Tm? Or does it assume a specific survival function shape? Formalize this assumption and assess its validity.

---

## HYPOTHESIS 3: GPD Scale Parameter Predicts Evolutionary Constraint

### Formal Statement

For each species s, fit a GPD to the lower 5th percentile of Tm (proteins with the lowest melting temperatures — the "thermally vulnerable subproteome"). Extract σ_s (the scale parameter, which measures the spread of temperatures in the vulnerable tail). For the corresponding set of tail proteins, compute mean dN/dS from ortholog alignments across the 13 species. The hypothesis predicts:

**σ_s is negatively correlated with mean(dN/dS_s)**

Proposed mechanism: narrow σ (tight vulnerability cluster) → strong purifying selection on individual amino acid changes → low dN/dS. Wide σ (spread vulnerability zone) → tolerance for Tm-reducing mutations → higher dN/dS.

### Mathematical Questions to Investigate

1. **Formal mapping between σ and selection pressure**:
   - In EVT: σ of the GPD measures the scale (spread) of the exceedance distribution.
   - In molecular evolution: purifying selection is proportional to fitness effect of a mutation; selection coefficient s ∝ ΔTm / tolerance_range.
   - Can σ be formally mapped to the width of the neutral zone in molecular evolution theory? Specifically, if tolerance range ∝ σ, and under Kimura's neutral theory the fixation probability of a slightly deleterious mutation scales with 1/(2Ns), does the mapping hold quantitatively?
   - Classify: **formal identity** / **structural analogy** / **metaphorical similarity**

2. **GPD scale parameter estimation precision**:
   Simulate the statistical precision of σ estimates. Generate 200 samples from GPD(σ=5, ξ=-0.2), fit GPD 1,000 times. What is SE(σ̂)? At n = 5th-percentile proteins per species (~250–500 proteins from ~5,000–7,000 measured), is σ estimated precisely enough to detect cross-species variation?

3. **Orthogonality to Leuenberger 2017**:
   Leuenberger et al. 2017 (Science 355:eaai7825) showed that protein size is the primary predictor of Tm (larger proteins are less stable). If large proteins are overrepresented in the thermally vulnerable tail, σ may reflect protein size distribution variation across species rather than evolutionary constraint. Formally: if Tm ≈ a - b·ln(MW) + ε, then the GPD applied to Tm exceedances is mathematically equivalent to a GPD applied to ln(MW) exceedances with different scale. In this case, σ is a proxy for protein size distribution spread. Assess whether this confound is sufficient to make the σ-dN/dS correlation spurious.

4. **Cross-species ortholog requirement**:
   For the σ-dN/dS correlation to be meaningful, the thermally vulnerable proteins (GPD exceedances) should be roughly the same genes across species. If different genes fall in the tail in different species, dN/dS of "tail protein orthologs" compares different gene sets. Compute: if thermally vulnerable identity is partly conserved across species (say 60% overlap between any two species), does the correlation test still have the correct interpretation? What is the statistical implication?

---

## Cross-Hypothesis Mathematical Analysis

After analyzing each hypothesis individually, address:

1. **Unified EVT framework**: All three hypotheses apply different EVT tools (GEV shape ξ, GPD return levels, GPD scale σ) to the same underlying dataset. Do these three analyses extract orthogonal information about the Tm distribution, or are they correlated measurements of the same biological quantity?
   - Specifically: for a GEV(μ, σ_GEV, ξ) distribution, what is the mathematical relationship between ξ, the GPD scale σ_GPD of lower-tail exceedances, and the return levels R_p?
   - Write code to demonstrate this relationship numerically.

2. **Domain-of-attraction question**: The FTG theorem guarantees that if Tm has a finite lower bound (which it does, biologically), block minima fall in the Weibull domain (ξ < 0). Does this mean Hypothesis 1's prediction (ξ < 0 for thermophiles) is mathematically guaranteed by the theorem rather than being an empirical finding? If so, the biologically meaningful prediction is the DEGREE of negativity of ξ (how negative), not the sign. Clarify whether the hypothesis is testing the sign or the magnitude of ξ.

3. **Structural correspondence depth**: For each hypothesis, output the formal connection classification and depth rating:
   - Hypothesis 1: EVT tail classification ↔ evolutionary strategy classification
   - Hypothesis 2: Hydrology return levels ↔ process failure temperatures
   - Hypothesis 3: GPD scale ↔ evolutionary constraint
   Which connection is the deepest (most formal), and which is most at risk of being metaphorical?

---

## Output Format

For each hypothesis, produce:

```
STRUCTURAL CONNECTION
═════════════════════
Title: [descriptive title]
Fields: Extreme Value Statistics ←→ Proteome Thermal Stability

Mathematical bridge: [specific theorem/formula/structure]

FORMAL MAPPING
──────────────
In EVT: [mathematical description of the EVT quantity]
In proteome biology: [mathematical description of the biological quantity]
Mapping type: [formal identity / structural analogy / metaphorical similarity]
Mapping depth: [Formal isomorphism / Structural correspondence / Surface analogy]

PREDICTION
──────────
If valid, this predicts: [specific, testable, quantitative prediction]

VERIFICATION APPROACH
─────────────────────
1. [how to check if mapping holds]
2. [computational or experimental test]

COMPUTATIONAL CHECK
───────────────────
[Code output verifying the formal mapping — include the code and its output]

CONFIDENCE: [1-10]
DEPTH: [Surface analogy / Structural correspondence / Formal isomorphism]
```

After all three, write a **Comparative Summary** ranking the three hypotheses by mathematical depth and identifying the most fruitful direction for further analysis.
