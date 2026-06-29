# Development Roadmap

This project is designed to grow gradually from a local prototype into a fine-tuned Arabic assistant.

## Phase 1: Repository Foundation

Status: Done

Completed items:

- Created project repository.
- Added README documentation.
- Added local inference script.
- Added Gradio interface.
- Added sample dataset.
- Added attribution documentation.
- Added fine-tuning placeholder.

## Phase 2: Local PC Testing

Goal: Run the base model on a local PC or laptop.

Tasks:

- Install Python environment.
- Install project dependencies.
- Run `python inference.py`.
- Run `python app.py`.
- Test Arabic and English prompts.
- Record examples of model responses.

Expected output:

- Screenshots of the local UI.
- Notes about speed, memory usage, and output quality.

## Phase 3: Dataset Expansion

Goal: Build a stronger custom Arabic instruction dataset.

Target size:

- Start: 50 examples
- Next: 200 examples
- Later: 1,000+ examples

Dataset categories:

- Arabic explanation
- Summarization
- Rewriting
- Technical Q&A
- Business writing
- Productivity assistance
- General assistant responses

## Phase 4: LoRA Fine-Tuning

Goal: Train a LoRA adapter on the custom dataset.

Planned tools:

- Python
- PyTorch
- Hugging Face Transformers
- PEFT
- TRL
- Datasets

Training environments:

- Local GPU if available
- Cloud GPU if needed

Expected output:

- LoRA adapter saved under `outputs/`
- Training notes
- Loss screenshots or logs
- Before/after examples

## Phase 5: Evaluation

Goal: Compare the base model and the adapted model.

Evaluation method:

- Prepare fixed prompts.
- Run prompts on the base model.
- Run the same prompts after LoRA training.
- Compare clarity, Arabic quality, consistency, and task-following.

## Phase 6: Portfolio Upgrade

Goal: Make the repository stronger for LinkedIn and CV use.

Planned additions:

- Project screenshots
- Training notebook
- Better dataset documentation
- Model card
- Demo video
- LinkedIn post
- CV bullet points

## Current Status Summary

The project is currently a working foundation for a general Arabic AI assistant using an open-source base model. Fine-tuning is prepared as the next phase and should be completed after local environment testing.
