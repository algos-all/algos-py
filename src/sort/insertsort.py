import operator


def insertsort0(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]
    cmp = operator.ge if reverse else operator.le

    for i in range(1, len(xs)):
        for j in range(i, 0, -1):
            if cmp(ys[j - 1], ys[j]): break

            xs[j - 1], xs[j] = xs[j], xs[j - 1]
            ys[j - 1], ys[j] = ys[j], ys[j - 1]


def insertsort1(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    for i in range(1, len(xs)):
        for j in range(i, 0, -1):
            if cmp(ys[j], ys[j - 1]):
                xs[j - 1], xs[j] = xs[j], xs[j - 1]
                ys[j - 1], ys[j] = ys[j], ys[j - 1]
            else:
                break


def insertsort2(xs, key=lambda x: x, reverse=False):
    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    for i in range(1, len(xs)):
        j = i
        while j and cmp(xs[j], xs[j - 1]):
            xs[j], xs[j - 1] = xs[j - 1], xs[j]
            ys[j], ys[j - 1] = ys[j - 1], ys[j]
            j -= 1
