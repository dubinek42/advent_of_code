import numpy


def _parse_input(filename) -> tuple[list, list]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.read()
    d, f = text_input.split("\n\n")
    dots = [tuple(int(v) for v in line.split(",")) for line in d.split("\n")]
    folds = [tuple(line[11:].split("=")) for line in f.split("\n")]
    return dots, folds


def _compose_paper(dots: list[tuple]) -> numpy.ndarray:
    coords = tuple(zip(*dots))
    size = tuple(max(n) + 1 for n in coords)
    paper = numpy.zeros(size)
    paper[coords] = 1
    # Return transposed so that x - horizontal, y - vertical
    return paper.T


def _fold(paper: numpy.ndarray, axis: str, number: int) -> numpy.ndarray:
    if axis == "x":
        paper = paper.T
    first_part = paper[:number, :]
    second_part = paper[number + 1 :, :]
    flipped = numpy.flip(second_part, 0)
    first_part[-len(flipped) :, :] += flipped
    return first_part.T if axis == "x" else first_part


def _pretty_print(paper: numpy.ndarray) -> None:
    paper = numpy.vectorize(lambda x: "#" if x else " ")(paper)
    for line in paper:
        print("".join(line))


def fold_it_up(filename: str) -> tuple[int, int]:
    dots, folds = _parse_input(filename)
    paper = _compose_paper(dots)

    first_fold = folds.pop(0)
    paper = _fold(paper, first_fold[0], int(first_fold[1]))
    dot_count = numpy.count_nonzero(paper)

    for axis, number in folds:
        paper = _fold(paper, axis, int(number))
    _pretty_print(paper)

    return dot_count, numpy.count_nonzero(paper)


print(fold_it_up("13.txt"))
