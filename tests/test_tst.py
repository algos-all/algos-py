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

    def test_gcp_empty_0(self):
        self.check_gcp_empty_0(TST())

    def test_gcp_empty_1(self):
        self.check_gcp_empty_1(TST())

    def test_gcp_0(self):
        self.check_gcp_0(TST())

    def test_gcp_1(self):
        self.check_gcp_1(TST())

    def test_gcp_2(self):
        self.check_gcp_2(TST())

    def test_gcp_3(self):
        self.check_gcp_3(TST())

    def test_all_0(self):
        self.check_all_0(TST())

    def test_all_1(self):
        self.check_all_1(TST())

    def test_all_2(self):
        self.check_all_2(TST())

    def test_all_random(self, times=10):
        for i in range(times):
            yield self.check_all_random, TST(), i

    def test_startswith_empty_0(self):
        self.check_startswith_empty_0(TST())

    def test_startswith_empty_1(self):
        self.check_startswith_empty_1(TST())

    def test_startswith_0(self):
        self.check_startswith_0(TST())

    def test_startswith_1(self):
        self.check_startswith_1(TST())

    def test_startswith_2(self):
        self.check_startswith_2(TST())

    def test_startswith_3(self):
        self.check_startswith_3(TST())
