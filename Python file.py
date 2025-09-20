import numpy as np
import matplotlib.pyplot as plt
import math

# loading data
d = np.loadtxt('spectra-bin-imf135_300.z002.dat',skiprows=1)
lam = d[:,0] # in Angstroms
#finc = d[:,2] # incident flux (BPASS), in cgs unit
#fntrans = d[:,3] # net transmitted flux (BPASS), in cgs units
metallicities_002= d[:,5]

d = np.loadtxt('spectra-bin-imf135_300.z003.dat',skiprows=1)
lam = d[:,0]
metallicities_003= d[:,5]

d = np.loadtxt('spectra-bin-imf135_300.z008.dat',skiprows=1)
lam = d[:,0]
metallicities_008= d[:,5]

# getting pretty colours
cols = plt.cm.magma(np.linspace(0,0.9,8))

# making plot with 4 subplots
fig = plt.figure(figsize=(21,6))
ax1 = plt.subplot(1,1,1) # the number are (number of rows, number of columns, which panel you're plotting on)


### plot in ax1 (left panel)
ax = ax1

ax.plot(lam,metallicities_002,color='green',ls=':',lw=1.5,label=r'metallicities.002 age = young',zorder=100)#a higher zorder means it gets plotted "on top" THis is used to make the box in the corner 
ax.plot(lam,metallicities_003,color='red',ls=':',lw=1.5,label=r'metallicities.003 age = young',zorder=100)#a higher zorder means it gets plotted "on top" THis is used to make the box in the corner
ax.plot(lam,metallicities_008,color='blue',ls=':',lw=1.5,label=r'metallicities.008 age = young',zorder=100)#a higher zorder means it gets plotted "on top" THis is used to make the box in the corner 


#ax.text(3,1,'Lucas de la Vega Mazzoni',size=9,color='#707070', zorder=100)#this plots the text in the top right of graph

ax.set_title('Plotting lux vs Wavelength',size=16,color=cols[3],weight='bold')

ax.legend(loc=3,fontsize='x-large',framealpha=1)

axes = [ax1]
for ax in axes:
    ax.tick_params(axis='both',which='major',labelsize=14)
    if ax == ax1:
        ax.set_xscale('linear')
        ax.set_yscale('linear')
        ax.set_xlabel(r'$\lambda$ [$\AA$]',size=16)
        ax.set_ylabel(r'Lux',size=16)
        ax.set_xlim(500,3000)
#        ax.set_ylim(0.7699667E+06,0.204317E+07)
    else:
        print("hello world")


plt.tight_layout()
plt.savefig('comparing_metallicities_of_stars_vs_wavelength.pdf')
plt.show()
