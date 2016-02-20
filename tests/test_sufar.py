import random, string

from sufar import sufar, sufar_baseline


class TestSuffixArray:
    def __init__(self):
        self.sufars = [sufar]

    def check_random(
            self, sufar, length=42, source=string.printable, seed=0
    ):
        assert length >= 0
        random.seed(seed)

        txt = "".join(random.choice(source) for i in range(length))

        assert sufar(txt) == sufar_baseline(txt)

    def test_empty(self):
        for sufar in self.sufars:
            yield self.check_random, sufar, 0

    def test_single(self, ntimes=10):
        for sufar in self.sufars:
            for time in range(ntimes):
                yield self.check_random, sufar, 1

    def test_random_0(self, ntimes=10):
        for sufar in self.sufars:
            for time in range(ntimes):
                yield self.check_random, sufar, 2

    def test_random_1(self, ntimes=10):
        for sufar in self.sufars:
            for time in range(ntimes):
                yield self.check_random, sufar, 2, "ab"

    def test_random_2(self, ntimes=10):
        for sufar in self.sufars:
            for time in range(ntimes):
                yield self.check_random, sufar, 3

    def test_random_3(self, ntimes=10):
        for sufar in self.sufars:
            for time in range(ntimes):
                yield self.check_random, sufar, 3, "ab"

    def test_random_4(self, ntimes=10, ns=range(100)):
        for sufar in self.sufars:
            for time in range(ntimes):
                for n in ns:
                    yield self.check_random, sufar, n

    def test_random_5(self, ntimes=10, ns=range(100)):
        for sufar in self.sufars:
            for time in range(ntimes):
                for n in ns:
                    yield self.check_random, sufar, n, "ab"

    def test_random_6(self, ntimes=10, ns=[10000]):
        for sufar in self.sufars:
            for time in range(ntimes):
                for n in ns:
                    yield self.check_random, sufar, n
