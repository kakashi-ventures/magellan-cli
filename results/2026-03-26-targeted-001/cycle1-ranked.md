# RANKER — Cycle 1 Ranking
**Session:** 2026-03-26-targeted-001
**Target:** Mechanobiology (ECM mechanics) × Epigenomics (genomic enhancer regulation)
**Mode:** BLIND (no WebSearch/WebFetch)
**Scoring weights:** Novelty 15% · Mechanism 20% · Testability 20% · Groundedness 20% · Cross-Domain Creativity 15% · Practical Impact 10%
**Cross-domain bonus policy:** +0.5 applied to all hypotheses — mechanobiology (biophysics/materials science) → epigenomics (molecular biology/genomics) spans 2+ disciplinary boundaries

---

## Per-Hypothesis Scoring Tables

---

### Hypothesis: C1-H3 — ECM Stiffness Coordinates a Dual-Enzyme Bivalent-to-Active Enhancer Switch via Concurrent KDM6B Activation and YAP-EP300 Recruitment

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 7 | Critic confirmed "no prior work on coordinated dual-enzyme enhancer switch under ECM stiffness." Both enzymes are individually mechanosensitive, but the idea that they converge on the same bivalent enhancer to execute a coordinated H3K27me3→H3K27ac switch has not been proposed. KDM6B's new role (Yu 2025) elevates novelty beyond existing YAP-EP300 biology. |
| Mechanistic Specificity | 20% | 7 | Names specific enzymes (KDM6B, UTX/KDM6A as revised candidate, EP300), specific residues (H3K27me3/H3K27ac), specific inhibitors with concentrations (GSK-J4 10 µM, A-485 3 µM), and specific cell type (hMSCs). Temporal mismatch (YAP in minutes, KDM6B in hours) is a real issue but the revised two-phase sequential model retains specificity. Genetic rescue (siKDM6B vs siKDM6A) resolves the GSK-J4 off-target problem. |
| Testability | 20% | 8 | Critic called this "excellent combinatorial inhibitor experiment." CUT&Tag for dual H3K27me3/H3K27ac on hMSCs across stiffness gradients is feasible with existing reagents. GSK-J4 + A-485 combinatorial inhibition produces a clean 2×2 experiment with clear predictions. The poised enhancer overlap (Rada-Iglesias maps) provides a priori prediction set. A PhD student could complete this in 3 months. |
| Groundedness | 20% | 5 | Critic revised to 55% (6/10 claims verifiable). KDM6B upregulation by ECM stiffness specifically cited (Yu MCB 2025, ChIP-qPCR). EP300 via YAP-TEAD partially grounded (STRING 0.692). H3K27me3/H3K27ac mutual exclusivity is canonical biochemistry. Core parametric claim — coordination at the same enhancer loci — is plausible but unverified. No hallucinations detected. |
| Cross-Domain Creativity | 15% | 7 | This hypothesis achieves genuine cross-domain synthesis: it imports the concept of "bivalent chromatin" from developmental epigenomics and intersects it with the mechanosensitive kinase/demethylase cascade from mechanobiology, proposing that ECM stiffness (a physical stimulus) executes a developmental epigenetic program at the same loci where embryonic stem cells resolve lineage identity. The bridging insight — that mechanical force mimics morphogen action at the chromatin level through enzymatic coordination — spans materials science, signaling biology, and epigenomics distinctly. |
| Practical Impact | 10% | 7 | Bivalent enhancers mark developmental decision points (Rada-Iglesias Nature 2011). If ECM stiffness resolves bivalency via dual-enzyme coordination, this directly explains stiffness-directed stem cell fate (Engler Cell 2006) at the chromatin level. Implications for tissue engineering (substrate pre-conditioning protocols), pathological fibrosis (ectopic stiffness-driven differentiation), and cancer mechanopathology are significant. |
| **Composite (raw)** | | **6.80** | 7(0.15)+7(0.20)+8(0.20)+5(0.20)+7(0.15)+7(0.10) = 1.05+1.40+1.60+1.00+1.05+0.70 |
| **Cross-domain bonus** | | **+0.5** | Mechanobiology (biophysics/materials science + cell biology) → Epigenomics (genomics/molecular biology): 2+ disciplinary boundaries |
| **Composite (final)** | | **7.30** | |

---

### Hypothesis: C1-H4 — Stiffness-Induced Enhancer H3K27ac Creates Self-Sustaining Transcriptional Condensates That Persist as Mechanical Memory

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 7 | Critic confirmed "PASSES — specific feedback loop mechanism for mechanical memory is novel." Yang 2014 demonstrated mechanical memory in MSCs but not at enhancer resolution, and without a molecular mechanism. Proposing that H3K27ac → BRD4 condensate → eRNA → condensate reinforcement is the storage mechanism at enhancers is a new framing. No paper combines mechanical memory + transcriptional condensates + enhancer-level readout. |
| Mechanistic Specificity | 20% | 5 | Names specific components (H3K27ac, BRD4, P-TEFb, eRNAs, EP300, HDAC) and specific perturbants (JQ1, A-485, actinomycin D). However, the mechanistic core — "self-sustaining" condensate — lacks a specified bistability mechanism. With H3K27ac half-life of 2–6h and eRNA half-life of 5–30 min, the proposed 24–72h persistence has no quantitative explanation. Revising to 6–12h short-term memory (Critic's recommendation) still leaves the positive feedback architecture underspecified. |
| Testability | 20% | 8 | Critic called this "excellent time-course design with JQ1 perturbation." The experimental protocol is well-constructed: 50 kPa (7d) → 1 kPa transfer + H3K27ac ChIP-seq + GRO-seq + YAP IF time-course. JQ1/A-485 applied at transfer cleanly tests condensate-dependent vs. condensate-independent memory. Actinomycin D test for eRNA-dependent maintenance is elegant. Fully feasible in 3 months. |
| Groundedness | 20% | 4 | Critic revised groundedness from 5 to 5, but the quantitative mismatch between H3K27ac turnover (2–6h) and proposed persistence (24–72h) actively undermines the central claim. Even revised to 6–12h, the mechanism lacks a quantitatively verified self-sustaining loop. Henninger 2021 verified but showed RNA broadly, not eRNAs specifically. Yang 2014 journal uncertain (Nat Materials vs Science). ~50% of claims verifiable, but the core mechanistic claim is quantitatively challenged. |
| Cross-Domain Creativity | 15% | 6 | The condensate-as-memory metaphor productively bridges soft matter physics (phase separation dynamics, persistence in condensates) with epigenetic memory (H3K27ac inheritance) and mechanobiology (stiffness stimulus). Less conceptually original than H3 because the phenomenon (mechanical memory) was already documented by Yang 2014 — this proposes a molecular mechanism rather than a new connection. Still a meaningful synthesis across condensate biology, epigenomics, and mechanobiology. |
| Practical Impact | 10% | 7 | Mechanical memory is clinically and biotechnologically important: cancer cells with durotactic history behave differently, and tissue engineering protocols could exploit mechanical pre-conditioning. Identifying the enhancer-level molecular mechanism of memory would be a landmark finding with implications for re-programming stiffness-exposed cells. |
| **Composite (raw)** | | **6.05** | 7(0.15)+5(0.20)+8(0.20)+4(0.20)+6(0.15)+7(0.10) = 1.05+1.00+1.60+0.80+0.90+0.70 |
| **Cross-domain bonus** | | **+0.5** | Mechanobiology (biophysics) → Epigenomics (molecular biology/condensate biology): 2+ disciplinary boundaries |
| **Composite (final)** | | **6.55** | |

---

### Hypothesis: C1-H5 — ECM Stiffness Rewires Enhancer-Promoter 3D Chromatin Loops via YAP-TEAD-Dependent NIPBL Recruitment and Cohesin Redistribution

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 5 | Critic assessed "MODERATE — HiChIP data under stiffness would be novel; mechanism is obvious inference." The experimental data gap is real and significant (no HiChIP under ECM stiffness exists). However, the mechanism — active enhancers recruit cohesin loader → more loops — is a direct logical inference from Kagey 2010 and Dupont 2011. The novelty is empirical, not conceptual. Score reflects: novel data, not novel mechanism. |
| Mechanistic Specificity | 20% | 5 | Names specific proteins (YAP, TEAD, EP300, BRD4, NIPBL, cohesin), specific published interactions (Kagey 2010, Olley 2018), and a detailed 6-step cascade. However, the 6-step cascade is both its strength and weakness: each step introduces uncertainty, and the BRD4-NIPBL interaction may be CdLS-specific. CTCF boundary dominance means the proposed mechanism may operate in the margins of loop architecture. |
| Testability | 20% | 8 | Critic confirmed "PASSES — HiChIP well-designed with perturbation panel." H3K27ac HiChIP on PA hydrogels with siNIPBL, JQ1, and verteporfin is a clean, feasible experiment with unambiguous outcomes. The data would be valuable regardless of whether the proposed mechanism is correct, because no HiChIP under stiffness gradients exists. |
| Groundedness | 20% | 4 | Critic assessed "45% — 4.5/9 claims verifiable." BRD4-NIPBL is partially grounded (Olley 2018, may be CdLS-specific). ECM stiffness → cohesin redistribution chain is parametric. Rao 2017 auxin data shows CTCF-determined loop positions are genetically robust to perturbation — this is active counter-evidence against the efficacy of the proposed mechanism. |
| Cross-Domain Creativity | 15% | 5 | The bridge from ECM stiffness to 3D genome architecture is conceptually interesting (biophysics → structural genomics), but the mechanism is mechanical in the sense of "trivially follows from premises." A graduate student knowing Kagey 2010 (NIPBL at enhancers) + Dupont 2011 (YAP on stiff substrates) could predict this. The cross-domain creativity score reflects structural novelty without conceptual originality. |
| Practical Impact | 10% | 6 | 3D genome architecture is fundamental to gene regulation. Demonstrating stiffness-dependent loop rewiring would add a new layer to mechanogenomics and could explain how physical signals in tumors alter gene regulatory circuits. But CTCF dominance limits the magnitude of the effect, reducing expected impact. |
| **Composite (raw)** | | **5.50** | 5(0.15)+5(0.20)+8(0.20)+4(0.20)+5(0.15)+6(0.10) = 0.75+1.00+1.60+0.80+0.75+0.60 |
| **Cross-domain bonus** | | **+0.5** | Mechanobiology (biophysics) → Structural genomics/3D epigenomics (molecular biology): 2+ disciplinary boundaries |
| **Composite (final)** | | **6.00** | |

---

### Hypothesis: C1-H1 — ECM Stiffness Nucleates Mechanosensitive Super-Enhancers via YAP-Dependent BRD4/MED1 Phase Condensate Assembly

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 4 | Critic identified a direct precedent: Zanconato et al. Nat Med 2018 established YAP/TAZ → BRD4 → super-enhancers in cancer. H1 adds only the ECM stiffness upstream trigger. Critic labeled this "PARTIAL KILL" on novelty — the connection is a one-hop extension. Mitigating factor: the stiffness-specific super-enhancer ChIP-seq gap is real (0 papers). Score reflects substantial prior art with a real data gap. |
| Mechanistic Specificity | 20% | 5 | Names specific molecules (YAP, BRD4, MED1, EP300, H3K27ac), specific concentrations (BRD4 phase separation ~5–10 µM), specific techniques (ChIP-seq, ROSE algorithm, JQ1). However, BRD4 phase separation model is contested (McSwiggen eLife 2019; Chong Science 2018), Sabari 2018 showed MED1 not BRD4 condensates (misattribution), and EP300 kcat is unverified in vivo. Phase separation threshold claim is the mechanism's core and it's the most contested piece. |
| Testability | 20% | 8 | ChIP-seq + ATAC-seq + RNA-seq on MCF10A across stiffness gradient with ROSE super-enhancer calling is a fully specified, feasible protocol. JQ1 perturbation provides clean mechanistic validation. TEAD motif enrichment analysis is analytically established. This is the most technically straightforward experiment of the cohort — a PhD student could execute this in 3 months. |
| Groundedness | 20% | 4 | Critic assessed ~50% grounded (4/8 core claims verifiable). Zanconato 2018 overlap reduces novelty but increases groundedness of the YAP→super-enhancer chain. The misattribution (Sabari 2018 = MED1 not BRD4) and contested phase separation model create a groundedness ceiling. YAP-BRD4 co-occurrence (31 PubMed papers) partially verifies the connection without resolving the phase separation claim. |
| Cross-Domain Creativity | 15% | 5 | The ECM stiffness → super-enhancer bridge is conceptually interesting (biophysics → transcriptional regulation), but the creative contribution is limited because it follows the YAP pathway mechanically from Dupont 2011 through Zanconato 2018 to a new upstream input. The phase separation metaphor adds some creative framing but relies on contested biology. Score reflects a straightforward extension of existing cross-domain thinking. |
| Practical Impact | 10% | 6 | Super-enhancers are disproportionately amplified in cancer and control cell identity genes. Linking stiffness-driven super-enhancer nucleation to tumor microenvironment stiffness and cancer progression is biomedically significant. Impact limited by the incremental nature of the mechanistic claim relative to Zanconato 2018. |
| **Composite (raw)** | | **5.35** | 4(0.15)+5(0.20)+8(0.20)+4(0.20)+5(0.15)+6(0.10) = 0.60+1.00+1.60+0.80+0.75+0.60 |
| **Cross-domain bonus** | | **+0.5** | Mechanobiology (biophysics) → Transcriptional epigenomics (molecular biology): 2+ disciplinary boundaries |
| **Composite (final)** | | **5.85** | |

---

### Hypothesis: C1-H6 — Tissue-Specific ECM Stiffness Selects Tissue-Specific Enhancer Programs Through Differential YAP Nuclear Residence Time and EP300 Occupancy Kinetics

| Dimension | Weight | Score (1–10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 15% | 5 | The stiffness-as-morphogen framing and kinetic selection model are genuinely novel framings. No prior paper proposes EP300 residence time as the selection mechanism for enhancer cohort activation under stiffness. However, Critic notes this concept is "novel because wrong" — the morphogen analogy fails structurally. The modest reframe (hierarchical TEAD enhancer activation at different stiffnesses) is likely real but significantly less exciting. |
| Mechanistic Specificity | 20% | 4 | The kinetic model (YAP dwell time → EP300 occupancy kinetics → threshold-dependent activation) is well-articulated conceptually, but the fatal flaw — YAP-TEAD targets are shared proliferation/survival genes, not tissue-specific enhancers — means the stated mechanism cannot explain the claimed outcome (tissue-specific selection). Lineage TFs (MYOD, RUNX2, PPARγ) are required for tissue identity and are absent from the mechanism. A specific mechanism that leads to the wrong place scores poorly. |
| Testability | 20% | 7 | The experimental design is feasible: hMSCs on 5 stiffness points, H3K27ac ChIP-seq, TEAD motif analysis, ENCODE/Roadmap comparison. However, Critic flags that prediction (d) — stiffness profiles match tissue profiles — is likely false, reducing the value of the experiment. The simpler version (hierarchical TEAD enhancer activation) is testable and would likely yield positive data, but it tests a weaker hypothesis than stated. |
| Groundedness | 20% | 3 | Critic revised groundedness from 5 to 4. The conceptual flaw is not just a gap but an active contradiction: MSCs on stiff substrates without supplements show minimal differentiation, and YAP inhibits adipogenesis, directly opposing the tissue-specificity claim. Elosegui-Artola 2017 and Engler 2006 are well-grounded, but the hypothesis uses them to support a conclusion (tissue-specific enhancer selection) that they don't actually support. Levental 2007 journal uncertain. ~45% claims verifiable, but the verifiable claims don't support the core prediction. |
| Cross-Domain Creativity | 15% | 5 | The morphogen analogy imports a concept from developmental biology (Turing morphogens, French flag model) into mechanobiology and epigenomics. This is a creative cross-domain import. However, the import fails structurally because morphogens generate qualitatively different programs across a gradient, while YAP generates quantitatively graded output of the same program. The creative intent is visible but the execution has a category error. |
| Practical Impact | 10% | 5 | If a modest version is confirmed (hierarchical TEAD enhancer activation at physiological stiffness values), this would provide an enhancer-level framework for understanding stiffness-directed differentiation — useful for tissue engineering. But the full version (tissue-specific enhancer selection) is likely false, capping impact. |
| **Composite (raw)** | | **4.80** | 5(0.15)+4(0.20)+7(0.20)+3(0.20)+5(0.15)+5(0.10) = 0.75+0.80+1.40+0.60+0.75+0.50 |
| **Cross-domain bonus** | | **+0.5** | Mechanobiology (biophysics) → Epigenomics (molecular biology/developmental biology): 2+ disciplinary boundaries |
| **Composite (final)** | | **5.30** | |

---

## Final Ranking Table

| Rank | ID | Title | Novelty | Mech | Test | Ground | X-Dom | Impact | Raw | Bonus | **Final** |
|------|-----|-------|---------|------|------|--------|-------|--------|-----|-------|-----------|
| 1 | C1-H3 | Dual-Enzyme Bivalent-to-Active Enhancer Switch (KDM6B + EP300) | 7 | 7 | 8 | 5 | 7 | 7 | 6.80 | +0.5 | **7.30** |
| 2 | C1-H4 | Mechanical Memory via H3K27ac Condensate Feedback | 7 | 5 | 8 | 4 | 6 | 7 | 6.05 | +0.5 | **6.55** |
| 3 | C1-H5 | Enhancer-Promoter 3D Loop Rewiring via NIPBL/Cohesin | 5 | 5 | 8 | 4 | 5 | 6 | 5.50 | +0.5 | **6.00** |
| 4 | C1-H1 | Super-Enhancer Nucleation via YAP-BRD4 Phase Condensates | 4 | 5 | 8 | 4 | 5 | 6 | 5.35 | +0.5 | **5.85** |
| 5 | C1-H6 | Tissue-Specific Stiffness Selects Enhancer Programs via YAP Dwell Time | 5 | 4 | 7 | 3 | 5 | 5 | 4.80 | +0.5 | **5.30** |

**Note:** All hypotheses receive the +0.5 cross-domain bonus. The mechanobiology (biophysics/materials science/cell biology) → epigenomics (molecular biology/genomics) bridge spans 2+ disciplinary boundaries. Per v5.8 policy: retrieval infrastructure (PubMed, KEGG, STRING) is bio-centric, creating systematic infrastructure penalty for non-biomedical domains; but all 5 hypotheses are life sciences so the bonus normalizes the biophysics-to-molecular-biology distance.

---

## Diversity Check

**Top 3 hypotheses examined for redundancy:**

| Pair | Mechanism | Subfield target | Prediction type | Verdict |
|------|-----------|----------------|-----------------|---------|
| C1-H3 + C1-H4 | Enzymatic coordination vs. feedback condensate | Bivalent enhancer conversion vs. memory persistence | CUT&Tag histone marks vs. ChIP-seq time-course | **DISTINCT** — different phenomena, orthogonal predictions |
| C1-H3 + C1-H5 | Enzymatic coordination vs. 3D loop rewiring | Histone marks vs. chromatin topology | Combinatorial inhibition vs. HiChIP | **DISTINCT** — different level of chromatin organization |
| C1-H4 + C1-H5 | Condensate feedback vs. NIPBL-cohesin | Temporal persistence vs. spatial architecture | Memory time-course vs. loop topology | **DISTINCT** — orthogonal questions |

**Diversity verdict: PASS — No adjustment needed.**

All three top hypotheses address different aspects of the mechanobiology → epigenomics bridge:
- C1-H3 asks: *what epigenetic mark switch occurs?* (H3K27me3→H3K27ac, via dual-enzyme)
- C1-H4 asks: *does the switch persist after stiffness removal?* (condensate-based memory)
- C1-H5 asks: *does the switch rewire 3D architecture?* (cohesin/loop topology)

These three questions are scientifically complementary, not redundant. A research group could run all three in parallel without duplication.

---

## Elo Tournament Sanity Check (Top 4)

**Participants:** C1-H3, C1-H4, C1-H5, C1-H1
**Comparisons:** 4 × 3 / 2 = **6 pairwise matches**

**Format:** "Which of these two hypotheses would a domain researcher want to test FIRST, and why?"

---

**Match 1: C1-H3 vs C1-H4**
A researcher tests C1-H3 first. The dual-enzyme coordination hypothesis has no quantitative self-consistency problem — the mechanism is challenged but not internally contradicted. C1-H4's core mechanism (self-sustaining H3K27ac feedback) requires H3K27ac to persist for 24–72h with a 2–6h half-life, making it harder to motivate experimentally without first revising the timescale. **Winner: C1-H3**

**Match 2: C1-H3 vs C1-H5**
A researcher tests C1-H3 first. C1-H5 will generate valuable HiChIP data regardless of mechanism, but the mechanism is a predictable inference from existing biology. C1-H3 asks a more conceptually original question (does stiffness resolve bivalent enhancers?) with a cleaner inhibitor design and greater potential for mechanistic discovery. **Winner: C1-H3**

**Match 3: C1-H3 vs C1-H1**
A researcher tests C1-H3 first. C1-H1 extends the already-established Zanconato 2018 YAP→BRD4→super-enhancer connection. C1-H3's dual-enzyme coordination is genuinely unexplored and addresses a deeper developmental question about bivalent enhancer resolution. **Winner: C1-H3**

**Match 4: C1-H4 vs C1-H5**
A researcher tests C1-H4 first. Mechanical memory at enhancer resolution is a fundamental open question (Yang 2014 showed the phenomenon 12 years ago with no molecular mechanism identified). C1-H5's HiChIP data would be interesting but its mechanism is more predictable. The discovery potential of C1-H4 is higher if the timescale is revised. **Winner: C1-H4**

**Match 5: C1-H4 vs C1-H1**
A researcher tests C1-H4 first. C1-H1 is largely pre-empted by Zanconato 2018, making it a refinement experiment. C1-H4 addresses an open mechanistic question about a phenomenon (mechanical memory) with no current molecular explanation at enhancer resolution. **Winner: C1-H4**

**Match 6: C1-H5 vs C1-H1**
A researcher tests C1-H5 first. While both have moderate mechanism quality, C1-H5 fills a completely unstudied data gap (Hi-C/HiChIP under ECM stiffness). C1-H1 would confirm and extend Zanconato 2018, which is lower priority. The architectural question (do stiffness gradients reorganize enhancer-promoter loops?) is a higher-priority unknown. **Winner: C1-H5**

---

**Elo Standings:**

| Hypothesis | Wins | Losses | Win Rate | Elo Rank |
|------------|------|--------|----------|----------|
| C1-H3 | 3 | 0 | 1.00 | **1st** |
| C1-H4 | 2 | 1 | 0.67 | **2nd** |
| C1-H5 | 1 | 2 | 0.33 | **3rd** |
| C1-H1 | 0 | 3 | 0.00 | **4th** |

**Elo linear ranking:** H3 > H4 > H5 > H1

**Comparison with composite ranking:** Identical. **Elo confirms linear ranking.**

No divergence detected. The linear composite and pairwise tournament agree on ordering, which increases confidence in the ranking. Notably, C1-H1's strong Testability score (8) inflates its composite slightly relative to its Elo performance — researchers would not prioritize testing an already-established pathway over genuinely open questions, even if the experiment is technically easy. This is a known limitation of linear composites: high Testability alone doesn't create research priority.

---

## Evolution Selection

**Selected for Cycle 1 Evolution (post-diversity-check):** C1-H3, C1-H4, C1-H5

| Hypothesis | Final Score | Selection Rationale |
|------------|------------|---------------------|
| C1-H3 | 7.30 | Critic's strongest survivor; dual-enzyme concept is genuinely novel and testable; must revise KDM6B→UTX/KDM6A and reframe as sequential two-phase model |
| C1-H4 | 6.55 | Mechanical memory at enhancer resolution is an open 12-year-old question; must revise timescale (24–72h → 6–12h) and specify bistability mechanism or reposition as short-term bridge to DNA methylation memory |
| C1-H5 | 6.00 | Fills completely unstudied data gap (HiChIP under stiffness); must reframe as experimental prediction rather than mechanistic discovery; acknowledge CTCF dominance explicitly |

**Not selected for evolution:**
- C1-H1 (5.85): Novelty pre-empted by Zanconato 2018; phase separation model contested; marginal value over existing biology. May be worth reformulating without phase separation as a Cycle 2 hypothesis if MRTF-SRF suggestion is explored.
- C1-H6 (5.30): Conceptual flaw (YAP-TEAD targets are not tissue-specific) is too fundamental to evolve productively. The modest reframe (hierarchical TEAD enhancer activation) is probably correct but unexciting. Not worth evolution slot.

**Priority critic questions to address in evolution:**
- C1-H3: Reformulate with UTX as primary/alternative; sequential two-phase model
- C1-H4: Revise timescale; specify bistability or reposition as bridge to DNA methylation
- C1-H5: Acknowledge triviality; reframe as dataset hypothesis; address CTCF dominance
- NEW (Critic suggestion): MRTF-SRF as a second independent enhancer program activated by ECM stiffness — potential Cycle 2 hypothesis generated during evolution
