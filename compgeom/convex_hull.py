import numpy as np
from util import *

def slowConvHull(points):
    """
    Computes convex hull of planar points
    input: set of points in the plane
    output: a list containing the vertices of CH(P) in clockwise order
    speed: o(n^3)
    
    for all directed edges (vertex pairs)
    if all the other vertices are at the left side of the edge, we add that edge to the hull
    """
    
    E = []
    
    for p in points:
        for q in points:
            if p != q:
                candLine = (p, q)
                valid = True
                for r in points:
                    # ??? OR AND ???
                    if p != r and q != r:
                        if isDirLineLeftSide(r, candLine):
                            valid = False
                if valid:
                    E.append(candLine)
                        
    return E
    

    
def convHull(points):
    """
    Computes convex hull of planar points
    input: set of points in the plane
    output: a list containing the vertices of CH(P) in clockwise order
    speed: O(n*logn)
    
    determines the convex hull separately, first the upper hull, then the lower hull
    adds the sorted (by x coord) vertices one-by-one
    checks is there is a right turn, if so delete the point in the middle from the last 3 added points
        looping this until the upper hull contains only left turns
    """
    n = len(points)
    lup = []
    ldown = []
    
    points = sorted(points, key=lambda p: p[0])
    
    # upper hull
    lup.append(points[0])
    lup.append(points[1])
    
    for i in range(3, n):
        lup.append(points[i])
        while len(lup) > 2 and isLeftTurn(lup[-3], lup[-2], lup[-1]):
            lup = [ lup[i] for i in range(len(lup)) if i != (len(lup)-2) ]
    
    # lower hull
    ldown.append(points[-1])
    ldown.append(points[-2])
    
    for i in range(1,n+1):
        i = n-i
        ldown.append(points[i])
        while len(ldown) > 2 and isLeftTurn(ldown[-3], ldown[-2], ldown[-1]):
            ldown = [ ldown[i] for i in range(len(ldown)) if i != (len(ldown)-2) ]
    
    # contstructing the full hull
    hull = lup + ldown
    return hull
    