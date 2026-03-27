# Meltome Atlas — Thermal Proteome Stability Across the Tree of Life

**Authors:** Jarzab A, Kurzawa N, Hopf T, Moerch M, et al.
**Year:** 2020
**Journal:** Nature Methods
**DOI:** 10.1038/s41592-020-0801-4
**PMID:** 32284610
**URL:** https://www.nature.com/articles/s41592-020-0801-4

## Abstract
A mass spectrometry-based proteomic approach was used to compile an atlas of the thermal stability of 48,000 proteins across 13 species ranging from archaea to humans, covering melting temperatures of 30–90°C. Protein sequence, composition, and size affect thermal stability in prokaryotes; eukaryotic proteins show a nonlinear relationship between the degree of disordered protein structure and thermal stability. Evolutionary conservation of protein complexes is reflected by similar thermal stability of their proteins. Proteins of the respiratory chain were found to be very stable in many organisms, and human mitochondria showed close to normal respiration at 46°C. Cell-type-specific effects can affect protein stability or the efficacy of drugs.

## Key Findings Relevant to Candidate 1 (EVT × Proteome Thermal Vulnerability)

1. **Distribution scope:** 48,000 proteins across 13 species — the largest Tm distribution dataset currently available.
2. **Tm range:** 30–90°C covered. Critically, **up to 20% of the proteome has Tm values outside measurable ranges**, indicating heavy tails or extreme-outlier proteins that are methodologically problematic under current statistical approaches.
3. **Gap with EVT:** The paper uses descriptive statistics (mean, SD) for Tm distributions — no extreme value theory formalism (GEV, Gumbel, Weibull, peaks-over-threshold) is applied at any point.
4. **Organism-level gap:** All eukaryotes show a substantial gap between optimal growth temperature (OGT) and the temperature at which proteins begin to precipitate. This "safety margin" is exactly the kind of return-level problem EVT was designed to address.
5. **Statistical approach used:** t-tests and z-tests with known limitations for tail behavior; GPMelt (Gaussian process) proposed as alternative but no EVT.

## Relevance to Disjointness
This paper represents the state of the art in proteome thermal stability data. It explicitly does NOT use extreme value statistical approaches. The 20% of proteins with Tm outside measurable ranges represents the methodological gap that EVT is uniquely positioned to address.
