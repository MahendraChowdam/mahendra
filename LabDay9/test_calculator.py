import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.sub(5, 3) == 2

def test_mul():
    assert calculator.mul(4, 3) == 12

def test_div():
    assert calculator.div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        calculator.div(10, 0)
