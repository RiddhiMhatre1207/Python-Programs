import importlib

module = importlib.import_module('Code.05_fibonacci_series')
fibonacci_series = module.fibonacci_series

def test_fibonacci_series():
    assert fibonacci_series(1) == [0]

def test_fibonacci_series():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]

def test_fibonacci_series():
    assert fibonacci_series(0) == []