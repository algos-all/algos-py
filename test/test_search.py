import pytest, random

from string import ascii_lowercase
from random import seed, choice, randrange

from src.search import SearchBM, SearchKMP


@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
def test_empty_pattern_0(search):
    s = search("")

    assert s.search("Hello, world!") == 0

@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
def test_empty_pattern_1(search):
    s = search("")

    assert s.search("") == 0

@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
def test_pattern_0(search):
    s = search("a")

    assert s.search("a") == 0
    assert s.search("ba") == 1
    assert s.search("bab") == 1

@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
def test_pattern_1(search):
    s = search("ABBA")

    assert s.search("a") == 1
    assert s.search("abba") == 4
    assert s.search("ABBA") == 0
    assert s.search("AABBA") == 1
    assert s.search("ABABBA") == 2

@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
def test_pattern_2(search):
    s = search("ABC")

    assert s.search("ABBC") == 4, s.search("ABBC")

@pytest.mark.parametrize("search", [SearchBM, SearchKMP])
@pytest.mark.parametrize("n", list(range(1, 100)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_random(search, n, seed):
    random.seed(seed)

    txt = "".join(choice(ascii_lowercase) for i in range(n))

    for i in range(10):
        pat = txt[randrange(0, n) : randrange(0, n)]

        s = search(pat)

        assert s.search(txt) == txt.find(pat)

        pat += "A"

        s = search(pat)

        assert s.search(txt) == len(txt)
