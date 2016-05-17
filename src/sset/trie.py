class Trie:
    class Node:
        def __init__(self):
            self.edges = {}
            self.val = None

        def __iter__(self):
            return iter(self.edges)

        def __getitem__(self, key):
            return self.edges[key]

        def put(self, key, val, i=0):
            for n in range(i, len(key)):
                if key[n] not in self:
                    self.edges[key[n]] = Trie.Node()

                self = self.edges[key[n]]
            self.val = val

        def get_node_with_parent(self, key):
            parent = None
            for i in range(len(key)):
                if key[i] not in self:
                    return self, parent, i

                self, parent = self[key[i]], self
            return self, parent, len(key)

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

    def all(self):
        if self.root is None: return []

        result = []

        def dfs(node, prefix):
            print(node, node.edges)
            for k in node:
                dfs(node[k], prefix + k)

            if node.val is not None:
                result.append(prefix)

        dfs(self.root, "")

        return result
