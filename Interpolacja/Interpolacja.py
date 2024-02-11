def interpol(x0, xy):
    n = len(xy)
    t = [0] * n
    x = [elm[0] for elm in xy]
    y = [elm[1] for elm in xy]

    for i in range(n):
        t[i] = y[i]
        for k in range(i - 1, -1, -1):
            t[k] = t[k] + (t[k + 1] - t[k]) * (x0 - x[k]) / (x[i] - x[k])
    return t[0]


'''
x = [KRad(0),KRad(30),KRad(45),KRad(60),KRad(90)]
y = [KSin(KRad(0)),KSin(KRad(30)),KSin(KRad(45)),KSin(KRad(60)),KSin(KRad(90))]

x0 = 1/3
xy=list(map(list,zip(x,y)))
wynik = interpol(x0,xy)

print("Wynik ze wzoru = ", wynik)
print("Wynik z biblioteki = ",math.sin(x0))
print("Bład = ",abs(wynik - math.sin(x0)))
'''
