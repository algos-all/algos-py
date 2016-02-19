def countsort0(xs):
    if not xs: return xs
    lo, hi = min(xs), max(xs) + 1

    def csort(xs, lo, hi):
        counts = [0 for i in range(hi - lo)]
        for i in xs:
            counts[i - lo] += 1
        return [i + lo for i, j in enumerate(counts) for k in range(j)]

    return csort(xs, lo, hi)

def countsort1(xs):
    if not xs: return xs
    lo, hi = min(xs), max(xs) + 1

    def csort(xs, lo, hi):
        aux, counts = [0 for i in xs], [0 for i in range(hi - lo + 1)]
        for i in xs:
            counts[i - lo + 1] += 1
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        for i in xs:
            aux[counts[i - lo]] = i
            counts[i - lo] += 1
        return aux

    return csort(xs, lo, hi)
