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

N=18 # Number of sites
Wt=0.6 	# Perturbation range +0.1
Bound = 'PBC' #Boundary conditions (can be PBC or OBC)
stateType = 2 # Initial state (can be 0,2,2.1,3 or 3.1) -- For more info check file statesqu.py

########################################################
#Creating operators for the chain
import operators as oper
sx_list, sy_list, sz_list, p_list = oper.generate_operators(N)


##########################################################
# Creating the initial state
import statesqu as st
psi0=st.instate(s=stateType,N=N) #initial state
##########################################################

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
##############################################################

#Loop over different perturbations
for W in np.arange(0.0, Wt, 0.1):

    # Creating the perturbation terms
    if W > 0.0: 
        hw = np.random.uniform(-W/2, W/2, (3*N)) #random and uniform distributions of perturbation strengh values
        m=0
        for n in range(N):
            H+= hw[m]*sx_list[n] + hw[m+1]*sy_list[n] + hw[m+2]*sz_list[n] #perturbating all directions
            m = m+3

    # Observable 
    B=0
    for n in range(N-1):
        B += sz_list[n]*sz_list[n+1] #correlation

    B=B/float(N-1) #average correlation



    nt = 1000 #Number of time steps
    ts = np.linspace(0.,20.,nt) # Time range

    result = sesolve(H, psi0, ts, [B],options=storing, progress_bar = True) #Time evolution
    psit= result.states # States in each time step


    gt=[] #List of Fidelity
    WList =[] #List of perturbation values

    for i in range(nt):
        gt.append(np.abs(psi0.overlap(psit[i]))**2)
        WList.append(W)

    ResultsFolder = 'Results'
    os.makedirs(ResultsFolder,exist_ok=True)
    newFolder = os.path.join(ResultsFolder,'Z'+ str(stateType))
    os.makedirs(newFolder, exist_ok=True)
    
    fMeasurement = os.path.join(newFolder, 'Measurements')
    os.makedirs(fMeasurement, exist_ok=True)
    FileName1 = newFolder+'/Measurements/PXP_' + str(N) + '_Z'+ str(stateType)+'_W0' +str(int(W*100))+ Bound + '.dat'  #File time X correlation X fidelity
    DataOut = column_stack((ts, result.expect[0],gt, WList)) #time vs observable vs fidelity vc perturbation strengh
    savetxt(FileName1, DataOut)

    # if your system is +16 sites uncomment only if you have A LOT of memory avaiable
    # fTimeEvolved = os.path.join(newFolder, 'TimeEvolved')
    # os.makedirs(fTimeEvolved, exist_ok=True)
    # FileName2 = newFolder+'/TimeEvolved/EvolutionPXP_' +str(N) + '_Z'+str(stateType)+ '_Perturb'+str(int(W*100))+ Bound 
    # qsave(psit, FileName2) #Save evolved states

stop =timeit.default_timer()
print('Time', stop-start )  ##Cheking how long it takes to run the calculations
