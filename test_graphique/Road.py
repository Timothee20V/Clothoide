import pygame



class road:

    def __init__(self):
        self.flag_coord = []

    def left_click(self, x, y):
        self.flag_coord.append(x)
        self.flag_coord.append(y)

    def create_clothoid_road(self):
        pass

    def create_straight_road(self):
        pass

