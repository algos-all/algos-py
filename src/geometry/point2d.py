def rotation_sign(x0, y0, x1, y1, x2, y2):
    '''
    Computes the sign of the cross product between two adjacent vectors.
    Corresponds to the direction of rotation for the angle formed by:
    (x0, y0) -> (x1, y1) -> (x2, y2)

    :return: +1 for clockwise, -1 for counter-clockwise and 0 for collinear
    '''

    # There are many ways to represent/rearrange the formula for result
    # Often, the formula with just two multiplications is picked.
    # The one below is the determinant of this orientation matrix:
    # x0, y0, 1
    # x1, y1, 1
    # x2, y2, 1
    # The matrix comes from the cross-product and the explanation is :(

    result = (y1 - y2) * x0 + (y2 - y0) * x1 + (y0 - y1) * x2

    return 0 if result == 0 else 1 if result < 0 else -1


def cw(x0, y0, x1, y1, x2, y2):
    return rotation_sign(x0, y0, x1, y1, x2, y2)


def ccw(x0, y0, x1, y1, x2, y2):
    result = rotation_sign(x0, y0, x1, y1, x2, y2)
    return 0 if result == 0 else 1 if result == -1 else -1


class Point2D:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.i = 0
        self.coords = [x, y]

    def __iter__(self):
        return self

    def __next__(self):

        if self.i == 2:
            self.i = 0

            raise StopIteration

        coord = self.coords[self.i]

        self.i += 1
        return coord


def rotation_sign_2d(point0: Point2D, point1: Point2D, point2: Point2D):
    x0, y0 = point0
    x1, y1 = point1
    x2, y2 = point2

    return compute_rotation_sign(x0, y0, x1, y1, x2, y2)


def cw(point0: Point2D, point1: Point2D, point2: Point2D):
    return rotation_sign(point0, point1, point2)


def ccw(point0: Point2D, point1: Point2D, point2: Point2D):
    result = rotation_sign(point0, point1, point2)
    return 0 if result == 0 else 1 if result == -1 else -1


if __name__ == '__main__':
    print('testing points...')
    p = Point2D(1, 2)

    x, y = p

    print(x, y)
