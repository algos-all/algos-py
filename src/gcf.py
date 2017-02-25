def gcf(a, b):
    while b:
        a, b = b, a % b

    return a


def xgcf(a, b):
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s2, s1 = s1 - q * s2, s2
        t2, t1 = t1 - q * t2, t2

    return a, s1, t1
