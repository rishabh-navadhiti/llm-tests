import os
import json

# 📂 Directory containing evaluation JSON files
INPUT_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-DeepSeek-R1-32b-gpt"
OUTPUT_FILE = "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-DeepSeek-R1-32b-gpt/Deepseek-qwen32b-report.md"
MODEL_NAME = "Medgemma-27B"

def process_eval_files(input_dir, output_file):
    records_summary = []
    all_percentages = []

    with open(output_file, "w", encoding="utf-8") as md:
        for filename in sorted(os.listdir(input_dir)):
            if filename.endswith("-eval.json"):
                file_path = os.path.join(input_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Extract record id (strip "-eval.json")
                record_id = filename.replace("-eval.json", "")

                md.write(f"# {record_id}\n\n")

                # Table header
                md.write("| Title | Score | Justification |\n")
                md.write("|-------|-------|---------------|\n")

                # Field scores
                for field, details in data["field_scores"].items():
                    score = details.get("score", "")
                    justification = details.get("justification", "").replace("\n", " ")
                    md.write(f"| {field} | {score} | {justification} |\n")

                # Totals and summary
                total_score = data.get("total_score", 0)
                percentage = data.get("percentage", 0)
                overall_summary = data.get("overall_summary", "")

                md.write(f"\n**Total Score:** {total_score}\n\n")
                md.write(f"**Percentage:** {percentage}\n\n")
                md.write(f"**Overall Summary:** {overall_summary}\n\n")
                md.write("---\n\n")

                # Keep track for final summary
                records_summary.append((record_id, total_score, percentage))

                # Collect numeric percentage (strip % if present)
                if isinstance(percentage, str) and percentage.endswith("%"):
                    try:
                        percentage_value = float(percentage.strip("%"))
                        all_percentages.append(percentage_value)
                    except ValueError:
                        pass
                elif isinstance(percentage, (int, float)):
                    all_percentages.append(float(percentage))

        # Final summary section
        md.write(f"## {MODEL_NAME} SUMMARY\n\n")
        md.write("| Record ID | Total Score | Percentage |\n")
        md.write("|-----------|-------------|-------------|\n")

        for rec_id, total, perc in records_summary:
            md.write(f"| {rec_id} | {total} | {perc} |\n")

        # Compute average rating
        if all_percentages:
            avg_percentage = sum(all_percentages) / len(all_percentages)
            rating_out_of_10 = round(avg_percentage / 10, 1)  # e.g. 82% → 8.2 / 10
        else:
            avg_percentage = 0
            rating_out_of_10 = 0

        md.write(f"\n**Overall Performance Rating: {rating_out_of_10} / 10**\n")

if __name__ == "__main__":
    process_eval_files(INPUT_DIR, OUTPUT_FILE)
