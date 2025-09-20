import numpy as np
import matplotlib.pyplot as plt
import math

# loading data
d = np.loadtxt('SED_U-2.0_NH19._BPASS_SED_bin-imf135all_100.z001_5e6_full_burst_dens2_samegasphaseZ.dat',skiprows=1)
lam = d[:,0] # in Angstroms
finc = d[:,1] # incident flux (BPASS), in cgs unit
fntrans = d[:,3] # net transmitted flux (BPASS), in cgs units

# getting pretty colours
cols = plt.cm.magma(np.linspace(0,0.9,8))

# making plot with 4 subplots
fig = plt.figure(figsize=(21,6))
ax1 = plt.subplot(1,3,1) # the number are (number of rows, number of columns, which panel you're plotting on)
ax2 = plt.subplot(1,3,2)
ax3 = plt.subplot(1,3,3)

### plot in ax1 (left panel)
ax = ax1
ax.plot(lam,finc,color='black',ls=':',lw=1.5,label=r'F$_{incident}$',zorder=100)#a higher zorder means it gets plotted "on top"
ax.plot(lam,fntrans,color=cols[3],ls='-',lw=1.5,label=r'F$_{net transmitted}$')
ax.text(3e3,2e-1,'Example text',size=16,color='#707070')
ax.set_title('Plotting lines',size=16,color=cols[3],weight='bold')
ax.legend(loc=3,fontsize='x-large',framealpha=1)

### plot in ax2 (centre panel)
ax = ax2
fake_low = np.array([1e-7]*len(lam)) # this makes an array where each element is 1e-7
ax.fill_between(lam,fake_low,finc,facecolor='none',edgecolor='black',hatch='x',zorder=100,label=r'F$_{incident}$')
ax.fill_between(lam,fake_low,fntrans,color=cols[5],label=r'F$_{net transmitted}$')
ax.set_title('Filling the area under the curve',size=16,color=cols[5],weight='bold')
ax.legend(loc=1,fontsize='x-large',frameon=False)

### plot in ax3 (right panel)
ax = ax3
X = np.linspace(0,10,20)
Y,Z = [],[]
for x in X:
    Y.append(math.sin(x))
    Z.append(x**2)
sc = ax.scatter(X,Y,c=Z,cmap='magma',s=100)
cb = plt.colorbar(sc,ax=ax)
cb.set_label(label=r'X$^2$', size='x-large')
cb.ax.tick_params(labelsize='large')
ax.set_title('Scatter plot + colour bar',size=16,color=cols[0],weight='bold')

axes = [ax1,ax2,ax3]
for ax in axes:
    ax.tick_params(axis='both',which='major',labelsize=14)
    if ax == ax1 or ax == ax2:
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel(r'$\lambda$ [$\AA$]',size=16)
        ax.set_ylabel(r'F$_{\lambda}$ [cgs]',size=16)
        ax.set_xlim(500,1e4)
        ax.set_ylim(1e-5,1e0)
    else:
        ax.set_xlabel(r'X',size=16)
        ax.set_ylabel(r'sin(X)',size=16)


plt.tight_layout()
plt.savefig('example_plot.pdf')
