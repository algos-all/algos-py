import random

from src.rbt import Node, RedBlackTree


class TestRedBlackTree:
    def check_contents(self, tree, keys2vals):
        for key in keys2vals:
            assert tree.get(key) == keys2vals[key], \
            "{}: {} != {}".format(key, tree.get(key), keys2vals[key])

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

    def check_depth(self, tree, msg=""):
        depths = []

        def traverse(node, depth=1):
            if node.edges[0]:
                traverse(node.edges[0], depth + 1)
            if node.edges[1]:
                traverse(node.edges[1], depth + 1)

            if node.edges[0] is None and node.edges[1] is None:
                depths.append(depth)

        if tree.root:
            traverse(tree.root)
        else:
            depths.append(0)

        assert 2 * min(depths) >= max(depths), \
            "min {} and max {}".format(min(depths), max(depths)) + msg

    def check_color(self, tree):
        def check_node(node):
            for i in range(2):
                if node.red and Node.isred(node.edges[i]):
                    assert False, "{}, to {}".format(node.key, i)

            for i in range(2):
                if node.edges[i]:
                    check_node(node.edges[i])

        if tree.root:
            assert tree.root.red is False
            check_node(tree.root)

    def check_links(self, tree):
        def check_link(node):
            for i in range(2):
                if node.edges[i]:
                    assert node.edges[i].edges[2] is node

                    check_link(node.edges[i])

        if tree.root:
            assert tree.root.edges[2] is None
            check_link(tree.root)

    def test_get_empty(self):
        tree = RedBlackTree()

        for i in range(-10, 10):
            assert tree.get(i) is None

    def test_both_kids_are_red(self):
        tree = RedBlackTree()

        tree.put(3, 3)
        tree.put(2, 2)
        tree.put(4, 4)
        tree.put(1, 1)

        assert tree.root
        assert tree.root.edges[0]
        assert tree.root.edges[1]

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)


    def test_single_rotate_left_left_on_root(self):
        tree = RedBlackTree()

        tree.put(2, 2)
        assert tree.get(2) == 2

        assert tree.root
        assert tree.root.key == 2
        assert tree.root.val == 2
        assert tree.root.red is False

        tree.put(1, 1)
        assert tree.get(2) == 2
        assert tree.get(1) == 1

        assert tree.root
        assert tree.root.key == 2
        assert tree.root.val == 2
        assert tree.root.red is False

        assert tree.root.edges[0]
        assert tree.root.edges[0].key == 1
        assert tree.root.edges[0].val == 1
        assert tree.root.edges[0].red is True

        tree.put(0, 0)
        assert tree.get(2) == 2
        assert tree.get(1) == 1
        assert tree.get(0) == 0

        assert tree.root
        assert tree.root.key == 1
        assert tree.root.val == 1
        assert tree.root.red is False

        assert tree.root.edges[0]
        assert tree.root.edges[0].key == 0
        assert tree.root.edges[0].val == 0
        assert tree.root.edges[0].red is True, \
            "under some implementations this may be False"

        assert tree.root.edges[1]
        assert tree.root.edges[1].key == 2
        assert tree.root.edges[1].val == 2
        assert tree.root.edges[1].red is True, \
            "under some implementations this may be False"

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

    def test_single_rotate_right_right_on_root(self):
        tree = RedBlackTree()

        tree.put(0, 0)
        assert tree.get(0) == 0

        assert tree.root
        assert tree.root.key == 0
        assert tree.root.val == 0
        assert tree.root.red is False

        tree.put(1, 1)
        assert tree.get(0) == 0
        assert tree.get(1) == 1

        assert tree.root
        assert tree.root.key == 0
        assert tree.root.val == 0
        assert tree.root.red is False

        assert tree.root.edges[1]
        assert tree.root.edges[1].key == 1
        assert tree.root.edges[1].val == 1
        assert tree.root.edges[1].red is True

        tree.put(2, 2)
        assert tree.get(0) == 0
        assert tree.get(1) == 1
        assert tree.get(2) == 2

        assert tree.root
        assert tree.root.key == 1
        assert tree.root.val == 1
        assert tree.root.red is False

        assert tree.root.edges[0]
        assert tree.root.edges[0].key == 0
        assert tree.root.edges[0].val == 0
        assert tree.root.edges[0].red is True, \
            "under some implementations this may be False"

        assert tree.root.edges[1]
        assert tree.root.edges[1].key == 2
        assert tree.root.edges[1].val == 2
        assert tree.root.edges[1].red is True, \
            "under some implementations this may be False"

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

    def test_double_rotate_left_right_on_root(self):
        tree = RedBlackTree()

        tree.put(5, 5)
        assert tree.get(5) == 5

        tree.put(3, 3)
        assert tree.get(5) == 5
        assert tree.get(3) == 3

        tree.put(4, 4)
        assert tree.get(5) == 5
        assert tree.get(4) == 4
        assert tree.get(3) == 3

        assert tree.root
        assert tree.root.key == 4
        assert tree.root.val == 4
        assert tree.root.red is False

        assert tree.root.edges[0]
        assert tree.root.edges[0].key == 3
        assert tree.root.edges[0].val == 3
        assert tree.root.edges[0].red is True

        assert tree.root.edges[1]
        assert tree.root.edges[1].key == 5
        assert tree.root.edges[1].val == 5
        assert tree.root.edges[1].red is True

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

    def test_double_rotate_right_left_on_root(self):
        tree = RedBlackTree()

        tree.put(3, 3)
        assert tree.get(3) == 3

        tree.put(5, 5)
        assert tree.get(5) == 5
        assert tree.get(3) == 3

        tree.put(4, 4)
        assert tree.get(5) == 5
        assert tree.get(4) == 4
        assert tree.get(3) == 3

        assert tree.root
        assert tree.root.key == 4
        assert tree.root.val == 4
        assert tree.root.red is False

        assert tree.root.edges[0]
        assert tree.root.edges[0].key == 3
        assert tree.root.edges[0].val == 3
        assert tree.root.edges[0].red is True

        assert tree.root.edges[1]
        assert tree.root.edges[1].key == 5
        assert tree.root.edges[1].val == 5
        assert tree.root.edges[1].red is True

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

    def test_successive_put_get(self):
        N = 1000

        tree = RedBlackTree()
        for i in range(0, N):
            tree.put(i, i)
            for j in range(0, i):
                assert tree.get(j) == j, \
                    "{} != {} at {}".format(tree.get(j), j, i)

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree, " at step {}".format(i))

        tree = RedBlackTree()
        for i in range(N, 0, -1):
            tree.put(i, i)
            for j in range(N, i - 1, -1):
                assert tree.get(j) == j, \
                    "{} != {} at {}".format(tree.get(j), j, i)

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree, " at step {}".format(N - i))

    def test_put_get_n_elements(self):
        random.seed(0)

        lo, hi = -2 ** 10, 2 ** 10

        for i in range(1000):
            keys2vals = {}
            tree = RedBlackTree()

            N = 1000

            for i in range(N):
                key = random.randint(lo, hi)
                val = random.randint(lo, hi)

                keys2vals[key] = val
                tree.put(key, val)

            self.check_contents(tree, keys2vals)

            for i in range(N):
                key = random.randint(lo, hi)
                val = random.randint(lo, hi)

                if key not in keys2vals:
                    assert tree.get(key) is None

    def test_remove_empty(self):
        tree = RedBlackTree()

        for i in range(-10, 10):
            assert tree.remove(i) is None

    def test_remove_root(self):
        tree = RedBlackTree()

        tree.put(42, 42)

        assert tree.root
        assert tree.root.key == 42
        assert tree.root.val == 42
        for i in range(3):
            assert tree.root.edges[i] is None

        tree.remove(42)

        assert tree.root is None

    def test_remove_red_rgt(self):
        tree = RedBlackTree()

        tree.put(1, 1)
        tree.put(2, 2)

        tree.remove(2)

        assert tree.get(1) == 1
        assert tree.get(2) is None
        assert tree.root.red is False

    def test_remove_red_lft(self):
        tree = RedBlackTree()

        tree.put(3, 3)
        tree.put(2, 2)

        tree.remove(2)

        assert tree.get(3) == 3
        assert tree.get(2) is None
        assert tree.root.red is False

    def test_remove_root_with_rgt(self):
        tree = RedBlackTree()

        tree.put(2, 2)
        tree.put(3, 3)

        tree.remove(2)

        assert tree.get(2) is None
        assert tree.get(3) == 3
        assert tree.root.red is False

    def test_remove_root_with_lft(self):
        tree = RedBlackTree()

        tree.put(3, 3)
        tree.put(2, 2)

        tree.remove(3)

        assert tree.get(2) == 2
        assert tree.get(3) is None
        assert tree.root.red is False

    def test_put_remove_n_elements(self):
        random.seed(0)

        lo, hi = -2 ** 10, 2 ** 10

        for i in range(1000):
            keys2vals = {}
            tree = RedBlackTree()

            N = 1000

            for i in range(N):
                key = random.randint(lo, hi)
                val = random.randint(lo, hi)

                keys2vals[key] = val
                tree.put(key, val)

            self.check_contents(tree, keys2vals)

            for key in list(keys2vals.keys())[: N // 2]:
                keys2vals.pop(key)
                tree.remove(key)

            self.check_contents(tree, keys2vals)

    def test_remove_root_with_children(self):
        tree = RedBlackTree()

        tree.put(2, 2)
        tree.put(1, 1)
        tree.put(3, 3)

        assert tree.root and tree.root.key == 2
        assert tree.root.edges[0] and tree.root.edges[0].key == 1
        assert tree.root.edges[1] and tree.root.edges[1].key == 3

        tree.remove(2)

        assert tree.get(1) == 1
        assert tree.get(2) is None
        assert tree.get(3) == 3

    def test_remove_r_bb(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(32, 32)
        tree.put(4, 4)
        tree.put(8, 8)
        tree.put(1, 1)
        tree.put(0, 0)

        assert tree.root

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32
        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 8
        assert tree.root.edges[0].edges[0].edges[0].key == 0

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[0].red is False
        assert tree.root.edges[0].edges[1].red is False
        assert tree.root.edges[0].edges[0].edges[0].red is True

        self.check_links(tree)

        tree.remove(0)

        assert tree.root

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32
        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 8

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[0].red is False
        assert tree.root.edges[0].edges[1].red is False

        self.check_links(tree)

        tree.remove(1)

        assert tree.root

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32
        assert tree.root.edges[0].edges[1].key == 8

        assert tree.root.red is False
        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[1].red is True

        self.check_links(tree)

        tree.put(1, 1)
        tree.put(2, 2)

        assert tree.root

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32
        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 8
        assert tree.root.edges[0].edges[0].edges[1].key == 2

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[0].red is False
        assert tree.root.edges[0].edges[1].red is False
        assert tree.root.edges[0].edges[0].edges[1].red is True

        self.check_links(tree)

        tree.remove(2)
        tree.remove(8)

        assert tree.root

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32
        assert tree.root.edges[0].edges[0].key == 1

        assert tree.root.red is False
        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[0].red is True

        self.check_links(tree)

    def test_remove_b_bb_00r0(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(8, 8)
        tree.put(64, 64)
        tree.put(32, 32)

        tree.remove(8)

        assert tree.root
        assert tree.root.key == 32
        assert tree.root.edges[0] and tree.root.edges[0].key == 16
        assert tree.root.edges[1] and tree.root.edges[1].key == 64

        self.check_links(tree)
        self.check_color(tree)

        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False

    def test_remove_b_bb_0r00(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(4, 4)
        tree.put(32, 32)
        tree.put(8, 8)

        tree.remove(32)

        assert tree.root
        assert tree.root.key == 8
        assert tree.root.edges[0] and tree.root.edges[0].key == 4
        assert tree.root.edges[1] and tree.root.edges[1].key == 16

        self.check_links(tree)
        self.check_color(tree)

        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False

    def test_remove_b_bb_00rr(self):
        tree = RedBlackTree()

        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(4, 4)
        tree.put(2, 2)
        tree.put(8, 8)

        tree.remove(0)

        assert tree.root
        assert tree.root.key == 2
        assert tree.root.edges[0] and tree.root.edges[0].key == 1
        assert tree.root.edges[1] and tree.root.edges[1].key == 4
        assert tree.root.edges[1].edges[1] \
            and tree.root.edges[1].edges[1].key == 8

        assert tree.root.red is False
        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False
        assert tree.root.edges[1].edges[1].red is True

        self.check_links(tree)

    def test_remove_b_bb_rr00(self):
        tree = RedBlackTree()

        tree.put(4, 4)
        tree.put(8, 8)
        tree.put(1, 1)
        tree.put(2, 2)
        tree.put(0, 0)

        tree.remove(8)

        assert tree.root
        assert tree.root.edges[0]
        assert tree.root.edges[1]
        assert tree.root.edges[0].edges[0]

        for i in range(2): tree.root.edges[0].edges[i] is None
        tree.root.edges[0].edges[1] is None

        assert tree.root.key == 2
        assert tree.root.edges[0].key == 1
        assert tree.root.edges[1].key == 4
        assert tree.root.edges[0].edges[0].key == 0

        assert tree.root.red is False
        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is False
        assert tree.root.edges[0].edges[0].red is True

        self.check_links(tree)

    def test_remove_b_bb_000r(self):
        tree = RedBlackTree()

        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(2, 2)
        tree.put(4, 4)

        tree.remove(0)

        assert tree.root
        assert tree.root.edges[0]
        assert tree.root.edges[1]
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j] is None, (i, j)

        assert tree.root.key == 2
        assert tree.root.edges[0].key == 1
        assert tree.root.edges[1].key == 4

        assert tree.root.red is False
        for i in range(2):
            assert tree.root.edges[i].red is False

        self.check_links(tree)

    def test_remove_b_bb_r000(self):
        tree = RedBlackTree()

        tree.put(2, 2)
        tree.put(4, 4)
        tree.put(1, 1)
        tree.put(0, 0)

        tree.remove(4)

        assert tree.root
        assert tree.root.edges[0]
        assert tree.root.edges[1]
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j] is None, (i, j)

        assert tree.root.key == 1
        assert tree.root.edges[0].key == 0
        assert tree.root.edges[1].key == 2

        assert tree.root.red is False
        for i in range(2):
            assert tree.root.edges[i].red is False

        self.check_links(tree)

    def test_remove_b_rb_bb00_00r0(self):
        tree = RedBlackTree()

        tree.put(8, 8)
        tree.put(16, 16)
        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(4, 4)
        tree.put(2, 2)

        tree.remove(0)

        assert tree.root
        for i in range(2): assert tree.root.edges[i]
        for i in range(2): assert tree.root.edges[0].edges[i]
        for i in range(2): assert tree.root.edges[1].edges[i] is None
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[0].edges[i].edges[j] is None

        assert tree.root.key

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False
        for i in range(2):
            assert tree.root.edges[0].edges[i].red is False

        self.check_links(tree)

    def test_remove_b_rb_bb00_0r00(self):
        tree = RedBlackTree()

        tree.put(8, 8)
        tree.put(16, 16)
        tree.put(2, 2)
        tree.put(4, 4)
        tree.put(0, 0)
        tree.put(1, 1)

        tree.remove(4)

        assert tree.root
        for i in range(2): assert tree.root.edges[i]
        for i in range(2): assert tree.root.edges[0].edges[i]
        for i in range(2): assert tree.root.edges[1].edges[i] is None
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[0].edges[i].edges[j] is None

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False
        for i in range(2):
            assert tree.root.edges[0].edges[i].red is False

        self.check_links(tree)

    def test_remove_b_rb_bb00_00rr(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(32, 32)
        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(4, 4)
        tree.put(2, 2)
        tree.put(8, 8)

        tree.remove(0)

        assert tree.root
        for i in range(2): assert tree.root.edges[i]

        for i in range(2): assert tree.root.edges[0].edges[i]
        for i in range(2): assert tree.root.edges[1].edges[i] is None

        for i in range(2):
            assert tree.root.edges[0].edges[0].edges[i] is None
        assert tree.root.edges[0].edges[1].edges[0] is None
        assert tree.root.edges[0].edges[1].edges[1]

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is False
        assert tree.root.edges[0].edges[1].edges[1].red is True

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 2
        assert tree.root.edges[1].key == 32

        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 4
        assert tree.root.edges[0].edges[1].edges[1].key == 8

        self.check_links(tree)

    def test_remove_b_rb_bb00_rr00(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(32, 32)
        tree.put(4, 4)
        tree.put(8, 8)
        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(2, 2)

        tree.remove(8)

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is False
        assert tree.root.edges[0].edges[0].edges[0].red is True

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 2
        assert tree.root.edges[1].key == 32

        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 4
        assert tree.root.edges[0].edges[0].edges[0].key == 0

        self.check_links(tree)

    def test_remove_b_rb_bb00_000r(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(32, 32)
        tree.put(1, 1)
        tree.put(0, 0)
        tree.put(4, 4)
        tree.put(8, 8)

        tree.remove(0)

        assert tree.root
        for i in range(2):
            assert tree.root.edges[i]

        for i in range(2):
            assert tree.root.edges[0].edges[i]
        for i in range(2):
            assert tree.root.edges[1].edges[i] is None

        for i in range(2):
            for j in range(2):
                assert tree.root.edges[0].edges[i].edges[j] is None

        assert tree.root.red is False
        for i in range(2):
            assert tree.root.edges[i].red is False

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is True

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 4
        assert tree.root.edges[1].key == 32

        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 8

        self.check_links(tree)

    def test_remove_b_rb_bb00_r000(self):
        tree = RedBlackTree()

        tree.put(16, 16)
        tree.put(32, 32)
        tree.put(4, 4)
        tree.put(8, 8)
        tree.put(1, 1)
        tree.put(0, 0)

        tree.remove(8)

        assert tree.root
        for i in range(2):
            assert tree.root.edges[i]

        for i in range(2):
            assert tree.root.edges[0].edges[i]
        for i in range(2):
            assert tree.root.edges[1].edges[i] is None

        for i in range(2):
            for j in range(2):
                assert tree.root.edges[0].edges[i].edges[j] is None

        assert tree.root.red is False
        for i in range(2):
            tree.root.edges[i].red is False

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is True

        assert tree.root.key == 16
        assert tree.root.edges[0].key == 1
        assert tree.root.edges[1].key == 32

        assert tree.root.edges[0].edges[0].key == 0
        assert tree.root.edges[0].edges[1].key == 4

        self.check_links(tree)

    def test_remove_triple_rotation_left(self):
        tree = RedBlackTree()

        tree.put(1, 1)

        tree.put(0, 0)
        tree.put(16, 16)

        tree.put(4, 4)
        tree.put(64, 64)

        tree.put(2, 2)
        tree.put(8, 8)

        tree.put(32, 32)
        tree.put(128, 128)

        tree.remove(0)

        assert tree.root
        for i in range(2): assert tree.root.edges[i]

        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if i == 0 and j == 1 and k == 1:
                        assert tree.root.edges[i].edges[j].edges[k]
                        continue

                    assert tree.root.edges[i].edges[j].edges[k] is None

        assert tree.root.red is False
        assert tree.root.edges[0].red is True
        assert tree.root.edges[1].red is False

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is False

        for i in range(2):
            assert tree.root.edges[1].edges[i].red is True

        assert tree.root.edges[0].edges[1].edges[1].red is True

        assert tree.root.key == 16

        assert tree.root.edges[0].key == 2
        assert tree.root.edges[1].key == 64

        assert tree.root.edges[0].edges[0].key == 1
        assert tree.root.edges[0].edges[1].key == 4
        assert tree.root.edges[1].edges[0].key == 32
        assert tree.root.edges[1].edges[1].key == 128

        assert tree.root.edges[0].edges[1].edges[1].key == 8

        assert tree.get(0) is None

        self.check_links(tree)


    def test_remove_triple_rotation_right(self):
        tree = RedBlackTree()

        tree.put(64, 64)

        tree.put(4, 4)
        tree.put(128, 128)

        tree.put(1, 1)
        tree.put(16, 16)

        tree.put(0, 0)
        tree.put(2, 2)

        tree.put(8, 8)
        tree.put(32, 32)

        tree.remove(128)

        assert tree.root
        for i in range(2): assert tree.root.edges[i]

        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if i == 1 and j == 0 and k == 0:
                        assert tree.root.edges[i].edges[j].edges[k]
                        continue

                    assert tree.root.edges[i].edges[j].edges[k] is None

        assert tree.root.red is False
        assert tree.root.edges[0].red is False
        assert tree.root.edges[1].red is True

        for i in range(2):
            assert tree.root.edges[0].edges[i].red is True

        for i in range(2):
            assert tree.root.edges[1].edges[i].red is False

        assert tree.root.edges[1].edges[0].edges[0].red is True

        assert tree.root.key == 4

        assert tree.root.edges[0].key == 1
        assert tree.root.edges[1].key == 32

        assert tree.root.edges[0].edges[0].key == 0
        assert tree.root.edges[0].edges[1].key == 2
        assert tree.root.edges[1].edges[0].key == 16
        assert tree.root.edges[1].edges[1].key == 64

        assert tree.root.edges[1].edges[0].edges[0].key == 8

        assert tree.get(128) is None

        self.check_links(tree)

    # def test_remove_largest(self):
    #     tree = RedBlackTree()

    #     for N in range(1, 100):

    #         for i in range(N):
    #             tree.put(i, i)

    #         for i in range(N - 1, -1, -1):
    #             tree.remove(i)

    #             self.check_links(tree)
    #             self.check_color(tree)
    #             self.check_depth(tree)

    #             for j in range(i):
    #                 assert tree.get(j) == j, \
    #                     "loosing {} at step {}, {}".format(j, i, N)
    #             for j in range(i, N): assert tree.get(j) is None

    def test_remove_with_child(self):
        tree = RedBlackTree()

        tree.put(4, 4)
        tree.put(1, 1)
        tree.put(8, 8)

        tree.put(0, 0)

        tree.remove(1)

        assert tree.root
        for i in range(2):
            assert tree.root.edges[i]
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j] is None

        assert tree.root.key == 4
        assert tree.root.edges[0].key == 0
        assert tree.root.edges[1].key == 8

        assert tree.root.red is False
        for i in range(2): assert tree.root.edges[i].red is False

        self.check_links(tree)

        tree.put(1, 1)
        tree.remove(0)

        assert tree.root
        for i in range(2):
            assert tree.root.edges[i]
        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j] is None

        assert tree.root.key == 4
        assert tree.root.edges[0].key == 1
        assert tree.root.edges[1].key == 8

        assert tree.root.red is False
        for i in range(2): assert tree.root.edges[i].red is False

    def test_remove_decrease_black_height(self):
        tree = RedBlackTree()

        tree.put(8, 8)
        tree.put(2, 2)
        tree.put(32, 32)
        tree.put(1, 1)
        tree.put(4, 4)
        tree.put(16, 16)
        tree.put(128, 128)
        tree.put(0, 0)
        tree.put(64, 64)
        tree.put(256, 256)
        tree.put(512, 512)

        assert tree.root
        for i in range(2):
            assert tree.root.edges[i]
            assert tree.root.edges[i].red is False

        for i in range(2):
            for j in range(2):
                assert tree.root.edges[i].edges[j]
                if i == 1 and j == 1:
                    assert tree.root.edges[i].edges[j].red is True
                else:
                    assert tree.root.edges[i].edges[j].red is False

        assert tree.root.edges[0].edges[0].edges[0]
        assert tree.root.edges[0].edges[0].edges[0].red is True

        assert tree.root.edges[1].edges[1].edges[0]
        assert tree.root.edges[1].edges[1].edges[0].red is False
        assert tree.root.edges[1].edges[1].edges[1]
        assert tree.root.edges[1].edges[1].edges[1].red is False

        assert tree.root.edges[1].edges[1].edges[1].edges[1]
        assert tree.root.edges[1].edges[1].edges[1].edges[1].red is True

        tree.remove(0)
        tree.remove(1)

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)

        tree.remove(4)

        self.check_links(tree)
        self.check_color(tree)
        self.check_depth(tree)
