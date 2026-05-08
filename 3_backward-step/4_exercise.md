---
layout: default
title: Exercise
parent: 3. Backward-Step
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the incompressible flow over a backward-facing step had unresolved issues, namely:
 - end time of 1 second might be too short,
 - influence of the mesh resolution was not investigated,
 - spatial and temporal accuracy was only of first order.

In order to resolve these issues, additional simulations should be performed.


## 1. Increase End Time

The simulation was run for 1 second of flow time. As both the residuals and the maximum velocity had not yet reached steady values, the simulation may not be fully converged. In this task, the end time should be extended to verify convergence.

### Tasks

1. Change the `endTime` in the `controlDict` in the `system` directory from 1 to 2 seconds.
2. Rerun the simulation with `foamRun` and recreate the plots with `python3 create_plots.py`.
3. Are there any changes in the flow field beyond 1 second of flow time?
4. How do the residuals and the maximum velocity change for a longer simulation time?


## 2. Increase Mesh Resolution

In CFD, the solution should be independent of the mesh resolution. To verify this, a mesh dependency study is performed by running the same case on a finer mesh and comparing the results. As halving the cell size doubles the number of cells in each direction, the time step size must also be reduced accordingly to maintain a stable Courant number.

### Tasks

1. Create a copy of the `1_backward-step` case directory for a second simulation with a refined mesh.
2. Double the number of cells in each direction for the hex-blocks in `blockMeshDict` with the exception of the *z*-direction. Recreate the mesh with `blockMesh`.
3. Reduce the time step size `deltaT` in the `controlDict` from $$6.25 \times 10^{-4}\,\text{s}$$ to $$3.125 \times 10^{-4}\,\text{s}$$. Why is this reduction necessary to maintain a Courant number below 1?
4. Rerun the simulation and compare the results to the coarse mesh.
5. Do you notice any major changes in the flow behavior due to the increased mesh resolution?
6. How did the total computational time change between the coarse and the medium-sized mesh?


## 3. Higher Order Discretization

So far, both the temporal and spatial discretization have been first order accurate. While first order schemes are robust and stable, they introduce significant numerical diffusion that can smear out flow features. In this task, the discretization should be changed to second order to investigate the effect on the solution.

### Tasks

1. Create a copy of the previously created medium-sized mesh setup.
2. In `fvSchemes` in the `system` folder, change the temporal discretization from first order `Euler` to second order `backward`.
3. Change the discretization of the convective term in the momentum equation from first order `Gauss upwind` to second order `Gauss linear`.
4. Rerun the simulation and compare the results to the first order setup.
5. Do you notice any major changes in the flow behavior due to second order discretization?
6. How did the total computational time and the residuals change between first and second order discretization?