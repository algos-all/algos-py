from string import ascii_lowercase
from random import seed, choice, randrange

class CheckSearch:
    def check_empty_pattern_0(self, search):
        s = search("")

        assert s.search("Hello, world!") == 0

    def check_empty_pattern_1(self, search):
        s = search("")

        assert s.search("") == 0

    def check_pattern_0(self, search):
        s = search("a")

        assert s.search("a") == 0
        assert s.search("ba") == 1
        assert s.search("bab") == 1

    def check_pattern_1(self, search):
        s = search("ABBA")

        assert s.search("a") == 1
        assert s.search("abba") == 4
        assert s.search("ABBA") == 0
        assert s.search("AABBA") == 1
        assert s.search("ABABBA") == 2

    def check_pattern_2(self, search):
        s = search("ABC")

        assert s.search("ABBC") == 4, s.search("ABBC")

    def check_random(self, search, n, s):
        seed(s)

        txt = "".join(choice(ascii_lowercase) for i in range(n))

        for i in range(10):
            pat = txt[randrange(0, n) : randrange(0, n)]

            s = search(pat)

            assert s.search(txt) == txt.find(pat)

            pat += "A"

            s = search(pat)

            assert s.search(txt) == len(txt)
