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
n=int(input("nombre?"))
while i<n :


    L = L + C
    phi = phi + L / C ** 2
    x1.append(x1[i] + cos(phi) * C)
    y1.append(y1[i] + sin(phi) * C)
    i=i+1
L=10

phi = 0
i = 2
while i<n :


    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] - cos(phi) * C)
    y2.append(y2[i] - sin(phi) * C)
    i=i+1





x2.reverse()
y2.reverse()

for k in range(len (x1)):
    x2.append(x1[k])
    y2.append(y1[k])
plot(x2, y2, '-0', color='red')


show()