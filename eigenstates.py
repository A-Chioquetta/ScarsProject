from numpy import column_stack, savetxt
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import Gt, nsimplify
storing = Options(store_states=True, method='adams')
store = True


import timeit
start =timeit.default_timer()

N=12 # Number of sites
W=0.0	# Perturbation range
Bound = 'PBC' #Boundary conditions (can be PBC or OBC)
# stateType = 0 # Initial state (can be 0,2,2.1,3 or 3.1) -- For more info check file statesqu.py

########################################################
#Creating operators for the chain
si = qeye(2)
sx = sigmax()
sy = sigmay()
sz = sigmaz()
sp = sigmap()
sm = sigmam()
p=(si-sz)/2.0

sx_list = []
sy_list = []
sz_list = []
sp_list = []
sm_list = []
p_list = []




#Creating operators for the chain
import operators as oper
sx_list, sy_list, sz_list, p_list = oper.generate_operators(N) # Sx,Sy,Sz, P (projector spin down)
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

hw = np.random.uniform(-W/2, W/2, (3*N)) #random and uniform distributions of perturbation strengh values
m=0
for n in range(N):
    H+= hw[m]*sx_list[n] + hw[m+1]*sy_list[n] + hw[m+2]*sz_list[n] #perturbating all directions
    m = m+3
##############################################################

eigenFile = 'Eigenstates/PXP'+str(N)+'s'+'_W0' +str(int(W*100))+Bound
hEigen = H.eigenstates()
qsave(hEigen, eigenFile)

stop =timeit.default_timer()
print('Time', stop-start )


