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
