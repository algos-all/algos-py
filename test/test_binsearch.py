import pytest
import random

from src.binsearch import binary_search0, binary_search1


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
def test_empty(binary_search):
    assert binary_search([], 42) is None


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
def test_single_0(binary_search):
    assert binary_search([0], 1) is None


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
def test_single_1(binary_search):
    assert binary_search([0], 0) == 0


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
@pytest.mark.parametrize("n", list(range(1, 10)))
def test_random_present(binary_search, n, lft=-1024, rgt=1024):
    assert n > 0 and lft < rgt

    random.seed(0)

    xs = sorted([random.randint(lft, rgt) for _ in range(n)])

    i = random.randrange(0, n)

    j = binary_search(xs, xs[i])

    assert j is not None
    assert xs[i] == xs[j]


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
@pytest.mark.parametrize("n", list(range(1, 10)))
def test_random_missing_internal(binary_search, n, lft=-1024, rgt=1024):
    assert 0 < n < rgt - lft and lft < rgt

    random.seed(0)

    xs = sorted([random.randint(lft, rgt) for _ in range(n)])

    x = random.randint(lft, rgt)
    while x in xs:
        x = random.randint(lft, rgt)

    assert binary_search(xs, x) is None


@pytest.mark.parametrize("binary_search", [binary_search0, binary_search1])
@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("left", [True, False])
def test_random_missing_external(binary_search, n, left, lft=-1024, rgt=1024):
    assert n > 0 and lft < rgt

    random.seed(0)

    xs = sorted([random.randint(lft, rgt) for _ in range(n)])

    x = lft - 1 if left else rgt + 1

    assert binary_search(xs, x) is None
