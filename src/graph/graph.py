from src.graph.agraph import AbstractGraph


class Graph(AbstractGraph):

    def add_edge(self, n1, n2):
        if n1 not in self.graph: self.graph[n1] = []
        if n2 not in self.graph: self.graph[n2] = []

        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def del_edge(self, n1, n2):
        if n1 not in self.graph: return
        if n2 not in self.graph: return

        self.graph[n1] = [n for n in self.graph[n1] if n != n2]
        self.graph[n2] = [n for n in self.graph[n2] if n != n1]


class DiGraph(AbstractGraph):

    def add_edge(self, n1, n2):
        if n1 not in self: self.graph[n1] = []
        if n2 not in self: self.graph[n2] = []

        self.graph[n1].append(n2)

    def del_edge(self, n1, n2):
        if n1 not in self: return

        self.graph[n1] = [n for n in self[n1] if n != n2]

    def transpose(self):
        g = DiGraph()

        g.graph = {
            src: [
                n for n in self if n not in dst and n is not src
            ] for src, dst in self.graph.items()
        }

        return g

    def has_cycle(self):
        def dfs(node, i):
            visited[node] = i

            for n in self[node]:
                if visited[n] == i:
                    return True
                if visited[n] is not None:
                    continue

                if dfs(n, i): return True

            return False

        visited = {node: None for node in self}

        for i, node in enumerate(self):
            if visited[node] is not None:
                continue

            if dfs(node, i):
                return True

        return False

    def rpostdfs(self):
        def dfs(node, i):
            visited[node] = i

            for n in self[node]:
                if visited[n] is not None:
                    continue

                dfs(n, i)

            postdfs.append(node)

        postdfs = []
        visited = {node: None for node in self}

        for i, node in enumerate(self):
            if visited[node] is not None: continue

            dfs(node, i)

        return reversed(postdfs)

    def toposort(self):
        return None if self.has_cycle() else self.rpostdfs()

    def sconcomp(self):
        def dfs(node, i):
            visited[node] = i

            for n in self[node]:
                if visited[n] is not None: continue

                dfs(n, i)

        visited = {node: None for node in self}

        for i, node in enumerate(self.transpose().rpostdfs()):
            if visited[node] is not None: continue

            dfs(node, i)

        return visited
