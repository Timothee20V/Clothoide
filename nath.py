from matplotlib.pyplot import *
from math import *


# methode d'euler avec dvpt limité
# http://2.3jachtuches.pagesperso-orange.fr/dossiers/semi/semi.htm


def distance(x1, x2, y1, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


def dvpt_limite_de_x(s, nmax):
    x = 0
    for n in range(0, nmax):
        x += ((-1) ** n) * ((pi / 2) ** (2 * n)) * (1 / factorial(2 * n)) * ((s ** (4 * n + 1)) / (4 * n + 1))
    return x


def dvpt_limite_de_y(s, nmax):
    y = 0
    for n in range(0, nmax):
        y += ((-1) ** n) * ((pi / 2) ** (2 * n + 1)) * (1 / factorial(2 * n + 1)) * ((s ** (4 * n + 3)) / (4 * n + 3))
    return y


def A_angot(s, nmax):
    a = 0
    for n in range(0, nmax):
        a += ((-1) ** (n + 1)) * (1.5 * (4 * n + 1)) / ((pi * s ** 2) ** (2 * n + 1))
    return a


def B_angot(s, nmax):
    b = 0
    for n in range(0, nmax):
        b += ((-1) ** (n + 1)) * (1.5 * (4 * n - 1)) / ((pi * s ** 2) ** (2 * n))
    return b


def x_par_angot(s, nmax):
    return (1 / 2 + A_angot(s, nmax) * (cos((pi * s ** 2) / 2) / (pi * s)) - B_angot(s, nmax) * (
            (sin((pi * s ** 2) / 2)) / (pi * s)))


def y_par_angot(s, nmax):
    return (1 / 2 + A_angot(s, nmax) * (sin((pi * s ** 2) / 2) / (pi * s)) - B_angot(s, nmax) * (
            (cos((pi * s ** 2) / 2)) / (pi * s)))


ω = 10

w = np.arange(0, ω, 0.01)

liste_x1 = []
liste_y = []
precision_du_devpt_limité = 300
A = 1

for i in range(len(w)):
    '''liste_x1.append(dvpt_limite_de_x(w[i], precision_du_devpt_limité))
    liste_y.append(dvpt_limite_de_y(w[i], precision_du_devpt_limité))'''
    liste_x1.append(x_par_angot(w[i], precision_du_devpt_limité))
    liste_y.append(y_par_angot(w[i], precision_du_devpt_limité))

print(liste_x1)
print(liste_y)
plot(liste_x1, liste_y, '-0', color='red')
# plot(w, liste_y, '-0', color='blue')
axis("equal")

show()
