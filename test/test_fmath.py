import pytest

from math import factorial

from src.fmath import fcomb, next_permutation


@pytest.mark.parametrize("n", list(range(100)))
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


def test_next_permutation_empty():
    xs = []
    next_permutation(xs)
    assert xs == []


def test_next_permutation_one_element():
    xs = [1]
    next_permutation(xs)
    assert xs == [1]


def test_next_permutation_two_elements_one():
    xs = [1, 2]
    next_permutation(xs)
    assert xs == [2, 1]


def test_next_permutation_two_elements_two():
    xs = [2, 1]
    next_permutation(xs)
    assert xs == [1, 2]


def test_next_permutation_duplicates():
    xs = [1, 2, 2]
    next_permutation(xs)
    assert xs == [2, 1, 2]
