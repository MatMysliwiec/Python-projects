from Square import Ksqrt as sqrt
from mpmath import mp, sqrt

def pi_Gauss_Legendre():
    iterations = 10000
    mp.dps = iterations + 2
    an = mp.mpf(1.0)
    bn = mp.mpf(1.0) / sqrt(2)
    tn = mp.mpf(0.25)
    pn = mp.mpf(1.0)
    a_pom = mp.mpf(1.0)

    for i in range(iterations):
        a_pom = an
        an = (an + bn) / 2
        bn = sqrt(a_pom * bn)
        tn = tn - pn * (a_pom - an)**2
        pn *= 2

    return (an + bn)**2 / (4.0 * tn)

def validate():

    while True:
        s = input("Digits of pi: ")
        try:
            digits = int(s)
            if digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("Enter a nonnegative integer.")

digits = validate()
pi = pi_Gauss_Legendre()
formatted_pi = "{:.{}f}".format(float(pi), digits)
print(formatted_pi)