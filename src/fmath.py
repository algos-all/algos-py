def fcomb(n, k):
    '''
    Compute the number of ways to choose k elements out of a pile of n.

    Use an iterative approach with the multiplicative formula:
    \frac{n!}{k!(n - k)!} =
    \frac{n(n - 1)\dots(n - k + 1)}{k(k-1)\dots(1)} =
    \prod{i = 1}{k}\frac{n + 1 - i}{i}

    Also rely on the symmetry: C_n^k = C_n^{n - k}, so the product can
    be calculated up to min(k, n - k)

    :param n: the size of the pile of elements
    :param k: the number of elements to take from the pile
    :return: the number of ways to choose k elements out of a pile of n
    '''

    # When k out of sensible range, should probably throw an exception.
    # For compatibility with scipy.special.{comb, binom} returns 0 instead.
    if n < 0 or k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1

    total_ways = 1
    for i in range(min(k, n - k)):
        total_ways = total_ways * (n - i) // (i + 1)

    return total_ways


def next_permutation(xs):
    if len(xs) == 0 or len(xs) == 1:
        return xs

    i, j = len(xs) - 2, len(xs) - 1

    while i != -1 and xs[i] >= xs[j]:
        i -= 1
        j -= 1

    if i == -1:
        xs.reverse()

        return

    while j != len(xs) and xs[i] <= xs[j]:
        j += 1

    xs[i], xs[j - 1] = xs[j - 1], xs[i]

    i, j = i + 1, len(xs) - 1

    while i < j:
        xs[i], xs[j] = xs[j], xs[i]
        i += 1
        j -= 1
