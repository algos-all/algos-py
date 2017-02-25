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

    def get(self, lft, rgt):
        return self.goget(0, 0, len(self.xs), lft, rgt)

    def goget(self, n, fst, lst, lft, rgt):
        if fst == lft and lst == rgt:
            return self.ns[n]

        lchild = 2 * n + 1
        rchild = 2 * n + 2
        mid = (fst + lst) // 2

        if rgt <= mid:
            return self.goget(lchild, fst, mid, lft, rgt)
        if lft >= mid:
            return self.goget(rchild, mid, lst, lft, rgt)

        return self.g(
            self.goget(lchild, fst, mid, lft, mid),
            self.goget(rchild, mid, lst, mid, rgt)
        )
