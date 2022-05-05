from tkinter import *


def point(event):
    x, y = event.x, event.y
    points_x.append(x)
    points_y.append(y)
    print(points_x)
    print(points_y)
    cnv.create_text(points_x[-1], points_y[-1], text='x')
    if len(points_x) > 1:
        cnv.create_line(points_x[-2],points_y[-2],points_x[-1],points_y[-1])


route = Tk()
route.title('Route')

points_x = []
points_y = []

DIM = 40
cnv = Canvas(route, width=DIM * 11, height=DIM * 11)
cnv.pack()

cnv.bind("<Button-1>", point)

route.mainloop()
