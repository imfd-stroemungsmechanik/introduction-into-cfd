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

In the tutorial, the airfoil was simulated at an angle of attack of $$\alpha = 0^\circ$$. For aerodynamic design, it is essential to understand how lift and drag change across a range of angles of attack. The angle of attack is introduced by changing the inflow direction rather than rotating the mesh. Since the NACA 0012 is a symmetric airfoil, only positive angles need to be investigated.

### Tasks

1. Create a copy of the `4_airfoil` case directory for each of the following angles of attack: $$\alpha = 2^\circ$$, $$4^\circ$$, $$6^\circ$$, $$8^\circ$$, and $$10^\circ$$.
2. For each case, update the inflow velocity in the U file in the 0 directory. The velocity components are decomposed based on the angle of attack as follows: $$U_x = U_\text{in} \cos{\alpha}$$, $$U_y = U_\text{in} \sin{\alpha}$$. This applies to `internalField`, `inletValue`, and `value` of the `farfield` patch.
3. Update the `dragDir` and `liftDir` entries in the `functions` file in the `system` directory. Drag is defined parallel to the freestream direction and lift perpendicular to it: $$\text{dragDir} = (\cos{\alpha}, \sin{\alpha}, 0)$$, $$\text{liftDir} = (-\sin{\alpha}, \cos{\alpha}, 0)$$.
4. Run each simulation with `foamRun` and verify convergence using `python3 create_plots.py`.
5. How do the residuals and the number of iterations to convergence change for higher angles of attack?
6. Visualize the flow field in ParaView for $$\alpha = 10^\circ$$. How does the velocity field differ from the $$\alpha = 0^\circ$$ case?

{: .note }
It is important that dragDir and liftDir are aligned with the freestream direction, not with the grid axes. Otherwise, the reported force coefficients will correspond to the $$x$$- and $$y$$-components of the total force rather than the actual drag and lift.

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

