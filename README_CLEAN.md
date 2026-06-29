# Arabic Language Assistant using Qwen3 and LoRA

A general-purpose Arabic language assistant built on top of an open-source language model.

This repository is positioned as an NLP and language-model engineering project. It focuses on local inference, Arabic prompt behavior, a simple Gradio interface, dataset structure, validation utilities, and a LoRA-ready adaptation path.

## Current Status

Working prototype with an initial adaptation layer. The next phase is local PC testing, dataset expansion, and adapter training.

## Base Model

- Base model: Qwen/Qwen3-0.6B
- Provider: Qwen Team
- Original model page: https://huggingface.co/Qwen/Qwen3-0.6B

## Developed Components

- Python inference pipeline
- Reusable assistant engine
- Arabic prompt presets
- Gradio local interface
- Sample Arabic instruction dataset
- Dataset validation utility
- Evaluation and portfolio notes
- LoRA-ready improvement path

## Local Usage

Install dependencies:

pip install -r requirements.txt

Run the local interface:

python app.py

Run the command line version:

python inference.py

Validate the dataset:

python tools/validate_dataset.py

## Development Plan

1. Run the project locally.
2. Test the base model responses.
3. Expand the Arabic instruction dataset.
4. Train a LoRA adapter.
5. Compare outputs before and after adaptation.
6. Document the results before publishing trained artifacts.

## Portfolio Summary

Developed and adapted a general-purpose Arabic language assistant based on Qwen3-0.6B using Python, Hugging Face Transformers, and Gradio, with reusable inference code, Arabic prompt presets, dataset validation, and a LoRA-ready improvement path.
