from sort.selectsort import selectsort0, selectsort1

from check_sort import CheckSort


class TestSelectSort:
    def __init__(self):
        self.sorts = [selectsort0, selectsort1]

        self.onsorted = CheckSort.onsorted_ip
        self.onrandom = CheckSort.onrandom_ip

    def test_empty(self):
        for sort in self.sorts: yield self.onsorted, sort, 0

    def test_single_0(self):
        for sort in self.sorts: yield self.onsorted, sort, 1

    def test_single_1(self):
        for sort in self.sorts: yield self.onrandom, sort, 1

    def test_sorted_0(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.onsorted, sort, n

    def test_sorted_1(self, ns=range(10)):
        for sort in self.sorts:
            for n in ns:
                yield self.onsorted, sort, n, True

    def test_random_0(self, ns=range(100)):
        for sort in self.sorts:
            for n in ns:
                yield self.onrandom, sort, n

    def test_random_1(self):
        for sort in self.sorts:
            yield self.onrandom, sort, 1024, -1024, 1024

    def test_random_2(self):
        for sort in self.sorts:
            yield self.onrandom, sort, 1337, -1024, 1024
