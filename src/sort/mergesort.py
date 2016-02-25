def mergesort0(l):
    if len(l) <= 1: return l

    l1, l2 = mergesort0(l[:len(l) // 2]), mergesort0(l[len(l) // 2:])
    i1, i2 = 0, 0

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            l[i1 + i2], i1 = l1[i1], i1 + 1
        else:
            l[i1 + i2], i2 = l2[i2], i2 + 1

    for i in range(i1, len(l1)):
        l[i + i2] = l1[i]
    for i in range(i2, len(l2)):
        l[i1 + i] = l2[i]

    return l


def mergesort1(xs):
    step = 1

    while step < len(xs):
        for n in range(0, len(xs) - step, 2 * step):
            ls, rs = xs[n : n + step], xs[n + step : n + 2 * step]

            li, ri = 0, 0

            while li < len(ls) and ri < len(rs):
                if ls[li] < rs[ri]:
                    xs[n + li + ri] = ls[li]
                    li += 1
                else:
                    xs[n + li + ri] = rs[ri]
                    ri += 1

            for i in range(li, len(ls)):
                xs[n + i + ri] = ls[i]
            for i in range(ri, len(rs)):
                xs[n + li + i] = rs[i]

        step *= 2


def mergesort2(xs):
    step = 1

    while step < len(xs):
        for n in range(0, len(xs) - step, 2 * step):
            aux = xs[n : n + 2 * step]

            li, ri = 0, step

            while li < step and ri < len(aux):
                if aux[li] < aux[ri]:
                    xs[n + li + ri - step] = aux[li]
                    li += 1
                else:
                    xs[n + li + ri - step] = aux[ri]
                    ri += 1

            for i in range(li, step):
                xs[n + i + ri - step] = aux[i]
            for i in range(ri, len(aux)):
                xs[n + li + i - step] = aux[i]

        step *= 2

