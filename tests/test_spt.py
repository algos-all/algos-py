import math, random

from nose.tools import raises

from spt import LazyDijkstra
from wgraph import WeightedDiGraph


class CheckShortestPath:
    def is_shortest(self, spt, wdgraph):
        for n1 in wdgraph.edges:
            if spt.costs[n1] is None: continue

            for n2, w in wdgraph.edges[n1]:
                if spt.costs[n2] > spt.costs[n1] + w:
                    return False

        return True

    @raises(RuntimeError)
    def check_empty(self, spt):
        spt(WeightedDiGraph())

    def check_chain(self, spt, N=10):
        assert N > 0

        g = WeightedDiGraph()

        for i in range(N):
            g.add_edge(i, i + 1, 1)

        h = spt(g, 0)

        for i in range(N):
            assert h.edges[i] == [[i + 1, 1]], h.edges
            assert h.costs[i] == i * 1

    def check_random(self, spt, V=10, E=10, seed=0):
        assert V > 1 and E > 0
        random.seed(seed)

        g = WeightedDiGraph()

        for i in range(E):
            n1, n2 = random.sample(range(V), 2)
            g.add_edge(n1, n2, random.random())

        h = spt(g, n1)

        assert self.is_shortest(h, g)


class TestShortestPath(CheckShortestPath):
    def test_empty(self):
        yield self.check_empty, LazyDijkstra

    def test_chain(self, ns=range(1, 10)):
        for n in ns:
            yield self.check_chain, LazyDijkstra, n

    def test_random_0(self, ns=range(2, 8)):
        for n in ns:
            yield self.check_random, LazyDijkstra, n, math.factorial(n)

    def test_random_1(self, ns=range(2, 100)):
        for n in ns:
            yield self.check_random, LazyDijkstra, n, n
