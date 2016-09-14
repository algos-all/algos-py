import copy, random, operator


class CheckSort:
    @staticmethod
    def issorted(xs, reverse=False):
        cmp = operator.ge if reverse else operator.le

        for i in range(1, len(xs)):
            if not cmp(xs[i - 1], xs[i]):
                return False

        return True

    def check_on_sorted(self, sort, N=10, reverse=False):
        assert N >= 0

        xs = list(reversed(range(N))) if reverse else list(range(N))
        ys = copy.copy(xs)

        zs = sort(xs)

        if zs is None or zs is xs:
            # assume an in-place sort
            assert xs == list(range(N))
        else:
            # assume a not-in-place sort
            assert xs == ys
            assert zs == list(range(N))

    def check_on_random(
            self, sort, key=lambda x: x, reverse=False,
            N=10, seed=0, lo=-1024, hi=1024
    ):
        assert N >= 0 and lo <= hi

        random.seed(seed)

        xs = [random.randint(lo, hi) for i in range(N)]
        ys = copy.copy(xs)

        zs = sort(xs, key, reverse)

        if zs is None or zs is xs:
            # assume an in-place sort
            assert CheckSort.issorted(xs, reverse)
        else:
            # assume a not-in-place sort
            assert xs == ys
            assert CheckSort.issorted(zs, reverse)
