import math


def S3(a, b, fa, fb, hmin3=1 / 100):
    global N
    c = (a + b) / 2
    h = b - a
    fc = f(c)

    if h > hmin3:
        lewa = S3(a, c, fa, fc, hmin3)
        prawa = S3(c, b, fc, fb, hmin3)
        wynik = lewa + prawa
        N += 1
    else:
        wynik = (fa + 4 * fc + fb) * h / 6

    return wynik


def S5(a, b, fa, fb, hmin5=1 / 100):
    global M
    h = b - a
    c0 = (a + b) / 2
    cL = (a + c0) / 2
    cR = (c0 + b) / 2
    fL = f(cL)
    f0 = f(c0)
    fR = f(cR)

    if h > hmin5:
        lewa = S5(a, c0, fa, f0, hmin5)
        prawa = S5(c0, b, f0, fb, hmin5)
        wynik = lewa + prawa
        M += 1
    else:
        wynik = h / 90 * (7 * fa + 32 * fL + 12 * f0 + 32 * fR + 7 * fb)

    return wynik


def f(x):
    return math.cos(x)


N = 0
M = 0
a = 0
b = math.pi
fa = f(a)
fb = f(b)

result1 = S3(a, b, fa, fb)
result2 = S5(a, b, fa, fb)
linia = "-" * 45
print(N, M)
print(linia)
print("Porównania działania integratorów 3 i 5 punktowego")
print(linia)
print('Wartosc dokładna ', math.sin(b) - math.sin(a))
print(f'Intergrator 3 punktowy: {result1}, iteracje: {N}')
print(f'Integrator 5 punktowy: {result2}, iteracje: {M}')
print('Błąd względny metod', abs(result1 - result2))
