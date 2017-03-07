from nose.tools import raises

from tests.test_sset.check_sset import CheckStringSet
from sset.tst import TernarySearchTree as TST


class TestTernarySearchTree(CheckStringSet):
    def test_empty_get(self):
        self.check_empty_get(TST())

    @raises(RuntimeError)
    def test_empty_put(self):
        TST().put('', 'key')

    def test_str_repr(self):
        tst = TST()

        tst.put("hello", "world")

        assert repr(tst.root) == str(tst.root)

    def test_show(self):
        tst = TST()

        assert tst.show() == []

        tst.put("hello", "world")

        expected = \
"""[['o', 'world', [None, None, None]],
 ['l', None, [None, None, 'o']],
 ['l', None, [None, None, 'l']],
 ['e', None, [None, None, 'l']],
 ['h', None, [None, None, 'e']]]
"""

        assert str(tst.show()) == "".join(expected.split("\n"))

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

    def test_empty_remove_0(self):
        self.check_empty_remove_0(TST())

    def test_empty_remove_1(self):
        self.check_empty_remove_1(TST())

    def test_remove_0(self):
        self.check_remove_0(TST())

    def test_remove_1(self):
        self.check_remove_1(TST())

    def test_remove_2(self):
        self.check_remove_2(TST())

    def test_remove_3(self):
        self.check_remove_3(TST())

    def test_remove_4(self):
        self.check_remove_4(TST())

    def test_remove_5(self):
        self.check_remove_5(TST())

    def test_remove_6(self):
        self.check_remove_6(TST())
