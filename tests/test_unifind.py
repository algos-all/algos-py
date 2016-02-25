import random
from nose.tools import raises

from unifind import QuickFind, QuickUnion


class CheckUnionFind:
    @raises(KeyError)
    def check_empty_find(self, UF):
        UF().find(0)

    @raises(KeyError)
    def check_empty_union(self, UF):
        UF().union(0, 0)

    def check_xs_ys(self, UF, xs=range(10), ys=range(10)):
        assert len(xs) == len(ys)
        for y in ys: assert y in xs

        uf = UF(xs)

        for x, y in zip(xs, ys):
            uf.union(x, y)

        for x, y in zip(xs, ys):
            assert uf.find(x) == uf.find(y)

    def check_random(self, UF, N=10, seed=0):
        assert N > 0

        random.seed(seed)

        xs = list(range(N))
        ys = [random.randrange(0, N) for i in range(N)]

        self.check_xs_ys(UF, xs, ys)

    def check_transitive_union(self, UF, N=10):
        assert N > 1

        xs = list(range(N))
        ys = [
            xs[0] for i in xs[: N // 2]
        ] + [
            xs[N // 2] for i in xs[N // 2 :]
        ]

        uf = UF(xs)

        for x, y in zip(xs, ys):
            uf.union(x, y)

        uf.union(xs[N // 2 - 1], xs[-1])

        for i in range(N):
            for j in range(N):
                assert uf.find(i) == uf.find(j)


class TestUnionFind(CheckUnionFind):
    def __init__(self):
        self.UFS = [QuickFind, QuickUnion]

    def test_empty_find(self):
        for UF in self.UFS:
            yield self.check_empty_find, UF

    def test_empty_union(self):
        for UF in self.UFS:
            yield self.check_empty_union, UF

    def test_all_distinct(self):
        for UF in self.UFS:
            yield self.check_xs_ys, UF

    def test_all_the_same(
            self, xs=range(10), ys=[0 for i in range(10)]
    ):
        for UF in self.UFS:
            yield self.check_xs_ys, UF, xs, ys

    def test_random(self, ns=range(1, 100)):
        for UF in self.UFS:
            for n in ns:
                yield self.check_random, UF, n

    def test_transitive_union(self, ns=range(2, 50)):
        for UF in self.UFS:
            for n in ns:
                yield self.check_transitive_union, UF, n
