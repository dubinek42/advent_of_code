import typing

import numpy
from pydantic import BaseModel


class Point(BaseModel):
    number: int
    marked: bool = False


def _parse_input(
    filename: str,
) -> typing.Tuple[typing.List[int], typing.List[numpy.ndarray]]:
    """Parse text input into game turns and boards.

    Returns:
        List of drawn numbers.
        List of all playing boards.
    """
    with open(f"inputs/{filename}") as file:
        text_input = file.read()
    split = text_input.split("\n\n")
    return list(map(int, split[0].split(","))), _get_boards(split[1:])


def _get_boards(boards: typing.List[str]) -> typing.List[numpy.ndarray]:
    return [
        numpy.array(
            [
                [Point(number=int(number)) for number in line.split()]
                for line in board.split("\n")
            ]
        )
        for board in boards
    ]


def _check_rows(board: numpy.ndarray) -> bool:
    """Check if there's any winning row in a board."""
    return any(all(point.marked for point in line) for line in board)


def _check_win(board: numpy.ndarray) -> bool:
    """Check if the board has already won."""
    return _check_rows(board) or _check_rows(board.transpose())


def _sum_unmarked(board: numpy.ndarray) -> int:
    """Get the sum of all unmarked numbers in a board."""
    return sum(point.number for line in board for point in line if not point.marked)


def _mark_point(turn: int, point: Point) -> Point:
    """Compare turn with point and mark if equal."""
    if turn == point.number:
        point.marked = True
    return point


def _play_turn(
    turn: int, boards: typing.List[numpy.ndarray]
) -> typing.List[numpy.ndarray]:
    """Mark points in all boards for current turn."""
    return numpy.vectorize(_mark_point)(turn, boards)


def _get_score(turn: int, board: numpy.ndarray) -> typing.Optional[int]:
    return turn * _sum_unmarked(board)


def _pop_winning(boards: typing.List[numpy.ndarray]) -> tuple:
    winning: typing.List[numpy.ndarray] = []
    not_winning: typing.List[numpy.ndarray] = []
    for board in boards:
        (not_winning, winning)[_check_win(board)].append(board)
    return winning, not_winning


def play_bingo(filename: str) -> tuple:
    """Play the game.

    Returns: Score of the first and last winning board.

    """
    turns, boards = _parse_input(filename)
    scores = []
    while turn := turns.pop(0) if turns else False and boards:
        _play_turn(turn, boards)
        winning, boards = _pop_winning(boards)
        if winning:
            scores += [_get_score(turn, board) for board in winning]
    return scores[0], scores[-1]


print(play_bingo("04.txt"))
