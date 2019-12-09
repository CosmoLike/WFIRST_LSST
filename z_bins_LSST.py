#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm#, SymLogNorm
# import matplotlib.image as mpimg
import sys
import math
from numpy import linalg as LA

###########################################################

pathOut = "./tex_paper/plots/"
Nell = 15
Ng = 10
Ns = 10

###########################################################
###########################################################
# full dn/dz clustering

path = "zdistris/SRD_zdistri_model_z0=2.800000e-01_beta=9.000000e-01_Y10_lens.txt"
clusteringdensity=48.0
data = np.genfromtxt(path)
zmin = data[:,0]
z = data[:,1]
zmax = data[:,2]
nz = data[:,3]

delta=3.5/300.
nzsum=np.cumsum(nz)
print nzsum[299]
norm=nzsum[299]*delta/clusteringdensity
nz=nz/norm
fig=plt.figure(1)
ax=fig.add_subplot(111)

ax.plot(z, nz, 'blue', lw=2, label=r'LSST Clustering Sample')


# ###########################################################
# # lens bins

path = "zdistris/LSST_zdist_lenses_bin"

for iS in range(Ns):
   data = np.genfromtxt(path+str(iS)+".txt")
   z = data[:,0]
   #nz_norm = data[:,1]
   nz = data[:,1]
   #print "normalized to", np.trapz(nz,z)
   
   ax.fill_between(z, 0, nz*clusteringdensity/18., facecolor=plt.cm.winter(1.*iS/Ns), edgecolor='', alpha=0.8)
ax.plot([], [], color=plt.cm.winter(0.), lw=2, alpha=0.7)

# ###########################################################

# path = pathOut+"datav/LSST_cmbs4_LSSxCMB_Nell25_Ns10_Ng4_zdist_lenses_bin"

# for ig in range(Ng):
#    data = np.genfromtxt(path+str(ig)+".txt")
#    z = data[:,0]
#    nz_norm = data[:,1]
#    nz = data[:,2]
#    bz = data[:,3]
#    print "normalized to", np.trapz(nz,z)

#    ax.fill_between(z, 0., 10.*nz, facecolor=plt.cm.autumn(1.*ig/Ng), edgecolor='', alpha=1)
# ax.plot([], [], color=plt.cm.autumn(0.), lw=2, alpha=0.7, label=r'lenses$\times$10')

###########################################################
###########################################################
# full dn/dz clustering

path = "zdistris/SRD_zdistri_model_z0=1.100000e-01_beta=6.800000e-01_Y10_source.txt"
lensingdensity=26.0
data = np.genfromtxt(path)
zmin = data[:,0]
z = data[:,1]
zmax = data[:,2]
nz = data[:,3]

delta=3.5/300.
nzsum=np.cumsum(nz)
print nzsum[299]
norm=nzsum[299]*delta/lensingdensity
nz=nz/norm

fig=plt.figure(1)
ax=fig.add_subplot(111)

ax.plot(z, nz, 'RED', lw=2, label=r'LSST Weak Lensing Sample')


#  source bins
path2 = "zdistris/LSST_zdist_sources_bin"
for ig in range(Ng):
   data = np.genfromtxt(path2+str(ig)+".txt")
   z = data[:,0]
   #nz_norm = data[:,1]
   nz = data[:,1]
   #print "normalized to", np.trapz(nz,z)

   ax.fill_between(z, 0., nz*lensingdensity/10., facecolor=plt.cm.autumn(1.*ig/Ng), edgecolor='', alpha=0.7)
ax.plot([], [], color=plt.cm.autumn(0.), lw=2, alpha=0.7)

# ###########################################################
# # lensing efficiency

# path = pathOut+"zdist/lensing_efficiency.txt"

# data = np.genfromtxt(path)
# z_cmblens = data[:,0]
# w_cmblens = data[:,1]

# ax.plot(z_cmblens, w_cmblens * 35., 'm-', lw=2, label=r'CMB lensing efficiency')

###########################################################

ax.plot([], [], 'k', lw=2)
#
ax.set_xlim((0., 3.5))
ax.set_ylim((0., 40))
ax.legend(loc=1)
ax.set_xlabel(r'$z$', fontsize=24)
ax.set_ylabel(r'$\frac{dN}{d\Omega \, dz}$ [arcmin$^{-2}$]', fontsize=22)

fig.savefig(pathOut+"zbins_LSST.pdf", bbox_inches='tight')

