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
2. Duplicate this folder and rename it to `kEpsilon_fine`. This way the results of the first simulation do not get overwritten.
3. Within the `kEpsilon_fine` case folder, remove all results folders (except `0`) and the `postProcessing` folder for a clean setup.
4. Increase the number of inflation layers in `meshDict` in the `system` directory by changing the entry `nLayers` from 1 to 12.
5. Generate the mesh using `cartesian2DMesh` and check the quality of the mesh using `checkMesh`.
6. Rerun the simulation with the solver `simpleFoam`.
7. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Are there any improvements in the prediction of the flow separation at the lower diffuser wall?
