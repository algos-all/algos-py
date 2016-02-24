def mergesort0(xs):
    if len(xs) <= 1: return xs

    ls = mergesort0(xs[: len(xs) // 2])
    rs = mergesort0(xs[len(xs) // 2 :])

    li, ri = 0, 0

    while li < len(ls) and ri < len(rs):
        if ls[li] < rs[ri]:
            xs[li + ri] = ls[li]

            li += 1
        else:
            xs[li + ri] = rs[ri]

            ri += 1

    for i in range(li, len(ls)):
        xs[i + ri] = ls[i]
    for i in range(ri, len(rs)):
        xs[li + i] = rs[i]

    return xs


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

