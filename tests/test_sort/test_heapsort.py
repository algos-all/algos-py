from sort.heapsort import heapsort

from check_sort import CheckSort


class TestHeapSort(CheckSort):
    def test_empty(self):
        yield self.check_on_sorted, heapsort, 0

    def test_single_0(self):
        yield self.check_on_sorted, heapsort, 1

    def test_single_1(self):
        yield self.check_on_random, heapsort, 1

    def test_sorted_0(self, ns=range(10)):
        for n in ns: yield self.check_on_sorted, heapsort, n

    def test_sorted_1(self, ns=range(10)):
        for n in ns: yield self.check_on_sorted, heapsort, n, True

    def test_random_0(self, ns=range(100)):
        for n in ns: yield self.check_on_random, heapsort, n

    def test_random_1(self):
        yield self.check_on_random, heapsort, 1024, -1024, 1024

    def test_random_2(self):
        yield self.check_on_random, heapsort, 1337, -1024, 1024
