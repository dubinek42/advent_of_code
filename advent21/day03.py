from typing import Callable


def _parse_input(filename: str) -> list[str]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]


def _count_occurences(diagnostics: list[str]) -> dict:
    results = {i: {"0": 0, "1": 0} for i in range(len(diagnostics[0]))}
    for number in diagnostics:
        for i, _ in enumerate(number):
            results[i][number[i]] += 1
    return results


def _rate(occurences: dict, func: Callable) -> int:
    return int(
        "".join(
            [func(occurences[i], key=occurences[i].get) for i in occurences.keys()]
        ),
        2,
    )


def _hack_default(func: Callable) -> dict:
    return {"1": 0, "0": 0} if func == max else {"0": 0, "1": 0}


def _do_filtering(i: int, diagnostics: list[str], func: Callable) -> int:
    results = _hack_default(func)
    for number in diagnostics:
        results[number[i]] += 1
    keeping = func(results, key=results.get)
    filtered = [number for number in diagnostics if number[i] == keeping]
    if len(filtered) == 1:
        return int(filtered[0], 2)
    else:
        return _do_filtering(i + 1, filtered, func)


def power_consumption(diagnostics: list[str]) -> int:
    occurences = _count_occurences(diagnostics)
    return _rate(occurences, max) * _rate(occurences, min)


def life_support(diagnostics: list[str]) -> int:
    return _do_filtering(0, diagnostics, max) * _do_filtering(0, diagnostics, min)


def run_both(filename: str) -> tuple[int, int]:
    diagnostics = _parse_input(filename)
    return power_consumption(diagnostics), life_support(diagnostics)


print(run_both("03.txt"))
