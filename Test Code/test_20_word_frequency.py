import re
from collections import Counter


def word_frequency(sentence):
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    return dict(Counter(words))

sentence = "Hello world! Hello Python."
print(word_frequency(sentence))

{'hello': 2, 'world': 1, 'python': 1}

from word_frequency import word_frequency


def test_repeated_words():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_case_insensitive():
    assert word_frequency("Python python PYTHON") == {
        "python": 3
    }


def test_empty_sentence():
    assert word_frequency("") == {}


def test_single_word():
    assert word_frequency("hello") == {
        "hello": 1
    }


def test_punctuation():
    assert word_frequency("Hi, hi! Hello.") == {
        "hi": 2,
        "hello": 1
    }


def test_different_words():
    assert word_frequency("cat dog bird") == {
        "cat": 1,
        "dog": 1,
        "bird": 1
    }
