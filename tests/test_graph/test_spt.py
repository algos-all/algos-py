import math, random

from itertools import product
from nose.tools import raises

from graph.wgraph import WeightedDiGraph
from graph.spt import Dijkstra, BellmanFord


class CheckShortestPath:
    def is_shortest(self, spt, wdgraph):
        for n1 in wdgraph:
            # there may be several connected components
            if spt.costs[n1] is None: continue

            for n2, w in wdgraph[n1]:
                if spt.costs[n2] > spt.costs[n1] + w:
                    return False

        return True

    def is_negative_cycle(self, spt, wdgraph):
        def min_edge(n1, n2):
            ws = [w for n, w in wdgraph[n1] if n == n2]
            assert ws, "n1 and n2 are not actually connected"

            return min(ws)

        assert len(spt.cycle) > 0, spt.cycle

        total = 0
        for i in range(1, len(spt.cycle)):
            total += min_edge(spt.cycle[i - 1], spt.cycle[i])
        total += min_edge(spt.cycle[-1], spt.cycle[0])

        if total < 0:
            return True

        return False

    @raises(RuntimeError)
    def check_empty(self, spt):
        spt(WeightedDiGraph())

    def check_source(self, spt):
        g = WeightedDiGraph()

        g.add_edge(0, 1, 2)

        h = spt(g, 0)

        assert h.costs[0] == 0, h.costs[0]
        assert h.costs[1] == 2, h.costs[1]

    def check_chain(self, spt, N=10):
        assert N > 0

        g = WeightedDiGraph()

        for i in range(N):
            g.add_edge(i, i + 1, 1)

        h = spt(g, 0)

        assert self.is_shortest(h, g)

    def check_random(self, spt, V=10, E=10, seed=0):
        assert V > 1 and E > 0
        random.seed(seed)

        g = WeightedDiGraph()

        for i in range(E):
            n1, n2 = random.sample(range(V), 2)
            g.add_edge(n1, n2, random.random())

        h = spt(g, n1)

        assert self.is_shortest(h, g)
        if isinstance(h, BellmanFord):
            assert h.cycle == [], h.cycle

    def check_random_negative(self, spt, V=10, E=10, seed=0):
        assert V > 1 and E > 0
        random.seed(seed)

        g = WeightedDiGraph()
        j = WeightedDiGraph()

        for i in range(E):
            n1, n2 = random.sample(range(V), 2)
            g.add_edge(n1, n2, random.random() - 0.5)

        for src in g:
            for dst, w in g[src]:
                j.add_edge(src, dst, w)

        h = spt(g, n1)

        for src in j:
            for dst, w in j[src]:
                assert [dst, w] in g[src]

        if h.cycle:
            assert self.is_negative_cycle(h, g), h.cycle
        else:
            assert self.is_shortest(h, g)


class TestDijkstra(CheckShortestPath):
    def test_empty(self):
        yield self.check_empty, Dijkstra

    def test_source(self):
        yield self.check_source, Dijkstra

    def test_chain(self, ns=range(1, 10)):
        for n in ns:
            yield self.check_chain, Dijkstra, n

    def test_random_0(self, ns=range(2, 8), ntimes=10):
        for n in ns:
            e = math.factorial(n)

            for i in range(ntimes):
                yield self.check_random, Dijkstra, n, e, i

    def test_random_1(self, ns=range(2, 100), ntimes=10):
        for n in ns:
            for i in range(ntimes):
                yield self.check_random, Dijkstra, n, n


class TestBellmanFord(CheckShortestPath):
    def test_empty(self):
        yield self.check_empty, BellmanFord

    def test_source(self):
        yield self.check_source, BellmanFord

    def test_chain(self, ns=range(1, 10)):
        for n in ns:
            yield self.check_chain, BellmanFord, n

    def test_random_0(self, ns=range(2, 8), ntimes=10):
        for n in ns:
            e = math.factorial(n)

            for i in range(ntimes):
                yield self.check_random, BellmanFord, n, e, i

    def test_random_1(self, ns=range(2, 100), ntimes=10):
        for n in ns:
            for i in range(ntimes):
                yield self.check_random, BellmanFord, n, n, i

    def test_negative_0(self):
        g = WeightedDiGraph()
        g.add_edge(0, 1, -1)

        h = BellmanFord(g, 0)

        assert h.costs[0] == 0
        assert h.costs[1] == -1
        assert h.paths[0] == None
        assert h.paths[1] == 0

    def test_negative_1(self):
        g = WeightedDiGraph()
        g.add_edge(0, 1, -1)
        g.add_edge(0, 1, -2)

        h = BellmanFord(g, 0)

        assert h.costs[0] == 0
        assert h.costs[1] == -2
        assert h.paths[0] == None
        assert h.paths[1] == 0

    def test_negative_cycle_0(self):
        g = WeightedDiGraph()
        g.add_edge(0, 1, -1)
        g.add_edge(1, 0, -1)

        h = BellmanFord(g, 0)

        print(h.cycle)
        print(h.paths)

        assert self.is_negative_cycle(h, g)

    def test_negative_cycle_1(self):
        g = WeightedDiGraph()
        g.add_edge(0, 0, -1)

        h = BellmanFord(g, 0)

        assert self.is_negative_cycle(h, g)

    def test_negative_cycle_2(self):
        g = WeightedDiGraph()

        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, -3)

        h = BellmanFord(g, 0)

        assert self.is_negative_cycle(h, g), h.cycle

    def test_disconnected_0(self):
        g = WeightedDiGraph()

        g.graph[0] = []
        g.graph[1] = []

        h = BellmanFord(g, 0)

        assert h.costs[0] == 0
        assert h.costs[1] == None
        assert h.paths[0] == None
        assert h.paths[1] == None

    def test_random_negative_1(self, ns=range(2, 8), ntimes=100):
        for n, i in product(ns, range(ntimes)):
            e = math.factorial(n)

            yield self.check_random_negative, BellmanFord, n, e, i

    def test_random_negative_1(self, ns=range(2, 100), ntimes=100):
        for n, i in product(ns, range(ntimes)):
            yield self.check_random_negative, BellmanFord, n, n, i
