from char_frequency import count_char_frequency


def test_normal_string():
    assert count_char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_empty_string():
    assert count_char_frequency("") == {}


def test_repeated_characters():
    assert count_char_frequency("aaa") == {"a": 3}


def test_case_sensitive():
    assert count_char_frequency("AaA") == {
        "A": 2,
        "a": 1
    }


def test_spaces():
    assert count_char_frequency("a a") == {
        "a": 2,
        " ": 1
    }