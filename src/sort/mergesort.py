import operator


def mergesort0(xs, key=lambda x: x, reverse=False):
    if len(xs) <= 1:
        return xs

    def mergesort(zs):
        if len(zs) <= 1:
            return zs

        ls = mergesort(zs[: len(zs) // 2])
        rs = mergesort(zs[len(zs) // 2:])

        li, ri = 0, 0

        while li < len(ls) and ri < len(rs):
            if cmp(ls[li], rs[ri]):
                zs[li + ri] = ls[li]

                li += 1
            else:
                zs[li + ri] = rs[ri]

                ri += 1

        for i in range(li, len(ls)):
            zs[i + ri] = ls[i]
        for i in range(ri, len(rs)):
            zs[li + i] = rs[i]

        return zs

    zs = list(zip([key(x) for x in xs], xs))
    cmp = operator.gt if reverse else operator.lt

    return [z[1] for z in mergesort(zs)]


def mergesort1(xs, key=lambda x: x, reverse=False):
    n, step = len(xs), 1

    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    while step < n:
        for i in range(0, n - step, 2 * step):
            xls, xrs = xs[i: i + step], xs[i + step: i + 2 * step]
            yls, yrs = ys[i: i + step], ys[i + step: i + 2 * step]

            li, ri = 0, 0
            ln, rn = len(yls), len(yrs)
            while li < len(yls) and ri < len(yrs):
                if cmp(yls[li], yrs[ri]):
                    xs[i + li + ri] = xls[li]
                    ys[i + li + ri] = yls[li]
                    li += 1
                else:
                    xs[i + li + ri] = xrs[ri]
                    ys[i + li + ri] = yrs[ri]
                    ri += 1

            if li != ln:
                xs[i + li + ri: i + ln + ri] = xls[li:]
                ys[i + li + ri: i + ln + ri] = yls[li:]

            if ri != rn:
                xs[i + li + ri: i + li + rn] = xrs[ri:]
                ys[i + li + ri: i + li + rn] = yrs[ri:]

        step *= 2


def mergesort2(xs, key=lambda x: x, reverse=False):
    n, step = len(xs), 1

    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    while step < n:
        for i in range(0, len(xs) - step, 2 * step):
            xaux = xs[i: i + 2 * step]
            yaux = ys[i: i + 2 * step]

            li, ri = 0, step

            while li < step and ri < len(yaux):
                if cmp(yaux[li], yaux[ri]):
                    xs[i + li + ri - step] = xaux[li]
                    ys[i + li + ri - step] = yaux[li]
                    li += 1
                else:
                    xs[i + li + ri - step] = xaux[ri]
                    ys[i + li + ri - step] = yaux[ri]
                    ri += 1

            for j in range(li, step):
                xs[i + j + ri - step] = xaux[j]
                ys[i + j + ri - step] = yaux[j]
            for j in range(ri, len(yaux)):
                xs[i + li + j - step] = xaux[j]
                xs[i + li + j - step] = yaux[j]

        step *= 2
