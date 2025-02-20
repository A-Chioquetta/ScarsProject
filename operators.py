from qutip import *

def generate_operators(N):
    si = qeye(2)
    sx = sigmax()
    sy = sigmay()
    sz = sigmaz()
    sp = sigmap()
    sm = sigmam()
    p = (si - sz) / 2.0
    q = (si + sz) / 2.0

    sx_list = []
    sy_list = []
    sz_list = []
    sp_list = []
    sm_list = []
    p_list = []
    q_list = []

    for n in range(N):
        op_list = [si] * N

        op_list[n] = sx
        sx_list.append(tensor(op_list))

        op_list[n] = sy
        sy_list.append(tensor(op_list))

        op_list[n] = sz
        sz_list.append(tensor(op_list))

        op_list[n] = sp
        sp_list.append(tensor(op_list))

        op_list[n] = sm
        sm_list.append(tensor(op_list))

        op_list[n] = p
        p_list.append(tensor(op_list))

        op_list[n] = q
        q_list.append(tensor(op_list))

    return sx_list, sy_list, sz_list,p_list, q_list, sp_list, sm_list 
