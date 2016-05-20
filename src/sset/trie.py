class Trie:
    class Node:
        def __init__(self):
            self.val = None
            self.top = None
            self.edges = {}

        def __iter__(self):
            return iter(self.edges)

        def __getitem__(self, key):
            return self.edges[key]

        def put(self, key, val, i):
            for n in range(i, len(key)):
                if key[n] not in self:
                    self.edges[key[n]] = Trie.Node()
                    self.edges[key[n]].top = self

                self = self.edges[key[n]]
            self.val = val

        def get_node_with_parent(self, key):
            for i in range(len(key)):
                if key[i] not in self:
                    return self, self.top, i

                self = self[key[i]]
            return self, self.top, len(key)

        def get(self, key):
            node, _, i = self.get_node_with_parent(key)
            return None if len(key) != i else node.val

        def gcp(self, key):
            return self.get_node_with_parent(key)[2]

        def startswith(self, key):
            node, _, i = self.get_node_with_parent(key)

            if i < len(key):
                return []

            results = []

            def dfs(node, prefix):
                for k in node:
                    dfs(node[k], prefix + k)

                if node.val is not None: results.append(prefix)

            dfs(node, key)

            return results

    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        if self.root is None: return None, None, 0
        return self.root.get_node_with_parent(key)

    def get(self, key):
        return None if self.root is None else self.root.get(key)

    def gcp(self, key):
        return 0 if self.root is None else self.root.gcp(key)

    def startswith(self, key):
        return [] if self.root is None else self.root.startswith(key)

    def put(self, key, val):
        node, parent, i = self.get_node_with_parent(key)

        if node is None and parent is None:
            self.root = Trie.Node()
            node = self.root

        node.put(key, val, i)

    def remove(self, key):
        node, _, i = self.get_node_with_parent(key)

        if node is None or node.val is None or i < len(key): return

        node.val = None

        for i in range(len(key) - 1, 0, -1):
            if len(node.edges) != 0 or node.val is not None: return

            node = node.top
            node.edges.pop(key[i])

        if len(node.edges) == 0:
            self.root.edges.pop(key[0])

            if len(self.root.edges) == 0:
                self.root = None

    def all(self):
        if self.root is None: return []

        result = []

        def dfs(node, prefix):
            print(node, node.top, node.edges, node.val)
            for k in node:
                dfs(node[k], prefix + k)

            if node.val is not None:
                result.append(prefix)

        dfs(self.root, "")

        return result
