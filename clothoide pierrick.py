from matplotlib.pyplot import *
from math import *

title("Clothoïde")
x1 = [0, 100, 100]
y1 = [0, 0, 0.01]

x2=[0,-100,-100]
y2=[0,0,-0.01]

L = 100

C = 1000

phi = 0
i = 2
n = 1000
while i < n:
    L = L + C
    phi = phi + L / C ** 2
    x1.append(x1[i] + C * (cos(phi)))
    y1.append(y1[i] + C * (sin(phi)))
    i = i + 1


"""on va retourner la clothoïde"""


L=100
C=1000

phi = 0
i = 2
while i<n :


    L = L + C
    phi = phi + L / C ** 2
    x2.append(x2[i] - cos(phi) * C)
    y2.append(y2[i] - sin(phi) * C)
    i=i+1

x1.reverse()
y1.reverse()

for k in range(len (x1)):
    x1.append(x2[k])
    y1.append(y2[k])

plot(x1, y1, '-0', color='red')

show()
