from src.heap import Heap
from collections import deque


class Dijkstra:

    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("Source node not in graph")

        self.costs = {node: None for node in wdgraph}
        self.paths = {node: None for node in wdgraph}

        self.costs[src] = 0

        edges = Heap(
            xs=[[src, dst, w] for dst, w in wdgraph[src]],
            key=lambda x: x[-1], reverse=False
        )

        while edges:
            src, dst, c = edges.pop()

            if self.costs[dst] is not None and self.costs[dst] <= c:
                continue

            self.costs[dst] = c
            self.paths[dst] = src

            for node, w in wdgraph[dst]:
                edges.append([dst, node, w + c])


class BellmanFord:
    """
    Compute travel costs from the given vertex to all others.

    This algorithm handles negative weights. If a negative cycle
    is detected, the algorithm aborts and reports the found cycle.
    """

    def __init__(self, wdgraph, src=None):
        if src not in wdgraph:
            raise RuntimeError("Node not in graph")

        self.costs = {node: None for node in wdgraph}
        self.paths = {node: None for node in wdgraph}

        torelax = deque(maxlen=len(wdgraph))
        inrelax = {node: False for node in wdgraph}

        self.costs[src] = 0
        torelax.append(src)
        inrelax[src] = True

        nepoch = len(wdgraph) + 1
        lepoch = 1  # len(torelax)

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
        visited = {n: None for n in self.paths}

        for i, n in enumerate(self.paths):
            if visited[n] is not None:
                continue

            path = []

            while n is not None and visited[n] is None:
                visited[n] = i
                path.append(n)

                n = self.paths[n]

            if n is not None and visited[n] == i:
                # cycle can start with a "tail" that is not part of it
                self.cycle = list(reversed(path[path.index(n):]))
                return

        self.cycle = []
