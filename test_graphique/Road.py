import pygame

from test_graphique.clothoide import *

class road:

    def __init__(self):
        self.flag_coord = []

    def left_click(self, x, y):
        self.flag_coord.append(x)
        self.flag_coord.append(y)

    def create_clothoid_road(self):
        return point((self.flag_coord[0],self.flag_coord[1]),(self.flag_coord[2],self.flag_coord[3]),(self.flag_coord[4],self.flag_coord[5]))


