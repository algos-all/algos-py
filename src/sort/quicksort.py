import random


def qsort0(xs):
    def qsort(xs, fst, lst):
        if fst >= lst: return

        i, j = fst, lst
        pivot = xs[random.randint(fst, lst)]

        while i <= j:
            while xs[i] < pivot: i += 1
            while xs[j] > pivot: j -= 1
            if i <= j:
                xs[i], xs[j] = xs[j], xs[i]
                i, j = i + 1, j - 1
        qsort(xs, fst, j)
        qsort(xs, i, lst)
    qsort(xs, 0, len(xs) - 1)


def qsort1(xs):
    def qsort(xs, fst, lst):
        if fst >= lst: return

        i, j = fst, lst
        pivot = xs[random.randint(fst, lst)]

        while i < j:
            while xs[i] < pivot: i += 1
            while xs[j] > pivot: j -= 1

            if i > j: break

            xs[i], xs[j] = xs[j], xs[i]
            i, j = i + 1, j - 1

        qsort(xs, fst, j)
        qsort(xs, i, lst)

    qsort(xs, 0, len(xs) - 1)


def qsort2(xs):
    def qsort(xs):
        if not xs: return xs

        pivot = xs[random.randrange(0, len(xs))]
        xhead = qsort([el for el in xs if el < pivot])
        xtail = qsort([el for el in xs if el > pivot])

        return xhead + [el for el in xs if el == pivot] + xtail

    return qsort(xs)


def qsort3(xs):
    """ J. Bentley and D. McIlroy partitioning """

    def qsort(xs, fst, lst):
        if fst >= lst: return

        i, j = fst, lst # [p, i) are < pivot, (j, q] are > pivot
        p, q = fst, lst # [fst, p) and (q, lst] are all equal to pivot
        pivot = xs[random.randint(fst, lst)]

        while i <= j:
            while i <= j and xs[i] <= pivot:
                if xs[i] == pivot:
                    xs[i], xs[p] = xs[p], xs[i]
                    p += 1
                i += 1
            while i <= j and xs[j] >= pivot:
                if xs[j] == pivot:
                    xs[j], xs[q] = xs[q], xs[j]
                    q -= 1
                j -= 1

            if i <= j:
                xs[i], xs[j] = xs[j], xs[i]
                i, j = i + 1, j - 1

        for k in range(fst, p):
            xs[j], xs[k] = xs[k], xs[j]
            j -= 1

        for k in range(q + 1, lst + 1):
            xs[i], xs[k] = xs[k], xs[i]
            i += 1

        qsort(xs, fst, j)
        qsort(xs, i, lst)

    qsort(xs, 0, len(xs) - 1)
