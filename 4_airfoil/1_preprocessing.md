---
layout: default
title: Pre-Processing
parent: 4. Airfoil
nav_order: 1
---


# Pre-Processing

## OpenFOAM Case Structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `airfoil`. This folder contains the following subfolders and files:

```
backward-step
├── 0
│   ├── p
│   └── U
├── constant
│   ├── turbulenceProperties
│   └── transportProperties
├── geometries
│   ├── airfoil_0deg.stl
│   ├── airfoil_2deg.stl
│   ├── airfoil_4deg.stl
│   ├── airfoil_6deg.stl
│   ├── airfoil_8deg.stl
│   └── airfoil_10deg.stl
└── system
    ├── controlDict
    ├── fvSchemes
    ├── fvSolution
    └── meshDict

4 directories, 12 files
```

The *relevant* files for this tutorial case are:
- `0` - This directory stores the initial values and boundary condition for each variables solved.
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `transportProperties` has the physical properties of the fluid, e.g. viscosity.
    - `turbulenceProperties` contains the setting for the turbulence mode.
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `transportProperties` has the physical properties of the fluid, e.g. viscosity.
    - `turbulenceProperties` contains the setting for the turbulence mode.
- `geometries` - This directory contains all geometry files required for the tutorial.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `fvSolution` for the solver settings used in the Finite Volume Method.
    - `meshDict` contains the configuration for the automated meshing process.

