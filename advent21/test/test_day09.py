from advent21.day09 import _parse_input, calculate_basins, calculate_minima


def test_minima_and_basins():
    area = _parse_input("09_test.txt")
    assert 15 == calculate_minima(area)
    assert 1134 == calculate_basins(area)
