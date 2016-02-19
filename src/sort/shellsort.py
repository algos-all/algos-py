def shellsort0(xs):
    m, n = 1, len(xs)
    while m < n // 3:
        m = 3 * m + 1
    while m > 0:
        for i in range(m, n):
            for j in range(i, m - 1, -m):
                if xs[j - m] > xs[j]:
                    xs[j - m], xs[j] = xs[j], xs[j - m]
                else:
                    break
        m //= 3

def shellsort1(xs):
    m, n = 1, len(xs)
    while m < n // 3:
        m = 3 * m + 1
    while m > 0:
        for i in range(m, n):
            for j in range(i, m - 1, -m):
                if xs[j - m] <= xs[j]: break

                xs[j - m], xs[j] = xs[j], xs[j - m]
        m //= 3
