# ScarsProject

This repository contains codes and results for the PXP model.

## Summary

The PXP model is implemented here using the QuTiP library. Below is a brief overview of the main components:

### Prerequisites

Ensure you have the Qutip library installed to run the codes effectively.

### Files

- **TimeEvol_PXP.py**: This script evaluates the time evolution of the PXP model with perturbation (optional), offering options for Periodic Boundary Conditions (PBC) or Open Boundary Conditions (OBC).
  
  **Hamiltonian Definitions:**
  - **H_{PXP}**: $ \sum_{i=1}^{N} P_{i-1}X_{i}P_{i+1} $
  - **H_{OBC}**: $ X_1P_2 + P_{N-1}X_{N} $
  - **H_{perturb}**: $ \sum_{i}^{N} (W_{X}^i X_{i} + W_{Y}^i Y_{i} + W_{Z}^i Z_{i}) $

- **pxp_eigenstates.py**: This script evaluates the eigenstates of the Hamiltonian with the same options as above.

- **overlapEigen.py**: Evaluates the overlap between the initial state and the eigenstates of the system.

- **statesqu.py**: Module for creating initial states.

- **operators.py**: Module for creating chain operators.

### Results (Optional)

Results are included in the repository, demonstrating the application of the PXP model and the functionality of the provided scripts.


