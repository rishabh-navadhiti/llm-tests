import os
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kstest, anderson

# Paths
eval_dir = "/Users/rish/Development/runpod dev/llm-tests/newTest/Qwen3-30B-A3B/Framework-eval"
results_dir = "/Users/rish/Development/runpod dev/llm-tests/newTest/Qwen3-30B-A3B/Results"
os.makedirs(results_dir, exist_ok=True)

output_md = os.path.join(results_dir, "eval_stats.md")

# Fields to track
FIELDS = [
    "PATIENT_NAME",
    "CHIEF_COMPLAINT",
    "HPI_SPENCER",
    "MUSCULOSKELETAL_VERBATIM",
    "IMAGING_RESULTS",
    "ASSESSMENT_SPENCER",
    "PLAN_SPENCER_"
]

# Metrics inside each field
METRICS = ["bleu_score", "content_analysis", "content_similarity", "rhetorical_similarity", "topic_similarity"]

# Collect data
data = {field: {metric: {} for metric in METRICS} for field in FIELDS}

for fname in os.listdir(eval_dir):
    if not fname.startswith("REC-") or not fname.endswith(".json"):
        continue

    record_id = int(fname.split("-")[1].replace(".json", ""))  # Extract 6602 from REC-6602.json
    with open(os.path.join(eval_dir, fname), "r") as f:
        results = json.load(f)

    for entry in results:
        key = entry.get("key")
        if key in FIELDS:
            for metric in METRICS:
                val = entry.get(metric, None)
                if val is not None:
                    data[key][metric][record_id] = val

# Save markdown
with open(output_md, "w") as md:
    md.write("# Evaluation Statistics\n\n")

    for field in FIELDS:
        md.write(f"## Field: {field}\n\n")

        for metric in METRICS:
            values = list(data[field][metric].values())
            if not values:
                continue

            arr = np.array(values)

            mean = np.mean(arr)
            std = np.std(arr, ddof=1) if len(arr) > 1 else 0
            var = np.var(arr, ddof=1) if len(arr) > 1 else 0

            md.write(f"### Metric: {metric}\n")
            md.write(f"- Mean: {mean:.4f}\n")
            md.write(f"- Std Dev: {std:.4f}\n")
            md.write(f"- Variance: {var:.4f}\n")

            # Statistical tests
            try:
                shapiro_stat, shapiro_p = shapiro(arr)
                md.write(f"- Shapiro-Wilk: statistic={shapiro_stat:.4f}, p={shapiro_p:.4f}\n")
            except Exception as e:
                md.write(f"- Shapiro-Wilk: Error ({e})\n")

            try:
                ks_stat, ks_p = kstest(arr, "norm", args=(mean, std if std > 0 else 1e-6))
                md.write(f"- Kolmogorov-Smirnov: statistic={ks_stat:.4f}, p={ks_p:.4f}\n")
            except Exception as e:
                md.write(f"- Kolmogorov-Smirnov: Error ({e})\n")

            try:
                ad_result = anderson(arr)
                md.write(f"- Anderson-Darling: statistic={ad_result.statistic:.4f}\n")
                crit_vals = ", ".join(f"{cv:.4f}" for cv in ad_result.critical_values)
                sig_levels = ", ".join(str(sl) for sl in ad_result.significance_level)
                md.write(f"  - Critical Values: {crit_vals}\n")
                md.write(f"  - Significance Levels: {sig_levels}\n")
            except Exception as e:
                md.write(f"- Anderson-Darling: Error ({e})\n")

            md.write("\n")

        # Compute covariance across metrics
        md.write("### Covariance Matrix (across metrics)\n\n")
        all_metric_data = []
        labels = []
        for metric in METRICS:
            vals = list(data[field][metric].values())
            if len(vals) == len(list(data[field][METRICS[0]].values())):
                all_metric_data.append(vals)
                labels.append(metric)

        if len(all_metric_data) > 1:
            cov_matrix = np.cov(all_metric_data)
            md.write("| Metric | " + " | ".join(labels) + " |\n")
            md.write("|" + " --- |" * (len(labels) + 1) + "\n")
            for i, row in enumerate(cov_matrix):
                row_str = " | ".join(f"{x:.4f}" for x in row)
                md.write(f"| {labels[i]} | {row_str} |\n")
        md.write("\n")

                # ---- Scatter subplot chart (4 metrics only, skip BLEU) ----
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle(f"Scatter Plots for {field}", fontsize=14)

        score_types = [
            ("content_similarity", "Content Similarity", "blue"),
            ("rhetorical_similarity", "Rhetorical Similarity", "green"),
            ("topic_similarity", "Topic Similarity", "red"),
            ("content_analysis", "Content Analysis", "purple"),
        ]

        for ax, (metric, title, color) in zip(axes.flat, score_types):
            rec_ids = list(data[field][metric].keys())
            values = list(data[field][metric].values())
            if not values:
                continue

            # Scatter points only
            ax.scatter(rec_ids, values, color=color, alpha=0.7)

            ax.set_title(title)
            ax.set_xlabel("Record ID")
            ax.set_ylabel("Score")
            ax.set_ylim(0, 1.05)

            mean_val = np.mean(values)
            std_val = np.std(values, ddof=1) if len(values) > 1 else 0
            ax.text(0.5, -0.25,
                    f"Mean={mean_val:.3f}, Std={std_val:.3f}",
                    transform=ax.transAxes,
                    ha="center", fontsize=8, color="black")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(os.path.join(results_dir, f"{field}_subplots.png"), dpi=300)
        plt.close()


    md.write("\n---\n")
