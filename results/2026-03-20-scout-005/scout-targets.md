# Scout Targets — Session 2026-03-20-scout-005

**Strategies used**: anomaly-first, tool-transfer, scale-bridging (3 of 8)
**Avoided domains**: bioelectric signaling, biomolecular condensates, active matter/nematics, stem cell niches, THz spectroscopy, biological quantum coherence

---

## Target 1: Mitochondrial Cristae Dynamics x Lyotropic Liquid Crystal Physics

**Strategy**: anomaly-first

| Dimension | Detail |
|-----------|--------|
| **Field A** | Mitochondrial cristae remodeling — how inner mitochondrial membrane folds restructure during apoptosis, metabolic state transitions, and bioenergetic adaptation (OPA1, MICOS complex, cardiolipin redistribution) |
| **Field C** | Lyotropic liquid crystal phase transitions — concentration-dependent mesophase behavior in amphiphilic lipid systems (lamellar → inverse hexagonal → cubic), governed by packing parameter and elastic curvature theory |
| **Bridge concepts** | Gaussian curvature elasticity, inverse hexagonal (H_II) phase transitions, cardiolipin cone-angle packing parameter, membrane bending moduli (kappa_c, kappa_G) |
| **Disjointness** | DISJOINT — Mitochondrial biologists model cristae through protein machinery (OPA1 GTPase, Mic60/Mic10 scaffolding). Liquid crystal physicists characterize identical lamellar-to-tubular geometric transitions as lyotropic phase behavior. Near-zero cross-citation between J. Biol. Chem./EMBO J. and Soft Matter/Langmuir on this topic. |

**The anomaly**: Cristae undergo dramatic geometric transformations (lamellar → tubular → vesicular) during metabolic transitions. Biologists attribute this entirely to protein-driven remodeling. Yet the mitochondrial inner membrane is 20-25% cardiolipin — a cone-shaped lipid whose packing parameter (P ~ 1.2-1.4) places it at the lamellar/inverse-hexagonal phase boundary. Lipid physicists have shown that cardiolipin-rich model membranes spontaneously undergo the exact same geometric transitions (lamellar → H_II → cubic) as a function of concentration, pH, and divalent cation binding.

**Key insight**: Cristae remodeling may be a cardiolipin-driven liquid crystal phase transition *modulated* by OPA1/MICOS, not a purely protein-scaffolded process. The cristae junction geometry (diameter ~12-20 nm, negative Gaussian curvature) matches predictions from Helfrich elastic theory for saddle-splay energy minimization at lyotropic phase boundaries, not predictions from protein-only scaffolding models.

**Thermodynamic plausibility**: Cardiolipin phase transitions occur at kT-scale energies (bending modulus ~10-20 kT for CL-rich membranes). Cristae remodeling timescales (seconds to minutes) are consistent with lipid mesophase kinetics. The free energy landscape is dominated by curvature elastic terms (Helfrich Hamiltonian) with protein contributions as perturbations (~2-5 kT per OPA1 dimer). Proton motive force across cristae membranes (~180 mV) generates sufficient electrostatic stress (~0.5-1.0 mN/m surface pressure) to shift phase boundaries.

**Falsifiable prediction**: Cristae geometry in cardiolipin synthase (CLS) mutants with graded CL depletion will follow lyotropic phase diagram predictions (lamellar stabilization at low CL, loss of tubular junctions), even when OPA1/MICOS levels are held constant. Cryo-ET of CL-depleted mitochondria should show a lamellar-locked state inconsistent with protein-scaffolding models.

**Confidence**: 8/10
**Target quality**: 8/10

---

## Target 2: Acoustic Mechanobiology x Topological Phononics

**Strategy**: tool-transfer

| Dimension | Detail |
|-----------|--------|
| **Field A** | Acoustic mechanotransduction — cellular responses to ultrasound and acoustic stimulation (LIPUS for bone healing, focused ultrasound neuromodulation, sonogenetics via Piezo1/MscL) |
| **Field C** | Topological phononics — engineered acoustic metamaterials exhibiting topologically protected edge states, one-way phonon transport, and backscatter-immune acoustic waveguiding (quantum spin Hall analogs for sound) |
| **Bridge concepts** | Phononic bandgap engineering at cellular length scales (~10-100 um), topologically protected acoustic edge modes, sub-wavelength acoustic focusing, frequency-selective acoustic delivery |
| **Disjointness** | DISJOINT — Mechanobiologists use bulk transducers with mm-scale spatial resolution and broadband frequency content. Topological phononics groups publish in Phys. Rev. Lett./Nature Physics on macroscopic metamaterials. No cross-citation between these communities. The length scale gap (metamaterial unit cells typically ~cm vs. cell diameter ~10 um) has prevented interaction. |

**The connection**: Topological phononics has demonstrated backscatter-immune acoustic waveguides, frequency-selective one-way transport, and acoustic "topological insulators" where sound propagates along edges without scattering. Meanwhile, acoustic mechanobiology struggles with two fundamental problems: (1) poor spatial selectivity — ultrasound stimulates entire tissue volumes, not specific cell populations, and (2) poor spectral control — broadband pulses activate all mechanosensitive channels simultaneously.

**Key insight**: Miniaturized topological phononic metamaterials (achievable via MEMS/nanofabrication at ~10-50 um unit cells for MHz frequencies) could serve as programmable acoustic delivery platforms for mechanobiology. Topologically protected edge states would enable: (a) spatially selective acoustic stimulation of individual cells or cell clusters without crosstalk, (b) frequency-selective delivery matching specific mechanosensitive channel resonances (Piezo1 ~MHz, MscL ~100 kHz), (c) robust delivery immune to scattering from tissue heterogeneity.

**Thermodynamic plausibility**: Acoustic energy delivered to cells in LIPUS (~30 mW/cm^2, ~1.5 MHz) corresponds to ~0.1-1.0 pN forces on membranes — sufficient for Piezo1 gating (threshold ~0.3-0.5 pN). Topological edge modes conserve energy (no backscatter loss), so delivered acoustic power would be higher and more spatially concentrated than conventional focused ultrasound. Phononic crystal unit cell size scales as ~lambda/2; for 1.5 MHz in water (lambda ~1 mm), this gives ~500 um unit cells — achievable with current microfabrication but still above single-cell resolution. Moving to 15 MHz gives ~50 um unit cells, matching cellular scales, though attenuation increases.

**Falsifiable prediction**: A topological phononic metamaterial substrate with MHz-frequency bandgap and edge states, co-cultured with Piezo1-expressing cells, will show >10-fold spatial selectivity in calcium signaling (cells on topological edge vs. bulk) compared to conventional planar ultrasound stimulation at matched intensity.

**Confidence**: 7/10
**Target quality**: 8/10

---

## Target 3: Ferroptosis x Serpentinization Geochemistry

**Strategy**: scale-bridging

| Dimension | Detail |
|-----------|--------|
| **Field A** | Ferroptosis — iron-dependent regulated cell death driven by lipid peroxidation, GPX4 inactivation, and failure of the cystine/glutathione antioxidant axis (major target in cancer therapy, neurodegeneration) |
| **Field C** | Serpentinization geochemistry — abiotic water-rock reactions at oceanic spreading centers where olivine (Fe2SiO4) reacts with water, oxidizing Fe(II) to Fe(III), generating H2, and producing diverse organic molecules including oxidized lipid species |
| **Bridge concepts** | Fe(II)/Fe(III) Fenton cycling, iron-mineral-catalyzed lipid peroxidation, phospholipid hydroperoxide intermediates (PLOOH), ferrihydrite surface catalysis, abiotic lipid oxidation products |
| **Disjointness** | DISJOINT — Ferroptosis researchers (Cell/Nature Cell Biology) study iron-dependent lipid peroxidation in mammalian cells. Geochemists (Geochimica et Cosmochimica Acta, PNAS Earth Sciences) study iron-mineral-catalyzed organic oxidation in hydrothermal systems. The identical core chemistry (Fe-catalyzed PUFA peroxidation) is studied independently with no cross-citation. Prebiotic chemistry provides a thin conceptual bridge but focuses on synthesis, not the peroxidation degradation pathway. |

**The connection**: Serpentinization generates Fe(III)-oxyhydroxide minerals (ferrihydrite, green rust) that catalyze lipid peroxidation through the same Fenton chemistry that drives ferroptosis. Geochemists have characterized the kinetics, product distributions, and mineral-surface catalytic mechanisms of iron-mediated lipid oxidation in detail — including the role of mineral surface area, Fe(II)/Fe(III) ratios, pH, and dissolved oxygen. These quantitative parameters map directly onto the intracellular ferroptosis environment: labile iron pool (~0.5-1.0 uM Fe(II)), lysosomal pH (~4.5-5.0), and membrane PUFA composition.

**Key insight**: Geochemical kinetic models of mineral-catalyzed lipid peroxidation could predict ferroptosis sensitivity across cell types based on labile iron pool speciation (Fe(II)/Fe(III) ratio, chelation state, mineral vs. free iron). Conversely, the evolved GPX4/GSH defense system in cells may illuminate why certain abiotic lipid peroxidation products are absent in serpentinization environments (selection against specific PLOOH species implies they were most lethal in prebiotic membrane contexts).

**Thermodynamic plausibility**: Fenton reaction thermodynamics are identical regardless of biological vs. geological context: Fe(II) + H2O2 -> Fe(III) + OH* + OH- (deltaG ~ -76 kJ/mol). The rate-limiting step in both systems is the same: Fe(II) regeneration from Fe(III) via reductants (GSH in cells, H2 in serpentinization). Lipid peroxidation propagation kinetics (k_prop ~10^2 M-1 s-1 for PUFA) are independent of the initiating context. The quantitative kinetic framework is directly transferable.

**Falsifiable prediction**: Cell lines ranked by ferroptosis sensitivity (RSL3 EC50) will correlate with a geochemistry-derived "peroxidation potential" index calculated from: labile iron pool Fe(II)/Fe(III) ratio x membrane PUFA unsaturation index x inverse GSH concentration — using rate constants from mineral-catalyzed lipid peroxidation literature rather than cell biology measurements. If the geochemical rate constants predict cellular ferroptosis kinetics (r > 0.7 across >10 cell lines), this validates the mechanistic identity.

**Confidence**: 7/10
**Target quality**: 7/10

---

## Target Quality Self-Check

| Criterion | Target 1 (Cristae x LC) | Target 2 (Acoustics x Topo) | Target 3 (Ferroptosis x Serp) |
|-----------|-------------------------|------------------------------|-------------------------------|
| Disjointness | Strong — different journals, different departments | Strong — physics vs. biology, length scale gap | Moderate — prebiotic chemistry creates thin bridge |
| Bridge specificity | Gaussian curvature, H_II phases, cardiolipin packing — all quantifiable | Phononic bandgaps, edge states — specific engineering parameters | Fenton kinetics, PLOOH intermediates — specific chemistry |
| Thermodynamic plausibility | Yes — kT-scale bending energies, physiological timescales | Yes — MHz acoustics, achievable fabrication | Yes — identical thermodynamics by definition |
| Falsifiability | CL depletion + cryo-ET is feasible | Metamaterial + cell culture is feasible (harder) | Cell line correlation is directly testable |
| Novelty risk | Moderate — some curvature work exists in biophysics, but not LC framing | Low — truly unexplored intersection | Moderate — iron chemistry is broad, but this specific bridge is new |
| Strategy diversity | anomaly-first | tool-transfer | scale-bridging |
