import argparse
import json
from pathlib import Path


def read_jsonl(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def preview_dataset(path):
    rows = read_jsonl(path)
    print("Dataset path:", path)
    print("Rows:", len(rows))
    if rows:
        print("First instruction:", rows[0].get("instruction", ""))
    return rows


def main():
    parser = argparse.ArgumentParser(description="Adapter preparation script")
    parser.add_argument("--dataset", default="data/sample_dataset.jsonl")
    parser.add_argument("--output", default="outputs/qwen3-arabic-adapter")
    args = parser.parse_args()

    preview_dataset(args.dataset)
    Path(args.output).mkdir(parents=True, exist_ok=True)

    notes_path = Path(args.output) / "training_plan.txt"
    notes_path.write_text(
        "Base model: Qwen/Qwen3-0.6B\n"
        "Method: LoRA adapter fine-tuning\n"
        "Status: prepared for local GPU or cloud GPU run\n",
        encoding="utf-8",
    )
    print("Prepared output folder:", args.output)


if __name__ == "__main__":
    main()
