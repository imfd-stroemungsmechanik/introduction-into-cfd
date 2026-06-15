---
layout: default
title: 5. Diffuser
nav_order: 6
---

# Buice-Eaton 2D Diffuser

## Objectives

The objectives for this tutorial are as follows:

- Import the two-dimensional mesh of the Buice-Eaton 2D diffuser into OpenFOAM and check its quality,
- Set boundary conditions and material properties based on Reynolds-number,
- Run a steady-state, incompressible simulation with the solver `incompressibleFluid` using the standard $$k-\epsilon$$ turbulence model,
- Visualize the velocity field in ParaView,
- Plot the velocity profile in the separation region and compare it with experimental data,
- Analyze friction coefficient and dimensionless wall distance, and
- Repeat the simulation with the SST $$k-\omega$$ turbulence model.

## Overview

This tutorial will describe how to pre-process, run, and post-process a case of a steady-state, isothermal, incompressible flow through the Buice-Eaton 2D diffuser. The geometry consists of an inlet on the left and an outlet on the right, which are both extended to reduce the influence of the boundary conditions on the solution, and top and bottom no-slip walls (see the following figure). The flow will be solved using the OpenFOAM solver `incompressibleFluid`, suitable for laminar and turbulent, isothermal, incompressible flows.

![Diffuser case geometry](figures/diffuser-geometry.png)

The problem is characterized by the inlet Reynolds-number of $$\text{Re} = 2 \times 10^4$$, which renders the flow turbulent. Based on the channel height of $$H = 1\,\text{m}$$ and Reynolds-number, kinematic viscosity and inlet flow velocity have to be chosen accordingly.

The case is used for validating the ability of turbulence models to predict separation and simulate flows under adverse pressure gradients correctly. It was published by Buice and Eaton in 2000:

> Buice, C. U. and Eaton, J. K., 
> "Experimental Investigation of Flow Through an Asymmetric Plane Diffuser", 
> Journal of Fluids Engineering, Vol. 122, No. 2, June 2000, pp. 433-435.

Furthermore, a numerical study from NASA can be found [here](https://www.grc.nasa.gov/www/wind/valid/buice/buice01/buice01.html).

## Preparation

Before starting, perform the following steps for preparation:

 1. Download the archive file [5_diffuser.zip]() containing the case folders.
 2. Extract the archive and move its content to the `OpenFOAM_Projects` folder, which has been created in the first tutorial. 
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM using the `of13` alias.