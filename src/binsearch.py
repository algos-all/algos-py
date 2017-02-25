def binsearch0(l, v):
    lo, hi = 0, len(l) - 1

    while lo <= hi:
        i = (lo + hi) // 2
        if l[i] == v:
            return i
        elif v < l[i]:
            hi = i - 1
        elif v > l[i]:
            lo = i + 1

    return None


def binsearch1(l, v):
    lo, hi = 0, len(l)

    while lo < hi:
        i = (lo + hi) // 2
        if v < l[i]:
            hi = i
        elif v > l[i]:
            lo = i + 1
        else:
            return i

    return None
