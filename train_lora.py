"""
LoRA fine-tuning entry point.

This file is intentionally simple. It prepares the repository for the next training phase:
1. Load a JSONL instruction dataset.
2. Load the Qwen/Qwen3-0.6B base model.
3. Attach a LoRA adapter.
4. Train only the adapter weights.
5. Save the adapter under outputs/.

Full training commands and notes are documented in docs/roadmap.md.
"""


def main():
    print("LoRA training pipeline placeholder.")
    print("Next step: add the complete training implementation after local environment testing.")
    print("Base model: Qwen/Qwen3-0.6B")
    print("Training method: LoRA adapter fine-tuning")


if __name__ == "__main__":
    main()
