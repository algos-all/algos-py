from search import SearchKMP, SearchBM
from tests.check_search import CheckSearch

class TestSearchKMP(CheckSearch):
    def test_empty_pattern_0(self):
        self.check_empty_pattern_0(SearchKMP)

    def test_empty_pattern_1(self):
        self.check_empty_pattern_1(SearchKMP)

    def test_pattern_0(self):
        self.check_pattern_0(SearchKMP)

    def test_pattern_1(self):
        self.check_pattern_1(SearchKMP)

    def test_pattern_2(self):
        self.check_pattern_2(SearchKMP)

    def test_random(self, ns=100, ntimes=10):
        for n in range(1, ns):
            for i in range(ntimes):
                yield self.check_random, SearchKMP, n, i


class TestSearchBM(CheckSearch):
    def test_empty_pattern_0(self):
        self.check_empty_pattern_0(SearchBM)

    def test_empty_pattern_1(self):
        self.check_empty_pattern_1(SearchBM)

    def test_pattern_0(self):
        self.check_pattern_0(SearchBM)

    def test_pattern_1(self):
        self.check_pattern_1(SearchBM)

    def test_pattern_2(self):
        self.check_pattern_2(SearchBM)

    def test_random(self, ns=100, ntimes=10):
        for n in range(1, ns):
            for i in range(ntimes):
                yield self.check_random, SearchBM, n, i
