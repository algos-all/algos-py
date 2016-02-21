from heap import Heap
from wgraph import WeightedGraph
from unifind import QuickFind


class LazyPrimMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vnodes = {node : None for node in wgraph.edges}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        node1 = next(iter(wgraph.edges), None)

        for i in range(len(wgraph.edges) - 1):
            vnodes[node1] = True

            for node2, w in wgraph.edges[node1]:
                wedges.push([node1, node2, w])

            node1, node2, w = wedges.pop()
            while vnodes[node2] is not None:
                node1, node2, w = wedges.pop()

            self.add_edge(node1, node2, w)

            node1 = node2


class EagerPrimMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vnodes = {node : None for node in wgraph.edges}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        node1 = next(iter(wgraph.edges), None)

        for i in range(len(wgraph.edges) - 1):
            vnodes[node1] = True

            for node2, w in wgraph.edges[node1]:
                if vnodes[node2] is True:
                    continue

                if vnodes[node2] is None:
                    vnodes[node2] = [node1, w]
                    wedges.push([node1, node2, w])
                    continue

                if vnodes[node2][-1] > w:
                    vnodes[node2] = [node1, w]
                    wedges.push([node1, node2, w])
                    continue

            node1, node2, w = wedges.pop()
            while vnodes[node2] is True:
                node1, node2, w = wedges.pop()

            self.add_edge(node1, node2, w)

            node1 = node2


class KruskalMST(WeightedGraph):
    def __init__(self, wgraph):
        super().__init__()

        # visited nodes and weighted edges
        vunion = QuickFind(n for n in wgraph.edges)
        wedges = Heap(
            xs=wgraph.get_edges(), key=lambda x, y: x[-1] < y[-1]
        )

        for i in range(len(wgraph.edges) - 1):
            n1, n2, w = wedges.pop()

            while vunion.find(n1) == vunion.find(n2):
                n1, n2, w = wedges.pop()

            self.add_edge(n1, n2, w)

            vunion.union(n1, n2)
