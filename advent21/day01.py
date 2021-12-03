test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open("inputs/01.txt") as file:
    lines = file.readlines()
    puzzle_input = [int(line.rstrip()) for line in lines]


def increases(numbers):
    return len([i for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]])


def windows(numbers):
    return [sum(numbers[i:i+3]) for i in range(0, len(numbers)-2)]


print(increases(puzzle_input))
print(increases(windows(puzzle_input)))
