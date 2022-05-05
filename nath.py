from matplotlib.pyplot import *
from math import *

# methode d'euler avec dvpt limité
#http://2.3jachtuches.pagesperso-orange.fr/dossiers/semi/semi.htm
liste_x1 = [0, 0.001]
liste_y = [0, 0.00001]


def distance(x1, x2, y1, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


def dvpt_limite_de_x(s, nmax):
    x = 0
    for n in range(0, nmax):
        x += (((-1) ** n) * s ** (4 * n + 1)) / (factorial(2 * n) * (4 * n + 1) * 2 ** (2 * n))
    return x


def dvpt_limite_de_y(s, nmax):
    y = 0
    for n in range(0, nmax):
        y += (((-1) ** n) * s ** (4 * n + 3)) / (factorial(2 * n + 1) * (4 * n + 3) * 2 ** (2 * n + 1))
    return y


t = 10
precision_du_devpt_limité = 1
i = 0
s = 0

while i < 500:
    x1 = dvpt_limite_de_x(s, precision_du_devpt_limité)
    s += distance(liste_x1[i], liste_x1[1 + i], liste_y[i], liste_y[1 + i])
    print(s)
    y = dvpt_limite_de_y(s, precision_du_devpt_limité)
    liste_x1.append(x1)
    liste_y.append(y)
    i += 1

print(liste_x1)
print(liste_y)
plot(liste_x1, liste_y, '-0', color='red')

show()
