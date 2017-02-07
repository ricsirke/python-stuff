import numpy as np

def isDirLineLeftSide(r, line):
    """decides whether the point r lies left of the directed line from p to q"""
    p = line[0]
    q = line[1]
    
    m = [
            [1, p[0], p[1]],
            [1, q[0], q[1]],
            [1, r[0], r[1]]
        ]
        
    return np.linalg.det(m) >= 0
    
    
def isLeftTurn(p, q, r):
    """decides whether the point triplet p,q,r makes a left turn"""
    line = (p, q)
    return isDirLineLeftSide(r, line)