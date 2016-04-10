class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def __len__(self):
        return len(self.graph)

    def __iter__(self):
        return iter(self.graph)

    def __getitem__(self, node):
        return self.graph[node]

    def __eq__(self, other):
        return self.graph == other

    def __ne__(self, other):
        return self.graph != other

    def __repr__(self):
        return self.graph.__repr__()

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


class WeightedDiGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2, w=0):
        if n1 not in self.edges: self.edges[n1] = []
        if n2 not in self.edges: self.edges[n2] = []

        self.edges[n1].append([n2, w])

    def del_edge(self, n1, n2):
        if n1 not in self.edges: return

        self.edges[n1] = [[n, w] for n, w in self.edges[n1] if n != n2]

    def get_edges(self):
        return [
            [n1, n2, w] for n1 in self.edges
            for n2, w in self.edges[n1]
        ]
