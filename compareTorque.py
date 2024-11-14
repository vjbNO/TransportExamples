import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pyla

font = {'size':15}
mpl.rc('font',**font)

data = sys.argv[1:]
Nx = 200
labels = [r'$+x, \tau=0.02$',r'$+x, \tau=0.01$',r'$-x, \tau=0.01$',r'$-x, \tau=0.02$']#,'4','5']
labels2 = [r'$0.01$',r'$0.02$']
c = pyla.cm.coolwarm(np.linspace(0,1,len(data)))
m = ['s','o','v','^']
fig1,(ax1,ax2) = plt.subplots(1,2,figsize=(10,5))

for d in range(len(data)):
    dat = np.mean(np.loadtxt(data[d]),axis=0) #average over y direction
    ax1.plot(np.arange(Nx),dat,label=labels[d],color=c[d],marker=m[d])

ax2.plot(np.arange(Nx),np.mean(np.loadtxt(data[2]),axis=0)-np.mean(np.loadtxt(data[1]),axis=0),label=r'$0.01$',linewidth=4,color=c[-2],marker=m[-2])
ax2.plot(np.arange(Nx),np.mean(np.loadtxt(data[3]),axis=0)-np.mean(np.loadtxt(data[0]),axis=0),label=r'$0.02$',linewidth=4,color=c[-1],marker=m[-1])
ax1.legend(title='torque direction \n and strength (T)')
ax2.legend(title=r'$\tau$ (T)')
ax1.set_xlabel('x (nm)')
ax2.set_xlabel('x (nm)')
ax1.set_ylabel(r'$\mu$')
ax2.set_ylabel(r'$\Delta \mu$')

plt.subplots_adjust(left=0.1,bottom=0.15,right=0.99,top=0.98,wspace=0.3)
plt.savefig('Plots/FM_Mu_torqueInj_comparison.pdf')
