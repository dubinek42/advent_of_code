from advent21.day08 import count_easy_codes, decode_all


def test_count_easy_codes():
    assert 26 == count_easy_codes("08_test.txt")


def test_decode_all():
    assert 61229 == decode_all("08_test.txt")
