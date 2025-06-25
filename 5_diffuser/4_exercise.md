---
layout: default
title: Exercise
parent: 5. Diffuser
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the turbulent, incompressible flow through a diffuser did not yield good results compared with experimental measurements. There are two main issues, which might be responsible:
 - Near-wall mesh resolution to coarse with a non-dimensionless wall distance of $$y^+ \approx 20$$.
 - Standard $$k-\epsilon$$ simply not able to model flows under adverse pressure gradients and with separation.

In order to resolve these issues, additional simulations should be performed.


## Tasks

### 1. Increase Near-wall Mesh Resolution

Increase the mesh resolution at the wall by using a total of 12 inflation layers.

#### Subtasks

1. Rename the original case folder from `diffuser` to something more descriptive, like `kEpsilon_coarse`.
2. Duplicate this folder and rename it to `kEpsilon_fine`. This way the results of the first simulation do not get overwritten by this second simulation.
3. Within the `kEpsilon_fine` case folder, remove all results folders (except `0`) and the `postProcessing` folder for a clean setup.
4. Increase the number of inflation layers in `meshDict` in the `system` directory by changing the entry `nLayers` from 1 to 12.
5. Generate the mesh using `cartesian2DMesh` and check the quality of the mesh using `checkMesh`.
6. Rerun the simulation with the solver `simpleFoam`.
7. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Did the convergence change compared to the first simulation?
2. Are there any improvements in the prediction of the flow separation at the lower diffuser wall?



### 2. Simulation with the SST $$k-\omega$$ Turbulence Model

Repeat the simulations with the SST $$k-\omega$$ turbulence model instead of the Standard $$k-\epsilon$$ model. This involves changing the turbulence model, applying suitable boundary conditions for the new variable specific dissipation rate $$\omega$$ and adjusting the solver and discretization schemes.

#### Subtasks

1. Duplicate the folder with the refined mesh from Task 1 and rename it to `kOmegaSST_fine`.
2. Within the `kOmegaSSt_fine` case folder, remove all results folders (except `0`) and the `postProcessing` folder for a clean setup.
3. Change the turbulence model from `kEpsilon` to `kOmegaSST` in the `turbulenceProperties` file in the `constant` dictionary.
4. In the `0` folder, rename the `epsilon` file to `omega` for the new variable solved and apply the following changes to the file itself:
    - Set the name of the object in line 14 to `omega`.
    - Change the dimensions of the variable to $$\text{seconds}^{-1}$$.
    - The inlet boundary condition must be of type `turbulentMixingLengthFrequencyInlet`.
    - Replace the `epsilonWallFunction` at the wall patches with `omegaWallFunction`.
5. In `controlDict`, `fvSchemes`, and `fvSolution` in the `system` directory, replace all instances of `epsilon` with `omega` to use the same discretization schemes, solver settings, residual criteria, and relaxation factors for the $$\omega$$ transport equation as for the $$\epsilon$$ transport equation in the previous simulations.
6. Add the following entry in the `fvSchemes` file, which specifies how the SST $$k-\omega$$ turbulence model computes the distance from a cell to the next wall:
```
wallDist
{
    method              meshWave;
}
```
7. Rerun the simulation with the solver `simpleFoam`.
8. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Are there any improvements in the prediction of the flow separation at the lower diffuser wall?
2. Plot the velocity profile of of all three simulations and the experimental measurements in a single graph in ParaView. Which model is best suited for modelling this complex flow?
