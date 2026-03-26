# Ranking: Mechanobiology × Enhancer Epigenomics
## Session: 2026-03-25-targeted-002 | Cycle 1 | Generated: 2026-03-25

**Agent**: ranker-v5.2
**Hypotheses ranked**: 5 (all CONDITIONAL from Critique)
**Scoring**: 6-dimension weighted composite + cross-domain creativity bonus

---

## Scoring Dimensions and Weights

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Novelty (N) | 15% | Genuinely unstudied; gap confirmed by PubMed co-occurrence |
| Mechanistic Specificity (MS) | 20% | Named proteins, specific marks, quantitative predictions |
| Testability (T) | 20% | Practical experimental feasibility in realistic lab setting |
| Groundedness (G) | 20% | Supported by published evidence; [GROUNDED] vs [INFERRED] ratio |
| Impact/Significance (I) | 15% | Field impact if confirmed; disease relevance |
| Falsifiability (F) | 10% | Clean, specific falsification test exists |
| **Cross-domain bonus** | **+0.5** | **Applied when 2+ discipline boundaries crossed** |

Scores are integers 1–10 per dimension. Composite = weighted sum + optional bonus.

---

## Per-Hypothesis Scoring Tables

### H3: YAP-BRD4 Condensate Size Supralinear Encoding

**Disciplines**: Mechanobiology × Condensate Biophysics × Enhancer Epigenomics (3 fields → +0.5 bonus)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 8 | Stiffness-switch via LLPS cooperativity completely unstudied; supralinear encoding concept novel; 0 PubMed co-occurrence |
| Mechanistic Specificity | 7 | Cooperative LLPS model; Hill coefficient n=2–4; threshold stiffness ~10 kPa predicted; condensate volume power law |
| Testability | 7 | smFISH for CTGF/CYR61 feasible; power law fitting standard; STORM for BRD4 puncta technically demanding but achievable in specialized lab |
| Groundedness | 6 | YAP-BRD4 condensates established (Zanconato 2018; 2025 TAZ condensate literature); Hill coefficient estimated from generic LLPS; condensate formation in fibroblast/hydrogel UNVERIFIED (major gap) |
| Impact | 9 | Mechanical threshold switch explains fibrosis onset quantitatively; broad implications for disease threshold biology; quantitatively testable switch model is rare in mechanobiology |
| Falsifiability | 8 | Power law vs linear model fit is clean statistical test (F-test); IDR-deleted YAP mutant as condensate-cooperativity discriminant is elegant genetic control |

**Weighted score**: 0.15×8 + 0.20×7 + 0.20×7 + 0.20×6 + 0.15×9 + 0.10×8 = 1.20+1.40+1.40+1.20+1.35+0.80 = **7.35**
**Cross-domain bonus**: +0.5
**FINAL SCORE: 7.85** 🥇

**Critique adjustments applied**: Added IDR-deleted YAP as primary condensate-cooperativity discriminant; prerequisite condensate detection step added; nuclear import saturation acknowledged as alternative.

---

### H4: MRTF-A Preferentially Occupies CaRG-Box Mechanoenhancers on Stiff ECM

**Disciplines**: Mechanobiology × Enhancer Epigenomics (2 fields → no bonus)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 8 | MRTF-A ChIP-seq in mechanical context completely unstudied; CaRG-box mechanoenhancer occupancy never tested; 0 PubMed co-occurrence |
| Mechanistic Specificity | 7 | MRTF-A→EP300→H3K27ac with CaRG motif specificity; SRF as co-factor; clear genomic targets (CaRG-containing mechanoenhancers from Cosgrove catalog) |
| Testability | 8 | CUT&RUN/ChIP-seq is field-standard assay; MRTF-A antibody validated; hydrogel cell culture routine; knockdown controls clear |
| Groundedness | 7 | MRTF-A nuclear on stiff ECM: very well established (Miralles 2003+); EP300-MRTFA STRING 0.710 (experimental+co-expression); SRF/CaRG motifs at stiff mechanoenhancers: Cosgrove 2025 confirms; after critique: preference claim dropped, remaining claims well-grounded |
| Impact | 7 | Defines distinct MRTF-A-driven mechanoenhancer program; cytoskeletal gene regulation mechanistically explained; relevant to fibrosis, smooth muscle biology |
| Falsifiability | 9 | MRTF-A siRNA → H3K27ac loss at CaRG-box but NOT TEAD mechanoenhancers = clean positive/negative internal control test; one of the most elegant falsification designs in the set |

**Weighted score**: 0.15×8 + 0.20×7 + 0.20×8 + 0.20×7 + 0.15×7 + 0.10×9 = 1.20+1.40+1.60+1.40+1.05+0.90 = **7.55**
**Cross-domain bonus**: 0
**FINAL SCORE: 7.55** 🥈

**Critique adjustments applied**: "Preferentially occupies enhancers over promoters" claim removed; core claim reframed as MRTF-A occupies CaRG-box mechanoenhancers with H3K27ac deposition.

---

### H2: Piezo1→CaMKII→EP300 Rapid Pre-Priming

**Disciplines**: Mechanobiology × Calcium Signaling × Enhancer Epigenomics (3 fields → +0.5 bonus)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 8 | Rapid H3K27ac pre-priming concept before TF binding novel; Piezo1 as epigenome regulator unstudied; 0 PubMed co-occurrence for Piezo1+enhancer+H3K27ac |
| Mechanistic Specificity | 6 | Critique reveals: CaMKII→EP300 direct phosphorylation not established; revised route via HDAC4/5 nuclear export weakens direct chain; Piezo1 Ca²⁺ → CaMKII well-defined but HDAC4/5→EP300 step is indirect |
| Testability | 7 | CUT&RUN time course (15-min resolution) feasible; GsMTx4 issue flagged but Piezo1 conditional KO available; kinetic temporal separation is testable; pharmacological vs genetic approach comparison feasible |
| Groundedness | 6 | Piezo1 static stiffness activation CONFIRMED by web search; Science Advances 2025 Piezo1→H3K acetylation; CAMK2A-EP300 STRING 0.908; but CaMKII→HDAC4/5→EP300 indirect route reduces grounding; revised route is chemically valid |
| Impact | 8 | Establishes Piezo1 ion channels as chromatin regulators; rapid pre-priming concept has broad implications for mechanobiology timing; Piezo1 pharmacology (GsMTx4, Yoda1) now relevant to epigenetics |
| Falsifiability | 8 | Temporal kinetic test (15-min Piezo1-dependent H3K27ac before 30-min YAP nuclear entry) is clean falsification; Piezo1 KO eliminates Phase 1 but not Phase 2 |

**Weighted score**: 0.15×8 + 0.20×6 + 0.20×7 + 0.20×6 + 0.15×8 + 0.10×8 = 1.20+1.20+1.40+1.20+1.20+0.80 = **7.00**
**Cross-domain bonus**: +0.5
**FINAL SCORE: 7.50** 🥉

**Critique adjustments applied**: Mechanistic route revised from CaMKII→EP300 direct to CaMKII→HDAC4/5→EP300; Piezo1 static stiffness activation confirmed (counter-evidence retracted); genetic Piezo1 KO added as preferred control.

---

### H1: KDM6B→EP300 Sequential Epigenetic Relay

**Disciplines**: Mechanobiology × Enhancer Epigenomics (2 fields → no bonus)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 8 | KDM6B×mechanoenhancer completely unstudied; sequential epigenetic relay concept novel; 0 PubMed co-occurrence; only 1 paper (Tayler 2026) linking KDM6B to stiffness at all |
| Mechanistic Specificity | 7 | Sequential KDM6B→H3K27me3 demethylation→EP300→H3K27ac conversion; specific time prediction (2–4h lag); bivalent enhancer state as intermediate; KDM6B knockdown ablation test specific |
| Testability | 8 | CUT&RUN H3K27me3+H3K27ac time course is routine; KDM6B siRNA knockdown standard; cell system (Cosgrove 2025 fibroblasts) established; well-defined loci (mechanoenhancer catalog) |
| Groundedness | 6 | KDM6B-EP300 STRING 0.754 (co-expression+text-mining, not experimental direct binding); KDM6B stiffness control: 1 paper in MSCs (not fibroblasts); H3K27me3 at mechanoenhancers in fibroblasts UNVERIFIED — the critical false premise flagged by critique; bivalency unusual in differentiated cells |
| Impact | 7 | Explains how Polycomb-repressed mechanoenhancers become active; relevant to fibrosis epigenomics; establishes KDM6B as mechanosensitive epigenetic enzyme in fibroblasts |
| Falsifiability | 8 | KDM6B knockdown → ATAC-accessible but H3K27ac-negative mechanoenhancers (accessible-but-inactive state) = highly specific and clean falsification |

**Weighted score**: 0.15×8 + 0.20×7 + 0.20×8 + 0.20×6 + 0.15×7 + 0.10×8 = 1.20+1.40+1.60+1.20+1.05+0.80 = **7.25**
**Cross-domain bonus**: 0
**FINAL SCORE: 7.25** (4th)

**Critique adjustments applied**: Reformulated as conditional on H3K27me3 bivalency at mechanoenhancers; prerequisite verification (H3K27me3 CUT&RUN on soft ECM fibroblasts) stated; KDM6B relevance restricted to bivalent subset.

---

### H5: Phase-Separated YAP Condensates Mediate Looping-Independent E-P Contacts

**Disciplines**: Mechanobiology × Condensate Biophysics × Enhancer 3D Genome (3 fields → +0.5 bonus)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 9 | Directly addresses the most important unexplained anomaly from Cosgrove 2025 (86.2% looping-independent); condensate-mediated multi-enhancer co-localization not studied; most creative connection in set |
| Mechanistic Specificity | 5 | Critique reveals: verteporfin mechanism wrong (14-3-3σ sequestration ≠ condensate dissolution); 5 competing mechanisms predict same co-localization; surface tension force argument unverified for endogenous YAP condensates; mechanism revision needed |
| Testability | 6 | Oligopaint ORCA + STORM combination technically challenging (competing fixation requirements); IDR-deleted YAP approach requires molecular construct engineering; Micro-C feasible but expensive; highest technical bar of the 5 |
| Groundedness | 5 | 86.2% looping-independent confirmed (Cosgrove 2025); Shin 2018 surface tension mechanism from ARTIFICIAL condensates (not endogenous YAP); YAP condensates in fibroblasts/hydrogels UNVERIFIED; 5 competing alternatives |
| Impact | 9 | If confirmed: condensate physics established as primary E-P contact mechanism; explains major mystery in chromatin biology; bridges mechanobiology, condensate physics, and 3D genome |
| Falsifiability | 7 | IDR-deleted YAP control is clean; Micro-C pre/post is standard; but 5 competing mechanisms mean positive co-localization result doesn't exclusively confirm condensate role; needs mechanistic discrimination |

**Weighted score**: 0.15×9 + 0.20×5 + 0.20×6 + 0.20×5 + 0.15×9 + 0.10×7 = 1.35+1.00+1.20+1.00+1.35+0.70 = **6.60**
**Cross-domain bonus**: +0.5
**FINAL SCORE: 7.10** (5th)

**Critique adjustments applied**: Verteporfin replaced by IDR-deleted YAP as primary control; 5 competing alternatives acknowledged; condensate formation prerequisite in fibroblast/hydrogel system added.

---

## Composite Rankings

| Rank | ID | Title (short) | N | MS | T | G | I | F | Raw | Bonus | **Final** |
|------|----|--------------|---|----|----|---|---|---|-----|-------|-----------|
| 🥇 1 | H3 | YAP-BRD4 Supralinear Encoding | 8 | 7 | 7 | 6 | 9 | 8 | 7.35 | +0.5 | **7.85** |
| 🥈 2 | H4 | MRTF-A CaRG Mechanoenhancers | 8 | 7 | 8 | 7 | 7 | 9 | 7.55 | 0 | **7.55** |
| 🥉 3 | H2 | Piezo1→CaMKII Pre-Priming | 8 | 6 | 7 | 6 | 8 | 8 | 7.00 | +0.5 | **7.50** |
| 4 | H1 | KDM6B→EP300 Relay | 8 | 7 | 8 | 6 | 7 | 8 | 7.25 | 0 | **7.25** |
| 5 | H5 | YAP Condensates Loop-Less E-P | 9 | 5 | 6 | 5 | 9 | 7 | 6.60 | +0.5 | **7.10** |

**Score range**: 7.10–7.85 (all hypotheses clustered within 0.75 points — no dominant outlier)
**Mean score**: 7.45

---

## Elo Tournament Sanity Check

Pairwise comparisons among all 5 hypotheses (10 matchups):

| Matchup | Winner | Rationale |
|---------|--------|-----------|
| H3 vs H4 | H3 | Higher impact (9 vs 7) and cross-domain bonus offset lower groundedness |
| H3 vs H2 | H3 | Stronger mechanistic specificity; higher impact; comparable testability |
| H3 vs H1 | H3 | Higher impact, higher bonus; H1 grounded but lower impact |
| H3 vs H5 | H3 | Better testability, groundedness; despite H5 having equal impact (9) |
| H4 vs H2 | H4 | Better groundedness (7 vs 6), better testability (8 vs 7); H2 has bonus but smaller |
| H4 vs H1 | H4 | Better groundedness (7 vs 6), higher falsifiability (9 vs 8) |
| H4 vs H5 | H4 | Substantially better testability (8 vs 6) and groundedness (7 vs 5) |
| H2 vs H1 | H2 | Higher impact (8 vs 7) + bonus; H1 slightly better raw score but no bonus; Elo marginal |
| H2 vs H5 | H2 | Better testability (7 vs 6) and groundedness (6 vs 5) |
| H1 vs H5 | H1 | Better testability (8 vs 6), groundedness (6 vs 5) |

**Elo-implied ranking**: H3 > H4 > H2 > H1 > H5

✅ **Elo order matches composite ranking** — no paradoxes detected.

---

## Diversity Check

| Pair | Overlap | Concern? |
|------|---------|----------|
| H3 + H5 | Both test YAP condensates at mechanoenhancers; different predictions but overlapping mechanism space | MINOR — ranked #1 and #5; top-3 selection avoids co-selection |
| H1 + H2 | Both involve EP300 recruitment at mechanoenhancers; via distinct triggers (KDM6B vs Piezo1/CaMKII) | MINOR — complementary, not redundant |
| H4 (all others) | MRTF-A CaRG program is mechanistically orthogonal to all other hypotheses | NONE |

**Diversity assessment**: Top 3 (H3, H4, H2) covers three distinct mechanistic classes:
- H3: Condensate biophysics (stiffness encoding via cooperative LLPS)
- H4: Transcriptional coactivator binding (MRTF-A CaRG-box program)
- H2: Ion channel → kinase → epigenetic enzyme (rapid kinetic pre-priming)

✅ **No diversity constraint violated in top 3.**

---

## Top 3 Selected for Evolution / Quality Gate

1. **H3** (7.85) — YAP-BRD4 Condensate Supralinear Encoding
2. **H4** (7.55) — MRTF-A CaRG-Box Mechanoenhancer Occupancy
3. **H2** (7.50) — Piezo1→CaMKII→EP300 Rapid Pre-Priming

**H1** (7.25) and **H5** (7.10) proceed to Evolution for recombination with top-3 elements.

---

## Ranker Notes

- All scores are tightly clustered (range: 0.75 pts) — this is a cohesive, well-developed hypothesis set without clear outliers.
- **H3** leads primarily on Impact (9/10) — the quantitative switch model has the most potential for paradigm-level impact if confirmed.
- **H4** leads on Falsifiability (9/10) — the cleanest experimental design; most likely to produce a publishable result even if the hypothesis is falsified.
- **H5** ranks last despite highest Novelty (9/10) due to low Mechanistic Specificity (5/10) and Groundedness (5/10) after critique; it requires the most preliminary work before the core test is tractable.
- **H1's** false premise concern (bivalency assumption) is the key risk; if mechanoenhancers are NOT H3K27me3-poised in fibroblasts, H1 collapses. CUT&RUN prerequisite experiment (H3K27me3 at mechanoenhancers) would resolve this rapidly.
