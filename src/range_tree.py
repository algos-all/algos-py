"""
Implementation of a one-dimensional Range Tree. [1]

It is also widely known as Range Minimum Query but the problem with
that name is the query function does not *have* to be a minimum. [2]

[1]: https://en.wikipedia.org/wiki/Range_tree
[2]: http://e-maxx-eng.appspot.com/sequences/rmq.html
"""


class RangeTree:

    def __init__(self, xs, f=lambda x: x, g=lambda x, y: x + y):
        """
        :param xs: original list
        :param f:  function applied at the leaves
        :param g:  function to combine range queries (sum, min, etc)
        """

        self.xs = xs
        # TODO: link to or explain the math behind times four
        self.ns = [0 for i in range(4 * len(xs))]

        self.f, self.g = f, g

        if xs: self.init(0, 0, len(xs))

    def init(self, n, fst, lst):
        """
        Helper function to recursively initialize RangeTree instance.

        :param n:   index of the tree node
        :param fst: index of first node in range
        :param lst: one past the index of the last node in range
        """

        if fst + 1 == lst:
            self.ns[n] = self.f(self.xs[fst])
            return

        lchild = 2 * n + 1
        rchild = 2 * n + 2
        mid = (fst + lst) // 2

        self.init(lchild, fst, mid)
        self.init(rchild, mid, lst)

        self.ns[n] = self.g(self.ns[lchild], self.ns[rchild])

    def get(self, lft=0, rgt=None, n=0, fst=0, lst=None):
        """
        Compute the value of some function for the given range.

        :param lft: given index into xs[lft:rgt]
        :param rgt: given past-the-last index into xs[lft:rgt]
        :param n:   index of the current node
        :param fst: current first index in ns[fst:lst]
        :param lst: current past-the-last index into ns[fst:lst]
        :returns: the value of self.g for xs[lft:rgt]
        """
        print(fst, lst, lft, rgt)

        if rgt is None:
            rgt = len(self.xs)

        if lst is None:
            lst = len(self.xs)

        if lft == fst and rgt == lst:
            return self.ns[n]

        lchild = 2 * n + 1
        rchild = 2 * n + 2
        mid = (fst + lst) // 2

        if rgt <= mid:
            return self.get(lft, rgt, lchild, fst, mid)

        if lft >= mid:
            return self.get(lft, rgt, rchild, mid, lst)

        return self.g(
            self.get(lft, mid, lchild, fst, mid),
            self.get(mid, rgt, rchild, mid, lst)
        )
