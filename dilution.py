# Evaluate how the initial state is spread in the constrained subspace 

import sys
from numpy import column_stack, savetxt
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import Gt, nsimplify
storing = Options(store_states=True, method='adams')
store = True

N=14
Bound = 'PBC'
stateType = 0

import statesqu as st
psi0=st.instate(s=stateType,N=N) #initial state

eigenFile = 'Subspace_eigenstates_'+ str(N)+'s_'+Bound
energyFile = 'Subspace_energies'+ str(N)+'s_'+Bound 
eigenstates = qload(eigenFile)  # Load the eigenstates of the subspace in full space form
energies = qload(energyFile) # Load eigenvalues




OverList1 =[]
LogList1 = []
OverEnergy1 = []
for i in range(len(eigenstates)):
    eigen = eigenstates[i]
    energy = energies[i]
    overlap = np.abs(eigen.overlap(psi0))**2
    if overlap <0.00000001: # Truncation
        overlap = 0.0
    else:
        OverList1.append(overlap) #List of overlap between the chosen state and the eigenstates
        OverEnergy1.append(energy) #List of energies
        LogList1.append(np.log10(overlap)) #List of log(overlap)

    
result1 = column_stack((OverEnergy1,OverList1,LogList1))
resultFile1 = 'Dilution/DilutionPXP_SUBSPACE_'+str(N)+ Bound + 'Z'+str(stateType)+'.dat'
savetxt(resultFile1,result1)


