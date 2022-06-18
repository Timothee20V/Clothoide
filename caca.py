from matplotlib.pyplot import *
from math import *

title("Clothoïde")
x1 = [xa, xf, xf]
y1 = [ya, yf, yf]
"""
x2=[0,-1.00,-1.01]
y2=[0,0,0]"""





L = 1.00

C=500

phi = 0
i = 2
n=int(input("nombre?"))
while i<n :


    L = L + C
    phi = phi + L / C ** 2
    x1.append(x1[i] +C*( cos(phi) * x1[0]+sin(phi)*y1[0]))
    y1.append(y1[i] + C*( cos(phi) * y1[1]+sin(phi)*x1[1]))
    i=i+1
L=10
'''
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
'''

show()