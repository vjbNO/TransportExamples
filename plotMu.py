import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
font = {'size':15}
mpl.rc('font',**font)
'''
a = np.array([1,2,3,4,1.1,2.1,3.1,4.1])
b = a.reshape((2,4))
print(a)
print(b)
stop'''

data = sys.argv[1:]

tlen = len(data)
Nx,Ny = 150,50
M = np.zeros((tlen,Ny,Nx))

for t in range(tlen):
    d = np.array(np.loadtxt(data[t],skiprows=1))[:,0]
    matrix = d.reshape((Ny,Nx))
    M[t,:,:] = matrix


meanPerTime = np.mean(M,axis=1)
fig1,ax1 = plt.subplots()
ax1.scatter(np.arange(tlen),meanPerTime[:,20],label='20nm',color='black',marker='s')
ax1.scatter(np.arange(tlen),meanPerTime[:,80],label='80nm',color='blue')
#ax1.scatter(np.arange(tlen),meanPerTime[:,80],label='60nm')
plt.legend(title='position')
ax1.set_xlabel('t (ps)')
ax1.set_ylabel(r'$\mu$')
plt.savefig('Plots/TotalSpinAccOverTime_FM_thermalInj_hotter.pdf')'''

TimeAveragedMu = np.mean(M[int(tlen/10):,:,:],axis=0)
fig2,ax2 = plt.subplots()
ax2.scatter(np.arange(Nx),np.mean(TimeAveragedMu,axis=0))
ax2.set_xlabel('x (nm)')
ax2.set_ylabel(r'$\mu$')
#ax2.set_xlim(10,90)
plt.savefig('Plots/TimeAvSpinAccumulationOverSpace_FM_thermalInj_hotter.pdf')
