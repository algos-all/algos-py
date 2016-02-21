import random, collections

from wgraph import WeightedGraph
from mst import LazyPrimMST, EagerPrimMST, KruskalMST


class CheckMST:
    def check_empty(self, mst):
        g = WeightedGraph()

        g = mst(g)

        assert g.edges == {}

    def check_chain(self, mst, N=10, seed=0):
        assert N > 0

        random.seed(seed)

        g = WeightedGraph()
        for i in range(N):
            g.add_edge(i, i + 1, random.random())

        h = mst(g)

        for n1 in h.edges:
            for n2, w in h.edges[n1]:
                assert [n2, w] in g.edges[n1]

    def check_complete3(self, mst):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(0, 2, 2)

        h = mst(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert h.edges[2] == [[1, 1]]

    def check_complete4_0(self, mst):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 0, 3)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 3, 5)

        h = mst(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert len(h.edges[2]) == 2
        assert [1, 1] in h.edges[2] and [3, 2] in h.edges[2]

        assert h.edges[3] == [[2, 2]]

    def check_complete4_1(self, mst):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 0, 3)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 3)

        h = mst(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert len(h.edges[2]) == 2
        assert [1, 1] in h.edges[2] and [3, 2] in h.edges[2]

        assert h.edges[3] == [[2, 2]]

    def check_controlled_traversal_0(self, mst):
        g = WeightedGraph()

        g.edges = collections.OrderedDict()

        g.add_edge("a", "b", 1)
        g.add_edge("a", "c", 2)

        h = mst(g)

        assert len(h.edges["a"]) == 2
        assert ["b", 1] in h.edges["a"]
        assert ["c", 2] in h.edges["a"]

        assert len(h.edges["b"]) == 1
        assert h.edges["b"] == [["a", 1]]

        assert len(h.edges["c"]) == 1
        assert h.edges["c"] == [["a", 2]]

    def check_controlled_traversal_1(self, mst):
        g = WeightedGraph()

        g.edges = collections.OrderedDict()

        g.add_edge("a", "b", 1)
        g.add_edge("a", "c", 2)
        g.add_edge("a", "d", 3)
        g.add_edge("a", "e", 4)

        h = mst(g)

        assert len(h.edges["a"]) == 4
        for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
            assert [n, w] in h.edges["a"]

        for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
            assert h.edges[n] == [["a", w]]


class TestPrimMST(CheckMST):
    def __init__(self):
        self.msts = [LazyPrimMST, EagerPrimMST]

    def test_empty(self):
        for mst in self.msts:
            yield self.check_empty, mst

    def test_chain(self, ns=range(1, 10)):
        for mst in self.msts:
            for n in ns:
                yield self.check_chain, mst, n

    def test_complete3(self):
        for mst in self.msts:
            yield self.check_complete3, mst

    def test_complete4_0(self):
        for mst in self.msts:
            yield self.check_complete4_0, mst

    def test_complete4_1(self):
        for mst in self.msts:
            yield self.check_complete4_1, mst

    def test_controlled_traversal_0(self):
        for mst in self.msts:
            yield self.check_controlled_traversal_0, mst

    def test_controlled_traversal_1(self):
        for mst in self.msts:
            yield self.check_controlled_traversal_1, mst


class TestKruskalMST(CheckMST):
    def test_empty(self):
        yield self.check_empty, KruskalMST

    def test_chain(self, ns=range(1, 10)):
        for n in ns:
            yield self.check_chain, KruskalMST, n

    def test_complete3(self):
        yield self.check_complete3, KruskalMST

    def test_complete4_0(self):
        yield self.check_complete4_0, KruskalMST

    def test_complete4_1(self):
        yield self.check_complete4_1, KruskalMST

    def test_controlled_traversal_0(self):
        yield self.check_controlled_traversal_0, KruskalMST

    def test_controlled_traversal_1(self):
        yield self.check_controlled_traversal_1, KruskalMST
