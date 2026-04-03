#!/usr/bin/env python3
"""
GEV Tail Index Analysis of the Meltome Atlas
=============================================

MAGELLAN Hypothesis Verification (Session 2026-03-27-scout-013, C1-H1):
  "GEV Tail Index (ξ) as Phylogenomic Signature of Thermal Adaptation Strategy"

Prediction: The shape parameter ξ of the GEV distribution fitted to proteome-wide
melting temperature (Tm) distributions should correlate negatively with optimal
growth temperature (OGT) — thermophiles compress their lower Tm tail (more negative ξ),
while psychrophiles maintain broader tails (ξ closer to 0).

Data: Jarzab et al. 2020, Nature Methods 17:495-503
  - Meltome Atlas: 48,000 proteins across 13 species
  - PRIDE accession: PXD011929
  - Supplementary Table S2 (MOESM4): pre-computed Tm per protein per dataset

Usage:
  python analyze_gev_meltome.py            # Full analysis
  python analyze_gev_meltome.py --download  # Download data first, then analyze

Dependencies:
  pip install pandas openpyxl scipy matplotlib numpy

Author: MAGELLAN computational verification pipeline
License: Apache 2.0
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import genextreme, spearmanr, pearsonr, anderson, kstest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

warnings.filterwarnings('ignore', category=FutureWarning)

# ─── Configuration ───────────────────────────────────────────────────

DATA_DIR = Path(__file__).parent
MOESM3 = DATA_DIR / "MOESM3.xlsx"  # Dataset metadata
MOESM4 = DATA_DIR / "MOESM4.xlsx"  # Protein Tm values per dataset
OUTPUT_DIR = DATA_DIR / "results"

BASE_URL = "https://static-content.springer.com/esm/art%3A10.1038%2Fs41592-020-0801-4/MediaObjects"
MOESM3_URL = f"{BASE_URL}/41592_2020_801_MOESM3_ESM.xlsx"
MOESM4_URL = f"{BASE_URL}/41592_2020_801_MOESM4_ESM.xlsx"

# One representative lysate dataset per species (avoids cell-vs-lysate confound)
# Selected: first lysate experiment per species from MOESM3 metadata
SPECIES_DATASETS = {
    "Oleispira antarctica":          {"dataset": "ma_0001", "ogt": 15, "domain": "Bacteria"},
    "Caenorhabditis elegans":        {"dataset": "ma_0012", "ogt": 20, "domain": "Eukaryota"},
    "Arabidopsis thaliana":          {"dataset": "ma_0011", "ogt": 25, "domain": "Eukaryota"},
    "Drosophila melanogaster":       {"dataset": "ma_0013", "ogt": 28, "domain": "Eukaryota"},
    "Danio rerio":                   {"dataset": "ma_0014", "ogt": 28, "domain": "Eukaryota"},
    "Bacillus subtilis":             {"dataset": "ma_0002", "ogt": 30, "domain": "Bacteria"},
    "Saccharomyces cerevisiae":      {"dataset": "ma_0010", "ogt": 30, "domain": "Eukaryota"},
    "Escherichia coli":              {"dataset": "ma_0003", "ogt": 37, "domain": "Bacteria"},
    "Mus musculus":                  {"dataset": "ma_0015", "ogt": 37, "domain": "Eukaryota"},
    "Homo sapiens":                  {"dataset": "ma_0018", "ogt": 37, "domain": "Eukaryota"},
    "Geobacillus stearothermophilus": {"dataset": "ma_0006", "ogt": 55, "domain": "Bacteria"},
    "Picrophilus torridus":          {"dataset": "ma_0007", "ogt": 60, "domain": "Archaea"},
    "Thermus thermophilus":          {"dataset": "ma_0008", "ogt": 70, "domain": "Bacteria"},
}

# Quality thresholds for including proteins
MIN_R2 = 0.8       # Minimum R² of sigmoidal curve fit
REQUIRE_CONVERGED = True  # Only proteins where curve fit converged

# GEV fit parameters
MIN_PROTEINS_FOR_GEV = 100  # Minimum number of valid Tm values to attempt GEV fit


# ─── Data Loading ────────────────────────────────────────────────────

def download_data():
    """Download supplementary data files from Nature Methods."""
    import urllib.request
    for url, path in [(MOESM3_URL, MOESM3), (MOESM4_URL, MOESM4)]:
        if path.exists():
            print(f"  {path.name} already exists, skipping")
            continue
        print(f"  Downloading {path.name} ({url})...")
        urllib.request.urlretrieve(url, path)
        print(f"  Saved: {path} ({path.stat().st_size / 1024:.0f} KB)")


def load_tm_data():
    """Load Tm values from MOESM4 for each species."""
    print("\nLoading Tm data from MOESM4.xlsx...")
    results = {}

    for species, info in SPECIES_DATASETS.items():
        sheet = info["dataset"]
        try:
            df = pd.read_excel(MOESM4, sheet_name=sheet)
        except Exception as e:
            print(f"  WARNING: Could not read sheet {sheet} for {species}: {e}")
            continue

        # Filter for quality
        mask = pd.Series([True] * len(df))
        if "R2 of curve fit" in df.columns:
            mask &= df["R2 of curve fit"] >= MIN_R2
        if "Curve fit converged" in df.columns and REQUIRE_CONVERGED:
            mask &= df["Curve fit converged"] == True

        tm_col = "Melting point [°C]"
        if tm_col not in df.columns:
            # Try alternative column names
            tm_candidates = [c for c in df.columns if "melt" in c.lower() and "°" in c]
            if tm_candidates:
                tm_col = tm_candidates[0]
            else:
                print(f"  WARNING: No Tm column found for {species}")
                continue

        tm_values = df.loc[mask, tm_col].dropna().values.astype(float)

        # Remove obvious outliers (Tm outside physical range)
        tm_values = tm_values[(tm_values >= 20) & (tm_values <= 100)]

        results[species] = {
            "tm": tm_values,
            "n_total": len(df),
            "n_filtered": len(tm_values),
            "ogt": info["ogt"],
            "domain": info["domain"],
            "dataset": sheet,
        }
        print(f"  {species} (OGT={info['ogt']}°C): "
              f"{len(tm_values)}/{len(df)} proteins passed QC "
              f"(median Tm={np.median(tm_values):.1f}°C)")

    return results


# ─── GEV Analysis ────────────────────────────────────────────────────

def fit_gev(tm_values, species_name=""):
    """Fit GEV distribution to Tm values using MLE."""
    if len(tm_values) < MIN_PROTEINS_FOR_GEV:
        return None

    try:
        # scipy genextreme uses c = -ξ convention
        # genextreme.fit returns (c, loc, scale) where c = -ξ
        c, loc, scale = genextreme.fit(tm_values)
        xi = -c  # Convert to standard EVT convention (ξ)

        # Compute standard errors via bootstrap
        n_boot = 1000
        xi_boot = np.zeros(n_boot)
        rng = np.random.default_rng(42)
        for i in range(n_boot):
            sample = rng.choice(tm_values, size=len(tm_values), replace=True)
            try:
                c_b, _, _ = genextreme.fit(sample)
                xi_boot[i] = -c_b
            except Exception:
                xi_boot[i] = np.nan

        xi_boot = xi_boot[~np.isnan(xi_boot)]
        xi_se = np.std(xi_boot)
        xi_ci_lo = np.percentile(xi_boot, 2.5)
        xi_ci_hi = np.percentile(xi_boot, 97.5)

        # Goodness of fit: KS test
        ks_stat, ks_pval = kstest(tm_values, 'genextreme', args=(c, loc, scale))

        # Anderson-Darling (for supplementary info)
        # Not directly available for GEV, use KS

        return {
            "xi": xi,
            "xi_se": xi_se,
            "xi_ci": (xi_ci_lo, xi_ci_hi),
            "mu": loc,
            "sigma": scale,
            "c_scipy": c,
            "ks_stat": ks_stat,
            "ks_pval": ks_pval,
            "n": len(tm_values),
        }
    except Exception as e:
        print(f"  WARNING: GEV fit failed for {species_name}: {e}")
        return None


def run_gev_analysis(data):
    """Run GEV analysis on all species."""
    print("\n" + "="*70)
    print("GEV DISTRIBUTION FITTING")
    print("="*70)

    results = {}
    for species, info in sorted(data.items(), key=lambda x: x[1]["ogt"]):
        tm = info["tm"]
        fit = fit_gev(tm, species)
        if fit is None:
            print(f"\n  {species}: SKIPPED (insufficient data)")
            continue

        results[species] = {**info, **fit}
        domain_tag = f"[{info['domain'][:1]}]"
        print(f"\n  {species} {domain_tag} (OGT={info['ogt']}°C, n={fit['n']})")
        print(f"    ξ = {fit['xi']:.4f} ± {fit['xi_se']:.4f}  "
              f"(95% CI: [{fit['xi_ci'][0]:.4f}, {fit['xi_ci'][1]:.4f}])")
        print(f"    μ = {fit['mu']:.2f}°C, σ = {fit['sigma']:.2f}°C")
        print(f"    KS test: D={fit['ks_stat']:.4f}, p={fit['ks_pval']:.4f}")

        if fit['xi'] < 0:
            print(f"    → Weibull domain (bounded upper tail)")
        elif abs(fit['xi']) < 0.05:
            print(f"    → Near Gumbel domain (exponential tail)")
        else:
            print(f"    → Fréchet domain (heavy tail)")

    return results


def compute_correlations(results):
    """Compute correlation between ξ and OGT."""
    print("\n" + "="*70)
    print("CORRELATION ANALYSIS: ξ vs OGT")
    print("="*70)

    species_list = sorted(results.keys(), key=lambda s: results[s]["ogt"])
    xi_vals = np.array([results[s]["xi"] for s in species_list])
    ogt_vals = np.array([results[s]["ogt"] for s in species_list])

    # Spearman rank correlation (robust to outliers)
    rho_s, p_s = spearmanr(ogt_vals, xi_vals)
    # Pearson correlation
    rho_p, p_p = pearsonr(ogt_vals, xi_vals)

    print(f"\n  n = {len(species_list)} species")
    print(f"\n  Spearman:  ρ = {rho_s:.4f}, p = {p_s:.6f}")
    print(f"  Pearson:   r = {rho_p:.4f}, p = {p_p:.6f}")

    # MAGELLAN prediction: ξ should become MORE NEGATIVE as OGT increases
    # i.e., negative correlation expected
    if rho_s < 0 and p_s < 0.05:
        verdict = "CONFIRMED"
        detail = (f"ξ correlates negatively with OGT (ρ={rho_s:.3f}, p={p_s:.4f}). "
                  "Thermophiles show more negative ξ (Weibull domain), "
                  "consistent with tail truncation strategy.")
    elif rho_s < 0 and p_s < 0.1:
        verdict = "WEAKLY SUPPORTED"
        detail = (f"Negative trend observed (ρ={rho_s:.3f}) but not statistically "
                  f"significant at α=0.05 (p={p_s:.4f}).")
    elif rho_s > 0:
        verdict = "FALSIFIED"
        detail = (f"ξ correlates POSITIVELY with OGT (ρ={rho_s:.3f}), "
                  "opposite to prediction.")
    else:
        verdict = "INCONCLUSIVE"
        detail = f"No significant correlation detected (ρ={rho_s:.3f}, p={p_s:.4f})."

    print(f"\n  MAGELLAN PREDICTION VERDICT: {verdict}")
    print(f"  {detail}")

    return {
        "spearman_rho": rho_s, "spearman_p": p_s,
        "pearson_r": rho_p, "pearson_p": p_p,
        "verdict": verdict, "detail": detail,
        "species": species_list, "xi": xi_vals, "ogt": ogt_vals,
    }


# ─── Visualization ───────────────────────────────────────────────────

def plot_results(results, correlations, output_dir):
    """Generate publication-quality figures."""
    output_dir.mkdir(exist_ok=True)

    species_list = correlations["species"]
    xi_vals = correlations["xi"]
    ogt_vals = correlations["ogt"]
    xi_ses = np.array([results[s]["xi_se"] for s in species_list])
    domains = [results[s]["domain"] for s in species_list]

    # Color by domain
    domain_colors = {"Bacteria": "#2196F3", "Eukaryota": "#4CAF50", "Archaea": "#FF9800"}
    colors = [domain_colors.get(d, "#999") for d in domains]

    # ─── Figure 1: ξ vs OGT scatter ─────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 7))

    for i, sp in enumerate(species_list):
        short = sp.split()[0][0] + ". " + sp.split()[1] if len(sp.split()) > 1 else sp
        ax.errorbar(ogt_vals[i], xi_vals[i], yerr=xi_ses[i],
                    fmt='o', color=colors[i], markersize=10, capsize=5,
                    linewidth=1.5, markeredgecolor='white', markeredgewidth=1)
        offset_x = 1.5 if ogt_vals[i] < 60 else -1.5
        ha = 'left' if ogt_vals[i] < 60 else 'right'
        ax.annotate(short, (ogt_vals[i], xi_vals[i]),
                    xytext=(offset_x, 8), textcoords='offset points',
                    fontsize=8, ha=ha, style='italic')

    # Linear fit line
    slope, intercept = np.polyfit(ogt_vals, xi_vals, 1)
    x_fit = np.linspace(ogt_vals.min() - 5, ogt_vals.max() + 5, 100)
    ax.plot(x_fit, slope * x_fit + intercept, '--', color='#666',
            alpha=0.7, linewidth=1.5)

    ax.axhline(y=0, color='black', linewidth=0.5, alpha=0.3)
    ax.set_xlabel("Optimal Growth Temperature (°C)", fontsize=13)
    ax.set_ylabel("GEV Shape Parameter ξ", fontsize=13)
    ax.set_title("GEV Tail Index vs Optimal Growth Temperature\n"
                 "Meltome Atlas (Jarzab et al. 2020, 13 species)",
                 fontsize=14)

    rho = correlations["spearman_rho"]
    pval = correlations["spearman_p"]
    verdict = correlations["verdict"]
    ax.text(0.02, 0.02,
            f"Spearman ρ = {rho:.3f}, p = {pval:.4f}\n"
            f"Pearson r = {correlations['pearson_r']:.3f}\n"
            f"MAGELLAN prediction: {verdict}",
            transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Domain legend
    for domain, color in domain_colors.items():
        ax.scatter([], [], c=color, s=80, label=domain)
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    fig.savefig(output_dir / "fig1_xi_vs_ogt.png", dpi=300, bbox_inches='tight')
    fig.savefig(output_dir / "fig1_xi_vs_ogt.pdf", bbox_inches='tight')
    plt.close()
    print(f"\n  Saved: fig1_xi_vs_ogt.png/pdf")

    # ─── Figure 2: Tm distributions per species ─────────────────────
    fig, axes = plt.subplots(4, 4, figsize=(16, 14))
    axes = axes.flatten()

    for i, sp in enumerate(species_list):
        if i >= 16:
            break
        ax = axes[i]
        tm = results[sp]["tm"]
        fit = results[sp]

        # Histogram
        ax.hist(tm, bins=50, density=True, alpha=0.6,
                color=domain_colors.get(results[sp]["domain"], "#999"),
                edgecolor='white', linewidth=0.3)

        # GEV fit overlay
        x = np.linspace(tm.min() - 5, tm.max() + 5, 200)
        pdf = genextreme.pdf(x, fit["c_scipy"], loc=fit["mu"], scale=fit["sigma"])
        ax.plot(x, pdf, 'r-', linewidth=2, alpha=0.8)

        short = sp.split()[0][0] + ". " + sp.split()[-1]
        ax.set_title(f"{short}\nOGT={fit['ogt']}°C, ξ={fit['xi']:.3f}",
                     fontsize=9, style='italic')
        ax.set_xlabel("Tm (°C)", fontsize=8)
        ax.set_ylabel("Density", fontsize=8)
        ax.tick_params(labelsize=7)

    # Remove unused subplots
    for j in range(len(species_list), 16):
        axes[j].set_visible(False)

    fig.suptitle("Proteome Melting Temperature Distributions with GEV Fits\n"
                 "Meltome Atlas — 13 species across the tree of life",
                 fontsize=14, y=1.02)
    plt.tight_layout()
    fig.savefig(output_dir / "fig2_tm_distributions.png", dpi=300, bbox_inches='tight')
    fig.savefig(output_dir / "fig2_tm_distributions.pdf", bbox_inches='tight')
    plt.close()
    print(f"  Saved: fig2_tm_distributions.png/pdf")

    # ─── Figure 3: ξ by domain ──────────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 5))

    for domain in ["Bacteria", "Archaea", "Eukaryota"]:
        idx = [i for i, d in enumerate(domains) if d == domain]
        if idx:
            ax.scatter(ogt_vals[idx], xi_vals[idx],
                       c=domain_colors[domain], s=120, label=domain,
                       edgecolors='white', linewidths=1, zorder=3)
            # Connect within domain
            sorted_idx = sorted(idx, key=lambda i: ogt_vals[i])
            ax.plot(ogt_vals[sorted_idx], xi_vals[sorted_idx],
                    '--', color=domain_colors[domain], alpha=0.4, linewidth=1)

    ax.axhline(y=0, color='black', linewidth=0.5, alpha=0.3)
    ax.set_xlabel("Optimal Growth Temperature (°C)", fontsize=12)
    ax.set_ylabel("GEV Shape Parameter ξ", fontsize=12)
    ax.set_title("ξ vs OGT by Phylogenetic Domain", fontsize=13)
    ax.legend(fontsize=11)
    plt.tight_layout()
    fig.savefig(output_dir / "fig3_xi_by_domain.png", dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: fig3_xi_by_domain.png")


# ─── Report Generation ───────────────────────────────────────────────

def generate_report(results, correlations, output_dir):
    """Generate a markdown report of the analysis."""
    output_dir.mkdir(exist_ok=True)

    species_list = correlations["species"]
    lines = []
    lines.append("# GEV Tail Index Analysis of the Meltome Atlas")
    lines.append("")
    lines.append("## MAGELLAN Hypothesis Verification")
    lines.append("")
    lines.append("**Hypothesis**: GEV Tail Index (ξ) as Phylogenomic Signature of Thermal Adaptation Strategy")
    lines.append("**Session**: 2026-03-27-scout-013, C1-H1 (PASS, composite score 7.85)")
    lines.append("")
    lines.append("**Prediction**: The shape parameter ξ of the GEV distribution fitted to proteome-wide Tm distributions")
    lines.append("should correlate negatively with OGT — thermophiles compress their lower Tm tail (more negative ξ).")
    lines.append("")
    lines.append(f"**Data**: Jarzab et al. 2020, Nature Methods 17:495-503 (PRIDE: PXD011929)")
    lines.append(f"**Species analyzed**: {len(species_list)}")
    lines.append(f"**OGT range**: {min(correlations['ogt']):.0f}°C – {max(correlations['ogt']):.0f}°C")
    lines.append("")

    lines.append("## Results Summary")
    lines.append("")
    lines.append(f"| Species | Domain | OGT (°C) | n proteins | ξ | 95% CI | μ (°C) | σ (°C) | KS p-value |")
    lines.append(f"|---------|--------|----------|------------|---|--------|--------|--------|------------|")

    for sp in species_list:
        r = results[sp]
        short = sp.split()[0][0] + ". " + sp.split()[-1]
        lines.append(
            f"| *{short}* | {r['domain']} | {r['ogt']} | {r['n']} | "
            f"{r['xi']:.4f} | [{r['xi_ci'][0]:.3f}, {r['xi_ci'][1]:.3f}] | "
            f"{r['mu']:.1f} | {r['sigma']:.1f} | {r['ks_pval']:.3f} |"
        )

    lines.append("")
    lines.append("## Correlation Analysis")
    lines.append("")
    lines.append(f"- **Spearman rank correlation**: ρ = {correlations['spearman_rho']:.4f}, p = {correlations['spearman_p']:.6f}")
    lines.append(f"- **Pearson correlation**: r = {correlations['pearson_r']:.4f}, p = {correlations['pearson_p']:.6f}")
    lines.append("")
    lines.append(f"## Verdict: **{correlations['verdict']}**")
    lines.append("")
    lines.append(correlations["detail"])
    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    if correlations["verdict"] == "CONFIRMED":
        lines.append("The MAGELLAN-generated hypothesis is computationally supported by the data.")
        lines.append("Thermophilic organisms show more negative ξ values, indicating their proteome Tm")
        lines.append("distributions have truncated lower tails (Weibull domain). This is consistent with")
        lines.append("evolutionary selection against thermolabile proteins at high growth temperatures.")
        lines.append("")
        lines.append("Psychrophilic and mesophilic organisms show ξ values closer to zero (Gumbel domain),")
        lines.append("indicating their Tm distributions maintain broader tails — consistent with a")
        lines.append("distribution-shift strategy rather than tail-truncation.")
    elif correlations["verdict"] == "FALSIFIED":
        lines.append("The MAGELLAN prediction is not supported. The observed correlation is opposite")
        lines.append("to the predicted direction. This falsifies the specific hypothesis that thermophiles")
        lines.append("truncate their Tm lower tail relative to psychrophiles.")
    else:
        lines.append("The data does not provide strong evidence for or against the hypothesis.")
        lines.append("Possible explanations: measurement censoring (Tm range 30-90°C), phylogenetic")
        lines.append("confounds, or the effect may be present but too weak to detect with 13 species.")

    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append("1. Loaded pre-computed Tm values from Jarzab et al. 2020 Supplementary Table S2 (MOESM4)")
    lines.append(f"2. Quality filter: R² ≥ {MIN_R2}, converged curve fits only, Tm in [20°C, 100°C]")
    lines.append("3. Selected one lysate dataset per species (avoids cell-vs-lysate confound)")
    lines.append("4. Fitted GEV distribution via MLE (scipy.stats.genextreme)")
    lines.append("5. Bootstrap standard errors (n=1000)")
    lines.append("6. Spearman rank correlation of ξ vs OGT across 13 species")
    lines.append("")
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("```bash")
    lines.append("# 1. Download data")
    lines.append("python analyze_gev_meltome.py --download")
    lines.append("# 2. Run analysis")
    lines.append("python analyze_gev_meltome.py")
    lines.append("```")
    lines.append("")
    lines.append("All code and data sources are open. PRIDE PXD011929 is publicly accessible.")
    lines.append("")
    lines.append("## Citation")
    lines.append("")
    lines.append("Jarzab, A. et al. Meltome atlas — thermal proteome stability across the tree of life.")
    lines.append("Nature Methods 17, 495–503 (2020). https://doi.org/10.1038/s41592-020-0801-4")
    lines.append("")
    lines.append("---")
    lines.append("*Generated by MAGELLAN computational verification pipeline*")

    report_path = output_dir / "GEV_MELTOME_REPORT.md"
    report_path.write_text("\n".join(lines))
    print(f"\n  Saved report: {report_path}")

    return report_path


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    os.chdir(DATA_DIR)

    if "--download" in sys.argv:
        print("Downloading supplementary data...")
        download_data()

    if not MOESM4.exists():
        print(f"ERROR: {MOESM4} not found. Run with --download first.")
        sys.exit(1)

    # Load data
    data = load_tm_data()
    if len(data) < 5:
        print(f"ERROR: Only {len(data)} species loaded, need at least 5")
        sys.exit(1)

    # Fit GEV distributions
    gev_results = run_gev_analysis(data)
    if len(gev_results) < 5:
        print(f"ERROR: Only {len(gev_results)} species with successful GEV fits")
        sys.exit(1)

    # Correlation analysis
    corr = compute_correlations(gev_results)

    # Generate figures
    print("\nGenerating figures...")
    plot_results(gev_results, corr, OUTPUT_DIR)

    # Generate report
    report = generate_report(gev_results, corr, OUTPUT_DIR)

    # Summary
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print(f"\n  Species analyzed: {len(gev_results)}")
    print(f"  Spearman ρ(ξ, OGT) = {corr['spearman_rho']:.4f} (p = {corr['spearman_p']:.4f})")
    print(f"  VERDICT: {corr['verdict']}")
    print(f"\n  Report: {report}")
    print(f"  Figures: {OUTPUT_DIR}/fig1_xi_vs_ogt.png")
    print(f"           {OUTPUT_DIR}/fig2_tm_distributions.png")
    print(f"           {OUTPUT_DIR}/fig3_xi_by_domain.png")


if __name__ == "__main__":
    main()
