from math import *


class Vect:
    def __init__(self, x1, y1, x2, y2, genre):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = x2 - x1
        self.y = y2 - y1
        self.genre = genre

    def affiche(self):
        print(self.x, self.y, self.genre)

    def __sub__(self, other):
        if self.genre == "vecteur" and other.genre == "vecteur":
            return Vect(self.x - other.x, self.y - other.y, genre="vecteur")

    def produit_scalaire(self, other):
        val = self.x * other.x + self.y * other.y
        return val

    def norme(self):
        if self.genre == "vecteur":
            val = sqrt((self.x ** 2 + self.y ** 2))
            return val

    def angle(self, other):
        if (self.genre and other.genre) == 'vecteur':
            scalaire = self.produit_scalaire(other)
            BA = self.norme()
            BC = other.norme()
            print(BA, BC)
            angle_rad = acos(scalaire / (BA * BC))
            angle_deg = 360 * angle_rad / (2 * pi)
            return angle_deg


AB = Vect(0,0,5,5,'vecteur')
CB = Vect(0,0,-5,5,'vecteur')
print(AB.x, AB.y)
print(CB.x, CB.y)
print(AB.produit_scalaire(CB))
print(AB.angle(CB))


