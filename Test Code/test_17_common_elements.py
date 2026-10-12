from common import common_elements


def test_partial_match():
    assert set(common_elements([1, 2, 3], [2, 3, 4])) == {2, 3}


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_duplicate_elements():
    assert set(common_elements([5, 5, 6], [5, 7])) == {5}


def test_empty_list():
    assert common_elements([], [1, 2]) == []


def test_identical_lists():
    assert set(common_elements([1, 2, 3], [1, 2, 3])) == {1, 2, 3}
