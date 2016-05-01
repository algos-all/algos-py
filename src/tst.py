class TernarySearchTree:
    class Node:
        def __init__(self, key, val=None):
            self.key = key
            self.val = val

            self.edges = [None, None, None]

        def __getitem__(self, key):
            return self.edges[key]

        def __setitem__(self, key, val):
            self.edges[key] = val

        def __str__(self):
            return self.key + ": " + " ".join(map(str, self.edges))

        def __repr__(self):
            return self.__str__()

        def get_node_with_parent(self, key):
            i, flag, parent = 0, True, None

            while self:
                if key[i] == self.key:
                    if i + 1 == len(key):
                        return self, parent, len(key), True
                    flag = True
                    self, parent, i = self[2], self, i + 1
                else:
                    flag = False
                    here = 0 if key[i] < self.key else 1
                    self, parent = self[here], self

            return None, parent, i, flag

        def get(self, key):
            node, _, _, _ = self.get_node_with_parent(key)
            return None if node is None else node.val

    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        if self.root is None: return None, None, 0, False
        return self.root.get_node_with_parent(key)

    def get(self, key):
        if self.root is None or len(key) == 0: return None
        return self.root.get(key)

    def put(self, key, val):
        if len(key) == 0:
            raise RuntimeError("Can not save empty key")

        node, parent, i, flag = self.get_node_with_parent(key)

        if node is None and parent is None:
            self.root = self.Node(key[0])
            node = self.root
        elif node is None:
            here = 2 if flag else 0 if key[i] < parent.key else 1

            parent[here] = self.Node(key[i])

            node = parent[here]

        for n in range(i + 1, len(key)):
            node[2] = self.Node(key[n])

            node = node[2]

        node.val = val

    def all(self):
        if self.root is None: return []

        results = []

        def dfs(node, prefix):
            for n in node.edges[:2]:
                if n is not None:
                    dfs(n, prefix)

            if node.edges[2] is not None:
                dfs(node.edges[2], prefix + node.key)

            vs = [
                None if node.edges[i] is None else node.edges[i].key
                for i in range(3)
            ]
            results.append(
                [node.key, vs]
            )

            # if node.val is not None:
            #     results.append(prefix + node.key)

        dfs(self.root, "")

        return results
