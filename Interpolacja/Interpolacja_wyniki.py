from Interpolacja.FunkcjaSin import KSin, Pipol
from Interpolacja import interpol

import matplotlib.pyplot as plt


def Kread(source):
    with open(source, 'r') as file:
        lines = file.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
    return x, y


plik = 'dane.txt'
x, y = Kread(plik)
n = 5
x0 = 3.0 / 5.0
idx = [0, 1, 2, 3, 4]
x_wezly = [x[i] for i in idx]
y_wezly = [y[i] for i in idx]
linia = "-" * 45
print(linia)
print('Test działania programu')
print(linia)
xy = list(map(list, zip(x_wezly, y_wezly)))
y0 = interpol(x0, xy)

print(f'Wartość wyliczona za pomoca programu: {y0}')
print(f'Wartość dokładna ', KSin(x0))
print('Błąd względny ', abs(KSin(x0) - y0))

x_rz = [Pipol * k / (12 * n - 1) for k in range(0, 15 * n, 2)]
x_int = [Pipol * k / (12 * n - 1) for k in range(1, 15 * n, 2)]

y_rz = [KSin(phi) for phi in x_rz]
y_int = [interpol(phi, xy) for phi in x_int]

plt.scatter(x, y, color='black', s=30, label='Wezły')
plt.scatter(x_rz, y_rz, color='black', s=1, label='Dane dokładne')
plt.scatter(x_int, y_int, color='red', s=1, label=f'Interpolacja ({n} węzłów)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolacja Lagrange\'a')
plt.show()
