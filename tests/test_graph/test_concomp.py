import pytest

from src.graph.graph import Graph
from src.graph.concomp import concomp0, concomp1, concomp2


@pytest.mark.parametrize(
    "concomp", [concomp0, concomp1, concomp2]
)
def test_one_edge(concomp):
    msg = "{} failed".format(concomp.__name__)

    g = Graph()

    g.add_edge(0, 1)

    cc = concomp(g)

    assert len(cc) == 2, msg
    assert cc[0] == cc[1], msg

@pytest.mark.parametrize(
    "concomp", [concomp0, concomp1, concomp2]
)
@pytest.mark.parametrize("n", list(range(2, 42)))
def test_simple_chain(concomp, n):
    assert n > 1

    msg = "{} failed".format(concomp.__name__)

    g = Graph()

    for i in range(n):
        g.add_edge(i, i + 1)

    cc = concomp(g)

    assert len(cc) == n + 1

    for i in range(n):
        assert cc[i] == cc[i + 1], msg


@pytest.mark.parametrize(
    "concomp", [concomp0, concomp1, concomp2]
)
def test_two_disjoint_edges(concomp):
    msg = "{} failed".format(concomp.__name__)

    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(2, 3)

    cc = concomp(g)

    assert len(cc) == 4
    assert cc[0] == cc[1]
    assert cc[2] == cc[3]
    assert cc[0] != cc[2]
