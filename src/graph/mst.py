from heap import Heap
from graph.wgraph import WeightedGraph
from unifind import QuickFind


class LazyPrimMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vnodes = {node : None for node in wgraph}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        src = next(iter(wgraph), None)

        for i in range(len(wgraph) - 1):
            vnodes[src] = True

            for dst, w in wgraph[src]:
                wedges.push([src, dst, w])

            src, dst, w = wedges.pop()
            while vnodes[dst] is not None:
                src, dst, w = wedges.pop()

            self.add_edge(src, dst, w)

            src = dst


class EagerPrimMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vnodes = {node : None for node in wgraph}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        src = next(iter(wgraph), None)

        for i in range(len(wgraph) - 1):
            vnodes[src] = True

            for dst, w in wgraph[src]:
                if vnodes[dst] is True:
                    continue

                if vnodes[dst] is None:
                    vnodes[dst] = w
                    wedges.push([src, dst, w])
                    continue

                if vnodes[dst] > w:
                    vnodes[dst] = w
                    wedges.push([src, dst, w])
                    continue

            src, dst, w = wedges.pop()
            while vnodes[dst] is True:
                src, dst, w = wedges.pop()

            self.add_edge(src, dst, w)

            src = dst


class KruskalMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vunion = QuickFind(n for n in wgraph)
        wedges = Heap(
            xs=wgraph.get_edges(), key=lambda x, y: x[-1] < y[-1]
        )

        for i in range(len(wgraph) - 1):
            n1, n2, w = wedges.pop()

            while vunion.find(n1) == vunion.find(n2):
                n1, n2, w = wedges.pop()

            self.add_edge(n1, n2, w)

            vunion.union(n1, n2)
