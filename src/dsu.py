class DisjointSetUnion:

    def __init__(self, xs=None):
        self.xs = {x: x for x in xs} if xs else {}
        self.ws = {x: 1 for x in xs} if xs else {}

        self.count = len(xs) if xs else 0

    def __iter__(self):
        return iter(self.xs)

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, val):
        if key is not val:
            raise RuntimeError("key and val must be the same object")

        self.xs[key] = key
        self.ws[key] = 1

    def find(self, key, w=0):
        if self.xs[key] == key:
            self.ws[key] += w

            return key

        self.ws[self.xs[key]] -= self.ws[key]
        self.xs[key] = self.find(self.xs[key], self.ws[key])

        return self.xs[key]

    def union(self, key1, key2):
        val1 = self.find(key1)
        val2 = self.find(key2)

        if val1 == val2: return

        if self.ws[val1] < self.ws[val2]:
            val1, val2 = val2, val1

        self.xs[val1] = val2
        self.ws[val2] += self.ws[val1]
