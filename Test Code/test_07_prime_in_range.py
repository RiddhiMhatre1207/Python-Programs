import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/07_prime_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_prime = module.is_prime


def test_prime():
    assert is_prime(2) == True


def test_not_prime():
    assert is_prime(4) == False


def test_primes_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]


def test_no_primes():
    assert primes_in_range(8, 10) == []