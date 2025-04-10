import numpy as np
import pytest

def addition(a, b):
    return np.sum(a + b)

if __name__ =='__main__':
    print(addition(2, 3))