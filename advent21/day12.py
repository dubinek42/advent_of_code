from typing import Callable


def _parse_input(filename: str) -> list[tuple[str, ...]]:
    with open(f"advent21/inputs/{filename}", encoding="utf-8") as file:
        text_input = file.readlines()
    return [tuple(line.rstrip().split("-")) for line in text_input]


def _compose_graph(edges: list[tuple[str, ...]]) -> dict:
    graph: dict[str, set] = {}
    for x, y in edges:
        if x in graph:
            graph[x].add(y)
        else:
            graph[x] = {y}
        if y in graph:
            graph[y].add(x)
        else:
            graph[y] = {x}
    return graph


def _my_condition(node: str, path: list[str]) -> bool:
    return node not in ("start", "end") and not any(
        path.count(p) > 1 and not p.isupper() for p in path
    )


def _find_all_paths(
    graph: dict,
    start: str,
    end: str,
    current_path: list,
    additional_condition: Callable,
) -> list:
    current_path = current_path + [start]
    if start == end:
        return [current_path]
    paths = []
    for node in graph[start]:
        if (
            node not in current_path
            or node.isupper()
            or additional_condition(node, current_path)
        ):
            paths += _find_all_paths(
                graph, node, end, current_path, additional_condition
            )
    return paths


def count_paths(filename: str) -> tuple[int, int]:
    graph = _compose_graph(_parse_input(filename))
    paths1 = _find_all_paths(graph, "start", "end", [], lambda *_: False)
    paths2 = _find_all_paths(graph, "start", "end", [], _my_condition)
    return len(paths1), len(paths2)


print(count_paths("day12.txt"))
