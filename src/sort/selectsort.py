import operator


def selectsort0(xs, key=lambda x: x, reverse=False):
    n = len(xs)
    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    for i in range(n - 1):
        for j in range(i + 1, n):
            if cmp(ys[j], ys[i]):
                xs[i], xs[j] = xs[j], xs[i]
                ys[i], ys[j] = ys[j], ys[i]

def selectsort1(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]
    nxt = max if reverse else min
    cmp = operator.gt if reverse else operator.lt

    for i in range(len(xs) - 1):
        j = i + 1 + ys[i + 1:].index(nxt(ys[i + 1:]))

        if cmp(ys[j], ys[i]):
            xs[i], xs[j] = xs[j], xs[i]
            ys[i], ys[j] = ys[j], ys[i]
