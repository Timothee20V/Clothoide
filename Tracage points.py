from tkinter import *
from math import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)
    print(points_x)
    print(points_y)
    cnv.create_text(points_x[-1], points_y[-1], text='●')
    cnv.create_text(points_x[-1], points_y[-1]+10, text=len(points_x))

    if len(points_x) > 1:
        cnv.create_line(points_x[-2], points_y[-2], points_x[-1], points_y[-1])

    if len(points_x) > 2:
        A = points_x[-3], points_y[-3]
        B = points_x[-2], points_y[-2]
        C = points_x[-1], points_y[-1]
        cnv.create_text(points_x[-2], points_y[-2]-10, text=round(angle(A, B, C)), fill='red')
        E = bissectrice(A, B, C)


def angle(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    vect1x, vect1y = xA - xB, yA - yB
    vect2x, vect2y = xC - xB, yC - yB
    scalaire = vect1x * vect2x + vect1y * vect2y
    BA = sqrt((vect1x ** 2 + vect1y ** 2))
    BC = sqrt((vect2x ** 2 + vect2y ** 2))
    angle = acos(scalaire / (BA * BC))
    angle_deg = 360 * angle / (2 * pi)
    return angle_deg


def clear():
    cnv.delete(ALL)
    points_x.clear()
    points_y.clear()


'''def bissectrice(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    vect1x, vect1y = xA - xB, yA - yB
    vect2x, vect2y = xC - xB, yC - yB
    BA = sqrt((vect1x ** 2 + vect1y ** 2))
    BC = sqrt((vect2x ** 2 + vect2y ** 2))
    EA = BA - 1
    xE, yE = (dist*xA+EA*xB)/BA, (dist*yA+EA*yB)/BA
    DC = BC - 1
    xD, yD = (dist*xC + DC * xB) / BC, (dist*yC + DC * yB) / BC
    E = xE, yE
    D = xD, yD
    F = (xE+xD)/2, (yE+yD)/2
    print(F)
    cnv.create_text(F, text='●')

    return E'''


def bissectrice(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    xD, yD = 100 + xB, yB
    D = xD, yD
    angle_1 = angle(D, B, A)
    angle_2 = angle(A, B, C) / 2
    if (xA>xC and yC>yB) or (xA>xC and yC<yB and yA<yB):
        angleF = angle_1 + angle_2
        print("1")
    elif (xA<xC and yC>yB) or (xA>xC and yC<yB and yA>yB) or (xA<xC and yC<yB):
        angleF = angle_1 - angle_2
        print("2")


    print(B, D)
    print("DBA:", angle_1)
    print("ABC:", angle_2)
    print("F:", angleF)
    xE, yE = xB + cos(angleF)*20, yB + sin(angleF)*20
    cnv.create_text(xE, yE, text='●')
    cnv.create_line(B, D)


route = Tk()
route.title('Route')

points_x = []
points_y = []

DIM = 600
dist = 2
cnv = Canvas(route, width=DIM, height=DIM)

cnv.pack()

Bouton1 = Canvas(route)
Button(Bouton1, text="Effacer", command=clear, bg='red').pack()
Bouton1.pack()

cnv.bind("<Button-1>", point)

route.mainloop()
