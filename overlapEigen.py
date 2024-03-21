import sys
import os
from numpy import column_stack, savetxt
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import Gt, nsimplify

import timeit
start =timeit.default_timer()
# Run pxp_eigenstates.py before this one

# Initial config below must be the same as in pxp_eigenstates.py
N=10 # Number of sites
Wt=0.6 	# Perturbation range
Bound = 'PBC' #Boundary conditions (can be PBC or OBC)
stateType =2

import statesqu as st
psi0=st.instate(s=stateType,N=N) #initial state

for W in np.arange(0.0, Wt, 0.1):
    fileDiag = 'Results/Eigenstates/EigenstatesPXP_'+ str(N)+'_Perturb'+str(int(W*100)) + Bound #Files with Eigenstates
    hEigen = qload(fileDiag)



    eigenOver =[]
    eigenVal =[]
    for i in range(2**N):
        eigenOver.append(np.abs(psi0.overlap(hEigen[1][i]))**2) #Overlap between initial state and eigenvectors
        eigenVal.append(hEigen[0][i]) #Eigenvalues


    maxEigenOver = eigenOver[0]
    eigenValMax = hEigen[0][0]
    maxEigen = hEigen[1][0]

    for i in range((2**N)-1):
        if eigenOver[i+1]> maxEigenOver or eigenOver[i+1] ==maxEigenOver:
            maxEigenOver = eigenOver[i+1] #largest overlap between initial state and eigenvectors
            maxEigen = hEigen[1][i+1] #eigenvector related to the largest overlap
            eigenValMax = hEigen[0][i+1] #eigenvalue related to the largest overlap
        
    
    ResultsFolder = 'Results'
    os.makedirs(ResultsFolder,exist_ok=True)
    newFolder = os.path.join(ResultsFolder,'Overlaps_Z'+str(stateType))
    os.makedirs(newFolder, exist_ok=True)

    eigenOverlap =column_stack((eigenVal,eigenOver)) #Overlap vs eigenvalues
    fOverlapEigen = os.path.join(newFolder, 'OverlapEigen')
    os.makedirs(fOverlapEigen, exist_ok=True)
    fileOverEigen = newFolder+'/OverlapEigen/OverlapEigen_PXP' + str(N)+ '_Z'+ str(stateType)+'W0'+str(int(W*100)) + Bound 
    savetxt(fileOverEigen, eigenOverlap)
    
    maxEigenOver = column_stack((maxEigenOver,eigenValMax)) #Largest overlap vs eigenvalue related to the largest overlap
    fMaxOverlap = os.path.join(newFolder, 'MaxOverlap')
    os.makedirs(fMaxOverlap, exist_ok=True)
    fileMaxEigenOver = newFolder+'/MaxOverlap/maxEigen_PXP'+ str(N)+ '_Z'+ str(stateType)+'W0'+str(int(W*100)) + Bound 
    savetxt(fileMaxEigenOver, maxEigenOver)

    fMaxOverlapEigen = os.path.join(newFolder, 'MaxOverlapEigen')
    os.makedirs(fMaxOverlapEigen, exist_ok=True)
    fileMaxEigenvector = newFolder+'/MaxOverlapEigen/EigenstateMax_PXP'+ str(N)+ '_Z'+ str(stateType)+'W0'+str(int(W*100)) + Bound 
    qsave(maxEigen,fileMaxEigenvector)