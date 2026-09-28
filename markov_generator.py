import argparse
import random
import re
from collections import defaultdict
from pathlib import Path

def tokenize(text):
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*|[.,!?;:]", text)

def build_model(tokens):
    transitions = defaultdict(list)
    for i in range(len(tokens) - 2):
        state = (tokens[i].lower(), tokens[i + 1].lower())
        transitions[state].append(tokens[i + 2])
    return transitions

def generate(seed, transitions, length=35, seed_value=42):
    rng = random.Random(seed_value)
    seed_tokens = tokenize(seed)
    if len(seed_tokens) >= 2:
        state = (seed_tokens[-2].lower(), seed_tokens[-1].lower())
    else:
        candidates = [k for k in transitions if k[0].startswith(seed_tokens[0].lower())]
        state = rng.choice(candidates) if candidates else rng.choice(list(transitions))

    output = seed_tokens[:]
    for _ in range(length):
        choices = transitions.get(state)
        if not choices:
            state = rng.choice(list(transitions))
            choices = transitions[state]
        nxt = rng.choice(choices)
        output.append(nxt)
        state = (state[1], nxt.lower())

    text = " ".join(output)
    return re.sub(r"\s+([.,!?;:])", r"\1", text)

def main():
    parser = argparse.ArgumentParser(description="Word-level order-2 Markov text generator")
    parser.add_argument("--corpus", default="corpus.txt")
    parser.add_argument("--seed", default="Engineering students")
    parser.add_argument("--length", type=int, default=35)
    parser.add_argument("--random-seed", type=int, default=42)
    args = parser.parse_args()

    corpus = Path(args.corpus).read_text(encoding="utf-8")
    tokens = tokenize(corpus)
    transitions = build_model(tokens)
    print(generate(args.seed, transitions, args.length, args.random_seed))

if __name__ == "__main__":
    main()
