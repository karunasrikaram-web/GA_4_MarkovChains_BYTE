# Comparison Note: Markov Chain vs Neural Text Generation

This project uses a word-level order-2 Markov chain as a statistical baseline. Its main strengths are simplicity, speed, transparency, and very low computational cost. The model is easy to implement, and its next-word choice can be inspected directly from the transition table.

Its main weakness is limited context. The generator only uses the previous two words, so it can lose long-range meaning and may repeat phrases, especially when the corpus is small. The quality of its output also depends heavily on the training corpus.

Neural text generators generally model much richer context and can produce more coherent long-form text, but they require substantially more computation, memory, and engineering effort. They can also be harder to inspect because their learned representations are complex.

The Markov model is therefore useful as a simple baseline: it demonstrates probabilistic text generation and provides a transparent reference point for later experiments with neural models.
