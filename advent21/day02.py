test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def _parse_input(filename: str) -> list[list[str]]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        lines = file.readlines()
    return [list(command.split(" ")) for command in [line.rstrip() for line in lines]]


def run_submarine(instructions: list[list[str]]) -> int:
    horizontal = 0
    depth = 0

    for ins in instructions:
        if ins[0] == "forward":
            horizontal += int(ins[1])
        elif ins[0] == "down":
            depth += int(ins[1])
        elif ins[0] == "up":
            depth -= int(ins[1])

    return horizontal * depth


def run_submarine2(instructions: list[list[str]]) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for ins in instructions:
        if ins[0] == "down":
            aim += int(ins[1])
        elif ins[0] == "up":
            aim -= int(ins[1])
        elif ins[0] == "forward":
            horizontal += int(ins[1])
            depth += aim * int(ins[1])

    return horizontal * depth


def run(filename: str) -> tuple[int, int]:
    instructions = _parse_input(filename)
    return run_submarine(instructions), run_submarine2(instructions)


print(run("02.txt"))
