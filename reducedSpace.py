#Reduced space

import sys
import os
from numpy import column_stack, savetxt
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import Gt, nsimplify
import timeit
start =timeit.default_timer()

#Parameters
N=12 # Number of sites
W = 0.0
Bound = 'PBC' #Boundary conditions (can be PBC or OBC)

########################################################
#Creating operators for the chain
import operators as oper
sx_list, sy_list, sz_list, p_list = oper.generate_operators(N) # Sx,Sy,Sz, P (projector spin down)


#Hamiltonian PXP
H = 0
for n in range(N-2):
    H +=  p_list[n]*sx_list[n+1]*p_list[n+2] 

# Boundary conditions #
if Bound == 'pbc' or Bound == 'PBC':
    H += p_list[N-2]*sx_list[N-1]*p_list[0]+p_list[N-1]*sx_list[0]*p_list[1] #PBC

if Bound == 'obc' or Bound == 'OBC':
    H+= sx_list[0]*p_list[1] + p_list[N-2]*sx_list[N-1] #OBC

hw = np.random.uniform(-W/2, W/2, (3*N)) #random and uniform distributions of perturbation strengh values
m=0
for n in range(N):
    H+= hw[m]*sx_list[n] + hw[m+1]*sy_list[n] + hw[m+2]*sz_list[n] #perturbating all directions
    m = m+3


subSpace1 =qload('group1_'+str(N)+'s') # load constrained subspace base
subSpace1_dag = [state.dag() for state in subSpace1] 
# test =[]
H2 = np.zeros((len(subSpace1), len(subSpace1)), dtype=complex)
for i in range(len(subSpace1)):
    for j in range(len(subSpace1)):
        H2[i,j] = H.matrix_element(subSpace1_dag[i],subSpace1[j]) #H in the constrained subspace base

print("passo 1")
        

H2 = Qobj(H2) # Transform to Qobj so QuTip can operate
print("passo 2")
eigen2 = H2.eigenstates() #Evaluate the eigenstates
print("passo 3")


print("passo 4")
eigenSubspace_tot =[]
energySubspace_tot =[]
for n in range(len(subSpace1)):
    eigenElement_n = eigen2[1][n].full()
    eigenSubspace_n = eigenElement_n[0][0]*subSpace1[0]
    for i in np.arange(1,len(subSpace1),1):
        eigenSubspace_n += eigenElement_n[i][0]*subSpace1[i]  # Eigenstate in the full space
        

    eigenSubspace_tot.append(eigenSubspace_n)
    energySubspace_tot.append(eigen2[0][n])
    print(n)
qsave(eigenSubspace_tot, 'SubspacePerturb_eigenstates_'+ str(N)+'s_'+'_W0' +str(int(W*100))+Bound)
qsave(energySubspace_tot, 'SubspacePerturb_energies'+ str(N)+'s_'+'_W0' +str(int(W*100))+Bound)

