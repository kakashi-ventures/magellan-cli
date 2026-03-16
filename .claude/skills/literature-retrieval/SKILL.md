---
name: literature-retrieval
description: Systematic scientific literature retrieval via web search. Auto-loaded when searching for papers, checking novelty, finding counter-evidence, or building literature context for hypothesis generation.
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

## Citation Quality
- Peer-reviewed journal > preprint > blog/news
- Nature/Science/Cell > specialized journals > conference proceedings
- Note: preprints may contain errors not caught by peer review
