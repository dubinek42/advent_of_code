LE_HASH_MAP = {
    2: lambda *_: 1,
    3: lambda *_: 7,
    4: lambda *_: 4,
    5: lambda _, s, u, c: 3 if s < c else 2 if u < c else 5,
    6: lambda f, s, _, c: 9 if f < c else 0 if s < c else 6,
    7: lambda *_: 8,
}


def _parse_input(filename: str) -> list[tuple[list[str], list[set[str]]]]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.readlines()
    result = []
    for line in text_input:
        pattern, code = line.rstrip().split(" | ")
        result.append((pattern.split(" "), [set(c) for c in code.split(" ")]))
    return result


def _get_by_len(input_list: list, length: int) -> set:
    return set(
        next(
            iter(
                filter(lambda x: len(x) == length, input_list)  # type: ignore[arg-type]
            )
        )
    )


def _decode(patterns: list[str], codes: list[set]) -> int:
    four, seven, eight = map(_get_by_len, [patterns] * 3, [4, 3, 7])
    uniques = {c for c in eight if c not in four.union(seven)}
    digits = []
    for code in codes:
        digits.append(
            LE_HASH_MAP[len(code)](four, seven, uniques, code)  # type: ignore
        )
    return int("".join(str(d) for d in digits))


def count_easy_codes(filename: str) -> int:
    return sum(
        1
        for _, codes in _parse_input(filename)
        for code in codes
        if len(code) in (2, 3, 4, 7)
    )


def decode_all(filename: str) -> int:
    total = 0
    for line in _parse_input(filename):
        total += _decode(*line)
    return total


print(count_easy_codes("08.txt"))
print(decode_all("08.txt"))
