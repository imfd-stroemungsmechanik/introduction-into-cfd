---
layout: default
title: Exercise
parent: 4. Airfoil
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the incompressible flow over around an airfoil gave very good results. However, it is unclear how drag and lift change with increasing angle of attack. Therefore, additional simulations should be performed.

In the `geometries` folder are several airfoil geometries for various angle of attacks. For example, the geometry file `airfoil_2deg.stl` represents a rectangular domain with a NACA 0012 airfoil at 2 degrees of angle of attack.


## Tasks

### 1. Simulate Various Angle of Attack

Copy the original `airfoil` folder and create new case folders for the angle of attack from 2 to 10 degrees in steps of 2 degrees. Repeat the simulations.

#### Questions

1. How does the flow field change with an increase in angle of attack?
2. Does this behaviour also influcence the convergence via residuals and force coefficients?
3. Which of our earlier assumptions about the flow no longer holds true at high angle of attack?



### 2. Speed up Simulation

Relaxation factors are required to keep steady-state simulations stable. The lower these factors, the more stable the simulation at the cost of longer computation time.

#### Questions

1. Try to increase the relaxation factors in order to speed up the simulation. What are the maximum values possible without crashing the simulation?