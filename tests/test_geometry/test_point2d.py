import pytest

from src.geometry.point2d import Point2D

lft = -4
rgt = +4

@pytest.mark.parametrize('x0', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y0', [y for y in range(lft, rgt)])
@pytest.mark.parametrize('x1', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y1', [y for y in range(lft, rgt)])
def test_point2d_cmp(x0, y0, x1, y1):
    if x0 == x1 and y0 == y1:
        assert (Point2D(x0, y0) == Point2D(x1, y1)) is True
        assert (Point2D(x0, y0) != Point2D(x1, y1)) is False

        assert (Point2D(x0, y0) <  Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) <= Point2D(x1, y1)) is True
        assert (Point2D(x0, y0) >  Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) >= Point2D(x1, y1)) is True
    else:
        assert (Point2D(x0, y0) == Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) != Point2D(x1, y1)) is True

    if x0 < x1 or x0 == x1 and y0 < y1:
        assert (Point2D(x0, y0) <  Point2D(x1, y1)) is True
        assert (Point2D(x0, y0) <= Point2D(x1, y1)) is True
        assert (Point2D(x0, y0) >  Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) >= Point2D(x1, y1)) is False

    if x0 > x1 or x0 == x1 and y0 > y1:
        assert (Point2D(x0, y0) <  Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) <= Point2D(x1, y1)) is False
        assert (Point2D(x0, y0) >  Point2D(x1, y1)) is True
        assert (Point2D(x0, y0) >= Point2D(x1, y1)) is True
