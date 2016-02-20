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

    def test_half_by_half(self, N=100):
        xs = range(N)
        ys = [0 for i in range(N // 2)] + [1 for i in range(N // 2, N)]

        for UF in self.UFS:
            yield self.check_xs_ys, UF, xs, ys
