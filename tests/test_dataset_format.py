import json
from pathlib import Path


def test_sample_dataset_has_required_fields():
    path = Path("data/sample_dataset.jsonl")
    required = {"instruction", "input", "output"}

    rows = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                rows.append(json.loads(line))

    assert rows
    for row in rows:
        assert required.issubset(row.keys())
        assert row["instruction"].strip()
        assert row["output"].strip()
