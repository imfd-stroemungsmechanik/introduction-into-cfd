---
layout: default
title: 4. Airfoil
nav_order: 5
---

# Airfoil

## Objectives

The objectives for this tutorial are as follows:

- Create a two-dimensional mesh in OpenFOAM with `cartesian2DMesh` and check its quality,
- Set boundary conditions based on Reynolds-number,
- Run a steady-state, incompressible simulation with `simpleFoam`,
- Check convergence and compute drag and lift coefficient,
- Repeat the simulation with varying angle of attack, and
- Visualize the velocity field in ParaView.

## Overview

This tutorial will describe how to pre-process, run, and post-process a case involving a steady-state, isothermal, incompressible flow over a NACA 0012 airfoil. The geometry is shown in the following figure with an inlet on the left, the airfoil in the center, slip walls at the top and bottom, and an outlet at the right. The flow will be solved using the OpenFOAM solver `simpleFoam` the suitable for laminar and turbulent, isothermal, incompressible, steady-state flows.

![Backward-facing step case geometry](figures/airfoil-geometry.png)



## Preparation

Before starting, perform the following steps for preparation:
 1. Download the archive `4_airfoil.zip` from the Downloads folder on the [OPAL course page](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/19816513539).
 2. Extract the archive.
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM.
