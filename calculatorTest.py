import pytest
from calculator.py import is_even

def test_even():
    assert is_even(4) == True

def test_odd():
    assert is_even(3) == False
