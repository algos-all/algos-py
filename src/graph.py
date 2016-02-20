from heap import Heap
from unifind import QuickFind

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2):
        if n1 not in self.edges: self.edges[n1] = []
        if n2 not in self.edges: self.edges[n2] = []

        self.edges[n1].append(n2)
        self.edges[n2].append(n1)

    def del_edge(self, n1, n2):
        if n1 not in self.edges: return
        if n2 not in self.edges: return

        self.edges[n1] = [n for n in self.edges[n1] if n != n2]
        self.edges[n2] = [n for n in self.edges[n2] if n != n1]


class WeightedGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2, w=0):
        if n1 not in self.edges: self.edges[n1] = []
        if n2 not in self.edges: self.edges[n2] = []

        self.edges[n1].append([n2, w])
        self.edges[n2].append([n1, w])

    def del_edge(self, n1, n2):
        if n1 not in self.edges: return
        if n2 not in self.edges: return

        self.edges[n1] = [[n, w] for n, w in self.edges[n1] if n != n2]
        self.edges[n2] = [[n, w] for n, w in self.edges[n2] if n != n1]

    def get_edges(self):
        return [
            [n1, n2, w] for n1 in self.edges
            for n2, w in self.edges[n1] if n1 > n2
        ]

    def lazy_prim_mst(self):
        g = WeightedGraph()

        # visited nodes and weighted edges
        vnodes = {node : None for node in self.edges}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        node1 = next(iter(self.edges), None)

        for i in range(len(self.edges) - 1):
            vnodes[node1] = True

            for node2, w in self.edges[node1]:
                wedges.push([node1, node2, w])

            node1, node2, w = wedges.pop()
            while vnodes[node2] is not None:
                node1, node2, w = wedges.pop()

            g.add_edge(node1, node2, w)

            node1 = node2

        return g

    def eager_prim_mst(self):
        g = WeightedGraph()

        # visited nodes and weighted edges
        vnodes = {node : None for node in self.edges}
        wedges = Heap(xs=None, key=lambda x, y: x[-1] < y[-1])

        node1 = next(iter(self.edges), None)

        for i in range(len(self.edges) - 1):
            vnodes[node1] = True

            for node2, w in self.edges[node1]:
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

            g.add_edge(node1, node2, w)

            node1 = node2

        return g

    def kruskal_mst(self):
        g = WeightedGraph()

        vunion = QuickFind(n for n in self.edges)
        wedges = Heap(
            xs=self.get_edges(), key=lambda x, y: x[-1] < y[-1]
        )

        for i in range(len(self.edges) - 1):
            n1, n2, w = wedges.pop()

            while vunion.find(n1) == vunion.find(n2):
                n1, n2, w = wedges.pop()

            g.add_edge(n1, n2, w)
            vunion.union(n1, n2)

        return g

class DiGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2):
        if n1 not in self.edges: self.edges[n1] = []
        if n2 not in self.edges: self.edges[n2] = []

        self.edges[n1].append(n2)

    def del_edge(self, n1, n2):
        if n1 not in self.edges: return

        self.edges[n1] = [n for n in self.edges[n1] if n != n2]

    def transpose(self):
        g = DiGraph()

        g.edges = {
            src : [
                n for n in self.edges if n not in dst and n is not src
            ] for src, dst in self.edges.items()
        }

        return g

    def has_cycle(self):
        def dfs(edges, node, i):
            visited[node] = i

            for n in edges[node]:
                if visited[n] == i:
                    return True
                if visited[n] is not None:
                    continue

                if dfs(edges, n, i):
                    return True

            return False

        visited = {node : None for node in self.edges}

        for i, node in enumerate(self.edges):
            if visited[node] is not None: continue

            if dfs(self.edges, node, i): return True

        return False

    def rpostdfs(self):
        def dfs(edges, node, i):
            visited[node] = i

            for n in edges[node]:
                if visited[n] is not None: continue

                dfs(edges, n, i)

            postdfs.append(node)

        postdfs = []
        visited = {node : None for node in self.edges}

        for i, node in enumerate(self.edges):
            if visited[node] is not None: continue

            dfs(self.edges, node, i)

        return reversed(postdfs)

    def toposort(self):
        return None if self.has_cycle() else self.rpostdfs()

    def sconcomp(self):
        def dfs(edges, node, i):
            visited[node] = i

            for n in edges[node]:
                if visited[n] is not None: continue

                dfs(edges, n, i)

        visited = {node : None for node in self.edges}

        for i, node in enumerate(self.transpose().rpostdfs()):
            if visited[node] is not None: continue

            dfs(self.edges, node, i)

        return visited
