---
name: literature-retrieval
description: Systematic scientific literature retrieval via web search and structured database APIs (PubMed, KEGG, STRING). Auto-loaded when searching for papers, checking novelty, finding counter-evidence, querying pathway databases, or building literature context for hypothesis generation.
user-invocable: false
---

# Literature Retrieval Skill

## Search Strategies by Database

### Semantic Scholar (via web search)
- `site:semanticscholar.org "[exact phrase]"`
- Good for: citation networks, related papers, influence metrics

### PubMed (via web search)
- `site:pubmed.ncbi.nlm.nih.gov [MeSH terms]`
- Good for: biomedical literature, clinical evidence

### arXiv (via web search)
- `site:arxiv.org [field] [concept] 2025 OR 2026`
- Good for: physics, math, CS, quantitative biology preprints

### bioRxiv (via web search)
- `site:biorxiv.org [concept] 2025 OR 2026`
- Good for: biology preprints, very recent unpublished work

### Google Scholar (via web search)
- `[concept A] [concept B] site:scholar.google.com`
- Good for: broad coverage, citation counts

## Cross-Field Search Patterns
To find if Field A and Field C have been connected:
1. `"[Field A]" "[Field C]" review OR survey`
2. `"[mechanism from A]" applied "[domain C]"`
3. `"[Field A]" "[Field C]" hypothesis OR proposes`

## Recency Filters
Always prioritize recent work. Add year filters:
- `[query] 2026` for latest
- `[query] 2025 OR 2026` for last ~18 months

## Absence Detection
If searches return no results, document this explicitly.
"No published work found connecting [A] and [C] as of [date]"
is a valuable finding — it confirms novelty.

## Structured Database APIs (via WebFetch)

Beyond web search, use these REST APIs for **structured, machine-readable data**
that web search cannot provide — pathway maps, protein interactions, ontological
cross-references. These are especially valuable for mechanism-level discovery.

### PubMed E-Utilities (NCBI)
Structured metadata, MeSH terms, citation links — more precise than `site:pubmed`.

- **Search**: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=10&term=[QUERY]`
- **Fetch abstract**: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=[PMID]`
- **Related articles**: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id=[PMID]&cmd=neighbor_score&retmode=json`

Use case: find papers linking two MeSH terms, then follow citation graph via elink.
Query syntax: use `[MeSH]` qualifiers (e.g., `autophagy[MeSH]+AND+neoplasms[MeSH]`).

### KEGG REST API
Pathway cross-referencing — the single most useful API for "latent link" discovery.
Maps genes → pathways → diseases → drugs, enabling mechanistic bridging.

- **Find pathways for a gene**: `https://rest.kegg.jp/link/pathway/hsa:[GENE_ID]`
- **Find genes in a pathway**: `https://rest.kegg.jp/link/hsa/[PATHWAY_ID]`
- **Pathway details**: `https://rest.kegg.jp/get/[PATHWAY_ID]`
- **Search by keyword**: `https://rest.kegg.jp/find/pathway/[KEYWORD]`
- **Cross-reference pathway↔disease**: `https://rest.kegg.jp/link/disease/[PATHWAY_ID]`
- **List all human pathways**: `https://rest.kegg.jp/list/pathway/hsa`

Discovery pattern: gene from Field A → KEGG pathways → shared pathway with gene from Field C → latent mechanistic link.

### STRING Protein Interaction Network
Protein-protein interaction data with confidence scores. Validates whether
two proteins (from different fields) have known or predicted interactions.

- **Interactions for a protein**: `https://string-db.org/api/json/network?identifiers=[PROTEIN]&species=9606`
- **Interaction between two proteins**: `https://string-db.org/api/json/network?identifiers=[PROT_A]%0d[PROT_B]&species=9606`
- **Functional enrichment**: `https://string-db.org/api/json/enrichment?identifiers=[PROTEIN]&species=9606`

Species 9606 = human. Confidence scores: >0.9 highest, >0.7 high, >0.4 medium.
Use case: check if proteins from two apparently unrelated pathways have predicted interactions.

### When to Use APIs vs Web Search

| Need | Use |
|---|---|
| "What papers exist on X?" | Web search |
| "What pathways involve gene X?" | KEGG API |
| "Do proteins A and B interact?" | STRING API |
| "What MeSH terms link fields A and C?" | PubMed E-Utilities |
| "Recent breakthroughs in X" | Web search |
| "Mechanistic pathway connecting X to Y" | KEGG API → STRING API |
| "Citation network around paper X" | PubMed elink |

### API Error Handling
- If an API returns empty results, this is informative (no known link).
- If an API is unreachable, fall back to web search equivalent.
- Rate limits: add 1-second pauses between sequential API calls to the same service.

## Citation Quality
- Peer-reviewed journal > preprint > blog/news
- Nature/Science/Cell > specialized journals > conference proceedings
- Note: preprints may contain errors not caught by peer review
