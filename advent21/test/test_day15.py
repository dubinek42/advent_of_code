import pytest
from advent21.day15 import find_path, find_path_bigger


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("15_test.txt", 40),
        ("15.txt", 435),
    ],
)
def test_find_path(filename, expected):
    assert expected == find_path(filename)


@pytest.mark.parametrize(
    "filename, k, expected",
    [
        ("15_test.txt", 5, 315),
        ("15.txt", 5, 2842),
    ],
)
def test_find_path_bigger(filename, k, expected):
    assert expected == find_path_bigger(filename, k)
