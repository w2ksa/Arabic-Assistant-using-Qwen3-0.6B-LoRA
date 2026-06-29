import gradio as gr

from assistant_core.engine import generate_answer, load_assistant


tokenizer = None
model = None


def load_model_once():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer, model = load_assistant()
    return tokenizer, model


def respond(prompt, preset, thinking_mode):
    if not prompt or not prompt.strip():
        return "اكتب رسالة أولًا."

    tokenizer, model = load_model_once()
    return generate_answer(
        tokenizer=tokenizer,
        model=model,
        user_prompt=prompt.strip(),
        preset=preset,
        thinking=thinking_mode,
    )


EXAMPLES = [
    ["اشرح مفهوم الشبكات العصبية بطريقة مبسطة", "technical", False],
    ["لخص فكرة المشروع في ثلاث نقاط", "general", False],
    ["اكتب وصفًا مهنيًا قصيرًا لمشروع مساعد ذكاء اصطناعي عربي", "business", False],
]


with gr.Blocks(title="Arabic Assistant using Qwen3-0.6B") as demo:
    gr.Markdown("# Arabic Assistant using Qwen3-0.6B + LoRA")
    gr.Markdown(
        "General Arabic AI assistant prototype built on an open-source base model. "
        "This version includes reusable inference code, prompt presets, a local UI, "
        "and a development path for future LoRA fine-tuning."
    )

    with gr.Row():
        preset = gr.Dropdown(
            choices=["general", "technical", "business"],
            value="general",
            label="Assistant Mode",
        )
        thinking_mode = gr.Checkbox(label="Enable Qwen thinking mode", value=False)

    prompt = gr.Textbox(
        label="Prompt / السؤال",
        lines=6,
        placeholder="مثال: اشرح مفهوم التعلم الآلي بطريقة مبسطة",
    )
    output = gr.Textbox(label="Assistant Response", lines=12)
    button = gr.Button("Generate")

    button.click(fn=respond, inputs=[prompt, preset, thinking_mode], outputs=output)

    gr.Examples(
        examples=EXAMPLES,
        inputs=[prompt, preset, thinking_mode],
        outputs=output,
        fn=respond,
        cache_examples=False,
    )


if __name__ == "__main__":
    demo.launch()
