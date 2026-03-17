# Critiqued Hypotheses — Cycle 1
## Session: 2026-03-17-scout-001

---

## H1: Bioelectric Voltage Patterns Spatially Organize Condensate Landscapes via Calcium-Kinase Cascades

### Attack 1: Mechanism plausibility
**Counter-evidence:** The 2024 J Phys Chem Lett paper showed that external electric fields actually SUPPRESS LLPS (not promote it), which partially contradicts the idea that Vmem gradients would control condensate formation. However, this used AC fields on purified protein — intracellular conditions differ significantly (crowding, multicomponent systems, indirect calcium-mediated effects rather than direct electric field).

### Attack 2: Specificity problem
**Counter-evidence:** Calcium regulates hundreds of downstream pathways. Attributing condensate spatial organization specifically to calcium-dependent kinase phosphorylation of IDP scaffolds risks the "single cause attribution" fallacy. Many other calcium targets could explain observed correlations.

### Attack 3: Novelty check
**Web search result:** No published papers propose Vmem -> calcium -> kinase -> condensate spatial organization as a morphogenetic mechanism. NOVEL.

### Attack 4: Correlation vs causation
The prediction that depolarized cells have fewer condensates could be confounded by the hundreds of other differences between stem/proliferative cells and differentiated cells.

### Verdict: SURVIVES (weakened)
Core mechanism is plausible (calcium does facilitate phase separation per 2024 Nat Commun). Specificity concern is valid but addressable with targeted experiments. The direct electric field suppression result creates tension but applies to different conditions (AC in vitro vs indirect intracellular signaling).
**Confidence adjustment:** 5/10 -> 4/10

---

## H2: Gap Junction-Mediated Ion Sharing Creates Tissue-Scale Condensate Coherence Domains

### Attack 1: Size limitation
**Counter-evidence:** Gap junctions pass molecules < ~1 kDa. They can share ions (Ca2+, Mg2+, K+) and small metabolites (cAMP, IP3), but CANNOT share the IDP proteins that form condensates (typically 20-100+ kDa). So "isocondensate states" would depend entirely on shared ions creating identical local conditions, not shared condensate components.

### Attack 2: Ion concentration change magnitude
**Counter-evidence:** Gap junction-mediated ion transfer equilibrates concentrations but the magnitude of change in a receiving cell may be small. Bhatt 2024 showed 5x Mg2+ enrichment IN condensates, but this is driven by condensate formation itself, not by external Mg2+ delivery. The amount of Mg2+ shared via gap junctions may be insufficient to meaningfully shift condensate thresholds.

### Attack 3: Novelty check
**Web search:** No papers connect gap junction ion sharing to condensate coordination across cells. NOVEL.

### Attack 4: Testability
The prediction (gap junction blockade -> heterogeneous condensate states) is testable with carbenoxolone + condensate reporters, but carbenoxolone has many off-target effects.

### Verdict: SURVIVES (weakened)
The core logic holds — gap junctions share ions, ions affect condensate formation — but the quantitative argument is weak. Need specific modeling of how much ion sharing occurs and whether it reaches condensate-modifying thresholds.
**Confidence adjustment:** 4/10 -> 3/10

---

## H3: V-ATPase-Driven Local pH Microdomains Act as Condensate Nucleation Templates

### Attack 1: Strong mechanistic support
**SUPPORTING:** The 2025 Nature Chemistry paper explicitly showed condensates sustain pH gradients without energy input, and formation is pH-dependent. V-ATPase creates proton gradients. This is the most mechanistically grounded hypothesis.

### Attack 2: Spatial specificity concern
**Counter-evidence:** V-ATPase is primarily located on intracellular organelle membranes (lysosomes, endosomes), not plasma membrane in most cell types. Plasma membrane V-ATPase is restricted to certain specialized cells (osteoclasts, renal intercalated cells, some cancer cells). This limits the generality of the mechanism.

### Attack 3: pH buffering
**Counter-evidence:** Cytoplasmic pH is heavily buffered (typically 7.2 +/- 0.05). Local pH microdomains near V-ATPase would be rapidly dissipated by buffering. Only near-membrane or intra-organellar pH changes would be significant enough to nucleate condensates.

### Attack 4: Novelty check
**Web search:** No papers propose V-ATPase as a condensate nucleation template. NOVEL.

### Attack 5: V-ATPase in aging/neurodegeneration
**SUPPORTING:** V-ATPase expression declines with aging in neurons (Burrinha 2023). This connects to both bioelectric decline AND potential condensate dysregulation, strengthening the translational angle.

### Verdict: SURVIVES (moderate strength)
Strong mechanistic grounding. The pH buffering concern is real but surmountable near organellar membranes. V-ATPase localization limits plasma membrane effects but organellar condensate nucleation is plausible and interesting.
**Confidence adjustment:** 5/10 -> 5/10

---

## H4: Bidirectional Bioelectric-Condensate Feedback Creates Morphogenetic Bistability

### Attack 1: Feedback loop verification
**SUPPORTING:** Both directions are independently demonstrated: (A) Vmem -> condensates (indirect, via calcium/pH), and (B) condensates -> Vmem (direct, Bhatt 2024). Feedback loop existence is logically sound.

### Attack 2: Timescale mismatch
**Counter-evidence:** Condensate formation occurs on seconds-to-minutes timescale. Bioelectric pattern changes occur over hours-to-days (morphogenesis timescale). For bistability, both processes need to operate on compatible timescales. The rapid condensate dynamics may average out before influencing slow bioelectric changes.

### Attack 3: Many other feedback loops
**Counter-evidence:** The Vmem-proliferation-differentiation decision involves many feedback loops (ERK, Wnt, Notch signaling). Adding condensates to the list is not wrong but may not be the DOMINANT mechanism. Risk of "just another pathway" rather than a key switch.

### Attack 4: Novelty check
**Web search:** Bidirectional bioelectric-condensate feedback not proposed. NOVEL.

### Attack 5: Bimodality prediction
The prediction of bimodal Vmem + condensate distributions at morphogenetic boundaries is specific and falsifiable. This is a strength.

### Verdict: SURVIVES
The logic is sound and both directions are empirically supported. Timescale and dominance concerns are valid but don't kill the hypothesis. The bimodality prediction is strong.
**Confidence adjustment:** 5/10 -> 4/10

---

## H5: Bioelectric Dysregulation Drives Neurodegeneration Through Aberrant Condensate Phase Transitions

### Attack 1: Causal direction problem
**Counter-evidence:** The standard model is that protein aggregation causes neuronal dysfunction (including bioelectric changes). H5 inverts this. While Tabibzadeh (2024) discusses bioelectric aging as a target for intervention, no experimental evidence demonstrates that bioelectric decline PRECEDES aggregation. This is reverse causation until proven otherwise.

### Attack 2: V-ATPase decline evidence is mixed
**Counter-evidence:** V-ATPase decline in aging is documented but the effect size is modest (partial reduction), and neurons have many compensatory mechanisms. Gap junction decline with age is also documented but attributing condensate pathology to it specifically is a large inferential leap.

### Attack 3: Novelty check
**PARTIALLY EXPLORED:** Tabibzadeh (2024) in "Aging and Cancer" discusses membrane potential targeting for aging. Levin's group published "Aging as a loss of morphostatic information: A developmental bioelectricity perspective" (2024). These discuss bioelectric aging broadly but do NOT connect it to condensate phase transitions specifically. The condensate angle is NOVEL.

### Attack 4: Therapeutic prediction
The prediction that restoring bioelectric homeostasis normalizes condensate properties is testable but extraordinarily difficult experimentally.

### Verdict: SURVIVES (weakened)
The causal direction concern is serious and must be acknowledged. However, the specific mechanism (bioelectric -> condensate material properties -> aggregation) is novel and adds mechanistic specificity to the existing bioelectric aging framework.
**Confidence adjustment:** 4/10 -> 3/10

---

## H6: Morphogenetic Memory Is Physically Stored in Self-Sustaining Condensate-Voltage Circuits

### Attack 1: Alternative explanations
**Counter-evidence:** Planaria morphogenetic memory involves chromatin modifications and stable gene expression states. Levin's group acknowledges that "the permanent change of pattern memory also involves chromatin modification machinery." Condensate-voltage circuits would be one layer among many.

### Attack 2: Condensate lifetime problem
**Counter-evidence:** Most cytoplasmic condensates have lifetimes of minutes to hours (FRAP recovery times typically seconds to minutes). Morphogenetic memory persists for weeks to months. Even with self-sustaining Donnan potentials, individual condensates would turn over many times. The memory would need to be in the PATTERN of condensate formation, not in individual condensates.

### Attack 3: 1,6-hexanediol test is flawed
**Counter-evidence:** 1,6-hexanediol (used in proposed test) directly impairs kinases and phosphatases at standard concentrations (5-10%), causes chromatin condensation, and can rupture membranes. The proposed test (dissolve condensates, wash out, check if pattern returns) would be confounded by massive kinase/phosphatase inhibition and chromatin damage.

### Attack 4: Novelty check
**Web search:** No papers propose condensate-voltage circuits as morphogenetic memory storage. NOVEL but highly speculative.

### Verdict: SURVIVES (heavily weakened)
The core idea of condensate patterns encoding morphogenetic information is intriguing but faces serious challenges: condensate lifetime vs memory duration, and the confounded experimental test. Needs reformulation with better experimental approach.
**Confidence adjustment:** 4/10 -> 2/10

---

## H7: Circadian Bioelectric Oscillations Gate Daily Condensate Renewal, Preventing Aggregation

### Attack 1: Circadian ion channel regulation
**SUPPORTING:** Clock genes DO regulate ion channel expression rhythmically. Brown & Nagel (2025) show clock regulates stress granule formation via eIF2alpha. The circadian-condensate connection has emerging evidence.

### Attack 2: Missing direct evidence of Vmem oscillations
**Counter-evidence:** While circadian regulation of ion channels is documented, daily oscillations in tissue-level Vmem patterns (as opposed to single-cell membrane potential fluctuations) have not been clearly demonstrated. The bioelectric code framework deals with stable patterns, not oscillations.

### Attack 3: Circadian disruption -> aggregation is already partially explored
**Counter-evidence:** Circadian disruption worsens neurodegeneration (well-documented). The addition of "via condensate renewal failure" is novel but adds a layer of speculation on top of an existing observation.

### Attack 4: Novelty check
The circadian-condensate link itself is EMERGING (2025 publications). The specific bioelectric oscillation mechanism for condensate renewal is NOVEL.

### Attack 5: FRAP circadian oscillation test
The prediction (FRAP recovery oscillates with circadian time) is specific and testable. This is a strength.

### Verdict: SURVIVES
Good integration of three fields (circadian, bioelectric, condensate). Specific testable prediction. But builds on partially explored territory.
**Confidence adjustment:** 5/10 -> 4/10

---

## H8: Electric Field-Directed Condensate Positioning Explains Left-Right Asymmetry Breaking

### Attack 1: Competing mechanism is well-established
**CRITICAL COUNTER-EVIDENCE:** Left-right asymmetry breaking in vertebrates is primarily driven by nodal cilia generating leftward fluid flow, with Pkd2 mechanosensitive channels detecting the flow. This "nodal flow" model has extensive experimental support (2024 paper confirms even 2 cilia suffice). Bioelectric gradients are proposed as an EARLIER or PARALLEL mechanism (Levin), not the dominant one.

### Attack 2: Electric field magnitude problem
**Counter-evidence:** Endogenous electric fields in embryos are ~1-10 mV/mm. For electrophoretic movement of condensates (~100 nm diameter, modest charge), the force would be extremely small compared to thermal fluctuations (kT). Back-of-envelope calculation: electrophoretic force ~ qE ~ (10e) * (10 V/m) ~ 10^-17 N. Thermal force scale ~ kT/r ~ 10^-14 N. The electric field force is ~1000x too weak to overcome thermal noise.

### Attack 3: Timescale and diffusion
**Counter-evidence:** Even if the force were sufficient, condensates diffuse freely and would rapidly re-equilibrate. Sustained asymmetric positioning would require continuous electric field application, which conflicts with the transient nature of the symmetry-breaking event.

### Attack 4: Novelty check
**Web search:** No papers propose electric field-directed condensate positioning for laterality. NOVEL, but may be novel because the physics doesn't work.

### Verdict: KILLED
The electrophoretic force calculation is lethal. The force from physiological electric fields is ~1000x too weak to position condensates against thermal fluctuations. The dominant cilia-based mechanism is well-established. This hypothesis fails on basic physical grounds.
**Kill reason:** Electrophoretic force orders of magnitude too weak vs thermal noise. Established cilia-based mechanism explains the phenomenon.

---

## SUMMARY

| Hypothesis | Verdict | Post-Critique Confidence |
|---|---|---|
| H1 (Vmem-Ca-Kinase-Condensate) | SURVIVES (weakened) | 4/10 |
| H2 (Gap Junction Condensate Coherence) | SURVIVES (weakened) | 3/10 |
| H3 (V-ATPase pH Nucleation) | SURVIVES (moderate) | 5/10 |
| H4 (Bidirectional Feedback Bistability) | SURVIVES | 4/10 |
| H5 (Bioelectric Neurodegeneration) | SURVIVES (weakened) | 3/10 |
| H6 (Morphogenetic Memory Storage) | SURVIVES (heavily weakened) | 2/10 |
| H7 (Circadian Condensate Renewal) | SURVIVES | 4/10 |
| H8 (LR Asymmetry Condensate) | KILLED | 0/10 |

**Survivors:** 7 of 8
**Killed:** 1 (H8 — insufficient electrophoretic force)
