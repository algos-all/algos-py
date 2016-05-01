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

        for letter in inside: ss.put(letter, letter)

        for letter in inside:
            assert ss.get(letter) == letter

        for letter in outside:
            assert ss.get(letter) == None

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
            assert ss.get(w) == i

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

        for i, w in enumerate(words):
            assert ss.get(w) == values[w]
