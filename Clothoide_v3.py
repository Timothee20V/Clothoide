import matplotlib.pyplot as plt
from math import *
from Vecteurs_test import *

plt.title("Clothoïde")

"""on change la base de la clothoïde"""
def changement(xa,ya,xf,yf,xe,ye):
    x1x=xf-xa
    x1y=yf-ya
    x1x=x1x/(sqrt((xf-xa)**2+(yf-ya)**2))
    x1y=x1y/(sqrt((xf-xa)**2+(yf-ya)**2))
    y1x = xe - xf
    y1y= ye - yf
    y1x= y1x / (sqrt((xe - xf) ** 2 + (ye - yf) ** 2))
    y1y=y1y / (sqrt((xe - xf) ** 2 + (ye - yf) ** 2))
    return(x1x,x1y,y1x,y1y)
"""on trace la clothoïde dans la nouvelle base"""
def clothoide_fct(xa,ya,xb,xf,yf,xe,ye):
    x1x,x1y,y1x,y1y=changement(xa,ya,xf,yf,xe,ye)
    phi=0
    x2=[xa,xf]
    y2=[ya,yf]

    #la liste dees points
    L = sqrt((xa - xf) ** 2 + (ya - yf) ** 2)
    C = L*10
    i=1

    #longueur du premier pan de courbe
    x2.append(x2[i] + cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y + cos(phi) * C * x1y)

    i = 2

    #on itère une fois le programme pour éviter la division par 0
    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] + cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y + cos(phi) * C * x1y)
    i = i + 1
    L = L + C
    phi = phi + L / C ** 2

    x2.append(x2[i] + cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y + cos(phi) * C * x1y)
    i = i + 1
    nb=3
    if xb!=xe:

        while phi<3.14/2:





            L = L + C
            phi = phi + L / C ** 2
            x2.append(x2[i] + cos(phi) * C*x1x+sin(phi)*C*y1x)
            y2.append(y2[i] + sin(phi) * C*y1y+cos(phi)*C*x1y)
            i=i+1
            nb+=1







    plt.plot(x2, y2, '-0', color='red')
    print("nombre=", nb * 2)
    plt.show()










