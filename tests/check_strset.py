import string

class CheckStringSet:
    def check_empty_get(self, ss):
        assert ss.get("") is None

        ss.put("a", 42)

        assert ss.get("") is None

    def check_single_letters(self, ss):
        inside = string.ascii_letters[:13]
        outside = string.ascii_letters[13:]

        for letter in inside: ss.put(letter, letter)

        print(ss.all())

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

    def check_simple_words(self, ss, inside, outside):
        for i, word in enumerate(inside):
            ss.put(word, i)

        for i, word in enumerate(inside):
            assert ss.get(word) == i

        for word in outside:
            assert ss.get(word) is None, ss.get(word)
