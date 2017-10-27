import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line2D:

    def __init__(self, p0: Point2D, p1: Point2D):
        self.p0 = p0
        self.p1 = p1

        self.A = None
        self.B = None
        self.C = None

def compute_standard_line(x0, y0, x1, y1):
    '''
    Computes the coefficients of Ax + By + C = 0 given two plane points.

    :return: a tuple (A, B, C); it is (0, 0, 0) if both points are the same
    '''

    return y0 - y1, x1 - x0, (x0 - x1) * y0 + (y1 - y0) * x0

def compute_dot_product(ps, qs, sum=sum):
    '''
    Computes the dot product of two vectors.

    :ps: the nnlist of coordinates of the first vector
    :qs: the list of coordinates of the second vector
    :sum: consider using math.fsum if you need to sum over many floats
    :return: a single scalar, the dot product
    '''

    assert len(ps) == len(qs), 'arguments must have the same length'

    return sum(p * q for p, q in zip(ps, qs))

def compute_sign(x0, y0, x1, y1, x2, y2):
    '''
    Computes the sign of the cross product between two adjacent vectors.

    :return: +1 for clockwise, -1 for counter-clockwise and 0 for collinear
    '''

    # There are many ways to represent/rearrange the formula for result
    # Often, the formula with just two multiplications is picked.
    # The one below is the determinant of this orientation matrix:
    # [[x0, y0, 1],
    #  [x1, y1, 1],
    #  [x2, y2, 1]]
    # The matrix comes from the cross-product and the explanation is :(

    result = (y1 - y2) * x0 + (y2 - y0) * x1 + (y0 - y1) * x2

    return 0 if result == 0 else 1 if result < 0 else -1
