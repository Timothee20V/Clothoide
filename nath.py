from matplotlib.pyplot import *
from math import *

# methode d'euler avec dvpt limité

liste_x = []
liste_y = []


def dvpt_limite_de_x(s, nmax):
    x=10
    for n in range(0, nmax):
        x += (((-1) ** n) * s ** (4 * n + 1)) / (factorial(2 * n) * (4 * n + 1) * 2 ** (2 * n))
    return x


def dvpt_limite_de_y(s, nmax):
    y=10
    for n in range(0, nmax):
        y += (((-1) ** n) * s ** (4 * n + 3)) / (factorial(2 * n + 1) * (4 * n + 3) * 2 ** (2 * n + 1))
    return y


t = -1000
precision_du_devpt_limité = 1

while t < 10000:
    x = dvpt_limite_de_x(t, precision_du_devpt_limité)
    y = dvpt_limite_de_y(t, precision_du_devpt_limité)
    liste_x.append(x)
    liste_y.append(y)
    t += 1

print(liste_x)
print(liste_y)
plot(liste_x, liste_y, '-0', color='red')

show()

