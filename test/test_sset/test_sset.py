import pytest

from string import ascii_lowercase
from random import seed, choice, randint

from src.sset.tst import TernarySearchTree
from src.sset.trie import Trie


@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_empty_get(UUT):
    uut = UUT()
    
    assert uut.get("") is None

    uut.put("a", 42)

    assert uut.get("") is None

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_single_letters(UUT):
    uut = UUT()
    lhs = ascii_lowercase[:13]
    rhs = ascii_lowercase[13:]

    for letter in lhs:
        uut.put(letter, letter)

    for letter in lhs:
        assert uut.get(letter) == letter, "{} != {}".format(
            uut.get(letter), letter
        )

    for letter in rhs:
        assert uut.get(letter) == None, "{} != None".format(
            uut.get(letter)
        )

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_single_digits(UUT):
    uut = UUT()
    lhs = list(range(0, 5))
    rhs = list(range(5, 10))

    for digit in lhs:
        uut.put([digit], digit)

    for digit in lhs:
        assert uut.get([digit]) == digit

    for digit in rhs:
        assert uut.get([digit]) is None

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
@pytest.mark.parametrize("n", [i for i in range(1, 11)])
def test_simple_chain(UUT, n):
    if n <= 0:
        raise RuntimeError("n should be length (positive)")

    uut, word = UUT(), "".join(["i" for i in range(n)])

    for i in range(1, n):
        uut.put(word[:i], i)

    for i in range(1, n):
        assert uut.get(word[:i]) == i, uut.all()

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_words_0(UUT):
    uut, words = UUT(), ["a", "aa", "aaa", "abbb"]

    for i, w in enumerate(words):
        uut.put(w, i)

    for i, w in enumerate(words):
        assert uut.get(w) == i

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_words_1(UUT):
    uut, words = UUT(), ["c", "cb", "cc", "ce"]

    for i, w in enumerate(words):
        uut.put(w, i)

    for i, w in enumerate(words):
        assert uut.get(w) == i

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_words_2(UUT):
    uut, words = UUT(), ["good", "go"]

    for i, w in enumerate(words):
        uut.put(w, i)

    for i, w in enumerate(words):
        assert uut.get(w) == i, "expected {}: {}".format(w, i)

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_words_3(UUT):
    uut, words = UUT(), ["b", "a", "c"]

    for i, w in enumerate(words):
        uut.put(w, i)

    for i, w in enumerate(words):
        assert uut.get(w) == i

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_words_4(UUT):
    uut, words = UUT(), ["b", "a", "c", "ball", "all", "cya"]

    for i, w in enumerate(words):
        uut.put(w, i)

    for i, w in enumerate(words):
        assert uut.get(w) == i

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_empty_0(UUT):
    assert UUT().gcp("") == 0

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_empty_1(UUT):
    uut = UUT()
    
    uut.put("a", 42)

    assert uut.gcp("") == 0

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_0(UUT):
    uut, words = UUT(), ["a", "b"]

    for i, w in enumerate(words):
        uut.put(w, i)

    assert uut.gcp("c") == 0, uut.gcp("c")

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_1(UUT):
    uut, words = UUT(), ["a", "b", "c"]

    for i, w in enumerate(words):
        uut.put(w, i)

    assert uut.gcp("c") == 1, uut.gcp("c")

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_2(UUT):
    uut = UUT()
    
    uut.put("a", 0)
    assert uut.gcp("a") == 1

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_gcp_3(UUT):
    uut = UUT()
    
    uut.put("a", 0)
    assert uut.gcp("aa") == 1

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_all_0(UUT):
    uut = UUT()
    
    assert uut.all() == []

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_all_1(UUT):
    uut = UUT()
    
    uut.put("a", 0)
    assert uut.all() == ["a"], uut.all()

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_all_2(UUT):
    uut = UUT()
    
    words = ["a", "b", "c"]

    for i, w in enumerate(words):
        uut.put(w, i)

    result = uut.all()

    for r in result:
        assert r in words, result

    for w in words:
        assert w in result, result

def setup_random_tst(uut, s, n, m, alpha):
    assert n >= 1 and m >= 1 and len(alpha) != 0

    seed(s)

    words, values = [
        "".join([choice(alpha) for i in range(randint(1, m))])
        for j in range(n)
    ], {}

    for i, w in enumerate(words):
        uut.put(w, i)
        values[w] = i

    return uut, words, values

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
@pytest.mark.parametrize("s", [i for i in range(3)])
@pytest.mark.parametrize("n", [i for i in range(1, 100)])
@pytest.mark.parametrize("m", [100])
@pytest.mark.parametrize("alpha", [ascii_lowercase, "01"])
def test_random_words(UUT, s, n, m, alpha):
    uut, words, values = setup_random_tst(UUT(), s, n, m, alpha)

    for i, w in enumerate(words):
        assert uut.get(w) == values[w]

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
@pytest.mark.parametrize("s", [i for i in range(3)])
@pytest.mark.parametrize("n", [i for i in range(1, 100)])
@pytest.mark.parametrize("m", [100])
@pytest.mark.parametrize("alpha", [ascii_lowercase, "01"])
def test_all_random(UUT, s, n, m, alpha):
    uut, words, values = setup_random_tst(UUT(), s, n, m, alpha)

    result = uut.all()

    for r in result:
        assert r in words

    for w in words:
        assert w in result

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_empty_0(UUT):
    assert UUT().startswith("") == []

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_empty_1(UUT):
    uut = UUT()
    
    words = ["a", "b", "c"]

    for i, w in enumerate(words):
        uut.put(w, i)

    result = uut.startswith("")

    for r in result:
        assert r in words, result

    for w in words:
        assert w in result, result

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_0(UUT):
    uut = UUT()

    uut.put("a",  0)

    assert uut.startswith("a") == ["a"]

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_1(UUT):
    uut = UUT()

    words = ["a", "b"]

    for i, w in enumerate(words): uut.put(w, i)

    for w in words: assert uut.startswith(w) == [w]

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_2(UUT):
    uut = UUT()
    
    words = ["help", "hell"]

    for i, w in enumerate(words):
        uut.put(w, i)

    result = uut.startswith("hel")

    for w in words:
        assert w in result, result

    for w in words:
        result = uut.startswith(w)

        assert result == [w], result

    result = uut.startswith("helpme")
    assert result == []

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_startswith_3(UUT):
    uut = UUT()
    
    uut.put("help", 0)

    assert uut.startswith("hell") == []
    assert uut.startswith("helpme") == []

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_empty_remove_0(UUT):
    uut = UUT()
    
    uut.remove("")

    assert True

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_empty_remove_1(UUT):
    uut = UUT()
    
    uut.put("aaaaa", 0)

    uut.remove("")

    assert True

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_0(UUT):
    uut = UUT()
    
    uut.put("a", 0)
    uut.remove("a")

    assert uut.get("a") == None

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_1(UUT):
    uut = UUT()
    
    uut.put("aaaa", 0)

    uut.remove("a")
    uut.remove("aa")
    uut.remove("aaa")

    assert uut.get("aaaa") == 0

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_2(UUT):
    uut = UUT()
    
    uut.put("aaaa", 0)

    uut.remove("b")

    assert uut.get("aaaa") == 0

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_3(UUT):
    uut = UUT()
    
    uut.put("a", 0)
    uut.remove("a")
    uut.put("a", 0)

    assert uut.get("a") == 0

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_4(UUT):
    uut = UUT()
    
    words = ["a", "b", "c"]

    for i, w in enumerate(words):
        uut.put(w, i)

    uut.remove("a")

    assert uut.get("a") == None
    assert uut.get("b") == 1
    assert uut.get("c") == 2

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_5(UUT):
    uut = UUT()
    
    words = ["a", "aa", "aaa"]

    for i, w in enumerate(words):
        uut.put(w, i)

    uut.remove("a")

    assert uut.get("") == None
    assert uut.get("a") == None
    assert uut.get("aa") == 1
    assert uut.get("aaa") == 2

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_5(UUT):
    uut = UUT()
    
    words = ["a", "aa", "aaa"]

    for i, w in enumerate(words):
        uut.put(w, i)

    uut.remove("aa")

    assert uut.get("") == None
    assert uut.get("a") == 0
    assert uut.get("aa") == None
    assert uut.get("aaa") == 2

@pytest.mark.parametrize("UUT", [TernarySearchTree, Trie])
def test_remove_6(UUT):
    uut = UUT()
    
    words = ["a", "aa", "aaa"]

    for i, w in enumerate(words):
        uut.put(w, i)

    uut.remove("a")

    assert uut.get("") == None
    assert uut.get("a") == None
    assert uut.get("aa") == 1
    assert uut.get("aaa") == 2

    uut.remove("aa")

    assert uut.get("") == None
    assert uut.get("a") == None
    assert uut.get("aa") == None
    assert uut.get("aaa") == 2

    uut.remove("aaa")

    assert uut.get("") == None
    assert uut.get("a") == None
    assert uut.get("aa") == None
    assert uut.get("aaa") == None
