import random, pytest

from src.binsearch import binsearch0, binsearch1


@pytest.mark.parametrize("b", [binsearch0, binsearch1])
def test_empty(b):
    assert b([], 42) is None

@pytest.mark.parametrize("b", [binsearch0, binsearch1])
def test_single_0(b):
    assert b([0], 1) is None

@pytest.mark.parametrize("b", [binsearch0, binsearch1])
def test_single_1(b):
    assert b([0], 0) == 0

@pytest.mark.parametrize("b", [binsearch0, binsearch1])
@pytest.mark.parametrize("n", list(range(1, 10)))
def test_random_present(b, n, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    xs = sorted([random.randint(lo, hi) for i in range(n)])

    i = random.randrange(0, n)

    j = b(xs, xs[i])

    assert j is not None
    assert xs[i] == xs[j]

@pytest.mark.parametrize("b", [binsearch0, binsearch1])
@pytest.mark.parametrize("n", list(range(1, 10)))
def test_random_missing_internal(b, n, lo=-1024, hi=1024):
    assert n > 0 and lo < hi and n < hi - lo

    random.seed(0)

    xs = sorted([random.randint(lo, hi) for i in range(n)])

    x = random.randint(lo, hi)
    while x in xs:
        x = random.randint(lo, hi)

    assert b(xs, x) is None

@pytest.mark.parametrize("b", [binsearch0, binsearch1])
@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("left", [True, False])
def test_random_missing_external(b, n, left, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    xs = sorted([random.randint(lo, hi) for i in range(n)])

    x = lo - 1 if left else hi + 1

    assert b(xs, x) is None
