import pytest

from src.geometry.line2d import Line2D
from src.geometry.point2d import Point2D, cw
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


lft = -2
rgt = +2

@pytest.mark.parametrize('x0', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y0', [y for y in range(lft, rgt)])
@pytest.mark.parametrize('x1', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y1', [y for y in range(lft, rgt)])
@pytest.mark.parametrize('x2', [x for x in range(lft, rgt)])
@pytest.mark.parametrize('y2', [y for y in range(lft, rgt)])
def test_convhull2d_3(x0, y0, x1, y1, x2, y2):
    point0 = Point2D(x0, y0)
    point1 = Point2D(x1, y1)
    point2 = Point2D(x2, y2)

    points = sorted([point0, point1, point2])

    hull = ConvexHull2D([point0, point1, point2])

    if points[0] == points[1] and points[1] == points[2]:
        assert len(hull) == 1

        assert hull[0] == point0
    elif points[0] == points[1] or points[1] == points[2]:
        assert len(hull) == 2

        assert hull[0] == points[0]
        assert hull[1] == points[2]
    else:
        line = Line2D(point0, point1)

        if line.A * point2[0] + line.B * point2[1] + line.C == 0:
            assert len(hull) == 2

            assert hull[0] == points[0]
            assert hull[1] == points[2]
        else:
            assert len(hull) == 3

            assert cw(hull[0], hull[1], hull[2]) == 1
            assert cw(hull[1], hull[2], hull[0]) == 1
            assert cw(hull[2], hull[0], hull[1]) == 1
