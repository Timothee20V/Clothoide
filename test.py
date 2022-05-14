from tkinter import *
from math import *
from Vecteurs import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)

    cnv.create_text(points_x[-1], points_y[-1], text='●')
    cnv.create_text(points_x[-1], points_y[-1] + 10, text=len(points_x))

    if len(points_x) > 1:
        cnv.create_line(points_x[-2], points_y[-2], points_x[-1], points_y[-1])

    if len(points_x) > 2:
        BA = Vect(points_x[-2], points_y[-2], points_x[-3], points_y[-3], 'vecteur')
        BC = Vect(points_x[-2], points_y[-2], points_x[-1], points_y[-1], 'vecteur')
        cnv.create_text(points_x[-2], points_y[-2] - 10, text=round(BA.angle(BC)), fill='red')
        bissectrice(BA, BC)


def clear():
    cnv.delete(ALL)
    points_x.clear()
    points_y.clear()


def bissectrice(BA, BC):
    xA, yA = BA.x2, BA.y2
    xB, yB = BA.x1, BA.y1
    xC, yC = BC.x2, BC.y2
    BD = Vect(BC.x1, BC.y1, BC.x1 + 100, BC.y1, 'vecteur')
    angle_1 = BD.angle(BA)
    angle_2 = BA.angle(BC) / 2
    T = R/tan(BA.angle(BC)/2)
    U = R / sin(((2 * pi) * (BA.angle(BC)) / 360) / 2)

    print('T:', T, 'U:', U)

    # meme moitié
    if xA >= xB and xC >= xB and yA >= yB >= yC:
        print("1")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA >= xB and xC >= xB and yA <= yB <= yC:
        print("2")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA <= xB and xC <= xB and yA <= yB <= yC:
        print("3")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA <= xB and xC <= xB and yA >= yB >= yC:
        print("4")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA <= xB <= xC and yA <= yB and yC <= yB:
        print("5")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA >= xB >= xC and yA <= yB and yC <= yB:
        print("6")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA <= xB <= xC and yA >= yB and yC >= yB:
        print("7")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA >= xB >= xC and yA >= yB and yC >= yB:
        print("8")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    # symétrique par rapport au centre
    if xA >= xB >= xC and yA > yB > yC:
        print("9")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("9.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        else:
            print("9.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA <= xB <= xC and yA < yB < yC:
        print("10")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("10.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        else:
            print("10.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA <= xB <= xC and yA > yB > yC:
        print("11")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("11.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        else:
            print("11.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA >= xB >= xC and yA < yB < yC:
        print("12")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("12.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        else:
            print("12.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    # meme quart
    if xA > xB and xC > xB and yA > yB and yC > yB:
        print("13")
        if BD.angle(BA) - BD.angle(BC) < 0:
            print("13.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        else:
            print("13.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA < xB and xC < xB and yA > yB and yC > yB:
        print("14")
        if BD.angle(BA) - BD.angle(BC) > 0:
            print("14.1")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        else:
            print("14.2")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U

    if xA < xB and xC < xB and yA < yB and yC < yB:
        print("15")
        if BD.angle(BA) - BD.angle(BC) > 0:
            print("15.1")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        else:
            print("15.2")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    if xA > xB and xC > xB and yA < yB and yC < yB:
        print("16")
        if BD.angle(BA) - BD.angle(BC) < 0:
            print("16.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        else:
            print("16.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U

    print('T = ', BA*(1/(BA.norme)))
    BE = Vect(xB, yB, xE, yE, 'vecteur')
    cnv.create_text(xE, yE, text='●')
    cnv.create_text(xE, yE + 10, text=round(BE.angle(BA)), fill='green')
    cnv.create_line(xB, yB, xE, yE)


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
