from math import *


class Vect:
    def __init__(self, x1, y1, x2, y2, genre):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = x2 - x1
        self.y = y2 - y1
        self.norme = sqrt((self.x ** 2 + self.y ** 2))
        self.genre = genre

    def __mul__(self, other):
        if self.genre == "vecteur":
            return Vect(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other, genre="vecteur")

    def produit_scalaire(self, other):
        if (self.genre and other.genre) == 'vecteur':
            val = self.x * other.x + self.y * other.y
            return val

    def angle(self, other):
        if (self.genre and other.genre) == 'vecteur':
            scalaire = self.produit_scalaire(other)
            BA = self.norme
            BC = other.norme
            angle_rad = acos(scalaire / (BA * BC))
            angle_deg = 360 * angle_rad / (2 * pi)
            return angle_deg