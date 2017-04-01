class RangeTree:

    def __init__(self, xs, f=lambda x: x, g=lambda x, y: x + y):
        self.xs = xs
        self.ns = [0 for i in range(4 * len(xs))]

        self.f, self.g = f, g

        if xs: self.init(0, 0, len(xs))

    def init(self, n, fst, lst):
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
            self.get(lft, rgt, lchild, fst, mid),
            self.get(lft, rgt, rchild, mid, lst)
        )
