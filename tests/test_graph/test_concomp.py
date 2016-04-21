from graph.graph import Graph
from graph.concomp import concomp0, concomp1, concomp2


class CheckConnectedComponent:
    def setup(self):
        self.g = Graph()

    def check_one_edge(self, concomp):
        msg = "{} failed".format(concomp.__name__)

        self.g.add_edge(0, 1)
        cc = concomp(self.g)

        assert len(cc) == 2, msg
        assert cc[0] == cc[1], msg

    def check_many_linked_edges(self, concomp):
        N = 42
        msg = "{} failed".format(concomp.__name__)

        for i in range(N):
            self.g.add_edge(i, i + 1)

        cc = concomp(self.g)

        assert len(cc) == N + 1
        for i in range(N):
            assert cc[i] == cc[i + 1], msg

    def check_two_disjoint_edges(self, concomp):
        msg = "{} failed".format(concomp.__name__)

        self.g.add_edge(0, 1)
        self.g.add_edge(2, 3)
        cc = concomp(self.g)

        assert len(cc) == 4
        assert cc[0] == cc[1]
        assert cc[2] == cc[3]
        assert cc[0] != cc[2]


class TestConnectedComponent(CheckConnectedComponent):
    def __init__(self):
        self.concomps = [concomp0, concomp1, concomp2]

    def test_one_edge(self):
        for concomp in self.concomps:
            yield self.check_one_edge, concomp

    def test_many_linked_edges(self):
        for concomp in self.concomps:
            yield self.check_many_linked_edges, concomp

    def test_two_disjoint_edges(self):
        for concomp in self.concomps:
            yield self.check_two_disjoint_edges, concomp
