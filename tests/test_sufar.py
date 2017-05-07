import random, string, pytest

from src.sufar import sufar, sufar_baseline


@pytest.mark.parametrize("n", list(range(100)) + [10000])
@pytest.mark.parametrize(
    "alpha", [string.printable, "a", "ab"]
)
@pytest.mark.parametrize("seed", list(range(10)))
def test_random(n, alpha, seed):
    assert n >= 0 and len(alpha) != 0

    random.seed(seed)

    txt = "".join(random.choice(alpha) for i in range(n))

    assert sufar(txt) == sufar_baseline(txt)
