import os
import json

SCORES_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-Qwen-30B"
OUTPUT_FILE = "eval_result/Eval-Deepseek-Qwen32b/Eval-Qwen-30B.md"

def json_to_markdown(file_path, record_name):
    """Convert a single JSON score file into markdown string."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    md = []
    title = record_name.replace("-eval", "")
    md.append(f"# {title} Score\n")

    # Table header
    md.append("| Title | Score (0-5)| Justification |")
    md.append("|-------|-------|---------------|")

    for field, content in data["field_scores"].items():
        title = field
        score = content.get("score", "")
        justification = content.get("justification", "").replace("\n", " ")
        md.append(f"| {title} | {score} | {justification} |")

    # Totals
    md.append(f"\n**Total Score:** {data.get('total_score', '')}/35")
    md.append(f"\n**Percentage:** {data.get('percentage', '')}%\n")

    # Summary
    summary = data.get("overall_summary", "")
    if summary:
        md.append(f"**Overall Summary:** {summary}\n")

    md.append("\n---\n\n")  # Separator between records
    return "\n".join(md)


def main():
    all_markdown = []
    for filename in sorted(os.listdir(SCORES_DIR)):
        if filename.endswith(".json"):
            record_name = os.path.splitext(filename)[0]  # e.g. REC-6612
            file_path = os.path.join(SCORES_DIR, filename)
            all_markdown.append(json_to_markdown(file_path, record_name))

    # Write combined markdown
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(all_markdown))

    print(f"✅ Markdown report generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
