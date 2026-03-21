# Final Hypotheses — Session 007
## Fe-S Cluster Biogenesis x Circadian Clock Regulation
### 2026-03-21 | Status: SUCCESS | 5 hypotheses approved (1 PASS + 4 CONDITIONAL_PASS)

---

## Pipeline Summary
- **Generated**: 15 hypotheses across 2 cycles
- **Survived critique**: 10 (67%)
- **Passed Quality Gate**: 5 of 6 evaluated (83%)
- **Kill rate (critique)**: 33% | **Kill rate (QG)**: 17%
- **Attrition rate (overall)**: 67% (15 generated -> 5 final)
- **Strategy**: network_gap_analysis | **Disjointness**: DISJOINT
- **Evolver**: Skipped both cycles (top-3 avg >= 6.5)

---

## HYPOTHESIS 1: PASS (Rubric 7.5/10)

```
=====================================================================
HYPOTHESIS: IRP1 [4Fe-4S] Cluster Occupancy as Feeding-Entrained
            Iron-Redox Chronostat
=====================================================================
ID: H2.1 (evolved from H4, Cycle 1 rank 1)
CONNECTION: Fe-S cluster biogenesis -->
            IRP1 [4Fe-4S] cluster occupancy oscillation
            (dual feeding-entrained iron supply + NAD+/NADH redox) -->
            Diurnal IRE-mRNA control (Nadimpalli 2024 mechanism)
CONFIDENCE: 6/10 (was 7; lowered by IRP2 dominance concern)
NOVELTY: Partially explored (IRP1 switch known; diurnal occupancy unmeasured)
GROUNDEDNESS: 8/10 -- all claims individually verified
IMPACT IF TRUE: High

MECHANISM
---------
IRP1 (ACO1) is a bifunctional protein: with its [4Fe-4S] cluster it
functions as cytoplasmic aconitase; without the cluster it binds iron-
responsive elements (IREs) in mRNAs for ferritin, TfR1, ferroportin,
and ALAS2 [GROUNDED: textbook, Rouault 2006]. Nadimpalli et al. 2024
(PMID 38773499) established that diurnal IRE-mRNA control is driven by
FEEDING rhythms, showed IRP1 protein is CONSTANT while IRP2 oscillates
10-fold, and explicitly noted IRP1 [4Fe-4S] cluster occupancy across 24h
has NOT been measured -- the key unmeasured variable.

Two feeding-entrained pathways converge on IRP1 cluster occupancy:

Pathway 1 (Iron supply): Postprandial iron absorption -> serum iron peak
(30-50% amplitude, Dale 1969; Schaap 2013) -> hepatocyte LIP increase ->
mitochondrial import via mitoferrin -> frataxin-dependent Fe2+ donation to
ISCU2 [GROUNDED: Bridwell-Rabb 2014] -> enhanced [2Fe-2S] -> [4Fe-4S]
assembly -> CIA2A-dependent IRP1 maturation [GROUNDED: Stehling 2013].

Pathway 2 (Redox): Postprandial NADH surge (~30% amplitude, Peek 2013) ->
more reducing environment -> stabilized Fe-S clusters on FDX2/ISCU2 ->
higher assembly rate. Nernst: 30mV shift = 3.07-fold Kd change [VERIFIED].

Combined: ~2-3 fold IRP1 cluster occupancy oscillation. IRP2 (10-fold
transcriptional oscillation) is the dominant IRE regulator; IRP1 provides
a faster-responding post-translational layer that is functionally DISTINCT
because it also modulates cytoplasmic aconitase enzymatic activity.

SUPPORTING EVIDENCE
- Nadimpalli 2024: IRP1 protein constant, cluster occupancy unmeasured
- Serum iron 30-50% diurnal oscillation (clinical data, multiple studies)
- NAD+/NADH ~30% amplitude in liver (Peek 2013 Science)
- CIA2A specifically matures IRP1 (Stehling 2013)
- Nernst 30mV -> 3.07-fold Kd shift (computational validation)
- IRP1-C437S constitutive IRE-BP mutant available
- Native gel assay distinguishes aconitase from IRE-BP form

COUNTER-EVIDENCE & RISKS
- IRP2 dominates (10-fold vs IRP1 2-3 fold): addressed by IRP2 KO test
- Nadimpalli 2024 attributes rhythm to FEEDING: hypothesis embraces this
- JCI 2026 BMAL1->ATP7A->Cu pathway: different mechanism (copper, not iron)
- IRP1 cluster half-life ~3h is estimated, not measured in cells

HOW TO TEST
1. IRP1 holo/apo time course (2 weeks, ~$8K): Native PAGE + aconitase
   activity at 4h intervals in mouse liver over 24h. Compare ad lib vs
   time-restricted feeding.
2. IRP2 KO separation test (3 months, ~$12K): If ferritin/TfR1 oscillation
   persists in IRP2 KO mice, IRP1 cluster occupancy is sufficient.
3. Aconitase activity (concurrent): Cytoplasmic aconitase at same timepoints
   -- uniquely attributable to holo-IRP1.

DOMAIN EXPERTS NEEDED:
- Iron homeostasis biochemist (IRP1/IRP2 regulation)
- Circadian biologist (feeding-entrained rhythms)
- Mouse genetics / hepatocyte culture specialist
=====================================================================
```

---

## HYPOTHESIS 2: CONDITIONAL_PASS (Rubric 6.4/10)

```
=====================================================================
HYPOTHESIS: CISD2 [2Fe-2S] as Redox-Gated ER-Mitochondrial Calcium
            Timer (Forward Direction Only)
=====================================================================
ID: H2.3 (evolved from H2, Cycle 1 rank 3)
CONNECTION: Fe-S cluster biogenesis -->
            CISD2 [2Fe-2S] redox sensitivity at MAMs -->
            Circadian ER-mitochondrial Ca2+ transfer modulation
CONFIDENCE: 5/10
NOVELTY: Novel (zero publications linking CISD2 to circadian function)
GROUNDEDNESS: 6/10 -- CISD2 biochemistry grounded; circadian link speculative
IMPACT IF TRUE: High

MECHANISM
---------
CISD2/NAF-1 is a [2Fe-2S] protein at the outer mitochondrial membrane,
positioned at MAMs where it regulates Ca2+ transfer from ER to mitochondria
via IP3R [GROUNDED: Loncke 2025; Karmi 2018]. The 3Cys:1His coordination
makes the cluster uniquely labile and redox-sensitive [GROUNDED: PDB 3FNV].
CISD2 is a longevity gene: overexpression extends mouse lifespan; knockout
causes premature aging [GROUNDED: Chen 2009; Wu 2012].

Forward-only mechanism (feedback loop dropped per Cycle 1 critique):
Clock -> NAD+/NADH oscillation (30% amplitude) -> CISD2 [2Fe-2S] cluster
redox state modulation -> altered CISD2 conformation at MAMs -> oscillating
ER-to-mitochondria Ca2+ transfer.

Key refinement: CISD2's cluster is MORE stable than mitoNEET at physiological
pH but REMAINS redox-sensitive [GROUNDED: Biomedicines 2021]. The cluster
acts as a molecular SENSOR -- it stays on CISD2 and modulates conformation
based on redox state. Predicted: ~15% mito Ca2+ oscillation from CISD2
(50% cluster redox cycling x 30% CISD2 Ca2+ contribution).

RESOLVE BEFORE PUBLICATION:
- CISD2 redox midpoint is ~0mV at pH 7.5 (NOT -10mV from mitoNEET)
- Cluster half-life in cellulo remains unmeasured

SUPPORTING EVIDENCE
- CISD2 at MAMs, regulates Ca2+ via IP3R (Loncke 2025)
- 3Cys:1His labile coordination (Karmi 2018 JBIC; PDB 3FNV)
- Cluster stable at physiological pH but redox-sensitive (Biomedicines 2021)
- NAD+/NADH ~30% amplitude (Peek 2013)
- Longevity gene (Chen 2009)
- Zero CISD2 x circadian publications (PubMed verified)

COUNTER-EVIDENCE & RISKS
- CISD2 cluster stability vs redox sensitivity tension unresolved
- Multiple MAM Ca2+ regulators (MFN2, VDAC1, GRP75) -- CISD2 is one input
- CISD2 KO aging phenotype confounds circadian analysis
- Pioglitazone binds CISD2 (IC50 4.8uM) but Paddock 2007 is mitoNEET paper

HOW TO TEST
1. CISD2-roGFP2 fusion (3 months, ~$15K): Redox reporter on CISD2 in
   synchronized U2OS cells. Image at 4h intervals for 48h.
2. Mito Ca2+ readout (concurrent): Mito-R-GECO simultaneously with
   CISD2-roGFP2. Predict phase-locked oscillation.
3. CISD2 KO circadian (4 months, ~$20K): CISD2 KO in SCN2.2 cells,
   PER2::Luc rhythm. Predict altered amplitude.
4. Pioglitazone stabilization: Add pioglitazone -> predict dampened
   Ca2+ oscillation (cluster locked).

DOMAIN EXPERTS NEEDED:
- NEET protein biochemist (CISD2 redox chemistry)
- ER-mitochondria Ca2+ signaling specialist
- Circadian biologist (SCN2.2 reporter assays)
- Aging researcher (CISD2 longevity connection)
=====================================================================
```

---

## HYPOTHESIS 3: CONDITIONAL_PASS (Rubric 6.3/10)

```
=====================================================================
HYPOTHESIS: CIA Pathway as LIP/ROS-Responsive Circadian Gate for
            Cytoplasmic Fe-S Proteome
=====================================================================
ID: H2.6 (FRESH, Cycle 2)
CONNECTION: Fe-S cluster biogenesis -->
            CIAO3 LIP/ROS sensitivity (Maio & Rouault 2022) -->
            Coordinated circadian maturation of ~20 cytoplasmic
            Fe-S proteins (XPD, ABCE1, IRP1, POLD1)
CONFIDENCE: 4/10 (lowered from 5 by Critic)
NOVELTY: Novel (CIAO3 circadian regulation never proposed)
GROUNDEDNESS: 7/10 -- all cited literature verified (6/6 claims)
IMPACT IF TRUE: Transformative

MECHANISM
---------
The CIA targeting complex (CIA1/CIAO1-CIA2B/CIAO2B-MMS19) delivers
[4Fe-4S] clusters to all cytoplasmic and nuclear Fe-S proteins. CIAO3/IOP1
is a regulatory node whose interaction with the scaffold complex is
dynamically regulated by LIP, ROS, and O2 tension [GROUNDED: Maio & Rouault
2022, JBC, PMC9243173]:
- Iron supplementation STRENGTHENS CIAO3-CIA interactions
- Iron chelation WEAKENS them
- ROS exposure WEAKENS them
- Low O2 STRENGTHENS them

These two inputs (LIP, ROS) both oscillate circadianly (serum iron via
hepcidin; ROS via Prx/ETC cycles). During the fed state: higher LIP +
lower ROS = maximal CIA efficiency = robust cytoplasmic Fe-S maturation.
During fasting: lower LIP + higher ROS = reduced CIA efficiency.

This creates a daily gate affecting ~20 cytoplasmic Fe-S proteins
simultaneously: DNA repair (XPD), translation (ABCE1), iron regulation
(IRP1), DNA replication (POLD1).

RESOLVE BEFORE PUBLICATION:
- Extrapolation from acute pharmacological perturbation to circadian context
- Cytoplasmic LIP oscillation amplitude after ferritin buffering uncertain
- JCI 2026 BMAL1->ATP7A->Cu overlap needs explicit distinction

SUPPORTING EVIDENCE
- CIAO3 regulated by LIP, ROS, O2 (Maio & Rouault 2022 JBC)
- CIA2A specifically matures IRP1 (Stehling 2013)
- ~20 cytoplasmic Fe-S proteins identified as CIA targets
- Serum iron oscillates diurnally (clinical data)
- ROS oscillates circadianly (Edgar 2012)

COUNTER-EVIDENCE & RISKS
- CIAO3 sensitivity shown in acute perturbation, not circadian timescale
- Cytoplasmic LIP oscillation ~10-15% may be below CIAO3 sensitivity
- Target protein half-lives (24-72h) may dampen functional oscillation
- Relationship to BMAL1->ATP7A->Cu pathway (JCI 2026) unclear

HOW TO TEST
1. CIAO3 co-IP time course (3 months, ~$15K): CIAO3 with CIA1/MMS19
   at 4h intervals in synchronized HepG2. Predict oscillating interaction.
2. XPD functional readout (2 months, ~$10K): NER efficiency (host cell
   reactivation assay) at 4h intervals. Predict circadian variation.
3. Iron chelation timing (2 months, ~$8K): DFO at peak vs trough of
   CIA activity -> predict differential sensitivity.

DOMAIN EXPERTS NEEDED:
- CIA pathway biochemist (CIAO3 regulation)
- DNA repair biologist (XPD/NER)
- Iron homeostasis researcher
- Circadian biologist (synchronized cell systems)
=====================================================================
```

---

## HYPOTHESIS 4: CONDITIONAL_PASS (Rubric 5.9/10)

```
=====================================================================
HYPOTHESIS: Frataxin-Gated Fe-S Assembly Oscillation via Mitochondrial
            LIP in FTMT-Negative Tissues
=====================================================================
ID: H2.2 (evolved from H8, Cycle 1 rank 2)
CONNECTION: Fe-S cluster biogenesis -->
            Frataxin iron donation gated by hepcidin-driven LIP
            (FTMT-absent tissues) -->
            Tissue-specific circadian Fe-S assembly rate
CONFIDENCE: 5/10 (lowered from 6)
NOVELTY: Novel (FTMT tissue-specificity argument is new)
GROUNDEDNESS: 6/10 -- frataxin role partially mischaracterized
IMPACT IF TRUE: High

MECHANISM
---------
Frataxin (FXN) donates Fe2+ to ISCU2 for [2Fe-2S] assembly [GROUNDED:
Bridwell-Rabb 2014; NOTE: frataxin is primarily allosteric activator].
Lill 2025 (Nature) shows FDX2:FXN ~1:1 stoichiometry is critical.

Key insight: FTMT (mitochondrial ferritin) is NOT expressed in liver
hepatocytes [GROUNDED: Santambrogio 2007]. FTMT is restricted to testis,
brain, and heart. In liver, the mitochondrial LIP is therefore LESS
buffered than the cytoplasmic pool (which has abundant H/L-ferritin).

Plasma iron oscillation (30-50% diurnal) -> hepatocyte cytoplasmic LIP
(ferritin-buffered, dampened to ~10-15%) -> mitochondrial import via
mitoferrin -> mitochondrial LIP (UNBUFFERED in liver, amplified to
~20-30%) -> frataxin Fe2+ availability -> Fe-S assembly rate.

Prediction: Liver (FTMT-negative) shows larger circadian amplitude of
Fe-S enzyme activity than heart (FTMT-positive). FA heterozygous carriers
(~50% frataxin, ~1:100 Europeans) show reduced circadian amplitude.

RESOLVE BEFORE PUBLICATION:
- Frataxin is allosteric activator, not simply iron donor (Bridwell-Rabb)
- Mitochondrial LIP oscillation is purely speculative (zero measurements)
- "Unbuffered" is overstated -- frataxin, ACO2 themselves bind iron

SUPPORTING EVIDENCE
- FDX2:FXN ~1:1 stoichiometry (Lill 2025 Nature)
- FTMT absent in liver (Santambrogio 2007)
- Hepcidin circadian regulation (Schaap 2013)
- FA carriers: ~50% FXN, ~1:100 Europeans
- Hepatocyte LIP ~0.2 uM (Cabantchik 2014)

COUNTER-EVIDENCE & RISKS
- No published diurnal LIP measurements in hepatocytes
- Mitoferrin circadian expression unknown
- Ferritin rapidly captures and releases iron, potentially time-averaging
- FTMT absence may reflect low mitochondrial iron demand, not vulnerability

HOW TO TEST
1. Mitochondrial LIP (3 months, ~$15K): Mito-FerroGreen in synchronized
   HepG2 at 4h intervals. Compare to calcein-AM (cytoplasmic LIP).
2. FXN knockdown (3 months, ~$12K): 50% reduction -> predict amplified
   oscillation amplitude.
3. FA carrier clinical (6 months, ~$50K): 20 carriers vs 20 controls,
   PBMC aconitase at 4 timepoints.
4. FTMT rescue (4 months, ~$20K): Express FTMT in HepG2 -> predict
   dampened mitochondrial LIP oscillation.

DOMAIN EXPERTS NEEDED:
- Friedreich's ataxia researcher / clinician
- Mitochondrial iron biochemist
- Hematologist (iron homeostasis)
- Clinical trial designer (carrier studies)
=====================================================================
```

---

## HYPOTHESIS 5: CONDITIONAL_PASS (Rubric 6.0/10)

```
=====================================================================
HYPOTHESIS: Conserved Fe-S Requirement in Clock Neurons --
            Drosophila to Mammalian SCN
=====================================================================
ID: H2.7 (FRESH, Cycle 2)
CONNECTION: Fe-S cluster biogenesis -->
            NFS1-dependent Fe-S supply in SCN neurons -->
            Clock neuron function and circadian behavioral rhythms
CONFIDENCE: 5/10 (lowered from 6; SCN firing rate error)
NOVELTY: Novel (Drosophila published; mammalian prediction novel)
GROUNDEDNESS: 6/10 -- one factual error (SCN 10 Hz is light-stimulated)
IMPACT IF TRUE: Transformative

MECHANISM
---------
Mandilaras & Missirlis 2012 (PMID 22885802) showed RNAi knockdown of 5
Fe-S biogenesis genes disrupts circadian locomotor activity in Drosophila
clock neurons [GROUNDED]. This is the ONLY mechanistic link between Fe-S
biogenesis and circadian clock function. 14 years with zero mammalian
follow-up [VERIFIED].

This hypothesis predicts the Drosophila phenotype reflects a CONSERVED
requirement for active Fe-S cluster biogenesis in clock neurons. SCN neurons
oscillate between ~2.5 Hz (day) and ~1.5 Hz (night) [CORRECTED: 10 Hz is
light-stimulated, not baseline]. This still requires robust mitochondrial
ATP production dependent on Complex I (8 Fe-S clusters), II, and III.

Prediction: Conditional NFS1 knockout in SCN neurons (NFS1flox/flox x
VIP-Cre-ERT2) abolishes circadian behavioral rhythms, phenocopying the
Drosophila result. The mechanism is metabolic -- neurons require continuous
Fe-S cluster repair to sustain firing rate oscillation.

REVERSE DIRECTION: This hypothesis asks "does Fe-S regulate the clock?"
(Fe-S -> Clock), complementary to H2.1-H2.6 (Clock -> Fe-S). The two
directions could form a bidirectional feedback loop.

RESOLVE BEFORE PUBLICATION:
- SCN firing rate corrected (2.5 Hz baseline, not 10 Hz)
- dCRY confound: Drosophila photoreceptor mechanism not conserved
- Mandilaras 2012 primary finding was Fer2LCH (ferritin), Fe-S genes secondary
- Distinguish Fe-S-specific vs general mitochondrial disruption

SUPPORTING EVIDENCE
- Mandilaras 2012: 5 Fe-S genes disrupt Drosophila circadian (PMID 22885802)
- 14-year gap with zero mammalian follow-up (PubMed verified)
- Complex I has 8 Fe-S clusters
- Fe-S biogenesis genes conserved across Drosophila and mammals
- NFS1flox mice likely available (EUCOMM)
- VIP-Cre-ERT2 transgenic lines published

COUNTER-EVIDENCE & RISKS
- dCRY-specific confound: Drosophila CRY is photoreceptor, not conserved
- Fe-S disruption may cause general neurodegeneration, not specific clock defect
- Mandilaras primary finding was Fer2LCH ferritin, not Fe-S genes
- Many mitochondrial disruptions affect circadian -- hard to distinguish

HOW TO TEST
1. Mouse genetics (6 months, ~$40K): NFS1flox/flox x VIP-Cre-ERT2.
   Tamoxifen induction in adults. Wheel-running in constant darkness.
2. Ex vivo SCN slice (3 months, ~$20K): PER2::Luc rhythms in NFS1-deleted
   SCN. Predict dampened amplitude.
3. SCN2.2 cell line (2 months, ~$10K): NFS1 siRNA in immortalized SCN
   cells. Measure bioluminescence rhythm.
4. Fe-S assessment (concurrent): Complex I and aconitase activity in
   NFS1-deleted SCN tissue at 4h intervals.

DOMAIN EXPERTS NEEDED:
- Drosophila circadian geneticist (Mandilaras 2012 context)
- SCN neurophysiologist
- Mouse genetics specialist (conditional knockouts)
- Mitochondrial neurobiologist
=====================================================================
```

---

## Unexplored Targets for Future Sessions

From Session 007 scouting, two targets were not selected:

1. **Cuproptosis x Chemolithotrophic copper-sulfide metabolism** (Target 1, score 7/10)
   - Strategy: mechanism_transfer
   - Bridge: FDX1/ferredoxin family, lipoylation pathway conservation
   - Status: DISJOINT, available for future session

2. **Biomolecular condensate physics x Antibiotic persistence** (Target 2, score 8/10)
   - Strategy: implicit_disjoint
   - Bridge: (p)ppGpp triggering both condensates and persistence
   - Status: DISJOINT, available for future session

---

## Cross-Model Validation

Export files were generated for manual validation (no API keys configured in environment).

To validate externally:
1. Open `results/2026-03-21-scout-007/export-gpt.md` and paste into ChatGPT with GPT-5.4 Pro
2. Open `results/2026-03-21-scout-007/export-gemini.md` and paste into Gemini AI Studio with 3.1 Pro
3. Hypotheses where 2+ models agree on high novelty + confidence are your best candidates

To enable automatic validation: set OPENAI_API_KEY and/or GEMINI_API_KEY in environment.
