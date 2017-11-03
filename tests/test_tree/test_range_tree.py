import copy, random, pytest

from src.tree.range_tree import RangeTreeFixed1D

@pytest.mark.parametrize("seed", list(range(100)))
def test_one_sum(seed, lo=-1024, hi=1024):
    random.seed(seed)

    x = random.randint(lo, hi)

    tree = RangeTreeFixed1D([x])

    assert tree.get(0, 1) == x

@pytest.mark.parametrize("seed", list(range(100)))
def test_two_sum(seed, lo=-1024, hi=1024):
    random.seed(seed)

    xs = [random.randint(lo, hi) for i in range(2)]
    ys = copy.copy(xs)

    tree = RangeTreeFixed1D(xs)

    assert tree.get(0, 1) == ys[0]
    assert tree.get(1, 2) == ys[1]
    assert tree.get(0, 2) == sum(ys)

@pytest.mark.parametrize("seed", list(range(100)))
@pytest.mark.parametrize("n", list(range(2, 10)))
def test_random_sum(seed, n, lo=-1024, hi=1024):
    assert n > 1

    random.seed(seed)

    xs = [random.randint(lo, hi) for i in range(n)]
    ys = copy.copy(xs)

    tree = RangeTreeFixed1D(xs)

    for i in range(len(xs)):
        for j in range(i + 1, len(xs) + 1):
            assert tree.get(i, j) == sum(ys[i : j])

@pytest.mark.parametrize("seed", list(range(100)))
@pytest.mark.parametrize("n", list(range(2, 10)))
def test_random_max(seed, n, lo=-1024, hi=1024):
    assert n > 1

    random.seed(seed)

    xs = [random.randint(lo, hi) for i in range(n)]
    ys = copy.copy(xs)

    tree = RangeTreeFixed1D(
        xs, f=lambda x: x, g=lambda x, y: x if x > y else y
    )

    for i in range(len(xs)):
        for j in range(i + 1, len(xs) + 1):
            assert tree.get(i, j) == max(ys[i : j])
