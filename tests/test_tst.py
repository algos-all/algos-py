import string

from check_strset import CheckStringSet

from tst import TernarySearchTree as TST


class TestTernarySearchTree(CheckStringSet):
    def test_empty_get(self):
        self.check_empty_get(TST())

    def test_single_letters(self):
        self.check_single_letters(TST())

    def test_single_digits(self):
        self.check_single_digits(TST())

    def test_simple_chain(self):
        for i in range(1, 10):
            yield self.check_simple_chain, TST(), i

    def test_words_0(self):
        self.check_words_0(TST())

    def test_words_1(self):
        self.check_words_1(TST())

    def test_words_2(self):
        self.check_words_2(TST())

    def test_words_3(self):
        self.check_words_3(TST())

    def test_words_4(self):
        self.check_words_4(TST())

    def test_random_words_0(self, times=10):
        for i in range(times):
            yield self.check_random_words, TST(), i

    def test_random_words_1(self, times=10):
        for i in range(times):
            yield self.check_random_words, TST(), i, 100, 10

    def test_random_words_2(self, times=10):
        for i in range(times):
            yield self.check_random_words, TST(), i, 100, 10, "01"
