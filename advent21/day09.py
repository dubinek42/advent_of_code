import operator

import numpy
from scipy import ndimage

NEIGHBORS_FOOTPRINT = numpy.array(
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]
)
NEIGHBORS_DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def _parse_input(filename: str) -> numpy.ndarray:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.readlines()
    return numpy.array([[int(d) for d in list(line.rstrip())] for line in text_input])


def _my_filter(values: numpy.ndarray) -> int:
    """Apply conditions to value and its neighbors.

    Params:
        values: Value (in the middle) and its 4 neighbors.

    Returns:
        Value + 1 if condition is met, 0 otherwise.

    """
    value = int(values[2])
    neighbors = numpy.delete(values, 2)
    return value + 1 if all(value < x for x in neighbors) else 0


def _find_minima(area: numpy.ndarray) -> numpy.ndarray:
    return ndimage.generic_filter(
        area, _my_filter, footprint=NEIGHBORS_FOOTPRINT, mode="constant", cval=42
    )


def _basin_size(area: numpy.ndarray, x: int, y: int) -> int:
    # Surround area with 9s so we don't have to check boundaries.
    area = numpy.pad(area, 1, mode="constant", constant_values=9)
    x, y = x + 1, y + 1

    def _check_neighbors(coords: tuple, visited: set):
        result = 0
        for direction in NEIGHBORS_DIRECTIONS:
            new_x, new_y = tuple(map(operator.add, coords, direction))
            if area[new_x][new_y] < 9 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                result += 1 + _check_neighbors((new_x, new_y), visited)
        return result

    return _check_neighbors((x, y), set())


def calculate_minima(filename: str) -> int:
    area = _parse_input(filename)
    minima = _find_minima(area)
    return int(numpy.sum(minima))


def calculate_basins(filename: str) -> int:
    area = _parse_input(filename)
    minima_locations = list(zip(*numpy.where(_find_minima(area) == area + 1)))
    basin_sizes = sorted([_basin_size(area, *coords) for coords in minima_locations])
    return int(numpy.prod(basin_sizes[-3:]))


print(calculate_minima("09.txt"))
print(calculate_basins("09.txt"))
