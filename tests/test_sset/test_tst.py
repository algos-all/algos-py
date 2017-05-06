import pytest

from src.sset.tst import TernarySearchTree as TST


def test_empty_put():
    with pytest.raises(RuntimeError):
        TST().put('', 'key')

def test_str_repr():
    tst = TST()

    tst.put("hello", "world")

    assert repr(tst.root) == str(tst.root)

def test_show():
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
