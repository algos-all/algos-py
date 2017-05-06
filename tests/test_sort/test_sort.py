import pytest, copy, random, operator

from src.sort.countsort import countsort
from src.sort.heapsort import heapsort
from src.sort.insertsort import (
    insertsort0, insertsort1, insertsort2
)
from src.sort.mergesort import (
    mergesort0, mergesort1, mergesort2
)
from src.sort.quicksort import (
    qsort0, qsort1, qsort2, qsort3
)
from src.sort.selectsort import (
    selectsort0, selectsort1
)
from src.sort.shellsort import shellsort


def issorted(xs, reverse=False):
    cmp = operator.ge if reverse else operator.le

    for i in range(1, len(xs)):
        if not cmp(xs[i - 1], xs[i]):
            return False

    return True

@pytest.mark.parametrize("sort", [
    countsort,
    heapsort,
    insertsort0, insertsort1, insertsort2,
    mergesort0, mergesort1, mergesort2,
    qsort0, qsort1, qsort2, qsort3,
    selectsort0, selectsort1,
    shellsort
])
@pytest.mark.parametrize("N", [i for i in range(10)])
@pytest.mark.parametrize("reverse", [False, True])
def test_on_sorted(sort, N, reverse):
    assert N >= 0

    xs = list(reversed(range(N))) if reverse else list(range(N))
    ys = copy.copy(xs)

    zs = sort(xs)

    if zs is None or zs is xs:
        # assume an in-place sort
        assert xs == list(range(N))
    else:
        # assume a not-in-place sort
        assert xs == ys
        assert zs == list(range(N))

@pytest.mark.parametrize("sort", [
        countsort,
    heapsort,
    insertsort0, insertsort1, insertsort2,
    mergesort0, mergesort1, mergesort2,
    qsort0, qsort1, qsort2, qsort3,
    selectsort0, selectsort1,
    shellsort
])
@pytest.mark.parametrize(
    "N", [i for i in range(10)] + [999, 1000, 1001]
)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("seed", list(range(10)))
def test_on_random(
    sort, N, reverse, seed,
    key=lambda x: x, lo=-1024, hi=1024
):
    assert N >= 0 and lo <= hi

    random.seed(seed)

    xs = [random.randint(lo, hi) for i in range(N)]
    ys = copy.copy(xs)

    zs = sort(xs, key, reverse)

    if zs is None or zs is xs:
        # assume an in-place sort
        assert issorted(xs, reverse)
    else:
        # assume a not-in-place sort
        assert xs == ys
        assert issorted(zs, reverse)
