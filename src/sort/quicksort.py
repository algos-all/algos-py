import random
import operator


def qsort0(xs, key=lambda x: x, reverse=False):
    def qsort(fst, lst):
        if fst >= lst:
            return

        i, j = fst, lst
        pivot = ys[random.randint(fst, lst)]

        while i <= j:
            while cmp(ys[i], pivot):
                i += 1
            while cmp(pivot, ys[j]):
                j -= 1

            if i <= j:
                xs[i], xs[j] = xs[j], xs[i]
                ys[i], ys[j] = ys[j], ys[i]
                i, j = i + 1, j - 1

        qsort(fst, j)
        qsort(i, lst)

    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    qsort(0, len(xs) - 1)


def qsort1(xs, key=lambda x: x, reverse=False):
    def qsort(fst, lst):
        if fst >= lst:
            return

        i, j = fst, lst
        pivot = ys[random.randint(fst, lst)]

        while i < j:
            while cmp(ys[i], pivot):
                i += 1
            while cmp(pivot, ys[j]):
                j -= 1

            if i > j: break

            xs[i], xs[j] = xs[j], xs[i]
            ys[i], ys[j] = ys[j], ys[i]
            i, j = i + 1, j - 1

        qsort(fst, j)
        qsort(i, lst)

    ys = [key(x) for x in xs]
    cmp = operator.gt if reverse else operator.lt

    qsort(0, len(ys) - 1)


def qsort2(xs, key=lambda x: x, reverse=False):
    def qsort(zs):
        if not zs: return zs

        pivot = zs[random.randrange(0, len(zs))]

        xhead = qsort([z for z in zs if cmp(z, pivot)])
        xtail = qsort([z for z in zs if cmp(pivot, z)])

        return xhead + [z[1] for z in zs if z == pivot] + xtail

    cmp = operator.gt if reverse else operator.lt

    return qsort(list(zip([key(x) for x in xs], xs)))


def qsort3(xs, key=lambda x: x, reverse=False):
    """ J. Bentley and D. McIlroy partitioning """

    def qsort(fst, lst):
        if fst >= lst: return

        i, j = fst, lst  # [p, i) are < pivot, (j, q] are > pivot
        p, q = fst, lst  # [fst, p) and (q, lst] are all equal to pivot
        pivot = ys[random.randint(fst, lst)]

        while i <= j:
            while i <= j and cmp(ys[i], pivot):
                if ys[i] == pivot:
                    xs[i], xs[p] = xs[p], xs[i]
                    ys[i], ys[p] = ys[p], ys[i]
                    p += 1
                i += 1
            while i <= j and cmp(pivot, ys[j]):
                if ys[j] == pivot:
                    xs[j], xs[q] = xs[q], xs[j]
                    ys[j], ys[q] = ys[q], ys[j]
                    q -= 1
                j -= 1

            if i <= j:
                xs[i], xs[j] = xs[j], xs[i]
                ys[i], ys[j] = ys[j], ys[i]
                i, j = i + 1, j - 1

        for k in range(fst, p):
            xs[j], xs[k] = xs[k], xs[j]
            ys[j], ys[k] = ys[k], ys[j]
            j -= 1

        for k in range(q + 1, lst + 1):
            xs[i], xs[k] = xs[k], xs[i]
            ys[i], ys[k] = ys[k], ys[i]
            i += 1

        qsort(fst, j)
        qsort(i, lst)

    ys = [key(x) for x in xs]
    cmp = operator.ge if reverse else operator.le

    qsort(0, len(xs) - 1)
