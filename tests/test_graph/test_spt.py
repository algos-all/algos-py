import math, random, pytest

from itertools import product

from src.graph.wgraph import WeightedDiGraph
from src.graph.spt import Dijkstra, BellmanFord


def is_shortest(spt, wdgraph):
    for n1 in wdgraph:
        # there may be several connected components
        if spt.costs[n1] is None: continue

        for n2, w in wdgraph[n1]:
            if spt.costs[n2] > spt.costs[n1] + w:
                return False

    return True

def is_negative_cycle(spt, wdgraph):
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

@pytest.mark.parametrize("SPT", [Dijkstra, BellmanFord])
def test_empty(SPT):
    with pytest.raises(RuntimeError):
        SPT(WeightedDiGraph())

@pytest.mark.parametrize("SPT", [Dijkstra, BellmanFord])
def test_source(SPT):
    g = WeightedDiGraph()

    g.add_edge(0, 1, 2)

    h = SPT(g, 0)

    assert h.costs[0] == 0, h.costs[0]
    assert h.costs[1] == 2, h.costs[1]

@pytest.mark.parametrize("SPT", [Dijkstra, BellmanFord])
@pytest.mark.parametrize("N", list(range(1, 10)))
def test_chain(SPT, N):
    assert N > 0

    g = WeightedDiGraph()

    for i in range(N):
        g.add_edge(i, i + 1, 1)

    h = SPT(g, 0)

    assert is_shortest(h, g)

@pytest.mark.parametrize("SPT", [Dijkstra, BellmanFord])
@pytest.mark.parametrize(
    "V,E", [(i, i ** 2) for i in range(2, 50)]
)
@pytest.mark.parametrize("seed", list(range(3)))
def test_random(SPT, V, E, seed):
    assert V > 1 and E > 0

    random.seed(seed)

    g = WeightedDiGraph()

    for i in range(E):
        n1, n2 = random.sample(range(V), 2)
        g.add_edge(n1, n2, random.random())

    h = SPT(g, n1)

    assert is_shortest(h, g)
    
    if isinstance(h, BellmanFord):
        assert h.cycle == [], h.cycle

@pytest.mark.parametrize("SPT", [BellmanFord])
@pytest.mark.parametrize(
    "V,E", [(i, i ** 2) for i in range(2, 50)]
)
@pytest.mark.parametrize("seed", list(range(3)))
def test_random_negative(SPT, V, E, seed):
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

    h = SPT(g, n1)

    for src in j:
        for dst, w in j[src]:
            assert [dst, w] in g[src]

    if h.cycle:
        assert is_negative_cycle(h, g), h.cycle
    else:
        assert is_shortest(h, g)

def test_negative_0():
    g = WeightedDiGraph()

    g.add_edge(0, 1, -1)

    h = BellmanFord(g, 0)

    assert h.costs[0] == 0
    assert h.costs[1] == -1
    assert h.paths[0] == None
    assert h.paths[1] == 0

def test_negative_1():
    g = WeightedDiGraph()

    g.add_edge(0, 1, -1)
    g.add_edge(0, 1, -2)

    h = BellmanFord(g, 0)

    assert h.costs[0] == 0
    assert h.costs[1] == -2
    assert h.paths[0] == None
    assert h.paths[1] == 0

def test_negative_cycle_0():
    g = WeightedDiGraph()

    g.add_edge(0, 1, -1)
    g.add_edge(1, 0, -1)

    h = BellmanFord(g, 0)

    print(h.cycle)
    print(h.paths)

    assert is_negative_cycle(h, g)

def test_negative_cycle_1():
    g = WeightedDiGraph()

    g.add_edge(0, 0, -1)

    h = BellmanFord(g, 0)

    assert is_negative_cycle(h, g)

def test_negative_cycle_2():
    g = WeightedDiGraph()

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 0, -3)

    h = BellmanFord(g, 0)

    assert is_negative_cycle(h, g), h.cycle

def test_disconnected_0():
    g = WeightedDiGraph()

    g.graph[0] = []
    g.graph[1] = []

    h = BellmanFord(g, 0)

    assert h.costs[0] == 0
    assert h.costs[1] == None
    assert h.paths[0] == None
    assert h.paths[1] == None
