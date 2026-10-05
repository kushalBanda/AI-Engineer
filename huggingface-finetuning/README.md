# Hugging Face

[← AI Engineer](../README.md)

Train and evaluate open-source models. The notebook here fine-tunes a small LLM and measures the gain, so you see before and after numbers instead of a guess.

## What's inside

| Path | What it does |
| :--- | :--- |
| [`hf-model-trainer-skill.ipynb`](hf-model-trainer-skill.ipynb) | Fine-tunes `Qwen/Qwen3-0.6B` to route customer support tickets. Trains on the Bitext customer support dataset and compares routing metrics before and after, with plots |

Tier: advanced. Stack: Transformers, PEFT, Datasets, PyTorch.

## Run

1. Open the notebook in Jupyter, VS Code, or Colab.
2. Run the setup cell. It installs the dependencies with `uv`, or with `pip` if you prefer.
3. Run the cells in order. A GPU speeds up training. Apple Silicon (MPS) also works.

## Depends on

- A Hugging Face account and token for dataset and model downloads.


## Articles

Coming soon.
