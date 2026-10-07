import importlib.util

spec = importlib.util.spec_from_file_location(
    "factorial",
    "Code/04_factorial.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

calculate_factorial = module.calculate_factorial

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_one():
    assert calculate_factorial(1) == 1

def test_factorial_two():
    assert calculate_factorial(2) == 2

def test_factorial_negative():
    assert calculate_factorial(-2) is None

def test_factorial_large():
    assert calculate_factorial(5) == 120

if __name__ == "__main__":
    test_factorial_zero()
    test_factorial_one()
    test_factorial_two()
    test_factorial_negative()
    test_factorial_large()
    print("All test cases passed.")