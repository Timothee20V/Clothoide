from Vecteurs import *
from Clothoide_v2 import *


def point(A, B, C):
    global xA, yA
    global xB, yB
    global xC, yC

    xA, yA = A
    xB, yB = B
    xC, yC = C

    BA = Vect(xB, yB, xC, yC, 'vecteur')
    BC = Vect(xB, yB, xA, yA, 'vecteur')

    return clothoide(BA, BC)


def clothoide(BA, BC):
    global xA, yA
    global xB, yB
    global xC, yC
    global xE, yE
    global xF, yF
    global xH, yH
    global teta

    xA, yA = BA.x2, BA.y2
    xB, yB = BA.x1, BA.y1
    xC, yC = BC.x2, BC.y2

    BD = Vect(BC.x1, BC.y1, BC.x1 + 1, BC.y1, 'vecteur')  # Axe horizontal en B

    angle_1 = BD.angle(BA)  # Angle DBA deg
    angle_2 = BA.angle(BC) / 2  # Angle ABE deg
    teta = ((2 * pi) * (BA.angle(BC)) / 360) / 2  # Angle ABE rad

    T = R / tan(teta)  # Longueur BF
    U = R / sin(teta)  # Longueur BE

    BF = BA * (T / BA.norme)    #Pts F
    BH = BC * (T / BC.norme)    #Pts H

    xF, yF = BF.x + xB, BF.y + yB
    xH, yH = BH.x + xB, BH.y + yB

    # meme moitié
    if xA >= xB and xC >= xB and yA >= yB >= yC:
        print("1")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)

    if xA >= xB and xC >= xB and yA <= yB <= yC:
        print("2")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(1, -1)

    if xA <= xB and xC <= xB and yA <= yB <= yC:
        print("3")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)

    if xA <= xB and xC <= xB and yA >= yB >= yC:
        print("4")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(1, 1)

    if xA <= xB <= xC and yA <= yB and yC <= yB:
        print("5")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(1, -1)

    if xA >= xB >= xC and yA <= yB and yC <= yB:
        print("6")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)

    if xA <= xB <= xC and yA >= yB and yC >= yB:
        print("7")
        angleF = angle_1 - angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)

    if xA >= xB >= xC and yA >= yB and yC >= yB:
        print("8")
        angleF = angle_1 + angle_2
        xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
        x,y,x_sym,y_sym = clothoide_unitaire(1, 1)

    # symétrique par rapport au centre
    if xA >= xB >= xC and yA > yB > yC:
        print("9")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("9.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, 1)
        else:
            print("9.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)

    if xA <= xB <= xC and yA < yB < yC:
        print("10")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("10.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)
        else:
            print("10.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, -1)

    if xA <= xB <= xC and yA > yB > yC:
        print("11")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("11.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, 1)
        else:
            print("11.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)

    if xA >= xB >= xC and yA < yB < yC:
        print("12")
        if BD.angle(BC) + BD.angle(BA) > 180:
            print("12.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)
        else:
            print("12.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, -1)

    # meme quart
    if xA > xB and xC > xB and yA > yB and yC > yB:
        print("13")
        if BD.angle(BA) - BD.angle(BC) < 0:
            print("13.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, 1)
        else:
            print("13.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)

    if xA < xB and xC < xB and yA > yB and yC > yB:
        print("14")
        if BD.angle(BA) - BD.angle(BC) > 0:
            print("14.1")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, 1)
        else:
            print("14.2")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB + sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, 1)

    if xA < xB and xC < xB and yA < yB and yC < yB:
        print("15")
        if BD.angle(BA) - BD.angle(BC) > 0:
            print("15.1")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, -1)
        else:
            print("15.2")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)

    if xA > xB and xC > xB and yA < yB and yC < yB:
        print("16")
        if BD.angle(BA) - BD.angle(BC) < 0:
            print("16.1")
            angleF = angle_1 + angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(-1, -1)
        else:
            print("16.2")
            angleF = angle_1 - angle_2
            xE, yE = xB + cos(angleF * 2 * pi / 360) * U, yB - sin(angleF * 2 * pi / 360) * U
            x,y,x_sym,y_sym = clothoide_unitaire(1, -1)

    return x, y, x_sym, y_sym
    return x

def clothoide_unitaire(a, b):
    FE = Vect(xF, yF, xE, yE, 'vecteur')
    FH = Vect(xF, yF, xH, yH, 'vecteur')

    angle_tangente_final = pi / 2 - (FE.angle(FH)) * (2 * pi) / 360

    angle_tangente = 0
    x = []
    y = []
    w = 0
    while angle_tangente < angle_tangente_final:
        x.append(integ(w))
        y.append(integ2(w))
        if len(x) > 1:
            angle_tangente = atan((y[-1] - y[-2]) / (x[-1] - x[-2]))  # arctan(dy/dx)
        w = w + 0.01

    # symétrie
    x_sym = [i for i in x]
    y_sym = [-i + 2 * y[-1] for i in y]

    for i in range(0, len(x)-1):
        angle_pro = Vect(x[-1], y[-1], x[-1], y[-1]+1, 'vecteur').angle(Vect(x[-1], y[-1], x_sym[i], y_sym[i], 'vecteur'))
        angle_pro = angle_pro * 2 * pi / 360
        norme = Vect(x[-1], y[-1], x_sym[i], y_sym[i], 'vecteur').norme
        x_sym[i] = norme * cos(angle_pro - pi/2 + 2 * angle_tangente_final) + x[-1]
        y_sym[i] = norme * sin(angle_pro - pi/2 + 2 * angle_tangente_final) + y[-1]

    x, y = transformation_clothoide(a, b, x, y)
    x_sym, y_sym = transformation_clothoide(a, b, x_sym, y_sym)

    return x, y, x_sym, y_sym


def transformation_clothoide(a, b, x, y):
    global xG, yG

    BE = Vect(xB, yB, xE, yE, 'vecteur')
    BG_dist = R / cos((pi - 2 * teta) / 2) - R  # Longueur BG
    BG = BE * (BG_dist / BE.norme)

    xG, yG = BG.x + xB, BG.y + yB
    BG = Vect(xB, yB, xG, yG, 'vecteur')

    # dimension de la clothoide
    coef = BG.norme * sin(teta) / y[-1]
    for i in range(len(x)):
        x[i] = coef * x[i]
        y[i] = coef * y[i]

    # rotation d'angle phi, de la clothoide
    phi = Vect(xA, yA, xB, yB, 'vecteur').angle(Vect(xA, yA, xA + 1, yA, 'vecteur'))
    phi = phi * 2 * pi / 360

    for i in range(1, len(x)):
        angle_pro = Vect(0, 0, 1, 0, 'vecteur').angle(Vect(0, 0, x[i], y[i], 'vecteur'))
        angle_pro = angle_pro * 2 * pi / 360
        norme = Vect(0, 0, x[i], y[i], 'vecteur').norme
        x[i] = norme * cos(a*angle_pro + b*phi)
        y[i] = norme * sin(a*angle_pro + b*phi)

    # deplacement de la clothoide

    for i in range(0, len(x)):
        x[i] = x[i] + xG - x[-1]
        y[i] = yG - y[i] + y[-1]

    return x, y


R = 100



