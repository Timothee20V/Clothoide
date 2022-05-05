from matplotlib.pyplot import *
from scipy.integrate import quad
from math import *

def fonctionx(s):
    x = cos((s ** 2) / (2 * a))
    return x

def fonctiony(s):
    y = sin((s ** 2) / (2 * a))
    return y

def efneivnie():


def clothoide(T, precision):
    liste_x = []
    liste_y = []
    varT = abs(T)

    while T < varT:
        x, err1 = quad(fonctionx, 0, T)
        y, err2 = quad(fonctiony, 0, T)
        liste_x.append(x)
        liste_y.append(y)
        T = T + precision

    return liste_x, liste_y


def longueur_clothoide(liste1, liste2):
    longueur = 0
    for i in range(0,len(liste1)-1):
        longueur = longueur + sqrt((liste1[i+1]-liste1[i])**2 + (liste2[i+1]-liste2[i])**2)
    return longueur


title("Clothoïde")

a = 100

X, Y = clothoide(T=-100, precision=1)
print(X, Y)
print(longueur_clothoide(X, Y))
print(len(X), len(Y))
plot(X, Y, '-0', color='red')
axis('equal')
show()
