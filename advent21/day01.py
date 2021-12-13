def _parse_input(filename: str) -> list[int]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        lines = file.readlines()
    return [int(line.rstrip()) for line in lines]


def _increases(numbers: list[int]) -> int:
    return len([i for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]])


def _windows(numbers: list[int]) -> list[int]:
    return [sum(numbers[i : i + 3]) for i in range(0, len(numbers) - 2)]


def run(filename: str) -> tuple[int, int]:
    puzzle_input = _parse_input(filename)
    return _increases(puzzle_input), _increases(_windows(puzzle_input))


print(run("01.txt"))
