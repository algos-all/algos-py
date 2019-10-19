def build_powerset_0(xs):

    powerset = [[]]

    for x in xs:
        powerset.extend([subset + [x] for subset in powerset])

    return powerset


def build_powerset_1(xs):

    powerset = []

    for i in range(pow(2, len(xs))):

        j, subset = 0, []

        while i:
            if i % 2:
                subset.append(xs[j])

            j += 1
            i //= 2

        powerset.append(subset)

    return powerset
