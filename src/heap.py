#!/usr/bin/env python3

import operator


class Heap:

    def __init__(self, xs=None, key=operator.le):
        self.key = key
        self.xs = [] if xs is None else xs.copy()

        for i in range(len(self) // 2, -1, -1):
            self.sink(self.xs, i, len(self))

    def __len__(self):
        return len(self.xs)

    def __getitem__(self, i):
        return self.xs[i]

    def __setitem__(self, key, val):
        self.xs[key] = val

    def sink(self, xs, i, n):
        lchild = 2 * i + 1
        while lchild < n:
            rchild = lchild + 1

            if rchild < n and not self.key(xs[lchild], xs[rchild]):
                child = rchild
            else:
                child = lchild

            if self.key(xs[i], xs[child]): break

            xs[i], xs[child] = xs[child], xs[i]
            i, lchild = child, 2 * child + 1

    def swim(self, i):
        while i:
            parent = (i - 1) // 2
            if self.key(self[parent], self[i]): break

            self[parent], self[i] = self[i], self[parent]
            i = parent

    def push(self, val):
        self.xs.append(val)
        self.swim(len(self) - 1)

    def pop(self):
        el = self.xs.pop()

        if not self: return el

        el, self[0] = self[0], el
        self.sink(self.xs, 0, len(self))

        return el

    def sort(self):
        ys = self.xs.copy()

        for i in range(len(ys) - 1, -1, -1):
            ys[0], ys[i] = ys[i], ys[0]
            self.sink(ys, 0, i)

        return ys
