---
layout: default
title: Exercise
parent: 5. Diffuser
nav_order: 4
---

# Exercise

## Introduction

The simulation setup of the turbulent, incompressible flow through a diffuser did not yield good results compared with experimental measurements. The main reason is the choice of the turbulence model, namely the Standard $$k-\epsilon$$, which is not able to model flows under adverse pressure gradients and with separation.

In this exercise, an additional simulation with a more suitable turbulence model will be performed. Furthermore, the skin friction coefficient will be evaluated and compared with experimental data to further quantify the results.


## 1. Simulation with SST $$k-\omega$$ Turbulence Model

Repeat the simulations with the SST $$k-\omega$$ turbulence model instead of the Standard $$k-\epsilon$$ model. This involves changing the turbulence model, applying suitable boundary conditions for the new variable specific dissipation rate $$\omega$$ and adjusting the solver and discretization schemes.

### Tasks

1. Create a copy of the `diffuser` case directory for a second simulation called `diffuser_kOmegaSST`.
2. Within the `diffuser_kOmegaSST` case folder, remove all results folders (except `0`) and the `postProcessing` folder for a clean setup.
3. Change the turbulence model from `kEpsilon` to `kOmegaSST` in the `momentumTransport` file in the `constant` dictionary.
4. In the `0` folder, rename the `epsilon` file to `omega` for the new variable solved and apply the following changes to the file itself:
    - Set the name of the object entry in the `FoamFile` header to `omega`.
    - Change the dimensions of the variable to $$\text{seconds}^{-1}$$.
    - The inlet boundary condition must be of type `turbulentMixingLengthFrequencyInlet`.
    - Replace the `epsilonWallFunction` at the wall patches with `omegaWallFunction`.
5. In `functions`, `fvSchemes`, and `fvSolution` in the `system` directory, replace all instances of `epsilon` with `omega` to use the same discretization schemes, solver settings, and relaxation factors for the $$\omega$$ transport equation as for the $$\epsilon$$ transport equation in the previous simulations.
6. Add the following entry in the `fvSchemes` file, which specifies how the SST $$k-\omega$$ turbulence model computes the distance from a cell to the nearest wall:
```
wallDist
{
    method              meshWave;
}
```
7. Rerun the simulation with the solver `foamRun`.
8. Analyse the simulation results with ParaView similar to the first simulation.


#### Questions

1. Are there any improvements in the prediction of the flow separation at the lower diffuser wall?
2. Plot the velocity profile of both simulations and the experimental measurements in a single graph in ParaView. Which model is best suited for modelling this complex flow?



## 2. Skin Friction Coefficient

The `wallShearStress` function object computed the wall shear stress field during the simulation. Using this field, the skin friction coefficient $$C_f$$ can be evaluated along the upper wall and compared against the experimental measurements provided in `friction_coefficient.csv` in the `experimental_data` directory.

The skin friction coefficient is defined as

$$
C_f = \frac{-\tau_{w,x}}{0.5 U_\text{in}^2}
$$

where $$\tau_{w,x}$$ is the $$x$$-component of the wall shear stress and $$U_\text{in} = 0.3\,\text{m/s}$$ the inlet reference velocity. Since `incompressibleFluid` works with kinematic variables, the `wallShearStress` field is already divided by density (units $$\text{m}^2\text{/s}^2$$). Note the leading minus sign: OpenFOAM reports wall shear stress as the traction acting on the fluid, which is negative for attached flow in the streamwise direction.

### Tasks

1. In ParaView, restrict the view to the `upperWall` patch and make sure the `wallShearStress` field is loaded.
2. Use the **Calculator** filter to compute $$C_f$$ from the `wallShearStress` field using the equation above.
3. Plot the resulting skin friction coefficient along the streamwise direction using the **Plot Data** filter.
4. Load the experimental reference data from `friction_coefficient.csv` and overlay it in the same diagram.
5. How well does the simulated skin friction coefficient agree with the experimental measurements?