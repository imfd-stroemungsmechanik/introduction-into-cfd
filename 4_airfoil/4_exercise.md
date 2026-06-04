---
layout: default
title: Exercise
parent: 4. Airfoil
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the incompressible flow over around an airfoil gave very good results. However, it is unclear how drag and lift change with increasing angle of attack. Therefore, additional simulations should be performed.


## 1. Angle of Attack Study

In the tutorial, the airfoil was simulated at an angle of attack of $$\alpha = 0^\circ$$. For aerodynamic design, it is essential to understand how lift and drag change across a range of angles of attack. Instead of modifying the inflow velocity and force coefficient directions, the angle of attack can be changed by simply rotating the mesh using `transformPoints`, which was introduced in the meshing tutorial. Since the inflow direction remains fixed, the rotated airfoil geometry naturally produces the desired angle of attack.

### Tasks

1. Create a copy of the `4_airfoil` case directory for each of the following angles of attack: $$\alpha = 2^\circ$$, $$4^\circ$$, $$6^\circ$$, $$8^\circ$$, and $$10^\circ$$.
2. Instead of changing the inflow direction, we can rotate the mesh instead. Since all boundary conditions and function object settings are defined relative to the fixed inflow direction, no other changes are required. For each case, rotate the mesh around the $$z$$-axis using `transformPoints`:
```bash
transformPoints "Rz=<angle>"
```
3. Open the rotated mesh in ParaView and verify that the airfoil is tilted at the correct angle of attack.
4. Run each simulation with `foamRun` and verify convergence using `python3 create_plots.py`.
5. How do the residuals and the number of iterations to convergence change for higher angles of attack?
6. Visualize the flow field in ParaView for $$\alpha = 10^\circ$$. How does the velocity field differ from the $$\alpha = 0^\circ$$ case?


## 2. Validation Against Experimental Data

CFD results must always be validated against experimental or analytical reference data. In this task, the drag and lift coefficients from all simulations are collected and compared against the experimental measurements provided in the `experimental_data` folder.

### Tasks

1. For each angle of attack (including $$\alpha = 0^\circ$$), extract the final drag and lift coefficient from the last line of the `postProcessing/forceCoeffs/0/coefficient.dat` file. The following command prints the last line of the file:
```bash
tail -1 postProcessing/forceCoeffs/0/coefficient.dat
```
2. Create a file called `results.csv` in the `4_airfoil` directory with the following format and enter the values from each simulation:
```python
"alpha","Cd","Cl"
0,0.00821,0.00012
2,...,...
4,...,...
```
3. Run `python3 create_plots.py` to generate a validation diagram that compares the simulation results against the experimental reference data.
4. How well do the computed lift and drag coefficients agree with the experimental data?

