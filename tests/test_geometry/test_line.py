import pytest

from src.geometry.line import compute_standard_line

def test_standard_line_0():
    # One point is not enough to form a line
    for i in range(-10, 11):
        for j in range(-10, 11):
            A, B, C = compute_standard_line(i, j, i, j)

            assert A == 0 and B == 0 and C == 0

@pytest.mark.parametrize("points", [
    [(0, 0), (1, 1)], [(1, 1), (0, 0)],
    [(1, 1), (2, 2)], [(2, 2), (1, 1)],
    [(100, 100), (200, 200)], [(200, 200), (100, 100)]
])
def test_standard_line_1(points):
    point0, point1 = points

    A, B, C = compute_standard_line(
        point0[0], point0[1], point1[0], point1[1]
    )

    for i in range(-10, 10):
        assert i * A + i * B + C == 0

@pytest.mark.parametrize("points", [
    [(0, 0), (1, -1)], [(1, -1), (0, 0)],
    [(1, -1), (2, -2)], [(2, -2), (1, -1)],
    [(100, -100), (200, -200)], [(200, -200), (100, -100)]
])
def test_standard_line_2(points):
    point0, point1 = points

    A, B, C = compute_standard_line(
        point0[0], point0[1], point1[0], point1[1]
    )

    for i in range(-10, 10):
        assert i * A + (-i) * B + C == 0

def test_standard_line_3():
    A, B, C = compute_standard_line(0, 0, 0, 1)

    assert A * 0 + B * 2 + C == 0
    assert A * 0 + B * 101 + C == 0
    assert A * 0 + B * (-101) + C == 0

def test_standard_line_4():
    A, B, C = compute_standard_line(0, 0, 1, 0)

    assert A * 0 + B * 0 + C == 0
    assert A * 101 + B * 0 + C == 0
    assert A * (-101) + B * 0 + C == 0

def test_standard_line_5():
    A, B, C = compute_standard_line(0, 2, 10, 2)

    assert A * 101 + B * 2 + C == 0
    assert A *(-101) + B * 2 + C == 0
