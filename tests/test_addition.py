from src.addition import addition
import pytest

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-8, 3) == -5