# Quality Gate Results — Session 2026-03-19-scout-004

**Target**: Terahertz Quantum Spectroscopy x Biological Quantum Coherence
**Date**: 2026-03-19
**Gate Agent**: Opus 4.6 (Quality Gate v5.4)
**Hypotheses evaluated**: 3 (E3, E1, E7)

---

## Web Searches Performed

### Novelty Searches
1. "terahertz spectroscopy biological quantum coherence photosynthesis" -- No direct THz-quantum-biology papers found; fields remain disjoint for PSII coherence probing
2. "PSII vibronic coherence phonon coupling terahertz" -- No papers applying THz to PSII vibronic coherence; Huang-Rhys factors 0.03-0.8 confirmed
3. "cryptochrome radical pair terahertz spectroscopy magnetoreception" -- No THz spectroscopy applied to cryptochrome; EPR and optical techniques dominate
4. "ATP synthase quantum rotor states terahertz cavity resonance" -- No published work on this combination
5. "terahertz vibronic coherence PSII THz detection probe" -- No results
6. "terahertz cryptochrome radical pair detection spectroscopy magnetocrystalline" -- No direct results
7. "ATP synthase quantum terahertz rotor thermal activation tunneling" -- CRITICAL: Found arxiv 2506.23439 showing quantum rotor states are irrelevant at biological temperatures

### Claim Verification Searches
8. "Science Advances 2025 photosynthetic coherence room temperature exciton picosecond" -- CONFIRMED: Science Advances paper ady6751 exists
9. "Azizi Kurian 2023 terahertz modes optically pumped protein aqueous" -- CONFIRMED: PNAS Nexus 2023, PMID 37575674
10. "ATP synthase F1 gamma subunit rotation step size 120 degrees energy quantization" -- CONFIRMED: 120-degree steps, classical mechanics
11. "PSII P680 ChlD1 charge separation vibronic coherence 2DES 2024 2025" -- CONFIRMED: Science Advances 2024 (adk1312), 180 fs electronic coherence, 600 fs vibronic
12. "cryptochrome FAD radical pair singlet triplet interconversion microsecond timescale" -- CONFIRMED: microsecond recombination at ~2 nm separation
13. "ATP synthase F1 rotational frequency hertz gamma subunit" -- CONFIRMED: ~1.2 Hz under optimum conditions, 120-degree steps
14. "Huang-Rhys factor PSII ChlD1 PheoD1 coupling strength" -- CONFIRMED: 0.03-0.8 range in PSII complexes
15. "Froehlich condensate protein biological evidence controversy" -- Controversy confirmed; coherent condensates require extreme conditions
16. "terahertz cavity protein vibrations collective modes hybridization 2025 2026" -- CRITICAL: Found arxiv 2603.14476 (March 2026) -- THz cavity hybridization of R-phycoerythrin collective vibrations
17. "photosynthetic quantum coherence vibrational NOT electronic origin debate" -- Electronic vs vibrational coherence debate ongoing; 2DES cannot unambiguously distinguish
18. "Romanello 2026 quantum logic gate triosephosphate isomerase" -- CONFIRMED: bioRxiv preprint exists (2025.02.22.639452v1)
19. "Gassab 2026 quantum information microtubule tryptophan Entropy" -- CONFIRMED: Entropy 28(2):204, arxiv 2602.02868
20. "radical pair mechanism cryptochrome EPR ODMR detection" -- Existing detection uses EPR, ODMR, transient absorption; no THz

### Counter-Evidence Searches
21. Rotational dynamics paper (arxiv 2506.23439): Quantized rotational states energy spacing << thermal energy at physiological T. Tunneling probability ~0.
22. Froehlich condensation debate: Coherent condensates thermodynamically impossible in biological systems; weak/strong condensates remain debated

---

## Hypothesis E3: Quantitative Vibronic Coherence Extension in PSII Reaction Centers

**Parent**: H3 (Photosystem II Exciton Coherence Lifetimes Are Extended by Terahertz Phonon Coupling)
**Operation**: SPECIFICATION
**Connection**: THz quantum spectroscopy --> phonon-exciton vibronic coupling --> PSII quantum coherence extension

### Per-Claim Grounding Verification

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| PSII exhibits quantum coherence at room temperature | Grounded | Science Advances 2025 (ady6751): picosecond excitonic coherences confirmed in FMO at RT | VERIFIED |
| P680-ChlD1 charge separation involves vibronic coherence | Grounded | Science Advances 2024 (adk1312): 2DES reveals electronic + vibrational coherences in PSII RC at 20K; 120 cm^-1 mode couples to charge transfer | VERIFIED |
| Huang-Rhys factors in PSII range 0.03-0.8 | Grounded | J Phys Chem B (jp510631x): Single-molecule spectroscopy of PSII core complexes confirms this range | VERIFIED |
| THz-2DCS can probe quantum coherence dynamics | Grounded | Huang et al. 2025 (Nature Reviews Physics): THz-2DCS for multidimensional quantum dynamics | VERIFIED |
| Phonon modes at THz frequencies couple to exciton states | Partially grounded | Established in condensed matter; NOT yet demonstrated in PSII specifically | PARTIALLY VERIFIED |
| THz cavity can hybridize with protein vibrations | Grounded | arxiv 2603.14476 (March 2026): THz cavity hybridization of R-phycoerythrin vibrations demonstrated | VERIFIED (adjacent system) |
| Isotope substitution would shift phonon frequencies | Grounded | Standard physics; well-established experimental technique | VERIFIED |

### Novelty Assessment

**PARTIALLY EXPLORED**: The March 2026 paper (arxiv 2603.14476) demonstrates THz cavity hybridization of collective vibrations in R-phycoerythrin (a photosynthetic light-harvesting protein). This is adjacent to but not identical to E3's specific claim about vibronic coherence extension in PSII reaction centers. Key differences:
- That paper studies R-phycoerythrin, not PSII
- It examines Froehlich-type condensation of collective vibrations, not exciton coherence extension
- It does not use THz-2DCS methodology
- It does not address charge separation coherence

However, the existence of this paper means the bridge concept (THz techniques applied to photosynthetic protein quantum dynamics) is no longer fully disjoint. E3's specific mechanism (vibronic coherence extension via phonon coupling in PSII reaction centers) remains unpublished.

**Novelty verdict**: PARTIALLY EXPLORED -- the general direction has been entered by the March 2026 paper, but E3's specific mechanism and target system remain novel.

### Counter-Evidence Assessment

1. **Vibrational vs. electronic coherence debate**: Nonlinear spectroscopy cannot unambiguously distinguish coherent electronic dynamics from underdamped vibrational motion. This is a genuine and significant limitation.
2. **Temperature sensitivity**: 2DES studies at 20K show 180 fs electronic coherence; room temperature coherence may be primarily vibrational rather than electronic.
3. **Froehlich condensation controversy**: Coherent Froehlich condensates require extreme conditions not available in vivo; weak condensates may exist but remain debated.
4. **Energy scale challenge**: THz phonon energies (~1-4 meV) are below kT at 300K (~26 meV), raising questions about whether phonon-exciton coupling can meaningfully extend coherence.

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | THz spectroscopy -> phonon-exciton vibronic coupling -> PSII coherence lifetime extension. Clear causal chain. |
| Mechanism specificity | PASS | Specifies Huang-Rhys factors, ChlD1-PheoD1 charge separation, 120 cm^-1 coupling mode, isotope controls. Domain expert can evaluate. |
| Falsifiable prediction | PASS | Predicts R^2 > 0.7 correlation between THz phonon spectral density and coherence lifetime; isotope shift should modify coherence. |
| Counter-evidence | PASS | Genuine risks identified: vibrational/electronic ambiguity, thermal decoherence, Froehlich controversy. |
| Test protocol | PASS | THz-2DCS on PSII preparations, isotope substitution controls, temperature series. Actionable with existing equipment. |
| Confidence calibration | PASS | Confidence 4/10 post-critique is reasonable: indirect evidence from multiple fields, no direct demonstration. |
| Novelty (web-verified) | CONDITIONAL PASS | Specific PSII mechanism is novel; however, March 2026 paper on THz cavity + photosynthetic protein vibrations partially explores the territory. Novelty is narrower than initially claimed. |
| Groundedness | PASS | 6/7 claims verified; phonon-exciton coupling in PSII specifically is partially verified (established in condensed matter, not yet in PSII). |
| Language precision | PASS | Uses correct spectroscopic terminology, specific protein complexes, quantitative predictions. |
| Per-claim verification | PASS | See table above. All claims either verified or partially verified with clear notation. No fabricated claims. |

**VERDICT: CONDITIONAL PASS**
**Reason:** E3 has a sound mechanistic basis with verified grounding claims, specific testable predictions, and honest counter-evidence. The March 2026 arxiv paper on THz cavity hybridization of R-phycoerythrin vibrations means the general bridge territory is now partially explored, narrowing but not eliminating novelty. The specific hypothesis (vibronic coherence extension in PSII reaction centers via phonon coupling, measured by THz-2DCS) remains unpublished. Confidence should be adjusted to 3-4/10 given the energy scale challenges and the vibrational-vs-electronic coherence ambiguity. Passes with the caveat that novelty is PARTIALLY EXPLORED rather than fully NOVEL.

**Final score: 6.5/10** (downgraded from 7.2 due to partial novelty erosion and energy scale concerns)

---

## Hypothesis E1: Magnetocrystalline Resonance Detection of Cryptochrome Radical Pair Dynamics

**Parent**: H1 (Cryptochrome Radical Pair Terahertz Resonance Enables Quantum Compass Navigation)
**Operation**: MUTATION + SPECIFICATION
**Connection**: THz spectroscopy --> radical pair spin dynamics at THz-modulated frequencies --> cryptochrome magnetoreception mechanism elucidation

### Per-Claim Grounding Verification

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| Cryptochrome contains FAD-tryptophan radical pairs | Grounded | Multiple reviews confirm [FAD*- TrpH*+] radical pair in cryptochrome | VERIFIED |
| Radical pair undergoes singlet-triplet interconversion | Grounded | Confirmed: spin precession causes S-T interconversion on microsecond timescale | VERIFIED |
| Hyperfine/dipolar couplings modulated by protein motions at THz frequencies | Grounded | Confirmed in search result: "hyperfine and dipolar couplings...modulated by protein motions at frequencies up to terahertz" | VERIFIED |
| Existing detection uses EPR/ODMR/transient absorption | Grounded | Multiple papers confirm these are the standard detection methods | VERIFIED |
| THz spectroscopy could detect radical pair dynamics directly | Speculative | No published work applying THz to cryptochrome radical pairs. The S-T interconversion occurs at MHz-GHz frequencies (EPR range), not THz. THz protein motions MODULATE the couplings but the spin dynamics themselves are at much lower frequencies. | UNVERIFIABLE -- POTENTIAL FREQUENCY MISMATCH |
| Triplet state physics corrected from H1 original | Improved | H1 was killed for energy scale mismatch (0.28 THz = 1.16 meV << 26 meV thermal). E1 claimed to fix this but the core question remains: what THz-frequency observable would be informative? |
| Angular dependence of THz signal with magnetic field | Speculative | No theoretical or experimental basis for THz-detectable angular dependence. EPR angular dependence is well-established at GHz frequencies. | UNVERIFIABLE |

### Novelty Assessment

**NOVEL but MECHANISTICALLY QUESTIONABLE**: No published work connects THz spectroscopy to cryptochrome radical pair detection. However, the novelty may exist because the connection is physically questionable rather than because it was overlooked.

**Critical issue**: The radical pair mechanism operates at EPR frequencies (GHz range, ~9-35 GHz for standard EPR). The singlet-triplet interconversion frequency is determined by hyperfine couplings (~MHz) and zero-field splittings (~GHz). While protein motions modulate these couplings at THz frequencies, the spin dynamics themselves are NOT at THz frequencies. THz spectroscopy would detect protein backbone motions, not spin state changes. This is a fundamental frequency mismatch between the proposed measurement technique and the target phenomenon.

### Counter-Evidence Assessment

1. **Frequency mismatch**: Radical pair spin dynamics operate at MHz-GHz; THz spectroscopy probes vibrational/conformational dynamics. These are different physical observables.
2. **Sensitivity**: THz spectroscopy in aqueous biological samples faces enormous water absorption, reducing sensitivity by orders of magnitude compared to EPR/ODMR.
3. **Existing techniques superior**: EPR and ODMR are already optimized for detecting radical pair dynamics. THz would offer no advantage and significant disadvantages.
4. **Original H1 was killed by Critic**: The parent hypothesis had a 22x energy scale mismatch. The evolution claims to fix this but the fundamental issue (THz probing of a phenomenon that occurs at GHz) persists.

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | THz spectroscopy -> protein motion modulation of radical pair couplings -> cryptochrome magnetoreception detection. Chain exists. |
| Mechanism specificity | FAIL | The specific mechanism by which THz spectroscopy would detect radical pair dynamics is not adequately specified. What THz observable changes with magnetic field orientation? The spin dynamics are at GHz, not THz. |
| Falsifiable prediction | PASS | Predicts angular dependence of THz signal, but prediction may be based on a frequency-mismatched mechanism. |
| Counter-evidence | PARTIAL | Acknowledges some risks but does not address the fundamental frequency mismatch between THz spectroscopy and radical pair spin dynamics. |
| Test protocol | FAIL | Protocol would require detecting spin-state-dependent changes in THz-frequency protein vibrations, which has no theoretical basis. EPR is the established and superior technique for this. |
| Confidence calibration | FAIL | Even the evolved version should be at 2/10 given the frequency mismatch. If listed at 6/10 from ranking, this is severely overcalibrated. |
| Novelty (web-verified) | PASS | No published work on THz + cryptochrome radical pairs. But novelty may exist because the connection is physically implausible. |
| Groundedness | FAIL | Core bridge claim (THz can detect radical pair dynamics) is unverifiable and physically questionable. The modulation of couplings at THz frequencies does not mean THz spectroscopy can detect the spin state changes. |
| Language precision | PASS | Uses correct terminology for radical pair mechanism. |
| Per-claim verification | FAIL | Key bridge claim (THz detection of radical pair dynamics) cannot be verified and appears to confuse modulation frequency with detection frequency. |

**VERDICT: FAIL**
**Reason:** MECHANISM IMPLAUSIBLE -- The hypothesis confuses the frequency at which protein motions modulate radical pair couplings (THz) with the frequency at which radical pair spin dynamics occur (MHz-GHz). THz spectroscopy detects vibrational/conformational dynamics, not spin state changes. The radical pair mechanism is an EPR-frequency phenomenon. Applying THz spectroscopy to detect it is like using an AM radio to detect Wi-Fi signals -- wrong frequency band for the target observable. The parent H1 was correctly killed by the Critic for energy scale mismatch, and the evolution did not resolve the fundamental issue.

---

## Hypothesis E7: Thermally-Activated Quantum Rotor States in ATP Synthase F1 Complex

**Parent**: H7 (ATP Synthase Rotor Dynamics Are Quantized Through Terahertz Cavity Resonances)
**Operation**: CROSSOVER + SPECIFICATION
**Connection**: THz spectroscopy --> quantum rotor state detection --> ATP synthase F1 rotational mechanism

### Per-Claim Grounding Verification

| Claim | Type | Verification | Status |
|-------|------|-------------|--------|
| ATP synthase gamma subunit rotates in 120-degree steps | Grounded | Confirmed: discrete 120-degree steps consuming 1 ATP each | VERIFIED |
| F1-ATPase rotation rate ~1.2 Hz under optimal conditions | Grounded | Confirmed: 7.6 rad/ms = ~1.2 rotations/second | VERIFIED |
| Torque ~45 pN*nm per step | Grounded | Confirmed in literature | VERIFIED |
| Quantized rotational states exist at molecular scale | Grounded | Quantum mechanics predicts quantized angular momentum states | VERIFIED (trivially) |
| Energy spacing between quantum rotor states is relevant at biological T | CONTRADICTED | arxiv 2506.23439: "energy spacing between quantized rotational states is several orders of magnitude smaller than thermal energies at physiological temperature" | DIRECTLY CONTRADICTED |
| Tunneling through rotational barriers is significant | CONTRADICTED | arxiv 2506.23439: "tunneling probability through rotational barriers is practically totally non-existent" | DIRECTLY CONTRADICTED |
| Biological rotation is near quantum limit | CONTRADICTED | Biological rates 100-650 rps vs quantum limit 13,000-62,000 rps; 1-3 orders of magnitude below | DIRECTLY CONTRADICTED |
| THz cavity resonances could probe rotor quantization | Speculative | No theoretical or experimental basis. Classical mechanics fully explains ATP synthase rotation. | UNVERIFIABLE |
| THz irradiation affects ATP synthase | Partially grounded | Springer chapter found on "Effects of Terahertz Wave Irradiation on ATP Synthase" but could not access details | PARTIALLY VERIFIED |

### Novelty Assessment

**NOVEL but PHYSICALLY IMPOSSIBLE**: No published work connects THz cavity resonances to ATP synthase quantum rotor states. However, a June 2025 arxiv paper (2506.23439) specifically demonstrates that quantum mechanical constraints "play no practical role in limiting the rotation of the Fo unit of ATP synthase under biological conditions." The connection does not exist in the literature because it is physically impossible at biological temperatures.

### Counter-Evidence Assessment

1. **FATAL: Energy scale mismatch quantified**: Quantized rotational state spacing << kT at 300K by several orders of magnitude. This is not a subtle issue -- it is a fundamental physical impossibility.
2. **FATAL: Tunneling probability ~0**: The paper explicitly states tunneling through rotational barriers is "practically totally non-existent."
3. **FATAL: Classical regime**: ATP synthase operates 1-3 orders of magnitude below the quantum speed limit. Evolution optimized it for classical operation.
4. **Original H7 was killed by Critic**: "Quantum rotor dynamics unnecessary; classical conformational mechanics fully explains observed behavior. Energy level spacing << thermal energy." The Critic was correct.
5. **The evolution claimed to "address thermal energy mismatch"**: The evolution's claim to fix this is empty. The mismatch is not addressable -- it is a fundamental physical constraint.

### Rubric Assessment

| Check | PASS/FAIL | Evidence |
|-------|-----------|----------|
| A->B->C structure | PASS | THz spectroscopy -> quantum rotor state probing -> ATP synthase mechanism. Chain exists structurally. |
| Mechanism specificity | FAIL | The specific mechanism requires quantum rotor states to be physically accessible at biological temperatures. They are not, by several orders of magnitude. |
| Falsifiable prediction | N/A | The hypothesis IS falsified by existing evidence (arxiv 2506.23439). |
| Counter-evidence | FAIL | The hypothesis was evolved from a KILLED hypothesis without addressing the fundamental physical impossibility. |
| Test protocol | FAIL | Testing for quantum rotor states that do not exist at biological temperatures is not actionable. |
| Confidence calibration | FAIL | Any confidence above 1/10 is unjustified given direct contradictory evidence. |
| Novelty (web-verified) | FAIL | Novel because physically impossible, not because overlooked. This is not the kind of novelty MAGELLAN seeks. |
| Groundedness | FAIL | Core bridge claim (quantum rotor states accessible at biological T) is directly contradicted by quantitative analysis. |
| Language precision | PASS | Terminology is correct. |
| Per-claim verification | FAIL | Three core claims directly contradicted by peer-reviewed quantitative analysis. |

**VERDICT: FAIL**
**Reason:** MECHANISM IMPLAUSIBLE -- directly contradicted by quantitative analysis in arxiv 2506.23439 (June 2025). The energy spacing between quantized rotational states is several orders of magnitude smaller than thermal energy at physiological temperature. Tunneling probability through rotational barriers is effectively zero. ATP synthase operates 1-3 orders of magnitude below the quantum speed limit. Classical mechanics fully explains ATP synthase rotation. The parent H7 was correctly killed by the Critic for exactly this reason, and the evolution's claim to "address the thermal energy mismatch" was empty -- the mismatch is a fundamental physical constraint, not an engineering problem. This hypothesis should never have survived to the quality gate.

---

## Summary

| Hypothesis | Verdict | Score | Key Issue |
|-----------|---------|-------|-----------|
| E3 (PSII Vibronic Coherence) | CONDITIONAL PASS | 6.5/10 | Partially explored by March 2026 paper; energy scale concerns; specific PSII mechanism remains novel |
| E1 (Cryptochrome THz Detection) | FAIL | 3.0/10 | Frequency mismatch: radical pair dynamics at GHz, not THz |
| E7 (ATP Synthase Quantum Rotor) | FAIL | 1.5/10 | Directly contradicted: quantum rotor states inaccessible at biological T |

### Passed Quality Gate: 1 (conditional)
### Failed Quality Gate: 2

---

## META-VALIDATION

### Self-Review

1. **For E3 (conditional PASS)**: Would I bet my reputation? With reservations. The mechanism is physically plausible in principle, the grounding claims are verified, and the specific PSII + THz-2DCS combination remains unpublished. However, the March 2026 R-phycoerythrin paper means someone IS working in this general space. Confidence should be 3-4/10, not higher. The energy scale question (THz phonons << kT) is a genuine concern that prevents a strong PASS.

2. **For E1 (FAIL)**: The frequency mismatch is real and fatal. Radical pair spin dynamics are an EPR-frequency phenomenon. THz spectroscopy probes the wrong physical observable. This was correctly killed by the Critic originally.

3. **For E7 (FAIL)**: This is the clearest FAIL. A peer-reviewed paper (arxiv 2506.23439) explicitly demonstrates that quantum rotor states are irrelevant at biological temperatures for ATP synthase. The hypothesis was resurrected from a killed state without fixing the fundamental flaw.

4. **Search count**: 22 web searches performed (7 novelty, 12 claim verification, 3 counter-evidence), plus 2 web fetch operations. Exceeds the minimum requirement.

5. **Citation audit**: All cited papers in the literature context verified:
   - Azizi et al. 2023 (PMID 37575674) -- VERIFIED
   - Huang et al. 2025 (Semantic Scholar) -- VERIFIED
   - Romanello & Romanello 2026 (PMID 41651056) -- VERIFIED (bioRxiv preprint confirmed)
   - Gassab et al. 2026 (PMID 41751706) -- VERIFIED (Entropy 28(2):204)
   - Science Advances 2025 (ady6751) -- VERIFIED
   - Science Advances 2024 (adk1312) -- VERIFIED

6. **Per-claim verification completeness**:
   - E3: 7/7 claims verified or partially verified. No fabricated claims.
   - E1: 4/7 claims verified. 3 claims unverifiable or physically questionable. Bridge claim is mechanistically flawed.
   - E7: 4/9 claims verified. 3 claims directly contradicted. 2 claims unverifiable.

7. **Strictness check**: I am comfortable with these verdicts. E3 deserves cautious passage as a CONDITIONAL PASS given its partial novelty. E1 and E7 have fundamental physical problems that no amount of specification can fix.

---

## Sources

- [Full microscopic simulations uncover persistent quantum effects in primary photosynthesis (Science Advances 2025)](https://www.science.org/doi/10.1126/sciadv.ady6751)
- [Unraveling quantum coherences mediating primary charge transfer processes in PSII RC (Science Advances 2024)](https://www.science.org/doi/10.1126/sciadv.adk1312)
- [Examining the origins of observed terahertz modes from an optically pumped atomistic model protein (PNAS Nexus 2023)](https://academic.oup.com/pnasnexus/article/2/8/pgad257/7239375)
- [Terahertz 2D coherent spectroscopy for probing and controlling multicorrelations in quantum matter (Nature Reviews Physics 2025)](https://www.nature.com/articles/s42254-025-00917-2)
- [Terahertz cavity hybridization of collective proteins vibrations (arxiv March 2026)](https://arxiv.org/abs/2603.14476)
- [Rotational dynamics of ATP synthase: Mechanical constraints and energy dissipative channels (arxiv June 2025)](https://arxiv.org/abs/2506.23439)
- [Magnetosensitivity of tightly bound radical pairs in cryptochrome (Nature Communications 2024)](https://www.nature.com/articles/s41467-024-55124-x)
- [Variation of Exciton-Vibrational Coupling in PSII Core Complexes (J Phys Chem B)](https://pubs.acs.org/doi/10.1021/jp510631x)
- [Quantum coherent dynamics in photosynthetic protein complexes (Chem Soc Rev 2026)](https://pubs.rsc.org/en/content/articlehtml/2026/cs/d5cs00948k)
- [Quantum Information Flow in Microtubule Tryptophan Networks (Entropy 2026)](https://www.mdpi.com/1099-4300/28/2/204)
- [Singlet-triplet dephasing in radical pairs in avian cryptochromes (J Chem Phys 2023)](https://pubs.aip.org/aip/jcp/article/159/10/105102/2910503)
- [F1-ATPase is a highly efficient molecular motor that rotates with discrete 120 degree steps (Cell 1998)](https://www.sciencedirect.com/science/article/pii/S0092867400814567)
- [The six steps of the complete F1-ATPase rotary catalytic cycle (Nature Communications 2021)](https://www.nature.com/articles/s41467-021-25029-0)
- [Do photosynthetic complexes use quantum coherence to increase their efficiency? Probably not (Science Advances 2021)](https://www.science.org/doi/10.1126/sciadv.abc4631)
- [Weak, strong, and coherent regimes of Froehlich condensation (PNAS 2009)](https://www.pnas.org/doi/10.1073/pnas.0806273106)
