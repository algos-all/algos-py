def fpow0(x, n):
    '''
    Perform recursive fast exponentiation by squaring.

    :param x: the base to be exponentiated
    :param n: the target power value
    :return: x ^ n
    '''

    if x == 0:
        if n == 0:
            return 1
        elif n > 0:
            return 0
        else:
            raise ZeroDivisionError('Cannot raise 0.0 to a negative power')

    if n < 0:
        return fpow(1 / x, -n)

    if n == 0:
        return 1

    if n == 1:
        return x

    assert n == int(n), 'n must be an integer'

    if n % 2 == 0:
        return fpow0(x * x, n // 2)
    else:
        return x * fpow0(x * x, n // 2)


def fpow1(x, n):
    '''
    Perform iterative fast exponentiation by squaring.

    :param x: the base to be exponentiated
    :param n: the target power value
    :return: x ^ n
    '''

    if x == 0:
        if n == 0:
            return 1
        elif n > 0:
            return 0
        else:
            raise ZeroDivisionError('Cannot raise 0.0 to a negative power')

    if n < 0:
        x = 1 / x
        n = -n

    if n == 0:
        return 1

    y = 1

    while n > 1:
        if n % 2 == 0:
            x = x * x
            n = n // 2
        else:
            y = x * y
            x = x * x
            n = n // 2

    return x * y
