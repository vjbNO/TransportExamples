import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pyla

font = {'size':15}
mpl.rc('font',**font)

data = sys.argv[1:]
Nx = 200
labels = ['1','2','3','4']
c = pyla.cm.coolwarm(np.linspace(0.5,1,len(data)))
m = ['s','o','v','^']
fig1,ax1 = plt.subplots()
for d in range(len(data)):
    dat = np.mean(np.loadtxt(data[d]),axis=0) #average over y direction
    ax1.plot(np.arange(Nx),dat,label=labels[d],color=c[d],marker=m[d])
ax1.legend(title=r'$T_{ex}/T_0$')
ax1.set_xlabel('x (nm)')
ax1.set_ylabel(r'$\mu$')
plt.savefig('Plots/FM_Mu_thermInj_comparison.pdf')
