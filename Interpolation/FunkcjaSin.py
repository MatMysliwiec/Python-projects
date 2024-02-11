from math import sin, sqrt
import timeit

Pi = float(3.1415926535897932)
Pipol = float(1.5707963267948966)
Dwapi = 2.0 * Pi


def KSin(x):
    delta = float(x)
    deltamax = Pipol / 30.0
    sgn = 1

    if delta < 0.0:
        delta, sgn = -delta, -1

    delta = delta % Dwapi

    if delta > Pi:
        delta, sgn = delta - Pi, -sgn

    if delta > Pipol:
        delta = Pi - delta

    sqr = False

    if delta > Pipol / 2.0:
        sqr, delta = True, Pipol - delta

    k = 3
    if delta < 0.2958361062:
        k = 2
    if delta < 0.111414931009:
        k = 1
    if delta < 0.041960012965:
        k = 0

    delta = delta / (3.0 ** k)
    deltasq = delta * delta
    s = delta * (1.0 + (deltasq * (-1.0 + (deltasq * (1.0 - deltasq / 42.0)) / 20.0)) / 6.0)

    for i in range(1, k + 1):
        s = 4.0 * s * (0.75 - s * s)

    if sqr: s = sqrt(1.0 - s * s)

    err = 3 ** k * delta ** 5 / 120
    return sgn * s


def KRad(i):
    Rad = i * 0.01745329251
    return Rad

'''
f = open('wynik.txt', 'w')
linia = 120 * "-"
print(linia)
print("\t", "x[deg]", "\t", "x[rad]", "\t", "sin(x)", "\t", "KSin(x)", "\t", "Err")
for i in range(0, 901, 1):
    rad = i * 0.01745329251
    krok = i / 10
    Sinnum = KSin(krok)
    Sinteo = sin(krok)
    blad = abs(Sinnum - Sinteo)
    print(f"\t{krok:2}\t{KRad(i):.8f}\t{Sinteo:.18f}\t{Sinnum:.18f}\t{blad:.18f}")
    f.write(f"{krok:2}\t{KRad(i):.8f}\t{Sinteo:.18f}\t{Sinnum:.18f}\t{blad:.18f}\n")
print(linia)
f.close()

print("Test czasu działania programu")
print(linia)
start = timeit.default_timer()
for i in range(0, 10000, 1):
    KSin(90.0)

print("Czas trwania programu KSin", timeit.default_timer() - start)
start2 = timeit.default_timer()
for i in range(0, 10000, 1):
    sin(90.0)

print("Czas trwania programu sin z biblioteki math", timeit.default_timer() - start2)
'''