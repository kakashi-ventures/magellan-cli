#!/usr/bin/env python3
"""Multi-API bioinformatics query tool for MAGELLAN Dataset Evidence Miner.

Queries public bioinformatics databases and returns structured JSON results.
Uses only Python stdlib — no pip dependencies required.

Usage:
    python3 scripts/query-biodata.py --type gene_expression --gene BRCA1 --tissue Breast
    python3 scripts/query-biodata.py --type protein_interaction --protein1 TP53 --protein2 MDM2
    python3 scripts/query-biodata.py --type pathway_check --gene TP53
    python3 scripts/query-biodata.py --type gwas_association --gene BRCA1 --trait "breast carcinoma"
    python3 scripts/query-biodata.py --type compound_target --compound aspirin --target COX2
    python3 scripts/query-biodata.py --type protein_function --protein TP53
    python3 scripts/query-biodata.py --type protein_structure --protein SOD2
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

TIMEOUT = 10  # seconds per API call
MAX_RETRIES = 2
RETRY_DELAY = 1.5  # seconds between retries


def api_request(url, headers=None, timeout=TIMEOUT):
    """Make an HTTP GET request with retry logic."""
    if headers is None:
        headers = {"Accept": "application/json"}
    headers.setdefault("User-Agent", "magellan/1.0 (scientific-discovery-pipeline)")
    last_error = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError,
                TimeoutError, OSError) as e:
            last_error = str(e)
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
    return None, last_error


def result(status, api, data=None, error=None):
    """Standard output envelope."""
    out = {"status": status, "api": api}
    if data is not None:
        out["data"] = data
    if error is not None:
        out["error"] = error
    return out


# ---------------------------------------------------------------------------
# 1. STRING — Protein-protein interaction
# ---------------------------------------------------------------------------
def query_string(protein1, protein2):
    species = 9606  # Homo sapiens
    ids = f"{urllib.parse.quote(protein1)}%0d{urllib.parse.quote(protein2)}"
    url = (f"https://string-db.org/api/json/network"
           f"?identifiers={ids}&species={species}&caller_identity=magellan")
    resp = api_request(url)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "STRING", error=resp[1])
    if not resp:
        return result("NO_DATA", "STRING", data={"query": f"{protein1} × {protein2}"})

    # Find the edge between the two proteins
    best_score = 0
    edge = None
    for item in resp:
        a = item.get("preferredName_A", "")
        b = item.get("preferredName_B", "")
        score = item.get("score", 0)
        if ({a.upper(), b.upper()} == {protein1.upper(), protein2.upper()} and
                score > best_score):
            best_score = score
            edge = item

    if edge and best_score > 0:
        return result("DATA_FOUND", "STRING", data={
            "protein1": edge.get("preferredName_A"),
            "protein2": edge.get("preferredName_B"),
            "combined_score": best_score,
            "experimental_score": edge.get("escore", 0),
            "textmining_score": edge.get("tscore", 0),
            "database_score": edge.get("dscore", 0),
            "interpretation": ("HIGH_CONFIDENCE" if best_score > 0.7
                               else "MEDIUM_CONFIDENCE" if best_score > 0.4
                               else "LOW_CONFIDENCE")
        })
    return result("NO_DATA", "STRING", data={"query": f"{protein1} × {protein2}",
                                              "note": "No interaction found"})


# ---------------------------------------------------------------------------
# 2. KEGG — Pathway check
# ---------------------------------------------------------------------------
def query_kegg(gene, pathway=None):
    # First: find KEGG gene ID from gene symbol
    url = f"https://rest.kegg.jp/find/hsa/{urllib.parse.quote(gene)}"
    headers = {"Accept": "text/plain"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            text = resp.read().decode("utf-8").strip()
    except Exception as e:
        return result("API_UNAVAILABLE", "KEGG", error=str(e))

    if not text:
        return result("NO_DATA", "KEGG", data={"query": gene, "note": "Gene not found in KEGG"})

    # Parse gene IDs — find EXACT symbol match (format: "hsa:7157\tTP53, BCC7, ...; description")
    gene_ids = []
    gene_upper = gene.upper()
    exact_id = None
    for line in text.split("\n"):
        parts = line.split("\t")
        if len(parts) >= 2:
            kegg_id = parts[0].strip()
            gene_ids.append(kegg_id)
            # Check for exact gene symbol match in the names before ";"
            names_part = parts[1].split(";")[0].strip()
            symbols = [s.strip().upper() for s in names_part.split(",")]
            if gene_upper in symbols:
                exact_id = kegg_id
                break

    if not exact_id and not gene_ids:
        return result("NO_DATA", "KEGG", data={"query": gene})

    # Get pathways for this gene (prefer exact match)
    kegg_id = exact_id or gene_ids[0]
    url2 = f"https://rest.kegg.jp/link/pathway/{kegg_id}"
    req2 = urllib.request.Request(url2, headers=headers)
    try:
        with urllib.request.urlopen(req2, timeout=TIMEOUT) as resp:
            text2 = resp.read().decode("utf-8").strip()
    except Exception as e:
        return result("API_UNAVAILABLE", "KEGG", error=str(e))

    pathways = []
    for line in text2.split("\n"):
        parts = line.split("\t")
        if len(parts) >= 2:
            pw = parts[1].strip().replace("path:", "")
            if pw.startswith("hsa"):
                pathways.append(pw)

    if pathway:
        # Check specific pathway
        pathway_id = pathway if pathway.startswith("hsa") else f"hsa{pathway}"
        found = pathway_id in pathways
        return result("DATA_FOUND" if found else "NO_DATA", "KEGG", data={
            "gene": gene, "kegg_id": kegg_id,
            "target_pathway": pathway_id,
            "found_in_pathway": found,
            "total_pathways": len(pathways)
        })
    else:
        return result("DATA_FOUND" if pathways else "NO_DATA", "KEGG", data={
            "gene": gene, "kegg_id": kegg_id,
            "pathways": pathways[:10],
            "total_pathways": len(pathways)
        })


# ---------------------------------------------------------------------------
# 3. Human Protein Atlas — Gene expression by tissue
# ---------------------------------------------------------------------------
def _hpa_fetch(url):
    """Fetch from Human Protein Atlas (usually returns gzipped JSON)."""
    import gzip
    import io
    last_error = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "magellan/1.0"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read()
                # Try gzip first (HPA usually returns gzipped content)
                if raw[:2] == b'\x1f\x8b':
                    buf = io.BytesIO(raw)
                    with gzip.GzipFile(fileobj=buf) as f:
                        return json.loads(f.read().decode("utf-8"))
                # Fallback to plain text
                return json.loads(raw.decode("utf-8"))
        except Exception as e:
            last_error = str(e)
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
    return None, last_error


def query_gene_expression(gene, tissue):
    # Query Human Protein Atlas for tissue expression data
    url = (f"https://www.proteinatlas.org/api/search_download.php"
           f"?search={urllib.parse.quote(gene)}"
           f"&format=json&columns=g,eg,rnats,rnatd,up,scml")
    resp = _hpa_fetch(url)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "HumanProteinAtlas", error=resp[1])
    if not resp:
        return result("NO_DATA", "HumanProteinAtlas",
                       data={"query": gene, "note": "Gene not found in HPA"})

    # Find exact gene match
    entry = None
    for item in resp:
        if item.get("Gene", "").upper() == gene.upper():
            entry = item
            break
    if not entry and resp:
        entry = resp[0]
    if not entry:
        return result("NO_DATA", "HumanProteinAtlas", data={"query": gene})

    rna_specificity = entry.get("RNA tissue specificity", "")
    rna_distribution = entry.get("RNA tissue distribution", "")
    uniprot = entry.get("Uniprot", "")
    single_cell = entry.get("RNA single cell type specificity", "")

    tissue_lower = tissue.lower()

    # Determine if gene is expressed in queried tissue
    # HPA specificity field includes tissue name when enriched
    tissue_match = tissue_lower in rna_specificity.lower()
    broadly_expressed = ("detected in all" in rna_distribution.lower() or
                         "detected in many" in rna_distribution.lower())

    if tissue_match:
        interpretation = "TISSUE_ENRICHED"
    elif broadly_expressed:
        interpretation = "BROADLY_EXPRESSED"
    elif "detected in some" in rna_distribution.lower():
        interpretation = "SELECTIVELY_EXPRESSED"
    elif "detected in single" in rna_distribution.lower():
        interpretation = "RARELY_EXPRESSED"
    elif "not detected" in rna_distribution.lower():
        interpretation = "NOT_DETECTED"
    else:
        interpretation = "UNKNOWN"

    is_expressed = interpretation in ("TISSUE_ENRICHED", "BROADLY_EXPRESSED",
                                      "SELECTIVELY_EXPRESSED")

    return result("DATA_FOUND", "HumanProteinAtlas", data={
        "gene": entry.get("Gene", gene),
        "ensembl": entry.get("Ensembl", ""),
        "query_tissue": tissue,
        "rna_tissue_specificity": rna_specificity,
        "rna_tissue_distribution": rna_distribution,
        "single_cell_specificity": single_cell,
        "tissue_match_in_specificity": tissue_match,
        "is_expressed": is_expressed,
        "interpretation": interpretation,
        "note": ("Gene is enriched in queried tissue" if tissue_match
                 else f"Gene is {rna_distribution.lower()}; specificity: {rna_specificity}"
                 if is_expressed
                 else f"Gene expression: {rna_distribution}")
    })


# ---------------------------------------------------------------------------
# 4. GWAS Catalog — Genetic associations
# ---------------------------------------------------------------------------
def query_gwas(gene, trait=None):
    # Step 1: Find SNPs for this gene
    url = (f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms"
           f"/search/findByGene?geneName={urllib.parse.quote(gene)}")
    headers = {"Accept": "application/json"}
    resp = api_request(url, headers, timeout=15)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "GWAS_Catalog", error=resp[1])
    if not resp:
        return result("NO_DATA", "GWAS_Catalog", data={"query": gene})

    embedded = resp.get("_embedded", {}) if isinstance(resp, dict) else {}
    snps = embedded.get("singleNucleotidePolymorphisms", [])
    if not snps:
        return result("NO_DATA", "GWAS_Catalog", data={"query": gene,
                                                         "note": "No SNPs found"})

    # Step 2: Get associations for top SNPs (follow _links)
    associations = []
    for snp in snps[:10]:
        rs_id = snp.get("rsId", "")
        # Get genomic contexts for trait info
        contexts = snp.get("genomicContexts", [])
        for ctx in contexts:
            gene_info = ctx.get("gene", {})
            gene_name = gene_info.get("geneName", "")
            if gene_name.upper() == gene.upper():
                # Follow associations link
                assoc_link = (snp.get("_links", {}).get("associations", {})
                              .get("href", ""))
                if assoc_link:
                    assoc_resp = api_request(assoc_link, headers, timeout=10)
                    if not isinstance(assoc_resp, tuple) and assoc_resp:
                        assoc_items = (assoc_resp.get("_embedded", {})
                                       .get("associations", []))
                        for a in assoc_items[:5]:
                            traits = a.get("efoTraits", [])
                            trait_name = traits[0].get("trait", "") if traits else ""
                            pval = a.get("pvalue")
                            try:
                                pval = float(pval) if pval else None
                            except (ValueError, TypeError):
                                pval = None
                            if trait_name:
                                associations.append({
                                    "rsid": rs_id,
                                    "trait": trait_name,
                                    "pvalue": pval,
                                })
                break  # Found matching gene context
        if len(associations) >= 20:
            break
        time.sleep(0.5)  # Rate limit between SNP association lookups

    # Step 3: Filter by trait if specified
    if trait and associations:
        trait_lower = trait.lower()
        filtered = [a for a in associations
                    if trait_lower in a.get("trait", "").lower()]
        if filtered:
            return result("DATA_FOUND", "GWAS_Catalog", data={
                "gene": gene,
                "query_trait": trait,
                "matching_associations": filtered[:10],
                "total_snps": len(snps),
                "total_associations": len(associations),
                "interpretation": "TRAIT_ASSOCIATED"
            })
        return result("NO_DATA", "GWAS_Catalog", data={
            "gene": gene, "query_trait": trait,
            "note": (f"Gene has {len(snps)} SNPs and {len(associations)} "
                     f"associations but none matching '{trait}'"),
            "available_traits": list(set(
                a["trait"] for a in associations if a["trait"]))[:10]
        })

    if associations:
        return result("DATA_FOUND", "GWAS_Catalog", data={
            "gene": gene,
            "total_snps": len(snps),
            "total_associations": len(associations),
            "top_associations": associations[:10]
        })

    return result("DATA_FOUND", "GWAS_Catalog", data={
        "gene": gene,
        "total_snps": len(snps),
        "total_associations": 0,
        "note": f"Found {len(snps)} SNPs but could not retrieve trait associations"
    })


# ---------------------------------------------------------------------------
# 5. ChEMBL — Compound-target activity
# ---------------------------------------------------------------------------
def query_chembl(compound, target):
    # Step 1: Search for target
    url = (f"https://www.ebi.ac.uk/chembl/api/data/target/search.json"
           f"?q={urllib.parse.quote(target)}&limit=5")
    resp = api_request(url)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "ChEMBL", error=resp[1])

    targets = resp.get("targets", []) if resp else []
    if not targets:
        return result("NO_DATA", "ChEMBL", data={
            "query_compound": compound, "query_target": target,
            "note": "Target not found in ChEMBL"})

    target_chembl_id = targets[0].get("target_chembl_id", "")
    target_name = targets[0].get("pref_name", target)

    # Step 2: Search for compound
    url2 = (f"https://www.ebi.ac.uk/chembl/api/data/molecule/search.json"
            f"?q={urllib.parse.quote(compound)}&limit=5")
    resp2 = api_request(url2)
    if isinstance(resp2, tuple):
        return result("API_UNAVAILABLE", "ChEMBL", error=resp2[1])

    molecules = resp2.get("molecules", []) if resp2 else []
    molecule_chembl_id = ""
    molecule_name = compound
    if molecules:
        molecule_chembl_id = molecules[0].get("molecule_chembl_id", "")
        molecule_name = molecules[0].get("pref_name", compound) or compound

    # Step 3: Search for activity between compound and target
    if target_chembl_id and molecule_chembl_id:
        activity_url = (f"https://www.ebi.ac.uk/chembl/api/data/activity.json"
                        f"?target_chembl_id={target_chembl_id}"
                        f"&molecule_chembl_id={molecule_chembl_id}&limit=10")
    elif target_chembl_id and not molecule_chembl_id:
        return result("NO_DATA", "ChEMBL", data={
            "compound": compound, "target": target_name,
            "target_chembl_id": target_chembl_id,
            "note": f"Compound '{compound}' not found in ChEMBL; cannot search activities"
        })
    if target_chembl_id and molecule_chembl_id:

        resp3 = api_request(activity_url, timeout=15)
        if isinstance(resp3, tuple):
            return result("API_UNAVAILABLE", "ChEMBL", error=resp3[1])

        activities = resp3.get("activities", []) if resp3 else []
        if activities:
            parsed = []
            for act in activities[:10]:
                parsed.append({
                    "molecule": act.get("molecule_pref_name", ""),
                    "type": act.get("standard_type", ""),
                    "value": act.get("standard_value", ""),
                    "units": act.get("standard_units", ""),
                    "relation": act.get("standard_relation", ""),
                })
            return result("DATA_FOUND", "ChEMBL", data={
                "compound": molecule_name,
                "compound_chembl_id": molecule_chembl_id,
                "target": target_name,
                "target_chembl_id": target_chembl_id,
                "activities": parsed,
                "total_activities": len(activities)
            })

    return result("NO_DATA", "ChEMBL", data={
        "compound": molecule_name, "target": target_name,
        "target_chembl_id": target_chembl_id,
        "note": "No activity data found between compound and target"
    })


# ---------------------------------------------------------------------------
# 6. UniProt — Protein function and annotations
# ---------------------------------------------------------------------------
def query_uniprot(protein):
    url = (f"https://rest.uniprot.org/uniprotkb/search"
           f"?query=gene_exact:{urllib.parse.quote(protein)}"
           f"+AND+organism_id:9606+AND+reviewed:true"
           f"&fields=accession,gene_names,protein_name,cc_function,"
           f"cc_subcellular_location,ft_domain"
           f"&size=3&format=json")
    headers = {"Accept": "application/json"}
    resp = api_request(url, headers)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "UniProt", error=resp[1])
    if not resp:
        return result("NO_DATA", "UniProt", data={"query": protein})

    results_list = resp.get("results", [])
    if not results_list:
        return result("NO_DATA", "UniProt", data={"query": protein,
                                                   "note": "Protein not found"})

    entry = results_list[0]
    accession = entry.get("primaryAccession", "")
    protein_desc = entry.get("proteinDescription", {})
    rec_name = protein_desc.get("recommendedName", {})
    full_name = rec_name.get("fullName", {}).get("value", "") if rec_name else ""

    # Extract function
    comments = entry.get("comments", [])
    function_text = ""
    subcellular = []
    disease = []
    tissue_spec = ""

    for comment in comments:
        ctype = comment.get("commentType", "")
        if ctype == "FUNCTION":
            texts = comment.get("texts", [])
            if texts:
                function_text = texts[0].get("value", "")
        elif ctype == "SUBCELLULAR LOCATION":
            locs = comment.get("subcellularLocations", [])
            for loc in locs:
                location = loc.get("location", {})
                subcellular.append(location.get("value", ""))
        elif ctype == "INVOLVEMENT IN DISEASE":
            disease_info = comment.get("disease", {})
            if disease_info:
                disease.append(disease_info.get("diseaseId", ""))
        elif ctype == "TISSUE SPECIFICITY":
            texts = comment.get("texts", [])
            if texts:
                tissue_spec = texts[0].get("value", "")

    # Extract domains
    features = entry.get("features", [])
    domains = []
    for feat in features:
        if feat.get("type") == "Domain":
            desc = feat.get("description", "")
            if desc:
                domains.append(desc)

    return result("DATA_FOUND", "UniProt", data={
        "protein": protein,
        "accession": accession,
        "full_name": full_name,
        "function": function_text[:500] if function_text else "",
        "subcellular_location": subcellular[:5],
        "domains": domains[:10],
        "tissue_specificity": tissue_spec[:300] if tissue_spec else "",
        "disease_involvement": disease[:5],
    })


# ---------------------------------------------------------------------------
# 7. PDB / AlphaFold — Protein structure
# ---------------------------------------------------------------------------
def query_structure(protein):
    # First get UniProt accession
    url = (f"https://rest.uniprot.org/uniprotkb/search"
           f"?query=gene_exact:{urllib.parse.quote(protein)}"
           f"+AND+organism_id:9606+AND+reviewed:true"
           f"&fields=accession,xref_pdb&size=1&format=json")
    headers = {"Accept": "application/json"}
    resp = api_request(url, headers)
    if isinstance(resp, tuple):
        return result("API_UNAVAILABLE", "PDB", error=resp[1])

    results_list = resp.get("results", []) if resp else []
    if not results_list:
        return result("NO_DATA", "PDB", data={"query": protein,
                                               "note": "Protein not found"})

    accession = results_list[0].get("primaryAccession", "")

    # Get PDB cross-references
    pdb_refs = []
    for xref in results_list[0].get("uniProtKBCrossReferences", []):
        if xref.get("database") == "PDB":
            pdb_id = xref.get("id", "")
            props = {p.get("key", ""): p.get("value", "")
                     for p in xref.get("properties", [])}
            pdb_refs.append({
                "pdb_id": pdb_id,
                "method": props.get("Method", ""),
                "resolution": props.get("Resolution", ""),
                "chains": props.get("Chains", ""),
            })

    # Check AlphaFold
    alphafold_url = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"
    af_resp = api_request(alphafold_url)
    af_data = None
    if not isinstance(af_resp, tuple) and af_resp:
        af_entries = af_resp if isinstance(af_resp, list) else [af_resp]
        if af_entries:
            af_data = {
                "model_url": af_entries[0].get("pdbUrl", ""),
                "mean_plddt": af_entries[0].get("globalMetricValue", ""),
                "created_date": af_entries[0].get("modelCreatedDate", ""),
            }

    if pdb_refs or af_data:
        return result("DATA_FOUND", "PDB", data={
            "protein": protein,
            "uniprot_accession": accession,
            "pdb_structures": pdb_refs[:10],
            "total_pdb_structures": len(pdb_refs),
            "alphafold_available": af_data is not None,
            "alphafold": af_data,
        })

    return result("NO_DATA", "PDB", data={
        "protein": protein,
        "uniprot_accession": accession,
        "note": "No experimental structures or AlphaFold predictions found"
    })


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Query bioinformatics databases for MAGELLAN validation")
    parser.add_argument("--type", required=True,
                        choices=["gene_expression", "protein_interaction",
                                 "pathway_check", "gwas_association",
                                 "compound_target", "protein_function",
                                 "protein_structure"],
                        help="Type of query to run")
    parser.add_argument("--gene", help="Gene symbol (e.g., TP53, BRCA1)")
    parser.add_argument("--tissue", help="Tissue name for GTEx (e.g., Brain, Breast)")
    parser.add_argument("--protein", help="Protein/gene name for UniProt/PDB")
    parser.add_argument("--protein1", help="First protein for interaction query")
    parser.add_argument("--protein2", help="Second protein for interaction query")
    parser.add_argument("--pathway", help="KEGG pathway ID (e.g., hsa04110)")
    parser.add_argument("--trait", help="Trait/phenotype for GWAS query")
    parser.add_argument("--compound", help="Compound name for ChEMBL")
    parser.add_argument("--target", help="Target name for ChEMBL")

    args = parser.parse_args()

    try:
        if args.type == "gene_expression":
            if not args.gene or not args.tissue:
                print(json.dumps(result("ERROR", "GTEx",
                                        error="--gene and --tissue required")))
                sys.exit(1)
            out = query_gene_expression(args.gene, args.tissue)

        elif args.type == "protein_interaction":
            if not args.protein1 or not args.protein2:
                print(json.dumps(result("ERROR", "STRING",
                                        error="--protein1 and --protein2 required")))
                sys.exit(1)
            out = query_string(args.protein1, args.protein2)

        elif args.type == "pathway_check":
            if not args.gene:
                print(json.dumps(result("ERROR", "KEGG",
                                        error="--gene required")))
                sys.exit(1)
            out = query_kegg(args.gene, args.pathway)

        elif args.type == "gwas_association":
            if not args.gene:
                print(json.dumps(result("ERROR", "GWAS_Catalog",
                                        error="--gene required")))
                sys.exit(1)
            out = query_gwas(args.gene, args.trait)

        elif args.type == "compound_target":
            if not args.compound or not args.target:
                print(json.dumps(result("ERROR", "ChEMBL",
                                        error="--compound and --target required")))
                sys.exit(1)
            out = query_chembl(args.compound, args.target)

        elif args.type == "protein_function":
            if not args.protein:
                print(json.dumps(result("ERROR", "UniProt",
                                        error="--protein required")))
                sys.exit(1)
            out = query_uniprot(args.protein)

        elif args.type == "protein_structure":
            if not args.protein:
                print(json.dumps(result("ERROR", "PDB",
                                        error="--protein required")))
                sys.exit(1)
            out = query_structure(args.protein)

        print(json.dumps(out, indent=2))

    except Exception as e:
        print(json.dumps(result("ERROR", args.type, error=str(e))))
        sys.exit(1)


if __name__ == "__main__":
    main()
