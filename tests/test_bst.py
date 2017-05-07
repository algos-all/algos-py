import random, pytest

from src.bst import BinarySearchTree as BST


def check_tree(bst, k2v):
    for key in k2v:
        if bst.get(key) != k2v[key]:
            assert False

    assert True

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_put_get(n, seed, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    bst, k2v = BST(), {}

    for i in range(n):
        key, val = random.randint(lo, hi), random.randint(lo, hi)

        k2v[key] = val

        bst.put(key, val)

        check_tree(bst, k2v)

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_contains(n, seed, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    bst, k2v = BST(), {}

    for i in range(n):
        key, val = random.randint(lo, hi), random.randint(lo, hi)

        k2v[key] = val

        bst.put(key, val)

    for key in k2v:
        assert key in bst

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_setitem_getitem(n, seed, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    bst, k2v = BST(), {}

    for i in range(n):
        key, val = random.randint(lo, hi), random.randint(lo, hi)

        k2v[key], bst[key] = val, val

        for key in k2v:
            assert bst[key] == k2v[key]

@pytest.mark.parametrize("n", list(range(1, 10)))
@pytest.mark.parametrize("seed", list(range(3)))
def test_remove(n, seed, lo=-1024, hi=1024):
    assert n > 0 and lo < hi

    random.seed(0)

    bst, k2v =BST(), {}

    for i in range(n):
        key, val = random.randint(lo, hi), random.randint(lo, hi)

        k2v[key] = val
        bst.put(key, val)

    for key in list(k2v.keys()):
        bst.remove(key)
        k2v.pop(key)

        check_tree(bst, k2v)

    bst.remove(42)

    assert bst.root is None
