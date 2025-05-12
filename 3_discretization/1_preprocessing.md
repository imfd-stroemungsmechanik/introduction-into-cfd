---
layout: default
title: Pre-Processing
parent: 3. Discretization
nav_order: 1
---


# Pre-Processing

## OpenFOAM Case Structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `1_backward-step`. This folder contains the following subfolders and files:

```
backward-step
├── 0
│   ├── p
│   └── U
├── constant
│   └── turbulenceProperties
│   └── transportProperties
└── system
│   ├── controlDict
│   ├── fvSchemes
│   └── fvSolution
└── backward-step.msh     
3 directories, 8 files
```

The *relevant* files for this tutorial case are:
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `transportProperties` has the thermophysical properties of the fluid, e.g. viscosity.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `fvSchemes` holds the discretisation schemes used in the solution selected during runtime.


## Mesh Generation

The mesh for this case has been created using an external software and is stored in the ANSYS Fluent mesh format `*.msh`. Similar to the previous seminar, the mesh can be imported using the OpenFOAM tool `fluentMeshToFoam` with the following command:

```bash
fluentMeshToFoam backward-step.msh
```

The utlitity sucessfully imports the mesh and confirms this with the output:

```
...
Writing mesh... to "constant/polyMesh"  done.
 
End
```

The mesh has been successfully imported into the OpenFOAM format and stored within the `constant/polyMesh` folder.


## Mesh Quality

Once the mesh has been imported, it is always recommended to check the mesh statistics and quality. This can easily be done using the utility `checkMesh` from within the `backward-step` folder:

```
checkMesh
```

The most relevant output is as follows:

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
Create time

Create polyMesh for time = 0

Time = 0s

Mesh stats
    points:           18162
    internal points:  0
    faces:            35480
    internal faces:   17320
    cells:            8800
    faces per cell:   6
    boundary patches: 4
    point zones:      0
    face zones:       0
    cell zones:       0

...

Checking geometry...
    Overall domain bounding box (-0.05 -0.025 -0.001) (0.25 0.025 0.001)
    Mesh has 2 geometric (non-empty/wedge) directions (1 1 0)
    Mesh has 2 solution (non-empty) directions (1 1 0)
    All edges aligned with or perpendicular to non-empty directions.
    Boundary openness (-1.75855e-19 -1.41856e-17 1.87578e-18) OK.
    Max cell openness = 1.35525e-16 OK.
    Max aspect ratio = 1 OK.
    Minimum face area = 1.5625e-06. Maximum face area = 2.5e-06.  Face area magnitudes OK.
    Min volume = 3.125e-09. Max volume = 3.125e-09.  Total volume = 2.75e-05.  Cell volumes OK.
    Mesh non-orthogonality Max: 0 average: 0
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 2.19338e-13 OK.
    Coupled point location match (average 0) OK.


Mesh OK.
    
End
```

This gives us all relevant mesh statistics and quality criteria of the mesh:

- The mesh consists of 8800 cells,
- has 4 different boundary patches.

As this is a block-structured mesh with uniform cell size, the mesh quality is excellent with criteria such as:

- max cell aspect ratio of 1,
- a minimum and maximum cell volume of 3.125e-09,
- a maximum mesh non-orthogonality of 0, and
- a max cell skewness of 0.

The final output `Mesh OK.` indicates that no critical problems or errors were found during `checkMesh`. Therefore, we can continue with this mesh and proceed with the simulation.




## Physical Properties

The physical properties for the fluid, such as kinematic viscosity, are stored in the `transportProperties` file in the `constant` directory. In this tutorial, the Reynolds-number at the inlet should be 1250. Based on the inlet velocity of $$U_\text{in} = 1\,\text{m/s}$$ and the channel height at the inlet of $$H_\text{in} = 0.025\,\text{m}$$, the kinematic viscosity can be computed based on the equation for the Reynolds-number:

$$ \text{Re} = \frac{U_\text{in} \, H_\text{in}}{\nu} \quad \rightarrow \quad \nu = \frac{U_\text{in} \, H_\text{in}}{\text{Re}} = 2.5 \times 10^{-5}\,\text{m}^2\text{/s} $$

This value has to be specified in SI-units in the `transportProperties` dictionary as follows:

```
16
17  viscosityModel  Newtonian;
18
19  nu              2.5e-5;
20
21  // ************************************************************************* //
```
