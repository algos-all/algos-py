def compute_standard_line(x0, y0, x1, y1):
    '''
    Computes the coefficients of Ax + By + C = 0 given two plane points.
    '''

    return y0 - y1, x1 - x0, (x0 - x1) * y0 + (y1 - y0) * x0
