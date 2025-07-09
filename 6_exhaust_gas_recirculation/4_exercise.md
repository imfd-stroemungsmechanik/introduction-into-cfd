---
layout: default
title: Exercise
parent: 6. Exhaust Gas Recirculation
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the turbulent, compressible flow through a exhaust gas recirculation system did give reasonable results. However, there are unresolved issues:
 - Maximum and minimum temperature within the computational domain where unphysical.
 - How does the mixing temperature as well as maximum temperature at the outlet change with varying exhaust gas flow rate?

In order to resolve these issues, additional simulations should be performed.


## Tasks

### 1. Improved Discretization Schemes

Repeat the simulation with a limited gradient scheme to suppress unphysical temperature.

#### Subtasks

1. Duplicate the case folder and rename it to `exhaust_gas_recirculation_gradient_scheme`. This way the results of the first simulation do not get overwritten by this second simulation.
2. Within the `exhaust_gas_recirculation_gradient_scheme` case folder, remove all results folders (except `0`), processor folder, and the `postProcessing` folder for a clean setup.
3. Set the default gradient scheme in `fvSchemes` in the `system` directory from `Gauss linear` to `cellLimited Gauss linear 1.0`.
4. Rerun the simulation in parallel:
    1. Decompose the case with `decomposePar`
    2. Run the simulation in parallel with `mpirun -np 4 rhoPimpleFoam -parallel`.
    3. Reconstruct the case with `reconstructPar`.
5. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Did the limited gradient scheme remove the unphysical temperature?


### 2. Variation of Exhaust Gas Flow Rate

Repeat the simulations with different volumetric flow rates of the exhaust gas.

#### Subtasks

1. Duplicate the folder with the updated discretization schemes from Task 1 and rename it to `exhaust_gas_recirculation_0.00125`.
2. Within the `exhaust_gas_recirculation_0` case folder, remove all results folders (except `0`), processor folder, and the `postProcessing` folder for a clean setup.
3. Change the volumetric flow rate of the `inlet_exhaust` from `0.0025` to `0.00125`.
4. Rerun the simulation in parallel:
    1. Decompose the case with `decomposePar`
    2. Run the simulation in parallel with `mpirun -np 4 rhoPimpleFoam -parallel`.
    3. Reconstruct the case with `reconstructPar`.
5. Analyse the simulation results with ParaView similar to the first simulation.
6. Repeat steps 1-5 with volumetric flow rates of 0.005 and 0.0075.


#### Questions

1. How does the maximum and average outlet temperature change with varying exhaust gas flow rate?
