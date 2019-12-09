#!/usr/bin/python
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-i","--ifile", help="Input File Datavector - assumed to be masked")
parser.add_argument("-o","--ofile", help="Ouput File Datavector - it will have full length")
args = parser.parse_args()

idata = np.genfromtxt(args.ifile)
xx = np.shape(idata)
odata = np.zeros((xx[0],xx[1]+1))
odata[:,1] = idata[:,-1]
odata[:,0] = 1
for i in range(xx[1]-1):
   odata[:,i+2] = idata[:,i]
np.savetxt(args.ofile, odata)
