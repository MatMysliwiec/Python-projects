import math
import timeit

def pier(s, delta=1e-14):
    x = s
    while abs(x * x - s) > delta:
        x = 0.5 * (x + s / x)
    return x

def Ksqrt(a, delta = 1e-14):
    x , tmp = a, 1
    tmp = 1
    while abs(x - tmp) > delta:
        x = 0.5 * (x +tmp)
        tmp = a/x
    return x
'''
N=0
M=0

i = 19.0
start1 = timeit.default_timer()
wynik1 = pier(i)
end1 = timeit.default_timer()
czas1 = end1 - start1

start2 = timeit.default_timer()
wynik2 = Ksqrt(i)
end2 = timeit.default_timer()
czas2 = end2 - start2

linia="-"*65
print(linia)
print("Porównanie działania programów")
print(linia)
print(f'Pierwsza metoda: {wynik1}, iteracji = {N}, czas trwania: {czas1}')
print(f'Druga metoda: {wynik2}, iteracji = {M}, czas trwania: {czas2}')
print('Błąd względny metod', abs(wynik1-wynik2))
print('Różnica czasu trwania', abs(czas2-czas1))
wynik = math.sqrt(i)
print(f'Dokładny wynik: {wynik}')
plik = open('wynik6.txt','w')
for i in range(1,61):
    startw1 = timeit.default_timer()
    wiel1 = pier(i)
    endw1 = timeit.default_timer()
    czasw1 = abs(endw1-startw1)
    startw2 = timeit.default_timer()
    wiel2 = Ksqrt(i)
    endw2 = timeit.default_timer()
    czasw2 = abs(endw2-startw2)
    wynikteo = math.sqrt(i)
    bladm1 = abs(wiel1-wynikteo)
    bladm2 = abs(wiel2-wynikteo)
    bladm = abs(wiel1-wiel2)
    plik.write(f'{i}\t{czasw1}\t{N}\t{czasw2}\t{M}\t{bladm1:0,.15f}\t{bladm2:0,.15f}\t{bladm:0,.15f}\n')
plik.close()
'''