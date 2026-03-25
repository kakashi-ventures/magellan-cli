# Final Hypotheses
## Session: session-20260325-000727
## Date: 2026-03-25
## Fields: Stochastic thermodynamics (TUR) × Bacterial cell biology (adder model)
## Quality Gate: 1 PASS + 6 CONDITIONAL PASS out of 8 evaluated (1 FAIL: E-H4)

---

## #1 — PASS: FtsZ GTPase ~2000× Over-Dissipating vs DnaA — Precision Bottleneck at Initiation Not Division (C2-H5)

**Confidence: 7/10 | Groundedness: HIGH | Composite: 7.90**

### Connection
Stochastic thermodynamics (comparative TUR efficiency) → FtsZ GTP hydrolysis during ring treadmilling as a second independent molecular current → Prediction that division machinery operates in "structural-excess" regime where TUR is irrelevant to precision.

### Mechanism
The bacterial cell cycle involves two major entropy-producing molecular currents: DnaA-ATP hydrolysis at oriC (Σ_DnaA = 11 × 20 kBT = 220 kBT) and FtsZ-GTP hydrolysis in the Z-ring (Σ_FtsZ ≈ 300 × 6.5 GTP/min × 15 min × 15 kBT ≈ 405,000 kBT). The entropy production ratio is 1,840×. DnaA counting sets a TUR floor of CV ≥ 9.5%; FtsZ sets CV ≥ 0.22%. The precision bottleneck is definitively at INITIATION (DnaA), not at DIVISION (FtsZ). FtsZ's high entropy production serves MECHANICAL function (constriction force), not INFORMATIONAL function (precision timing).

### Falsification Test
FtsZ84 (temperature-sensitive GTPase mutant, ~10% activity) at semi-permissive temperature: CV_added should NOT increase significantly. dnaA46 (temperature-sensitive initiation mutant) at semi-permissive temperature: CV_added should increase by 15-30%. The ASYMMETRIC response identifies the precision bottleneck.

### Quality Gate Assessment
All key parameters independently verified: FtsZ kcat ~8/min (Romberg & Mitchison 2004), FtsZ treadmilling (Bisson-Filho 2017 Science), FtsZ84 well-characterized, dnaA46 standard lab allele, N_eff=11 (McGarry 2004). Calculation robust — even at lowest Z-ring occupancy (200), ratio exceeds 800×.

---

## #2 — CONDITIONAL PASS: Variance-Component Decomposition of E. coli Adder (E-H1)

**Confidence: 6/10 | Groundedness: MEDIUM | Composite: 8.30**

### Connection
TUR on DnaA-ATP counting → additive variance decomposition CV²_added = CV²_counting + CV²_spatial + CV²_period + CV²_extrinsic → two-regime phase transition: counting-dominated at fast growth, C+D-dominated at slow growth, crossover at 0.8-1.0 dbl/hr.

### Mechanism
At fast growth (>1.5 dbl/hr): DnaA counting noise dominates (>50% of CV²_total), CV_counting ≈ 8.4-9.5%. Min spatial error contributes ~9%, C+D ~20%. At slow growth (<0.5 dbl/hr): C+D period fluctuations dominate (>55%), DnaA counting drops to <25%. Phase transition near 0.8-1.0 dbl/hr marks where the precision regime switches from DnaA-limited to C+D-limited.

### Three Independent Test Protocols
1. MinCDE deletion + SlmA anchor → isolate spatial component
2. C+D period measurement by flow cytometry → isolate period component
3. Single-molecule DnaA-mVenus tracking → directly measure counting noise

### Quality Gate Assessment
Novel framework with testable predictions. All grounded claims verified. **Risk**: Genthon 2026 (arxiv 2601.05193) shows extrinsic noise dominates bacterial size variability — intrinsic decomposition may be experimentally unresolvable.

---

## #3 — CONDITIONAL PASS: ppGpp → Supercoiling → N_eff Reduction as Stress-Responsive TUR Tuning (C2-H2)

**Confidence: 5/10 | Groundedness: MEDIUM | Composite: 7.00**

### Connection
ppGpp stringent response → supercoiling relaxation → reduced I/τ-site DnaA binding (supercoiling-sensitive) → N_eff drops from 11 to 5-7 → TUR floor shifts from 9.5% to 12-14% → CV_added increases as thermodynamic necessity, not resource shortage.

### Discriminating Test
DnaA overexpression (3× WT) + SHX-induced stringent response. If CV increase is due to DnaA shortage: DnaA overexpression prevents it. If due to supercoiling-N_eff reduction: CV increase persists regardless of DnaA level. Prediction: CV increases to 14-17% with or without DnaA overexpression.

### Quality Gate Assessment
Three independently verified mechanistic steps (Fernández-Coll & Cashel 2020; McGarry 2004; Leonard & Grimwade 2015). **Risk**: Cooperative DnaA filament assembly may invalidate independent-site N_eff model. Novobiocin secondary test confounded by DARS2 effects.

---

## #4 — CONDITIONAL PASS: RIDA Kinetic Timing Window — U-Shaped CV vs Hda Titration (E-H2)

**Confidence: 5/10 | Groundedness: MEDIUM | Composite: 6.10**

### Connection
RIDA counter-reset kinetics bounded by minimum speed (incomplete reset → memory contamination) and maximum speed (premature erasure → counting window truncation) → optimal timing window coupled to β-clamp residence at oriC → U-shaped CV_added vs Hda concentration.

### Key Prediction
U-shaped CV response to Hda titration (10 levels, 0.1× to 10× WT): both knockdown AND overexpression increase CV above WT optimum. This discriminates kinetic timing window (U-shaped) from Landauer erasure (L-shaped) and simple counter-reset (monotonic).

### Quality Gate Assessment
U-shaped prediction is uniquely discriminating — no competing model predicts bidirectional sensitivity. **Risk**: RIDA may be dispensable (PNAS 2024, Løbner-Olesen lab), suggesting alternative counter-reset mechanisms. Maduike 2014 PLOS Genetics citation unverifiable (tool exists regardless).

---

## #5 — CONDITIONAL PASS: TUR Dominates Berg-Purcell for DnaA-oriC (C2-H6)

**Confidence: 4/10 | Groundedness: MEDIUM | Composite: 6.60**

### Connection
TUR counting bound (CV ≥ 9.5%) vs Berg-Purcell diffusive sensing bound (CV ≥ 0.9-3.3%) for DnaA at oriC → TUR dominates by 3-10× across all parameter ranges → precision bottleneck is THERMODYNAMIC (counting), not DIFFUSIVE (transport).

### Implication
DnaA-ATP molecules arrive at oriC fast enough (diffusion solved), but N_eff = 11 irreversible binding events is too few for high precision. Cells cannot improve adder precision by increasing DnaA mobility — only by redesigning oriC with more binding sites.

### Quality Gate Assessment
HIGHLY NOVEL — no prior paper compares TUR and BPL for the same biological system. Theoretical comparison robust across parameter ranges. **Critical flaw**: Primary experiment (DnaA L366K → increased mobility → unchanged CV) is fatally broken — DnaA(L366K) cannot initiate replication from oriC. Must redesign experimental handle. D_DnaA in vivo never measured.

---

## #6 — CONDITIONAL PASS: Multi-Current TUR Decomposition — Noise Portfolio (C2-H1)

**Confidence: 4/10 | Groundedness: MEDIUM | Composite: 6.60**

### Connection
Multi-current TUR framework → independent TUR bounds for DnaA (~1.1× floor), MinCDE (~25×), FtsZ (~50×) → "Noise portfolio" revealing 20-60× asymmetry: informational tasks (counting) operate near TUR optimality; structural/mechanical tasks (positioning, constriction) operate far above.

### Meta-Prediction
Informational-vs-structural TUR hierarchy: subsystems performing counting/threshold detection near-optimal; subsystems performing force generation/positioning massively over-dissipating. This hierarchy is itself testable.

### Quality Gate Assessment
Novel theoretical contribution — noise portfolio concept. Individual calculations verified. **Risk**: Independence assumption unjustified (DnaA-FtsZ STRING 0.920), Genthon 2026 extrinsic noise dominance renders intrinsic decomposition potentially unmeasurable. Sound theory, challenged experimental program.

---

## #7 — CONDITIONAL PASS: Min Pareto-Frontier TUR with Pattern Instability (E-H7)

**Confidence: 5/10 | Groundedness: MEDIUM | Composite: 5.20**

### Connection
MinCDE oscillation dissipation → Pareto frontier at pattern instability bifurcation → U-shaped σ_z/L vs MinD concentration, with minimum at WT density.

### Novel Predictions Beyond Fei & Bhatt 2015
1. TUR Pareto-frontier framework explaining WHY excess dissipation hurts precision
2. Bifurcation coincidence: pattern instability threshold C* coincides with precision loss onset
3. Quantitative efficiency: Min at ~3-5× from pattern-instability-limited floor (not naively 14×)
4. Temperature shift moves C* to lower MinD density

### Quality Gate Assessment
Extends Fei & Bhatt 2015 (PLOS Comput Biol) with quantitative TUR framework. Specific experimental predictions (CRISPRi MinD titration, bifurcation coincidence) novel. **Issues**: Citation error — "Barato & Seifert 2017, PRL 119:140604" is actually PRX 6:041053 (2016); qualitative U-shape partially published.

---

## FAILED — E-H4: DnaA-ATP Membrane-Affinity Gradient

**FAIL: MECHANISM IMPLAUSIBLE**

DnaA diffusion (D~3 μm²/s) homogenizes any spatial DnaA-ATP gradient within ~0.3 seconds. The counting process operates on minutes timescale. Péclet number ~0.002. Individual grounded claims (CL at poles, DnaA-CL recharging) are correct but combining them into a spatial gradient mechanism violates basic diffusion physics. Same analysis killed C2-H4 in cycle 2 critique.
