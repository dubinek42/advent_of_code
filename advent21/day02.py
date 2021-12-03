test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

with open("inputs/02.txt") as file:
    lines = file.readlines()
    puzzle_input = [line.rstrip() for line in lines]


def parse_instructions(commands):
    return [command.split(" ") for command in commands]


def run_submarine(instructions):
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


def run_submarine2(instructions):
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


print(run_submarine(parse_instructions(puzzle_input)))
print(run_submarine2(parse_instructions(puzzle_input)))
