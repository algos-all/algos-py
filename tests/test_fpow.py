import pytest

from src.fpow import fpow0, fpow1

@pytest.mark.parametrize('fpow', [fpow0, fpow1])
@pytest.mark.parametrize('x', list(range(-100, 100)))
# 997 is a prime number. This ensures different choices for `n`.
@pytest.mark.parametrize('n', list(range(10)) + list(range(10, 10000, 997)))
def test_fpow_nonzero(fpow, x, n):
    if x == 0:
        assert True, 'a separate unit test will deal with x == 0'

        return

    assert fpow(x, n) == pow(x, n), '{} failed for {}^{}'.format(fpow.__name__, x, n)

@pytest.mark.parametrize('fpow', [fpow0, fpow1])
@pytest.mark.parametrize('x', list(range(-10, 10)))
def test_fpow_nzero(fpow, x):
    assert fpow(x, 0) == 1, '{} failed for {}^{}'.format(fpow.__name__, x, 0)

@pytest.mark.parametrize('fpow', [fpow0, fpow1])
@pytest.mark.parametrize('n', list(range(-100, 0)))
def test_fpow_xzero_nneg_throws(fpow, n):
    '''Make sure that for x == 0 and n < 0 an exception is throws'''

    with pytest.raises(ZeroDivisionError):
        fpow(0, n)
