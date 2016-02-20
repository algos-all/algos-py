import random, collections

from graph import Graph, WeightedGraph, DiGraph


class TestGraph:
    def setup(self):
        self.g = Graph()

    def test_add_edge(self):
        self.g.add_edge(0, 1)
        for i in range(2): len(self.g.edges[i]) == 1

    def test_add_edge_loop(self):
        for i in range(10):
            self.g.add_edge(i, i + 1)

        for i in range(1, 9):
            assert len(self.g.edges[i]) == 2

        for i in [0, 10]:
            assert len(self.g.edges[i]) == 1

    def test_del_edge(self):
        self.g.add_edge(0, 1)
        for i in [0, 1]:
            assert len(self.g.edges[i]) == 1

        self.g.del_edge(0, 1)
        for i in [0, 1]:
            assert len(self.g.edges[i]) == 0

    def test_del_edge_nonexistent(self):
        self.g.del_edge(0, 1)
        assert True

    def test_del_edge_multiple(self):
        for i in range(3): self.g.add_edge(0, 1)
        self.g.del_edge(0, 1)
        for i in range(2): assert len(self.g.edges[i]) == 0


class TestWeightedGraph:
    def test_add_edge_0(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)

        assert g.edges[0] == [[1, 42]]
        assert g.edges[1] == [[0, 42]]

    def test_del_edge_0(self):
        g = WeightedGraph()

        g.del_edge(0, 1)

        assert g.edges == {}

    def test_del_edge_1(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)
        g.del_edge(0, 1)

        assert g.edges[0] == []
        assert g.edges[1] == []

    def test_get_edges_0(self):
        g = WeightedGraph()

        g.add_edge(0, 1, 42)

        edges = g.get_edges()
        assert edges == [[0, 1, 42]] or edges == [[1, 0, 42]]

    def check_mst_0(self, method):
        g = WeightedGraph()

        g = method(g)

        assert g.edges == {}

    def test_kruskal_mst_0(self):
        self.check_mst_0(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_0(self):
        self.check_mst_0(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_0(self):
        self.check_mst_0(lambda g: g.lazy_prim_mst())

    def check_mst_1(self, method):
        g = WeightedGraph()
        g.add_edge(0, 1, 42)

        h = method(g)

        assert h.edges == g.edges

    def test_kruskal_mst_1(self):
        self.check_mst_1(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_1(self):
        self.check_mst_1(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_1(self):
        self.check_mst_1(lambda g: g.eager_prim_mst())

    def check_mst_2(self, method, N):
        g = WeightedGraph()
        for i in range(N):
            g.add_edge(i, i + 1, random.random())

        h = method(g)

        for n1 in h.edges:
            for n2, w in h.edges[n1]:
                assert [n2, w] in g.edges[n1]

    def test_kruskal_mst_2(self, N=10):
        self.check_mst_2(lambda g: g.kruskal_mst(), N)

    def test_lazy_prim_mst_2(self, N=10):
        self.check_mst_2(lambda g: g.lazy_prim_mst(), N)

    def test_eager_prim_mst_2(self, N=10):
        self.check_mst_2(lambda g: g.eager_prim_mst(), N)

    def check_mst_3(self, method):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(0, 2, 2)

        h = method(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert h.edges[2] == [[1, 1]]

    def test_kruskal_mst_3(self):
        self.check_mst_3(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_3(self):
        self.check_mst_3(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_3(self):
        self.check_mst_3(lambda g: g.eager_prim_mst())

    def check_mst_4(self, method):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 0, 3)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 3, 5)

        h = method(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert len(h.edges[2]) == 2
        assert [1, 1] in h.edges[2] and [3, 2] in h.edges[2]

        assert h.edges[3] == [[2, 2]]

    def test_kruskal_mst_4(self):
        self.check_mst_4(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_4(self):
        self.check_mst_4(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_4(self):
        self.check_mst_4(lambda g: g.eager_prim_mst())

    def check_mst_5(self, method):
        g = WeightedGraph()

        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 0, 3)
        g.add_edge(0, 2, 2)
        g.add_edge(1, 3, 3)

        h = method(g)

        assert h.edges[0] == [[1, 0]]

        assert len(h.edges[1]) == 2
        assert [0, 0] in h.edges[1] and [2, 1] in h.edges[1]

        assert len(h.edges[2]) == 2
        assert [1, 1] in h.edges[2] and [3, 2] in h.edges[2]

        assert h.edges[3] == [[2, 2]]

    def test_kruskal_mst_5(self):
        self.check_mst_5(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_5(self):
        self.check_mst_5(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_5(self):
        self.check_mst_5(lambda g: g.eager_prim_mst())

    def check_mst_6(self, method):
        g = WeightedGraph()

        # control the traversal order of the graph
        g.edges = collections.OrderedDict()

        g.add_edge("a", "b", 1)
        g.add_edge("a", "c", 2)

        h = method(g)

        assert len(h.edges["a"]) == 2
        assert ["b", 1] in h.edges["a"]
        assert ["c", 2] in h.edges["a"]

        assert len(h.edges["b"]) == 1
        assert h.edges["b"] == [["a", 1]]

        assert len(h.edges["c"]) == 1
        assert h.edges["c"] == [["a", 2]]

    def test_kruskal_mst_6(self):
        self.check_mst_3(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_6(self):
        self.check_mst_6(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_6(self):
        self.check_mst_6(lambda g: g.eager_prim_mst())

    def check_mst_7(self, method):
        g = WeightedGraph()

        # control the traversal order of the graph
        g.edges = collections.OrderedDict()

        g.add_edge("a", "b", 1)
        g.add_edge("a", "c", 2)
        g.add_edge("a", "d", 3)
        g.add_edge("a", "e", 4)

        h = method(g)

        assert len(h.edges["a"]) == 4
        for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
            assert [n, w] in h.edges["a"]

        for n, w in zip(["b", "c", "d", "e"], range(1, 5)):
            assert h.edges[n] == [["a", w]]

    def test_kruskal_mst_7(self):
        self.check_mst_3(lambda g: g.kruskal_mst())

    def test_lazy_prim_mst_7(self):
        self.check_mst_7(lambda g: g.lazy_prim_mst())

    def test_eager_prim_mst_7(self):
        self.check_mst_7(lambda g: g.eager_prim_mst())


class TestDiGraph:
    def setup(self):
        self.g = DiGraph()

    def test_add_edge_0(self):
        self.g.add_edge(0, 1)

        assert self.g.edges[0] == [1]
        assert self.g.edges[1] == []

    def test_add_edge_1(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 1)

        assert self.g.edges[0] == [1, 1]
        assert self.g.edges[1] == []

    def test_add_edge_2(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        assert self.g.edges[0] == [1]
        assert self.g.edges[1] == [0]

    def test_del_edge_0(self):
        self.g.del_edge(0, 1)

        assert self.g.edges == {}

    def test_del_edge_1(self):
        self.g.add_edge(0, 1)
        self.g.del_edge(0, 1)

        assert self.g.edges[0] == []
        assert self.g.edges[1] == []

    def test_del_edge_2(self, N=10):
        for i in range(N):
            self.g.add_edge(0, 1)

        self.g.del_edge(0, 1)

        assert self.g.edges[0] == []
        assert self.g.edges[1] == []

    def test_del_edge_3(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 2)
        self.g.add_edge(1, 2)

        self.g.del_edge(0, 1)

        assert self.g.edges[0] == [2]
        assert self.g.edges[1] == [2]
        assert self.g.edges[2] == []

    def test_transpose_0(self):
        t = self.g.transpose()

        assert t.edges == {}

    def test_transpose_1(self):
        self.g.add_edge(0, 1)

        t = self.g.transpose()

        assert t.edges[0] == []
        assert t.edges[1] == [0]

    def test_transpose_2(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        t = self.g.transpose()

        assert t.edges[0] == []
        assert t.edges[1] == []

    def test_transpose_3(self, N=10):
        for i in range(N):
            self.g.add_edge(i, i + 1)

        self.g.add_edge(N, 0)

        t = self.g.transpose()

        for i in range(N + 1):
            for j in range(N + 1):
                if j == i or j == i + 1 or (j == 0 and i == N):
                    assert j not in t.edges[i]
                else:
                    assert j in t.edges[i], "{} {}".format(j, i)

    def test_has_cycle_0(self):
        assert self.g.has_cycle() is False

    def test_has_cycle_1(self):
        self.g.add_edge(0, 1)

        assert self.g.has_cycle() is False

    def test_has_cycle_2(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        assert self.g.has_cycle() is True

    def test_has_cycle_3(self, N=10):
        for i in range(N):
            self.g.add_edge(i, i + 1)

        self.g.add_edge(N, 0)

        assert self.g.has_cycle() is True

    def test_rpostdfs_0(self):
        assert list(self.g.rpostdfs()) == []

    def test_rpostdfs_1(self, N=10):
        for i in range(N):
            self.g.add_edge(i, i + 1)

        rorder = self.g.rpostdfs()

        assert list(rorder) == list(range(N + 1))

    def test_rpostdfs_2(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        rorder = list(self.g.rpostdfs())

        assert rorder == [0, 1] or rorder == [1, 0]

    def test_toposort_0(self):
        assert list(self.g.toposort()) == []

    def test_toposort_1(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        assert self.g.toposort() is None

    def test_toposort_2(self, N=10):
        for i in range(N):
            self.g.add_edge(i + 1, i)

        assert list(self.g.toposort()) == list(range(N, -1, -1))

    def test_sconcomp_0(self):
        scc = self.g.sconcomp()

        assert scc == {}

    def test_sconcomp_1(self):
        self.g.add_edge(0, 1)

        scc = self.g.sconcomp()

        assert scc[0] != scc[1], scc[1]

    def test_sconcomp_2(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 0)

        scc = self.g.sconcomp()

        assert scc[0] == scc[1]

    def test_sconcomp_3(self, N=10):
        for i in range(N):
            self.g.add_edge(i, i + 1)

        self.g.add_edge(N, 0)

        scc = self.g.sconcomp()

        for i in range(N):
            assert scc[i] == scc[i + 1]
