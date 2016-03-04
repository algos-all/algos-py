def countsort0(xs):
    def csort(xs, mi, ma):
        cs = [0 for i in range(ma - mi + 1)]
        for x in xs:
            cs[x - mi] += 1
        return [i + mi for i, j in enumerate(cs) for k in range(j)]

    return xs if not xs else csort(xs, min(xs), max(xs))

def countsort1(xs):
    def csort(xs, mi, ma):
        ys = [0 for x in xs]
        cs = [0 for i in range(ma - mi + 2)]
        for x in xs:
            cs[x - mi + 1] += 1
        for i in range(1, len(cs)):
            cs[i] += cs[i - 1]
        for x in xs:
            ys[cs[x - mi]] = x
            cs[x - mi] += 1
        return ys

    return xs if not xs else csort(xs, min(xs), max(xs))
