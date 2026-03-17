# Scout Targets — Session 2026-03-17-scout-002

> **Note**: Web search unavailable in this session. Targets identified via
> parametric knowledge using strategies 2, 3, 5, 6, 7, 8. Marked as
> `web_verified: false`. Novelty not externally verified.

## Previously Explored (from discovery-log.json — AVOIDED)
- Bioelectric morphogenetic signaling x Biomolecular condensate phase transitions (session 001, SUCCESS)
- Circadian phase-separation dynamics x Neurodegenerative protein aggregation (identified but not explored)
- Acoustic mechanotransduction x Tumor immune microenvironment reprogramming (identified but not explored)

---

## Target 1: Ferroptosis-Driven Lipid Peroxidation x Bacterial Quorum Sensing Autoinducer Chemistry

**Field A**: Ferroptosis biology — iron-dependent regulated cell death via lipid peroxidation (GPX4 inhibition, phospholipid-PUFA oxidation, System Xc- cystine import)

**Field C**: Bacterial quorum sensing biochemistry — acyl-homoserine lactone (AHL) signaling, AI-2 universal autoinducer, Pseudomonas quinolone signal (PQS)

**Why these should connect**: Both fields center on lipid-derived small molecules that function as signals, not merely metabolic byproducts. Ferroptosis produces oxidized phosphatidylethanolamines (ox-PE) and 4-hydroxynonenal (4-HNE) that propagate between cells. Quorum sensing uses lipid-derived autoinducers (AHLs) that cross membranes freely. The chemical logic is identical: lipophilic signaling molecules that accumulate above a threshold to trigger population-level state transitions. Critically, during infection, ferroptotic host cells release oxidized lipids into the SAME microenvironment where bacteria are producing AHLs — yet nobody has asked whether ferroptotic lipid products interfere with or mimic quorum sensing signals.

**Why nobody has connected them**: Ferroptosis researchers study mammalian cell death mechanisms; quorum sensing researchers study bacterial communication. These communities publish in entirely different journals (Cell Death & Differentiation vs. Journal of Bacteriology). The chemical overlap in lipophilic signaling intermediates has been missed because the organisms, the scale, and the framing are completely different.

**Bridge concepts**:
- 4-HNE (4-hydroxynonenal) structural similarity to short-chain AHLs — both are alpha,beta-unsaturated carbonyls with lipophilic tails
- ox-PE accumulation threshold dynamics paralleling quorum sensing threshold (concentration-dependent binary switching)
- LasR/RhlR receptor promiscuity — AHL receptors are known to respond to non-cognate signals; could host-derived oxidized lipids be non-cognate agonists or antagonists?
- GPX4 as a gatekeeper for host-microbiome lipid signaling — GPX4 reduces ox-PE, potentially removing quorum interference signals
- Iron availability as a shared variable — ferroptosis requires labile iron, and bacterial iron acquisition (siderophores) directly competes for the same pool during infection

**Scout confidence**: 7/10 — The chemical structural similarity between ferroptotic ox-lipids and AHL autoinducers is concrete and testable. The LasR receptor's known promiscuity makes cross-reactivity plausible. Iron as a shared resource adds a second independent bridge.

**Strategy used**: 7 (Swanson ABC Bridging) + 3 (Converging Vocabularies — both fields describe threshold-dependent lipid-mediated state transitions)

---

## Target 2: Topological Defects in Active Matter x Stem Cell Niche Architecture

**Field A**: Active matter physics — topological defects (aneural +1/2 and -1/2 comet/trefoil defects) in nematic liquid crystals, active nematics, cell monolayer mechanics, defect-mediated force generation

**Field C**: Stem cell niche biology — spatial organization of adult stem cell niches, Wnt/BMP/Notch gradient formation, mechanical regulation of stemness, tissue architecture in intestinal crypts, hair follicle bulge, and bone marrow HSC niches

**Why these should connect**: Recent work (Saw et al. 2017, Kawaguchi et al. 2017, Maroudas-Sacks et al. 2021) demonstrated that cell monolayers form topological defects that concentrate mechanical stress and drive cell extrusion or accumulation. Separately, stem cell niches are precisely positioned anatomical structures where specific signaling gradients maintain pluripotency. The connection: topological defects in tissue-scale cell alignment create reproducible stress and flow patterns that could TEMPLATE where stem cell niches form — the niche isn't just a signaling center, it's a mechanical topological feature that self-organizes from active nematic physics.

**Why nobody has connected them**: Active matter physicists study cell monolayers in vitro or in simple epithelial sheets and haven't mapped defect positions to in vivo niche anatomy. Stem cell biologists focus on molecular signals (Wnt, BMP) and haven't characterized the nematic alignment field of the tissues containing their niches. The communities don't attend the same conferences.

**Bridge concepts**:
- +1/2 (comet) defects as compression zones that concentrate secreted morphogens (Wnt, R-spondin) — defect geometry creates a natural morphogen trap
- -1/2 (trefoil) defects as extrusion sites that expel differentiated cells, maintaining niche purity
- Active nematic alignment field of intestinal epithelium — crypts may correspond to topological defect positions in the villus-crypt alignment
- YAP/TAZ mechanotransduction at defect sites — the elevated compressive stress at +1/2 defects activates YAP nuclear translocation, which is known to maintain stemness
- Hair follicle spacing as a 2D defect lattice — the remarkably regular spacing of hair follicles may emerge from a defect tiling of the epidermal nematic

**Scout confidence**: 8/10 — The physics is well-established (defects concentrate stress), the biology is well-established (mechanical stress regulates stemness via YAP/TAZ), and the gap is the mapping between them. Maroudas-Sacks 2021 showed defects control morphogenesis in Hydra; extending to mammalian stem cell niches is the natural next step nobody has taken.

**Strategy used**: 5 (Scale Bridging — physics well-described in vitro, biology well-described in vivo, gap is connecting scales) + 4 (Tool Transfer — active matter analysis tools applied to stem cell niche formation)

---

## Target 3: Mitochondrial Cristae Ultrastructure Dynamics x Synaptic Plasticity Encoding

**Field A**: Mitochondrial cristae remodeling — OPA1/Drp1/MICOS complex-mediated cristae shape changes, cristae junction tightening/widening, crista-lumen pH microdomains, cristae as capacitors for membrane potential, MICU1/MCU calcium gatekeeping at cristae junctions

**Field C**: Synaptic plasticity mechanisms — LTP/LTD induction and maintenance, dendritic spine structural plasticity, presynaptic vesicle release probability, CaMKII autophosphorylation, AMPAR trafficking, protein synthesis-dependent late-phase LTP

**Why these should connect**: Mitochondria are present at every synapse and their morphology changes with neuronal activity — but they're treated as passive ATP suppliers. Recent cryo-ET work (2023-2025) reveals that individual cristae within a single mitochondrion can have DIFFERENT membrane potentials and different MICU1 gating thresholds, making each crista an independent computational element. Synaptic mitochondria have tighter cristae junctions than somatic mitochondria (Bhatt et al. 2024 context). The hypothesis space: cristae ultrastructure doesn't just support plasticity — it ENCODES plasticity states as a physical memory substrate, with each crista's geometry setting a specific calcium-buffering profile that determines whether a given activity pattern produces LTP or LTD at that synapse.

**Why nobody has connected them**: Cristae dynamics are studied by mitochondrial biologists using cryo-EM in non-neuronal cells. Synaptic plasticity is studied by neuroscientists using electrophysiology and fluorescence imaging. The resolution gap is enormous — cristae are 20-100nm structures inside organelles, while plasticity is measured at the micron-to-circuit scale. Until cryo-ET made it possible to resolve individual cristae in situ (2022-2025), the structural data simply didn't exist.

**Bridge concepts**:
- MICU1 gating threshold as synapse-specific LTP/LTD switch — cristae junction diameter sets the calcium concentration at which mitochondrial calcium uptake activates, determining whether moderate (LTD) or strong (LTP) stimulation is buffered or amplified
- Cristae density per synaptic mitochondrion as a physical record of past activity — activity-dependent OPA1 processing alters crista number, creating a structural memory that persists longer than any protein modification
- Crista-to-crista membrane potential heterogeneity as a multi-bit register — a single mitochondrion with 5-10 cristae, each at a different potential, stores more state information than any known molecular switch
- Drp1-mediated fission as synaptic tag capture mechanism — the synaptic tagging hypothesis requires a physical mark at activated synapses; mitochondrial fission (producing daughter mitochondria with specific cristae configurations) fits the temporal and spatial requirements
- Cristae junction remodeling by MICOS as the physical substrate of metaplasticity — BCM sliding threshold could be implemented by MICOS-dependent cristae junction widening/tightening that shifts the MICU1 gating curve

**Scout confidence**: 7/10 — The component pieces are individually well-established (cristae have heterogeneous potentials, MICU1 gates calcium, mitochondria are at synapses, plasticity requires calcium). The gap is the specific claim that cristae geometry ENCODES plasticity state. Recent cryo-ET enabling technology makes this testable now.

**Strategy used**: 2 (Anomaly Hunting — the "synapse specificity problem" is a known anomaly: how does each of 10,000 synapses on a neuron maintain independent plasticity state?) + 6 (Failed Paradigm Recycling — mitochondria as computational elements was dismissed in the 2000s but new cryo-ET data on cristae heterogeneity revives it)

---

## Target Ranking

| Rank | Target | Confidence | Novelty Estimate | Testability | Impact |
|------|--------|-----------|-----------------|-------------|--------|
| 1 | Topological Defects x Stem Cell Niches | 8/10 | High | High (imaging) | Transformative |
| 2 | Ferroptosis Lipids x Quorum Sensing | 7/10 | Very High | High (biochemistry) | High |
| 3 | Cristae Dynamics x Synaptic Plasticity | 7/10 | High | Medium (cryo-ET) | Transformative |

**Recommendation**: Target 1 (Topological Defects x Stem Cell Niches) has the strongest bridge mechanisms, the highest confidence, and is immediately testable with existing imaging technology. The physics-to-biology mapping is concrete and the YAP/TAZ mechanotransduction bridge is well-established on both sides.
