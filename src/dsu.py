class DisjointSetUnion:
    '''
    Construct a disjoint set union (DSU)

    This data structure tracks a set of elements partitioned into a
    number of *disjoint* (i.e. non-overlapping) subsets. It provides
    almost constant-time operations to:

    1. Add a new element to the set
    2. Join two sets into one (union)
    3. Find if two elements are in the same set (find)

    Alternative names for this data structure:

    1. Disjoint-set data structure
    2. Union-find data structure
    3. Merge-find set
    '''

    def __init__(self, xs=None):
        '''
        Create an empty or a pre-populated disjoint set union (DSU)

        :param xs: a list of elements. If None, then an empty DSU is
                   created. Otherwise, each element is treated as its
                   own set.
        '''
        self.xs = {x: x for x in xs} if xs else {}
        self.ws = {x: 1 for x in xs} if xs else {}

        self.count = len(xs) if xs else 0

    def __iter__(self):
        return iter(self.xs)

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, val):
        '''
        Add a new element to the disjoint set union (DSU)

        The item is added initially as its own set.

        :param key: the item to add to the DSU
        :param val: the value, must be equal to the provided key
        '''

        if key is not val:
            raise RuntimeError("key and val must be the same")

        self.xs[key] = key
        self.ws[key] = 1

    def find(self, key, w=0):
        '''
        Find the set of the provided key

        This method returns the same key for those keys that belong to
        the same set. Internally, the keys from the same set make up a
        tree whose root holds the key that represents the whole set.

        When you call find with a specific key, there are two edge
        cases:

        1. The provided key is, in fact, the root of the tree. If so,
        it is immediately returned.  2. The provided key is a leaf of
        some very long path to the root of the tree. In this case, the
        entire path to the root must be traversed.

        To avoid having very long paths, the second case also performs
        path compression after traversing the path to the root.

        :param key: the key whose set should be found
        :param w: the weight of the subtree of the key
        '''

        if self.xs[key] == key:
            self.ws[key] += w

            return key

        self.ws[self.xs[key]] -= self.ws[key]
        self.xs[key] = self.find(self.xs[key], self.ws[key])

        return self.xs[key]

    def union(self, key1, key2):
        '''
        Combine the sets that contain the two given keys into one

        If both keys belong to the same set, the method does not
        achieve much. However, path compression could still change
        the underlying data structure.

        :param key1: the key contained in the first set
        :param key2: the key contained in the second set
        '''
        val1 = self.find(key1)
        val2 = self.find(key2)

        if val1 == val2: return

        if self.ws[val1] < self.ws[val2]:
            val1, val2 = val2, val1

        self.xs[val1] = val2
        self.ws[val2] += self.ws[val1]
