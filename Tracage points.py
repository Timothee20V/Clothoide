from tkinter import *
from math import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)
    print(points_x)
    print(points_y)
    cnv.create_text(points_x[-1], points_y[-1], text='●')

    if len(points_x) > 1:
        cnv.create_line(points_x[-2], points_y[-2], points_x[-1], points_y[-1])

    if len(points_x) > 2:
        A = points_x[-3], points_y[-3]
        B = points_x[-2], points_y[-2]
        C = points_x[-1], points_y[-1]
        cnv.create_text(B, text=round(angle(A, B, C)), font=('arail', 24), fill='red')


def angle(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    vect1x, vect1y = xA-xB, yA-yB
    vect2x, vect2y = xC-xB, yC-yB
    scalaire = vect1x*vect2x + vect1y*vect2y
    BA = sqrt((vect1x**2 + vect1y**2))
    BC = sqrt((vect2x**2 + vect2y**2))
    angle = acos(scalaire/(BA * BC))
    angle_deg = 360*angle/(2*pi)
    return angle_deg


def clear():
    cnv.delete(ALL)
    points_x.clear()
    points_y.clear()


route = Tk()
route.title('Route')

points_x = []
points_y = []

DIM = 600
cnv = Canvas(route, width=DIM, height=DIM)

cnv.pack()

Bouton1 = Canvas(route)
Button(Bouton1, text="Effacer", command=clear, bg='red').pack()
Bouton1.pack()

cnv.bind("<Button-1>", point)

route.mainloop()
