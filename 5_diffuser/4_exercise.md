---
layout: default
title: Exercise
parent: 5. Diffuser
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the turbulent, incompressible flow through a diffuser did not yield good results compared with experimental measurements. The main reason is the choice of the turbulence model, namely the Standard $$k-\epsilon$$, which is not able to model flows under adverse pressure gradients and with separation.

In order to resolve this issue, an additional simulation should be performed.


## Simulation with SST $$k-\omega$$ Turbulence Model

Repeat the simulations with the SST $$k-\omega$$ turbulence model instead of the Standard $$k-\epsilon$$ model. This involves changing the turbulence model, applying suitable boundary conditions for the new variable specific dissipation rate $$\omega$$ and adjusting the solver and discretization schemes.

### Tasks

1. Create a copy of the `diffuser` case directory for a second simulation called `diffuser_kOmegaSST`.
2. Within the `diffuser_kOmegaSST` case folder, remove all results folders (except `0`) and the `postProcessing` folder for a clean setup.
3. Change the turbulence model from `kEpsilon` to `kOmegaSST` in the `momentumTransport` file in the `constant` dictionary.
4. In the `0` folder, rename the `epsilon` file to `omega` for the new variable solved and apply the following changes to the file itself:
    - Set the name of the object in line 14 to `omega`.
    - Change the dimensions of the variable to $$\text{seconds}^{-1}$$.
    - The inlet boundary condition must be of type `turbulentMixingLengthFrequencyInlet`.
    - Replace the `epsilonWallFunction` at the wall patches with `omegaWallFunction`.
5. In `functions`, `fvSchemes`, and `fvSolution` in the `system` directory, replace all instances of `epsilon` with `omega` to use the same discretization schemes, solver settings, and relaxation factors for the $$\omega$$ transport equation as for the $$\epsilon$$ transport equation in the previous simulations.
6. Add the following entry in the `fvSchemes` file, which specifies how the SST $$k-\omega$$ turbulence model computes the distance from a cell to the nearest wall:
```
wallDist
{
    method              meshWave;
}
```
7. Rerun the simulation with the solver `foamRun`.
8. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Are there any improvements in the prediction of the flow separation at the lower diffuser wall?
2. Plot the velocity profile of both simulations and the experimental measurements in a single graph in ParaView. Which model is best suited for modelling this complex flow?
3. How does the skin friction coefficient improve with the SST $$k-\omega$$ turbulence model?
