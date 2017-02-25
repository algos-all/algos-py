import operator


def heapsort(xs, key=lambda x: x, reverse=False):
    def plunge(i, n):
        lchild = 2 * i + 1

        while lchild < n:
            rchild = lchild + 1
            if rchild < n and cmp(ys[lchild], ys[rchild]):
                child = rchild
            else:
                child = lchild

            if cmp(ys[child], ys[i]): break

            xs[i], xs[child] = xs[child], xs[i]
            ys[i], ys[child] = ys[child], ys[i]
            i, lchild = child, 2 * child + 1

    n = len(xs)
    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    for i in range(n // 2, -1, -1):
        plunge(i, n)

    for i in range(n - 1, -1, -1):
        xs[0], xs[i] = xs[i], xs[0]
        ys[0], ys[i] = ys[i], ys[0]
        plunge(0, i)
