import numpy as np
import sys 
import matplotlib.pyplot as plt

data = sys.argv[1:]
tlen = len(data)
Nx,Ny = 100,50
M = np.zeros((tlen,Nx,Ny))

for t in range(tlen):
    d = np.loadtxt(data[t],skiprows=1)
    matrix = d.reshape((Nx,Ny))
    M[t,:,:] = matrix

mean = np.mean(M,axis=(1,2))
plt.scatter(np.arange(tlen),mean)
plt.savefig('TotalSpinAccOverTime.pdf')
