from Code.largest_of_three import find_largest


def test_largest_first():
    assert find_largest(7, 2, 9) == 9


def test_largest_second():
    assert find_largest(2, 10, 5) == 10


def test_largest_third():
    assert find_largest(1, 4, 3) == 4


def test_all_equal():
    assert find_largest(5, 5, 5) == 5


def test_negative_numbers():
    assert find_largest(-11, -15, -9) == -9