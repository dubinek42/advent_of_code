import pytest
from advent21.day14 import polymerize


@pytest.mark.parametrize(
    "filename, steps, expected",
    [
        ("14_test.txt", 10, 1588),
        ("14_test.txt", 40, 2188189693529),
        ("14.txt", 10, 2851),
        ("14.txt", 40, 10002813279337),
    ],
)
def test_polymerize(filename, steps, expected):
    assert expected == polymerize(filename, steps)
