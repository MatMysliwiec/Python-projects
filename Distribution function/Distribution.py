from FunkcjaExp import Kexp as exp
from Adapt53 import KAdapt53

from math import erf as erf_m
from scipy.special import erf as erf_s

const = 0.398942280401432677939946
sqrt2 = 1.41421356237309504880169
eps = 10 ** (-14)
n_max = 7


def f(x):
    return exp(-x * x / 2.0)


def S(a, b):
    c = (a + b) / 2.
    return KAdapt53(a, c, b, f(a), f(c), f(b), f, eps)


def I(k):
    return S(k - 1, k) if (isinstance(k, int) and k > 0) else 0.


J = (n_max + 1) * [0]
for n in range(1, n_max + 1):
    J[n] = J[n - 1] + I(n)


def dystrybuanta(x):
    xabs = abs(x)
    n = int(xabs)
    dJ = S(n, xabs) if xabs > n else 0.
    res = 0.5 + const * (J[n] + dJ)
    return res if x > 0 else 1.0 - res


def fmt(num, dl=14):
    string = (str(round(abs(num), dl)) + "0" * dl)[0:dl + 2]
    return " " + string if num >= 0 else "-" + string


with open('tabela_dystrybuanta_erf.txt', 'w') as tabela:
    print('x>0', '\t', 'Erf(x)', '\t', 'erf(x/sqrt2)', '\t\t', 'math.py', '\t', 'sci.py', '\t', 'm.py-sci.py-',
          file=tabela)
    '''for i in range(-20,20*n_max+1):'''
    for i in range(-200, 200):
        x = 0.02 * i
        y = dystrybuanta(x)
        print(fmt(x, 2), fmt(y), fmt(2 * y - 1), '\t', format((2 * y - 1) - erf_m(x / sqrt2), '.1e'), '\t',
              format((2 * y - 1) - erf_s(x / sqrt2), '.1e'), '\t', format(erf_m(x / sqrt2) - erf_s(x / sqrt2), '.1e'),
              file=tabela)
