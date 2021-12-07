import typing
from functools import lru_cache

test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def _parse_input(filename: str) -> typing.List[int]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.read()
    return [int(x) for x in text_input.split(",")]


def _try_position(crabs: typing.List[int], position: int, fn: typing.Callable) -> int:
    """Count fuel usage for position based on input function."""
    fuel = 0
    for crab in crabs:
        fuel += fn(abs(crab - position))
    return fuel


@lru_cache(maxsize=2000)
def expensive_fuel(distance: int) -> int:
    """Calculate fuel cost for part 2."""
    return sum(range(distance + 1))


def count_fuel(filename: str) -> typing.Tuple[int, int]:
    crabs = _parse_input(filename)
    max_position = max(crabs)
    cheap = min(_try_position(crabs, i, lambda x: x) for i in range(max_position + 1))
    expensive = min(
        _try_position(crabs, i, expensive_fuel) for i in range(max_position + 1)
    )
    return cheap, expensive


print(count_fuel("07.txt"))
