import operator


def selectsort0(xs, key=lambda x: x, reverse=False):
    n, ys = len(xs), [key(x) for x in xs]
    cmp = operator.ge if reverse else operator.le

    for i in range(n - 1):
        a, k = ys[i], i
        for j in range(i + 1, n):
            a, k = (a, k) if cmp(a, ys[j]) else (ys[j], j)

        if not cmp(ys[i], ys[k]):
            ys[i], ys[k] = ys[k], ys[i]
            xs[i], xs[k] = xs[k], xs[i]


def selectsort1(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]
    nxt = max if reverse else min
    cmp = operator.gt if reverse else operator.lt

    for i in range(len(xs) - 1):
        j = i + 1 + ys[i + 1:].index(nxt(ys[i + 1:]))

        if cmp(ys[j], ys[i]):
            xs[i], xs[j] = xs[j], xs[i]
            ys[i], ys[j] = ys[j], ys[i]
