def heapsort(l):
    def plunge(l, i, n):
        lchild = 2 * i + 1

        while lchild < n:
            rchild = lchild + 1
            if rchild < n and l[rchild] > l[lchild]:
                child = rchild
            else:
                child = lchild

            if l[i] > l[child]: break

            l[i], l[child] = l[child], l[i]
            i, lchild = child, 2 * child + 1

    for i in range(len(l) // 2, -1, -1):
        plunge(l, i, len(l))

    for i in range(len(l) - 1, -1, -1):
        l[0], l[i] = l[i], l[0]
        plunge(l, 0, i)
