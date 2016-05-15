def heapsort(xs):
    def plunge(xs, i, n):
        lchild = 2 * i + 1

        while lchild < n:
            rchild = lchild + 1
            if rchild < n and xs[lchild] < xs[rchild]:
                child = rchild
            else:
                child = lchild

            if xs[i] >= xs[child]: break

            xs[i], xs[child] = xs[child], xs[i]
            i, lchild = child, 2 * child + 1

    for i in range(len(xs) // 2, -1, -1):
        plunge(xs, i, len(xs))

    for i in range(len(xs) - 1, -1, -1):
        xs[0], xs[i] = xs[i], xs[0]
        plunge(xs, 0, i)
