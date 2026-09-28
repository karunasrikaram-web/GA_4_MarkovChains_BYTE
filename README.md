# Task 4 — Text Generation using Markov Chains

A simple statistical baseline for text generation using a word-level order-2 Markov chain.

## Task requirements covered

- Source corpus reference and license
- Markov generator implementation
- 20 distinct seeds/prompts
- 20 generated text samples
- Comparison note against neural text generation
- Reproducible run instructions

## Corpus

The included `corpus.txt` is an original mini-corpus written specifically for this project.
It contains engineering, programming, machine learning, and generative-AI sentences.

**License:** MIT for the original project files and corpus.

For a larger external corpus, Project Gutenberg's *Alice's Adventures in Wonderland* is
public domain in the USA. See:
https://www.gutenberg.org/ebooks/11

Always check the applicable copyright rules in your country before redistributing an external corpus.

## How it works

The generator uses an order-2 word-level Markov model:

`(previous word 1, previous word 2) -> possible next words`

A random next word is sampled from the learned transition table.

## Run

Requirements: Python 3.9+; no third-party packages are required.

```bash
python markov_generator.py
```

Use your own seed:

```bash
python markov_generator.py --seed "Artificial intelligence" --length 40 --random-seed 7
```

## Files

- `markov_generator.py` — generator implementation
- `corpus.txt` — original training corpus
- `prompts.txt` — 20 seeds/prompts
- `generated_samples/` — 20 generated outputs
- `comparison.md` — short comparison with neural text generation

## Limitations

This is intentionally a small statistical baseline. A small corpus and short context can cause
repetition, abrupt topic changes, and weak long-range coherence.
