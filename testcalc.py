# Simple Calculator App
# This script provides basic arithmetic operations: addition, subtraction, multiplication, and division.
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(8, 2) == 4
    assert divide(10, 5) == 2
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)