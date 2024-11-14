import numpy as np
import sys 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pyla

font = {'size':15}
mpl.rc('font',**font)

data = sys.argv[1:]
Nx = 150
labels = [r'$+\textbf{e}_x, \tau=0.02$',r'$+\textbf{e}_x, \tau=0.01$',r'$-\textbf{e}_x, \tau=0.01$',r'$-\textbf{e}_x, \tau=0.02$']#,'4','5']
#labels = ['2','3','4','5']
c = pyla.cm.coolwarm(np.linspace(0,1,len(data)))
m = ['s','o','v','^']
#fig1,(ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
fig1,ax1 = plt.subplots()
for d in range(len(data)):
    dat = np.mean(np.loadtxt(data[d]),axis=0) #average over y direction
    ax1.plot(np.arange(Nx),dat,label=labels[d],color=c[d],marker=m[d])
    #ax2.plot(np.arange(Nx),dat,label=labels[d],color=c[d],marker=m[d])
ax1.legend(title=r'\textbf{$p$}')
#ax1.legend(title=r'$T_{ex}/T_0$')
ax1.set_xlabel('x (nm)')
#ax2.set_xlabel('x (nm)')
ax1.set_ylabel(r'$\mu$')
#ax2.set_ylabel(r'$\mu$')
#ax2.set_yscale('log')
#ax2.set_xlim(10,90)
plt.savefig('Plots/TimeAvSpinAccumulationOverSpace_FM_torqueInj_comparison.pdf')
#plt.savefig('Plots/TimeAvSpinAccumulationOverSpace_FM_thermInj_comparison.pdf')
