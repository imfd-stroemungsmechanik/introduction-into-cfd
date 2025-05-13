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
1_backward-step
├── 0
│   ├── p
│   └── U
├── constant
│   └── turbulenceProperties
│   └── transportProperties
└── system
│   ├── controlDict
│   ├── fvSchemes
│   ├── fvSolution
│   └── meshDict
└── backward-step.stl     
3 directories, 8 files
```

The *relevant* files for this tutorial case are:
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `transportProperties` has the thermophysical properties of the fluid, e.g. viscosity.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `meshDict` contains the configuration for the automated meshing process.
- `backward-step.stl`: The geometry file forming the boundaries of the computational domain.


## Mesh Generation

The hexahedral-dominant, two-dimensional mesh is created automatically with the meshing utility `cartesian2DMesh` from a user provided surface geometry named `backward-step.stl` in the case folder.

Due to the simple geometry, the mesh has a uniform cell size of $$\Delta x = 1.25\,\text{m}$$ without any local refinement. Thus, the `meshDict` is as follows:

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFile     "backward-step.stl";

maxCellSize     1.25e-3;
```

In order to make sure all corresponding patches are grouped together correctly using a suitable patch type, the following lines are added in the `meshDict`:

```
renameBoundary
{
    newPatchNames
    {
        "inlet"
        {
            type    patch;
            newName inlet;
        }

        "outlet"
        {
            type    patch;
            newName outlet;
        }
        
        "wall.*"
        {
            type    wall;
            newName walls;
        }
        
        ".*Empty.*"
        {
            type    empty;
            newName frontAndBackPlanes;
        }
    }
}
```

Here, the `inlet` and `outlet` patches are of type `patch`, all `wall`-named surfaces of the surface geometry are grouped together in a patch named `walls` of type `wall`, and the front and back plane of the geometry is grouped together in a patch called `frontAndBackPlanes` of type `empty`.

In order to create the mesh, the `cartesian2DMesh` utility has to be executed:

```bash
cartesian2DMesh
```

At this point the mesh generation is complete. It consists of:
 - Background mesh with a cell size of $$1.25\,10^{-3}\,\text{m}$$.
 - Correct patch type for inlet, outlet, walls and front and back planes.


## Mesh Quality

Once the mesh has been created, it is always recommended to check the mesh statistics and quality. This can easily be done using the utility `checkMesh` from within the `backward-step` folder:

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
    points:           19180
    internal points:  0
    faces:            37501
    internal faces:   18323
    cells:            9304
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
    Boundary openness (7.18073e-19 1.63691e-17 -3.6231e-15) OK.
    Max cell openness = 1.96243e-16 OK.
    Max aspect ratio = 1.62464 OK.
    Minimum face area = 5.16938e-07. Maximum face area = 3.09863e-06.  Face area magnitudes OK.
    Min volume = 1.03388e-09. Max volume = 4.01961e-09.  Total volume = 2.75e-05.  Cell volumes OK.
    Mesh non-orthogonality Max: 14.2836 average: 0.557759
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 0.688247 OK.
    Coupled point location match (average 0) OK.



Mesh OK.
    
End
```

This gives us all relevant mesh statistics and quality criteria of the mesh:

- The mesh consists of 9304 cells,
- has 4 different boundary patches.

As this is a block-structured mesh with uniform cell size, the mesh quality is excellent with criteria such as:

- max cell aspect ratio of 1.625,
- a maximum mesh non-orthogonality of 14.28, and
- a max cell skewness of 0.69.

The final output `Mesh OK.` indicates that no critical problems or errors were found during `checkMesh`. Therefore, we can continue with this mesh and proceed with the simulation.




## Physical Properties

The physical properties for the fluid, such as kinematic viscosity, are stored in the `transportProperties` file in the `constant` directory.

In this tutorial, the Reynolds-number at the inlet should be 250. Based on the inlet velocity of $$U_\text{in} = 1\,\text{m/s}$$ and the channel height at the inlet of $$H_\text{in} = 0.025\,\text{m}$$, the kinematic viscosity can be computed using the Reynolds-number:
$$ \text{Re} = \frac{U_\text{in} \, H_\text{in}}{\nu} \quad \rightarrow \quad \nu = \frac{U_\text{in} \, H_\text{in}}{\text{Re}} = 1 \times 10^{-4}\,\text{m}^2\text{/s} $$
This value along side the rhological model of the fluid (here: Newtonian fluid) has to be specified in the `transportProperties` dictionary as follows:

```
viscosityModel  Newtonian;

nu              1e-4;

// ************************************************************************* //
```



## Simulation Control

Settings related to the control of time (for transient simulations) or iterations (for steady-state simulations) and reading and writing of the solution data are read in from the `controlDict` file in the system folder.


### Flow Solver

The file starts with the corresponding solver to be used:
```
application     pimpleFoam;
```
In this tutorial case, we are using the solver `pimpleFoam`, a pressure-based solver for incompressible, transient or steady-state, laminar or turbulent single-phase flows.


### Start and End Times


The start/stop times and the time step for the run must be set. OpenFOAM oﬀers great flexibility with time/iteration control. In this tutorial the run starts at time 0, which means that OpenFOAM needs to read field data from a directory named 0. Therefore we set the `startFrom` keyword to `startTime` and then specify the `startTime` keyword to be 0. The simulation should run until a time of 1 second and then stop. Therefore, the `stopAt` entry is set to `endTime` and the `endTime` entry itself is set to `1`.

The corresponding lines in the `controlDict` look as follows:

```
startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         1;
```

### Time Step Size

The time step size is defined via the keyword `deltaT`. To achieve temporal accuracy and numerical stability when running `pimpleFoam`, we aim for a Courant number of $$\text{Co} \approx 0.25$$. Based on the cell size $$\Delta x$$, flow velocity $$U$$, and time step size $$\Delta t$$, the Courant number is defined for a given cfell as:

$$ \text{Co} = \frac{U \delta t}{\delta x} $$

The flow velocity naturally varies across the domain and the Courant-number limitation must be kept in every cell. Therefore, we have to estimate the time step size based on known values. The cell size of this equidistant mesh is constant everywhere and can be estimated based on the channel height at the inlet $$H_\text{in}$$ and the corresponding cell count of $$n = 20$$ cells across the inlet as follows:

$$\Delta x = \frac{H_\text{in}}{n} = 1.25 \times 10^{-3}\,\text{m}$$

The characteristic velocity in the flow domain $$U$$ can be approximated to be equal to the inlet velocity $$U_\text{in}$$. Although the actual flow velocity will probably be higher locally further downstream the inlet, this gives a sufficiently good estimate for the time step size $$\Delta t$$.

Based on these assumptions and using the equation for the Courant number, the following expression for the allowable time step size can be derived:

$$ \Delta t = \frac{\text{Co} \, \Delta x}{U_\text{in}} = 3.125 \times 10^{-4}\,\text{s}$$

The corresponding lines in the `controlDict` look as follows:

```
deltaT          3.125e-04;
```


### Writing out Results

As the simulation progresses, results are written out at certain intervals of time that can later be analysed and visualized. The `writeControl` keyword presents several options for setting the iteration interval at which the results are written. Here, the `runTime` option is selected which specifies that results are written out at certain simulation time intervals. Here, the `writeInterval` keyword sets this interval to `0.05`, which means that every 0.05 seconds of simulation time a results folder will be written. When OpenFOAM writes out results, it creates a new directory *named as the current time* containing a individual file for each field written out.

The corresponding lines in the `controlDict` look as follows:
```
writeControl    runTime;

writeInterval   0.05;
```


## Discretization

The discretization schemes used are specified in the `fvSchemes` file in the `system` directory. The file consists of different keywords for the corresponding terms in the governing equations.

### Temporal Derivatives

The discretization of the temporal derivatives is defined within the `ddtSchemes` keyword. In this case, all derivatives are discretized using the first order **Euler Implicit** scheme. Therefore, the `default` discretization is set to `Euler`.

```
ddtSchemes
{
    default         Euler;
}
```

### Gradient Terms

The discretization of the gradient terms is defined within the `gradSchemes` keyword. All gradient schemes are discretized equally with a second order **central differencing scheme**. Hence, the `default` discretization is set to `Gauss linear`.

```
gradSchemes
{
    default         Gauss linear;
}
```

### Convective Terms

The discretization of the convective terms, e.g., convective fluxes, is defined within the `divSchemes` keyword. Here, `div(phi,U)` referes to the discretization of the convective flux $$\partial(u_i u_j)/\partial x_j$$ with `phi` being the (volumetric) flux and `U` the variable transported by the flux. In this case, the **first order upwind scheme** is employed called `Gauss upwind`.

Additionaly, `div((nuEff*dev2(T(grad(U)))))` denotes the divergence of the shear stress tensor in the momentum equation. Since this term is diffusive in nature, it is recommended to discretize it with a central differencing scheme, here `Gauss linear`.

```
divSchemes
{
    div(phi,U)          Gauss upwind;

    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
```

### Laplacian Terms

The Laplacian terms, e.g., second order spatial derivatives $$\partial^2/\partial x_j^2$$, are discretized using a **central differencing scheme** corrected for non-orthogonal meshes called `Gauss linear corrected`.

```
laplacianSchemes
{
    default         Gauss linear corrected;
}
```

### Interpolation Discretization

The interpolation of variables from cell centers to face centers is specified with the keyword `interpolationSchemes`. Here, all interpolation is done using a second order **central differencing scheme** called `linear`.

```
laplacianSchemes
{
    default         linear;
}
```

