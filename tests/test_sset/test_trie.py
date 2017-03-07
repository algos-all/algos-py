from tests.test_sset.check_sset import CheckStringSet
from sset.trie import Trie


class TestTrie(CheckStringSet):
    def test_empty_get(self):
        self.check_empty_get(Trie())

    def test_single_letters(self):
        self.check_single_letters(Trie())

    def test_single_digits(self):
        self.check_single_digits(Trie())

    def test_simple_chain(self):
        for i in range(1, 10):
            yield self.check_simple_chain, Trie(), i

    def test_words_0(self):
        self.check_words_0(Trie())

    def test_words_1(self):
        self.check_words_1(Trie())

    def test_words_2(self):
        self.check_words_2(Trie())

    def test_words_3(self):
        self.check_words_3(Trie())

    def test_words_4(self):
        self.check_words_4(Trie())

    def test_random_words_0(self, times=10):
        for i in range(times):
            yield self.check_random_words, Trie(), i

    def test_random_words_1(self, times=10):
        for i in range(times):
            yield self.check_random_words, Trie(), i, 100, 10

    def test_random_words_2(self, times=10):
        for i in range(times):
            yield self.check_random_words, Trie(), i, 100, 10, "01"

    def test_gcp_empty_0(self):
        self.check_gcp_empty_0(Trie())

    def test_gcp_empty_1(self):
        self.check_gcp_empty_1(Trie())

    def test_gcp_0(self):
        self.check_gcp_0(Trie())

    def test_gcp_1(self):
        self.check_gcp_1(Trie())

    def test_gcp_2(self):
        self.check_gcp_2(Trie())

    def test_gcp_3(self):
        self.check_gcp_3(Trie())

    def test_all_0(self):
        self.check_all_0(Trie())

    def test_all_1(self):
        self.check_all_1(Trie())

    def test_all_2(self):
        self.check_all_2(Trie())

    def test_all_random(self, times=10):
        for i in range(times):
            yield self.check_all_random, Trie(), i

    def test_startswith_empty_0(self):
        self.check_startswith_empty_0(Trie())

    def test_startswith_empty_1(self):
        self.check_startswith_empty_1(Trie())

    def test_startswith_0(self):
        self.check_startswith_0(Trie())

    def test_startswith_1(self):
        self.check_startswith_1(Trie())

    def test_startswith_2(self):
        self.check_startswith_2(Trie())

    def test_startswith_3(self):
        self.check_startswith_3(Trie())

    def test_empty_remove_0(self):
        self.check_empty_remove_0(Trie())

    def test_empty_remove_1(self):
        self.check_empty_remove_1(Trie())

    def test_remove_0(self):
        self.check_remove_0(Trie())

    def test_remove_1(self):
        self.check_remove_1(Trie())

    def test_remove_2(self):
        self.check_remove_2(Trie())

    def test_remove_3(self):
        self.check_remove_3(Trie())

    def test_remove_4(self):
        self.check_remove_4(Trie())

    def test_remove_5(self):
        self.check_remove_5(Trie())

    def test_remove_6(self):
        self.check_remove_6(Trie())
