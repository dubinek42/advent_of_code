from collections import Counter


def _parse_input(filename: str) -> tuple[str, dict]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.read()
    template, pairs = text_input.split("\n\n")
    insertions = dict(
        (k, v) for k, v in (pair.split(" -> ") for pair in pairs.split("\n"))
    )
    return template, insertions


def _apply_instruction(pair: str, instructions: dict) -> tuple[tuple[str, str], str]:
    """From one pair create 2 pairs according to insertion rules.

    Returns:
        2 new pairs and the letter that was added.

    """
    new_pairs = (pair[0] + instructions[pair], instructions[pair] + pair[1])
    return new_pairs, instructions[pair]


def _get_starting(template: str) -> tuple[Counter, Counter]:
    """Count letters and pairs of letters in starting template string."""
    pairs = Counter(template[i : i + 2] for i in range(len(template) - 1))
    occurences = Counter(template)
    return pairs, occurences


def _one_step(pairs: Counter, instructions: dict) -> tuple[Counter, Counter]:
    """For each pair create 2 new pairs and count what has been added."""
    added: Counter = Counter()
    pairs_copy = pairs.copy()
    for k, v in pairs.items():
        pairs_copy[k] -= v
        if pairs_copy[k] < 0:
            pairs_copy[k] = 0
        new_pairs, new_letter = _apply_instruction(k, instructions)
        for p in new_pairs:
            pairs_copy += Counter({p: v})
        added += Counter({new_letter: v})
    return pairs_copy, added


def _repeat_steps(
    pairs: Counter, occurences: Counter, insertions: dict, steps: int
) -> Counter:
    for _ in range(steps):
        pairs, added = _one_step(pairs, insertions)
        occurences += added
    return occurences


def _score(occurences: Counter) -> int:
    """Returns most common element minus least common element."""
    numbers = list(sorted(number for number in occurences.values()))
    return numbers[-1] - numbers[0]


def polymerize(filename: str, steps: int) -> int:
    template, insertions = _parse_input(filename)
    pairs, occurences = _get_starting(template)
    occurences = _repeat_steps(pairs, occurences, insertions, steps)
    return _score(occurences)


print(polymerize("14.txt", 10))
print(polymerize("14.txt", 40))
