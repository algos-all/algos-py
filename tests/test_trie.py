import string

from check_strset import CheckStringSet

from trie import Trie


class TestTrie(CheckStringSet):
    def test_empty_get(self):
        self.check_empty_get(Trie())

    def test_single_letters(self):
        self.check_single_letters(Trie())

    def test_single_digits(self):
        self.check_single_digits(Trie())

    def test_simple_words(self):
        inside = ["hello", "world", "this", "is", "dog"]
        outside = ["help", "thisis", "do"]
        self.check_simple_words(Trie(), inside, outside)

    def test_gcp_with_empty(self):
        trie = Trie()

        assert trie.gcp("") == 0

        trie.put("hello", 42)

        assert trie.gcp("") == 0

    def test_gcp(self):
        trie = Trie()

        trie.put("hello", 42)

        assert trie.gcp("h") == 1
        assert trie.gcp("hello") == len("hello")
        assert trie.gcp("helloworld") == len("hello")
        assert trie.gcp("help") == 3

    def test_empty_startwith(self):
        trie = Trie()

        assert trie.startwith("") == []
        assert trie.startwith("hello") == []

    def test_startwith_0(self):
        trie, word = Trie(), "hello"

        trie.put(word, 42)

        for i in range(1, len(word)):
            assert trie.startwith(word[:i]) == [word]

    def test_startwith_1(self):
        trie, word = Trie(), "hello"

        trie.put(word, 42)

        result = trie.startwith(word + word)

        assert result == [], result

        trie.put(word + word, 42)

        result = trie.startwith(word + word)
        assert result == [word + word], result
