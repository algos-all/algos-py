import random

from fractions import gcd
from gcf import gcf, xgcf


class TestGCF:
    def test_00(self):
        assert gcf(0, 0) == 0

    def test_10(self):
        assert gcf(1, 0) == 1

    def test_01(self):
        assert gcf(0, 1) == 1

    def check_random(self, lo=-1024, hi=1024, seed=0):
        random.seed(seed)

        a, b = random.randint(lo, hi), random.randint(lo, hi)

        g = gcf(a, b)

        assert g == gcd(a, b), "{}, {}".format(a, b)

    def test_random(self, times=10000):
        for i in range(times): yield self.check_random


class TestXGCF:
    def test_00(self):
        assert xgcf(0, 0)[0] == 0

    def test_10(self):
        assert xgcf(1, 0) == (1, 1, 0)

    def test_01(self):
        assert xgcf(0, 1) == (1, 0, 1)

    def check_random(self, lo=-1024, hi=1024, seed=0):
        random.seed(seed)

        a, b = random.randint(lo, hi), random.randint(lo, hi)

        g, s, t = xgcf(a, b)
        correct = gcd(a, b)

        assert correct == g, "{}, {}".format(a, b)
        assert correct == s * a + t * b, "{}, {}".format(a, b)

    def test_random(self, times=10000):
        for i in range(times): yield self.check_random

