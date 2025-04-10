import numpy as np
import pytest

def addition(a, b):
    return np.sum(a + b)

def test_addition():
    assert addition(2, 3) == 5
