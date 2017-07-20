from calculator import multiply
from calculator import divide

def test_numbers_multiply_poz():
    assert multiply(2,4) == 8

def test_numbers_multiply_neg():
    assert multiply(-2,-4) == 8

def test_numbers_multiply_neg_poz():
    assert multiply(-2,4) == -8

def test_numbers_0():
    assert multiply(0, 2) == 0

def test_numbers_0():
    assert multiply(0, 2) == 0

def test_decimals():
    assert multiply (0.5, 0.2) == 0.1

def test_numbers_divide_poz():
    assert divide(4,2) == 2

def test_numbers_divide_negative():
    assert divide(-4, -2) == 2

def test_numbers_divide_neg_poz():
    assert divide(-4, 2) == -2

def test_numbers_3_7():
    assert divide(3,7) == 0.14

def test_divideby0():
    assert divide (2,0) == "error do not give me zero ever again"

