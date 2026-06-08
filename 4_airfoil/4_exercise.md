---
layout: default
title: Exercise
parent: 4. Airfoil
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the incompressible flow around an airfoil gave very good results. However, it is unclear how drag and lift change with increasing angle of attack. Therefore, additional simulations should be performed.


## 1. Angle of Attack Study

In the tutorial, the airfoil was simulated at an angle of attack of $$\alpha = 0^\circ$$. For aerodynamic design, it is essential to understand how lift and drag change across a range of angles of attack. The angle of attack is introduced by rotating the mesh around the $$z$$-axis. Since the NACA 0012 is a symmetric airfoil, only positive angles need to be investigated.

### Tasks

1. Create a copy of the `4_airfoil` case directory for each of the following angles of attack: $$\alpha = 4^\circ$$, $$8^\circ$$, $$12^\circ$$, $$14^\circ$$, and $$16^\circ$$.
2. For each case, rotate the mesh using the `transformPoints` command as follows:

    ```bash
    transformPoints "Rz=<alpha>"
    ```

    This command rotates the mesh by `<alpha>` degrees around the z-axis.

3. Run each simulation with `foamRun` and verify convergence using `python3 create_plots.py`.
4. How do the residuals and the number of iterations to convergence change for higher angles of attack?
5. Visualize the flow field in ParaView for $$\alpha = 16^\circ$$. How does the velocity field differ from the $$\alpha = 0^\circ$$ case?


## 2. Validation Against Experimental Data

CFD results must always be validated against experimental or analytical reference data. In this task, the drag and lift coefficients from all simulations are collected and compared against the experimental measurements provided in the `experimental_data` folder.

### Tasks

1. For each angle of attack (including $$\alpha = 0^\circ$$), extract the final drag and lift coefficient from the last line of the `postProcessing/forceCoeffs/0/coefficient.dat` file. The following command prints the last line of the file:

    ```bash
    tail -1 postProcessing/forceCoeffs/0/coefficient.dat
    ```

2. Add the resulting data to the `results.csv` file in the original `4_airfoil` directory.
3. Run `python3 create_plots.py` to generate a validation diagram that compares the simulation results against the experimental reference data.
4. How well do the computed lift and drag coefficients agree with the experimental data?

