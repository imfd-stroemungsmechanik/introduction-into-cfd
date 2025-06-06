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
airfoil
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
- `geometries` - This directory contains all geometry files required for the tutorial.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `fvSolution` for the solver settings used in the Finite Volume Method.
    - `meshDict` contains the configuration for the automated meshing process.



## Mesh Generation

The hexahedral-dominant, two-dimensional mesh is created automatically with the meshing utility `cartesian2DMesh` from a surface geometry file inside the `geometries` directory. Different geometries are provided for varying angle of attack of the airfoil.

The airfoil has an overall length of $$1\,\text{m}$$. Therefore, the mesh has a maximum cell size of $$0.25\,\text{m}$$ and is refined towards the airfoil with a total of 5 circular, refinement regions around the airfoil. This adds 5 additional refinment levels resulting in a smallest cell size of about $$8\,\text{mm}$$.

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFile     "geometries/airfoil_0deg.stl";

maxCellSize     0.25;

objectRefinements
{
    refinement_5
    {
        type        cone;
        p0          (0 0 -1);
        p1          (0 0 1);
        radius0     1;
        radius1     1;
        additionalRefinementLevels    5;
    }
    refinement_4
    {
        type        cone;
        p0          (0 0 -1);
        p1          (0 0 1);
        radius0     2;
        radius1     2;
        additionalRefinementLevels    4;
    }
    refinement_3
    {
        type        cone;
        p0          (0 0 -1);
        p1          (0 0 1);
        radius0     3;
        radius1     3;
        additionalRefinementLevels    3;
    }
    refinement_2
    {
        type        cone;
        p0          (0 0 -1);
        p1          (0 0 1);
        radius0     4;
        radius1     4;
        additionalRefinementLevels    2;
    }
    refinement_1
    {
        type        cone;
        p0          (0 0 -1);
        p1          (0 0 1);
        radius0     5;
        radius1     5;
        additionalRefinementLevels    1;
    }
}
```

Additionally, the airfoil has a total of 18 inflation layers with a thickness ratio of 1.2. 

```
boundaryLayers
{
    patchBoundaryLayers
    {
        "(airfoil|trailing_edge)"
        {
            nLayers             18;

            thicknessRatio      1.2;
        }
    }
}
```

Finally, all corresponding patches are grouped together correctly using a suitable patch type. In order to create the mesh, the `cartesian2DMesh` utility has to be executed:

```bash
cartesian2DMesh
```

At this point the mesh generation is complete. It consists of:
 - Background mesh with a cell size of $$0.25 \text{m}$$
 - A circular refinement around the airfoil with a smallest cell size of about $$8\,\text{mm}$$.
 - Correct patch types for inlet, outlet, walls and front and back planes.

{: .note }
> OpenFOAM always operates in a 3 dimensional Cartesian coordinate system and all geometries are generated in 3 dimensions. OpenFOAM solves the case in 3 dimensions by default but can be instructed to solve in 2 dimensions by specifying a special `empty` boundary condition on boundaries normal to the 3rd dimension for which no solution is required. Since the created mesh is two-dimensional, it will have a single cell layer in $$z$$-direction with the patch `frontAndBackPlanes` of type `empty`.