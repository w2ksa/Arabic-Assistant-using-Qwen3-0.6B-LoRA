# Arabic Assistant using Qwen3-0.6B + LoRA

A general-purpose Arabic AI assistant prototype built on top of the open-source **Qwen/Qwen3-0.6B** language model.

The project is designed as a practical learning and portfolio project for running, testing, and gradually fine-tuning a small language model using Python, Hugging Face Transformers, and LoRA.

> Status: Working prototype + fine-tuning-ready pipeline.  
> The repository does not include trained model weights yet. LoRA fine-tuning is prepared as a next development phase.

---

## Project Goal

The goal is to start from an existing open-source language model instead of training a model from scratch, then add a clean Python structure around it:

- Local inference script
- Simple web UI
- Prompt templates for Arabic responses
- Sample Arabic instruction dataset
- LoRA fine-tuning script
- Evaluation examples
- Clear attribution to the original base model

This follows a practical machine-learning workflow: **use a base model, adapt it, test it, document it, then improve it over time.**

---

## Base Model

This project uses:

- **Model:** `Qwen/Qwen3-0.6B`
- **Provider:** Qwen Team
- **Model type:** Causal language model
- **License:** Apache 2.0, according to the model card on Hugging Face

Original model page:

```text
https://huggingface.co/Qwen/Qwen3-0.6B
```

---

## What I Added

This repository does not claim that the base model was created from scratch. The original model belongs to the Qwen Team.

My additions in this project:

1. Built a Python inference wrapper for the base model.
2. Added Arabic-first prompt formatting.
3. Added a Gradio web interface for local testing.
4. Created a sample Arabic instruction dataset.
5. Added a LoRA fine-tuning script for future training.
6. Added before/after evaluation templates.
7. Documented the development roadmap and attribution clearly.

---

## Use Cases

The assistant is intentionally general, not limited to one field. It can be adapted for:

- Arabic question answering
- Text summarization
- Writing assistance
- Idea generation
- Technical explanations
- Business and productivity use cases
- Future domain-specific fine-tuning

---

## Repository Structure

```text
.
├── app.py                    # Gradio web interface
├── inference.py              # Local inference script
├── train_lora.py             # LoRA fine-tuning script
├── requirements.txt          # Python dependencies
├── data/
│   └── sample_dataset.jsonl  # Sample Arabic instruction dataset
├── docs/
│   ├── attribution.md        # Source and contribution notes
│   ├── roadmap.md            # Development plan
│   └── evaluation.md         # Manual evaluation examples
└── README.md
```

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Local Inference

```bash
python inference.py
```

Example prompt:

```text
اشرح مفهوم الشبكات العصبية بطريقة مبسطة.
```

---

## Run Web Interface

```bash
python app.py
```

Then open the local Gradio link in your browser.

---

## Fine-Tuning Plan

The project includes `train_lora.py` as a starting point for LoRA fine-tuning.

Expected workflow:

1. Expand the dataset in `data/sample_dataset.jsonl`.
2. Run LoRA training on a local GPU or rented GPU.
3. Save the LoRA adapter.
4. Compare model behavior before and after fine-tuning.
5. Publish the adapter or training results separately.

---

## Ethical and Legal Notice

This project is based on an open-source model and includes clear attribution. The base model is not mine. My work is focused on implementation, adaptation, documentation, and future fine-tuning.

Do not upload private, sensitive, or copyrighted training data without permission.

---

## Portfolio Summary

A concise CV/LinkedIn description:

```text
Built a general-purpose Arabic AI assistant prototype using Qwen3-0.6B, Python, Hugging Face Transformers, Gradio, and a LoRA fine-tuning pipeline. The project includes local inference, a web UI, Arabic prompt formatting, sample instruction data, attribution documentation, and a roadmap for progressive model adaptation.
```
