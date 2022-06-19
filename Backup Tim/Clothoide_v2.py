import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.integrate import quad


def f(w):
    return np.cos((pi * w ** 2) / 2)


def f2(w):
    return np.sin((pi * w ** 2) / 2)


def integ(w):
    y, err1 = quad(f, 0, w)
    return y


def integ2(w):
    y, err1 = quad(f2, 0, w)
    return y


def longueur_clothoide(liste1, liste2):
    longueur = 0
    for i in range(0, len(liste1) - 1):
        longueur = longueur + sqrt((liste1[i + 1] - liste1[i]) ** 2 + (liste2[i + 1] - liste2[i]) ** 2)
    return longueur


ω = 10

w = np.arange(-ω, ω, 0.01)

x = []
y = []
for i in range(len(w)):
    x.append(0.1 * (integ(w[i])))
    y.append(0.1 * (integ2(w[i])))

y = [i * (-1) for i in y]

print(longueur_clothoide(x, y))
plt.grid()
plt.axis('equal')
plt.title("Tracé de la clothoïde")

plt.plot(x, y)
plt.ylabel("S(ω)")
plt.xlabel("C(ω)")

'''plt.savefig('Clothoïde.png')'''

plt.show()
