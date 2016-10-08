import random

from bst import BinarySearchTree as bst


class CheckTree:
    def check_tree(self, bst, k2v):
        for key in k2v:
            if bst.get(key) != k2v[key]:
                return False

        return True

    def check_put_get(self, bst, N=10, lo=-1024, hi=1024, seed=0):
        assert N > 0 and lo <= hi

        random.seed(0)
        k2v = {}

        for i in range(N):
            key, val = random.randint(lo, hi), random.randint(lo, hi)

            k2v[key] = val

            bst.put(key, val)

            assert self.check_tree(bst, k2v)

    def check_contains(self, bst, N=10, lo=-1024, hi=1024, seed=0):
        assert N > 0 and lo <= hi

        random.seed(0)
        k2v = {}

        for i in range(N):
            key, val = random.randint(lo, hi), random.randint(lo, hi)

            k2v[key] = val

            bst.put(key, val)

        for key in k2v:
            assert key in bst

    def check_setitem_getitem(
            self, bst, N=10, lo=-1024, hi=1024, seed=0
    ):
        random.seed(0)

        k2v = {}

        for i in range(N):
            key, val = random.randint(lo, hi), random.randint(lo, hi)

            k2v[key], bst[key] = val, val

            for key in k2v:
                assert bst[key] == k2v[key]

    def check_remove(self, bst, N=10, lo=-1024, hi=1024, seed=0):
        random.seed(0)

        k2v = {}

        for i in range(N):
            key, val = random.randint(lo, hi), random.randint(lo, hi)

            k2v[key] = val
            bst.put(key, val)

        for key in list(k2v.keys()):
            bst.remove(key)
            k2v.pop(key)

            assert self.check_tree(bst, k2v)

        bst.remove(42)
        assert bst.root is None


class TestBinarySearchTree(CheckTree):
    def test_put_get(self, ns=range(1, 101)):
        for n in ns:
            yield self.check_put_get, bst(), n

    def test_check_contains(self, ns=range(1, 101)):
        for n in ns:
            yield self.check_contains, bst(), n

    def test_setitem_getitem(self, ns=range(1, 101)):
        for n in ns:
            yield self.check_setitem_getitem, bst(), n

    def test_remove(self, ns=range(1, 101)):
        for n in ns:
            yield self.check_remove, bst(), n
