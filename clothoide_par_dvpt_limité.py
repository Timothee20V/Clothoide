from matplotlib.pyplot import *
from math import *
import scipy.special as sy  # pour les facorielles

'''methode d'euler avec dvpt limité'''

'''developement de coordonnée de x de la courbes en fonction de l'abscisse curviligne'''


def dvpt_limite_de_x(s, nmax):
    x = 0
    for n in range(0, nmax):
        x += ((-1) ** n) * ((pi / 2) ** (2 * n)) * (1 / (sy.factorial(2 * n))) * ((s ** (4 * n + 1)) / (4 * n + 1))
    return x


'''developement de coordonnée de y de la courbes en fonction de l'abscisse curviligne'''


def dvpt_limite_de_y(s, nmax):
    y = 0
    for n in range(0, nmax):
        y += ((-1) ** n) * ((pi / 2) ** (2 * n + 1)) * (1 / (sy.factorial(2 * n + 1))) * (
                    (s ** (4 * n + 3)) / (4 * n + 3))
    return y

'''liste de point de 0 à 6 avec 0.01 d'ecart entre chaque'''
w = np.arange(0, 6, 0.01)

liste_x1 = []
liste_y = []
'''precision du dvpt ne peut pas aller au dessus de 115 sinon erreure'''
precision_du_devpt_limité = 115
'''coefficient A regle la taille de la clothoide '''
A = 1

'''création de tout les points de la liste'''
for i in range(len(w)):
    liste_x1.append(dvpt_limite_de_x(w[i], precision_du_devpt_limité))
    liste_y.append(dvpt_limite_de_y(w[i], precision_du_devpt_limité))

liste_x1 = [i for i in liste_x1 if i != "nan"]
liste_y = [i for i in liste_y if i != "nan"]

print(liste_x1)
print(liste_y)
plot(liste_x1, liste_y, '-0', color='red')
# plot(w, liste_y, '-0', color='blue')
axis("equal")

show()
