from itertools import product

from tests.test_sort.check_sort import CheckSort
from src.sort.selectsort import selectsort0, selectsort1


class TestSelectSort(CheckSort):
    def __init__(self):
        self.revs = [False, True]

        self.sorts = [selectsort0, selectsort1]

    def test_empty(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 0

    def test_single_0(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 1

    def test_sorted_0(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.check_on_sorted, sort, n

    def test_sorted_1(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.check_on_sorted, sort, n, True

    def test_random(self, ns=range(100), ss=range(10)):
        for sort, rev, n, s in product(self.sorts, self.revs, ns, ss):
            yield self.check_on_random, sort, lambda x: x, rev, n, s

    def test_random_big(self, ns=[1000, 1001, 1002], ss=range(10)):
        for sort, rev, n, s in product(self.sorts, self.revs, ns, ss):
            yield self.check_on_random, sort, lambda x: x, rev, n, s
