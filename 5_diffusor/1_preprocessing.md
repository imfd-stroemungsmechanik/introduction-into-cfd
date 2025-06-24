---
layout: default
title: Pre-Processing
parent: 5. Diffusor
nav_order: 1
---


# Pre-Processing

## OpenFOAM Case Structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `diffusor`. This folder contains the following subfolders and files:

```
├── 0
│   ├── epsilon
│   ├── k
│   ├── nut
│   ├── p
│   └── U
├── constant
│   ├── turbulenceProperties
│   └── transportProperties
├── system
│   ├── controlDict
│   ├── fvSchemes
│   ├── fvSolution
│   └── meshDict
└── diffusor.stl

3 directories, 11 files
```

The *relevant* files for this tutorial case are:
- `0` - This directory stores the initial values and boundary condition for each variables solved.
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `turbulenceProperties` defines, which turbulence model to use for the simulation
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `fvSchemes` for the discretization schemes used in the Finite Volume Method.
    - `fvSolution` for the solver settings used in the Finite Volume Method.
    - `meshDict` contains the configuration for the automated meshing process.



## Mesh Generation

The hexahedral-dominant, two-dimensional mesh is created automatically with the meshing utility `cartesian2DMesh` from a user provided surface geometry named `diffusor.stl, which is located in the case folder.

The diffusor has an initial channel height of $$H = 1\,\text{m}$$ at the inlet and extends to $$4.7\,\text{m}$$ towards the outlet. In order to achieve 10 cells across the channel height (exluding inflation layers), the maximum cell size is set to $$0.1\,\text{m}$$. Additionally, the walls for the first mesh have a single inflation layer with a thickness ratio of 1.2. This way standard wall functions can be used by ensuring a dimensionless wall distance is $$y^+ > 30$$.

The resulting `meshDict` looks as follows:

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFile     "diffuser.stl";

maxCellSize     0.1;

objectRefinements
{}

boundaryLayers
{
    patchBoundaryLayers
    {
        "(lowerWall|upperWall)"
        {
            nLayers             1;

            thicknessRatio      1.2;
        }
    }
}
```

Finally, all corresponding patches are grouped together correctly using a suitable patch type. In order to create the mesh, the `cartesian2DMesh` utility has to be executed:

```bash
cartesian2DMesh
```

The resulting mesh should look like follows:

![Diffusor coarse mesh](figures/diffusor-mesh_coarse.png)


At this point the mesh generation is complete. It consists of:
 - Background mesh with a cell size of $$0.1 \text{m}$$
 - A single inflation layer at the walls with a thickness ratio of 1.2.
 - Correct patch types for inlet, outlet, lower and upper walls and front and back planes.

{: .note }
> OpenFOAM always operates in a 3 dimensional Cartesian coordinate system and all geometries are generated in 3 dimensions. OpenFOAM solves the case in 3 dimensions by default but can be instructed to solve in 2 dimensions by specifying a special `empty` boundary condition on boundaries normal to the 3rd dimension for which no solution is required. Since the created mesh is two-dimensional, it will have a single cell layer in $$z$$-direction with the patch `frontAndBackPlanes` of type `empty`.




## Mesh Quality

Once the mesh has been created, it is always recommended to check the mesh statistics and quality. This can easily be done using the utility `checkMesh` from within the `diffusor` folder:

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
    points:           59346
    internal points:  0
    faces:            115814
    internal faces:   56470
    cells:            28714
    faces per cell:   6
    boundary patches: 5
    point zones:      0
    face zones:       0
    cell zones:       0

...

Checking geometry...
    Overall domain bounding box (-30 0 -0.651697) (61 4.7 0.651697)
    Mesh has 2 geometric (non-empty/wedge) directions (1 1 0)
    Mesh has 2 solution (non-empty) directions (1 1 0)
    All edges aligned with or perpendicular to non-empty directions.
    Boundary openness (-2.77203e-18 -1.50709e-16 9.20305e-15) OK.
    Max cell openness = 2.61181e-16 OK.
    Max aspect ratio = 1.58715 OK.
    Minimum face area = 0.00397046. Maximum face area = 0.155254.  Face area magnitudes OK.
    Min volume = 0.00517507. Max volume = 0.0143652.  Total volume = 362.148.  Cell volumes OK.
    Mesh non-orthogonality Max: 14.4587 average: 0.802326
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 0.426205 OK.
    Coupled point location match (average 0) OK.

Mesh OK.
    
End
```

This gives us all relevant mesh statistics and quality criteria of the mesh:

- The mesh consists of 28714 cells,
- has 5 different boundary patches.

As this is a hexa-dominant, unstructured mesh with a single layer of inflation cells on the wall surfaces, the mesh quality in general is very good:

- max cell aspect ratio of 1.59,
- a maximum mesh non-orthogonality of 14.5, and
- a max cell skewness of 0.43.

The final output `Mesh OK.` indicates that no critical problems or errors were found during `checkMesh`. Therefore, we can continue with this mesh and proceed with the simulation.


## Physical Properties

The physical properties for the fluid, such as kinematic viscosity, are stored in the `transportProperties` file in the `constant` directory.

Since the fluid is considered air, the kinematic viscosity is $$15 \times 10^{-6}\,\text{m}^2\text{/s} and set accordingly in the `transportProperties` dictionary as follows:

```
viscosityModel  Newtonian;

nu              2e-5;
```





## Turbulence Modelling

The turbulence model is set in the `turbulenceProperties` file in the `constant` directory. The content of the file is as follows:

```
simulationType RAS;

RAS
{
    RASModel        kEpsilon;

    turbulence      on;

    printCoeffs     on;
}
```

For this set of simulation the Reynolds-Averaged Navier-Stokes (RANS) equations should be solved. Therefore, the entry `simulationType` is set to `RAS`, which stands for **R**eynolds-**A**veraged **S**imulation. Now the actual turbulence model has to be specified in a `RAS` sub-dictionary with the keyword `RASModel` set to `kEpsilon`, which selects the standard $$k-\epsilon$$ turbulence model. The entries `turbulence` and `printCoeffs` then actually turn on turbulence modelling and print out all relevant coefficients of the chosen turbulence model, respectively.



## Boundary Conditions

Since the simulation starts at time $$t=0$$, the boundary and initial field data is stored in the `0` sub-directory. This must be done for all variables solved for, in particular pressure `p`, velocity `U`, and additionally the turbulent quantities turbulent kinetic energy `k`, turbulent dissipation rate `epsilon`, and turbulent viscosity `nut`.

