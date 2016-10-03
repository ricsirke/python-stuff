import matplotlib.pyplot as plt
import math
import numpy as np

# exp(a+bi) = exp(a)*(cos(b) + isin(b))
#           = ( exp(a)cos(b), exp(a)*sin(b) )

# exp(a2 + b2 + 2abi) = exp(a2 + b2)*exp(2ab i)


def func(z=(0,0)):
	a = float(z[0])
	b = float(z[1])
	return (a**2 - b**2 - 0.4, 2*a*b + 0.6)
	#return (math.exp(a)*math.cos(b), math.exp(a)*math.sin(b)) # uncsi
	#return (math.exp(a**2 + b**2)*math.cos(2*a*b), math.exp(a**2 + b**2)*math.sin(2*a*b))
	#return (b**3*math.sin(a), a**2*b**2*math.sin(a))
	
def compAbs(z=(0,0)):
	a = z[0]
	b = z[1]
	
	return a**2 + b**2
	
def isToInf(z=(0,0)):
	val = z
	it = 0
	n = 0
	
	#print val

	while compAbs(val) < 10 and n < 245:
		it += 1
		val = func(val)
		n += 10
		
	# not exploded
	return n

def plot_j():
	N = 1000		
	dx = 4/float(N)		
			
	x_ax = [(n-(N/2))*dx for n in range(N)]
	y_ax = [(n-(N/2))*dx for n in range(N)]

	#print x_ax

	graph = np.zeros((N,N,3))

	count = 0
	
	vals = {}
	
	for i in range(N):
		for j in range(N):
			
			n_val = isToInf((x_ax[i], y_ax[j]))
			#print n_val, x_ax[i], y_ax[j]
			graph[i][j] = [n_val,n_val,n_val]
			
			try:
				vals[n_val] += 1
			except KeyError:
				vals[n_val] = 1
	
			count += 1
			if count % 100 == 0:
				#print count
				pass

	print vals
	
	plt.imshow(graph, interpolation='nearest')
	plt.show()
	
	
def idfk():
	x = [0.35]
	y = [0.75]
	
	for i in range(7):
		x_n, y_n = func((x[-1],y[-1]))
		x.append(x_n)
		y.append(y_n)
		
	plt.scatter(x,y)
	plt.show()
		
#idfk()
plot_j()