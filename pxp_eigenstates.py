import sys
import os
from numpy import column_stack, savetxt
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import Gt, nsimplify
storing = Options(store_states=True, method='adams')
store = True


import timeit
start =timeit.default_timer()
N=10 # Number of sites
Wt=0.6 	# Perturbation range
Bound = 'PBC' #Boundary conditions (can be PBC or OBC)

########################################################
#Creating operators for the chain
import operators as oper
sx_list, sy_list, sz_list, p_list = oper.generate_operators(N) # Sx,Sy,Sz, P (projector spin down)

##########################################################


#Hamiltonian PXP
H = 0

for n in range(N-2):
    H +=  p_list[n]*sx_list[n+1]*p_list[n+2] 

# Boundary conditions #
if Bound == 'pbc' or Bound == 'PBC':
    H += p_list[N-2]*sx_list[N-1]*p_list[0]+p_list[N-1]*sx_list[0]*p_list[1] #PBC

if Bound == 'obc' or Bound == 'OBC':
    H+= sx_list[0]*p_list[1] + p_list[N-2]*sx_list[N-1] #OBC

####################################
    
####################################
#Loop over different perturbations
for W in np.arange(0.0, Wt, 0.1):

    # Creating the perturbation terms
    if W > 0.0: 
        hw = np.random.uniform(-W/2, W/2, (3*N)) #random and uniform distributions of perturbation strengh values
        m=0
        for n in range(N):
            H+= hw[m]*sx_list[n] + hw[m+1]*sy_list[n] + hw[m+2]*sz_list[n] #perturbating all directions
            m = m+3
    ####################################
   
    ResultsFolder = 'Results'
    os.makedirs(ResultsFolder,exist_ok=True)
    newFolder = os.path.join(ResultsFolder,'Eigenstates')
    os.makedirs(newFolder, exist_ok=True)
    fileDiagName = newFolder+'/EigenstatesPXP_'+ str(N)+'_Perturb'+str(int(W*100)) + Bound  # Naming the files
    
    hEigen = H.eigenstates() #Calculating Eigenstates and Eigenvalues
    qsave(hEigen, fileDiagName) #Save Eigenstates



stop =timeit.default_timer()
print('Time', stop-start )  ##Cheking how long it takes to run the calculations
