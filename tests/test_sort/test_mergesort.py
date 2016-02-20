from sort.mergesort import mergesort0, mergesort1, mergesort2

from check_sort import CheckSort


class TestMergeSort(CheckSort):
    def __init__(self):
        self.sorts = [mergesort0, mergesort1, mergesort2]

    def test_empty(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 0

    def test_single_0(self):
        for sort in self.sorts:
            yield self.check_on_sorted, sort, 1

    def test_single_1(self):
        for sort in self.sorts:
            yield self.check_on_random, sort, 1

    def test_sorted_0(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.check_on_sorted, sort, n

    def test_sorted_1(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.check_on_sorted, sort, n, True

    def test_random_0(self, ns=range(100)):
        for sort in self.sorts:
            for n in ns:
                yield self.check_on_random, sort, n

    def test_random_1(self):
        for sort in self.sorts:
            yield self.check_on_random, sort, 1024, -1024, 1024

    def test_random_2(self):
        for sort in self.sorts:
            yield self.check_on_random, sort, 1337, -1024, 1024
