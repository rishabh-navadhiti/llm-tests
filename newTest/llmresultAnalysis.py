import os
import json

# 📂 Directory containing evaluation JSON files
INPUT_DIR = "/Users/rish/Development/runpod dev/llm-tests/newTest/Qwen3-30B-A3B/LLM-eval"
OUTPUT_FILE = "/Users/rish/Development/runpod dev/llm-tests/newTest/Qwen3-30B-A3B/Results/LLM-Report.md"
MODEL_NAME = "Medgemma 27b"

def process_eval_files(input_dir, output_file):
    records_summary = []
    all_percentages = []

    # For consolidated field scores
    field_names = None
    field_scores_by_record = []  # list of dicts: {record_id, field1: score, ...}
    field_totals = {}  # aggregate sum per field

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

                # Capture field names once
                if field_names is None:
                    field_names = list(data["field_scores"].keys())
                    # initialize totals
                    for field in field_names:
                        field_totals[field] = 0

                # Collect scores for consolidated view
                record_fields = {"Record ID": record_id}

                for field, details in data["field_scores"].items():
                    score = details.get("score", 0)
                    justification = details.get("justification", "").replace("\n", " ")
                    md.write(f"| {field} | {score} | {justification} |\n")

                    # Store for summary
                    record_fields[field] = score
                    field_totals[field] += score

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
                field_scores_by_record.append(record_fields)

                # Collect numeric percentage
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

        # ================================
        # Consolidated Field Score Table
        # ================================
        if field_names:
            md.write("\n## Field Scores by Record\n\n")
            md.write("| Record ID | " + " | ".join(field_names) + " | Total/35 |\n")
            md.write("|-----------|" + "|".join(["-----------"] * len(field_names)) + "|-----------|\n")

            for record in field_scores_by_record:
                row_fields = [str(record.get(field, "")) for field in field_names]
                total_score = sum(record.get(field, 0) for field in field_names)
                row = [record["Record ID"]] + row_fields + [f"{total_score}/35"]
                md.write("| " + " | ".join(row) + " |\n")


            # ================================
            # Average per Field (scaled to 10)
            # ================================
            md.write("\n## Average Field Ratings\n\n")
            md.write("| Key | Rating (/10) |\n")
            md.write("|-----|--------------|\n")

            num_records = len(field_scores_by_record)
            for field in field_names:
                avg_score = field_totals[field] / num_records if num_records > 0 else 0
                rating_out_of_10 = round((avg_score / 5) * 10, 1)  # scale to 10
                md.write(f"| {field} | {rating_out_of_10} |\n")


if __name__ == "__main__":
    process_eval_files(INPUT_DIR, OUTPUT_FILE)
