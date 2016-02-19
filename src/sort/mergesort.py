def mergesort0(l):
    if len(l) <= 1: return l

    l1, l2 = mergesort0(l[:len(l) // 2]), mergesort0(l[len(l) // 2:])
    i1, i2 = 0, 0

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            l[i1 + i2], i1 = l1[i1], i1 + 1
        else:
            l[i1 + i2], i2 = l2[i2], i2 + 1

    for i in range(i1, len(l1)):
        l[i + i2] = l1[i]
    for i in range(i2, len(l2)):
        l[i1 + i] = l2[i]

    return l


def mergesort1(l):
    n, step = len(l), 1
    while step < n:
        for i in range(0, n, 2 * step):
            i1, i2 = i, min(i + step, n)
            n1, n2 = i2, min(i + 2 * step, n)

            aux = l[i1 : n2]

            j = i
            i1, i2 = i1 - i, i2 - i
            n1, n2 = n1 - i, n2 - i

            while i1 < n1 and i2 < n2:
                if aux[i1] < aux[i2]:
                    l[j], i1 = aux[i1], i1 + 1
                else:
                    l[j], i2 = aux[i2], i2 + 1
                j += 1

            for k in range(i1, n1):
                l[j], j = aux[k], j + 1

            for k in range(i2, n2):
                l[j], j = aux[k], j + 1

        step *= 2


def mergesort2(l):
    n, step = len(l), 1
    while step < n:
        for offset in range(0, n, 2 * step):
            i1, i2 = offset, min(offset + step, n)
            n1, n2 = i2, min(offset + 2 * step, n)

            aux1, aux2 = l[i1 : n1], l[i2 : n2]

            i, i1, i2 = offset, 0, 0
            while i1 < len(aux1) and i2 < len(aux2):
                if aux1[i1] < aux2[i2]:
                    l[i], i1 = aux1[i1], i1 + 1
                else:
                    l[i], i2 = aux2[i2], i2 + 1
                i += 1

            for k in range(i1, len(aux1)):
                l[i], i = aux1[k], i + 1

            for k in range(i2, len(aux2)):
                l[i], i = aux2[k], i + 1

        step *= 2
