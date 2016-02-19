from sort.heapsort import heapsort

from check_sort import CheckSort


class TestHeapsort:
    def __init__(self):
        self.onsorted = CheckSort.onsorted_ip
        self.onrandom = CheckSort.onrandom_ip

    def test_empty(self):
        yield self.onsorted, heapsort, 0

    def test_single_0(self):
        yield self.onsorted, heapsort, 1

    def test_single_1(self):
        yield self.onrandom, heapsort, 1

    def test_sorted_0(self, ns=range(10)):
        for n in ns: yield self.onsorted, heapsort, n

    def test_sorted_1(self, ns=range(10)):
        for n in ns: yield self.onsorted, heapsort, n, True

    def test_random_0(self, ns=range(100)):
        for n in ns: yield self.onrandom, heapsort, n

    def test_random_1(self):
        yield self.onrandom, heapsort, 1024, -1024, 1024

    def test_random_2(self):
        yield self.onrandom, heapsort, 1337, -1024, 1024
