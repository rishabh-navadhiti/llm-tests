import os
import re
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kstest, anderson

# ------------------------------
# Helper function to load scores
# ------------------------------
def load_scores_from_jsons(folder_path):
    results = {
        "file_ids": [],
        "content_similarity": [],
        "rhetorical_similarity": [],
        "topic_similarity": [],
        "content_analysis": []
    }

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            
            # Extract ID (e.g. REC-6602 -> 6602)
            match = re.search(r"REC-(\d+)", filename)
            file_id = match.group(1) if match else filename.replace(".json", "")
            
            with open(filepath, "r") as f:
                data = json.load(f)

            scores_accum = {
                "content_similarity": [],
                "rhetorical_similarity": [],
                "topic_similarity": [],
                "content_analysis": []
            }
            
            for field in data:
                field_name, field_scores = list(field.items())[0]
                if field_name == "PATIENT_NAME":
                    continue
                scores_accum["content_similarity"].append(field_scores.get("content_similarity", 0.0))
                scores_accum["rhetorical_similarity"].append(field_scores.get("rhetorical_similarity", 0.0))
                scores_accum["topic_similarity"].append(field_scores.get("topic_similarity", 0.0))
                scores_accum["content_analysis"].append(field_scores.get("content_analysis", 0.0))
            
            results["file_ids"].append(file_id)
            for key in scores_accum:
                avg = sum(scores_accum[key]) / len(scores_accum[key]) if scores_accum[key] else 0.0
                results[key].append(avg)

    return results


# ------------------------------
# Stats function
# ------------------------------
def compute_stats(scores):
    arr = np.array(scores)
    return {
        "mean": np.mean(arr),
        "std": np.std(arr, ddof=1),  # sample std
        "var": np.var(arr, ddof=1),
    }


# ------------------------------
# Normality Tests
# ------------------------------
def run_normality_tests(values, label):
    arr = np.array(values)

    print(f"\n--- Normality Tests for {label} ---")

    # Shapiro-Wilk
    stat, p = shapiro(arr)
    print(f"Shapiro-Wilk: statistic={stat:.4f}, p-value={p:.4f}")

    # Kolmogorov-Smirnov (compare with Normal(μ, σ))
    mu, sigma = np.mean(arr), np.std(arr, ddof=1)
    ks_stat, ks_p = kstest(arr, 'norm', args=(mu, sigma))
    print(f"Kolmogorov-Smirnov: statistic={ks_stat:.4f}, p-value={ks_p:.4f}")

    # Anderson-Darling
    ad_result = anderson(arr, dist='norm')
    print(f"Anderson-Darling: statistic={ad_result.statistic:.4f}")
    for cv, sig in zip(ad_result.critical_values, ad_result.significance_level):
        print(f"  Critical Value at {sig}%: {cv:.4f}")


# ------------------------------
# Plotting function
# ------------------------------
def plot_scores(scores):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Evaluation Scores Across Files", fontsize=16)

    file_ids = scores["file_ids"]

    score_types = [
        ("content_similarity", "Content Similarity", "blue"),
        ("rhetorical_similarity", "Rhetorical Similarity", "green"),
        ("topic_similarity", "Topic Similarity", "red"),
        ("content_analysis", "Content Analysis", "purple"),
    ]

    # Collect scores for covariance
    all_scores = []

    for ax, (key, title, color) in zip(axes.flat, score_types):
        values = scores[key]
        all_scores.append(values)

        stats = compute_stats(values)

        # Scatter plot
        ax.scatter(file_ids, values, color=color)
        ax.set_title(title)
        ax.set_xlabel("File ID")
        ax.set_ylabel("Score")
        ax.set_ylim(0, 1.05)  # keep scale consistent

        # Annotate mean & std on plot
        ax.text(0.5, -0.25,
                f"Mean={stats['mean']:.3f}, Std={stats['std']:.3f}",
                transform=ax.transAxes,
                ha="center", fontsize=9, color="black")

        # Print full stats to terminal
        print(f"\n[{title}]")
        print(f"  Mean: {stats['mean']:.4f}")
        print(f"  Std:  {stats['std']:.4f}")
        print(f"  Var:  {stats['var']:.4f}")

        # Normality tests
        run_normality_tests(values, title)

    # Covariance matrix (between score types)
    all_scores = np.array(all_scores)
    cov_matrix = np.cov(all_scores)

    labels = [title for _, title, _ in score_types]

    print("\nCovariance matrix (between scores):")
    print("             " + "  ".join(f"{l[:12]:>12}" for l in labels))
    for i, row in enumerate(cov_matrix):
        print(f"{labels[i][:12]:>12} " + " ".join(f"{val:12.4f}" for val in row))

    plt.tight_layout()
    plt.show()


# ------------------------------
# Main execution
# ------------------------------
if __name__ == "__main__":
    folder_path = "/Users/rish/Development/runpod dev/llm-tests/evaluation/scatterplot/output_extracted_scores"
    scores = load_scores_from_jsons(folder_path)
    plot_scores(scores)
