import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

 is_prime = module.is_prime

def test_two():
    assert is_prime(2) == True

def test_one():
    assert is_prime(1) == False

def test_three():
    assert is_prime(3) == True

def test_four():
    assert is_prime(4) == False

def test_zero():
    assert is_prime(0) == False