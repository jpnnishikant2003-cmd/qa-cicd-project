import pytest
from app.calculator import add,subtract,multiply,divide

def test_add():
    result =add(2,3)
    assert result == 5

def test_subtract():
    result =subtract(5,2)
    assert result == 3

def test_multiply():
    result =multiply(4, 3)
    assert result == 12

def test_divide():
    result =divide(10,2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)
