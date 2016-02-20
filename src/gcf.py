#!/usr/bin/env python3

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

if __name__ == "__main__":
    a, b = 0, 1
    print(a, b, " : ", xgcf(a, b))

    a, b = 6, 3
    print(a, b, " : ", xgcf(a, b))

    a, b = 7, 2
    print(a, b, " : ", xgcf(a, b))
