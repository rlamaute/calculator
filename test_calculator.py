from calculator import multiply
from calculator import divide

def test_numbers_2_4():
    assert multiply(2,4) == 8
def test_numbers_4_2():
    assert divide(4,2) == 2

def test_numbers_0():
    assert multiply(0, 2) == 0

def test_numbers_3_7():
    assert divide(3,7) == 1

def test_decimals():
    assert (0.5, 0.2) == "error"
