def findZeroWithBisection(f, x0, x1, epsilon):
    a = f(x0)
    if a * f(x1) > 0:
        return None
    while True:
        if x1 - x0 < epsilon:
            return (x1 + x0) / 2.0
        mid = (x1 + x0) / 2.0
        if f(mid) == 0:
            return mid
        if (f(mid) * a) > 0:  # see [mid, x1]
            x0 = mid
        elif (f(mid) * a) < 0:  # see [x0, mid]
            x1 = mid


def almostEqual(d1, d2, epsilon=10 ** -7):  # helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
    # return math.isclose(d2, d1, abs_tol=epsilon)


def f1(x): return x * x - 2  # root at x=sqrt(2)


def f2(x): return x ** 2 - (x + 1)  # root at x=phi


def f3(x): return x ** 5 - 2 ** x  # f(1)<0, f(2)>0


if __name__ == '__main__':
    print('Testing findZeroWithBisection()... ', end='')
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert (almostEqual(x, 1.41421356192))
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert (almostEqual(x, 1.61803398887))
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert (almostEqual(x, 1.17727855081))
    print('Passed.')
