#!/usr/bin/env python3
# http://goo.gl/PMph4W


def sufar_baseline(txt):
    return [
        s[1] for s in sorted([(txt[i:], i) for i in range(len(txt))])
    ]


def sufar(txt):
    txt = txt + chr(0)
    N, tokens = len(txt), sorted(set(txt))

    equivalence = {t: i for i, t in enumerate(tokens)}
    cls, res, n = [equivalence[t] for t in txt], [(0, 0, 0)], 1

    while n < N:
        res = sorted((cls[i], cls[(i + n) % N], i) for i in range(N))

        cls[res[0][2]] = 0
        for i in range(1, N):
            cls[res[i][2]] = cls[res[i - 1][2]]
            if res[i][0:2] != res[i - 1][0:2]:
                cls[res[i][2]] += 1

        n *= 2

    return [r[2] for r in res][1:]
