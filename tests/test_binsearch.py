import random

from binsearch import binsearch0, binsearch1


class CheckBinsearch:
    def check_empty(self, b):
        assert b([], 42) is None

    def check_single_0(self, b):
        assert b([0], 1) is None

    def check_single_1(self, b):
        assert b([0], 0) == 0

    def check_random_present(self, b, N=10, lo=-1024, hi=1024):
        assert N > 0 and lo <= hi

        random.seed(0)

        xs = sorted([random.randint(lo, hi) for i in range(N)])

        i = random.randrange(0, N)

        j = b(xs, xs[i])

        assert j is not None
        assert xs[i] == xs[j]

    def check_random_missing_internal(
            self, b, N=10, lo=-1024, hi=1024
    ):
        assert N > 0 and lo <= hi and N < hi - lo

        random.seed(0)

        xs = sorted([random.randint(lo, hi) for i in range(N)])

        x = random.randint(lo, hi)
        while x in xs: x = random.randint(lo, hi)

        assert b(xs, x) is None

    def check_random_missing_external(
        self, b, N=10, left=True, lo=-1024, hi=1024
    ):
        assert N > 0 and lo <= hi

        random.seed(0)

        xs = sorted([random.randint(lo, hi) for i in range(N)])

        x = lo - 1 if left else hi + 1

        assert b(xs, x) is None


class TestBinsearch(CheckBinsearch):
    def __init__(self):
        self.bs = [binsearch0, binsearch1]

    def test_empty(self):
        for b in self.bs: yield self.check_empty, b

    def test_single_0(self):
        for b in self.bs: yield self.check_single_0, b

    def test_single_1(self):
        for b in self.bs: yield self.check_single_1, b

    def test_random_present(self, ns=range(1, 100)):
        for b in self.bs:
            for n in ns:
                yield self.check_random_present, b, n

    def test_random_missing_internal(self, ns=range(1, 100)):
        for b in self.bs:
            for n in ns:
                yield self.check_random_missing_internal, b, n

    def test_random_missing_external_0(self, ns=range(1, 100)):
        for b in self.bs:
            for n in ns:
                yield self.check_random_missing_external, b, n

    def test_random_missing_external_1(self, ns=range(1, 100)):
        for b in self.bs:
            for n in ns:
                yield self.check_random_missing_external, b, n, False
