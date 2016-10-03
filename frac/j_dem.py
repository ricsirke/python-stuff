import math, cmath
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

max_iter = 500
rad_lim = 20
N = 500

class Julia:
	def __init__(self, c):
		if not isinstance(c, complex):
			Exception("init: c is not complex")
			
		self.c = c
		
		
	def func(self, z):
		if not isinstance(z, complex):
			Exception("func: z is not complex")
		 
		return z**2 + self.c
		
	def dist_to_color(self, dist, min_dist, max_dist):
		# converts distance to a number between 0 and 255
		dists_dist = max_dist - min_dist
		return ((dist-min_dist)/dists_dist)*254
		
	def dist(self, z):
		if not isinstance(z, complex):
			Exception("dist: z is not complex")
		
		dz = complex(1,0)
		z_iter = z
		
		cnt = 1
		
		while cnt<max_iter:
			z_new = self.func(z_iter)
			
			z_abs = abs(z_new)
			if z_abs > rad_lim:
				break
			
			dz_new = 2*z_iter*dz
			
			z_iter = z_new
			dz = dz_new
			
			cnt += 1
			
		#return (z_abs*math.log(z_abs))/(abs(dz))
		return z_abs
		
	def plot(self):
		x_ax = np.linspace(-2.0, 2.0, N)
		y_ax = np.linspace(-2.0, 2.0, N)
		
		graph = np.zeros((N,N,3))
		
		dists = []
		# colors = []
		
		for i in range(N):
			for j in range(N):
				dist = self.dist(complex(x_ax[i], y_ax[j]))
				color = dist
				# the color is cyclic (mod 255)
				graph[i][j] = [color, color, color]
				dists.append(dist)
				# colors.append(color)
				
			if (i % 100) == 0:
				print i
				
				
		min_dist = min(dists)
		max_dist = max(dists)
		
		print "min, max dists:", min_dist, max_dist
		# print "min, max colors:", min(colors), max(colors)
		
		new_colors = []
		
		for i in range(N):
			for j in range(N):
				new_color = 255 - self.dist_to_color(graph[i][j][0], min_dist, max_dist)
				graph[i][j] = [new_color, new_color, new_color]
				new_colors.append(graph[i][j][0])
				
		print "min, max new colors:", min(new_colors), max(new_colors)
		
		# fig, axes = plt.subplots(nrows=3)
		
		# axes[0].hist(dists, bins=20)
		# axes[0].set(title="distances from julia set")
		# axes[1].hist(colors, bins=20)
		# axes[1].set(title="colors")
		# axes[2].imshow(graph, interpolation='nearest')
		
		plt.imshow(graph, interpolation='nearest')
		plt.show()
		
c = complex(-0.8, 0.16)
j = Julia(c)
j.plot()