import pytest
from advent21.day14 import polymerize


@pytest.mark.parametrize(
    "filename, steps, expected",
    [
        ("14_test.txt", 10, 1588),
        ("14_test.txt", 40, 2188189693529),
        ("14.txt", 10, 2851),
        ("14.txt", 40, 10002813279337),
        (
            "14.txt",
            500,
            41462946311064936094075217688662424071542349672924341947607409843836583855136601205192141928433492017773166336671246705012397965181183081010241673519774,  # noqa: line-too-long
        ),
    ],
)
def test_polymerize(filename, steps, expected):
    assert expected == polymerize(filename, steps)
