from typing import Callable, Optional

import numpy


def _parse_input(filename: str) -> list[list[tuple[int, ...]]]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        lines = file.readlines()
    return [
        [
            tuple(points)
            for points in [
                map(int, pair.split(",")) for pair in line.rstrip().split(" -> ")
            ]
        ]
        for line in lines
    ]


def _get_size(points: list[list[tuple[int, ...]]]) -> tuple[int, ...]:
    """Get max values of x and y from all coordinates.

    Reverse order for better vizualization.
    """
    return tuple(
        int(max(zipped)) + 1  # type: ignore[call-overload, type-var]
        for zipped in map(list, zip(*[coords for pair in points for coords in pair]))
    )[::-1]


def _draw_line(field: numpy.ndarray, points: list[tuple]) -> numpy.ndarray:
    """Add 1 to points in field that underlay line constructed from pair of coords."""
    y, x = zip(*points)  # Work with reversed axes.
    # Swap axes if needed, so that we always have the "easier" axis as X.
    transpose = abs(x[1] - x[0]) < abs(y[1] - y[0])
    if transpose:
        field = field.T
        x, y = y, x
    # Swap directions if needed, so that we always go from left to right.
    if x[0] > x[1]:
        x, y = x[::-1], y[::-1]
    # Find the points that line goes through.
    x_fill = numpy.arange(x[0], x[1] + 1)
    y_fill = numpy.round(
        ((y[1] - y[0]) / (x[1] - x[0])) * (x_fill - x[0]) + y[0]
    ).astype(x_fill.dtype)
    # Increment those points.
    field[x_fill, y_fill] += 1
    return field.T if transpose else field


def _draw_all_lines(
    points: list[list[tuple[int, ...]]],
    restriction: Optional[Callable],
):
    field = numpy.zeros(_get_size(points))
    for pair in points:
        if restriction and not restriction(pair):
            continue
        field = _draw_line(field, pair)
    return field


def _count_overlaps(field: numpy.ndarray):
    return numpy.count_nonzero(field > 1)


def _restriction(coords: list[tuple[int, int]]) -> bool:
    """For first part of day 5: Filter only horizontal and vertical lines."""
    return coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]


def find_overlaps(filename: str) -> tuple[int, int]:
    """Run the whole thing."""
    coord_pairs = _parse_input(filename)
    return (
        _count_overlaps(_draw_all_lines(coord_pairs, _restriction)),
        _count_overlaps(_draw_all_lines(coord_pairs, None)),
    )


print(find_overlaps("05.txt"))
