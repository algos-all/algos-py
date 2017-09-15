def compute_standard_line(x0, y0, x1, y1):
    return y0 - y1, x1 - x0, (y0 - y1) * x0 + (x1 - x0) * y0
