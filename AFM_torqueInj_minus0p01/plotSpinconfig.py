import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
font = {'size':15}
mpl.rc('font',**font)

data = sys.argv[1]
Nx,Ny = 200,50
d = np.array(np.loadtxt(data,skiprows=1))[:,0]
matrix = d.reshape((Ny,Nx))
plt.imshow(matrix)
plt.savefig('spinconfig.pdf')
