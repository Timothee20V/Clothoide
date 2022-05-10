from matplotlib.pyplot import *
from math import *

title("Clothoïde")
x1 = [0, 1.00, 1.01]
y1 = [0, 0, 0]
x2=[0,-1.00,-1.01]
y2=[0,0,0]






L = 1.00

C=int(input("quelle est al vitesse?"))

phi = 0
i = 2
"""
n=int(input("nombre?"))
while i<n :


    L = L + C
    phi = phi + L / C ** 2
    x1.append(x1[i] + cos(phi) * C)
    y1.append(y1[i] + sin(phi) * C)
    i=i+1"""
L=1.0

phi = 0
i = 2
lb=0
while cos(phi)>0.02 :


    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] - cos(phi) * C)
    y2.append(y2[i] - sin(phi) * C)
    i=i+1
    if cos(phi)>cos(3.14/4):
        lb=lb+cos(phi)*C

del x1[-1]
del y1[-1]
print (lb)


x2.reverse()
y2.reverse()

"""for k in range(len (x1)):
    x2.append(x1[k])
    y2.append(y1[k])"""
plot(x2, y2, '-0', color='red')


show()