import importlib.util
spec = importlib.util.spec_from_file_location(
    "pos_neg_zero",
    "Code/03_pos_neg_zero.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_number = module.check_number

def test_positive():
    assert check_number(10) == "Positive"

def test_negative():
    assert check_number(-7) == "Negative"

def test_zero():
    assert check_number(0) == "Zero"

def test_small_positive():
    assert check_number(2) == "Positive"

def test_small_negative():
    assert check_number(-2) == "Negative"

if __name__ =="__main__":
    test_positive()
    test_negative()
    test_zero()
    test_small_positive()
    test_small_negative()
    print("All test cases passed.")