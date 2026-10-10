import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome= module.is_palindrome

def test_palindrome_number():
    assert is_palindrome(121) == True

def test_non_palindrome_number():
    assert is_palindrome(123) == False

def test_single_digit():
    assert is_palindrome(7) == True

def test_zero():
    assert is_palindrome(0) == True

def test_palindrome_even_digits():
    assert is_palindrome(1221) == True