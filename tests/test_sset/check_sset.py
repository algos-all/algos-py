from string import ascii_lowercase
from random import seed, choice, randint

class CheckStringSet:
    def check_empty_get(self, ss):
        assert ss.get("") is None

        ss.put("a", 42)

        assert ss.get("") is None

    def check_single_letters(self, ss):
        inside = ascii_lowercase[:13]
        outside = ascii_lowercase[13:]

        for letter in inside:
            ss.put(letter, letter)

        for letter in inside:
            assert ss.get(letter) == letter, "{} != {}".format(
                ss.get(letter), letter
            )

        for letter in outside:
            assert ss.get(letter) == None, "{} != None".format(
                ss.get(letter)
            )

    def check_single_digits(self, ss):
        inside = list(range(0, 5))
        outside = list(range(5, 10))

        for digit in inside: ss.put([digit], digit)

        for digit in inside:
            assert ss.get([digit]) == digit

        for digit in outside:
            assert ss.get([digit]) is None

    def check_simple_chain(self, ss, n=10):
        if n <= 0:
            raise RuntimeError("n should be length (positive)")

        word = "".join(["i" for i in range(n)])

        for i in range(1, n):
            ss.put(word[:i], i)

        for i in range(1, n):
            assert ss.get(word[:i]) == i, ss.all()

    def check_words_0(self, ss):
        words = ["a", "aa", "aaa", "abbb"]

        for i, w in enumerate(words):
            ss.put(w, i)

        for i, w in enumerate(words):
            assert ss.get(w) == i

    def check_words_1(self, ss):
        words = ["c", "cb", "cc", "ce"]

        for i, w in enumerate(words):
            ss.put(w, i)

        for i, w in enumerate(words):
            assert ss.get(w) == i

    def check_words_2(self, ss):
        words = ["good", "go"]

        for i, w in enumerate(words):
            ss.put(w, i)

        for i, w in enumerate(words):
            assert ss.get(w) == i, "expected {}: {}".format(w, i)

    def check_words_3(self, ss):
        words = ["b", "a", "c"]

        for i, w in enumerate(words):
            ss.put(w, i)

        for i, w in enumerate(words):
            assert ss.get(w) == i

    def check_words_4(self, ss):
        words = ["b", "a", "c", "ball", "all", "cya"]

        for i, w in enumerate(words):
            ss.put(w, i)

        for i, w in enumerate(words):
            assert ss.get(w) == i

    def check_random_words(
            self, ss, s, n=10, m=3, alpha=ascii_lowercase
    ):
        assert n >= 1 and m >= 1 and len(alpha) != 0

        seed(s)

        words, values = [
            "".join([choice(alpha) for i in range(randint(1, m))])
            for j in range(n)
        ], {}

        for i, w in enumerate(words):
            ss.put(w, i)
            values[w] = i

        for i, w in enumerate(words):
            assert ss.get(w) == values[w]

    def check_gcp_empty_0(self, ss):
        assert ss.gcp("") == 0

    def check_gcp_empty_1(self, ss):
        ss.put("a", 42)

        assert ss.gcp("") == 0

    def check_gcp_0(self, ss):
        words = ["a", "b"]

        for i, w in enumerate(words):
            ss.put(w, i)

        assert ss.gcp("c") == 0, ss.gcp("c")

    def check_gcp_1(self, ss):
        words = ["a", "b", "c"]

        for i, w in enumerate(words):
            ss.put(w, i)

        assert ss.gcp("c") == 1, ss.gcp("c")

    def check_gcp_2(self, ss):
        ss.put("a", 0)
        assert ss.gcp("a") == 1

    def check_gcp_3(self, ss):
        ss.put("a", 0)
        assert ss.gcp("aa") == 1

    def check_all_0(self, ss):
        assert ss.all() == []

    def check_all_1(self, ss):
        ss.put("a", 0)
        assert ss.all() == ["a"], ss.all()

    def check_all_2(self, ss):
        words = ["a", "b", "c"]

        for i, w in enumerate(words):
            ss.put(w, i)

        result = ss.all()

        for r in result:
            assert r in words, result

        for w in words:
            assert w in result, result

    def check_all_random(
            self, ss, i, n=10, m=3, alpha=ascii_lowercase
    ):
        assert n >= 1 and m >= 1 and len(alpha) != 0

        seed(i)

        words, values = [
            "".join([choice(alpha) for i in range(randint(1, m))])
            for j in range(n)
        ], {}

        for i, w in enumerate(words):
            ss.put(w, i)
            values[w] = i

        result = ss.all()

        for r in result:
            assert r in words

        for w in words:
            assert w in result

    def check_startswith_empty_0(self, ss):
        assert ss.startswith("") == []

    def check_startswith_empty_1(self, ss):
        words = ["a", "b", "c"]

        for i, w in enumerate(words): ss.put(w, i)

        result = ss.startswith("")

        for r in result: assert r in words, result
        for w in words: assert w in result, result

    def check_startswith_0(self, ss):
        ss.put("a", 0)
        assert ss.startswith("a") == ["a"]

    def check_startswith_1(self, ss):
        words = ["a", "b"]

        for i, w in enumerate(words): ss.put(w, i)

        for w in words: assert ss.startswith(w) == [w]

    def check_startswith_2(self, ss):
        words = ["help", "hell"]

        for i, w in enumerate(words): ss.put(w, i)

        result = ss.startswith("hel")

        for w in words:
            assert w in result, result

        for w in words:
            result = ss.startswith(w)

            assert result == [w], result

        result = ss.startswith("helpme")
        assert result == []

    def check_startswith_3(self, ss):
        ss.put("help", 0)

        assert ss.startswith("hell") == []
        assert ss.startswith("helpme") == []

    def check_empty_remove_0(self, ss):
        ss.remove("")

        assert True

    def check_empty_remove_1(self, ss):
        ss.put("aaaaa", 0)

        ss.remove("")

        assert True

    def check_remove_0(self, ss):
        ss.put("a", 0)
        ss.remove("a")

        assert ss.get("a") == None

    def check_remove_1(self, ss):
        ss.put("aaaa", 0)

        ss.remove("a")
        ss.remove("aa")
        ss.remove("aaa")

        assert ss.get("aaaa") == 0

    def check_remove_2(self, ss):
        ss.put("aaaa", 0)

        ss.remove("b")

        assert ss.get("aaaa") == 0

    def check_remove_3(self, ss):
        ss.put("a", 0)
        ss.remove("a")
        ss.put("a", 0)

        assert ss.get("a") == 0

    def check_remove_4(self, ss):
        words = ["a", "b", "c"]

        for i, w in enumerate(words):
            ss.put(w, i)

        ss.remove("a")

        assert ss.get("a") == None
        assert ss.get("b") == 1
        assert ss.get("c") == 2

    def check_remove_5(self, ss):
        words = ["a", "aa", "aaa"]

        for i, w in enumerate(words):
            ss.put(w, i)

        ss.remove("a")

        assert ss.get("") == None
        assert ss.get("a") == None
        assert ss.get("aa") == 1
        assert ss.get("aaa") == 2

    def check_remove_5(self, ss):
        words = ["a", "aa", "aaa"]

        for i, w in enumerate(words):
            ss.put(w, i)

        ss.remove("aa")

        assert ss.get("") == None
        assert ss.get("a") == 0
        assert ss.get("aa") == None
        assert ss.get("aaa") == 2


    def check_remove_6(self, ss):
        words = ["a", "aa", "aaa"]

        for i, w in enumerate(words):
            ss.put(w, i)

        ss.remove("a")

        assert ss.get("") == None
        assert ss.get("a") == None
        assert ss.get("aa") == 1
        assert ss.get("aaa") == 2

        ss.remove("aa")

        assert ss.get("") == None
        assert ss.get("a") == None
        assert ss.get("aa") == None
        assert ss.get("aaa") == 2

        ss.remove("aaa")

        assert ss.get("") == None
        assert ss.get("a") == None
        assert ss.get("aa") == None
        assert ss.get("aaa") == None
