import matplotlib.pyplot as plt
from math import *
from Vecteurs_test import *

plt.title("Clothoïde")
def angle(xa,ya,xb,yb,xc,yc):
    V1=Vect(xa,ya,xb,yb,"vecteur")
    V2=Vect(xb,yb,xc,yc,"vecteur")
    return V1.angle(V2)

#changement de base
def changement(xa,ya,xb,yb,xf,yf,xe,ye):
    x1x=xf-xa
    x1y=yf-ya
    x1x=x1x/(sqrt((xf-xa)**2+(yf-ya)**2))
    x1y=x1y/(sqrt((xf-xa)**2+(yf-ya)**2))
    y1x = xe - xf
    y1y= ye - yf
    y1x= y1x / (sqrt((xe - xf) ** 2 + (ye - yf) ** 2))
    y1y=y1y / (sqrt((xe - xf) ** 2 + (ye - yf) ** 2))
    return(x1x,x1y,y1x,y1y)

def clothoide_fct(xa,ya,xb,yb,xf,yf,xe,ye):
    x1x,x1y,y1x,y1y=changement(xa,ya,xb,yb,xf,yf,xe,ye)
    phi=0
    x2=[xa,xf]
    y2=[ya,yf]

    #la liste dees points
    L = sqrt((xa - xf) ** 2 + (ya - yf) ** 2)
    C = L/2
    i=1

    #longueur du premier pan de courbe
    x2.append(x2[i] - cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y - cos(phi) * C * x1y)

    i = 2

    #on itère une fois le programme pour éviter la division par 0
    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] - cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y - cos(phi) * C * x1y)
    i = i + 1
    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] - cos(phi) * C * x1x + sin(phi) * C * y1x)
    y2.append(y2[i] + sin(phi) * C * y1y - cos(phi) * C * x1y)
    i = i + 1
    if xb!=xe:
        #xb=xe entraine un division par 0
        while ((x2[-1]-xe)*(yb-ye)/abs(xb-xe)-y2[-1]+ye)*((x2[-2]-xe)*(yb-ye)/abs(xb-xe)-y2[-2]+ye)>0:

            print(angle(xb, yb, x2[-1], y2[-1], xe, ye))

#on vérifie que ce pan de droite ne traverse pas BE

            L = L + C
            phi = phi + L / C ** 2
            x2.append(x2[i] - cos(phi) * C*x1x+sin(phi)*C*y1x)
            y2.append(y2[i] + sin(phi) * C*y1y-cos(phi)*C*x1y)
            i=i+1
    for i in range (0,len (x2)):
        x2[i]=-x2[i]

    if xb==xe:
        while x2[-1]*x2[-2]>0:
            # on vérifie que ce pan de droite ne traverse pas BE

            L = L + C
            phi = phi + L / C ** 2
            x2.append(x2[i] + cos(phi) * C * x1x + sin(phi) * C * y1x)
            y2.append(y2[i] + sin(phi) * C * y1y + cos(phi) * C * x1y)
            i = i + 1



    """#la symétrie
    l=len(x2)
    for  i in range(1,l-2):
        x2.append(2*xe-x2[l-i])
        y2.append(2*ye-y2[l-i])"""

    plt.plot(x2, y2, '-0', color='red')

    plt.show()






"""
x2.reverse()
y2.reverse()
"""
"""for k in range(len (x1)):
    x2.append(x1[k])
    y2.append(y1[k])"""
