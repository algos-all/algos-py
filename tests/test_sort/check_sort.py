import copy, random, operator


class CheckSort:
    @staticmethod
    def issorted(xs, key=operator.le):
        for i in range(1, len(xs)):
            if not key(xs[i - 1], xs[i]):
                return False

        return True

    @staticmethod
    def onsorted_ip(sort, N=10, reverse=False):
        assert N >= 0

        xs = list(reversed(range(N))) if reverse else list(range(N))

        sort(xs)

        assert xs == list(range(N))

    @staticmethod
    def onrandom_ip(sort, N=10, lo=-10, hi=10, seed=0):
        assert N >= 0 and lo <= hi

        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(N)]

        sort(xs)

        assert CheckSort.issorted(xs)

    @staticmethod
    def onsorted_op(sort, N=10, reverse=False):
        assert N >= 0

        xs = list(reversed(range(N))) if reverse else list(range(N))
        ys = copy.copy(xs)

        zs = sort(xs)

        assert xs == ys
        assert zs == list(range(N))

    @staticmethod
    def onrandom_op(sort, N=10, lo=-10, hi=10, seed=0):
        assert N >= 0 and lo <= hi

        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(N)]
        ys = copy.copy(xs)

        zs = sort(xs)

        assert xs == ys
        assert CheckSort.issorted(zs)
