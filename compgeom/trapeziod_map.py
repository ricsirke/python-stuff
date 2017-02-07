import numpy as np
from utils import *

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