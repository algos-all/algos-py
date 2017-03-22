import operator


def sink(xs, ys, i, n, reverse=False):
    cmp = operator.gt if reverse else operator.lt

    lchild = 2 * i + 1

    while lchild < n:
        rchild = lchild + 1

        if rchild < n and cmp(ys[rchild], ys[lchild]):
            child = rchild
        else:
            child = lchild

        if not cmp(ys[child], ys[i]):
            break

        xs[child], xs[i] = xs[i], xs[child]
        ys[child], ys[i] = ys[i], ys[child]

        i, lchild = child, 2 * child + 1


def swim(xs, ys, i, reverse=False):
    cmp = operator.gt if reverse else operator.lt

    while i != 0:
        parent = (i - 1) // 2

        if not cmp(ys[i], ys[parent]):
            return

        xs[parent], xs[i] = xs[i], xs[parent]
        ys[parent], ys[i] = ys[i], ys[parent]

        i = parent


def xheapify(xs, ys, reverse=False):
    for i in range(len(xs) // 2, -1, -1):
        sink(xs, ys, i, len(xs), reverse=reverse)


def heapify(xs, key=lambda x: x, reverse=False):
    xheapify(xs, [key(x) for x in xs], reverse=reverse)


def xheapsort(xs, ys, reverse=False):
    for i in range(len(xs) - 1, -1, -1):
        xs[0], xs[i] = xs[i], xs[0]
        ys[0], ys[i] = ys[i], ys[0]

        sink(xs, ys, 0, i, not reverse)


def heapsort(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]

    xheapify(xs, ys, not reverse)

    xheapsort(xs, ys, reverse=reverse)
