from heap import Heap
from collections import deque


class Dijkstra:
    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("Source node not in graph")

        self.costs = {node : None for node in wdgraph}
        self.paths = {node : None for node in wdgraph}

        self.costs[src] = 0

        edges = Heap(
            xs=[[src, dst, w] for dst, w in wdgraph[src]],
            key=lambda x, y: x[-1] < y[-1]
        )

        while edges:
            src, dst, c = edges.pop()

            if self.costs[dst] is not None and self.costs[dst] <= c:
                continue

            self.costs[dst] = c
            self.paths[dst] = src

            for node, w in wdgraph[dst]:
                edges.push([dst, node, w + c])

class BellmanFord:
    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("Node not in graph")

        self.costs = {node : None for node in wdgraph}
        self.paths = {node : None for node in wdgraph}

        torelax = deque(maxlen=len(wdgraph))
        inrelax = {node : False for node in wdgraph}

        self.costs[src] = 0
        torelax.append(src)
        inrelax[src] = True

        nepoch = len(wdgraph) + 1
        lepoch = 1 # len(torelax)

        while torelax:
            src = torelax.popleft()
            inrelax[src] = False

            s = self.costs[src]

            for dst, w in wdgraph[src]:
                d = self.costs[dst]

                if d is not None and d <= s + w: continue

                self.costs[dst] = s + w
                self.paths[dst] = src

                if not inrelax[dst]:
                    torelax.append(dst)
                    inrelax[dst] = True

            lepoch -= 1

            if lepoch == 0:
                nepoch -= 1
                lepoch = len(torelax)

            if nepoch == 0:
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
