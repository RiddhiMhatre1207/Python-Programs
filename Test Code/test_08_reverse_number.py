import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_number",
    "Code/08_reverse_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_number= module.reverse_number

def test_reverse_number():
    assert reverse_number(12345) == 54321

def test_reverse_small_number():
    assert reverse_number(123) == 321  

def test_reverse_single_digit():
    assert reverse_number(1) == 1

def test_reverse_zero():
    assert reverse_number(0) == 0

def test_reverse_negative():
    assert reverse_number(-12345) == -54321