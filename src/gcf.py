def gcf(a, b):
    """Compute the greatest common factor of a and b"""

    a = a if a >= 0 else -a
    b = b if b >= 0 else -b

    while b:
        a, b = b, a % b

    return a


def xgcf(a, b):
    """Compute the extended greatest common factor of a and b"""

    a = a if a >= 0 else -a
    b = b if b >= 0 else -b

    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s2, s1 = s1 - q * s2, s2
        t2, t1 = t1 - q * t2, t2

    # Bézout's identity says: s1 * a + t1 * b == gcd(a, b)
    return a, s1, t1
