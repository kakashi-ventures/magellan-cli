# Collagen Density Regulates the Activity of Tumor-Infiltrating T Cells

**Authors:** Dorota E. Kuczek, Daniel H. Madsen et al. (Copenhagen University Hospital Herlev)
**Journal:** Journal for ImmunoTherapy of Cancer, 7:68 (2019)
**DOI:** 10.1186/s40425-019-0556-6
**PubMed:** PMID 30867051
**PMC:** PMC6417085

## Abstract Summary
High-density collagen matrix (4 mg/mL) suppresses T cell proliferation, shifts CD4:CD8 ratio, and impairs cytotoxic killing compared to low-density matrix (1 mg/mL). Mechanism involves TGF-β autocrine signaling and downregulation of cytotoxic activity genes.

## Key Quantitative Findings
- **Collagen concentrations tested**: 1 mg/mL (LD, healthy tissue mimic) vs. 4 mg/mL (HD, tumor mimic)
- **Proliferation**: Significantly reduced in HD matrix; CD4:CD8 ratio increased after 5 days
- **Cytotoxic killing**: CD8+ T cells in HD matrix showed dramatically reduced killing of autologous melanoma cells (51Cr-release assay)
- **Transcriptomics**: 6 of 7 cytotoxic activity markers downregulated in HD vs. LD conditions
- **Signaling**: SMAD4/FOXO1 motifs upregulated → autocrine TGF-β pathway activated
- **Clinical correlation**: Reduced CD8+ T cell infiltration in human breast cancers with high collagen density (IHC)

## Methods
- 3D collagen gel culture of primary T cells at 1 mg/mL and 4 mg/mL
- Whole transcriptome RNA-seq
- 51Cr-release killing assay with autologous melanoma cells
- Flow cytometry for T cell subset analysis
- Human breast cancer tissue IHC analysis

## Key Numbers for Percolation Modeling
- **Low density (healthy)**: 1 mg/mL collagen — permissive state (p > p_c in percolation terms)
- **High density (tumor)**: 4 mg/mL collagen — exclusion state (p < p_c)
- Pore size at 1 mg/mL: ~50 µm (permissive to T cell passage)
- Pore size at 4 mg/mL: estimated ~5–10 µm (restrictive vs T cell nuclear diameter 8–10 µm)
- Note: Paper does NOT measure MSD, migration speed, or diffusion coefficients

## Critical Gap
- Tests only two concentrations (1 vs. 4 mg/mL) — no dose-response to identify a sharp threshold
- No connection to percolation theory or ECM connectivity metrics
- Gap: No paper has measured T cell MSD across a continuous range of collagen density to identify a percolation-like transition point

## Relevance to Session 015
- Provides functional evidence that collagen density switches T cells from active-killing to excluded state
- The 1→4 mg/mL jump likely spans a percolation threshold in ECM pore connectivity
- Motivates measuring T cell MSD vs. continuous LOX activity (crosslinking density) to find p_c

## Source URLs
- https://pubmed.ncbi.nlm.nih.gov/30867051/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6417085/
