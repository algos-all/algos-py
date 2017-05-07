import random, pytest

from fractions import gcd
from src.gcf import gcf, xgcf


def test_00():
    assert gcf(0, 0) == 0

def test_10():
    assert gcf(1, 0) == 1

def test_01():
    assert gcf(0, 1) == 1

@pytest.mark.parametrize("seed", list(range(100)))
def test_random_gcd(seed, lo=-1024, hi=1024):
    random.seed(seed)

    a, b = random.randint(lo, hi), random.randint(lo, hi)

    g = gcf(a, b)

    assert g == gcd(a, b), "{}, {}".format(a, b)

def test_00():
    assert xgcf(0, 0)[0] == 0

def test_10():
    assert xgcf(1, 0) == (1, 1, 0)

def test_01():
    assert xgcf(0, 1) == (1, 0, 1)

@pytest.mark.parametrize("seed", list(range(100)))
def test_random_gcf(seed, lo=-1024, hi=1024):
    random.seed(seed)

    a, b = random.randint(lo, hi), random.randint(lo, hi)

    g, s, t = xgcf(a, b)
    correct = gcd(a, b)

    assert correct == g, "{}, {}".format(a, b)
    assert correct == s * a + t * b, "{}, {}".format(a, b)

