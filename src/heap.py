from src.sort.heapsort import swim, sink, xheapify, xheapsort


class Heap:

    def __init__(self, xs=None, key=lambda x: x, reverse=False):
        self.xs = [] if xs is None else [x for x in xs]
        self.ys = [] if xs is None else [key(x) for x in xs]

        xheapify(self.xs, self.ys, reverse=reverse)

        self.key = key
        self.reverse = reverse

    def __len__(self):
        return len(self.xs)

    def __getitem__(self, i):
        return self.xs[i]

    def __setitem__(self, key, val):
        self.xs[key] = val
        self.ys[key] = self.key(val)

    def append(self, val):
        self.xs.append(val)
        self.ys.append(self.key(val))

        swim(self.xs, self.ys, len(self.xs) - 1, self.reverse)

    def pop(self):
        x = self.xs.pop()
        y = self.ys.pop()

        if not self.xs:
            return x

        self.xs[0], x = x, self.xs[0]
        self.ys[0], y = y, self.ys[0]

        sink(self.xs, self.ys, 0, len(self.xs), self.reverse)

        return x

    def sort(self, key=lambda x: x, reverse=False):
        if reverse is self.reverse:
            raise RuntimeError("Cannot sort if heap has same reverse")

        xheapsort(self.xs, self.ys, reverse)
