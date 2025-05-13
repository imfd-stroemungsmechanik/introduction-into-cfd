---
layout: default
title: Exercise
parent: 3. Discretization
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the incompressible flow over a backward facing step had unresolved issues, namely:
 - the end time of 1 second might be too short
 - the spatial and temporal accuracy was only of first order,
 - the influence of the mesh resolution is not investigated.

In order to resolve these issues, additional simulations should be performed.

## Tasks

### 1. Increase End Time

Change the `endTime` in the `controlDict` in the `system` directory from 1 to 2 seconds and rerun the simulations.

**Questions**
1. Are there any changes in the flow field beyond 1 second flow time?
2. How do the residuals change for a longer simulation time?

### 2. Increase Mesh Resolution

Create a copy of the  `backward-step` case directory for a second simulation with a refined mesh. Reduce the maximum cell size from $$1.25 \times 10^{-3} \, \text{m}$$ to $$6.125 \times 10^{-4}\,\text{m}$$ in the `meshDict` in the `system` directory. Make sure that the time step size in the `controlDict` is also reduced accordingly to maintain a Courant number of below 1 and set the `endTime` to 1 second.

#### Questions

1. Do you notice any major changes in the flow behavior?
2. How did the total computational time change between the coarse and the finer mesh?