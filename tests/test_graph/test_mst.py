import random, collections, pytest

from src.graph.wgraph import WeightedGraph
from src.graph.mst import LazyPrimMST, EagerPrimMST, KruskalMST


@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def check_empty(MST):
    assert MST(WeightedGraph()) == {}

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
@pytest.mark.parametrize("N", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_chain(MST, N, seed):
    assert N > 0

    random.seed(seed)

    g = WeightedGraph()
    for i in range(N):
        g.add_edge(i, i + 1, random.random())

    h = MST(g)

    for n1 in h:
        for n2, w in h[n1]:
            errmsg = "{} {} is not in {}".format(n2, w, g[n1])

            assert [n2, w] in g[n1], errmsg

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def test_complete3(MST):
    g = WeightedGraph()

    g.add_edge(0, 1, 0)
    g.add_edge(1, 2, 1)
    g.add_edge(0, 2, 2)

    h = MST(g)

    assert h[0] == [[1, 0]], h[0]

    assert len(h[1]) == 2
    assert [0, 0] in h[1] and [2, 1] in h[1]

    assert h[2] == [[1, 1]], h[2]

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def test_complete4_0(MST):
    g = WeightedGraph()

    g.add_edge(0, 1, 0)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 0, 3)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 5)

    h = MST(g)

    assert h[0] == [[1, 0]], h[0]

    assert len(h[1]) == 2
    assert [0, 0] in h[1] and [2, 1] in h[1]

    assert len(h[2]) == 2
    assert [1, 1] in h[2] and [3, 2] in h[2]

    assert h[3] == [[2, 2]], h[3]

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def test_complete4_1(MST):
    g = WeightedGraph()

    g.add_edge(0, 1, 0)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 0, 3)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 3)

    h = MST(g)

    assert h[0] == [[1, 0]], h[0]

    assert len(h[1]) == 2
    assert [0, 0] in h[1] and [2, 1] in h[1]

    assert len(h[2]) == 2
    assert [1, 1] in h[2] and [3, 2] in h[2]

    assert h[3] == [[2, 2]], h[3]

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def test_controlled_traversal_0(MST):
    g = WeightedGraph()

    g.graph = collections.OrderedDict()

    g.add_edge("a", "b", 1)
    g.add_edge("a", "c", 2)

    h = MST(g)

    assert len(h["a"]) == 2
    assert ["b", 1] in h["a"]
    assert ["c", 2] in h["a"]

    assert len(h["b"]) == 1
    assert h["b"] == [["a", 1]]

    assert len(h["c"]) == 1
    assert h["c"] == [["a", 2]]

@pytest.mark.parametrize(
    "MST", [LazyPrimMST, EagerPrimMST, KruskalMST]
)
def test_controlled_traversal_1(MST):
    g = WeightedGraph()

    g.graph = collections.OrderedDict()

    g.add_edge("a", "b", 1)
    g.add_edge("a", "c", 2)
    g.add_edge("a", "d", 3)
    g.add_edge("a", "e", 4)

    h = MST(g)

    assert len(h["a"]) == 4
    for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
        assert [n, w] in h["a"]

    for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
        assert h[n] == [["a", w]]
