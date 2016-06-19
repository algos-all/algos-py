import copy, random, operator

from nose.tools import raises

from heap import Heap

class TestHeap:
    def test_len_0(self):
        h = Heap()

        assert len(h) == 0

    def test_len_1(self):
        h = Heap([42])

        assert len(h) == 1

    @raises(IndexError)
    def test_getitem_0(self):
        Heap()[0]

    def test_getitem_1(self):
        h = Heap([42])

        assert h
        assert h[0] == 42
        assert h[:] == [42]
        assert h[:42] == [42]

    def test_setitem_0(self):
        h = Heap([42])

        h[0] = 43

        assert h
        assert h[0] == 43

    def test_push_0(self):
        h = Heap()

        h.push(42)

        assert h
        assert h[0] == 42

    def test_push_1(self):
        h = Heap()

        h.push(42)
        h.push(43)

        assert h
        assert h[0] == 42
        assert h[1] == 43

    def test_push_2(self, N=10):
        h = Heap()

        for i in range(N):
            h.push(i)

        assert h
        for i in range(N):
            assert h[i] == i

    @raises(IndexError)
    def test_pop_0(self):
        Heap().pop()

    def test_pop_1(self):
        h = Heap()

        h.push(42)

        t = h.pop()

        assert t == 42
        assert not h

    def test_pop_2(self, N=10):
        h = Heap()

        for i in range(N):
            h.push(i)

        assert len(h) == N
        for i in range(N):
            assert i == h.pop()
        assert not h

    def test_pop_3(self, N=10):
        h = Heap()

        for i in range(N):
            h.push(i)

        assert len(h) == N
        for i in reversed(range(N)):
            assert i == N - 1 - h.pop()
        assert not h

    def test_heap_0(self, N=1000, fst=-1024, lst=1024):
        data = [random.randint(fst, lst) for i in range(N)]
        orig = data.copy()

        h = Heap(data)

        assert len(h) == N
        for i in range(len(h)):
            if 2 * i + 1 < len(h):
                assert h[i] <= h[2 * i + 1]
            if 2 * i + 2 < len(h):
                assert h[i] <= h[2 * i + 2]
        assert data == orig

    def test_heap_sort_0(self, N=1000, fst=-1024, lst=1024):
        xs = [random.randint(fst, lst) for i in range(N)]

        ys = xs.copy()

        h = Heap(xs)

        zs = h.sort()

        assert zs == sorted(xs, reverse=True)
        assert xs == ys

    def test_heap_sort_1(self, N=1000, fst=-1024, lst=1024):
        xs = [random.randint(fst, lst) for i in range(N)]

        ys = xs.copy()

        h = Heap(xs, key=operator.ge)
        zs = h.sort()

        assert zs == sorted(xs)
        assert xs == ys
