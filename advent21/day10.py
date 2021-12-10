from typing import List, Tuple

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def _parse_input(filename: str) -> List[str]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.readlines()
    return [line.rstrip() for line in text_input]


def _illegal(line: str) -> int:
    stack = []
    for c in line:
        if c in ("(", "[", "{", "<"):
            stack.append(c)
            continue
        s = stack.pop()
        if (
            (s == "(" and not c == ")")
            or (s == "[" and not c == "]")
            or (s == "{" and not c == "}")
            or (s == "<" and not c == ">")
        ):
            return SCORES[c]
    return 0


def _incomplete(line: str) -> int:
    stack = []
    for c in line:
        if c in ("(", "[", "{", "<"):
            stack.append(c)
        else:
            stack.pop()
    stack.reverse()
    score = 0
    for c in stack:
        score *= 5
        score += SCORES[c]
    return score


def run_checks(filename: str) -> Tuple[int, int]:
    lines = _parse_input(filename)

    final_illegal_score = sum(_illegal(line) for line in lines)

    incomplete = [line for line in lines if not _illegal(line)]
    incomplete_scores = sorted([_incomplete(line) for line in incomplete])
    final_incpomlete_score = incomplete_scores[len(incomplete_scores) // 2]

    return final_illegal_score, final_incpomlete_score


print(run_checks("10.txt"))
