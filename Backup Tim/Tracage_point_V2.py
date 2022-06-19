from tkinter import *
from math import *
from Vecteurs_test import *
from Clothoide_v2 import *
from Clothoide_v3 import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)

    cnv.create_text(points_x[-1], points_y[-1], text='●')
    # cnv.create_text(points_x[-1], points_y[-1] + 10, text=len(points_x))

    if len(points_x) > 1:
        cnv.create_line(points_x[-2], points_y[-2], points_x[-1], points_y[-1])

    if len(points_x) > 2:
        BA = Vect(points_x[-2], points_y[-2], points_x[-3], points_y[-3], 'vecteur')
        BC = Vect(points_x[-2], points_y[-2], points_x[-1], points_y[-1], 'vecteur')
        # cnv.create_text(points_x[-2], points_y[-2] - 10, text=round(BA.angle(BC)), fill='red')
        bissectrice(BA, BC)


def clear():
    cnv.delete(ALL)
    points_x.clear()
    points_y.clear()


def bissectrice(BA, BC):
    xA, yA = BA.x2, BA.y2
    xB, yB = BA.x1, BA.y1
    xC, yC = BC.x2, BC.y2

    BD = Vect(BC.x1, BC.y1, BC.x1 + 1, BC.y1, 'vecteur')  # Axe horizontal en B

    angle_1 = BD.angle(BA)  # Angle DBA deg
    angle_2 = BA.angle(BC) / 2  # Angle ABE deg
    teta = ((2 * pi) * (BA.angle(BC)) / 360) / 2  # Angle ABE rad

    T = R / tan(teta)  # Longueur BF
    U = R / sin(teta)  # Longueur BE

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

    BF = BA * (T / BA.norme)
    BH = BC * (T / BC.norme)
    BE = Vect(xB, yB, xE, yE, 'vecteur')
    EF = Vect(xE, yE, BF.x + xB, BF.y + yB, 'vecteur')

    BG_dist = R / cos((pi - 2 * teta) / 2) - R  # Longueur BG
    BG = BE * (BG_dist / BE.norme)

    xF, yF = BF.x + xB, BF.y + yB
    xG, yG = BG.x + xB, BG.y + yB
    xH, yH = BH.x + xB, BH.y + yB

    global A
    global B
    global C
    global E
    global F
    global G

    A = xA, yA
    B = xB, yB
    C = xC, yC
    E = xE, yE
    F = xF, yF
    G = xG, yG
    H = xH, yH

    global FE
    FE = Vect(xF, yF, xE, yE, 'vecteur')
    global FH
    FH = Vect(xF, yF, xH, yH, 'vecteur')

    cnv.create_text(xA, yA + 10, text='A')
    cnv.create_text(xB, yB + 10, text='B')
    cnv.create_text(xC, yC + 10, text='C')
    cnv.create_text(xE, yE + 10, text='E')
    cnv.create_text(xF, yF + 10, text='F')
    cnv.create_text(xG, yG + 10, text='G')
    cnv.create_text(xH, yH + 10, text='H')
    cnv.create_text(E, text='●')
    cnv.create_text(F, text='●')
    cnv.create_text(G, text='●')
    cnv.create_text(H, text='●')
    # cnv.create_text(xE, yE + 10, text=round(BE.angle(BA)), fill='green')
    cnv.create_line(B, E)
    cnv.create_line(F, E)
    cnv.create_line(F, H)

    '''print('A:', A)
    print('B:', B)
    print('C:', C)
    print('F:', F)
    print('E:', E)
    print('G:', G)
    print('T =', T)
    print('U =', U)
    print('EF =', EF.norme)
    print('EG =', Vect(xE, yE, xG, yG, 'vecteur').norme)
    print('BE =', BE.norme)
    print('BG =', BG_dist)
    print('C =', 2*R*sin(pi - 2*teta))
    print('C1=', Vect(xF, yF, xH, yH, 'vecteur').norme)'''


def clothoide():
    xE, yE = E
    xB, yB = B
    global x
    global y

    angle_tangente_final = pi / 2 - (FE.angle(FH)) * (2 * pi) / 360

    angle_tangente = 0
    x = []
    y = []
    w = 0
    while angle_tangente < angle_tangente_final:
        x.append(200*integ(w))
        y.append(200*integ2(w))
        if len(x) > 1:
            angle_tangente = atan((y[-1] - y[-2]) / (x[-1] - x[-2]))  # arctan(dy/dx)
        w = w + 0.01

    #symétrie
    '''x_sym = []
    y_sym = []
    for i in range(len(x)-1):
        xI = x[i]
        yI = y[i]
        print('xI:', xI, 'yI:', yI)
        alpha = Vect(x[-1], y[-1], xI, yI, 'vecteur').angle(Vect(xE, yE, xB, yB, 'vecteur'))
        print("alpha deg =", alpha)
        alpha = alpha * 2 * pi / 360

        print("alpha =", alpha)
        X = (xI - x[-1]) * cos(2*pi - 2 * alpha) - (yI - y[-1]) * sin(2*pi - 2 * alpha)
        Y = (xI - x[-1]) * sin(2*pi - 2 * alpha) + (yI - y[-1]) * cos(2*pi - 2 * alpha)
        x_sym.append(X + x[-1])
        y_sym.append(Y + y[-1])'''

    print('w =', w)
    print('angle_tangente_final =', angle_tangente_final)
    print('angle_tangente =', angle_tangente)
    affichage_clothoide()


def affichage_clothoide():
    xA, yA = A
    xB, yB = B

    # rotation d'angle phi, de la clothoide
    phi = Vect(xA, yA, xB, yB, 'vecteur').angle(Vect(xA, yA, xA + 1, yA, 'vecteur'))
    print(phi)
    phi = phi * 2 * pi / 360

    for i in range(1, len(x)):
        xI = x[i]
        yI = y[i]
        angle_pro = Vect(0, 0, 1, 0, 'vecteur').angle(Vect(0, 0, xI, yI, 'vecteur'))
        angle_pro = angle_pro * 2 * pi / 360
        norme = Vect(0, 0, xI, yI, 'vecteur').norme
        x[i] = norme * cos(angle_pro + phi)
        y[i] = norme * sin(angle_pro + phi)



    # deplacement de la clothoide

    for i in range(0, len(x)):
        x[i] = x[i] + xA
        y[i] = yA - y[i]
        if i > 2:
            cnv.create_line(x[i-1], y[i-1], x[i], y[i])
        cnv.create_text(0, 0, text='●')
        cnv.create_text(10, 100, text='100y')
        cnv.create_text(100, 10, text='100x')

route = Tk()
route.title('Route')

points_x = []
points_y = []

DIM = 600
dist = 2
R = 100
cnv = Canvas(route, width=DIM, height=DIM)

cnv.pack()

Bouton1 = Canvas(route)
Button(Bouton1, text="Effacer", command=clear, bg='red').pack()
Bouton1.pack()

Bouton2 = Canvas(route)
Button(Bouton2, text="Clothoide", command=clothoide, bg='red').pack()
Bouton2.pack()

cnv.bind("<Button-1>", point)

route.mainloop()
