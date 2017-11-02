from src.geometry.point2d import Point2D


def dot_product(ps, qs, sum=sum):
    '''
    Computes the dot product of two vectors.

    :ps: the nnlist of coordinates of the first vector
    :qs: the list of coordinates of the second vector
    :sum: consider using math.fsum if you need to sum over many floats
    :return: a single scalar, the dot product
    '''

    assert len(ps) == len(qs), 'arguments must have the same length'

    return sum(p * q for p, q in zip(ps, qs))


def standard_line(x0, y0, x1, y1):
    '''
    Computes the coefficients of Ax + By + C = 0 given two plane points.

    :return: a tuple (A, B, C); it is (0, 0, 0) if both points are the same
    '''

    return y0 - y1, x1 - x0, (x0 - x1) * y0 + (y1 - y0) * x0


class Line2D:

    def __init__(self, point0: Point2D, point1: Point2D):
        '''
        Construct a line using two *distinct* points

        :raises RuntimeError: if provided points are the same
        '''

        x0, y0 = point0
        x1, y1 = point1

        self.A, self.B, self.C = standard_line(x0, y0, x1, y1)

        if self.A == 0 and self.B == 0 and self.C == 0:
            # TODO: use custom errors?
            message = 'Cannot construct line: points are the same'
            raise RuntimeError(message)

    def __iter__(self):
        return self

    def __next__(self):

        if self.i == 4:
            self.i = 0

            raise StopIteration

        coef = self.coefs[self.i]

        self.i += 1
        return coef


class Segment2D:

    def __init__(self, point0: Point2D, point1: Point2D):
        '''
        Constructs a line segment using two *distinct* points

        :raises RuntimeError: if provided points are the same
        '''

        self.p0 = p0
        self.p1 = p1

        self.line = Line2D(point0, point1)


def compute_line_intersection_2d(line0: Line2D, line1: Line2D):
    A0, B0, C0 = line0
    A1, B1, C1 = line1

    x = A1 * B0 - A0 * B1

    if x == 0:
        # line0 and line1 do not intersect
        # they are either the same or parallel
        return None

    return Point2D((B0 * C1 - B1 * C0) / x, (A1 * C0 - A0 * C1) / x)
