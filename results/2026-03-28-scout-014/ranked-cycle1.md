# Ranked Hypotheses — Cycle 1
# Session: 2026-03-28-scout-014
# Target: Non-equilibrium statistical mechanics (Mpemba effect spectral theory) x Neurodegenerative protein biochemistry (amyloid aggregation selectivity)
# Ranker: Sonnet 4.6 (structured scoring mode)
# Date: 2026-03-28

---

## Scoring Notes

**Cross-domain bonus eligibility:** All four surviving hypotheses bridge non-equilibrium statistical mechanics / mathematical physics to protein biochemistry / neurodegenerative disease biology. This spans at least two disciplinary boundaries (physics -> chemistry -> biology), and in the case of H7 a third (molecular biology -> prion strain biology). The cross-domain +0.5 bonus applies to all four hypotheses per v5.8 rules.

**Groundedness penalties applied per Critic assessment:**
- H1: ~57% grounded (3 citation errors including 1 likely fabricated reference)
- H4: ~60% grounded (Kusumoto 1998 misattributed; key empirical claim falsely attributed)
- H5: ~75% grounded (cleanest; Zwanzig 1988 and Jia 2020 verified; honestly flagged uncertainties)
- H7: ~50% grounded (individual claims grounded but key computation non-existent; minor journal error on Manka 2022)

---

## Per-Hypothesis Scoring Tables

---

### H5: Rough Energy Landscape Diffusion Asymmetry (D_fold >> D_misfold) Creates the Spectral Signature That the Mpemba Index Detects

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | The Critic's web search found zero papers connecting Zwanzig roughness asymmetry between folding and misfolding landscapes to Mpemba-exploitable eigenvalue structure ("Zwanzig roughness amyloid misfolding eigenvalue spectrum" — 0 results). Individual components (Zwanzig 1988, energy landscape theory, MSM eigenvalues) are established, but the synthesis is genuinely new. The score is 8 rather than 9 because the component concepts are so well-known that the bridge, while novel, is narrow — it is a specific application of existing machinery rather than a conceptual leap across unrelated fields. |
| Mechanistic Specificity | 20% | 7 | The mechanism chain is concretely specified: rough misfolding landscape (epsilon ~ 1.5–2.5 kT roughness amplitude) -> reduced D_misfold via Zwanzig's D_eff = D_0 * exp(-(epsilon/kT)^2) -> bimodal eigenvalue spectrum with tau_slow/tau_fast > 100 for amyloidogenic proteins -> Mpemba-exploitable spectral structure. Specific quantitative thresholds are named (Sarle's bimodality coefficient > 0.555, tau_slow/tau_fast > 100 for amyloidogenic vs < 10 for controls). The score is 7 rather than 9 because the D_fold/D_misfold ratio itself is not directly measured — it is estimated from barrier heights using a 1D formula applied to a high-dimensional system, which the hypothesis honestly acknowledges. |
| Cross-field Distance | 10% | 7 | The bridge spans non-equilibrium statistical mechanics (Zwanzig roughness theory, 1988 physics) to biophysical chemistry (protein energy landscape theory) to protein biochemistry (amyloid MSMs). These are adjacent in the sense that both communities use energy landscape language, but the mathematical physics community and the protein biochemistry community rarely interact at the level of eigenvalue spectrum structure. The score is 7 rather than 9 because both fields share the MSM formalism as common ground — the disciplinary gap is real but not maximal. |
| Testability | 20% | 7 | The protocol is clearly stated: build MSMs for 4 amyloidogenic and 4 non-amyloidogenic proteins, compute full eigenvalue spectra, compute Sarle's bimodality coefficient, compare groups. Standard tools (TICA, k-means, PyEMMA, deeptime) support all steps. A PhD student in computational biophysics could execute the computational side in under 3 months if MD trajectory data exists or can be obtained from Folding@Home. The score is 7 rather than 8 because obtaining sufficient MD trajectory coverage (>100 microseconds aggregate) for 8 proteins is non-trivial and may extend the timeline; obtaining or building adequate MSMs for some less-studied proteins is a real bottleneck. |
| Impact: Paradigm | 5% | 6 | If true, this provides the first physical explanation (grounded in Zwanzig's diffusion theory) for WHY amyloidogenic proteins are more susceptible to Mpemba-like eigenspectral perturbations. It would connect landscape physics to Mpemba thermodynamics in a biologically meaningful context. This extends the existing frameworks but does not overturn them — it fills a mechanistic gap rather than opening a new field. Score 6. |
| Impact: Translational | 5% | 4 | The hypothesis produces a computational signature (bimodal eigenvalue spectrum) for amyloid vulnerability, which could eventually inform drug target selection or therapeutic cooling protocol design. However, the translational pathway is long: bimodal eigenvalue spectra do not directly suggest drug targets or diagnostics. The link to clinical application is indirect and speculative at this stage. Score 4. |
| Groundedness | 20% | 7 | The Critic verified: Zwanzig 1988 PNAS 85:2029 (VERIFIED), Bryngelson et al. 1995 Proteins 21:167 (VERIFIED), Jia et al. 2020 PNAS 117:10322 (VERIFIED, energy barriers 2-8 kcal/mol), Husic & Pande 2018 JACS 140:2386 (VERIFIED), computational validator independently confirmed the D ratio is plausible. No fabricated citations. The ~75% grounding assessment is the strongest in the set. The score is 7 rather than 8 because the estimated D_fold/D_misfold ratio (the central quantitative claim) is derived from a 1D formula applied to a multidimensional system, and no direct measurement exists for any protein. |
| **Composite (pre-bonus)** | | **7.10** | 0.20*8 + 0.20*7 + 0.10*7 + 0.20*7 + 0.05*6 + 0.05*4 + 0.20*7 = 1.6 + 1.4 + 0.7 + 1.4 + 0.30 + 0.20 + 1.4 = 7.00. Corrected: 1.6+1.4+0.7+1.4+0.3+0.2+1.4 = 7.00 |
| **Cross-domain bonus** | | **+0.5** | Physics (statistical mechanics, Zwanzig 1988) -> Chemistry (energy landscape biophysics) -> Biology (amyloid neurodegeneration): 2+ disciplinary boundaries confirmed. |
| **Composite (final)** | | **7.50** | 7.00 + 0.50 |

---

### H1: Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | The Critic confirmed via web search: "Mpemba AND amyloid" = 0 PubMed papers; "Mpemba effect protein folding aggregation amyloid spectral" = 0 results; "Markov state model Mpemba effect protein biophysics 2024 2025 2026" = 0 results; Teza et al. 2025 comprehensive review verified zero biophysical Mpemba applications. The connection is entirely unexplored. Score 9 (not 10) because the mathematical formalism for applying Mpemba indices to Markov chains is established — the novelty is specifically in the protein MSM application. |
| Mechanistic Specificity | 20% | 6 | The mechanism is mathematically well-specified: compute eigendecomposition of protein MSM transition matrix T, identify slowest eigenmode v_2 (Fiedler mode), evaluate overlap <p_init | v_2> across Boltzmann distributions at 280K-400K, count zero-crossings. Specific quantitative predictions are named (Mpemba(Abeta42) >= 2, Mpemba(Abeta40) = 0 or 1, Spearman rho > 0.7). However, the Critic identified a key unverified assumption: that v_2 encodes the misfolding pathway specifically rather than some other slow conformational rearrangement. This assumption is empirically unverified and could invalidate the entire framework. Score 6 (not 7+) due to this central unverified structural assumption. |
| Cross-field Distance | 10% | 8 | The Mpemba index is a concept from non-equilibrium statistical physics (Klich et al. 2019, PRX); protein MSMs and aggregation propensity are central to biochemistry and neurodegeneration research. These communities have essentially no overlap. A statistical physicist would not know what a protein MSM is; a protein biochemist would not know what a Mpemba index is. Score 8 (not 9-10) because both communities share the common formalism of Markov chains at the mathematical level, providing a structural bridge that reduces the effective disciplinary gap. |
| Testability | 20% | 5 | The prediction is clearly falsifiable: compute Mpemba indices from published MSMs and correlate with ThT aggregation kinetics. However, the Critic's central finding is that the proposed MSMs do not actually exist as described: Rosenman 2013 is REMD (not MSM), Robustelli 2018 is a force field paper (not MSM), Eschmann 2015 is unverifiable. Constructing adequate MSMs from scratch is "itself a substantial research project" per the Critic — extending the timeline well beyond 3 months and requiring specialized expertise beyond a typical biophysics PhD student. Score 5: falsifiable in principle with substantial additional work, not readily executable. |
| Impact: Paradigm | 5% | 7 | If the Mpemba index reliably distinguishes amyloidogenic from non-amyloidogenic proteins, it would introduce a new kinetic eigenspectral paradigm for understanding aggregation vulnerability — an entirely different language from current sequence-based (thermodynamic) approaches. This would not overturn existing paradigms but would open a new spectral physics approach to neurodegeneration. Score 7. |
| Impact: Translational | 5% | 5 | A validated Mpemba index predictor could serve as a computational classifier for amyloid risk, complementing existing sequence-based tools. It could also motivate MSM-guided protein engineering to reduce amyloidogenicity by flattening the eigenspectrum. These are plausible translational pathways but are several steps removed from clinical application. Score 5. |
| Groundedness | 20% | 4 | The Critic's assessment: ~57% grounded with 3 citation errors, including one likely fabricated citation (Eschmann et al. 2015 — no matching paper found), one mischaracterized citation (Robustelli 2018 is a force field paper presented as an MSM), and one citation with wrong year, volume, and pages that is also mischaracterized as an MSM (Rosenman 2013). These are not peripheral citations — they are the proposed test data sources. The hypothesis falsely implies that protein MSMs are already published and ready to use for the computation, when in fact the key MSMs do not exist. Score 4: the theoretical framework is grounded (Klich 2019 VERIFIED, Jia 2020 VERIFIED), but the proposed computational pathway rests on fabricated infrastructure. |
| **Composite (pre-bonus)** | | **5.90** | 0.20*9 + 0.20*6 + 0.10*8 + 0.20*5 + 0.05*7 + 0.05*5 + 0.20*4 = 1.80 + 1.20 + 0.80 + 1.00 + 0.35 + 0.25 + 0.80 = 6.20. Recalculated carefully: 1.80+1.20+0.80+1.00+0.35+0.25+0.80 = 6.20 |
| **Cross-domain bonus** | | **+0.5** | Physics (non-equilibrium statistical mechanics, Mpemba effect) -> Chemistry (protein folding biophysics) -> Biology (amyloid neurodegeneration): 2+ disciplinary boundaries confirmed. |
| **Composite (final)** | | **6.70** | 6.20 + 0.50 |

---

### H4: Inverse Mpemba Protocol Suppresses Amyloid Fibril Formation by Exploiting Eigenmode Decoupling

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The specific application of Mpemba eigenmode analysis to design amyloid-suppressing cooling protocols is novel (Critic confirmed: 0 results for this combination). However, the general concept that cooling rate affects amyloid formation is well-known in protein biochemistry — rapid cooling vs. slow annealing is standard laboratory practice. The Mpemba eigenmode framing of this observation provides a novel mechanistic interpretation but builds on an already-observed phenomenon. Score 7: specific eigenmode-cooling protocol design is novel; the broader phenomenon it predicts has known competing explanations. |
| Mechanistic Specificity | 20% | 5 | The mechanism is stated: rapid quench preserves the high-temperature ensemble's eigenmode projection, bypassing the "dangerous intermediate regime" where overlap with the misfolding eigenmode is maximal. The test protocol specifies non-monotonic cooling rate dependence as a distinguishing test. However, the Critic identified a critical factual error: the claimed empirical anchor (Kusumoto 1998 showing maximal nucleation at intermediate temperatures) is FALSE — the paper shows monotonic Arrhenius behavior. Without the intermediate-temperature maximum, the eigenmode-overlap argument loses its empirical grounding and is rendered indistinguishable from the trivial "rapid cooling = less time at high T = less aggregation" explanation. Score 5: mechanism is conceptually specified but the key empirical anchor is falsely attributed. |
| Cross-field Distance | 10% | 8 | Mpemba effect from non-equilibrium statistical physics applied as a protocol design principle in biochemistry to suppress protein aggregation. The conceptual jump from thermodynamic eigenmode analysis to a wet-lab cooling protocol for amyloid disease is genuinely cross-disciplinary. Score 8 for bridging physics theory to experimental biochemistry and disease application. |
| Testability | 20% | 8 | This is the most practically testable hypothesis in the set. The test protocol is concrete and immediately executable: prepare Abeta42 at 25 uM in PBS, protocol A (rapid quench from 60C to 37C), protocol B (slow cooling 0.1C/min), monitor ThT fluorescence. Positive and negative controls are specified. The non-monotonic cooling rate dependence test (step 3) would distinguish eigenmode from trivial kinetic mechanisms. A PhD student in protein biochemistry could execute this in under 3 months with standard laboratory equipment. Score 8 — the highest testability in the set, but not 9 because the computational eigenmode verification step requires MSMs that do not yet exist. |
| Impact: Paradigm | 5% | 5 | If the eigenmode-suppression mechanism is validated (rather than the trivial kinetic explanation), it would establish that Mpemba physics governs a biologically relevant aggregation process, opening new rational cooling protocol design based on spectral analysis. This extends rather than overturns existing frameworks. Score 5. |
| Impact: Translational | 5% | 7 | Amyloid suppression protocols have direct disease relevance (Alzheimer's, Parkinson's). If rapid eigenmode-optimized cooling reduces fibril formation by 50%+, this could motivate temperature-based therapeutic strategies (therapeutic hypothermia protocols, biopharmaceutical manufacturing improvements to reduce aggregation during processing). More concrete translational pathway than H1 or H5. Score 7. |
| Groundedness | 20% | 4 | The Critic's assessment: ~60% grounded. The core Mpemba framework citation is verified (Klich 2019). Noji et al. 2021 (Communications Biology) is verified. However, the critical empirical claim — that Kusumoto 1998 shows "maximal nucleation at intermediate temperatures" — is a FALSE ATTRIBUTION. The paper shows monotonic Arrhenius kinetics, the opposite of what is claimed. This is not a minor citation error; it is the empirical foundation for the entire hypothesis. Score 4: the Mpemba framework is grounded, the experimental design is sound, but the central factual claim that motivates the hypothesis is fabricated from a real paper. |
| **Composite (pre-bonus)** | | **5.75** | 0.20*7 + 0.20*5 + 0.10*8 + 0.20*8 + 0.05*5 + 0.05*7 + 0.20*4 = 1.40 + 1.00 + 0.80 + 1.60 + 0.25 + 0.35 + 0.80 = 6.20. Recalculated: 1.40+1.00+0.80+1.60+0.25+0.35+0.80 = 6.20 |
| **Composite correction** | | | Re-examining: Novelty 7 * 0.20 = 1.40; Mech. Spec 5 * 0.20 = 1.00; Cross-field 8 * 0.10 = 0.80; Testability 8 * 0.20 = 1.60; Paradigm 5 * 0.05 = 0.25; Translational 7 * 0.05 = 0.35; Groundedness 4 * 0.20 = 0.80. Sum = 6.20 |
| **Cross-domain bonus** | | **+0.5** | Physics (Mpemba effect, non-equilibrium thermodynamics) -> Experimental biochemistry (ThT aggregation assay) -> Neurodegenerative disease biology: 2+ disciplinary boundaries confirmed. |
| **Composite (final)** | | **6.70** | 6.20 + 0.50 |

---

### H7: Mpemba Eigenmode Branching Explains Prion Strain Selection

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 9 | The Critic confirmed: explaining prion strain selection via Mpemba eigenmode branching is entirely novel. Petkova et al. 2005 established that growth conditions produce different polymorphs, but the eigenmode branching explanation is new. The combination of prion strain physics with Mpemba formalism has zero prior literature. Score 9: maximally novel on the specific bridge, with small deduction because prion strain diversity as a phenomenon is well-documented and the hypothesis is explaining an observed phenomenon rather than predicting an undiscovered one. |
| Mechanistic Specificity | 20% | 5 | The mechanism is conceptually clear: multiple slow eigenmodes of the PrP MSM map to distinct strain conformations; different thermal histories project onto different eigenmodes; each trajectory relaxes into a different metastable misfolded basin. The hypothesis names specific experimental tools (RT-QuIC, PK digestion, HDX-MS, cryo-EM) and specific temperatures. However, a central mechanism element cannot be evaluated: the PrP MSM does not exist and cannot currently be constructed (PrP misfolding involves massive alpha-helix to beta-sheet transition beyond current MD sampling). The mechanism is stated at a conceptual level but cannot be operationalized with current tools. Score 5: good conceptual specification, but the core quantitative machinery is inaccessible. |
| Cross-field Distance | 10% | 9 | This is the widest disciplinary bridge in the set: non-equilibrium statistical physics (Mpemba eigenmode branching) -> molecular biology (PrP misfolding MSMs) -> prion strain biology (a specialized sub-field of neurodegenerative disease with unique biological inheritance rules). Prion biology is sufficiently far from statistical mechanics that essentially no researcher operates in both fields. Score 9. |
| Testability | 20% | 3 | The fundamental problem is that the primary test system (PrP MSM with multiple slow eigenmodes) does not exist. The hypothesis acknowledges this: "PrP misfolding involves massive conformational change (alpha-helix to beta-sheet) that is beyond current MD sampling capabilities for all-atom simulations." The Critic concurs: "the mechanism is conceptually coherent but practically untestable." The experimental prediction (different cooling rates produce different PrP polymorphs via RT-QuIC, HDX-MS, cryo-EM) is testable, but it cannot distinguish eigenmode branching from alternative explanations without the MSM. Score 3: the experimental observation is testable, but the mechanistic claim (eigenmode branching specifically) is not falsifiable with current technology. |
| Impact: Paradigm | 5% | 8 | If the eigenmode branching framework explains prion strain selection, it would provide the first physical-mathematical account of how a single amino acid sequence supports multiple stable self-propagating conformations — one of the deepest puzzles in prion biology. This would reframe prion strain diversity from a biological enigma to a predictable consequence of eigenspectrum structure. Score 8: this would be a genuinely paradigm-shifting insight for both prion biology and protein science generally. |
| Impact: Translational | 5% | 5 | A validated eigenmode branching model of strain selection could guide therapeutic strategies that bias the eigenmode projection away from pathogenic strains (e.g., using specific thermal denaturation/renaturation protocols to select for less pathogenic prion conformations). The translational pathway is speculative and long. Score 5. |
| Groundedness | 20% | 4 | The Critic's assessment: ~50% grounded. Individual supporting citations are well-verified (Collinge & Clarke 2007 VERIFIED, Petkova 2005 VERIFIED, Legname 2004 VERIFIED, Deleault 2012 VERIFIED). However, the key computational element is acknowledged to be absent: no MSM for PrP misfolding exists. Additionally, the proposed 80C starting temperature is above PrP's denaturation temperature (~65C), meaning the "thermally expanded ensemble" is actually a denatured, non-specifically aggregating state. A minor journal error on Manka 2022 (cited as Nature, actual journal is Nature Communications) is also present. Score 4: the framework is conceptually grounded but the central computation cannot be performed, and a key experimental parameter (80C) is physically inappropriate. |
| **Composite (pre-bonus)** | | **5.35** | 0.20*9 + 0.20*5 + 0.10*9 + 0.20*3 + 0.05*8 + 0.05*5 + 0.20*4 = 1.80 + 1.00 + 0.90 + 0.60 + 0.40 + 0.25 + 0.80 = 5.75 |
| **Composite correction** | | | Re-examining: 1.80+1.00+0.90+0.60+0.40+0.25+0.80 = 5.75 |
| **Cross-domain bonus** | | **+0.5** | Physics (Mpemba eigenmode branching, statistical mechanics) -> Molecular biology (PrP misfolding) -> Prion strain biology (a distinct discipline within neuroscience with unique biological inheritance mechanisms): 2+ disciplinary boundaries confirmed, arguably 3. |
| **Composite (final)** | | **6.25** | 5.75 + 0.50 |

---

## Score Computation Summary

### Detailed Weighted Calculations

**H5:**
- Novelty: 8 * 0.20 = 1.60
- Mechanistic Specificity: 7 * 0.20 = 1.40
- Cross-field Distance: 7 * 0.10 = 0.70
- Testability: 7 * 0.20 = 1.40
- Impact Paradigm: 6 * 0.05 = 0.30
- Impact Translational: 4 * 0.05 = 0.20
- Groundedness: 7 * 0.20 = 1.40
- Pre-bonus total: **7.00**
- Cross-domain bonus: +0.50
- **Final composite: 7.50**

**H1:**
- Novelty: 9 * 0.20 = 1.80
- Mechanistic Specificity: 6 * 0.20 = 1.20
- Cross-field Distance: 8 * 0.10 = 0.80
- Testability: 5 * 0.20 = 1.00
- Impact Paradigm: 7 * 0.05 = 0.35
- Impact Translational: 5 * 0.05 = 0.25
- Groundedness: 4 * 0.20 = 0.80
- Pre-bonus total: **6.20**
- Cross-domain bonus: +0.50
- **Final composite: 6.70**

**H4:**
- Novelty: 7 * 0.20 = 1.40
- Mechanistic Specificity: 5 * 0.20 = 1.00
- Cross-field Distance: 8 * 0.10 = 0.80
- Testability: 8 * 0.20 = 1.60
- Impact Paradigm: 5 * 0.05 = 0.25
- Impact Translational: 7 * 0.05 = 0.35
- Groundedness: 4 * 0.20 = 0.80
- Pre-bonus total: **6.20**
- Cross-domain bonus: +0.50
- **Final composite: 6.70**

**H7:**
- Novelty: 9 * 0.20 = 1.80
- Mechanistic Specificity: 5 * 0.20 = 1.00
- Cross-field Distance: 9 * 0.10 = 0.90
- Testability: 3 * 0.20 = 0.60
- Impact Paradigm: 8 * 0.05 = 0.40
- Impact Translational: 5 * 0.05 = 0.25
- Groundedness: 4 * 0.20 = 0.80
- Pre-bonus total: **5.75**
- Cross-domain bonus: +0.50
- **Final composite: 6.25**

---

## Final Ranking Table

| Rank | ID | Title | Composite | Verdict |
|------|----|-------|-----------|---------|
| 1 | H5 | Rough Energy Landscape Diffusion Asymmetry (D_fold >> D_misfold) Creates Mpemba-Detectable Spectral Signature | **7.50** | SURVIVES — evolve |
| 2 | H1 | Mpemba Index of Protein Folding MSMs Predicts Amyloid Aggregation Propensity | **6.70** | WOUNDED — evolve |
| 2 (tie) | H4 | Inverse Mpemba Protocol Suppresses Fibril Formation by Exploiting Eigenmode Decoupling | **6.70** | WOUNDED — evolve |
| 4 | H7 | Mpemba Eigenmode Branching Explains Prion Strain Selection | **6.25** | WOUNDED — evolve (diversity role) |

**H1 and H4 are tied at 6.70.** Tiebreaker applied (see Diversity Check below).

---

## Diversity Check

### Top-4 Analysis (all surviving hypotheses considered, as only 4 survive)

Pair assessments:

| Pair | Same bridge mechanism? | Same subfields? | Same prediction type? | Convergent? |
|------|----------------------|-----------------|----------------------|-------------|
| H5 vs H1 | Partial — both use MSM eigenvalue spectra; H5 explains the physical origin of the spectral structure while H1 computes the Mpemba index from it | Same (protein MSMs, amyloid aggregation) | Similar (compare amyloidogenic vs non-amyloidogenic proteins) | PARTIALLY CONVERGENT |
| H5 vs H4 | Different — H5 is a theoretical mechanism paper; H4 is an experimental protocol design | Overlapping but different emphasis | Different prediction type (spectral bimodality vs fibril mass reduction) | LOW convergence |
| H5 vs H7 | Different — H7 applies to prion strain selection, not aggregation propensity comparison | Different (prion biology vs amyloid MSMs) | Different (polymorph selection vs spectral structure) | LOW convergence |
| H1 vs H4 | Partial — both predict MSM eigenmode effects on amyloidogenicity; H4 specifically exploits the MSM structure for protocol design | Same (Abeta42, protein MSMs) | Different (computational classification vs wet-lab cooling protocol) | MODERATE convergence |
| H1 vs H7 | Partial — both use Mpemba eigenmode overlap; different biological systems | Different (amyloid aggregation vs prion strains) | Different (propensity ranking vs strain polymorph selection) | LOW convergence |
| H4 vs H7 | Different — H4 is a wet-lab protocol; H7 is a theoretical framework for prion biology | Different | Different | LOW convergence |

### Convergence Assessment

The main convergence risk is between H5 and H1. Both:
- Operate on protein MSM eigenvalue spectra
- Compare amyloidogenic vs non-amyloidogenic proteins
- Use the same core proteins (Abeta42, alpha-synuclein)
- Are computational in nature

However, they are NOT redundant. H5 asks "WHY does the eigenvalue spectrum have Mpemba-exploitable structure?" (physical mechanism: D_fold/D_misfold asymmetry via Zwanzig roughness). H1 asks "WHAT does the Mpemba index value predict about aggregation propensity?" (phenomenological correlation). These are complementary questions in a mechanism-discovery pipeline, and both should proceed to evolution. H5 provides the mechanistic grounding that H1 needs.

H4 has a different prediction type (wet-lab experimental outcome) and represents the translational face of the same framework. It is complementary to H5 and H1 and scores identically to H1 at 6.70.

H7 scores lowest but is the most diverse hypothesis — it applies the framework to a completely different biological system (prion strains vs amyloid aggregation kinetics) and is the widest disciplinary bridge. It qualifies for the diversity promotion: it is the only hypothesis targeting prion biology and would bring genuine diversity to the evolution cycle.

### H1 vs H4 Tiebreaker (both 6.70)

Both share the same composite score. Tiebreaker dimensions:
- **Testability**: H4 scores 8 vs H1's 5 — H4 wins
- **Groundedness**: H4 scores 4 vs H1's 4 — tie
- **Mechanistic Specificity**: H4 scores 5 vs H1's 6 — H1 wins

The testability advantage of H4 is decisive for evolution selection: the Evolver can design a test protocol for H4 immediately with existing wet-lab tools. H4 is ranked above H1 in the final evolution selection ordering.

**No diversity penalty applied.** H5 and H1 are convergent in domain but divergent in question type (mechanism vs phenomenology). All four hypotheses bring distinct contributions. No hypothesis is demoted.

**Evolution selection: all 4 hypotheses advance**, as the set is small enough (4 survivors from 7 generated) and each occupies a distinct role: H5 (mechanistic explanation), H4 (experimental protocol), H1 (computational classifier), H7 (prion biology / diversity).

---

## Elo Tournament Sanity Check (Top-4, 6 pairwise comparisons)

*Prompt for each pair: "Which hypothesis would a domain researcher want to test FIRST, and why?"*

**Comparison 1: H5 vs H1**
H5 wins. A researcher would test H5 first because it addresses the physical MECHANISM underlying the entire Mpemba-amyloid framework. If the bimodal eigenvalue spectrum predicted by H5 does not exist, the entire program (including H1's Mpemba index computation) collapses. H5 provides the mechanistic foundation and is better grounded. H1 depends on H5's validity.
*Winner: H5*

**Comparison 2: H5 vs H4**
H5 wins narrowly. H4 is more immediately testable in a wet lab, but H5 provides the theoretical foundation explaining WHY the cooling protocol in H4 would work. Testing H4 without H5 would yield an empirical result without a mechanism. A theoretically-minded researcher chooses H5; an experimentally-minded researcher might choose H4. For mechanistic discovery, H5 comes first.
*Winner: H5 (narrow)*

**Comparison 3: H5 vs H7**
H5 wins clearly. H5 is testable now with existing or obtainable MSM data. H7 requires constructing PrP MSMs that are computationally impossible with current technology. The testability gap is decisive.
*Winner: H5*

**Comparison 4: H1 vs H4**
H4 wins. H4 provides an immediately executable wet-lab experiment. H1 requires building protein MSMs that the Critic confirmed do not exist as described. A researcher wanting empirical progress on the Mpemba-amyloid connection would start with H4's cooling protocol experiment, which can be done in weeks with standard equipment.
*Winner: H4*

**Comparison 5: H1 vs H7**
H1 wins narrowly. Both are computationally intensive, but H1 operates on a more tractable system (amyloid MSMs are further along than PrP MSMs) and has better grounding for the individual component claims. H7's prion system is essentially intractable computationally at present.
*Winner: H1*

**Comparison 6: H4 vs H7**
H4 wins clearly. H4 is executable tomorrow with ThT assays. H7 requires a PrP MSM that cannot be built. The practical research agenda strongly favors H4.
*Winner: H4*

### Elo Win Tally

| Hypothesis | Wins | Losses | Win Rate |
|------------|------|--------|----------|
| H5 | 3 | 0 | 3/3 = 100% |
| H4 | 2 | 1 | 2/3 = 67% |
| H1 | 1 | 2 | 1/3 = 33% |
| H7 | 0 | 3 | 0/3 = 0% |

### Elo vs Linear Ranking Comparison

| | Linear Composite | Elo Win Rate |
|---|---|---|
| H5 | 7.50 (1st) | 100% (1st) |
| H4 | 6.70 (2nd, post-tiebreak) | 67% (2nd) |
| H1 | 6.70 (3rd, post-tiebreak) | 33% (3rd) |
| H7 | 6.25 (4th) | 0% (4th) |

**Result: Elo confirms linear ranking.** The pairwise tournament agrees exactly with the composite score ordering. The tiebreaker between H1 and H4 is confirmed by Elo: H4 wins 2/3 including the direct H1 vs H4 matchup.

**Diagnostic signal from Elo:** The pairwise comparison captures a practical "testability premium" that the linear composite partially captures but understates for H4. H4 scores only marginally lower than H5 on testability (8 vs 7) but the practical gap feels larger in pairwise comparison because H4 requires no new computational infrastructure at all, while H5 requires substantial MSM construction work. This is a signal for the Evolver: H4's testability should be preserved and extended; H5's mechanism should be strengthened by proposing how to operationalize the D_fold/D_misfold asymmetry measurement directly.

---

## Evolution Selection

**Top 4 hypotheses selected for evolution (post-diversity-check):**

1. **H5** — Composite 7.50 — Mechanistic physical foundation for the entire framework. Evolve by: strengthening the D_fold/D_misfold measurement protocol, proposing a direct experimental test of eigenvalue bimodality in existing amyloid MSM datasets (e.g., Folding@Home Abeta trajectories), and incorporating the high-dimensional correction to Zwanzig's formula.

2. **H4** — Composite 6.70 — Most immediately testable hypothesis; only one requiring no new computational infrastructure. Evolve by: removing the Kusumoto 1998 false attribution, rebuilding the temperature-dependence argument from scratch (citing actual data on Abeta42 temperature-dependent aggregation), and strengthening the mechanism-distinguishing element (non-monotonic cooling rate dependence test).

3. **H1** — Composite 6.70 — Phenomenological classifier and conceptual entry point for the Mpemba-amyloid framework. Evolve by: replacing fabricated MSM citations with accurate references, acknowledging that new MSM construction is required, and shifting from "ready-to-compute" to "construction protocol specified." The Critic's question about which MSMs actually exist should be addressed directly.

4. **H7** — Composite 6.25 — Lowest composite but highest diversity value; only hypothesis targeting prion biology. Evolve by: replacing the 80C starting temperature with a sub-denaturation protocol (< 60C), pivoting to amyloid systems with known polymorphism (Abeta polymorphs per Petkova 2005) as a more computationally tractable proxy test system, and addressing the cofactor dependence counter-evidence.

---

*Cycle 1 ranking complete. All 4 surviving hypotheses advance to evolution.*
*Highest composite score (H5): 7.50*
*Session phase: evolution*
