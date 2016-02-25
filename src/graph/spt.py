from heap import Heap
from collections import deque


class Dijkstra:
    def __init__(self, wdgraph, src=None):
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

            for n3, w in wdgraph.edges[n2]:
                edge_costs.push([n2, n3, w, c + w])


class BellmanFord:
    def __init__(self, wdgraph, src=None):
        if src not in wdgraph.edges:
            raise RuntimeError("Source node not in graph")

        self.costs = {node : None for node in wdgraph.edges}
        self.paths = {node : None for node in wdgraph.edges}

        this_epoch = deque(maxlen=len(wdgraph.edges))
        next_epoch = {node : False for node in wdgraph.edges}

        self.costs[src] = 0
        self.paths[src] = None

        this_epoch.append(src)
        next_epoch[src] = True

        i, j = 0, 1

        while this_epoch:
            n1 = this_epoch.popleft()
            next_epoch[n1] = False

            cost1 = self.costs[n1]
            for n2, w in wdgraph.edges[n1]:
                cost2 = self.costs[n2]

                if cost2 is not None and cost2 < cost1 + w: continue

                self.costs[n2] = cost1 + w
                self.paths[n2] = n1

                if not next_epoch[n2]:
                    this_epoch.append(n2)
                    next_epoch[n2] = True

            j -= 1

            if j == 0: i, j = i + 1, len(this_epoch)

            if i % (len(wdgraph.edges) + 1) == 0:
                break

        self._check_negative_cycle()

    def _check_negative_cycle(self):
        onpath = {n : None for n in self.paths}

        for i, n in enumerate(self.paths):
            if onpath[n] is not None:
                continue

            while n is not None and onpath[n] is None:
                onpath[n] = i

                n = self.paths[n]

            if n is not None and onpath[n] == i: break
        else:
            self.cycle = []
            return

        self.cycle = [n]
        n = self.paths[n]

        while self.cycle[0] is not n:
            self.cycle.append(n)

            n = self.paths[n]

        self.cycle = list(reversed(self.cycle))
