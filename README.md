# ScarsProject

This repository contains codes and results for the PXP model.

## Summary

The PXP model is implemented here using the QuTiP [1,2] library. Below is a brief overview of the main components:

### Prerequisites

Ensure you have the Qutip library installed to run the codes effectively.

### Files

- **TimeEvol_PXP.py**: This script evaluates the time evolution of the PXP model with perturbation (optional), offering options for Periodic Boundary Conditions (PBC) or Open Boundary Conditions (OBC).
  
  **Hamiltonian Definitions:**
  
  
  <img src= 'images/pxp.png' width='190'>
  <br>
  <img src= 'images/obc.png' width='250'>
  <br>

  <img src= 'images/perturb.png' width='280'>
 

- **pxp_eigenstates.py**: This script evaluates the eigenstates of the Hamiltonian with the same options as above.

- **overlapEigen.py**: Evaluates the overlap between the initial state and the eigenstates of the system.

- **statesqu.py**: Module for creating initial states.

- **operators.py**: Module for creating chain operators.

### Results (Optional)

Results are included in the repository, demonstrating the application of the PXP model and the functionality of the provided scripts.



[1] J. R. Johansson, P. D. Nation, and F. Nori: "QuTiP 2: A Python framework for the dynamics of open quantum systems.", Comp. Phys. Comm. 184, 1234 (2013) [DOI: 10.1016/j.cpc.2012.11.019].

[2] J. R. Johansson, P. D. Nation, and F. Nori: "QuTiP: An open-source Python framework for the dynamics of open quantum systems.", Comp. Phys. Comm. 183, 1760–1772 (2012) [DOI: 10.1016/j.cpc.2012.02.021].
