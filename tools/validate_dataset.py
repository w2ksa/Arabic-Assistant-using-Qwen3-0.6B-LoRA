import json
from pathlib import Path

REQUIRED_FIELDS = {"instruction", "input", "output"}


def validate_jsonl(path):
    path = Path(path)
    errors = []
    rows = 0

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            rows += 1
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"Line {line_number}: invalid JSON - {exc}")
                continue

            missing = REQUIRED_FIELDS - set(item.keys())
            if missing:
                errors.append(f"Line {line_number}: missing fields {sorted(missing)}")

            if not str(item.get("instruction", "")).strip():
                errors.append(f"Line {line_number}: instruction is empty")

            if not str(item.get("output", "")).strip():
                errors.append(f"Line {line_number}: output is empty")

    return rows, errors


def main():
    dataset_path = "data/sample_dataset.jsonl"
    rows, errors = validate_jsonl(dataset_path)
    print(f"Rows checked: {rows}")

    if errors:
        print("Dataset validation failed:")
        for error in errors:
            print("-", error)
        raise SystemExit(1)

    print("Dataset validation passed.")


if __name__ == "__main__":
    main()
