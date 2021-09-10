from src.heap import Heap
from src.graph.wgraph import WeightedGraph

from src.dsu import DisjointSetUnion


"""
Minimum Spanning Tree (MST) is a subset of the edges of a connected graph that
has weights assigned to its edges. The tree connects all vertices of the graph
together and has the minimum possible total edge weight.
"""


class LazyPrimMST(WeightedGraph):
    """
    Creates a minimum spanning tree from the provided weighted graph

    The complexity of this implementation is:

        time : (|V| + |E|)log|E| (?)
        space:  |V| + |E|        (?)
    """

    def __init__(self, wgraph):

        super().__init__()

        nodes = {node: None for node in wgraph}
        edges = Heap(xs=None, key=lambda x: x[-1], reverse=False)

        src = next(iter(wgraph), None)

        for _ in range(len(wgraph) - 1):
            nodes[src] = True

            for dst, w in wgraph[src]:
                edges.append([src, dst, w])

            src, dst, w = edges.pop()
            while nodes[dst] is not None:
                src, dst, w = edges.pop()

            self.add_edge(src, dst, w)

            src = dst


class EagerPrimMST(WeightedGraph):
    """
    Creates a minimum spanning tree from the provided weighted graph

    The complexity of this implementation is:

        time : (|V| + |E|)log|E| (?)
        space:  |E| + |V|        (?)
    """

    def __init__(self, wgraph):

        super().__init__()

        nodes = {node: None for node in wgraph}
        edges = Heap(xs=None, key=lambda x: x[-1], reverse=False)

        src = next(iter(wgraph), None)

        for i in range(len(wgraph) - 1):
            nodes[src] = True

            for dst, w in wgraph[src]:
                if nodes[dst] is True:
                    continue

                if nodes[dst] is None or nodes[dst] > w:
                    nodes[dst] = w
                    edges.append([src, dst, w])

            src, dst, w = edges.pop()
            while nodes[dst] is True:
                src, dst, w = edges.pop()

            self.add_edge(src, dst, w)

            src = dst


class KruskalMST(WeightedGraph):
    """
    Creates a minimum spanning tree from the provided weighted graph

    The complexity of this implementation is:

        time:  |E|log|E| = |E|log|V|
        space: |E| + |V|

    TODO:
        * instead of the heap, pre-sort the edges once. Wikipedia describes so:
            https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    """

    def __init__(self, wgraph):

        super().__init__()

        nodes = DisjointSetUnion([node for node in wgraph])
        edges = Heap(xs=wgraph.get_edges(), key=lambda x: x[-1], reverse=False)

        while edges:
            src, dst, w = edges.pop()

            if nodes.find(src) == nodes.find(dst):
                continue

            self.add_edge(src, dst, w)

            nodes.union(src, dst)
