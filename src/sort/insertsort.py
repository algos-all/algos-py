def insertsort0(xs):
    for i in range(1, len(xs)):
        for j in range(i, 0, -1):
            if xs[j - 1] <= xs[j]: break

            xs[j - 1], xs[j] = xs[j], xs[j - 1]

def insertsort1(xs):
    for i in range(1, len(xs)):
        for j in range(i, 0, -1):
            if xs[j - 1] > xs[j]:
                xs[j - 1], xs[j] = xs[j], xs[j - 1]
            else:
                break

def insertsort2(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
