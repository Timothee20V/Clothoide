from tkinter import *
from math import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)

    cnv.create_text(points_x[-1], points_y[-1], text='')
    cnv.create_text(points_x[-1], points_y[-1] + 10, text=len(points_x))

    if len(points_x) > 1:
        cnv.create_line(points_x[-2], points_y[-2], points_x[-1], points_y[-1])

    if len(points_x) > 2:
        A = points_x[-3], points_y[-3]
        B = points_x[-2], points_y[-2]
        C = points_x[-1], points_y[-1]
        cnv.create_text(points_x[-2], points_y[-2] - 10, text=round(angle(A, B, C)), fill='red')
        bissectrice(A, B, C)


def angle(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    vect1x, vect1y = xA - xB, yA - yB
    vect2x, vect2y = xC - xB, yC - yB
    scalaire = vect1x * vect2x + vect1y * vect2y
    BA = sqrt((vect1x ** 2 + vect1y ** 2))
    BC = sqrt((vect2x ** 2 + vect2y ** 2))
    angle_rad = acos(scalaire / (BA * BC))
    angle_deg = 360 * angle_rad / (2 * pi)
    return angle_deg


def clear():
    cnv.delete(ALL)
    points_x.clear()
    points_y.clear()


def bissectrice(A, B, C):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    xD, yD = 100 + xB, yB
    D = xD, yD
    angle_1 = angle(D, B, A)
    angle_2 = angle(A, B, C) / 2

    # meme moitié
    if xA > xB and xC > xB and yA > yB > yC:
        print("1")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA > xB and xC > xB and yA < yB < yC:
        print("2")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    if xA < xB and xC < xB and yA < yB < yC:
        print("3")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    if xA < xB and xC < xB and yA > yB > yC:
        print("4")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA < xB < xC and yA < yB and yC < yB:
        print("5")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    if xA > xB > xC and yA < yB and yC < yB:
        print("6")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    if xA < xB < xC and yA > yB and yC > yB:
        print("7")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA > xB > xC and yA > yB and yC > yB:
        print("8")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    # symétrique par rapport au centre
    if xA > xB > xC and yA > yB > yC:
        print("9")
        if angle(D, B, C) + angle(D, B, A) > 180:
            print("9.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R
        else:
            print("9.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA < xB < xC and yA < yB < yC:
        print("10")
        if angle(D, B, C) + angle(D, B, A) > 180:
            print("10.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R
        else:
            print("10.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    if xA < xB < xC and yA > yB > yC:
        print("11")
        if angle(D, B, C) + angle(D, B, A) > 180:
            print("11.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R
        else:
            print("11.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA > xB > xC and yA < yB < yC:
        print("12")
        if angle(D, B, C) + angle(D, B, A) > 180:
            print("12.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R
        else:
            print("12.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB - sin(angleF * 2 * pi / 360) * R

    # meme quart
    if xA > xB and xC > xB and yA > yB and yC > yB:
        print("13")
        if angle(D, B, C) + angle(D, B, A) > 45:
            print("13.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R
        else:
            print("13.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    if xA < xB and xC < xB and yA > yB and yC > yB:
        print("14")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * R, yB + sin(angleF * 2 * pi / 360) * R

    print("DBA:", angle_1)
    print("ABC:", angle_2 * 2)
    print("ABC/2:", angle_2)
    print("F:", angleF)
    cnv.create_text(xE, yE, text='●')
    cnv.create_text(xE, yE + 10, text=round(angle(A, B, (xE, yE))), fill='green')
    cnv.create_line(B, xE, yE)


route = Tk()
route.title('Route')

points_x = []
points_y = []

DIM = 600
dist = 2
R = 20
cnv = Canvas(route, width=DIM, height=DIM)

cnv.pack()

Bouton1 = Canvas(route)
Button(Bouton1, text="Effacer", command=clear, bg='red').pack()
Bouton1.pack()

cnv.bind("<Button-1>", point)

route.mainloop()
