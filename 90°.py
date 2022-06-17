from matplotlib.pyplot import *
from math import *

title("Clothoïde")




def changement(xb,yb,xf,yf,xe,ye):
    x1=xb-xf,yb-yf
    x1=x1/(sqrt((xa-xf)**2+(ya-yf)**2))
    y1 = xe - xf, ye - yf
    y1 = y1 / (sqrt((xe - xf) ** 2 + (ye - yf) ** 2))
    return(x1,y1)

def clothoide(xa,ya,xb,yb,xf,yf,xe,ye,xg,yg):
    x1,y1=changement(xa,ya,xf,yf,xe,ye,xg,yg)
    phi=0
    x2=[xa,xf]
    y2=[ya,yf]




    L=sqrt((xa-xf)**2+(ya-yf)**2)


    i = 1
    C=1
    while x2[-1]!=xg :
        x2 = [xa, xf]
        y2 = [ya, yf]
        while x2[-1]/y2[-1]!=(xb-xe)/(yb-ye)
            x11,y11=x1
            x12,y12=y1

            L = L + C
            phi = phi + L / C ** 2
            x2.append(x2[i] - cos(phi) * C*x11+sin(phi)*C*x12)
            y2.append(y2[i] + sin(phi) * C*y11+sin(phi)*C*y12)
            i=i+1

    l=len(x2)
    for  i in range(1,l-2):
        x2.append(2xe-x2[l-i])
        y2.append(2*ye[l-1]-y2[l-i])


"""
x2.reverse()
y2.reverse()
"""
"""for k in range(len (x1)):
    x2.append(x1[k])
    y2.append(y1[k])"""
plot(x2, y2, '-0', color='red')


show()