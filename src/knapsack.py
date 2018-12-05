def knapsack(W, vs, ws):
    """
    Finds the set of items with largest total value within weight limit
    """

    if len(vs) != len(ws):
        raise RuntimeError("Expected vs and ws to have the same length")

    return _knapsack_1(W, vs, ws)


def _knapsack_0(W, vs, ws):
    """
    This is an O(pow(2, n)) inefficient solution that lists all subsets
    """

    value, weight = 0, 0

    for i in range(1, pow(2, len(vs))):

        v, w = 0, 0
        j, k = i, 0

        while j:
            if j % 2:
                v += vs[k]
                w += ws[k]

            k += 1
            j //= 2

            if w > W:
                break

        if value <= v and w <= W:
            value, weight = v, w

    return value


def _knapsack_1(limit, vs, ws):
    """
    This is an O(pow(2, n)) inefficeint solution that uses recursion
    """

    def _knapsack(limit, vs, ws, i):

        if limit == 0 or i == len(vs):
            return 0

        accept, reject = 0, _knapsack(limit, vs, ws, i + 1)

        if ws[i] <= limit:
            accept = vs[i] + _knapsack(limit - ws[i], vs, ws, i + 1)

        return max(accept, reject)

    return _knapsack(limit, vs, ws, 0)


def _knapsack_2(limit, vs, ws):
    """
    This is a DP solution based on the recursive approach
    """

    memory = [[None for _ in range(limit + 1)] for _ in range(len(vs))]

    def _knapsack(limit, vs, ws, i):

        if limit == 0 or i == len(vs):
            return 0

        if memory[i][limit] is not None:
            return memory[i][limit]

        reject = _knapsack(limit, vs, ws, i + 1)
        accept = _knapsack(limit - ws[i], vs, ws, i + 1) + vs[i] if ws[i] <= limit else 0

        memory[i][limit] = max(accept, reject)

        return memory[i][limit]

    return _knapsack(limit, vs, ws, 0)


# def _knapsack_3(limit, vs, ws):
#
#     n = len(vs)
#
#     memory = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]
#
#     for i in range(n):
#
#         for j in range(limit):
#
#             pass
