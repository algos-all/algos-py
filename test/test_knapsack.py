import pytest

from src.knapsack import _knapsack_0, _knapsack_1, _knapsack_2, _knapsack_3


knapsacks = [_knapsack_0, _knapsack_1, _knapsack_2, _knapsack_3]


@pytest.mark.parametrize("knapsack", knapsacks)
def test_one_element_0(knapsack):

    assert knapsack(0, [1], [1]) == 0


@pytest.mark.parametrize("knapsack", knapsacks)
def test_one_element_1(knapsack):

    assert knapsack(1, [1], [1]) == 1


@pytest.mark.parametrize("knapsack", knapsacks)
def test_one_element_2(knapsack):

    assert knapsack(1, [-1], [1]) == 0


@pytest.mark.parametrize("knapsack", knapsacks)
def test_simple_choice_0(knapsack):

    assert knapsack(1, [1, 2], [1, 1]) == 2
    assert knapsack(1, [2, 1], [1, 1]) == 2


@pytest.mark.parametrize("knapsack", knapsacks)
def test_simple_choice_1(knapsack):

    assert knapsack(2, [1, 2, 3], [1, 1, 1]) == 5
    assert knapsack(2, [3, 2, 1], [1, 1, 1]) == 5
    assert knapsack(2, [1, 3, 2], [1, 1, 1]) == 5


@pytest.mark.parametrize("knapsack", knapsacks)
def test_simple_sum_0(knapsack):

    assert knapsack(3, [1, 2, 3], [1, 1, 1]) == 6


@pytest.mark.parametrize("knapsack", knapsacks)
def test_simple_benchmark(benchmark, knapsack):

    vs = [v for v in range(15)]
    ws = [w for w in range(15)]

    assert benchmark(knapsack, sum(ws), vs, ws) == sum(vs)
