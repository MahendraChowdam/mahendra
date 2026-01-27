import pytest
import calculator

def test_mul(numbers, resource):
    a, b = numbers
    assert calculator.mul(a, b) == 50

def test_div(numbers):
    a, b = numbers
    assert calculator.div(a, b) == 2

def test_div_by_zero():
    with pytest.raises(ValueError):
        calculator.div(10, 0)
