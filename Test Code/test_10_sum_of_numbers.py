import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("sum_digits", "Code/10_sum_of_digits.py").load_module()

assert program.sum_digits(1234) == 10

assert program.sum_digits(10) == 1

print("Test 10 passed")