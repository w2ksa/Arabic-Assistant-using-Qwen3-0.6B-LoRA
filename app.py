import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "Qwen/Qwen3-0.6B"

SYSTEM_PROMPT = """
You are a helpful Arabic AI assistant. Answer clearly, directly, and professionally.
Support general use cases such as summarization, explanation, writing help, planning, and technical Q&A.
""".strip()


tokenizer = None
model = None


def load_model_once():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype="auto",
            device_map="auto",
        )
    return tokenizer, model


def respond(prompt, thinking_mode):
    if not prompt or not prompt.strip():
        return "اكتب رسالة أولًا."

    tokenizer, model = load_model_once()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt.strip()},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=thinking_mode,
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
    answer = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
    return answer


with gr.Blocks(title="Arabic Assistant using Qwen3-0.6B") as demo:
    gr.Markdown("# Arabic Assistant using Qwen3-0.6B + LoRA")
    gr.Markdown(
        "General Arabic AI assistant prototype built on Qwen3-0.6B. "
        "This interface runs the base model locally and prepares the project for future LoRA fine-tuning."
    )

    prompt = gr.Textbox(
        label="Prompt / السؤال",
        lines=6,
        placeholder="مثال: اشرح مفهوم التعلم الآلي بطريقة مبسطة",
    )
    thinking_mode = gr.Checkbox(label="Enable Qwen thinking mode", value=False)
    output = gr.Textbox(label="Assistant Response", lines=10)
    button = gr.Button("Generate")

    button.click(fn=respond, inputs=[prompt, thinking_mode], outputs=output)


if __name__ == "__main__":
    demo.launch()
