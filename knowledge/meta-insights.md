# MAGELLAN Meta-Insights (Cumulative)
Updated: 2026-03-22 after Session 008
Based on 8 sessions, ~119 hypotheses generated, ~43 passed Quality Gate

---

## Strategy Performance (all sessions)

| Strategy | Sessions | Targets produced | Hyps generated | Survived critique | Passed QG | QG pass rate | Avg composite |
|---|---|---|---|---|---|---|---|
| network_gap_analysis | 006, 007, 008 | 3 | 41 | 25 | 16 | 39% | 6.92 |
| scale_bridging | 005 | 1 | 14 | 8 | 4 | 29% | 6.75 |
| recent_breakthrough_radiation | 004 | 1 | 15 | 5 | 2 | 13% | ~6.0 |
| implicit_disjoint (sessions 001–002) | 001, 002 | 2 | ~20 | ~7 | ~7 | ~35% | ~7.0 |
| contradiction_mining | 006 (as secondary) | — | — | — | — | — | — |
| evolutionary_conservation_gap | 006 (as secondary) | — | — | — | — | — | — |
| dimensional_mismatch | 006 (as secondary) | — | — | — | — | — | — |

**Recommendation for Scout**: Prioritize `network_gap_analysis` — 39% QG pass rate across 3 sessions (16/41 generated), far exceeding all other strategies. It identifies fields with zero cross-citations but genuinely shared small-molecule chemistry (GSH/iron/lipid aldehydes in S006; iron/NAD+/NADH/ROS in S007; Cu/Fe-S/sulfide in S008). `scale_bridging` is second-best (29%) for geochemistry-biology pairs. `recent_breakthrough_radiation` has the lowest QG pass rate (13%) — use only when the technique is genuinely new (< 2 years) and the biological target is in active need of measurement tools. **CAUTION**: network_gap_analysis has been primary strategy for 3 consecutive sessions (S006-S008). Future sessions MUST force-select an alternative strategy to build empirical data.

---

## Disjointness vs Outcome (all sessions)

| Disjointness | Sessions | Targets selected | Hyps survived | QG passed | Rate |
|---|---|---|---|---|---|
| DISJOINT | 001, 002, 004, 005, 006, 007, 008 | 8 | ~44 | ~37 | ~84% |
| PARTIALLY_EXPLORED | 001, 002, 004, 005 | 0 selected | — | — | — |
| PARTIALLY_CONNECTED | 005 | 0 selected | — | — | — |

Note: PARTIALLY_EXPLORED targets have been identified but never selected across 8 sessions. All selected targets have been DISJOINT.

**Recommendation for Scout**: DISJOINT preference is strongly confirmed across 8 consecutive successes. The pattern "DISJOINT by citation/pathway analysis but connected by shared small-molecule chemistry" is the most productive target profile. Reject targets classified PARTIALLY_EXPLORED unless no DISJOINT candidates of sufficient quality are found.

---

## Bridge Type Performance (all sessions)

| Bridge Type | Sessions | Used | Survived | QG Passed | Survival Rate | Notes |
|---|---|---|---|---|---|---|
| Published unmeasured variable (gap paper) | 007 | 1 | 1 | 1 | 100% (PASS 8/10) | Nadimpalli 2024 identified IRP1 cluster occupancy as unmeasured → H2.1. Highest-quality bridge type yet |
| Indirect enzymatic cascade (multi-step biochemical) | 001, 006 | 8+ | 8+ | 6+ | ~100% | V-ATPase chain (S1), PYO→GSH→GPX4 chain (S6) |
| Mathematical topology constraints | 002 | 3 | 3 | 3 | 100% | Poincare-Hopf gives necessary predictions |
| Vibronic/phonon coupling (phonon-exciton) | 004 | 3 | 3 | 2 | 100% | Best performer in quantum biology domain |
| Quantitative thermodynamic framework (Pourbaix) | 005 | 1 | 1 | 1 | 100% | Elegant but kinetics can override thermodynamics |
| Tool transfer (PHREEQC geochemistry model) | 005 | 1 | 1 | 1 | 100% | High novelty but biological constraints must be checked |
| Nanoparticle dissolution kinetics analogy | 005 | 1 | 1 | 1 | 100% | Clean mineral-to-cell comparison |
| Radical regioselectivity contrast (enzymatic vs abiotic) | 005 | 1 | 1 | 1 | 100% | Textbook chemistry on both sides |
| pH/ion microdomains as molecular effectors | 001 | 4 | 4 | 4 | 100% | Works because pH/ions couple broadly |
| Quantitative scavenging budget (mass-balance feasibility) | 006 | 1 | 1 | 1 | 100% | Inter-compartment signal transit feasibility |
| Electrophilic lipid modifier of receptor (covalent) | 006 | 1 | 1 | 1 | 100% (COND) | 4-HNE→LasR Michael addition; outcome uncertain |
| Tissue expression pattern → vulnerability map | 006 | 1 | 1 | 1 | 100% (COND 7/10) | Incremental extension — passes QG but low impact |
| ER-mito Ca2+ signaling at MAMs (CISD2) | 007 | 1 | 1 | 1 | 100% (COND 7/10) | Triple intersection: longevity × circadian × Fe-S. Zero publications |
| Cytoplasmic maturation pathway gate (CIA/CIAO3) | 007 | 1 | 1 | 1 | 100% (COND 7/10) | Pathway-level: ~20 proteins coordinately affected |
| Substrate supply bottleneck (frataxin/FTMT) | 007 | 1 | 1 | 1 | 100% (COND 6/10) | Tissue-specificity argument novel (FTMT absence) |
| Conservation gap with time lag (reverse direction) | 007 | 1 | 1 | 1 | 100% (COND 6/10) | 14-year Drosophila→mammalian follow-up gap |
| Enzyme saturation (Km-gated stoichiometry) | 007 | 1 | 1 | 0 | 0% | FDXR Km=0.7µM, >99% saturated. Substrate oscillation cannot gate rate |
| Non-transcriptional redox timer (Prx→H2O2) | 007 | 1 | 0 | 0 | 0% | H2O2 gap 2-3 orders of magnitude below Fe-S activation threshold |
| Species numbering error (cross-organism annotation) | 007 | 1 | 0 | 0 | 0% | H1: Cys328 E. coli IscS cited as human NFS1 regulatory residue |
| Direct electric/electromagnetic field effects | 001, 004 | 8 | 0 | 0 | 0% | Always killed: energy scale mismatch |
| Quantum entanglement/information storage | 004 | 3 | 0 | 0 | 0% | Decoherence in biology is fatal |
| Fröhlich condensates | 004 | 2 | 0 | 0 | 0% | Thermodynamically impossible at 300K |
| Abiotic PUFA synthesis (FTT route) | 005 | 2 | 0 | 0 | 0% | Fatal: Fischer-Tropsch doesn't make PUFAs |
| Homogeneous Fenton at wrong pH | 005 | 2 | 0 | 0 | 0% | Fatal: pH 10 (serpentinization) ≠ pH 7.2 (cell) |
| Vocabulary re-description | 002, 005 | 2 | 0 | 0 | 0% | No predictive power added |
| Thermodynamic displacement (Irving-Williams/Ksp) | 008 | 1 | 1 | 1 | 100% (PASS 8.1/10) | Cu(I)→Fe-S displacement via 29-order Ksp driving force. CIA/LIAS differential rescue prediction. Cross-model HIGH PRIORITY |
| Electrochemical potential matching (Pourbaix/Eh-pH) | 008 | 1 | 1 | 1 | 100% (COND 7.3/10) | FDX1 E0' at Cu²⁺/Cu⁺ boundary. Needs separation-of-function experiment (LplA bypass) |
| Evolutionary co-selection (genomic signatures) | 008 | 1 | 1 | 1 | 100% (COND 5.2/10) | Weakly motivated causal geochemistry; needs phylogenetic triage first |
| Ligand homology (molecular fossil) | 008 | 1 | 1 | 1 | 100% (COND 5.4/10) | Dithiolane ring-strain prediction testable by DFT + ITC |
| Phase formation (nanoparticle at insufficient concentration) | 008 | 2 | 1 | 0 | 50% | H1.3 survived as CuS sink (oscillator rejected by Bendixson); H1.6 killed (CuS-Fenton not novel) |
| Chemical identity prediction (spectroscopic counter-evidence) | 008 | 1 | 0 | 0 | 0% | H1.5 killed by NMR data from Cobine JBC 2006 — CuL has aromatic features incompatible with dithiolane |
| Novel bacterial receptor for proposed ligand (no known family) | 006 | 1 | 0 | 0 | 0% | Kill: H2.4 — no precedent for bacterial phospholipid sensing |

**Recommendation for Generator**:
- **Use**: Published unmeasured variable bridges (highest quality). Indirect multi-step enzymatic cascades. Quantitative mass-balance frameworks (scavenging budgets, speciation, Pourbaix). Mathematical necessity arguments (topology). Vibronic coupling in structured protein environments.
- **Avoid**: Direct field effects. Quantum entanglement in biology. Any bridge requiring a novel receptor with no known homolog. pH conditions incompatible with the target organism. Vocabulary re-description. Cross-species protein annotation errors.
- **New rule (Session 006)**: Before proposing a bacterial sensing mechanism, verify that a receptor family for the proposed ligand class exists in the target organism's genome.
- **New (Session 007)**: "Published unmeasured variable" bridges — when a recent paper explicitly identifies a gap (e.g., Nadimpalli 2024 noting IRP1 cluster occupancy unmeasured over 24h) — are the highest-quality bridge type. The resulting hypothesis is pre-grounded.
- **New (Session 007)**: Triple-intersection bridges (3 normally separate fields converging on one molecule) produce highest novelty but carry higher parametric error risk. Verify all quantitative parameters independently.
- **New (Session 008)**: Thermodynamic displacement bridges using Ksp/Irving-Williams series produce the highest QG scores (8.1/10) when grounded in well-characterized equilibrium constants. Geochemical quantitative frameworks (Pourbaix, speciation diagrams) are powerful when applied to biology for the first time.
- **New (Session 008)**: Generator self-critique flagging "decorative" framing should be a hard gate — if the geochemical connection is ornamental rather than mechanistically necessary, do not include the hypothesis.
- **Avoid (Session 007)**: Enzyme Km-gated mechanisms where Km << [S] — the enzyme is saturated and substrate oscillation cannot modulate its rate.
- **Avoid (Session 007)**: Cross-species protein annotation — always verify residue numbering matches target organism, not homologs.
- **Avoid (Session 008)**: Proposing chemical identity predictions (e.g., "CuL = lipoic acid") without first checking published spectroscopic data. H1.5 was killed by existing NMR evidence.
- **Avoid (Session 008)**: Proposing novelty for well-studied environmental chemistry reactions (CuS-Fenton). QG novelty search caught what Critic missed.

---

## Kill Pattern Distribution (all sessions, cumulative)

Estimated from all documented kills across sessions 001–008.

| Kill Reason | Estimated count | Approx % | Sessions |
|---|---|---|---|
| Energy scale mismatch (thermal overwhelm, too weak) | 14 | 21% | 001, 004 dominant |
| Substrate/condition mismatch | 8 | 12% | 005 dominant |
| Quantitative impossibility (Km saturation, concentration gap) | 8 | 12% | 005, 007, 008 (H1.6 H2O2 concentration gap) |
| Classical explanation sufficiency (simpler mechanism exists) | 6 | 9% | 001, 002, 004 |
| Mechanism fabrication (no known receptor/enzyme/pathway) | 5 | 8% | 002, 006 |
| Thermodynamic impossibility (wrong redox potential) | 4 | 6% | 007 (CISD2 midpoint), 005 |
| Citation hallucination / unverifiable reference | 3 | 5% | 004 |
| Mathematical invalidity | 3 | 5% | 002 |
| Scope overreach / universal claim | 3 | 5% | 002 |
| Novelty failure (well-studied in another domain) | 2 | 3% | NEW (008) - H1.6 CuS-Fenton extensively characterized in environmental chemistry |
| Vocabulary re-description | 2 | 3% | 002, 005 |
| Spectroscopic counter-evidence (published NMR/EXAFS/etc.) | 1 | 2% | NEW (008) - H1.5 CuL identity contradicted by Cobine JBC 2006 NMR |
| Partial novelty reduction (prior work partially covers) | 1 | 2% | 006 (H2.3 COND) |
| Species numbering error (cross-organism annotation) | 1 | 2% | 007 - H1 Cys328 E. coli ≠ human NFS1 |
| Pathway direction error | 1 | 2% | 007 - H7 AMPK→CRY1 not BMAL1→AMPK |
| Dependency cascade | 1 | 2% | 007 - H5 killed because dependent on H1 |
| Oscillator model mathematically impossible | 1 | 2% | NEW (008) - H1.3 Bendixson criterion rejects limit cycle (Gemini proof) |

**Recommendation for Generator**:
1. **Thermal energy pre-screen**: For any quantum or physical mechanism, compute kT (26 meV at 300K) vs proposed effect BEFORE writing the hypothesis.
2. **Substrate compatibility check**: Verify conditions in Field A can exist in Field C (pH, temperature, available substrates). Serpentinization pH 10 does not transfer to pH 7.2 cells.
3. **Receptor existence check (NEW from Session 006)**: Before proposing a novel sensing or receptor mechanism in bacteria (or any organism), verify a receptor family for the ligand class exists.
4. **Back-of-envelope self-consistency**: All calculations in SELF-CRITIQUE must be internally consistent. ~40x numerical errors have been caught only at Quality Gate.
5. **Classical alternative**: Before proposing any exotic mechanism, verify classical biochemistry cannot explain the observation.
6. **Citation journal verification**: Verify journal name, not just author/year. Journal attribution errors recur but content has been accurate — this is a low-severity but recurring issue.
7. **Scope limitation**: Restrict claims to specific systems where assumptions hold. Avoid "all tissues", "universal", "every bacterium" constructions.
8. **Km pre-verification (NEW from Session 007)**: Before proposing any enzyme-gated mechanism, verify the Km relative to physiological substrate concentration. If Km << [S], the enzyme is saturated and substrate oscillation cannot gate its activity. H2.5 FDXR Km=0.7µM vs NADPH ~50-100µM → >99% saturated, <1% rate change.
9. **Redox midpoint verification (NEW from Session 007)**: Before building a redox-cycling mechanism, verify the redox midpoint of the specific protein isoform (not a homolog). H2.3 used mitoNEET/CISD1 midpoint for CISD2 — different proteins with different potentials.
10. **Correctable vs structural errors (NEW from Session 007)**: Distinguish between structural impossibility (mechanism cannot work under any parameters) and parametric errors (mechanism works with corrected values). Only structural impossibilities warrant FATAL kills.
11. **Species annotation verification (NEW from Session 007)**: Always verify protein residue numbering matches target organism. Cross-species annotation errors (E. coli IscS Cys328 ≠ human NFS1) are a new failure mode.

---

## Session Performance History

| Session | Target | Hyps gen | Critique survival | QG passed | QG pass rate | Kill rate @ QG | Status |
|---|---|---|---|---|---|---|---|
| 001 | Bioelectric x Condensates | ~8 | ~4 | 4 | 50% | ~50% | SUCCESS |
| 002 | Active matter x Stem cells | ~12 | ~3 | 3 | 25% | ~75% | SUCCESS |
| 003 | (targeted, early session) | — | — | — | — | — | — |
| 004 | THz spectroscopy x Quantum coherence | 15 | 5 | 2 | 13% | 67% | SUCCESS |
| 005 | Ferroptosis x Serpentinization | 14 | 8 | 4 | 29% | 50% | SUCCESS |
| 006 | Ferroptosis x Quorum sensing | 14 | 9 | 6 | 43% | 0% | SUCCESS |
| 007 | Fe-S cluster biogenesis x Circadian clock | 15 | 10 | 5 | 33% | 17% | SUCCESS |
| 008 | Cuproptosis x Vent Cu-S Geochemistry | 12 | 10 | 5 | 42% | 17% | SUCCESS |

**Trend**: QG pass rate shows sustained high performance — 13% (S4) → 29% (S5) → 43% (S6) → 33% (S7) → 42% (S8). Session 008 returns to the S006 high-water mark. Kill rate stable at 17% (same as S007). The pipeline is in a mature operating regime with 33-43% QG pass rate and 17% kill rate.

---

## Cross-Model Validation Patterns (Sessions 4–8)

### GPT vs Gemini Divergence
- **Gemini** consistently scores mathematical/structural correctness highly (8–10/10)
- **GPT** consistently scores biological plausibility and practical utility (2–6/10)
- **Divergence is largest** when math is sound but biology is domain-irrelevant (S8 H1.7: GPT 2 vs Gemini 8)
- **Divergence is smallest** when both chemistry AND biology are well-grounded (S5 H2.1, S7 H2.1, S8 H1.4)
- **New (S8)**: Gemini can provide formal mathematical proofs that kill hypotheses (Bendixson criterion rejecting H1.3 oscillator). This is a unique strength — use Gemini for structural/mathematical falsification.

**Recommendation for Quality Gate**: When cross-model scores diverge by > 4 points (Gemini vs GPT), prioritize the GPT score for biological plausibility; investigate the Gemini score for structural/mathematical validity. A hypothesis scoring high on Gemini but low on GPT likely has correct formal structure but is biologically peripheral.

---

## Productive Bridge Concept Patterns (cumulative)

1. **Published unmeasured variable bridges** (Session 007): When recent literature explicitly identifies gaps ("X remains unmeasured", "the role of Y is unknown"), building hypotheses around these gaps produces pre-grounded, high-scoring results. Nadimpalli 2024 → IRP1 → H2.1 PASS demonstrates the pattern.
2. **Indirect enzymatic cascades** (Sessions 001, 006): Multi-step pathways through well-characterized intermediaries survive at 100%. The more named molecules in the chain, the more falsifiable — and falsifiable hypotheses score higher.
3. **pH/ion microdomains as molecular effectors** (Session 001): Works because pH and Ca2+ ions are promiscuous regulators across biological scales.
4. **Mathematical topology constraints** (Session 002): Poincare-Hopf theorem gives mathematically necessary predictions that cannot be dismissed.
5. **Vibronic coupling in structured protein scaffolds** (Session 004): Phonon-exciton coupling is established physics; the novelty comes from applying it to a new protein system.
6. **Shared mineral chemistry** (Session 005): Iron minerals (ferrihydrite, magnetite) bridge geochemistry and cell biology through identical chemical species.
7. **Tool transfer** (Session 005): Applying geochemistry computational tools (PHREEQC, Pourbaix) to biology. High novelty but requires checking biological constraints.
8. **Quantitative scavenging budget** (Session 006): Computing whether a reactive intermediate can physically traverse an extracellular space to reach its target organism, given known scavenging rates and rate constants. Applicable to any inter-kingdom or inter-compartment signaling hypothesis.
9. **Returning to identified-but-unexplored DISJOINT targets** (Session 006): Session 002 scout flagged ferroptosis x QS as high-quality but unexplored. Session 006 selected it and it delivered the best results to date. Scout should maintain a "deferred targets" queue.
10. **Thermodynamic displacement via equilibrium constants** (Session 008): When two metals compete for the same coordination site (e.g., Cu vs Fe in Fe-S clusters), the ratio of formation/solubility constants provides a quantitative, irrefutable driving force. The 29-order Ksp difference (Cu₂S vs FeS) made H1.4 the highest-scoring hypothesis. This bridge type works because the thermodynamics are identical in mineral and protein phases — only the kinetic pathway differs.
11. **Pourbaix/Eh-pH framework transfer** (Session 008): Geochemists have 50+ years of copper speciation data in Eh-pH space. Applying these frameworks to intracellular compartments (mitochondria at Eh ≈ −250 to −300 mV) is absolutely novel — zero publications found. High-value bridge for any metal-dependent biological process.

---

## Infection Biology as High-Productivity Domain (from Session 006)

Session 006 produced the highest QG pass rate (43%) and the first 10/10 rubric scores across all sessions. Key enabling factors:
- Both fields (ferroptosis, quorum sensing) have defined molecular players with published structures and kinetics
- Shared chemical intermediaries (GSH, iron, lipid aldehydes) are the same molecules in both fields
- Testability is high: P. aeruginosa QS assays, GPX4 knockdown cell lines, ferrostatin-1 rescue experiments are all standard
- One prior landmark paper (Dar et al. 2018) provides an anchor — novel hypotheses can position explicitly relative to it

**Recommendation for Scout**: Infection biology targets (host cell death pathway x bacterial virulence mechanism) should be considered high-priority candidates when they share a defined metabolic intermediate.

## Cuproptosis-Geochemistry as High-Productivity Domain (NEW from Session 008)

Session 008 explored cuproptosis × hydrothermal vent Cu-S geochemistry and achieved 42% QG pass rate with the session's highest individual score (8.1/10). Key enabling factors:
- **Quantitative thermodynamic framework**: Ksp values, Irving-Williams series, Pourbaix diagrams provide numerical predictions that are irrefutable and testable
- **Well-characterized molecular targets**: FDX1, LIAS, DLAT, ISCA1/ISCA2 — all with published structures, kinetics, and knockout phenotypes
- **Geochemistry precision**: 50+ years of Cu-S speciation data (chalcopyrite, covellite, Cu⁺/Cu²⁺ equilibria) transferable to biology
- **Cross-model validation**: Both GPT and Gemini confirmed the thermodynamic bridge is mathematically valid (formal isomorphism of Nernst/mass-action equations)
- **Clean falsifiability**: CIA vs LIAS differential rescue, FDX1-KO + LplA bypass, ferrozine Fe²⁺ release — all standard biochemistry

**Recommendation for Scout**: Metal-dependent cell death pathways paired with geochemical mineral chemistry are high-productivity targets when shared equilibrium constants provide quantitative bridges. The "biology meets geology" pattern (also S005 ferroptosis × serpentinization) consistently produces well-grounded hypotheses.

## Fe-S Cluster Biology as High-Productivity Domain (NEW from Session 007)

Session 007 explored Fe-S cluster biogenesis × circadian regulation and achieved 33% QG pass rate with unprecedented bridge type quality. Key enabling factors:
- **Rich molecular infrastructure**: NFS1, ISCU2, FDX2, frataxin, GLRX5, CIA pathway — all well-characterized with published kinetics
- **Published quantitative gaps**: Nadimpalli 2024 explicitly identifies IRP1 cluster occupancy as unmeasured over 24h cycles
- **High testability**: Native gel assays, IRP2 KO mice, Co-IP protocols, iron chelation experiments all standard
- **Active field validation**: JCI 2026 BMAL1→ATP7A→Cu→Fe-S establishes fundability while being mechanistically distinct
- **Quantitative framework**: Diurnal iron oscillation (20-50%), redox oscillation (30% NAD+/NADH), cluster half-lives (~2-4h) all compatible with 24h period

**Recommendation for Scout**: Fe-S cluster biology provides excellent molecular infrastructure for bridge concepts. When paired with regulatory fields (circadian, stress response, development), the temporal dimensions are almost completely unexplored.

---

## Critical Screening Rules (for Generator — cumulative)

1. **Thermal energy pre-screen**: For quantum/physical mechanisms, compute kT (26 meV @ 300K) comparison BEFORE proceeding. 30% of all kills trace to this failure.

2. **Substrate/condition compatibility**: Verify conditions in Field A actually exist or can be replicated in Field C. Serpentinization pH ≠ cytoplasmic pH. Check BEFORE writing.

3. **Receptor existence check (NEW S6)**: Before proposing a sensing or receptor mechanism, verify a receptor family for the ligand class exists in the target organism. H2.4 was killed for proposing bacterial phospholipid sensing with no known receptor.

4. **Quantitative scavenging budget (NEW S6)**: For inter-kingdom or inter-compartment signaling hypotheses involving reactive small molecules, compute the mass-balance: how much intermediate survives scavenging to reach the target compartment?

5. **Biological effect-size comparison**: Compare proposed mechanism's effect size to known dominant regulators. If GPX4/ACSL4 dominate by 100-fold, a 3-fold speciation effect is biologically minor.

6. **Geochemical/field specificity**: When claiming a connection to a specific setting, ensure bridge concepts are diagnostic for that setting, not generic.

7. **Citation verification**: Every [GROUNDED] claim must have a verifiable citation. Verify journal names, not just author/year.

8. **Classical alternative check**: Before proposing exotic mechanisms, verify classical biochemistry cannot explain the observation.

9. **Scope limitation**: Avoid universal claims. Restrict to specific systems where assumptions hold.

10. **Back-of-envelope self-consistency**: Self-critique calculations must match stated log K values and concentrations. Numerical inconsistencies (~40x errors) have slipped through before.

11. **Incremental extension check (NEW S6)**: Hypotheses of the form "X expression level determines susceptibility to known mechanism Y" consistently score as incremental (7/10 at QG). Apply higher novelty threshold — does the hypothesis reveal a new mechanism, or just map a known one to a new tissue/context?

12. **Published gap exploitation (NEW S7)**: Search for recent reviews that explicitly identify "unmeasured variables" or "open questions" — these produce the highest-quality bridge concepts.

13. **Species annotation verification (NEW S7)**: Always verify protein residue numbering matches target organism. Cross-species errors (E. coli → human) are an emerging failure mode.

14. **Enzyme kinetics pre-check (NEW S7)**: Before proposing enzyme-gated mechanisms, verify Km vs [substrate]. If Km << [S], enzyme is saturated and substrate oscillation cannot gate rate.

15. **Decorative framing gate (NEW S8)**: If Generator self-critique identifies that the cross-field connection is ornamental ("decorative") rather than mechanistically necessary, do NOT include the hypothesis. H1.5 self-critique flagged vent chemistry as decorative but was still generated — this is a quality failure.

16. **Novelty pre-check in adjacent domains (NEW S8)**: Before proposing a reaction mechanism as novel, check whether it is well-studied in an adjacent domain (e.g., CuS-Fenton in environmental remediation). QG novelty search caught H1.6 but the Generator should pre-screen.

17. **Spectroscopic data pre-check (NEW S8)**: Before proposing a molecular identity or structural prediction, check for existing spectroscopic data (NMR, EXAFS, X-ray) that could immediately contradict it. H1.5 was killed by published NMR from Cobine 2006.

18. **Oscillator/limit cycle pre-check (NEW S8)**: Before proposing any oscillatory or feed-forward loop mechanism, verify Bendixson/Dulac criteria. If Jacobian trace is negative, no limit cycle can exist. Gemini formally proved H1.3 cannot oscillate.

---

## Unexplored High-Quality Targets (Scout queue)

From prior session scouting — all classified DISJOINT and identified but not yet explored:

| Target pair | Identified in | Strategy used | Scout confidence | Notes |
|---|---|---|---|---|
| Circadian x Neurodegeneration | 001 | contradiction_mining | — | Cross-session circadian oscillation → condensate aging |
| Acoustic mechanotransduction x Tumor immune microenvironment | 001 | — | — | Piezo1 differential expression |
| Cristae remodeling x Synaptic plasticity | 002 | — | — | MICU1 gating threshold |
| Mitochondrial hormesis x Cellular aging hallmarks | 004 | contradiction_mining | — | ROS threshold switching |
| Piezoelectric collagen x HSC fate decisions | 006 | contradiction_mining + dimensional_mismatch | 7/10 | CRITICAL CHECK: field magnitude vs Piezo1 threshold needed |
| BEV x Exosome immunomodulation | 006 | evolutionary_conservation_gap | 7/10 | Needs more specific bridge concepts before selection |
| Coral calcification x Vascular calcification | 008 | implicit_disjoint | — | Biomineralization bridge; not evaluated |

**Recommendation for Scout**: Piezoelectric Collagen x HSC is the strongest unexplored candidate from session 006 scouting (7/10), but the energy scale mismatch risk is explicitly flagged. **CRITICAL**: network_gap_analysis has been primary for 3 consecutive sessions (S006-S008). Session 009 MUST select a non-network_gap_analysis strategy as primary (e.g., implicit_disjoint, scale_bridging, contradiction_mining) to build empirical performance data on alternative strategies.

---

## Recommendations Summary

**For Scout**:
1. `network_gap_analysis` remains highest-performing (39% QG pass rate, 3 sessions) BUT has been primary for 3 consecutive sessions. **Session 009 MUST use an alternative primary strategy.**
2. Search for "gap papers" — recent reviews with explicit "unmeasured variables" or "open questions" lists (Nadimpalli 2024 pattern)
3. Maintain a deferred DISJOINT targets queue — validated by session 006 success
4. Metal-dependent cell death × geochemistry is a confirmed high-productivity domain (S005, S008)
5. Fe-S cluster biology provides excellent molecular infrastructure when paired with regulatory fields
6. Infection biology pairs with shared metabolic intermediaries remain high-productivity
7. Apply energy-scale pre-check to piezoelectric/electromagnetic targets before selection

**For Generator**:
1. Lead with quantitative thermodynamic bridges (Ksp ratios, Pourbaix boundaries, equilibrium constants) — highest QG scores
2. Exploit published gap papers — when literature identifies specific unmeasured variables, build hypotheses around them
3. Hard gate on "decorative" framing — if self-critique flags the cross-field connection as ornamental, cut the hypothesis
4. Check spectroscopic data before proposing molecular identity predictions
5. Check novelty in adjacent domains (environmental chemistry, materials science) before claiming biological novelty
6. Verify species-specific protein data — don't use E. coli numbering for human proteins
7. Enzyme kinetics pre-check — verify Km vs [substrate] before proposing rate-gating mechanisms
8. Oscillator/limit cycle pre-check — verify Bendixson criteria before proposing dynamic models
9. Distinguish structural vs parametric errors — only structural impossibilities merit abandonment
10. Indirect enzymatic cascades with named molecules maintain ~100% survival rate

**For Quality Gate**:
1. 17% kill rate stable across Sessions 007-008. Pipeline is in mature operating regime.
2. Continue quantitative rigor — back-of-envelope verification effectively discriminates
3. Independent novelty search function validated: caught CuS-Fenton (H1.6) that Critic missed
4. CONDITIONAL_PASS hypotheses should receive explicit "resolve before publication" annotations
5. Cross-model Gemini formal proofs (Bendixson criterion) are a unique kill mechanism — leverage for dynamic models