from src.graph.agraph import AbstractGraph


class WeightedGraph(AbstractGraph):

    def add_edge(self, n1, n2, w=0):
        if n1 not in self.graph: self.graph[n1] = []
        if n2 not in self.graph: self.graph[n2] = []

        self.graph[n1].append([n2, w])
        self.graph[n2].append([n1, w])

    def del_edge(self, n1, n2):
        if n1 not in self.graph: return
        if n2 not in self.graph: return

        self.graph[n1] = [[n, w] for n, w in self[n1] if n != n2]
        self.graph[n2] = [[n, w] for n, w in self[n2] if n != n1]

    def get_edges(self):
        return [
            [n1, n2, w] for n1 in self for n2, w in self[n1] if n1 > n2
        ]


class WeightedDiGraph(AbstractGraph):

    def add_edge(self, n1, n2, w=0):
        if n1 not in self.graph: self.graph[n1] = []
        if n2 not in self.graph: self.graph[n2] = []

        self.graph[n1].append([n2, w])

    def del_edge(self, n1, n2):
        if n1 not in self.graph: return

        self.graph[n1] = [[n, w] for n, w in self[n1] if n != n2]

    def get_edges(self):
        return [
            [n1, n2, w] for n1 in self for n2, w in self[n1]
        ]
