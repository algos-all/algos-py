def countsort(xs, key=lambda x: x, reverse=False):
    if len(xs) <= 1:
        return xs

    ys = list(range(len(xs)))
    zs = list(zip([key(x) for x in xs], xs))

    mi, ma = min(zs)[0], max(zs)[0]
    cs = [0 for i in range(0, ma - mi + 2)]

    for z in zs: cs[z[0] - mi + 1] += 1

    for i in range(1, len(cs)):
        cs[i] += cs[i - 1]

    if reverse:
        for z in zs:
            ys[len(ys) - 1 - cs[z[0] - mi]] = z[1]
            cs[z[0] - mi] += 1
    else:
        for z in zs:
            ys[cs[z[0] - mi]] = z[1]
            cs[z[0] - mi] += 1

    return ys
