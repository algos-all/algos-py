"""
Fast exponentiation by squaring
"""


def fpow0(x, n):
    """
    Perform recursive fast exponentiation by squaring.

    :param x: the base number
    :param n: the target power value, an integer
    :return: x to the power of n
    """
    if n < 0:
        return fpow0(1 / x, -n)
    if n == 0:
        return 1
    if x == 0:
        return 0

    assert n == int(n), "n must be an integer"

    return fpow0(x * x, n // 2) if n % 2 == 0 else x * fpow0(x * x, n // 2)


def fpow1(x, n):
    """
    Perform iterative fast exponentiation by squaring.

    :param x: the base number
    :param n: the target power value, an integer
    :return: x to the power of n
    """
    if n < 0:
        return fpow1(1 / x, -n)
    if n == 0:
        return 1
    if x == 0:
        return 0

    y = 1

    while n != 1:
        if n % 2 == 0:
            x = x * x
            n = n // 2
        else:
            y = x * y
            x = x * x
            n = n // 2

    return x * y


def fpow2(x, n):
    """
    Perform iterative fast exponentiation by squaring.

    :param x: the base number
    :param n: the target power value, an integer
    :return: x to the power of n
    """
    if n < 0:
        return fpow2(1 / x, -n)
    if n == 0:
        return 1
    if x == 0:
        return 0

    y = 1

    while n != 1:
        if n % 2 == 1:
            y *= x

        x *= x
        n = n // 2

    return y * x
