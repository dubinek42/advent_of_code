import operator
from typing import Set, Tuple

import numpy

NEIGHBORS_DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]


def _parse_input(filename: str) -> numpy.ndarray:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.readlines()
    return numpy.array([[int(d) for d in list(line.rstrip())] for line in text_input])


def _flash(
    grid: numpy.ndarray, coords: Tuple[int, int], flashed: Set[Tuple[int, int]]
) -> Tuple[numpy.ndarray, set]:
    """Do the flash. Recursively calculate all flashes and return total number."""
    flashed.add(coords)
    for direction in NEIGHBORS_DIRECTIONS:
        new_x, new_y = tuple(map(operator.add, coords, direction))
        if 0 <= new_x < grid.shape[0] and 0 <= new_y < grid.shape[1]:
            grid[new_x][new_y] += 1
            if grid[new_x][new_y] > 9 and (new_x, new_y) not in flashed:
                grid, flashed = _flash(grid, (new_x, new_y), flashed)
    return grid, flashed


def _step(grid: numpy.ndarray) -> Tuple[numpy.ndarray, int]:
    """Make one step - increment all and determine flashes."""
    grid = numpy.vectorize(lambda q: q + 1)(grid)
    flashed: Set[Tuple[int, int]] = set()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] > 9 and (x, y) not in flashed:
                grid, flashed = _flash(grid, (x, y), flashed)
    for x, y in flashed:
        grid[x][y] = 0
    return grid, len(flashed)


def count_flashes(grid: numpy.ndarray, steps: int) -> int:
    """Count how many times octopuses flash in given steps."""
    flashes = 0
    for _ in range(steps):
        grid, inc = _step(grid)
        flashes += inc
    return flashes


def when_mega_flash(grid: numpy.ndarray) -> int:
    """Find the first step when all octopuses flash at once."""
    steps = 0
    while 42:
        steps += 1
        grid, flashed = _step(grid)
        if flashed == grid.size:
            break
    return steps


def run(filename: str) -> Tuple[int, int]:
    grid = _parse_input(filename)
    return count_flashes(grid, 100), when_mega_flash(grid)


print(run("11.txt"))
