from qutip import *
import numpy as np




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
