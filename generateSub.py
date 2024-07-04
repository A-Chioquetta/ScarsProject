#Gerar os vetores dos subespaços ao invés de separar os autovetores de H

import qutip as qt
import numpy as np
from qutip import *

def binary_to_qobj(binary_str):
    # Transform a binary string into a tensor product of 'up' and 'down' states
    # '0' for 'down' (|0⟩) and '1' for 'up' (|1⟩)
    state_list = [qt.basis(2, int(bit)) for bit in binary_str]  # |0⟩ for '0', |1⟩ for '1'
    return qt.tensor(state_list)

def generate_all_spin_states(num_spins):
    # Generates all possible combinations of up and down states for `num_spins`
    states = []
    for i in range(2 ** num_spins):
        # Convert number to binary string padded with zeros
        binary_str = format(i, '0{}b'.format(num_spins))
        # Add to list
        binary_list = [1-int(bit) for bit in binary_str]
        states.append(binary_list)
    return states

num_spins = 12  # Change this number based on your system size
all_spin_states = generate_all_spin_states(num_spins)


group_1 = []
group_2 = []

group_1_states =[]
group_2_states =[]


for binary_list in all_spin_states:
    violates_blockade = any(binary_list[i] == 0 and binary_list[(i + 1) % len(binary_list)] == 0 for i in range(len(binary_list)))

    if violates_blockade:
        group_2.append((binary_list)) 
        group_2_states.append(binary_to_qobj(binary_list)) 
        # pass  
    else:
        group_1.append((binary_list))
        group_1_states.append(binary_to_qobj(binary_list))
        


# print(group_1)
# print(group_2)
# print(group_3)

qsave(group_1_states, 'group1_'+str(num_spins)+'s')
qsave(group_2_states, 'group2_'+str(num_spins)+'s')


