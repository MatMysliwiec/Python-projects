from math import sin

sq35 = 0.774596669241483377035853
sq51 = 0.538469310105683091036314  # sq51:=(1/3)*sqrt(5-2*sqrt(10/7))
sq52 = 0.906179845938663992797627  # sq52:=(1/3)*sqrt(5+2*sqrt(10/7))
w0 = 0.568888888888888888888889  # w0:=128/255
w1 = 0.478628670499366468041292  # w1:=161/450+(13/90)*sqrt(7/10)
w2 = 0.236926885056189087514264  # w2:=161/450-(13/90)*sqrt(7/10)


def KGauss5_(a, b, f):
    x0 = (a + b) / 2
    h0 = b - x0
    h1 = sq51 * h0
    h2 = sq52 * h0
    xRL, xRR = x0 + h1, x0 + h2
    xLL, xLR = x0 - h2, x0 - h1
    return h0 * (w2 * (f(xLL) + f(xRR)) + w1 * (f(xLR) + f(xRL)) + w0 * f(x0))


def KGauss3_(a, b, f):
    x0 = (a + b) / 2
    h0 = b - x0
    h = sq35 * h0
    return h0 * (5 * (f(x0 - h) + f(x0 + h)) + 8 * f(x0)) / 9


def KGauss36_adapt(a, b, func, eps=1.0e-8):
    global ntimes_dev, ntimes_stop
    c = (a + b) / 2
    S3 = KGauss3_(a, b, func)
    S6 = KGauss3_(a, c, func) + KGauss3_(c, b, func)
    Integ = (64 * S6 - S3) / 63
    if abs(S6 - S3) > eps * abs(S3 - 64 * S6) / 400:
        ntimes_dev += 1
        return KGauss36_adapt(a, c, func, eps) + KGauss36_adapt(c, b, func, eps)
    else:
        ntimes_stop += 1
        return Integ


pi = 3.14159265358979323846264
ln2 = 0.693147180559945309417232
ln10 = 2.30258509299404568401799
sin2 = 157.079632679489661923132


def f(x):
    return 4 / (1 + x * x)


print("4/(1+x*x),{x,0,1}")
print("Wartość teoretyczna = ", pi)
print('Integ', 'rel_err', 'ntimes', sep='\t')
ntimes_dev = 0
ntimes_stop = 0
S = KGauss36_adapt(0, 1, f, 1e-8)
print(S, (S - pi) / pi, ntimes_dev, ntimes_stop, sep='\t')
print(" ")


def f(x):
    return 1 / x


print("1/x,{x,1,2}")
print("Sin[x]**2,{x,0,100*Pi}")
print("Wartość teoretyczna = ", ln2)
print('Integ', 'rel_err', 'ntimes', sep='\t')
ntimes_dev = 0
ntimes_stop = 0
S = KGauss36_adapt(1, 2, f, 1e-11)
print(S, (S - ln2) / ln2, ntimes_dev, ntimes_stop, sep='\t')
print(" ")

print("1/x,{x,1,10}")
print("Wartość teoretyczna = ", ln10)
print('Integ', 'rel_err', 'ntimes', sep='\t')
ntimes_dev = 0
ntimes_stop = 0
S = KGauss36_adapt(1, 10, f, 1e-11)
print(S, (S - ln10) / ln10, ntimes_dev, ntimes_stop, sep='\t')
print(" ")


def f(x):
    return sin(x) ** 2


print("Sin[x]**2,{x,0,100*Pi}")
print("Wartość teoretyczna = ", sin2)
print('Integ', 'rel_err', 'ntimes', sep='\t')
ntimes_dev = 0
ntimes_stop = 0
S = KGauss36_adapt(0, 100 * pi, f, 1e-11)
print(S, "0.0", ntimes_dev, ntimes_stop, sep='\t')
print(" ")
