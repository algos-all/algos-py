class Node:
    def __init__(self, key, val, red=True, parent=None):
        self.key, self.val = key, val
        self.edges = [None, None, parent]

        self.red = red

    @staticmethod
    def isred(node):
        return node and node.red

    def both_kids_are_red(self):
        return Node.isred(self.edges[0]) and Node.isred(self.edges[1])

    def both_ll_or_rr_are_red(self, thisway):
        kid = self.edges[thisway]
        return Node.isred(kid) and Node.isred(kid.edges[thisway])

    def both_lr_or_rl_are_red(self, thisway):
        kid = self.edges[thisway]
        return Node.isred(kid) and Node.isred(kid.edges[not thisway])

    def get_node_with_parent(self, key):
        parent = None
        while self:
            if key == self.key:
                return self, parent

            here = 0 if key < self.key else 1
            self, parent = self.edges[here], self

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
        top, child = node.edges[2], node.edges[thisway]
        gchild = child.edges[not thisway]

        node.edges[thisway] = gchild
        if gchild: gchild.edges[2] = node

        child.edges[2] = top
        child.edges[not thisway], node.edges[2] = node, child

        if top:
            here = 0 if node is top.edges[0] else 1
            top.edges[here] = child
        else:
            self.root = child

    def double_rotate(self, node, thisway):
        child = node.edges[thisway]
        gchild = child.edges[not thisway]

        child.edges[not thisway] = gchild.edges[thisway]
        if gchild.edges[thisway]:
            gchild.edges[thisway].edges[2] = child

        gchild.edges[thisway], child.edges[2] = child, gchild
        node.edges[thisway], gchild.edges[2] = gchild, node

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
        parent.edges[thisway] = Node(key, val, parent=parent)

        if not parent.red: return

        node = parent.edges[2]

        while node:
            if node.both_kids_are_red():
                for i in range(2): node.edges[i].red = False

                if node is self.root: break

                node.red = True

                node = node.edges[2].edges[2]
                continue

            thisway = 0 if key < node.key else 1
            if node.both_ll_or_rr_are_red(thisway):
                self.single_rotate(node, thisway)
            elif node.both_lr_or_rl_are_red(thisway):
                self.double_rotate(node, thisway)
            else:
                break

            node, child = node.edges[2], node
            node.red, child.red = False, True
            break

    def remove(self, key):
        node, parent = self.get_node_with_parent(key)

        if node is None: return

        if node.edges[0] and node.edges[1]:
            heir, parent = node.edges[0], node

            while heir.edges[1]:
                heir, parent = heir.edges[1], heir

            node.key, node.val = heir.key, heir.val
            node = heir

        if node.edges[0] or node.edges[1]:
            child = node.edges[0] if node.edges[0] else node.edges[1]

            node.key, node.val = child.key, child.val
            for i in range(2): node.edges[i] = None

            child.key, child.val = None, None
            child.edges[2] = None

            for i in range(2): assert child.edges[i] is None

            return

        if node is self.root:
            node.key, node.val = None, None
            self.root = None

            return

        thisway = 0 if node is parent.edges[0] else 1
        thatway = 0 if thisway == 1 else 1

        if node.red:
            node.key, node.val = None, None
            node.edges[2], parent.edges[thisway] = None, None

            for i in range(2): assert node.edges[i] is None

            return

        node, prev, dead = node.edges[2], node, node

        while node:
            thisway = 0 if node.edges[0] is prev else 1
            thatway = 1 if thisway == 0 else 0

            if node.edges[thatway].red:
                self.single_rotate(node, thatway)
                node.red, node.edges[2].red = True, False

            if Node.isred(node.edges[thatway].edges[thisway]):
                self.double_rotate(node, thatway)
                node.edges[2].red, node.red = node.red, False
                break

            if Node.isred(node.edges[thatway].edges[thatway]):
                self.single_rotate(node, thatway)
                node.edges[2].edges[thatway].red = node.red
                break

            node.edges[thatway].red = True

            if node.red:
                node.red = False
                break

            node, prev = node.edges[2], node

        node = dead.edges[2]

        thisway = 0 if dead is node.edges[0] else 1

        dead.key, dead.val = None, None
        node.edges[thisway], dead.edges[2] = None, None

        for i in range(2): assert dead.edges[i] is None
