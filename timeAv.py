import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
font = {'size':15}
mpl.rc('font',**font)

savename = sys.argv[1]
data = sys.argv[2:]

tlen = len(data)
Nx,Ny = 200,50
M = np.zeros((tlen,Ny,Nx))

for t in range(tlen):
    d = np.array(np.loadtxt(data[t],skiprows=1))[:,0] #x component
    matrix = d.reshape((Ny,Nx))
    M[t,:,:] = matrix

TimeAveragedMu = np.mean(M,axis=0)

np.savetxt('Data/'+savename+'.txt',TimeAveragedMu)

