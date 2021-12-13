DAYS_TO_SPAWN = 6
DAYS_TO_SPAWN_BABY = DAYS_TO_SPAWN + 2


def _parse_input(filename: str) -> list[int]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.read()
    return [int(x) for x in text_input.split(",")]


def run_naive(start: list[int], days: int) -> int:
    def _decrease(number: int) -> int:
        return number - 1 if number > 0 else DAYS_TO_SPAWN

    fish = start
    spawn = 0
    for _ in range(days):
        fish = list(map(_decrease, fish)) + [DAYS_TO_SPAWN_BABY] * spawn
        spawn = fish.count(0)
    return len(fish)


def run_clever(start: list[int], days: int) -> int:
    fish_counts = [start.count(i) for i in range(DAYS_TO_SPAWN_BABY + 1)]
    final_count = len(start)
    for _ in range(days):
        fish = fish_counts.pop(0)
        final_count += fish
        fish_counts.append(fish)
        fish_counts[DAYS_TO_SPAWN] += fish
    return final_count


def run_both(filename: str) -> tuple[int, int]:
    fish = _parse_input(filename)
    return run_naive(fish, 80), run_clever(fish, 256)


print(run_both("06.txt"))
