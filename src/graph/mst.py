from src.heap import Heap
from src.graph.wgraph import WeightedGraph

from src.dsu import DisjointSetUnion


class LazyPrimMST(WeightedGraph):

    def __init__(self, wgraph):
        super().__init__()

        vnodes = {node: None for node in wgraph}
        wedges = Heap(xs=None, key=lambda x: x[-1], reverse=False)

        src = next(iter(wgraph), None)

        for i in range(len(wgraph) - 1):
            vnodes[src] = True

            for dst, w in wgraph[src]:
                wedges.append([src, dst, w])

            src, dst, w = wedges.pop()
            while vnodes[dst] is not None:
                src, dst, w = wedges.pop()

            self.add_edge(src, dst, w)

            src = dst


class EagerPrimMST(WeightedGraph):

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

                if nodes[dst] is None:
                    nodes[dst] = w
                    edges.append([src, dst, w])
                    continue

                if nodes[dst] > w:
                    nodes[dst] = w
                    edges.append([src, dst, w])
                    continue

            src, dst, w = edges.pop()
            while nodes[dst] is True:
                src, dst, w = edges.pop()

            self.add_edge(src, dst, w)

            src = dst


class KruskalMST(WeightedGraph):

    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        nodes = DisjointSetUnion([n for n in wgraph])
        edges = Heap(
            xs=wgraph.get_edges(), key=lambda x: x[-1], reverse=False
        )

        while edges:
            n1, n2, w = edges.pop()

            if nodes.find(n1) == nodes.find(n2):
                continue

            self.add_edge(n1, n2, w)

            nodes.union(n1, n2)
