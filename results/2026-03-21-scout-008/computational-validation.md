# Computational Validation Report

## Target: Cuproptosis (copper-induced cell death) × Hydrothermal Vent Copper-Sulfide Geochemistry
## Session: 2026-03-21-scout-008
## Bridge Concepts: FDX1 ferredoxin Cu2+ reductase, DLAT lipoyl Cu binding, Cu+/Cu2+ Pourbaix speciation, chalcopyrite CuFeS2 analog, copper chaperones, elesclomol-Cu2+ complex

---

### Check 1: Thermodynamic Feasibility — Cu2+/Cu+ Speciation at Mitochondrial Conditions

**Nernst equation:**
```
Eh = E0 + (RT/nF) × ln([Cu2+]/[Cu+])
R = 8.314 J/(mol·K), T = 310.15 K (37°C), F = 96485 C/mol, n = 1
RT/nF = 26.725 mV
E0(Cu2+/Cu+) = +159 mV (standard, pH-independent for free ions)
```

**Results — Cu2+/Cu+ ratio at various Eh:**

| Eh (mV) | [Cu2+]/[Cu+] | Cu+ favored by |
|---|---|---|
| -200 | 1.47 × 10⁻⁶ | 6.8 × 10⁵ |
| -250 | 2.26 × 10⁻⁷ | 4.4 × 10⁶ |
| -280 | 7.35 × 10⁻⁸ | 1.4 × 10⁷ |
| **-300** | **3.48 × 10⁻⁸** | **2.9 × 10⁷** |
| -320 | 1.65 × 10⁻⁸ | 6.1 × 10⁷ |
| -400 | 8.24 × 10⁻¹⁰ | 1.2 × 10⁹ |
| -500 | 1.95 × 10⁻¹¹ | 5.1 × 10¹⁰ |

At mitochondrial Eh (-280 to -320 mV), Cu⁺ is overwhelmingly favored at equilibrium by a factor of 10⁷–10⁸.

**FDX1 driving force:**
```
E0(FDX1) = -274 mV (midpoint potential)
E0(Cu2+/Cu+) = +159 mV
ΔE_cell = E0(cathode) - E0(anode) = (+159) - (-274) = +433 mV
ΔG = -nFΔE = -(1)(96485)(0.433) = -41.8 kJ/mol
```

**CRITICAL FINDING — Thermodynamic Redundancy Paradox:**
At mitochondrial Eh = -300 mV, Cu⁺ is already favored by 2.9 × 10⁷ : 1 at equilibrium. The ΔG for FDX1-mediated Cu²⁺ reduction is -41.8 kJ/mol (strongly favorable), but the ambient redox environment already thermodynamically dictates Cu⁺ dominance. FDX1 is therefore **thermodynamically redundant but experimentally essential** (Tsvetkov et al. 2022). This paradox resolves if FDX1 is a **kinetic facilitator**: the mitochondrial Eh is set by the NADH/NAD⁺ couple, not by freely available electrons. Cu²⁺ reduction requires a specific electron donor to provide the kinetic pathway, even though the thermodynamic destination (Cu⁺) is already favored.

**pH effect:** Cu²⁺/Cu⁺ couple is pH-independent for free ions (no H⁺ involved in Cu²⁺ + e⁻ → Cu⁺). However, Cu²⁺ hydrolysis (CuOH⁺, pKa ~7.5) means at pH 8.0, ~76% of any Cu²⁺ present is hydrolyzed, further reducing effective free Cu²⁺ availability.

**Verdict: PLAUSIBLE — with critical caveat that FDX1's role is kinetic, not thermodynamic**

---

### Check 2: Pourbaix Diagram Validity — Cu-S-H₂O System at 37°C

**Mitochondrial matrix Cu speciation:**

| pH | Eh (mV) | Cu⁺/Cu²⁺ ratio | Cu²⁺ as CuOH⁺ |
|---|---|---|---|
| 7.5 | -280 | 1.36 × 10⁷ | 50% |
| 7.5 | -300 | 2.88 × 10⁷ | 50% |
| 7.5 | -320 | 6.08 × 10⁷ | 50% |
| 8.0 | -280 | 1.36 × 10⁷ | 76% |
| 8.0 | -300 | 2.88 × 10⁷ | 76% |
| 8.0 | -320 | 6.08 × 10⁷ | 76% |
| 8.2 | -280 | 1.36 × 10⁷ | 83% |
| 8.2 | -300 | 2.88 × 10⁷ | 83% |
| 8.2 | -320 | 6.08 × 10⁷ | 83% |

**Alkaline hydrothermal vent Cu speciation:**

| pH | Eh (mV) | Cu⁺/Cu²⁺ ratio |
|---|---|---|
| 9 | -400 | 1.21 × 10⁹ |
| 9 | -500 | 5.12 × 10¹⁰ |
| 9 | -600 | 2.16 × 10¹² |
| 10 | -400 | 1.21 × 10⁹ |
| 10 | -500 | 5.12 × 10¹⁰ |
| 11 | -500 | 5.12 × 10¹⁰ |

**KEY FINDING — Speciation Overlap:**
Both environments place Cu firmly in the Cu⁺ stability field. The mitochondrial matrix and moderate hydrothermal vents share identical Cu speciation (Cu⁺ dominance) despite different pH and Eh ranges. The overlap zone is centered at Eh ~-300 mV, pH ~8–9.

**Covellite/chalcocite stability at mitochondrial conditions:**
- Ksp(CuS, covellite) = 10⁻³⁶
- Ksp(Cu₂S, chalcocite) = 10⁻⁴⁸
- At pH 8, Cu⁺ dominates → Cu₂S is the more relevant phase
- Cu₂S precipitation from 10 μM Cu⁺ requires [S²⁻] > 10⁻³⁸ M — any detectable sulfide triggers precipitation
- In healthy mitochondria: sulfide is sequestered in Fe-S clusters, not free
- During cuproptosis: Fe-S cluster degradation releases sulfide, potentially enabling Cu₂S/CuS formation

**Verdict: PLAUSIBLE — Cu speciation is identical in both environments; covellite/chalcocite thermodynamically stable when sulfide is available**

---

### Check 3: Concentration Compatibility

| Parameter | Cuproptosis | Hydrothermal Vents | Comparison |
|---|---|---|---|
| Total Cu | ~10 μM (Tsvetkov 2022) | 1–100 μM | **SAME ORDER** |
| Free Cu | <10⁻¹⁸ M (attomolar) | Ligand-complexed | Both negligible |
| Cu speciation | Cu⁺ (Eh -300 mV) | Cu⁺ (Eh -300 to -600 mV) | Identical |
| Cu ligands | Chaperones (ATOX1, CCS, COX17) | Organic complexes (up to 4 μM) | Both organic-buffered |
| Sulfide | Sequestered in Fe-S clusters | 1–12 mM free H₂S/HS⁻ | Vents >> cells |

**At cuproptosis threshold (10 μM Cu total) at Eh = -300 mV:**
- [Cu⁺] ≈ 10.0 μM (essentially all Cu)
- [Cu²⁺] ≈ 0.0003 nM (vanishingly small at equilibrium)

**Critical insight:** The Cu concentration regime where cuproptosis occurs (10 μM) is exactly the Cu concentration regime in moderate hydrothermal vent fluids (1–100 μM). Both systems manage Cu through competing organic ligand transfer, not free Cu chemistry. This concentration match is the strongest quantitative bridge between the two fields.

**Biological buffering:** GSH-Cu⁺ (log K ~11.6) at [GSH] = 1–10 mM provides substantial Cu buffering capacity (>> 10 μM). Cuproptosis requires overwhelming this buffering system. In vents, organic ligands serve an analogous buffering role.

**Verdict: PLAUSIBLE — concentration regimes match within one order of magnitude**

---

### Check 4: Fe-S Cluster Displacement by Cu⁺

**Irving-Williams series:** Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺
Cu²⁺ has the highest stability constant of all first-row divalent transition metals with most ligands.

**Stability constants with biological thiolate (cysteine S):**
- Fe²⁺ + RS⁻: log K ≈ 5–6
- Cu⁺ + RS⁻: log K ≈ 12–14 (Cu⁺ prefers soft S donors)

**Displacement equilibrium: Cu⁺ + [Fe-S] → [Cu-S] + Fe²⁺**
```
log K(displacement) ≈ log K(Cu-S) - log K(Fe-S) = 13 - 5.5 = 7.5
K(displacement) = 10^7.5 = 3.16 × 10⁷
ΔG(displacement) = -RT ln K = -44.5 kJ/mol
```

**50% displacement of Fe²⁺ from [2Fe-2S] at [Fe²⁺] = 1 μM requires [Cu⁺] = 3.2 × 10⁻¹⁴ M = 0.032 pM.** Even trace Cu⁺ strongly displaces Fe²⁺ from sulfide coordination. This explains why cells maintain free Cu at attomolar levels (<10⁻¹⁸ M) — even picomolar Cu⁺ would destabilize Fe-S clusters.

**Literature confirmation:** Macomber & Imlay 2009 (PNAS, PMID 19416816) — "The iron-sulfur clusters of dehydratases are primary intracellular targets of copper toxicity." Demonstrated experimentally in E. coli that Cu⁺ specifically destroys solvent-exposed [4Fe-4S] clusters in dehydratases (fumarase, isopropylmalate isomerase). This is direct mechanistic validation of the Cu→Fe-S displacement bridge concept, 13 years before cuproptosis was formally defined.

**Chalcopyrite (CuFeS₂) analogy:**
| Property | Chalcopyrite | Cuproptosis intermediate |
|---|---|---|
| Cu oxidation state | Cu⁺ | Cu⁺ |
| Fe oxidation state | Fe³⁺ | Fe³⁺ (in [2Fe-2S]) |
| Coordination | Tetrahedral MS₄ | Tetrahedral Cys-S |
| Displacement drive | Thermodynamic | Thermodynamic |
| Temperature | 200–350°C | 37°C |
| Long-range order | Crystalline | Molecular |

**Verdict: PLAUSIBLE — Cu⁺ displaces Fe²⁺ with K = 10⁷·⁵. Chalcopyrite analogy valid at molecular bonding level. Literature support from Macomber & Imlay 2009.**

---

### Check 5: PubMed Co-occurrence Matrix

Queries run via PubMed MCP tool (2026-03-22):

| Query | Count | Assessment |
|---|---|---|
| cuproptosis AND Pourbaix | 0 | **DISJOINT** |
| cuproptosis AND speciation | 3 | Not relevant (nanoparticle/biosensor papers) |
| FDX1 AND geochemistry | 0 | **DISJOINT** |
| copper Pourbaix biological cell | 0 | **DISJOINT** |
| elesclomol speciation copper | 0 | **DISJOINT** |
| cuproptosis AND hydrothermal | 3 | Not relevant (nanoparticle synthesis methods) |
| chalcopyrite biological analog | 0 | **DISJOINT** |
| lipoylation copper binding dithiolane | 0 | **DISJOINT** |
| ferredoxin copper reduction mitochondria | 2 | FDX1 review (2025) + elesclomol paper (2023) |
| copper displaces iron sulfur cluster | 5 | **KEY**: Macomber & Imlay 2009 (PMID 19416816) |

**Positive control:** ferroptosis AND serpentinization = 2 papers (known cross-domain, false-positive MeSH expansion)

**Co-occurrence verdict:** The cuproptosis × geochemistry bridge is CONFIRMED DISJOINT. Zero papers connect cuproptosis mechanistic biology to Pourbaix diagram speciation frameworks. The only relevant cross-domain paper is Macomber & Imlay 2009, which demonstrated Cu→Fe-S displacement in bacteria but did not connect this to geochemical mineral frameworks or Pourbaix analysis. No paper has applied Eh-pH speciation diagrams to understand cuproptosis Cu chemistry.

---

### Check 6: Back-of-Envelope — Key Quantitative Bridges

**6A. Elesclomol vs lipoyl binding competition:**
```
Ka(elesclomol-Cu²⁺) = 10^17.1 = 1.26 × 10¹⁷
Ka(lipoyl-Cu) = 1/Kd = 1/10⁻¹⁷ = 10¹⁷
Ratio = 1.26 (COMPARABLE)
```
Elesclomol and the lipoyl moiety of DLAT have nearly identical Cu binding affinity. This explains the efficient Cu delivery from elesclomol to lipoylated TCA proteins — thermodynamic transfer is near-isoenergetic.

**6B. CuS as thermodynamic sink:**
```
Ksp(CuS) = 10⁻³⁶
At [S²⁻] = 1 μM: equilibrium [Cu²⁺] = 10⁻³⁰ M
```
CuS precipitation is 10¹² more favorable than any biological Cu binding (Kd ~10⁻¹⁷). If free sulfide becomes available during Fe-S cluster degradation in cuproptosis, CuS/Cu₂S formation represents a massive thermodynamic sink that would sequester all available Cu. This has implications for cuproptosis kinetics: does Cu-sulfide precipitation terminate the death process by removing bioavailable Cu?

**6C. Cu²⁺ hydrolysis at mitochondrial pH:**
At pH 8.0: 76% of Cu²⁺ exists as CuOH⁺ (pKa ~7.5). This further reduces effective free Cu²⁺ concentration beyond what Nernst predicts from Eh alone.

---

## Summary Table

| Check | Result | Verdict | Confidence |
|---|---|---|---|
| 1. Thermodynamic feasibility | Cu⁺ dominates at mito Eh; FDX1 kinetically necessary | **PLAUSIBLE** | High |
| 2. Pourbaix diagram | Cu⁺ stability field in both environments | **PLAUSIBLE** | High |
| 3. Concentration match | 10 μM cuproptosis ≈ 1–100 μM vent Cu | **PLAUSIBLE** | High |
| 4. Fe-S displacement | K = 10⁷·⁵; Macomber 2009 confirmation | **PLAUSIBLE** | High |
| 5. PubMed co-occurrence | 0 papers at intersection | **DISJOINT** | High |
| 6. Back-of-envelope | ES-Cu ≈ lipoyl-Cu affinity; CuS massive sink | **PLAUSIBLE** | Medium |

## Key Findings

1. **Cu speciation is identical** in mitochondria and hydrothermal vents — Cu⁺ dominates by 10⁷–10¹² in both environments. This is the foundational quantitative bridge.

2. **Concentration regimes match**: cuproptosis threshold (10 μM) falls within vent Cu range (1–100 μM). Both systems use organic ligand buffering.

3. **FDX1 thermodynamic redundancy paradox** is a novel insight: at mitochondrial Eh, Cu⁺ is already overwhelmingly favored. FDX1's essentiality must be kinetic, not thermodynamic. This reframes FDX1's role and opens the question of whether ancient abiotic Cu²⁺ reduction at vents preceded enzymatic catalysis.

4. **Cu→Fe displacement is quantitatively validated**: K = 10⁷·⁵, requiring only picomolar Cu⁺ for 50% displacement. Macomber & Imlay 2009 provides direct experimental confirmation.

5. **The fields are genuinely DISJOINT**: zero papers apply Pourbaix/Eh-pH speciation to cuproptosis. The geochemical framework has never been brought to bear on this biology.

6. **CuS precipitation during cuproptosis** is a novel prediction: Fe-S cluster degradation releases sulfide → meets excess Cu⁺ → thermodynamically inevitable Cu₂S/CuS formation. This is testable by TEM/EDX of cuproptotic mitochondria.

## Concerns for Generator

1. **Do NOT claim FDX1 "drives" Cu²⁺ reduction thermodynamically.** The mitochondrial Eh already dictates Cu⁺. FDX1 is a kinetic facilitator — frame accordingly.
2. **Ligand-extended Pourbaix diagrams are hypothetical** (session evaluation condition). Standard Cu-H₂O Pourbaix is established; adding biological thiolate ligands requires new calculations without published precedent.
3. **Chalcopyrite analogy is valid at molecular level only** — not crystallographic. Do not imply cuproptosis produces mineral chalcopyrite.
4. **CuS formation in mitochondria requires free sulfide release** — this is pathological (during Fe-S degradation), not basal. Frame as a cuproptosis-specific prediction, not a general mitochondrial phenomenon.
5. **Elesclomol-Cu²⁺ vs lipoyl-Cu binding affinity match** (Ka ratio 1.26) is a strong quantitative point — emphasize in hypotheses about Cu delivery mechanisms.
6. **Cite Macomber & Imlay 2009** (PMID 19416816) for Fe-S displacement — it is the strongest published mechanistic support for the Cu→Fe-S bridge, predating the cuproptosis field by 13 years.

## Recommendation

**GO — with caution on thermodynamic framing**

All six checks are PLAUSIBLE. The quantitative bridges are strong: identical Cu speciation, matching concentration regimes, validated displacement thermodynamics. The fields are confirmed DISJOINT with zero papers at the intersection. The main risk is overstatement of thermodynamic driving forces (FDX1 redundancy paradox) and premature claims about ligand-extended Pourbaix diagrams. Generator should lead with concentration matching and Fe-S displacement (strongest bridges) and treat Pourbaix reframing as a novel analytical contribution rather than an established framework.
