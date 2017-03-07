import operator

from itertools import product

from tests.test_sort.check_sort import CheckSort
from sort.quicksort import qsort0, qsort1, qsort2, qsort3


class TestQuickSort(CheckSort):
    def __init__(self):
        self.revs = [False, True]

        self.sorts = [qsort0, qsort1, qsort2, qsort3]

    def test_empty(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 0

    def test_single_0(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 1

    def test_sorted_0(self, ns=range(10)):
        for sort, n in product(self.sorts, ns):
            yield self.check_on_sorted, sort, n

    def test_sorted_1(self, ns=[2]):
        for sort, n in product(self.sorts, ns):
            yield self.check_on_sorted, sort, n, True

    def test_random(self, ns=range(100), ss=range(10)):
        for sort, rev, n, s in product(self.sorts, self.revs, ns, ss):
            yield self.check_on_random, sort, lambda x: x, rev, n, s

    def test_random_big(self, ns=[10000, 10001, 10002], ss=range(10)):
        for sort, rev, n, s in product(self.sorts, self.revs, ns, ss):
            yield self.check_on_random, sort, lambda x: x, rev, n, s
