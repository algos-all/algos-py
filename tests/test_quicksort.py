from sort.quicksort import qsort0, qsort1, qsort2, qsort3

from check_sort import CheckSort


class TestQuickSort:
    def __init__(self):
        self.ip_sorts = [qsort0, qsort1, qsort3]
        self.op_sorts = [qsort2]

        self.sorts = [self.ip_sorts, self.op_sorts]

        self.check_sorted = [
            CheckSort.onsorted_ip, CheckSort.onsorted_op
        ]
        self.check_random = [
            CheckSort.onrandom_ip, CheckSort.onrandom_op
        ]

        self.check_sorts_onsorted = zip(self.sorts, self.check_sorted)
        self.check_sorts_onrandom = zip(self.sorts, self.check_random)

    def test_empty(self):
        for sorts, check in self.check_sorts_onsorted:
            for sort in sorts:
                yield check, sort, 0

    def test_single_0(self):
        for sorts, check in self.check_sorts_onsorted:
            for sort in sorts:
                yield check, sort, 1

    def test_single_1(self):
        for sorts, check in self.check_sorts_onrandom:
            for sort in sorts:
                yield check, sort, 1

    def test_sorted_0(self, N=10):
        for sorts, check in self.check_sorts_onsorted:
            for sort in sorts:
                for n in range(N):
                    yield check, sort, n

    def test_sorted_1(self, N=10):
        for sorts, check in self.check_sorts_onsorted:
            for sort in sorts:
                for n in range(N):
                    yield check, sort, n, True

    def test_random_0(self, N=100):
        for sorts, check in self.check_sorts_onrandom:
            for sort in sorts:
                for n in range(N):
                    yield check, sort, n

    def test_random_1(self):
        for sorts, check in self.check_sorts_onrandom:
            for sort in sorts:
                yield check, sort, 1024, -1024, 1024

    def test_random_2(self):
        for sorts, check in self.check_sorts_onrandom:
            for sort in sorts:
                yield check, sort, 1337, -1024, 1024
