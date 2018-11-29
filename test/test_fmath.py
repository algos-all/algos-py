import pytest

from math import factorial

from src.fmath import fcomb

@pytest.mark.parametrize('n', list(range(100)))
def test_main(n):
    for i in range(n + 1):
        result = fcomb(n, i)
        correct = factorial(n) // factorial(i) // factorial(n - i)

        assert result == correct

def test_negatives():
    assert fcomb(-1, 1) == 0
    assert fcomb(1, -1) == 0
    assert fcomb(-1, -1) == 0

    assert fcomb(-42, 42) == 0
    assert fcomb(42, -42) == 0
    assert fcomb(-42, -42) == 0

def test_k_larger_than_n():
    assert fcomb(1, 2) == 0
