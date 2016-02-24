from heap import Heap


class ShortestPathTree:
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2, w):
        if n1 not in self.edges: self.edges[n1] = []
        if n2 not in self.edges: self.edges[n2] = []

        self.edges[n1] = [n for n in self.edges[n1] if n != n2]
        self.edges[n1].append([n2, w])


class LazyDijkstra(ShortestPathTree):
    def __init__(self, wdgraph, src=None):
        super().__init__()

        if src not in wdgraph.edges:
            raise RuntimeError("Source node not in graph")

        self.costs = {node : None for node in wdgraph.edges}
        self.paths = {node : None for node in wdgraph.edges}

        self.costs[src] = 0

        edge_costs = Heap(
            xs = [[src, n, w, w] for n, w in wdgraph.edges[src]],
            key = lambda x, y: x[-1] < y[-1]
        )

        while edge_costs:
            n1, n2, w, c = edge_costs.pop()

            cost = self.costs[n2]

            if cost is not None and cost < c: continue

            self.costs[n2] = c
            self.paths[n2] = n1

            self.add_edge(n1, n2, w)

            for n3, w in wdgraph.edges[n2]:
                edge_costs.push([n2, n3, w, c + w])
