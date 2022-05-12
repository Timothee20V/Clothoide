from math import*


class cloto:
    def __init__(self,V,p1x,p1y,p2x,p2y,p3x,p3y):
        self.V=V
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
        self.p3x = p3x
        self.p3y = p3y
        self.p4x = 2*p1x-p2x
        self.p4y=2*p1x-p2y

    #modifier pour faire avec les 3 pts
        L=0.1
        x=[self.p4x,self.p1x]
        y=[self.p4y,self.p1y]
        phi  = 0.01
        i=1
        # on tourne dans l autre sens selon le signe de angle-180
        while x[-1]!=p3x or y[-1]!=p3y:
        #adapter a l angle d arrivee
        #en rajoutant phi dans la classe
            L = L + V
            phi = phi + L / V ** 2
            x.append(x[i] + cos(phi) * V)
            y.append(y[i] + sin(phi) * V)
            i = i + 1
            """
            if cos(phi) > cos(3.14 / 4):
                lb = lb + cos(phi) * C
            """
    def afficher(self):
        plot(self.x, self.y, '-0', color='red')

        show()


r=cloto(100,0,0,100,1,50,50)
afficher(r)
