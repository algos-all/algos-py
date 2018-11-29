from src.graph.wgraph import WeightedGraph, WeightedDiGraph


class TestWeightedGraph:
    def test_add_edge_0(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)

        assert g[0] == [[1, 42]]
        assert g[1] == [[0, 42]]

    def test_del_edge_0(self):
        g = WeightedGraph()

        g.del_edge(0, 1)

        assert g == {}

    def test_del_edge_1(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)
        g.del_edge(0, 1)

        assert g[0] == []
        assert g[1] == []

    def test_get_edges_0(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)

        edges = g.get_edges()
        assert edges == [[0, 1, 42]] or edges == [[1, 0, 42]]


class TestWeightedDiGraph:
    def test_add_edge_0(self):
        g = WeightedDiGraph()

        g.add_edge(0, 1, 42)

        assert g[0] == [[1, 42]]

    def test_del_edge_0(self):
        g = WeightedDiGraph()

        g.del_edge(0, 1)

        assert g == {}

    def test_del_edge_1(self):
        g = WeightedDiGraph()

        g.add_edge(0, 1, 42)
        g.del_edge(0, 1)

        assert g[0] == []

    def test_get_edges_0(self):
        g = WeightedDiGraph()

        g.add_edge(0, 1, 42)

        edges = g.get_edges()
        assert edges == [[0, 1, 42]]

