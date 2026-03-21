# Target Evaluation — Session 2026-03-20-scout-005

## Target 1: Mitochondrial Cristae Dynamics x Lyotropic Liquid Crystal Physics

| Axis | Verdict | Score | Detail |
|------|---------|-------|--------|
| Popularity Bias | **BLOCK** | 3/10 | Multiple review articles and quantitative studies already connect these fields. Ortiz et al. 2016, Renner & Bhatt 2011, Pezeshkian & Bhatt 2023 directly apply Helfrich elastic theory to cardiolipin in cristae. Boyd et al. 2023 and Wilson et al. 2019 quantify CL curvature sensing. This is an active research program, not a novel intersection. |
| Vagueness | PASS | 8/10 | Bridge concepts are specific and quantifiable: Gaussian curvature elasticity, HII phases, packing parameter P ~ 1.2-1.4. Experiment is directly writable from bridge. |
| Structural Impossibility | FLAG | 4/10 | HII phases are NOT observed in vivo in cristae. Cristae maintain bilayer topology stabilized by protein scaffolds (ATP synthase dimers, MICOS, OPA1). The framing conflates curvature preference with actual macroscopic phase transition. |
| Local-Optima | FLAG | 4/10 | Cristae/OPA1/MICOS was Session 2 target 3 (marked PARTIALLY_EXPLORED). Liquid crystal angle is new but core biological system is recycled. |

**Overall: BLOCK — Composite 4.75/10**
**Key concern**: This intersection is already actively studied in membrane biophysics; not a novel connection.

---

## Target 2: Acoustic Mechanobiology x Topological Phononics

| Axis | Verdict | Score | Detail |
|------|---------|-------|--------|
| Popularity Bias | PASS | 6/10 | Specific intersection (topological phononic metamaterials for cell stimulation) appears genuinely sparse. No direct cross-pollination papers found. |
| Vagueness | FLAG | 5/10 | Bridge lacks critical quantitative specs: frequencies, bandgap widths, material system, acoustic intensity at cell. Biological endpoint unclear — what does topological protection translate to biologically? |
| Structural Impossibility | **BLOCK** | 3/10 | Fundamental wavelength/cell-size mismatch. At 1 MHz (therapeutic ultrasound), wavelength = 1.5 mm; cell diameter ~10-20 um (100-150x mismatch). Achieving 10 um unit cells requires ~150 MHz where tissue attenuation is severe (sub-mm penetration). Manufacturing scalability of micrometer-scale topological devices undemonstrated. |
| Local-Optima | FLAG | 5/10 | Acoustic mechanotransduction recycled from Session 1 target 3. Physics angle (topology) is new. |

**Overall: BLOCK — Composite 4.75/10**
**Key concern**: Fundamental wavelength/cell-size mismatch makes single-cell acoustic stimulation physically implausible with current phononic crystal approaches.

---

## Target 3: Ferroptosis x Serpentinization Geochemistry

| Axis | Verdict | Score | Detail |
|------|---------|-------|--------|
| Popularity Bias | **PASS** | 9/10 | Zero papers connecting ferroptosis to serpentinization geochemistry. Extensive search confirmed: no cross-citations, no review articles, no conference sessions. Genuinely disjoint. |
| Vagueness | PASS | 7/10 | Bridge names specific chemistry: Fe(II)/Fe(III) Fenton cycling (known rate constants), PLOOH intermediates (specific molecules), ferrihydrite surface catalysis (named mineral + reaction). Testable prediction exists. |
| Structural Impossibility | FLAG | 5/10 | Large temperature/pH gap: serpentinization at 200-400C/pH 9-11 vs. ferroptosis at 37C/pH 7.4. Fenton reaction operates across both conditions but rate constants and surface chemistry differ. Mathematical form of kinetic models may transfer even if parameters need re-fitting. This is "nobody looked" not "people looked and it failed." |
| Local-Optima | PASS | 6/10 | Ferroptosis appeared in Session 2 but with completely different bridge (AHL molecular mimicry). Current bridge (mineral geochemistry) is entirely new. Serpentinization geochemistry never appeared in any session. |

**Overall: PASS — Composite 6.75/10**
**Key concern**: Temperature/pH gap between geochemical and biological conditions requires careful kinetic model adaptation.

---

## Recommendation

**Selected target: Target 3 (Ferroptosis x Serpentinization Geochemistry)**

Only target that passes all four axes without a BLOCK. Genuinely novel intersection with zero cross-citations, specific bridge chemistry, and real cross-disciplinary insight.
