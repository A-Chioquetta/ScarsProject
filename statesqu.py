from qutip import *
import numpy as np


#Initial state options (use chains with an even number of sites):
# s=0:    |0> = |down down ... down>
# s=2:    |Z2> = |up down up down ... up down> 
# s=2.1:  |Z2'> = |up down... up down DOWN down up down ... up down> (|Z2> with a flip in the middle)
# s=3:    |Z3> = |up down down up down down...up down down> (this state needs to have a multiple of 3 as well, e.g. N=12)
# s=3.1:  |Z3> = |up down down...up down down up down UP up down down... up down down> (|Z3> with a flip around the middle)




up=fock(2,0)
down=fock(2,1)

def instate(s=None,N=0):

    if s==0 or s==None:   #Z0
        psi0=down
        for i in range(N-1):
            psi0=tensor(psi0,down)

    if s==2: #Z2
        psi0=up
        for n in range(N-1):
            if n%2==0:
                psi0=tensor(psi0,down)
            else:
                psi0=tensor(psi0,up)     


    if s==2.1: #Z2 with defect
        psi0=up
        for n in range(N-1):
            if n==(N/2):
                psi0=tensor(psi0,down)
            else:

                if n%2==0:
                    psi0=tensor(psi0,down)


                else:
                    psi0=tensor(psi0,up)


    
    if s==3: #Z3
        psi0=up
        if N%3==0:
            for n in range(int(N-1-(N/3))):
                if n%2==0:
                    psi0=tensor(psi0,down)
                    psi0=tensor(psi0,down)
                else:
                    psi0=tensor(psi0,up)    

                    
    
        else:
            for n in range(int(N-1-int(N/3))):
                if n%2==0:
                    psi0=tensor(psi0,down)
                
                else:
                    psi0=tensor(psi0,down)
                    psi0=tensor(psi0,up)


    if s==3.1: #Z3 with defect
        psi0=up
        for n in np.arange(0,N-1,3):
            if n==0:
                psi0=tensor(psi0,down)
                psi0=tensor(psi0,down)
            elif n==(int(N/2)):
                psi0=tensor(psi0,up)
                psi0=tensor(psi0,down)
                psi0=tensor(psi0,up)
            else:
                psi0=tensor(psi0,up)
                psi0=tensor(psi0,down)
                psi0=tensor(psi0,down)

    


    state=psi0
    return state
