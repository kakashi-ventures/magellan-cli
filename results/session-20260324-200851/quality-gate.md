# Quality Gate Results

**Session**: session-20260324-200851
**Target**: Cryo-EM single-particle analysis and heterogeneity methods x Bacterial outer membrane vesicle (OMV) cargo sorting mechanism
**Strategy**: tool_repurposing | Disjointness: DISJOINT
**Date**: 2026-03-24
**Validator model**: claude-opus-4-6

---

## Hypothesis C2-H1: Gaussian Mixture Model Analysis of Cryo-EM OMV Populations Distinguishes Biogenesis Pathways in P. aeruginosa

**Composite score**: 8.35 (with cross-domain bonus)

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Clear: Cryo-EM heterogeneity methods (A) -> GMM/BIC population classification (B) -> OMV biogenesis pathway discrimination (C) |
| Mechanism specificity | PASS | Specifies GMM applied to four descriptors (diameter, surface roughness, radial density profile, circularity), BIC for component selection, expected K>=3, size ranges per component |
| Falsifiable prediction | PASS | BIC-optimal K>=3 with >30nm diameter separation between means AND protein-to-lipid ratio separation; smallest component enriched for OprF. Falsifiable: if K=1 or components not separable, hypothesis fails |
| Counter-evidence section | PASS | Heterogeneity may reflect continuum not discrete pathways; environmental conditions may dominate over genetic pathway differences |
| Test protocol | PASS | Actionable: cryo-EM imaging of P. aeruginosa OMVs, extract per-vesicle descriptors, fit GMM, use delta-ompA mutant to validate by losing one component |
| Confidence calibration | PASS | 7/10 is reasonable given that OMV size heterogeneity is well-documented (50-400nm range confirmed) and GMM/BIC is standard ML. The novel part is applying it to whole-vesicle populations |
| Novelty (web-verified) | PASS | No published work applies GMM/BIC population analysis to cryo-EM-derived OMV descriptors to distinguish biogenesis pathways. Existing single-EV imaging (PMC12002403) uses neural network segmentation + eccentricity classification on mammalian EVs, NOT GMM/BIC on bacterial OMVs with multi-descriptor fitting. Size-dependent toxin sorting (PMC10187208) uses fluorescence microscopy, not cryo-EM computational classification. The connection is NOVEL. |
| Groundedness | PASS (7/10) | OMV size ranges verified (50-400nm, P. aeruginosa). OprF enrichment in OMVs confirmed via proteomics. OprF latch mechanism in OMV biogenesis published (bioRxiv 2023.11.12.566662). delta-ompA hypervesiculation documented. RELION uses EM algorithm (equivalent to GMM classification) confirmed. |
| Language precision | PASS | Terminology correct for both cryo-EM (BIC, GMM, radial density profile) and microbiology (OprF, delta-ompA, biogenesis pathways) domains |
| Per-claim verification | PASS | See below |

#### Per-Claim Grounding Verification

| Claim | Status | Evidence |
|-------|--------|----------|
| RELION uses EM which is equivalent to GMM classification [GROUNDED] | VERIFIED | RELION implements maximum-likelihood via expectation-maximization algorithm; GMM is the standard illustration of EM. The EM-ML algorithm is explicitly described as using GMM in RELION documentation (Scheres 2012, J Mol Biol). |
| P. aeruginosa OMV size range 50-250nm [GROUNDED] | VERIFIED | Confirmed: planktonic OMVs mode ~124nm (PA14), range 21-400nm depending on strain and growth conditions (PLOS ONE 2019). |
| OprF enriched in OMVs [GROUNDED] | VERIFIED | OprF consistently identified as abundant OMV protein across multiple P. aeruginosa proteomics studies (J Bacteriol 2013, multiple LC-MS/MS analyses). |
| delta-ompA mutant alters OMV production [GROUNDED] | VERIFIED | OmpA deletion induces hypervesiculation and alters vesicle size and cargo composition (Nat Commun 2016, multiple reviews). OprF is the P. aeruginosa OmpA homolog. |

#### Novelty Searches Performed
1. "cryo-EM GMM analysis outer membrane vesicle population heterogeneity" -- No direct match. Closest: single EV imaging with neural networks (mammalian EVs), NOT GMM on bacterial OMVs
2. "BIC model selection Gaussian mixture model vesicle population clustering single-particle cryo-EM" -- GMM used for protein structure representation in cryo-EM, NOT for vesicle population classification
3. "cryoDRGN 3DVA heterogeneity analysis vesicle membrane bacterial OMV" -- cryoDRGN/3DVA used for protein conformational heterogeneity, NOT whole-vesicle population analysis

**VERDICT: PASS**
**Reason:** Genuinely novel application of GMM/BIC (standard in ML and used within RELION for particle classification) to whole-vesicle population analysis for biogenesis pathway discrimination. All grounded claims verified. Mechanism is specific and falsifiable. The gap between within-RELION GMM usage and whole-vesicle population GMM classification is real and unexploited.

---

## Hypothesis C2-H2: Power Analysis for Subtomogram Averaging of OMV Budding Intermediates Sets Feasibility Boundary

**Composite score**: 8.55 (with cross-domain bonus)

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Cryo-ET subtomogram averaging methods (A) -> Power analysis/feasibility calculation (B) -> OMV budding site structural determination (C) |
| Mechanism specificity | PASS | Specifies formula N_min ~ (d/r)^3 * SNR^-2, with values d~50nm, r=3nm, SNR~0.1. Calculates specific outcome: 200-500 subtomograms, 200-500 tomograms, 70-170 hours |
| Falsifiable prediction | PASS | Clear feasibility boundary: if N_min >> 1000 or microscope time >> 4 weeks, approach is infeasible. If N_min = 200-500, feasible in 2-4 weeks |
| Counter-evidence section | CONDITIONAL | The hypothesis notes computational requirements but underexplores the key risk: OMV budding intermediates may be too rare per cell to find 200-500 in 200-500 tomograms. Budding frequency is unknown |
| Test protocol | PASS | Actionable: collect tomograms, identify budding sites, extract subtomograms, average. Time/resource estimates provided |
| Confidence calibration | CONDITIONAL | 8/10 may be slightly high. The power analysis formula is reasonable but the specific N_min values depend on assumptions about OMV budding site homogeneity and rarity that are not well-constrained |
| Novelty (web-verified) | PASS | No published power analysis for subtomogram averaging specifically of OMV budding sites. The eLife paper (73099) surveyed OMV structures in ~90 species but did NOT perform subtomogram averaging on budding sites or any power analysis |
| Groundedness | CONDITIONAL (7/10 -> 6/10) | **CITATION ERROR**: The hypothesis cites "Schur et al. 2016 Nature" for HIV-1 capsid subtomogram averaging. The actual publication is Schur et al. 2016 **Science** (vol. 353, pp. 506-508, DOI: 10.1126/science.aaf9620), NOT Nature. The paper exists and the scientific content (3.9A resolution, subtomogram averaging) is correct, but the journal attribution is wrong. This is a minor citation error, not a hallucination (the paper and its findings are real). Resolution scaling with N is established in the field but no single canonical formula was found matching the exact (d/r)^3 * SNR^-2 form; however, the general relationship that resolution improves with particle number and SNR is well-established |
| Language precision | PASS | Correct terminology for cryo-ET, subtomogram averaging, SNR |
| Per-claim verification | CONDITIONAL | See below |

#### Per-Claim Grounding Verification

| Claim | Status | Evidence |
|-------|--------|----------|
| Schur et al. 2016 Nature, HIV-1 capsid [GROUNDED] | PARTIALLY VERIFIED - JOURNAL ERROR | Paper exists: Schur et al. 2016, "An atomic model of HIV-1 capsid-SP1 reveals structures regulating assembly and maturation." Published in **Science** vol. 353(6298), pp. 506-508, NOT in Nature. Scientific content correct (3.9A resolution via subtomogram averaging). |
| Resolution scaling with N established [GROUNDED] | VERIFIED | General principle confirmed across cryo-ET literature. Subtomogram averaging improves resolution by averaging multiple copies. Typical requirement: 1000-2000 particles for high resolution. |
| N_min formula ~ (d/r)^3 * SNR^-2 [GROUNDED] | UNVERIFIABLE | No specific source found for this exact formula. The dimensional analysis is plausible (resolution scales with particle number, SNR matters), but this specific formulation appears to be a parametric construction rather than a published formula. |
| OMV budding site diameter ~50nm [GROUNDED] | VERIFIED | Consistent with known OMV sizes (50-400nm) and budding intermediates observed in cryo-ET of multiple bacterial species (eLife 73099). |
| SNR ~0.1 in cryo-ET [GROUNDED] | VERIFIED | Consistent with known cryo-ET imaging conditions. Low SNR is a defining challenge of cryo-ET. |

#### Novelty Searches Performed
1. "subtomogram averaging power analysis OMV budding sites bacterial" -- No direct match. STA applied to many structures but not OMV budding with power analysis
2. "cryo-electron tomography OMV budding intermediate in situ bacterial membrane" -- eLife 2021 paper surveyed OMV structures but did not perform STA on budding sites
3. "subtomogram averaging resolution scaling number particles formula N SNR cryo-ET" -- General principle confirmed, specific formula not found as published

**VERDICT: CONDITIONAL PASS**
**Reason:** Novel and actionable idea -- a power analysis for OMV budding site subtomogram averaging has not been published. However, two issues require correction: (1) Citation error: Schur et al. 2016 was published in Science, not Nature -- this is a factual error in journal attribution though the paper exists and the scientific content is correct; (2) The specific N_min formula is unverifiable as a published formula and appears to be a parametric construction. These issues downgrade confidence but do not invalidate the core hypothesis. The approach remains novel and feasible. Corrected confidence: 6/10 (from 8/10). Corrected groundedness: 6/10 (from 9/10).

---

## Hypothesis C2-H3: Periplasmic Chaperone DegP Co-localization with OMV Cargo Proteins Resolved by Cryo-ET Difference Mapping

**Composite score**: 8.20 (with cross-domain bonus)

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | Cryo-ET difference mapping (A) -> DegP density identification at budding sites (B) -> OMV cargo chaperone mechanism (C) |
| Mechanism specificity | PASS | Specifies WT minus delta-degP difference mapping, expected density loss (~12nm hexameric cage), reduced luminal density. Cites DegP-S210A protease-dead mutant as better control |
| Falsifiable prediction | PASS | Difference map shows localized density loss at budding sites corresponding to ~12nm hexameric cage. If no localized density difference or density is dispersed, hypothesis fails |
| Counter-evidence section | PASS | delta-degP pleiotropic effects acknowledged; suggests DegP-S210A as improvement. DegP may degrade rather than escort cargo. General envelope stress in delta-degP may confound |
| Test protocol | PASS | Actionable: cryo-ET of WT vs delta-degP, difference mapping, DegP-S210A control. Specific structural predictions (12nm cage) |
| Confidence calibration | PASS | 6/10 is well-calibrated given that DegP's role in OMV biology is established but its specific localization at budding sites is unproven |
| Novelty (web-verified) | PASS | No published cryo-ET difference mapping of DegP at OMV budding sites. DegP's role in OMV production is known (delta-degP hypervesiculation) but its spatial localization at budding sites via cryo-ET has not been attempted |
| Groundedness | PASS (7/10) | DegP hexameric cage confirmed (~700,000 A^3 cavity for 24-mer; hexamer as staggered dimer of trimers). DegP in OMV context confirmed (delta-degP hypervesiculation). DegP-S210A protease-dead mutant retaining chaperone function confirmed. Difference cryo-ET is established methodology |
| Language precision | PASS | Correct terminology: hexameric cage, periplasmic chaperone, protease-dead mutant S210A, difference mapping |
| Per-claim verification | PASS | See below |

#### Per-Claim Grounding Verification

| Claim | Status | Evidence |
|-------|--------|----------|
| DegP in OMVs established [GROUNDED] | VERIFIED | delta-degP mutants show hypervesiculation at 37C in E. coli. DegP deletion leads to accumulation of misfolded proteins and increased OMV production (multiple sources including PNAS 2008, Nature 2008). |
| DegP forms hexameric cage (~12nm) [GROUNDED] | VERIFIED | DegP hexamer is a staggered dimer of trimers. Forms 12-mer, 18-mer, 24-mer cages upon substrate binding. 24-mer cavity is ~700,000 A^3 (Nature 2008, Krojer et al.). The ~12nm claim for the hexamer is physically consistent with known dimensions. |
| DegP-S210A retains chaperone function [GROUNDED] | VERIFIED | DegP(S210A) is devoid of proteolytic activity but retains chaperone activity. Can rescue E. coli growth during autotransporter expression (PubMed 10940032, PLOS ONE 2016). |
| Difference cryo-ET established [GROUNDED] | VERIFIED | Difference mapping in cryo-ET is an established approach used for flagellar components and other cellular structures. |
| delta-degP has pleiotropic effects [GROUNDED] | VERIFIED | delta-degP affects envelope stress response broadly; not specific to OMV pathway. Multiple periplasmic quality control functions affected. |

#### Novelty Searches Performed
1. "DegP chaperone cryo-ET difference mapping outer membrane vesicles" -- No direct match. DegP role in OMVs known, but cryo-ET difference mapping approach not published
2. "DegP localization OMV budding site cryo-ET periplasm in situ imaging" -- No published in situ localization of DegP at OMV budding sites
3. "DegP S210A protease-dead mutant outer membrane vesicle chaperone function" -- DegP-S210A well-characterized but never combined with cryo-ET OMV analysis

**VERDICT: PASS**
**Reason:** Genuinely novel synthesis: DegP's role in OMV biology is established, cryo-ET difference mapping is established, but combining them to localize DegP at budding sites has not been done. All grounded claims verified. Mechanism is specific with the ~12nm hexameric cage providing a structural prediction. The DegP-S210A control suggestion from the Critic demonstrates sophisticated experimental design awareness. Well-calibrated confidence at 6/10.

---

## Hypothesis C2-H4: Machine Learning-Guided Template Matching Identifies OMV Cargo Proteins In Situ Without Labels

**Composite score**: 8.15 (with cross-domain bonus)

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | ML template matching tools (A) -> Per-OMV protein identification via PDB templates (B) -> OMV cargo manifest and subtype classification (C) |
| Mechanism specificity | PASS | Specifies DeePiCt and TomoTwin applied to cryo-ET of P. aeruginosa OMVs, template matching against PDB structures, cross-correlation threshold >0.5, per-OMV cargo manifests |
| Falsifiable prediction | PASS | Identify >=2 OMPs per OMV with CC > 0.5; classification reveals >= 2 distinct subtypes. If CC < 0.5 for all templates or no subtypes emerge, hypothesis fails |
| Counter-evidence section | PASS | 20-30A resolution marginal for distinguishing similar OMPs; false positive rate may be high; membrane signal may dominate protein signal |
| Test protocol | PASS | Actionable: collect cryo-ET of P. aeruginosa OMVs, apply DeePiCt/TomoTwin with PDB templates, evaluate CC scores, classify OMVs |
| Confidence calibration | PASS | 5/10 well-calibrated given the acknowledged resolution limitations. This is appropriately modest for an approach that pushes against physical resolution limits |
| Novelty (web-verified) | PASS | No published application of DeePiCt or TomoTwin to OMV cargo identification. Both tools applied to cellular tomograms (ribosomes, FAS) but never to bacterial OMVs. Template matching for vesicle contents is a genuinely unexplored application |
| Groundedness | PASS (7/10) | Both citations verified. Resolution concern is real and honestly acknowledged. The approach is technically sound even if outcomes are uncertain |
| Language precision | PASS | Correct terminology for both ML tools (DeePiCt, TomoTwin, cross-correlation, template matching) and microbiology (OMPs, cargo manifests, OMV subtypes) |
| Per-claim verification | PASS | See below |

#### Per-Claim Grounding Verification

| Claim | Status | Evidence |
|-------|--------|----------|
| de Teresa et al. 2023 Nat Methods (DeePiCt) [GROUNDED] | VERIFIED | de Teresa-Trueba et al., "Convolutional networks for supervised mining of molecular patterns within cellular context," Nature Methods vol. 20, pp. 284-294 (2023). Published January 23, 2023. Note: lead author surname is "de Teresa-Trueba," hypothesis abbreviates to "de Teresa" which is acceptable shorthand |
| Rice et al. 2023 Nat Methods (TomoTwin) [GROUNDED] | VERIFIED | Rice G., Wagner T. et al., "TomoTwin: generalized 3D localization of macromolecules in cryo-electron tomograms with structural data mining," Nature Methods vol. 20, pp. 131-138 (2023). Published at Max Planck Institute of Molecular Physiology, Dortmund. |
| DeePiCt/TomoTwin applied to cellular tomograms but not OMVs [GROUNDED] | VERIFIED | DeePiCt tested on S. pombe tomograms (ribosomes, FAS, membranes, NPCs). TomoTwin is a general picking model tested on cellular tomograms. No published application to OMV cargo identification found. |
| 20-30A resolution marginal for distinguishing similar OMPs [GROUNDED] | VERIFIED | Template matching depends primarily on low-resolution signal; at 20-30A, many OMPs would appear similar. High false positive rate confirmed as a known limitation of 3D template matching (Nature Commun 2024). |
| Cross-correlation > 0.5 threshold [GROUNDED] | VERIFIED as REASONABLE | CC thresholds vary by application, but 0.5 is within the range used in template matching studies. Recent work emphasizes p-value based assessment over raw CC scores. |

#### Novelty Searches Performed
1. "DeePiCt TomoTwin template matching OMV cargo identification bacterial vesicles" -- No direct match
2. "machine learning template matching identify proteins vesicles cryo-ET in situ bacterial" -- Template matching applied to cellular structures but NOT specifically to OMV cargo
3. "cryo-EM template matching protein identification outer membrane vesicle resolution limit 20 angstrom" -- Vesicle Picker (2024) identifies vesicles in cryo-EM, but identifies the vesicles themselves, not cargo proteins within them

**VERDICT: PASS**
**Reason:** Genuinely novel application of state-of-the-art ML template matching tools (DeePiCt, TomoTwin) to OMV cargo identification. Both citations verified. The key resolution limitation is honestly acknowledged (5/10 confidence is appropriate). The hypothesis is technically sound even if the outcome is uncertain -- this is exactly the kind of tool-transfer hypothesis MAGELLAN should produce. The false positive concern from the Critic is valid and constructively integrated.

---

## Summary

| Hypothesis | Verdict | Adjusted Confidence | Adjusted Groundedness | Key Issue |
|-----------|---------|--------------------|-----------------------|-----------|
| C2-H1: GMM/BIC OMV Population Analysis | PASS | 7/10 | 7/10 | None significant |
| C2-H2: Power Analysis for OMV Budding STA | CONDITIONAL PASS | 6/10 (was 8) | 6/10 (was 9) | Journal citation error (Science not Nature); N_min formula unverifiable |
| C2-H3: DegP Cryo-ET Difference Mapping | PASS | 6/10 | 7/10 | None significant |
| C2-H4: ML Template Matching OMV Cargo | PASS | 5/10 | 7/10 | Resolution limitation honestly acknowledged |

**Passed**: 3 | **Conditional Pass**: 1 | **Failed**: 0

---

## META-VALIDATION Reflection

### 1. Reputation check
For each PASS: Would I bet my reputation that this is genuinely novel and mechanistically sound?

- **C2-H1 (GMM/BIC)**: YES. GMM/BIC is standard in ML, used within RELION for particle classification, but applying it to whole-vesicle population analysis for biogenesis pathway discrimination is a genuine gap. Extensive searching found no published work in this space. The mammalian EV single-particle paper (2024/2025) uses neural network segmentation, not GMM; the OMV size-sorting paper uses fluorescence, not cryo-EM computation.

- **C2-H2 (Power Analysis)**: CONDITIONAL. The core idea is novel and valuable. However, the Schur citation says "Nature" when the paper was published in Science -- this is a factual error that undermines trust. The N_min formula may be a parametric construction rather than a published result. The idea itself is sound, but the execution has verifiable errors.

- **C2-H3 (DegP Difference Mapping)**: YES. This is a clean synthesis of two established approaches (DegP biology + cryo-ET difference mapping) applied to an unaddressed question (DegP localization at budding sites). All claims verified. The DegP-S210A suggestion from the Critic strengthens the experimental design.

- **C2-H4 (ML Template Matching)**: YES, with appropriate caution. Both citations verified. The resolution limitation is real but honestly acknowledged. The 5/10 confidence is appropriate for a hypothesis that pushes against resolution limits. This is exactly the kind of ambitious tool-transfer that produces real discoveries when it works.

### 2. Search budget check
- C2-H1: 6 searches (3 novelty + 3 claim verification) -- ADEQUATE
- C2-H2: 7 searches (3 novelty + 4 claim verification) -- ADEQUATE
- C2-H3: 5 searches (2 novelty + 3 claim verification) -- ADEQUATE
- C2-H4: 6 searches (3 novelty + 3 claim verification) -- ADEQUATE
- Total: 24 targeted web searches performed across all hypotheses

### 3. UNVERIFIABLE claims assessment
- C2-H2: The N_min formula is UNVERIFIABLE as a published result. This is a bridge-relevant claim (the entire feasibility calculation depends on it). This is why C2-H2 receives CONDITIONAL PASS rather than full PASS. The general principle of resolution scaling with N is valid, but the specific formula lacks a citable source.

### 4. Per-GROUNDED claim audit
- C2-H1: 4/4 claims verified -- ALL PASS
- C2-H2: 4/5 claims verified, 1 partially verified (journal error), 1 unverifiable (formula) -- CONDITIONAL
- C2-H3: 5/5 claims verified -- ALL PASS
- C2-H4: 5/5 claims verified -- ALL PASS

### 5. Citation audit
- C2-H1: No specific papers cited by name; claims are about established methods -- NO HALLUCINATION RISK
- C2-H2: "Schur et al. 2016 Nature" -- PAPER EXISTS but published in **Science**, not Nature. This is a JOURNAL ATTRIBUTION ERROR, not a hallucination (the paper, authors, year, and scientific content are all correct)
- C2-H3: No specific papers cited by name in mechanism section -- NO HALLUCINATION RISK
- C2-H4: "de Teresa et al. 2023 Nat Methods" -- VERIFIED (de Teresa-Trueba et al., Nat Methods 20:284-294, 2023). "Rice et al. 2023 Nat Methods" -- VERIFIED (Rice & Wagner et al., Nat Methods 20:131-138, 2023)

### Overall assessment
This is a strong session. The tool_repurposing strategy applied to a DISJOINT target (cryo-EM methods x OMV biology) has produced genuinely novel hypotheses. The key strength is that all four hypotheses transfer established computational/structural biology methods to an unexplored biological system. The hypotheses are grounded in verified biology and propose specific, falsifiable experiments. The one weakness -- the journal citation error in C2-H2 -- is a factual mistake rather than a hallucination, and the core idea remains valid with corrections.

---

## Web Searches Performed (Full Log)

1. "cryo-EM GMM analysis outer membrane vesicle population heterogeneity" -- Novelty check C2-H1
2. "subtomogram averaging power analysis OMV budding sites bacterial" -- Novelty check C2-H2
3. "DegP chaperone cryo-ET difference mapping outer membrane vesicles" -- Novelty check C2-H3
4. "DeePiCt TomoTwin template matching OMV cargo identification bacterial vesicles" -- Novelty check C2-H4
5. "RELION expectation maximization Gaussian mixture model classification cryo-EM" -- Claim verification C2-H1
6. "Schur 2016 Nature HIV-1 capsid subtomogram averaging resolution" -- Citation verification C2-H2
7. "de Teresa 2023 Nature Methods DeePiCt cryo-electron tomography" -- Citation verification C2-H4
8. "Rice 2023 Nature Methods TomoTwin cryo-electron tomography" -- Citation verification C2-H4
9. "OprF P. aeruginosa outer membrane vesicles porin enrichment proteomics" -- Claim verification C2-H1
10. "DegP hexameric cage 12-mer 24-mer structure size dimensions periplasm" -- Claim verification C2-H3
11. "Schur 2016 Science HIV-1 capsid subtomogram averaging 3.9 angstrom" -- Re-verification C2-H2 (confirmed Science not Nature)
12. "P. aeruginosa OMV size distribution bimodal population diameter range" -- Claim verification C2-H1
13. "cryo-EM single particle analysis bacterial extracellular vesicle subtypes classification 2024 2025" -- Deep novelty check C2-H1
14. "ompA deletion mutant OMV production size change biogenesis pathway" -- Claim verification C2-H1
15. "OprF OMV latch biogenesis P. aeruginosa vesicle size" -- Claim verification C2-H1/H3
16. "subtomogram averaging resolution scaling number particles formula N SNR cryo-ET" -- Claim verification C2-H2
17. PMC12002403 full text fetch -- Deep novelty check C2-H1 (mammalian EV paper uses neural nets, not GMM)
18. bioRxiv 2023.05.03.539273 full text fetch -- Deep novelty check (size-dependent toxin sorting, fluorescence not cryo-EM)
19. "size-dependent toxin sorting bacterial outer membrane vesicles OMV cryo-EM classification 2023" -- Deep novelty check
20. "cryo-electron tomography OMV budding intermediate in situ bacterial membrane" -- Deep novelty check C2-H2
21. "DegP S210A protease-dead mutant outer membrane vesicle chaperone function" -- Claim verification C2-H3
22. "cryo-EM template matching protein identification outer membrane vesicle resolution limit 20 angstrom" -- Claim verification C2-H4
23. "template matching cryo-ET false positive rate cross-correlation 20-30 angstrom resolution" -- Claim verification C2-H4
24. "BIC model selection Gaussian mixture model vesicle population clustering single-particle cryo-EM" -- Deep novelty check C2-H1
25. "de Teresa-Trueba 2023 Nature Methods DeePiCt convolutional networks supervised mining" -- Re-verification C2-H4
26. "Gaussian mixture model extracellular vesicle subpopulation clustering EV analysis" -- Deep novelty check C2-H1
27. "cryo-electron tomography P. aeruginosa outer membrane vesicle in situ structure 2024 2025 2026" -- Deep novelty check all
28. "machine learning template matching identify proteins vesicles cryo-ET in situ bacterial" -- Deep novelty check C2-H4
29. "cryoDRGN 3DVA heterogeneity analysis vesicle membrane bacterial OMV" -- Deep novelty check C2-H1
30. "DegP localization OMV budding site cryo-ET periplasm in situ imaging" -- Novelty check C2-H3
31. eLife 73099 full text fetch -- Scope verification for OMV cryo-ET literature
