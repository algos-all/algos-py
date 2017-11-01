import pytest

from src.geometry.point2d import Point2D
from src.geometry.convhull2d import ConvexHull2D


lft = -5
rgt = +5

@pytest.mark.parametrize('x', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y', [y for y in range(lft, rgt)])
def test_convhull2d_1(x, y):
    p = Point2D(x, y)

    hull = ConvexHull2D([p])

    assert len(hull) == 1
    assert len(hull.outer) == 1

    assert len(hull.upper) == 1
    assert len(hull.lower) == 1

    assert hull.outer[0] == p

    assert hull.lower[0] == p
    assert hull.upper[0] == p

@pytest.mark.parametrize('x0', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y0', [y for y in range(lft, rgt)])
@pytest.mark.parametrize('x1', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y1', [y for y in range(lft, rgt)])
def test_convhull2d_2(x0, y0, x1, y1):
    p = Point2D(x0, y0)
    q = Point2D(x1, y1)

    hull = ConvexHull2D([p, q])

    if p == q:
        assert len(hull) == 1

        assert hull.outer[0] == p
    else:
        assert len(hull) == 2

        if p < q:
            assert hull.outer[0] == p
            assert hull.outer[1] == q
        else:
            assert hull.outer[0] == q
            assert hull.outer[1] == p
