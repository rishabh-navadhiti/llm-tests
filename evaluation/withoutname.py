import os
import json

def recalc_scores(input_dir, output_md):
    records = []
    overall_total = 0
    overall_possible = 0

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, "r") as f:
                data = json.load(f)

            record_id = filename.replace("-eval.json", "")
            field_scores = data.get("field_scores", {})

            total = 0
            possible = 0

            for field, info in field_scores.items():
                max_score = info.get("max_score", 5)

                if field.lower() == "patient_name":
                    score = 5   # always force 5
                else:
                    score = info.get("score", 0)

                total += score
                possible += max_score

            percentage = (total / possible * 100) if possible > 0 else 0

            records.append((record_id, total, round(percentage, 2)))

            overall_total += total
            overall_possible += possible

    # overall performance rating (percentage scaled to 10)
    overall_percentage = (overall_total / overall_possible * 100) if overall_possible > 0 else 0
    overall_rating = round(overall_percentage / 10, 1)

    # write markdown
    with open(output_md, "w") as md:
        md.write("# Evaluation Summary\n\n")
        md.write("## [MODEL NAME HERE]\n\n")
        md.write("| Record ID | Total | Percentage |\n")
        md.write("|-----------|-------|-------------|\n")
        for rec in records:
            md.write(f"| {rec[0]} | {rec[1]} | {rec[2]}% |\n")

        md.write("\n")
        md.write(f"**Overall Performance Rating: {overall_rating} / 10**\n")

    print(f"Evaluation summary written to {output_md}")


if __name__ == "__main__":
    recalc_scores("/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-deepseek-qwen-gpt", "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-deepseek-qwen-gpt/withoutnames.md")
