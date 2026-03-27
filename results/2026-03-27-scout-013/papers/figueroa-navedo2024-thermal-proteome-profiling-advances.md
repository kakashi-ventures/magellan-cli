# Experimental and Data Analysis Advances in Thermal Proteome Profiling

**Authors:** Figueroa-Navedo AM, Ivanov AR
**Year:** 2024
**Journal:** Cell Reports Methods
**DOI:** 10.1016/j.crmeth.2024.100717
**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10921035/

## Abstract
A review examining method development in mass spectrometry-based thermal shift assays for investigating protein-ligand interactions, covering improvements in data processing, experimental strategies, and data analysis workflows that impact the quality of thermal proteome profiles.

## Key Findings Relevant to Candidate 1 (EVT × Proteome Thermal Vulnerability)

1. **Out-of-range protein problem:** "For up to 20% of the analyzed proteome, Tm values are not determined because they are presumably outside of the typically used temperature ranges." This quantifies the "invisible tail" problem.
2. **Statistical limitations of Tm-centric approaches:** "Statistical conclusions out of one parameter Tm using a t or a z test showed a higher rate of false negatives" — mainstream statistics inadequate for tail behavior.
3. **Temperature window selection:** "Selection of inadequate temperature windows" identified as a key unresolved challenge — this is the peaks-over-threshold problem in EVT language.
4. **GPMelt alternative:** Advocates for non-Tm-dependent methods that avoid curve fitting assumptions; still uses Gaussian processes, NOT extreme value distributions.

## Relevance to Disjointness
This 2024 review confirms the field has recognized the tail/extreme-value problem (proteins with extreme Tm) but is solving it with Gaussian processes — NOT with the statistically rigorous EVT framework designed specifically for tail behavior estimation.
