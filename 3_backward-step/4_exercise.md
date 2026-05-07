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


## Tasks

### 1. Increase End Time

Change the `endTime` in the `controlDict` in the `system` directory from 1 to 2 seconds and rerun the simulation.

#### Questions

1. Are there any changes in the flow field beyond 1 second flow time?
2. How do the residuals and the maximum velocity change for a longer simulation time?


### 2. Increase Mesh Resolution

Create a copy of the `1_backward-step` case directory for a second simulation with a refined mesh. Increase the number of cells in each direction for the hex-blocks in `blockMeshDict` with the exception of the *z*-direction. Make sure that the time step size `deltaT` in the `controlDict` is also reduced accordingly from $$6.25 \, \times 10^{-4}\,\text{s}$$ to $$3.125 \, \times 10^{-4}\,\text{s}$$ to maintain a Courant number of below 1. Regenerate the mesh with `blockMesh` and rerun the simulation.

#### Questions

1. Do you notice any major changes in the flow behavior due to the increased mesh resolution?
2. How did the total computational time change between the coarse and the medium-sized mesh?


### 3. Higher Order Discretization

Create a copy of the previously created medium-sized mesh setup. In `fvSchemes` in the `system` folder, change the temporal discretization from first order `Euler` to second order `backward` and the discretization of the convective term in the momentum equation from first order `Gauss upwind` to second order `Gauss linear`. Rerun the simulation.

#### Questions

1. Do you notice any major changes in the flow behavior due to second order discretization?
2. How did the total computational time and the residuals change between first and second order discretization?