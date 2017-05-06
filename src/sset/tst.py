"""
Implementation of a Ternary Search Tree. [1]

Each node holds a single character and has up to three children.

[1]: https://en.wikipedia.org/wiki/Ternary_search_tree
"""


class TernarySearchTree:

    class Node:

        def __init__(self, top, key, val=None):
            """
            :param top: pointer to parent
            :param key: a key, usually a character
            :param val: a value, None has a special meaning

            If the value is None, then the node is an intermediate.
            """

            self.top = top
            self.key = key
            self.val = val

            self.edges = [None, None, None]

        def __len__(self):
            return sum(1 for e in self.edges if e is not None)

        def __bool__(self):
            """
            Return True if this node is intermediate or final.
            """

            return self.val is not None or bool(len(self))

        def __getitem__(self, key):
            return self.edges[key]

        def __setitem__(self, key, val):
            self.edges[key] = val

        def __str__(self):
            return self.key + ": " + " ".join(map(str, self.edges))

        def __repr__(self):
            return self.__str__()

        def get_node_with_parent(self, key):
            """
            Return a node (and its parent) that correspond to key.

            :param key: key, usually a string
            :returns: a list of [node, parent, i, flag]
            """
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

        def gcp(self, key):
            return self.get_node_with_parent(key)[2]

    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        if self.root is None or len(key) == 0:
            return None, None, 0, False
        return self.root.get_node_with_parent(key)

    def get(self, key):
        if self.root is None or len(key) == 0: return None
        return self.root.get(key)

    def put(self, key, val):
        if len(key) == 0:
            raise RuntimeError("Can't save empty key")

        node, parent, i, flag = self.get_node_with_parent(key)

        if node is None and parent is None:
            self.root = self.Node(None, key[0])
            node = self.root
        elif node is None:
            here = 2 if flag else 0 if key[i] < parent.key else 1

            parent[here] = self.Node(parent, key[i])

            node = parent[here]

        for n in range(i + 1, len(key)):
            node[2] = self.Node(node, key[n])

            node = node[2]

        node.val = val

    def remove(self, key):
        node, _, i, flag = self.get_node_with_parent(key)

        if node is None or node.val is None or i < len(key):
            return

        node.val = None

        for i in range(len(key) - 1, 0, -1):
            if node: return

            for i in range(3):
                if node.top[i] is node:
                    node.top[i] = None
                    break

            node = node.top

        if node: return
        self.root = None

    def gcp(self, key):
        """
        Return greatest common prefix of given key and tree keys
        """
        return 0 if self.root is None or len(key) == 0 else \
            self.root.gcp(key)

    def startswith(self, key):
        if self.root is None:
            return []

        if len(key) == 0:
            return self.all()

        node, _, _, _ = self.root.get_node_with_parent(key)

        if node is None:
            return []

        results = [] if node.val is None else [key]

        self._dfs(node[2], key, results)

        return results

    def all(self):
        if self.root is None: return []

        results = []

        self._dfs(self.root, "", results)

        return results

    def _dfs(self, node, prefix, results):
        if node is None: return

        for n in node.edges[:2]:
            self._dfs(n, prefix, results)

        self._dfs(node.edges[2], prefix + node.key, results)

        if node.val is not None:
            results.append(prefix + node.key)

    def show(self):
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
                [node.key, node.val, vs]
            )

        dfs(self.root, "")

        return results
