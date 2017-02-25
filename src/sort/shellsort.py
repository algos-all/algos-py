import operator


def shellsort(xs, key=lambda x: x, reverse=False):
    m, n = 1, len(xs)

    ys = [key(x) for x in xs]
    cmp = operator.ge if reverse else operator.le

    while m < n // 3:
        m = 3 * m + 1

    while m:
        for i in range(m, n):
            for j in range(i, m - 1, -m):
                if cmp(ys[j - m], ys[j]): break

                xs[j], xs[j - m] = xs[j - m], xs[j]
                ys[j], ys[j - m] = ys[j - m], ys[j]
        m //= 3
