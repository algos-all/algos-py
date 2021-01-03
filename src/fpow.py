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

    if x == 0:
        if n == 0:
            return 1
        if n > 0:
            return 0

        raise ZeroDivisionError("Cannot raise 0.0 to a negative power")

    if n == 0:
        return 1

    if n == 1:
        return x

    if n < 0:
        return fpow0(1 / x, -n)

    assert n == int(n), "n must be an integer"

    return fpow0(x * x, n // 2) if n % 2 == 0 else x * fpow0(x * x, n // 2)


def fpow1(x, n):
    """
    Perform iterative fast exponentiation by squaring.

    :param x: the base number
    :param n: the target power value, an integer
    :return: x to the power of n
    """

    if x == 0:
        if n == 0:
            return 1
        if n > 0:
            return 0

        raise ZeroDivisionError("Cannot raise 0.0 to a negative power")

    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

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

    if x == 0:
        if n == 0:
            return 1
        if n > 0:
            return 0

        raise ZeroDivisionError('Cannot raise 0.0 to a negative power')

    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    y = 1

    while n != 1:
        if n % 2 == 1:
            y *= x

        x *= x
        n = n // 2

    return y * x
