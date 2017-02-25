class AbstractGraph:

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
