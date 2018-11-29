import copy, random, pytest

from itertools import product

from src.dsu import DisjointSetUnion as DSU

def test_empty_find():
    with pytest.raises(KeyError):
        DSU().find(0)

def test_empty_union():
    with pytest.raises(KeyError):
        DSU().union(0, 0)

@pytest.mark.parametrize("n", list(range(10)))
def test_iter(n):
    xs = range(n)

    dsu = DSU(xs)

    for x in xs:
        assert dsu[x] == x

@pytest.mark.parametrize("n", list(range(10)))
def test_getitem(n):
    xs = range(n)

    dsu = DSU(xs)

    for i in range(1, len(xs) // 2):
        dsu.union(xs[i - 1], xs[i])

    for i in range(1, len(xs) // 2):
        assert dsu[i - 1] == dsu[i]

    for i in range(len(xs) // 2, len(xs)):
        assert dsu[i] == xs[i]

def test_setitem_0():
    dsu = DSU()

    with pytest.raises(RuntimeError):
        dsu[42] = 43

@pytest.mark.parametrize("n", list(range(10)))
def test_setitem_1(n):
    xs = range(n)

    dsu = DSU()

    for x in xs:
        dsu[x] = x

    for x in dsu:
        assert dsu[x] is x

def check_xs_ys(xs, ys):
    assert len(xs) == len(ys)

    for y in ys:
        assert y in xs

    dsu = DSU(xs)

    for x, y in zip(xs, ys):
        dsu.union(x, y)

    for x, y in zip(xs, ys):
        assert dsu.find(x) == dsu.find(y)

    for x, y in zip(xs, ys):
        assert dsu.find(x) == dsu[y]

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(10)))
def test_all_the_same(n, seed, lo=-1024, hi=1024):
    assert n > 0

    random.seed(seed)

    xs = [random.randint(lo, hi) for i in range(n)]
    ys = copy.copy(xs)

    check_xs_ys(xs, ys)

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(10)))
def test_random(n, seed):
    assert n > 0

    random.seed(seed)

    xs = list(range(n))
    ys = [random.randrange(0, n) for i in range(n)]

    check_xs_ys(xs, ys)

@pytest.mark.parametrize("n", list(range(2, 10)))
def test_transitive_union(n):
    assert n > 1

    xs = list(range(n))
    ys = [
        xs[0] for i in xs[: n // 2]
    ] + [
        xs[n // 2] for i in xs[n // 2 :]
    ]

    dsu = DSU(xs)

    for x, y in zip(xs, ys):
        dsu.union(x, y)

    dsu.union(xs[n // 2 - 1], xs[-1])

    for i, j in product(range(n), range(n)):
        assert dsu.find(i) == dsu.find(j)
