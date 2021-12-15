import heapq
from typing import Optional

import numpy

Position = tuple[int, int]


class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, Position]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: Position, priority: float) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Position:
        return heapq.heappop(self.elements)[1]


def _parse_input(filename: str) -> numpy.ndarray:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        lines = file.readlines()
    return numpy.array([[int(number) for number in line.rstrip()] for line in lines])


def _heuristic(a: Position, b: Position) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def _get_neighbors(position: Position, cave: numpy.ndarray) -> list[Position]:
    neighbors: list[Position] = []
    for new_position in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        node_position = position[0] + new_position[0], position[1] + new_position[1]
        if (
            0 <= node_position[0] < cave.shape[0]
            and 0 <= node_position[1] < cave.shape[1]
        ):
            neighbors.append(node_position)
    return neighbors


def _a_star(start: Position, end: Position, cave: numpy.ndarray) -> int:
    """A ⭐ search. Implementation inspired by www.redblobgames.com."""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Position, Optional[Position]] = {start: None}
    cost_so_far: dict[Position, float] = {start: 0.0}

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next_pos in _get_neighbors(current, cave):
            new_cost = cost_so_far.get(current) + cave[next_pos]
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost + _heuristic(next_pos, end)
                frontier.put(next_pos, priority)
                came_from[next_pos] = current

    return int(cost_so_far.get(end, 0))


def _multiply_cave(cave: numpy.ndarray, k: int) -> numpy.ndarray:
    caves_horizontal = [cave]
    last_cave = cave
    for _ in range(k - 1):
        new_cave = numpy.vectorize(lambda x: x + 1 if x < 9 else 1)(last_cave)
        caves_horizontal.append(new_cave)
        last_cave = new_cave
    caves_vertical = [numpy.concatenate(caves_horizontal, axis=1)]
    last_cave = caves_vertical[0]
    for _ in range(k - 1):
        new_cave = numpy.vectorize(lambda x: x + 1 if x < 9 else 1)(last_cave)
        caves_vertical.append(new_cave)
        last_cave = new_cave
    return numpy.concatenate(caves_vertical, axis=0)


def find_path(filename: str) -> int:
    cave = _parse_input(filename)
    return _a_star((0, 0), (cave.shape[0] - 1, cave.shape[1] - 1), cave)


def find_path_bigger(filename: str, k: int) -> int:
    cave = _parse_input(filename)
    cave = _multiply_cave(cave, k)
    return _a_star((0, 0), (cave.shape[0] - 1, cave.shape[1] - 1), cave)


print(
    (
        find_path("15.txt"),
        find_path_bigger("15.txt", 5),
    )
)
