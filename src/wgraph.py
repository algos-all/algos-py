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
