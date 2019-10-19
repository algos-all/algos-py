import cmath

def fft0(xs):
    n, ys = len(xs), []

    for i in range(n):
        yi = complex(0, 0)

        for j in range(n):
            yi += complex(xs[j]) * cmath.exp(complex(0, -2 * cmath.pi / n * i * j))

        ys.append(yi)

    return ys

if __name__ == '__main__':
    print(fft0([1, 2, 3]))
