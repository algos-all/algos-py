def countsort(xs, key = lambda x: x, reverse = False):
    """
    Performs counting sort on the provided list

    Args:
        xs (List[T]): a list of objects to sort
        key (Callable([T], Q)): a function to produce a comparable object
        reverse (bool): True if the sorting order should be reversed, False by default

    Returns:
        The reference to the new list. The new list is sorted.
    """

    N = len(xs)

    if N == 0 or N == 1:
        return xs

    ys, zs = [key(x) for x in xs], list(range(N))

    lower, upper = min(ys), max(ys)
    cs = [0 for i in range(0, upper - lower + 2)]

    for y in ys:
        cs[y - lower + 1] += 1

    for i in range(1, len(cs)):
        cs[i] += cs[i - 1]

    if reverse:
        for i in range(N):
            ci = ys[i] - lower

            zs[N - 1 - cs[ci]] = xs[i]

            cs[ci] += 1
    else:
        for i in range(N):
            ci = ys[i] - lower

            zs[cs[ci]] = xs[i]

            cs[ci] += 1

    return zs
