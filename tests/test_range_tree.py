import copy, random

from range_tree import RangeTree

class CheckRangeTree:
    def check_one_sum(self, seed=42, lo=-1024, hi=1024):
        random.seed(seed)

        x = random.randint(lo, hi)

        tree = RangeTree([x])

        assert tree.get(0, 1) == x

    def check_two_sum(self, seed=42, lo=-1024, hi=1024):
        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(2)]
        ys = copy.copy(xs)

        tree = RangeTree(xs)

        assert tree.get(0, 1) == ys[0]
        assert tree.get(1, 2) == ys[1]
        assert tree.get(0, 2) == sum(ys)

    def check_random_sum(self, seed=42, lo=-1024, hi=1024, n=10):
        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(2)]
        ys = copy.copy(xs)

        tree = RangeTree(xs)

        for i in range(len(xs)):
            for j in range(i + 1, len(xs) + 1):
                assert tree.get(i, j) == sum(ys[i : j])

    def check_random_max(self, seed=42, lo=-1024, hi=1024, n=10):
        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(2)]
        ys = copy.copy(xs)

        tree = RangeTree(
            xs, f=lambda x: x, g=lambda x, y: x if x > y else y
        )

        for i in range(len(xs)):
            for j in range(i + 1, len(xs) + 1):
                assert tree.get(i, j) == max(ys[i : j])


class TestRangeTree(CheckRangeTree):
    def test_one_sum(self, times=10):
        for time in range(times):
            yield self.check_one_sum, time

    def test_two_sum(self, times=10):
        for time in range(times):
            yield self.check_two_sum, time

    def test_random_sum(self, times=10, ns=range(100)):
        for n in ns:
            for time in range(times):
                yield self.check_random_sum, time, -1024, 1024, n

    def test_random_max(self, times=10, ns=range(100)):
        for n in ns:
            for time in range(times):
                yield self.check_random_max, time, -1024, 1024, n
