class cloto:
    def __init__(self,V,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
        self.V=V
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
        self.p3x = p3x
        self.p3y = p3y
        self.p4x = p4x
        self.p4y=p4y

        L=0.1
        x=[self.p1x,qzlf.p2x]
        y=[self.p1y,self.p2y]
        phi  = 0
        i=2
        # on tourne dans l autre sens selon le signe de angle-180
        while x[-1]!=p3x and y[-1]!=p3y:

            L = L + V
            phi = phi + L / C ** 2
            x2.append(x2[i] + cos(phi) * C)
            y2.append(y2[i] + sin(phi) * C)
            i = i + 1
            """
            if cos(phi) > cos(3.14 / 4):
                lb = lb + cos(phi) * C
            """



