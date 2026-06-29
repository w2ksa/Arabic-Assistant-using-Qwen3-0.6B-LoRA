import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from assistant_core import settings
from assistant_core.prompts import get_system_prompt


def get_base_model_name():
    return settings.BASE_MODEL


def load_assistant(model_name=None):
    model_id = model_name or settings.BASE_MODEL
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype="auto",
        device_map="auto",
    )
    return tokenizer, model


def make_messages(user_prompt, preset="general"):
    return [
        {"role": "system", "content": get_system_prompt(preset)},
        {"role": "user", "content": user_prompt},
    ]


def generate_answer(tokenizer, model, user_prompt, preset="general", thinking=False):
    messages = make_messages(user_prompt, preset=preset)
    chat_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=thinking,
    )
    inputs = tokenizer([chat_text], return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=settings.MAX_NEW_TOKENS,
        temperature=settings.TEMPERATURE,
        top_p=settings.TOP_P,
        top_k=settings.TOP_K,
        do_sample=True,
    )
    generated_tokens = outputs[0][len(inputs.input_ids[0]):]
    return tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
