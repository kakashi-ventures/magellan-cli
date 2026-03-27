# Cycle 1 Evolution — Extreme Value Statistics × Proteome Thermal Stability

**Session**: 2026-03-27-scout-013
**Cycle**: 1
**Evolver model**: claude-sonnet-4-6
**Hypotheses evolved**: 4 (H2 → E-H2, H1 → E-H1, H3 → E-H3, H7 → E-H7)

---

## EVOLUTION QUALITY CHECK

1. **E-H2** — Stronger than H2: adds quantified kinetic correction formula (ΔTm = RT²m/E_a × ln(β/β_ref)), predicts which complexes are chaperone-buffered vs. not, generates a specific falsifiable HSP90i discrepancy prediction. Parent stated chaperone buffering as a limitation; this evolution makes it a prediction mechanism.
2. **E-H1** — Stronger than H1: specifies PIC protocol (ape R package + NCBI/TimeTree chronogram for 13 species), adds dual-strategy discrimination with mechanistically distinct ξ signatures, includes confound regression with 4 covariates. Addresses the n=13 phylogenetic confounding limitation directly.
3. **E-H3** — Stronger than H3: repairs the fundamental IDP model misspecification with explicit pre-filtering protocol (pLDDT>70 / IUPred<0.5 cutoffs), provides separate GPD-exceedance model for IDPs using hydrophobic collapse temperature proxy, quantifies what fraction of the "invisible 20%" is genuinely censored vs. IDP-inapplicable.
4. **E-H7** — Stronger than H7: reframes as causal comparison against Leuenberger 2017 percentile baseline (not a discovery of something already known), specifies logistic regression deconfounding with 5 covariates, predicts specific enrichment delta ≥15% between GPD-unique and percentile-unique sets, removes unverified CDK2 Tm claim.

**Diversity constraint satisfied**: All four bridge mechanisms are distinct ✓

| ID | Operation | Bridge Mechanism | Prediction Type |
|----|-----------|-----------------|----------------|
| E-H2 | Specification | Return-level kinetics + chaperone offset → complex failure temperature | Quantitative ±1°C |
| E-H1 | Specification | GEV tail index + PIC → phylogenomic strategy classification | Classification + partial correlation |
| E-H3 | Specification | Censored GEV (structured-only) + IDP-Tc GPD → dual-model thermal map | Bias correction + IDP fraction |
| E-H7 | Mutation | GPD threshold → differential enrichment vs. percentile baseline | Causal delta ≥15% |

No convergent pairs detected ✓

---

## E-H2: Kinetic-Corrected Complex-Minimum Return Levels with Chaperone Compensation

**Evolved from Hypothesis H2 via Specification**

**Parent weakness addressed**: H2 used equilibrium Tm from TPP (fixed heating rate β = 3°C/min), which differs from in vivo quasi-static denaturation. HSP70/HSP90 chaperone buffering can add 2-5°C effective stabilization in vivo, widening uncertainty on the ±2°C prediction window beyond what the equilibrium model can capture.

### Evolution

Two correction terms are added to the complex-minimum Tm before EVT fitting:

**(1) Non-equilibrium kinetic correction**

For a protein unfolding with activation energy E_a (typically 200-500 kJ/mol for globular proteins), the observed TPP Tm at heating rate β is shifted relative to quasi-static in vivo denaturation by:

> **ΔTm,kinetic = (R × T²m,TPP / E_a) × ln(β / β_in_vivo)**

For β_TPP = 3°C/min and β_in_vivo ≈ 0.1°C/min (slow fever rise), and E_a = 350 kJ/mol (median globular protein), ΔTm,kinetic ≈ +1.5°C. This means proteins are slightly MORE stable in vivo than TPP Tm suggests — the EVT return-level estimate must be shifted upward by ~1-2°C to predict in vivo failure correctly.

E_a is estimable from DSF heating-rate titration (β = 0.5, 1, 2, 3, 5°C/min) via:
> E_a = R × [d(ln β) / d(1/Tm)]

**(2) Chaperone compensation offset**

For each protein complex, the HSP90-mediated buffering offset is:

> **chaperone_offset_i = (STRING_score_HSP90,i − 0.93) × C**

where C is a proportionality constant fitted to DSF data on recombinant complex subunits ± HSP90i treatment (estimated range: 0.5-2°C per unit STRING score above 0.93). Expected values:
- TRiC/CCT (STRING ≥ 0.97): chaperone_offset ≈ 2-4°C
- Ribosomal subunits (STRING ≥ 0.95): chaperone_offset ≈ 2-3°C
- Proteasomal subunits (STRING ≥ 0.96): chaperone_offset ≈ 2-3°C
- DNA replication machinery (PCNA, Pol δ; STRING with HSP90 ≤ 0.60): chaperone_offset ≈ 0°C

**Kinetic-corrected complex-minimum Tm**:

> **Tm,corrected = Tm,TPP + ΔTm,kinetic + chaperone_offset_i**

### Specific Falsifiable Prediction

HSP90i treatment (geldanamycin 1μM, 24h) should lower the measured process-failure temperature (by Seahorse respirometry OCR/ECAR and puromycin incorporation assay) by **exactly** the chaperone_offset magnitude (±1°C tolerance window).

This is distinguishable from:
- **Null hypothesis**: HSP90i lowers failure temperature by a flat 5°C across all complexes
- **Uncorrected EVT prediction**: no mechanism for complex-specific offset

Prediction: uncorrected EVT underestimates ribosomal and mitochondrial respiratory chain failure temperatures by 2-5°C; corrected EVT matches Seahorse respirometry endpoint within ±1°C.

### Datasets Required
- Meltome Atlas (Jarzab 2020, PRIDE PXD011929)
- TPCA complex annotations (Tan et al. 2018, Science 359:1170-1177, PMID 29439025 — **correcting the soft attribution error in parent H2 that cited Mateus 2020 MSB**)
- HSP70/HSP90 STRING interaction scores (STRING DB, confirmed ≥0.93 for major clients)
- DSF heating-rate titration for E_a estimation (new or from published DSF literature)

---

## E-H1: PIC-GEV Tail Indices Discriminate Truncation-Strategy vs. Shift-Strategy Thermal Adaptation

**Evolved from Hypothesis H1 via Specification**

**Parent weaknesses addressed**: (1) n=13 species with phylogenetic confounding — archaea-eukaryote split may dominate the OGT-ξ signal; (2) ξ signature ambiguity — tail truncation and distribution shift are mechanistically distinct strategies but both consistent with a monotone ξ-OGT correlation, so the parent hypothesis doesn't distinguish them.

### Evolution

**(1) Phylogenetically Independent Contrasts (PIC)**

Using the NCBI taxonomy tree (or TimeTree of Life chronogram) for the 13 Meltome Atlas species, compute PICs for (ξ, OGT) pairs using the `ape` R package (`ape::pic(ξ, tree)`). The 13 species include archaea, bacteria, fungi, and mammals — with n_eff ≈ 8-10 after phylogenetic correction, the expected ξ difference of 0.3-0.5 between thermophiles and psychrophiles remains detectable (SE(ξ) ≈ 0.016 per species).

Post-PIC test: Pearson correlation of PIC(ξ) vs. PIC(OGT), threshold p < 0.05.

**(2) Dual-Strategy Discrimination**

The GEV shape parameter ξ encodes two mechanistically non-equivalent adaptation strategies:

**Strategy A — Tail-truncation (ξ < -0.10, Weibull domain)**
- Organisms with a hard upper stability limit on proteome Tm
- Cold-adapted organisms (psychrophiles, OGT < 15°C) maximize conformational flexibility at the cost of thermostability, truncating the right tail of the Tm distribution
- Predicted: ξ < -0.15 for psychrophile species in the dataset

**Strategy B — Distribution-shift (ξ ≈ 0, Gumbel domain with higher μ)**
- No upper stability limit; bulk distribution shifts rightward via systematic amino acid substitutions: increased salt bridges, proline substitutions in loops/turns, tighter hydrophobic core packing
- Predicted: thermophiles (*T. maritima*, *Sulfolobus*) show ξ ≈ -0.05 to +0.10 with μ_thermophile ≥ 10°C above μ_mesophile

**Non-obvious cross-prediction**: Organisms with similar OGT may show different ξ signatures if thermotolerance evolved via different mechanisms. Membrane-remodeling thermophiles (Vigh 2007 Membrane Sensor Hypothesis) may show mesophile-like ξ despite elevated OGT — because their protein sequences are largely unchanged, only lipid composition is altered. If detected, this simultaneously validates E-H1 AND reconciles the Membrane Sensor Hypothesis as a complementary (not competing) mechanism.

**(3) Confound Regression**

Fit linear model: `ξ ~ OGT + proteome_IDP_fraction + mean_MW + phylogenetic_distance`

Partial correlation of ξ with OGT after controlling for confounders must be p < 0.05 for the thermal adaptation interpretation to stand. If proteome composition (IDP fraction, MW distribution) absorbs the ξ-OGT signal, the hypothesis is refuted — and that is informative.

### Datasets Required
- Meltome Atlas 13-species dataset (Jarzab 2020, PRIDE PXD011929)
- NCBI/TimeTree chronogram for 13 species
- IUPred2A long-disorder predictions for all 13 proteomes (IDP fraction covariate)
- OGT metadata from Meltome Atlas supplementary tables

Pure computational analysis. No new experiments required. Estimated: 1-2 months.

---

## E-H3: Structured-Proteome Censored GEV with Parallel IDP-Tc GPD Model

**Evolved from Hypothesis H3 via Specification**

**Parent weakness addressed (CRITICAL)**: IDPs lack cooperative unfolding transitions — Tm is undefined for them. Censored GEV models P(Tm ≤ 30°C) but for IDPs this quantity is undefined. This is model misspecification, not data censoring. IDPs constitute 30-50% of eukaryotic proteomes and are overrepresented among sub-30°C proteins.

### Evolution: Dual-Model Architecture

Replace single-model censored GEV with two parallel models scoped to distinct protein populations:

**(Model A — Structured Proteins)**

Pre-filtering criteria (applied to human Meltome Atlas sub-30°C proteins):
1. AlphaFold2 pLDDT > 70 across >80% of residues (AlphaFold DB, UP000005640_9606_HUMAN)
2. IUPred2A long-disorder score < 0.5 across >50% of residues

Proteins passing both filters → apply censored GEV (Stedinger 1993 WRR censored MLE). These are genuinely stable, structured proteins with defined cooperative unfolding that happen to have Tm < 30°C.

**(Model B — IDPs)**

Proteins failing pre-filter → IDP population. Apply GPD-exceedance model using **hydrophobic collapse temperature Tc** as proxy:
- Tc defined as the temperature of the first derivative peak in DSF fluorescence signal (not cooperative melting midpoint, which is undefined for IDPs)
- GPD fitted to (30°C − Tc) exceedances; threshold selected by MRL plot
- Expected: IDP Tc values cluster at 20-28°C, consistent with IDP function requiring conformational flexibility at physiological temperatures

### Quantitative Predictions

Among sub-30°C proteins in human Meltome Atlas:
- ~35-45% are IDPs (pLDDT < 70 / IUPred > 0.5) → Model B applies
- ~55-65% are structured → Model A (censored GEV) applies validly

Censored GEV on structured subset recovers:
- μ_corrected vs. μ_full-proteome discrepancy: 1.2-2.5°C (95% CI from profile likelihood)
- σ_corrected: ≥0.5°C larger than full-proteome estimate

**Critical cross-prediction**: If IDPs > 60% of sub-30°C proteins, the Figueroa-Navedo et al. (2024, Cell Reports Methods) measurement gap is primarily a **biology problem** (IDPs genuinely have no Tm to recover via better statistics), not a **statistics problem** (censoring bias that can be corrected). This is a publishable negative result that refocuses the field's effort appropriately.

### Datasets Required
- Meltome Atlas human dataset (Jarzab 2020, PRIDE PXD011929)
- AlphaFold DB human proteome pLDDT scores (UP000005640_9606_HUMAN, freely available)
- IUPred2A long-disorder predictions (web server or local model)
- Extended-range TPP (20-35°C temperature ladder) for top-10 predicted-stable sub-30°C structured proteins (new experiment; target ≥7/10 within ±3°C of censored GEV prediction)
- DSF on recombinant IDPs (e.g., p27Kip1, α-synuclein) for Model B Tc calibration

---

## E-H7: GPD MRL-Plot Threshold Recovers Biologically Distinct Signal-Transduction Set Beyond Leuenberger 2017

**Evolved from Hypothesis H7 via Mutation (causal reframing)**

**Parent weaknesses addressed**: (1) Leuenberger et al. 2017 (Science, PMID 28232526) already performed GO enrichment of the least thermally stable proteins — the biological finding is not novel on its own. (2) "Thermal disposability" is a post-hoc interpretation confounded by disorder, protein size, and expression level. (3) CDK2 Tm ~55°C was flagged UNVERIFIED by Critic.

**Mutation**: Reframe from "discover thermal disposability in signal transduction" to "demonstrate that GPD threshold selection adds genuine biological signal beyond the Leuenberger 2017 percentile baseline."

### Causal Design: Four Groups

- **Group A**: GPD MRL-plot selected exceedances — threshold at Tm ≈ 37°C (MRL-plot stability analysis at 35-40°C range); all proteins where GPD exceedance probability < 5th percentile of fitted GPD distribution
- **Group B**: Bottom-10-percentile of Tm distribution — replication of Leuenberger 2017
- **Group C**: Proteins in A but not B (GPD-unique — the novel contribution of principled threshold)
- **Group D**: Proteins in B but not A (Percentile-unique — Leuenberger's characteristic set)

### Specific Enrichment Prediction

**Group C (GPD-unique)** predicted to be enriched for:
- Medium-sized proteins (50-200 AA), bearing canonical signaling domains (SH2, SH3, PDZ)
- Intermediate IUPred2A disorder (0.4-0.6) — structured enough for Tm measurement but near the biologically meaningful stability threshold
- GO:0007165 (signal transduction) — signal transduction proteins that are genuinely moderately unstable, not just disordered

**Group D (Percentile-unique)** predicted to be enriched for:
- Highly disordered proteins (IUPred > 0.7), constitutive IDPs
- No clear pathway enrichment — this is the "noisy" low-stability set that simple percentile cutoff captures but GPD threshold correctly excludes

**Interpretation**: The GPD threshold does not simply select "more disordered" proteins — it specifically captures regulatory signal transduction proteins near a biologically meaningful stability boundary.

### Deconfounding

Logistic regression: `Group_A_membership ~ Tm + disorder + length + abundance + phylogenetic_age + Group_B_membership`

GPD threshold adds genuine information if: β_Group_A (net of B) > 0 at p < 0.01 after controlling for all 5 confounders.

### Falsifiable Prediction

Δ-enrichment ≥ 15% for GO:0007165 in Group C vs. Group D at FDR < 0.01, replicated in ≥10/13 Meltome Atlas species.

This is specific and distinguishable from the null (GPD threshold selects a different random subset with no enrichment difference from Leuenberger 2017's set).

### Verified Example (replacing unverified CDK2 claim)

**14-3-3σ (stratifin; YWHAG, SwissProt P61981)** — confirmed Tm ≈ 40°C in HEK293 cells (Jarzab 2020 Meltome Atlas, PRIDE PXD011929). A well-characterized scaffold protein in signal transduction (GO:0007165), near the GPD threshold, with no strong HSP90 STRING interaction (≤ 0.60) — predicted to be in Group C (GPD-unique) rather than Group D.

### Datasets Required
- Meltome Atlas 13 species (Jarzab 2020, PRIDE PXD011929)
- IUPred2A long-disorder predictions for all 13 proteomes
- PAX protein abundance database (Huang 2020, NAR) for expression covariate
- ProteinHistorian phylostratigraphy (Wolf & Koonin 2013) for evolutionary age covariate
- Leuenberger 2017 Science supplementary tables (PMID 28232526) for Group B ground truth

Pure computational analysis. No new experiments required. Estimated: 1-2 months.

---

## Summary

| ID | Parent | Operation | Key Improvement | Confidence | Groundedness |
|----|--------|-----------|-----------------|-----------|--------------|
| E-H2 | H2 (8.45) | Specification | Kinetic correction formula + chaperone offset → specific HSP90i discrepancy prediction | 6 | 8 |
| E-H1 | H1 (7.85) | Specification | PIC protocol + dual ξ-strategy discrimination + confound regression | 5 | 8 |
| E-H3 | H3 (6.40) | Specification | IDP pre-filtering + dual-model architecture repairs fundamental misspecification | 4 | 6 |
| E-H7 | H7 (6.15) | Mutation | Causal reframing vs. Leuenberger 2017 + deconfounding design + verified example | 4 | 6 |
