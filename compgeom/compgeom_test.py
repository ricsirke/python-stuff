import convex_hull as ch
from Tkinter import *
import random


magn = 400
offset = 30

def trf(coord):
    return magn*coord + offset


def drawPoint(canvas, p, color):
    rad = 5
    coords = (p[0]*magn - rad + offset, p[1]*magn - rad + offset, p[0]*magn + rad + offset, p[1]*magn + rad + offset)
    canvas.create_oval(*coords, fill=color)

def drawPoints(canvas, P):
    for p in P:
        drawPoint(canvas, p, "black")
        
def drawHull(canvas, hull):
    for e in hull:
        p = e[0]
        q = e[1]
        canvas.create_line(trf(p[0]), trf(p[1]), trf(q[0]), trf(q[1]), width=3, fill="red")
        
def drawHullFlat(canvas, hull):
    for i in range(len(hull)-1):
        p = hull[i]
        q = hull[i+1]
        canvas.create_line(trf(p[0]), trf(p[1]), trf(q[0]), trf(q[1]), width=3, fill="red")


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=1000, height=700, bg="white")
    canvas.pack()
    
    P = []
    for i in range(100):
        P.append((random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)))
    
    drawPoints(canvas, P)
    
    # slowhull = ch.slowConvHull(P)
    # drawHull(canvas, slowhull)
    
    hull = ch.convHull(P)
    drawHullFlat(canvas, hull)
    
    
    root.mainloop()