lge = 0.434294481903251827651128918916605082
ln10 = 2.30258509299404568401799145468436421
euler = 2.71828182845904523536028747135266250
euler2 = 7.38905609893065022723042746057500781
ieuler = 0.367879441171442321595523770161460867
ieuler2 = 0.135335283236612691893999494972484403


def Kexp(x):  # wersja pełna
    n = round(x)
    dx = x - n
    m = round(n * lge)
    dy = n * lge - m
    p = round(dx + dy * ln10)
    dz = dx + dy * ln10 - p
    ep = {2: euler2, 1: euler, -1: ieuler, -2: ieuler2}.get(p, 1)
    tmp = atnexp(dz / 3)
    tmp2 = tmp * tmp
    return float(str(1) + "e" + str(m)) * tmp2 * tmp * ep


def atnexp(x):  # n=len(atn) ==> atnexp(x)-exp(x) = O(2*n+3)
    atn = [1 / 12, 1 / 10, 17 / 168, 31 / 306, 691 / 6820, 5461 / 53898]
    x2 = x * x
    atn = [-x2 * val for val in atn]
    j = len(atn) - 1
    a = 1 + atn[-1]
    while j > 0:
        a = 1 + a * atn[j - 1]
        j -= 1
    a = a * x / 2
    return (1 + a) / (1 - a)
