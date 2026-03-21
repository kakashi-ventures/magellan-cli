# Ranked Hypotheses — Cycle 1

**Session**: 2026-03-21-scout-007
**Domain**: Fe-S cluster biogenesis × Circadian clock regulation
**Ranker model**: Opus 4.6
**Hypotheses scored**: 4 (H2, H3, H4, H8)

---

## Scoring Dimensions & Weights

| Dimension | Weight | What it measures |
|---|---|---|
| Novelty | 15% | How new is this connection? Prior work? |
| Mechanistic Specificity | 20% | Named molecules, rates, concentrations? |
| Testability | 20% | Can this be tested in 6-12 months? Available tools? |
| Groundedness | 20% | How much is literature-verified vs speculative? |
| Impact | 15% | If true, what changes? New therapy? New understanding? |
| Resilience | 10% | How well does it survive counter-evidence? |

---

## Final Rankings

### Rank 1: H4 — IRP1 [4Fe-4S] Cluster Occupancy as Mechanistic Driver of Diurnal IRE-mRNA Control
**Composite: 7.40**

| Novelty | Specificity | Testability | Groundedness | Impact | Resilience |
|---|---|---|---|---|---|
| 6 | 8 | 9 | 8 | 6 | 6 |

**Key strength**: Highest groundedness (8) and testability (9) of the entire set. The apo/holo native gel assay is cheap, fast, and immediately actionable — a single postdoc could generate publishable data in weeks. The measurement gap (nobody has tracked IRP1 [4Fe-4S] occupancy over circadian time) is robustly identified and literature-verified.

**Key weakness**: Nadimpalli 2024 attributes IRP1/IRE rhythmicity to feeding rather than the core clock, which could reduce the novelty claim. IRP2 oscillates ~10-fold vs IRP1's ~2-fold, suggesting IRP1 may play a secondary role. Impact is "filling a measurement gap" rather than opening new therapeutic territory.

**Why rank 1**: The combination of high groundedness and extreme testability makes this the safest bet for generating real data. Even if the feeding attribution partially scoops the concept, the cluster occupancy measurement itself has never been done. Low-risk, high-probability of producing a solid paper.

---

### Rank 2: H8 — Frataxin Iron Donation as Circadian Fe-S Rheostat via Hepcidin LIP
**Composite: 6.80**

| Novelty | Specificity | Testability | Groundedness | Impact | Resilience |
|---|---|---|---|---|---|
| 7 | 7 | 7 | 7 | 7 | 5 |

**Key strength**: Balanced across all dimensions — no score below 5 except resilience. All literature claims verified. Lill 2025 stoichiometry provides genuinely new mechanistic detail. The systemic (hepcidin) → mitochondrial (frataxin) → Fe-S assembly chain connects organismal iron regulation to organelle-level timing, a conceptually rich bridge. Distinct mechanism type from all other hypotheses.

**Key weakness**: Ferritin buffering may dampen LIP oscillation amplitude below biologically relevant thresholds. Mitoferrin could rate-limit independently of frataxin availability. Friedreich's ataxia carrier effect size may be too small to detect circadian phenotypes, undermining the most compelling test.

**Why rank 2**: Strong all-rounder with no fatal flaw but several compounding concerns. The ferritin buffering question is answerable experimentally but adds risk. Therapeutic implications for FA patients give it meaningful impact if validated.

---

### Rank 3: H2 — CISD2/NAF-1 as Circadian ER-Mito Calcium Timer via [2Fe-2S] Lability
**Composite: 6.70**

| Novelty | Specificity | Testability | Groundedness | Impact | Resilience |
|---|---|---|---|---|---|
| 9 | 6 | 7 | 6 | 7 | 5 |

**Key strength**: Highest novelty in the set (9) — zero publications linking CISD2 [2Fe-2S] lability to circadian calcium timing. Triple convergence of redox, pH, and Ca²⁺ signaling at the MAM is mechanistically elegant. If validated, opens an entirely new axis of circadian regulation at ER-mitochondria contact sites.

**Key weakness**: The cluster half-life (~4-6h) is estimated, not measured — the entire timing argument rests on an assumption. The NADH feedback loop introduces 3-4 untested mechanistic steps, each of which could fail independently. CISD2 KO mice have aging confounds that complicate circadian interpretation.

**Why rank 3**: The novelty is genuinely exceptional, but the mechanistic chain has too many unverified links. The estimated half-life is the load-bearing assumption, and if it's off by 2x in either direction, the circadian timing argument collapses. High ceiling, but significant execution risk.

---

### Rank 4: H3 — Peroxiredoxin Cycle as Non-Transcriptional Fe-S Clock via H₂O₂
**Composite: 5.75**

| Novelty | Specificity | Testability | Groundedness | Impact | Resilience |
|---|---|---|---|---|---|
| 8 | 5 | 6 | 5 | 7 | 3 |

**Key strength**: Compelling evolutionary logic connecting the ancient Prx redox cycle (present in archaea) to Fe-S cluster chemistry. The BMAL1 KO test (do Fe-S oscillations persist in clock-null cells?) is genuinely novel and would be transformative. Impact is high if the quantitative gap can be resolved.

**Key weakness**: Near-fatal quantitative gap — mitochondrial matrix H₂O₂ reaches ~0.15 μM during Prx3 hyperoxidation, but Fe-S cluster destruction requires >1 μM. This is nearly an order of magnitude below threshold. Additionally, mitochondrial Prx3 is resistant to hyperoxidation compared to cytosolic Prx isoforms, further weakening the mechanism. Lowest resilience score (3) reflects these compounding quantitative problems.

**Why rank 4**: The evolutionary narrative is compelling and the transformative potential is real, but the H₂O₂ concentration gap is a near-fatal flaw that cannot be hand-waved away. The hypothesis needs a quantitative rescue mechanism (local concentration amplification, sensitized Fe-S clusters, or microcompartmentation) that currently doesn't exist in the proposal.

---

## Diversity Check: **PASSED**

The top 4 hypotheses explore four mechanistically distinct pathways:

| Rank | Hypothesis | Mechanism Type | Key Axis |
|---|---|---|---|
| 1 | H4 | Post-transcriptional RNA regulation | IRP1 apo/holo → IRE binding |
| 2 | H8 | Systemic iron homeostasis | Hepcidin → LIP → frataxin |
| 3 | H2 | ER-mitochondria calcium signaling | CISD2 [2Fe-2S] → MAM Ca²⁺ |
| 4 | H3 | ROS/redox cycling | Prx hyperoxidation → H₂O₂ → Fe-S |

No two hypotheses share a primary mechanism type. The set spans post-transcriptional regulation, systemic iron trafficking, organelle contact site signaling, and redox chemistry — excellent diversity across biological scales (molecular → organelle → systemic).

---

## Elo Tournament

**Setup**: Starting Elo 1500, K-factor 32, 6 pairwise matchups.

### Matchups

**H4 vs H2**: H4 wins. Groundedness (8 vs 6) and testability (9 vs 7) decisive. Native gel assay is immediately actionable; CISD2's 3-4 untested feedback steps create execution risk.

**H4 vs H8**: H4 wins. Testability advantage (9 vs 7) and groundedness edge (8 vs 7). Ferritin buffering concern for H8 harder to resolve than feeding attribution concern for H4.

**H4 vs H3**: H4 wins clearly. H3's quantitative H₂O₂ gap (0.15 μM vs >1 μM threshold) is near-fatal. No contest on groundedness (8 vs 5).

**H2 vs H8**: H8 wins narrowly. H2 has superior novelty (9 vs 7) but H8's better groundedness (7 vs 6), verified literature, and absence of multi-step untested feedback loop give it the edge.

**H2 vs H3**: H2 wins. Zero-publication novelty and triple convergence beat H3's quantitative gap problem. H2's weaknesses are uncertainties; H3's are near-refutations.

**H8 vs H3**: H8 wins. Verified literature and distinct mechanism beat H3's threshold problem. H3's resilience (3) is the tournament's weakest.

### Elo Results

| Hypothesis | Matches | W-L | Final Elo | Elo Rank |
|---|---|---|---|---|
| H4 | 3 | 3-0 | 1548 | 1 |
| H8 | 3 | 2-1 | 1516 | 2 |
| H2 | 3 | 1-2 | 1484 | 3 |
| H3 | 3 | 0-3 | 1452 | 4 |

### Concordance: **CONFIRMED**

Elo ranking (H4 > H8 > H2 > H3) matches composite ranking exactly. No rank inversions. The linear scoring and pairwise comparison methods agree, increasing confidence in the ranking.

---

## Recommendations for Cycle 2

1. **H4** — Ready for refinement. Key question: can the feeding vs clock attribution be disambiguated with a restricted-feeding + constant-light protocol?
2. **H8** — Needs quantitative modeling of ferritin buffering dynamics to address the LIP oscillation dampening concern.
3. **H2** — Needs the cluster half-life measured or bounded more tightly. If the half-life can be experimentally constrained to 3-8h range, the hypothesis strengthens dramatically.
4. **H3** — Needs a quantitative rescue mechanism for the H₂O₂ concentration gap. Without it, evolution may not save this hypothesis.
