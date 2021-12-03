from typing import List, Callable

test_input = ["00100", "11110", "10110", "10111", "10101", "01111",
              "00111", "11100", "10000", "11001", "00010", "01010"]

with open("inputs/03.txt") as file:
    lines = file.readlines()
    puzzle_input = [line.rstrip() for line in lines]


def _count_occurences(diagnostics: List[str]) -> dict:
    results = {i: {"0": 0, "1": 0} for i in range(len(diagnostics[0]))}
    for number in diagnostics:
        for i in range(len(number)):
            results[i][number[i]] += 1
    return results


def _rate(occurences: dict, fn: Callable) -> int:
    return int("".join([fn(occurences[i], key=occurences[i].get) for i in occurences.keys()]), 2)


def _hack_default(fn: Callable) -> dict:
    return {"1": 0, "0": 0} if fn == max else {"0": 0, "1": 0}


def _do_filtering(i: int, diagnostics: List[str], fn: Callable) -> int:
    results = _hack_default(fn)
    for number in diagnostics:
        results[number[i]] += 1
    keeping = fn(results, key=results.get)
    filtered = [number for number in diagnostics if number[i] == keeping]
    if len(filtered) == 1:
        return int(filtered[0], 2)
    else:
        return _do_filtering(i + 1, filtered, fn)


def power_consumption(diagnostics: List[str]) -> int:
    occurences = _count_occurences(diagnostics)
    return _rate(occurences, max) * _rate(occurences, min)


def life_support(diagnostics: List[str]) -> int:
    return _do_filtering(0, diagnostics, max) * _do_filtering(0, diagnostics, min)


print(power_consumption(puzzle_input))
print(life_support(puzzle_input))
