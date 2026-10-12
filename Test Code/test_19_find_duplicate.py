from find_element import find_element


def test_element_present():
    assert find_element([10, 20, 30, 40], 30) == True


def test_element_absent():
    assert find_element([10, 20, 30, 40], 50) == False


def test_empty_list():
    assert find_element([], 10) == False


def test_first_element():
    assert find_element([10, 20, 30], 10) == True


def test_last_element():
    assert find_element([10, 20, 30], 30) == True


def test_single_element():
    assert find_element([5], 5) == True
