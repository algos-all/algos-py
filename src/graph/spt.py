from heap import Heap
from collections import deque


class Dijkstra:
    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("Source node not in graph")

        self.costs = {node : None for node in wdgraph}
        self.paths = {node : None for node in wdgraph}

        self.costs[src] = 0

        edge_costs = Heap(
            xs = [[src, dst, w, w] for dst, w in wdgraph[src]],
            key = lambda x, y: x[-1] < y[-1]
        )

        while edge_costs:
            src, dst, w, c0 = edge_costs.pop()

            c1 = self.costs[dst]

            if c1 is not None and c1 <= c0: continue

            self.costs[dst] = c0
            self.paths[dst] = src

            for n, w in wdgraph[dst]:
                edge_costs.push([dst, n, w, c0 + w])


class BellmanFord:
    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("src not in wdgraph")

        self.costs = {node : None for node in wdgraph}
        self.paths = {node : None for node in wdgraph}

        self.costs[src] = 0

        relaxed = deque(maxlen=len(wdgraph))
        newcost = {node : False for node in wdgraph}

        relaxed.append(src)
        newcost[src] = True

        nepoch = 1
        epochs = len(wdgraph) + 1

        while relaxed:
            n1 = relaxed.popleft()
            newcost[n1] = False

            c1 = self.costs[n1]

            for n2, w in wdgraph[n1]:
                c2 = self.costs[n2]

                if c2 is not None and c2 < c1 + w: continue

                self.costs[n2] = c1 + w
                self.paths[n2] = n1

                if not newcost[n2]:
                    relaxed.append(n2)
                    newcost[n2] = True

            nepoch -= 1

            if nepoch == 0:
                epochs -= 1
                nepoch = len(relaxed)

            if epochs == 0:
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
