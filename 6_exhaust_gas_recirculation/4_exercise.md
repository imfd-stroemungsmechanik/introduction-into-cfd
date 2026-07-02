---
layout: default
title: Exercise
parent: 6. Exhaust Gas Recirculation
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the turbulent, compressible flow through an exhaust gas recirculation system gave reasonable results. However, there are unresolved issues:
 - The maximum temperature within the computational domain exceeded the inlet temperature of $$900\,\text{K}$$, which is unphysical.
 - The influence of the exhaust gas flow rate on the mixing temperature has not been investigated.

In order to resolve these issues, additional simulations should be performed.


## 1. Bounded Discretization Scheme

In the tutorial, the unlimited second-order gradient scheme `Gauss linear` allowed local temperature overshoots at the sharp interface between the cold air and hot exhaust gas. Gradient limiting constrains the reconstructed face values so they cannot exceed the range of surrounding cell values, thereby enforcing physical bounds on the solution. In this task, the gradient scheme should be changed to a cell-limited variant to eliminate the unphysical temperature overshoot.

### Tasks

1. Create a copy of the `exhaust_gas_recirculation` case directory named `exhaust_gas_recirculation_limited`.
2. Within the copied case folder, remove all time directories (except `0`), all processor folders, and the `postProcessing` folder for a clean setup.
3. In `fvSchemes` in the `system` directory, change the default gradient scheme from `Gauss linear` to `cellLimited Gauss linear 1.0`.
4. Rerun the simulation in parallel:
    1. Decompose the case with `decomposePar`.
    2. Run the simulation in parallel with `mpirun -np 4 foamRun -parallel`.
    3. Reconstruct the case with `reconstructPar`.
5. Recreate the monitoring plots with `python3 create_plots.py`.
6. Visualize the temperature field in ParaView and inspect the region downstream of the exhaust gas inlet.

#### Questions

1. Does the maximum temperature in the domain now stay below $$900\,\text{K}$$?
2. How does the maximum temperature plot from `cellMax` compare to the original simulation?
3. Do you notice any differences in the overall flow field or the mixing temperature profile compared to the unlimited scheme?


## 2. Variation of Exhaust Gas Flow Rate

In the tutorial, the exhaust gas volumetric flow rate was set to $$Q = 0.0025\,\text{m}^3\text{/s}$$. In practice, the amount of recirculated exhaust gas varies depending on engine operating conditions. In this task, additional simulations with different exhaust gas flow rates should be performed to investigate their effect on the mixing temperature.

### Tasks

1. Create a copy of the `exhaust_gas_recirculation_limited` case directory (with the bounded gradient scheme from Task 1) and rename it to `exhaust_gas_recirculation_Q0.00125`.
2. Within the copied case folder, remove all time directories (except `0`), all processor folders, and the `postProcessing` folder for a clean setup.
3. In the velocity boundary condition file `U` in the `0` directory, change the `volumetricFlowRate` at the `inlet_exhaust` from `0.0025` to `0.00125`.
4. Rerun the simulation in parallel:
    1. Decompose the case with `decomposePar`.
    2. Run the simulation in parallel with `mpirun -np 4 foamRun -parallel`.
    3. Reconstruct the case with `reconstructPar`.
5. Recreate the monitoring plots with `python3 create_plots.py` and visualize the results in ParaView.
6. Repeat steps 1–5 for exhaust gas volumetric flow rates of $$Q = 0.005\,\text{m}^3\text{/s}$$ and $$Q = 0.0075\,\text{m}^3\text{/s}$$.

#### Questions

1. How does the average outlet temperature change with increasing exhaust gas flow rate?
2. How does the maximum temperature in the domain change across the different flow rates?
3. Compare the temperature contour and mixing temperature profile for all four flow rates. At what distance downstream of the T-junction is the mixing process approximately complete for each case?