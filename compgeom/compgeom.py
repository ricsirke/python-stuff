import numpy as np

def isDirLineLeftSide(r, line):
    p = line[0]
    q = line[1]
    
    m = [[1,p[0],p[1]], [1,q[0],q[1]], [1,r[0],r[1]]]
    return np.linalg.det(m) >= 0

def slowConvHull(points):
    """Computes convex hull of planar points
    input: set of points in the plane
    output: a list containing the vertices of CH(P) in clockwise order"""
    
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
    
    
def isLeftTurn(p, q, r):
    line = (p, q)
    return isDirLineLeftSide(r, line)
    
def convHull(points):
    n = len(points)
    lup = []
    ldown = []
    
    points = sorted(points, key=lambda p: p[0])
    
    lup.append(points[0])
    lup.append(points[1])
    
    for i in range(3, n):
        lup.append(points[i])
        while len(lup) > 2 and isLeftTurn(lup[-3], lup[-2], lup[-1]):
            lup = [ lup[i] for i in range(len(lup)) if i != (len(lup)-2) ]
            
    ldown.append(points[-1])
    ldown.append(points[-2])
    
    for i in range(1,n+1):
        i = n-i
        ldown.append(points[i])
        while len(ldown) > 2 and isLeftTurn(ldown[-3], ldown[-2], ldown[-1]):
            ldown = [ ldown[i] for i in range(len(ldown)) if i != (len(ldown)-2) ]
    
    return lup + ldown
    


def getBoundingBox(S):
    # TODO implement
    R = None
    return R
    
def findIntersectedTraps(s):
    # TODO implement
    traps = []
    return traps
    
def removeTrapT(T, trap):
    # TODO implement
    return T
    
def updateT(T, traps):
    for t in traps:
        T = removeTrapT(T, t)
    # TODO new traps
    return T
    
def removeTrapD(D, trap):
    # TODO implement
    return D
    
def updateD(D, traps):
    for t in traps:
        D = removeTrapD(D, t)
    # TODO new traps
    return D


def trapezoidalMap(S):
    """
    input: set S of n non-crossing line segments
    output: trapezoidal map T(S), search strucuture D in a bounding box
    
    trapezoidal map represented by doubly-connected edge list
    """
    R = getBoundingBox(S)
    T = None
    D = None
    
    Sp = np.random.permutation(S)
    n = len(Sp)
    
    for i in range(n):
        traps = findIntersectedTraps(Sp[i])
        T = updateT(T, traps)
        D = updateD(D, traps)
    
    return T, D
    