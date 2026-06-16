---
layout: default
title: Solving
parent: 5. Diffuser
nav_order: 2
---

# Solving


## Starting the Solver


In order to start the simulation, we have to execute the corresponding OpenFOAM application. As defined in the `controlDict`, the solver `incompressibleFluid` will be used, suitable for steady-state and transient, incompressible, laminar or turbulent flows. To start the solution process, execute the application `foamRun` in the terminal from within the case directory:

```bash
foamRun
```

The progress of the job is written to the terminal window. It tells the user the current iteration, the equations being solved, initial and final residuals for all fields and should look like follows:

```
Time = 626s

DILUPBiCG:  Solving for Ux, Initial residual = 7.84788e-07, Final residual = 1.91123e-07, No Iterations 1
DILUPBiCG:  Solving for Uy, Initial residual = 1.03153e-05, Final residual = 1.16383e-08, No Iterations 3
GAMG:  Solving for p, Initial residual = 5.40664e-06, Final residual = 6.56563e-07, No Iterations 1
time step continuity errors : sum local = 1.52435e-08, global = -3.94684e-10, cumulative = -3.20101e-05
DILUPBiCG:  Solving for epsilon, Initial residual = 4.89335e-07, Final residual = 1.39649e-08, No Iterations 1
DILUPBiCG:  Solving for k, Initial residual = 2.61077e-06, Final residual = 3.35381e-07, No Iterations 1
ExecutionTime = 27.8877 s  ClockTime = 29 s
```

This output at iteration 626 tells us in summary:
- The `DILUPBiCG` solver (short for bi-Conjugate Gradient solver with a simplified Diagonal-based Incomplete LU preconditioner) is used to solve the velocity components `Ux` and `Uy` in $$x$$- and $$y$$-direction. In this iteration, it takes 1 and 3 iterations to reach the specified residual criteria.
- The `GAMG` multigrid solver is used for solving the pressure correction equation in the pressure-velocity coupling algorithm.
- The error of the conservation of mass is denoted as `continuity error`. Since its value is very small, conservation of mass is maintained.
- The `DILUPBiCG` solver is also used to solve the turbulence model transport equations for turbulent kinetic energy and dissipation rate.
- The execution time for the simulation up until this iteration is roughly 28 seconds as indicated by the `ExecutionTime`.

After 630 iterations, the simulation automatically stops as the residuals fall below the specified residual criteria in `fvSolution`.


## Monitoring the Simulation

Three function objects are defined in the `functions` file in the `system` folder to monitor the run:

```
#includeFunc residuals
(
    name    = residuals,
    fields  = (p U k epsilon)
)

#includeFunc yPlus

#includeFunc wallShearStress
```

The `residuals` object writes the initial residuals of `(p U k epsilon)`, so pressure, velocity, turbulent kinetic energy and dissipation rate, to `postProcessing/residuals/0/residuals.dat` at every iteration.

The `yPlus` object evaluates the dimensionless wall distance $$y^+$$ to assess how well the mesh resolves the turbulent boundary layer. It writes the minimum, maximum and average $$y^+$$ over all wall patches to `postProcessing` and adds a `yPlus` field to each results folder for visualization. Since `writeControl` is set to `writeTime`, this is done every time a result is written (here every 250 iterations, as set in `controlDict`).

The `wallShearStress` object works the same way, writing per-wall min/max values and a `wallShearStress` field to each results folder, which will be used later for the comparison with experimental data.

In order to quickly evaluate the residuals, a script is added to the diffuser case directory called `create_plots.py`. Executing it will automatically create the diagram and store them as png file:

```bash
python3 create_plots.py
```

This creates the following diagram of the residuals on the $$y$$-axis plotted against the iteration on the $$x$$-axis in the case folder:

![Diffuser case residuals](figures/diffuser-results-residuals.png)

The plot shows that the residuals fall throughout the simulation to below $$10^{-5}$$ for all monitored variables. Since this is the specified residual criteria, the simulation stops automatically. We can assume this is a converged steady-state simulation.
