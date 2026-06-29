import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "Qwen/Qwen3-0.6B"

SYSTEM_PROMPT = """
You are a helpful Arabic AI assistant. Answer clearly, directly, and professionally.
When the user asks in Arabic, reply in Arabic. When the user asks in English, reply in English.
""".strip()


def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype="auto",
        device_map="auto",
    )
    return tokenizer, model


def generate_response(tokenizer, model, user_prompt: str, enable_thinking: bool = False) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=enable_thinking,
    )

    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.8,
        top_k=20,
        do_sample=True,
    )

    output_ids = generated_ids[0][len(inputs.input_ids[0]):]
    response = tokenizer.decode(output_ids, skip_special_tokens=True).strip()

    return response


def main():
    tokenizer, model = load_model()
    print("Arabic Assistant using Qwen3-0.6B")
    print("Type 'exit' to stop.\n")

    while True:
        prompt = input("You: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        if not prompt:
            continue

        response = generate_response(tokenizer, model, prompt)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
