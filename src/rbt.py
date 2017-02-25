class Node:

    def __init__(self, key, val, red=True, parent=None):
        self.key, self.val = key, val
        self.edges = [None, None, parent]

        self.red = red

    def __getitem__(self, key):
        return self.edges[key]

    def __setitem__(self, key, val):
        self.edges[key] = val

    @staticmethod
    def isred(node):
        return node and node.red

    def both_kids_are_red(self):
        return Node.isred(self[0]) and Node.isred(self[1])

    def both_ll_or_rr_are_red(self, thisway):
        kid = self[thisway]
        return Node.isred(kid) and Node.isred(kid[thisway])

    def both_lr_or_rl_are_red(self, thisway):
        kid = self[thisway]
        return Node.isred(kid) and Node.isred(kid[not thisway])

    def get_node_with_parent(self, key):
        parent = None
        while self:
            if key == self.key:
                return self, parent

            here = 0 if key < self.key else 1
            self, parent = self[here], self

        return None, parent

    def get(self, key):
        node, _ = self.get_node_with_parent(key)
        return None if node is None else node.val

    def __str__(self):
        return "{}: {}".format(self.key, self.val)


class RedBlackTree:

    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        if self.root is None: return None, None
        return self.root.get_node_with_parent(key)

    def get(self, key):
        if self.root is None: return None
        return self.root.get(key)

    def single_rotate(self, node, thisway):
        top, child = node[2], node[thisway]
        gchild = child[not thisway]

        node[thisway] = gchild
        if gchild: gchild[2] = node

        child[not thisway], node[2] = node, child

        if top:
            child[2], top[0 if node is top[0] else 1] = top, child
        else:
            child[2], self.root = None, child

    def double_rotate(self, node, thisway):
        child, gchild = node[thisway], node[thisway][not thisway]

        child[not thisway] = gchild[thisway]
        if gchild[thisway]: gchild[thisway][2] = child

        gchild[thisway], child[2] = child, gchild
        node[thisway], gchild[2] = gchild, node

        self.single_rotate(node, thisway)

    def put(self, key, val):
        node, parent = self.get_node_with_parent(key)

        if node:
            node.val = val
            return

        if parent is None:
            self.root = Node(key, val, red=False)
            return

        thisway = 0 if key < parent.key else 1
        parent[thisway] = Node(key, val, parent=parent)

        if not parent.red: return

        node = parent[2]

        while node:
            if node.both_kids_are_red():
                for i in range(2): node[i].red = False

                if node is self.root: break

                node.red = True

                node = node[2][2]
                continue

            thisway = 0 if key < node.key else 1
            if node.both_ll_or_rr_are_red(thisway):
                self.single_rotate(node, thisway)
            elif node.both_lr_or_rl_are_red(thisway):
                self.double_rotate(node, thisway)
            else:
                break

            node, child = node[2], node
            node.red, child.red = False, True
            break

    def remove(self, key):
        node, parent = self.get_node_with_parent(key)

        if node is None: return

        if node[0] and node[1]:
            heir, parent = node[0], node

            while heir[1]:
                heir, parent = heir[1], heir

            node.key, node.val = heir.key, heir.val
            node = heir

        if node[0] or node[1]:
            child = node[0] if node[0] else node[1]

            node.key, node.val = child.key, child.val
            for i in range(2): node[i] = None

            child.key, child.val = None, None
            child[2] = None

            for i in range(2): assert child[i] is None

            return

        if node is self.root:
            node.key, node.val = None, None
            self.root = None

            return

        thisway = 0 if node is parent[0] else 1
        thatway = 0 if thisway == 1 else 1

        if node.red:
            node.key, node.val = None, None
            node[2], parent[thisway] = None, None

            for i in range(2): assert node[i] is None

            return

        node, prev, dead = node[2], node, node

        while node:
            thisway = 0 if node[0] is prev else 1
            thatway = 1 if thisway == 0 else 0

            if node[thatway].red:
                self.single_rotate(node, thatway)
                node.red, node[2].red = True, False

            if Node.isred(node[thatway][thisway]):
                self.double_rotate(node, thatway)
                node[2].red, node.red = node.red, False
                break

            if Node.isred(node[thatway][thatway]):
                self.single_rotate(node, thatway)
                node[2][thatway].red = node.red
                break

            node[thatway].red = True

            if node.red:
                node.red = False
                break

            node, prev = node[2], node

        node = dead[2]

        thisway = 0 if dead is node[0] else 1

        dead.key, dead.val = None, None
        node[thisway], dead[2] = None, None

        for i in range(2): assert dead[i] is None
