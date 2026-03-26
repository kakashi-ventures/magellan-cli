# Hypothesis Card: Kinetically Gated Epigenetic Memory at Mechanosensitive Super-Enhancers via BRD4-Scaffolded EP300 Retention

**Session**: 2026-03-26-targeted-001 (Blind Mode — Holdout Validation)
**Target**: Mechanobiology (ECM mechanics) × Epigenomics (genomic enhancer regulation)
**ID**: H5-v2 | **Parent**: H5 — Enhancer-Encoded Mechanical Memory via Self-Reinforcing H3K27ac-BRD4-EP300 Positive Feedback
**Generation cycle**: 1 (evolved, mutation + specification operations)
**Date**: 2026-03-26

---

## One-Line Summary

BRD4's multivalent nucleosome scaffold at mechanosensitive super-enhancers (SEs) retains EP300 after YAP exits the nucleus upon ECM softening, creating a kinetically gated H3K27ac memory window (6–18h) that persists because the SE write rate (k_write × 10–50x EP300/BRD4 density) exceeds the HDAC3-mediated erase rate (k_erase, rising 2–3x post-softening) — distinguishable from transcriptional auto-regulation by triptolide control and from BRD4 bromodomain effects by dBET6 vs. JQ1 differential.

---

## Quality Gate Verdict

| Dimension | Score |
|---|---|
| Mechanistic Specificity | 1.5/2.0 |
| Novelty | 1.5/2.0 |
| Groundedness | 1.0/2.0 |
| Testability | 1.5/2.0 |
| Impact | 1.0/2.0 |
| **Total** | **6.5/10** |

**Verdict**: CONDITIONAL_PASS
**Confidence**: 0.45 | **Groundedness**: 7/10
**QG mode**: Post-blind web-verified (7+ searches, 0 citation hallucinations)
**Conditions for revision**:
1. Revise H3K27ac base half-life from "30–90 min" to ~1.5h at enhancers (in vivo measurement); propagate through kinetic model to provide corrected memory window estimate.
2. BRD4-CTD to EP300-KIX domain specificity is unverified (BRD4-CTD known partner is P-TEFb, not EP300-KIX). May need revision to BRD4 ET domain or indirect shared chromatin substrate.
**Key novelty confirmation**: No paper proposes BRD4-scaffolded EP300 retention as a specific mechanism for SE H3K27ac memory post-ECM-softening. Mechanical memory is known (Yang et al. Nat Materials 2014) but SE epigenetic retention mechanism is novel. BRD4 mitotic bookmarking is known but different context (cell division, not mechanical memory).

---

## Bridge Mechanism (A → B → C)

**A** — ECM stiffness (stiff → soft transfer): YAP nuclear translocation on stiff ECM → YAP + TEAD + EP300 co-occupancy at mechanosensitive SE loci → H3K27ac deposition + BRD4 recruitment via bromodomain-H3K27ac reading

**B** — BRD4 multivalent nucleosome scaffold at SEs (10–50x more EP300/BRD4 than typical enhancers; Hnisz 2013, Sabari 2018 [GROUNDED]): after YAP exits upon ECM softening, BRD4-CTD provides an alternative EP300 docking site [PARAMETRIC; BRD4-EP300 STRING 0.988; specific domain interface requires characterization], preventing EP300 dissociation. EP300 retains ~20% activity at SEs post-YAP-exit [PARAMETRIC]. This creates a kinetic window where k_write (SE-amplified) > k_erase (HDAC3, re-upregulated 2–3x post-softening)

**C** — H3K27ac memory window: 6–18h persistence of H3K27ac at mechanosensitive SEs after ECM softening; >3x slower H3K27ac decay at SEs vs. typical enhancers; memory is epigenetic (not transcriptional auto-regulation), as shown by triptolide control

---

## Detailed Mechanism

**Step 1 — Stiff ECM priming** (0–72h): RhoA-ROCK1 → cytoskeletal tension → YAP dephosphorylation → YAP nuclear translocation → YAP-TEAD binds TEAD-motif SEs (CTGF, CCN2, ANKRD1 loci) → EP300 co-recruitment → H3K27ac deposition. BRD4 binds H3K27ac-marked SE nucleosomes via tandem bromodomains → high-density BRD4/MED1 SE occupancy established.

**Step 2 — ECM softening** (transfer to soft substrate): YAP phosphorylation → nuclear exclusion (15–60 min). For typical enhancers: EP300 dissociates with YAP → H3K27ac erased by rising HDAC3 (re-upregulation inferred from Fu 2024 reverse [PARAMETRIC]) within 1.5–2h (base half-life at enhancers).

**Step 3 — SE memory retention** (key mechanism): At SEs, BRD4-CTD creates an alternative EP300 docking site independent of YAP-TEAD [PARAMETRIC; specific domain: BRD4-CTD or ET domain interacting with EP300 KIX or bromodomain]. BRD4's multivalent scaffold across 10–50x more H3K27ac-marked nucleosomes retains EP300 at ~20% activity. The kinetic rate model:
- k_write (SE) = k_basal × SE_amplification_factor (10–50x) × EP300_residual (0.2) ≈ 2–10x baseline
- k_erase = HDAC3_activity × 2–3x (post-softening re-upregulation) ≈ 2–3x baseline
- Memory window: when k_write > k_erase → 6–18h predicted from BRD4 FRAP data (~2–4h SE residence) and HDAC3 kinetics

**Step 4 — Memory collapse**: BRD4 dissociation from H3K27ac-depleted nucleosomes → loss of EP300 scaffold → HDAC3 erasure dominates → H3K27ac decays. Memory half-life: 8 ± 4h. Typical enhancers lack SE amplification → k_write ≈ k_erase at baseline → rapid H3K27ac decay (<2h).

**Step 5 — Mechanistic discriminator** (dBET6 vs. JQ1): If BRD4-CTD scaffold (not bromodomain) retains EP300, then dBET6 (PROTAC degrader, removes all BRD4 including CTD) should collapse memory faster than JQ1 (bromodomain inhibitor only, leaves BRD4-CTD intact). This differential distinguishes scaffold mechanism from bromodomain-H3K27ac reading.

---

## Quantitative Predictions

1. **SE H3K27ac half-life** (primary): H3K27ac at mechanosensitive SEs decays with half-life 8 ± 4h post-softening; >3x slower than non-SE mechanosensitive enhancers (which should decay within ~1.5h, consistent with in vivo half-life).

2. **dBET6 > JQ1 differential**: dBET6 (500 nM, BRD4 protein degrader) collapses SE H3K27ac memory faster than JQ1 (500 nM, bromodomain inhibitor only). If BRD4-CTD scaffold is the mechanism, JQ1 should preserve memory while dBET6 eliminates it.

3. **Triptolide epigenetic memory**: Triptolide (0.5 μM, PP2A-activating transcription inhibitor) added at softening time point → SE H3K27ac maintained for 6–12h despite immediate mRNA decline (confirms epigenetic, not transcriptional auto-regulation).

4. **RGFP966 memory extension**: HDAC3-selective inhibitor (RGFP966, 10 μM) added at softening → extends memory window beyond 18h (tests whether HDAC3 is the primary eraser).

---

## Experimental Protocol

**Cell model**: MSCs on polyacrylamide hydrogels, 72h at 25 kPa (priming) → transfer to 1 kPa (memory phase), n = 3 biological replicates, 5,000 cells/cm² on fibronectin-coated 1,000 μm² circular micropatterns.

**Time course**: H3K27ac CUT&Tag at 0h, 2h, 4h, 8h, 12h, 18h, 24h post-softening (to define decay kinetics per SE vs. typical enhancer class).

**Mechanistic perturbations** (added at softening time point, T=0):
- JQ1 500 nM (bromodomain inhibitor only)
- dBET6 500 nM (PROTAC BRD4 degrader, full protein removal)
- Triptolide 0.5 μM (transcription inhibitor — epigenetic memory dissection)
- RGFP966 10 μM (HDAC3-selective inhibitor — erase rate modulation)

**Additional readouts**:
- BRD4 ChIP-seq at 0h, 4h, 8h, 18h post-softening (confirm BRD4 SE occupancy persistence)
- mRNA RT-qPCR for CTGF, CCN2, ANKRD1 at matching time points (transcriptional vs epigenetic memory)
- HDAC3 western blot post-softening (confirm re-upregulation kinetics)

**Cell density control**: Include parallel experiment without micropatterning (free-area spreading) to confirm results are stiffness-dependent and not spreading-area-dependent YAP activation.

**Timeline**: 6 months for CUT&Tag time course; 3 months for perturbation experiments; 12 months total.

---

## Key Literature

| Paper | Relevance |
|---|---|
| Yang et al. Nat Materials 2014 (PMID 24633344) | Mechanical memory in MSCs: YAP/TAZ activation depends on prior stiff culture time; irreversible above threshold |
| Hnisz et al. Cell 2013 (PMID 24119843) | Super-enhancer definition: BRD4/MED1/H3K27ac-dense clusters |
| Sabari et al. Science 2018 (PMID 29930091) | BRD4/MED1 form phase condensates at SEs; 10-50x density enrichment |
| Fu et al. Bone Research 2024 (PMID 38789434) | ECM stiffening downregulates HDAC3 (used in reverse: softening re-upregulates HDAC3) |
| Filippakopoulos et al. Nature 2010 | BRD4 bromodomain binds H3K27ac; structural basis for SE reading |
| Hsia et al. J Cell Sci 2023 (PMID 37330288) | Force-epigenome review; mechanical memory context |
| McSwiggen et al. eLife 2019 | Phase separation contested; BRD4 condensates may be exchange dynamics — relevant to mechanism interpretation |

---

## Known Concerns / Limitations

1. **BRD4-CTD/EP300-KIX domain mapping is unverified**: BRD4-CTD known partner is P-TEFb (CDK9/CycT1), not EP300-KIX. The BRD4-EP300 interaction may be via BRD4 ET domain or indirect through shared H3K27ac substrates. The general BRD4-EP300 co-occupancy at SEs is well-established (STRING 0.988), but the specific CTD-KIX domain interface is PARAMETRIC and likely incorrect or underdetermined. Revise to BRD4 ET domain or indirect scaffold if domain mapping experiments are performed.

2. **H3K27ac base half-life discrepancy**: Claimed "30–90 min" is shorter than in vivo measured ~1.5h at enhancers. This does not invalidate the kinetic model (SE amplification dominates) but shifts the predicted memory window toward 8–18h rather than 6–18h. Revise base half-life to 1.5h and re-derive memory window.

3. **Rate model parameter sensitivity**: The 6–18h prediction is a 3x range, reflecting uncertainty in: k_write (EP300 residual activity 0.2 is estimated), k_erase (HDAC3 kinetics post-softening is inferred from Fu 2024 reverse), BRD4 FRAP (~2–4h at SEs is from cancer cell lines not primary MSCs). High parameter sensitivity warrants >18h time points to capture full decay.

4. **HDAC3 re-upregulation is inferred**: Fu 2024 showed HDAC3 downregulation on stiff ECM. The hypothesis proposes re-upregulation upon softening (reverse). This is a logical inference but not experimentally established. HDAC3 western blot time course is essential.

5. **Yang 2014 memory window mismatch**: Yang et al. showed mechanical memory persists >10 days (irreversible above threshold stiff priming). H5-v2 proposes a 6–18h H3K27ac window. These operate on different timescales — H5-v2 describes the SHORT-TERM epigenetic memory window before long-term memory (possibly via DNA methylation) is established. This limitation should be explicitly stated.

---

## Evolutionary Improvements Over Parent (H5)

1. **BRD4 directionality corrected**: Parent claimed BRD4 RECRUITS EP300 (contested). Evolved version: BRD4 RETAINS EP300 already present at SEs via YAP-TEAD. Mechanistically defensible distinction.

2. **Kinetic rate model provided**: k_write/k_erase ratio computed; 6–18h window derived from BRD4 FRAP data and HDAC3 kinetics. Model predicts ~8 ± 4h memory half-life; internally consistent with SE amplification despite short single-nucleosome H3K27ac t1/2.

3. **dBET6 vs. JQ1 differential as novel mechanistic discriminator**: Distinguishes BRD4-CTD scaffold (not bromodomain) mechanism. Triptolide elevated to central experiment for epigenetic vs. transcriptional memory dissection.
