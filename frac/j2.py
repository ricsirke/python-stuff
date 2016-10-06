import math, cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import groupby
import sys

max_iter = 200
rad_lim = 20
N = int(sys.argv[1])
T = 50

class Julia:
    def __init__(self, c):
        if not isinstance(c, complex):
            Exception("init: c is not complex")
            
        self.c = c
        
        
    def func(self, z):
        if not isinstance(z, complex):
            Exception("func: z is not complex")
         
        return z**2 + self.c
        
    def isToInf(self, z=(0,0)):
        val = z
        it = 0
        n = 0
        
        #print val

        while abs(val) < 10 and n < 245:
            it += 1
            val = self.func(val)
            n += 10
            
        return n
        
    def dc(self, t):
        if t < T/2:
            return complex(0.02,0.02)
        else:
            return complex(-0.02,-0.02)
        
    def calc_anim(self):    
        x_ax = np.linspace(-2.0, 2.0, N)
        y_ax = np.linspace(-2.0, 2.0, N)
        
        graph = np.zeros((T, N, N, 3))
        
        for t in range(T):
            for i in range(N):
                for j in range(N):
                    esc_rate = self.isToInf(complex(x_ax[i], y_ax[j]))
                    
                    # the color is cyclic (mod 255)
                    graph[t][i][j] = [esc_rate, esc_rate, esc_rate]
                    
            if (t % 10) == 0:
                print t
                
            self.c += self.dc(t)
    
        return graph
        
        
    def plot(self):        
        graph = self.calc_anim()        
            
        fig = plt.figure()
        ims = []
        for i in range(len(graph)):    
            im = plt.imshow(graph[i], interpolation='nearest', animated=True)
            ims.append([im])
            
        ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=0)
                
        plt.show()
        
    def saveVid(self):    
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=30, metadata=dict(artist='ricsard'), bitrate=180)
        ani.save("frac.mpeg", writer=writer)
        

c = complex(-0.8, 0.2)
j = Julia(c)
j.plot()