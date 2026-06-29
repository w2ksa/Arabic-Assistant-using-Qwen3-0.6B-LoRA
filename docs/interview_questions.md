# Interview Questions

## What did you build?

I developed and adapted a general-purpose Arabic AI assistant prototype based on Qwen3-0.6B.

## Did you train the model from scratch?

No. The project uses an open-source base model and builds an application and adaptation layer around it.

## What did you add?

- Local inference pipeline.
- Reusable assistant engine.
- Gradio web interface.
- Arabic prompt presets.
- Sample Arabic instruction dataset.
- Dataset validation tool.
- Evaluation notes.
- LoRA-ready improvement path.

## What is the next technical step?

The next step is to run the system locally, expand the dataset, then train a LoRA adapter and compare the model before and after adaptation.

## Why use LoRA?

LoRA is suitable for individual developers because it allows model adaptation without retraining all model weights. This makes experimentation more practical on limited hardware or rented GPUs.
