def selectsort0(xs):
    for i in range(len(xs) - 1):
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[i]: xs[i], xs[j] = xs[j], xs[i]

def selectsort1(xs):
    for i in range(len(xs) - 1):
        j = i + 1 + xs[i + 1:].index(min(xs[i + 1:]))

        if xs[j] < xs[i]:
            xs[i], xs[j] = xs[j], xs[i]
