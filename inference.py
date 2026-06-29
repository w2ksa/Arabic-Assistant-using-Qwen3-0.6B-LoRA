import argparse

from assistant_core.engine import generate_answer, load_assistant


def main():
    parser = argparse.ArgumentParser(description="Run the Arabic Assistant locally")
    parser.add_argument("--preset", default="general", choices=["general", "technical", "business"])
    parser.add_argument("--thinking", action="store_true")
    args = parser.parse_args()

    tokenizer, model = load_assistant()

    print("Arabic Assistant using Qwen3-0.6B")
    print("Preset:", args.preset)
    print("Type 'exit' to stop.\n")

    while True:
        prompt = input("You: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        if not prompt:
            continue

        response = generate_answer(
            tokenizer=tokenizer,
            model=model,
            user_prompt=prompt,
            preset=args.preset,
            thinking=args.thinking,
        )
        print("Assistant:", response, "\n")


if __name__ == "__main__":
    main()
