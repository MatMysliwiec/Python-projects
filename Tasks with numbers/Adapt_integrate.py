import math


def s3(a, b, fa, fb, hmin3=1 / 100):
    global N
    c = (a + b) / 2
    h = b - a
    fc = f(c)

    if h > hmin3:
        left = s3(a, c, fa, fc, hmin3)
        right = s3(c, b, fc, fb, hmin3)
        result = left + right
        N += 1
    else:
        result = (fa + 4 * fc + fb) * h / 6

    return result


def s5(a, b, fa, fb, hmin5=1 / 100):
    global M
    h = b - a
    c0 = (a + b) / 2
    cl = (a + c0) / 2
    cr = (c0 + b) / 2
    fl = f(cl)
    f0 = f(c0)
    fr = f(cr)

    if h > hmin5:
        left = s5(a, c0, fa, f0, hmin5)
        right = s5(c0, b, f0, fb, hmin5)
        result = left + right
        M += 1
    else:
        result = h / 90 * (7 * fa + 32 * fl + 12 * f0 + 32 * fr + 7 * fb)

    return result


def f(x):
    return math.cos(x)


N = 0
M = 0
a = 0
b = math.pi
fa = f(a)
fb = f(b)

result1 = s3(a, b, fa, fb)
result2 = s5(a, b, fa, fb)
print(N, M)
print("-" * 45)
print("Compere result using 3 and 5 points integrators")
print("-" * 45)
print('Exact value ', math.sin(b) - math.sin(a))
print(f'3 points integrator: {result1}, iterations: {N}')
print(f' points integrator: {result2}, iterations: {M}')
print('Relative error', abs(result1 - result2))
