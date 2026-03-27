# Cross-Model Validation Consensus — Session 2026-03-27-scout-013

**Target domain**: Extreme Value Theory x Proteome Thermal Stability
**Hypotheses validated**: C1-H1 (PASS, 8.45), C1-H2 (CONDITIONAL_PASS, 8.15), C1-H7 (CONDITIONAL_PASS, 7.00)

---

## Methodology

**GPT-5.4** (reasoning: high, web search: 25 searches, code interpreter: 13 executions, 42 web citations, 604s):
Empirical validation — web-grounded novelty verification against 2024-2026 literature, arithmetic verification via Python, citation verification, mechanism plausibility against experimental data, counter-evidence from recent psychrophile and heat shock studies, experimental design review.

**Gemini 3.1 Pro** (thinking: HIGH, code execution: 15 blocks across multiple attempts):
Structural analysis — computational verification of mathematical mappings, formal classification of each connection (formal identity / structural analogy / metaphorical similarity), numerical verification of all quantitative claims, cross-hypothesis mathematical consistency analysis.

---

## Per-Hypothesis Consensus

---

### C1-H1: GEV Shape Parameter as a Cross-Species Phylogenomic Signature

| Dimension | GPT-5.4 | Gemini 3.1 Pro | Consensus |
|-----------|---------|----------------|-----------|
| Novelty | PARTIALLY EXPLORED | Structurally novel application | Agree — novel EVT framing, biological question exists |
| Confidence | 4/10 | 7/10 | Diverge significantly — see below |
| Mechanism | Plausible but indirect; composition confounds | Structural analogy (deep mapping) | Partial agreement — both see confounds |
| Testability | MEDIUM — atlas too small | Structurally feasible | Moderate — limited by n=13 species |
| SE(xi) claim | Over-stated for n=5000-7000; ~300 blocks gives SE≈0.034-0.044 | Confirmed: SE≈0.036 at n=300 (not 0.029) | Converge: claim is inconsistent by ~3x |

**Agreement areas**: Both models independently confirmed that the SE(xi) ≈ 0.029 claim is numerically inconsistent. The value applies to ~300 block minima, not 5,000-7,000 observations. GPT simulation gives SE 0.034-0.044 at n=300; Gemini simulation gives SE 0.036 at n=300. Both also confirm the EVT framing (GEV/FTG) is sound as a mathematical framework and that no prior paper applies GEV shape parameters to proteome Tm distributions.

**Divergence areas**: GPT scores this 4/10, primarily concerned with the n=13 species limitation, phylogenetic confounding, and 2025 literature showing psychrophile distributions have complex altered tail shapes (not simple left-shifts). Gemini scores this 7/10, placing more weight on the formal mathematical rigor of the FTG theorem application and treating the ~10-sigma effect size as providing high statistical power at the block level. GPT's concern about proteome composition confounds (disorder content, membrane fraction, organelle composition) is not directly addressed by Gemini's mathematical analysis.

**Additional GPT finding**: A 2025 psychrophile study (*Pseudoalteromonas arctica* vs *E. coli*) found that the psychrophile proteome has a long right tail extending to 351K, inconsistent with the "cold adaptation = distribution shift with similar tail shape" story the hypothesis assumes. The Meltome Atlas includes only one archaeon, limiting thermophile representation.

**Additional Gemini finding**: The FTG theorem guarantees xi < 0 (Weibull domain) for any distribution with a finite lower bound — meaning ALL species' proteomes will have negative xi, since Tm is physically bounded below. The biologically informative signal is the *magnitude* of xi, not its sign. The hypothesis should be reframed accordingly.

**Combined recommendation**: PROMISING — pursue with corrections. The core mathematical framework is sound and genuinely novel. The SE calculation requires correction (n=300 blocks, SE≈0.035). The hypothesis must be reframed to test *magnitude* of xi (not sign) and must control for proteome composition. Current power is borderline (requires |r| > 0.55 with n=13) but the expected effect may be detectable.

---

### C1-H2: Complex-Minimum Tm Return Levels Predict Pathway-Specific Thermal Failure

| Dimension | GPT-5.4 | Gemini 3.1 Pro | Consensus |
|-----------|---------|----------------|-----------|
| Novelty | PARTIALLY EXPLORED — complex bottleneck work exists, EVT return-level framing is novel | Novel application | Agree — EVT framing novel, substrate partially anticipated |
| Confidence | 5/10 | 2/10 | Diverge sharply |
| Citation: Tan 2018 | Verified (>350 complexes, coordinates thermal behavior) | Not directly assessed | Verified |
| Citation: Lim 2023 NatComm | Discrepancy: first author is Sun, not Lim (Lim is coauthor) | Not assessed | New citation issue found by GPT |
| Formula correctness | Identified lower-tail orientation issue; provided correct formula (u - y_p) | Fatal sign inversion: formula extrapolates into upper tail; correct lower-tail value is 37.58°C not 52.42°C | Strong convergence on mathematical error |
| ±2°C precision claim | No literature basis found | CI spans ~9°C at n=100, invalidates ±2°C | Converge: claim is unsupported |
| Mechanism strength | Process failure often regulatory, not structural bottleneck | Binary bottleneck assumption too strong | Converge |

**Agreement areas**: Both models independently identify a mathematical directionality problem with the return level formula as applied to the lower tail. GPT provides the corrected formula (x_p = u - σ/ξ * [(p/q)^(-ξ) - 1]) and computes the 1% return level as ~39.46°C. Gemini provides the same correction and computes 37.58°C (using slightly different parameters: σ=4, ξ=-0.3 vs GPT's σ=3, ξ=-0.2). Both agree the ±2°C precision claim is not supported — Gemini shows the 95% CI for R_0.01 at n=100 spans ~9°C.

**Divergence areas**: GPT's higher confidence (5/10 vs Gemini's 2/10) reflects that GPT views the mathematical error as correctable and is more optimistic about the biological concept. Gemini treats the formula inversion as a "fatal flaw" and is concerned that EVT fitted on the 15% lower tail cannot validly extrapolate to the 99% bulk failure point. GPT additionally found that pathway failure is often regulatory (stress response at 42°C in neurons/HEK293) rather than driven by structural denaturation of annotated complex subunits.

**Additional GPT finding**: The Sun et al. 2023 NatComm TPCA paper (first author Sun, not Lim as cited in hypothesis) is a real citation error beyond the Mateus/Tan issue already flagged. GPT also found that mitochondrial translation factor Tufm is exceptionally heat-sensitive — a "special vulnerable regulator" mechanism that breaks the minimum-subunit bottleneck model.

**Additional Gemini finding**: Computed proof that the system-level survival model requires a binary (step-function) denaturation assumption, which is biologically unrealistic. Also demonstrated mathematically that the three EVT parameters (xi, R_p, sigma) are functionally dependent — changing xi for H1 forces changes in both return levels (H2) and GPD scale (H3).

**Combined recommendation**: NEEDS WORK — reframeable. The core idea (complex bottleneck EVT analysis) is real and novel. The formula orientation must be corrected. The ±2°C precision claim should be removed pending experimental data. The biological mechanism needs grounding in essential-subunit data rather than full CORUM membership. Pathway-specific POT may be underpowered (few complexes per pathway); whole-proteome complex analysis is better powered. GPT rates as more tractable than Gemini; the truth is between 2/10 and 5/10 (3-4/10 after corrections).

---

### C1-H7: GPD Scale Parameter Predicts Evolutionary Rate in the Thermally Vulnerable Subproteome

| Dimension | GPT-5.4 | Gemini 3.1 Pro | Consensus |
|-----------|---------|----------------|-----------|
| Novelty | PARTIALLY EXPLORED — new summary statistic for known biology | New application but metaphorical | Agree — not genuinely novel at mechanism level |
| Confidence | 2/10 | 4/10 | Diverge somewhat |
| Citation: Drummond 2005 | Verified as PNAS (not Cell) — correction confirmed | Not directly assessed | Correction confirmed |
| Mechanism | Too indirect; sigma is mixture property of species' vulnerable proteins | Metaphorical similarity; sigma = b * sigma_ln(MW) (Leuenberger confound proven mathematically) | Strong convergence: confound is severe |
| Power | n=13 severely underpowered; requires |r|>0.55 for p<0.05, |r|>0.75 for 80% power with covariates | Not explicitly computed | GPT computation governs |
| dN/dS framing | Incorrect to call dN/dS "evolutionary rate" (it is a constraint proxy) | Metaphorical bridge from EVT variance to Kimura neutral theory | Both flag conceptual issues |

**Agreement areas**: Both models converge that the protein-size confound (Leuenberger et al. 2017) is severe. Gemini proved mathematically that sigma_Tm = b * sigma_ln(MW) — the GPD scale parameter for Tm is algebraically equivalent to the scale of the protein size distribution. GPT independently flags expression level and abundance as dominant confounders that are already known to correlate with both stability and evolutionary rate. Both agree the link between stability and evolutionary constraint is real but already established, making this a new summary statistic rather than a new mechanism.

**Divergence areas**: GPT scores this 2/10 and recommends abandoning the 13-species species-level correlation entirely, suggesting a reframe to larger ortholog-group or within-species analysis using predicted Tm at scale. Gemini at 4/10 sees the structural skeleton as preserved if size and expression confounds are controlled. GPT also flags the conceptual misuse of dN/dS as "evolutionary rate" rather than as a constraint proxy.

**Additional GPT finding**: Computed that with n=13 and four covariates (sigma, expression, size, disorder), the required partial correlation rises to |r| > 0.75 for 80% power — this is an extremely high bar for a noisy comparative genomics question. Also identified a gene-identity mismatch problem: the thermally vulnerable subproteome likely differs across species, making species-level sigma-dN/dS comparison unstable.

**Additional Gemini finding**: Proved algebraically that sigma_Tm = b * sigma_ln(MW) using GPD affine transformation properties (ratio confirmed as exactly 2.000 in simulation). This is the strongest single finding for this hypothesis: the confound is not merely correlational but mathematically exact under the Leuenberger linear model.

**Combined recommendation**: UNLIKELY in current form. The protein-size confound is mathematically exact, not just correlational. At n=13, the design is severely underpowered. The hypothesis needs either: (a) a direct partial correlation analysis controlling for protein size and expression at the protein level within species, rather than at the species level, or (b) a redesign using hundreds of genomes with predicted Tm values. The current design should not be pursued without fundamental restructuring.

---

## Summary

### Confidence Adjustment Summary

| Hypothesis | QG Confidence | GPT Confidence | Gemini Confidence | Adjusted Estimate |
|------------|--------------|----------------|-------------------|-------------------|
| C1-H1 (GEV shape / phylogenomic) | 5/10 | 4/10 | 7/10 | 4-5/10 |
| C1-H2 (Return levels / pathway failure) | 5/10 | 5/10 | 2/10 | 3-4/10 (after math correction) |
| C1-H7 (GPD scale / evolutionary rate) | 4/10 | 2/10 | 4/10 | 2-3/10 |

### High-Priority Candidates (both models agree, positive)

**C1-H1 (GEV shape parameter / phylogenomic signature)** is the best candidate to pursue:
- Both models confirm the EVT framework is mathematically rigorous and genuinely novel in this application domain
- Both models confirmed no prior work applies GEV shape parameters to proteome Tm distributions (EVT in proteomics exists only for MS score calibration)
- The SE calculation inconsistency is a correctable presentation error, not a design flaw (SE ≈ 0.035 at n=300 block minima)
- Required corrections: (1) reframe to test magnitude |xi|, not sign (Gemini's Weibull tautology point); (2) include proteome composition controls; (3) acknowledge that 2025 psychrophile data (Pseudoalteromonas arctica) shows non-simple tail behavior that must be modeled

### Needs Significant Revision

**C1-H2 (Return levels / pathway failure)** is reframeable:
- Both models confirm the complex bottleneck concept is real
- The formula orientation error (upper vs. lower tail) must be corrected before any experimental work
- New citation error found by GPT: Sun et al. 2023 (not "Lim et al. 2023")
- The ±2°C prediction should be withdrawn and replaced with empirically-derived confidence intervals
- Redesign: use essential-subunit definitions, whole-proteome complex set (not pathway-specific), intact-cell TPP for functional validation

### Unlikely in Current Form

**C1-H7 (GPD scale / evolutionary rate)** needs fundamental redesign:
- The Leuenberger confound is mathematically exact (sigma_Tm = b * sigma_ln(MW))
- The n=13 species design is severely underpowered for the question being asked
- The signal may exist at the protein level within species, but not at the species level
- Drummond citation corrected: PNAS 102:14338 confirmed by both QG and GPT

---

## Key Disagreements to Investigate

1. **H1 confidence divergence (GPT: 4/10 vs Gemini: 7/10)**: Gemini weights the mathematical formalism; GPT weights the biological confounds and limited species number. The 2025 psychrophile paper showing complex tail shapes is the strongest piece of new evidence — this should be read before investing in the analysis.

2. **H2 mechanism disagreement**: Gemini sees a fatal EVT misapplication; GPT sees a correctable math orientation error but is more concerned about the regulatory biology. Both agree the ±2°C claim is unjustified, but GPT views the framework as more salvageable. The key experiment: measure actual in-cell complex bottleneck Tm values (via intact-cell TPP) and compare to functional failure temperatures with matched assays.

3. **H7 confound severity**: Gemini proves the size confound algebraically; GPT confirms it. The question is whether a within-species analysis at the protein level (not species level) could rescue the hypothesis. This redesign is worth exploring before abandoning the concept.

---

## Cross-Cutting Findings

**EVT in proteomics — prior art check (GPT web search)**:
EVT has been applied in proteomics for peptide-spectrum match score calibration and biomarker null-distribution modeling, but not for proteome thermal-stability distributions. The EVT x Tm bridge is genuinely novel as a methodological contribution.

**Meltome Atlas status (GPT web search)**:
The Atlas remains at 13 species / ~48,000 proteins as of the accessible site. No peer-reviewed cross-species expansion was found. The human chapter has additional cell-line data. This constrains H1 and H7 which require cross-species comparisons.

**Mathematical interdependence of all three hypotheses (Gemini)**:
sigma_GPD = sigma_GEV + xi*(u - mu). The three parameters being proposed as independent biological variables (xi for H1, R_p for H2, sigma for H3) are mathematically derived from the same underlying GEV fit. A change in xi (H1) mathematically forces changes in both the GPD scale (H3) and return levels (H2). This interdependence should be treated as a feature — they are three views of the same phenomenon — not as three independent hypotheses.

---

## Recommended Next Steps

1. **Immediate (C1-H1)**: Fit GEV to block minima in the actual Meltome Atlas 13-species data. Report SE(xi) correctly as ~0.035. Test whether |xi| correlates with OGT. Apply phylogenetic GLS. Read the 2025 Pseudoalteromonas arctica psychrophile paper before interpreting results.

2. **Before any experiment (C1-H2)**: Fix the return-level formula orientation. Redefine the validation target: use essential-subunit annotations from perturbation data, not full CORUM. Use whole-proteome complex set for POT (not pathway-specific). Measure process failure temperatures in matched cell lines with intact-cell TPP.

3. **Redesign required (C1-H7)**: Abandon the 13-species species-level correlation. Consider instead: within-species partial correlation of protein Tm vs. dN/dS (protein-level, not species-level), controlling for expression, size, and disorder. This requires merging Meltome Atlas data with ortholog dN/dS databases at the protein level, giving ~13,000 data points (proteins) instead of 13 (species).

4. **Domain experts to consult**: Dr. Manasa Ramakrishna (EVT statistical methodology for non-stationary distributions); a thermal proteomics expert who has worked with TPCA data (Mikhail Savitski lab for TPCA validation); a molecular evolutionist familiar with dN/dS confounders in the Drummond-Wilke framework.
