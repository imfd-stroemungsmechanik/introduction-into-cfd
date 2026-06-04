---
layout: default
title: Pre-Processing
parent: 4. Airfoil
nav_order: 1
---


# Pre-Processing

## OpenFOAM Case Structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `4_airfoil`. This folder contains the following subfolders and files:

```
4_airfoil
├── 0
│   ├── nut
│   ├── nuTilda
│   ├── p
│   └── U
├── constant
│   ├── momentumTransport
│   └── physicalProperties
├── system
│   ├── controlDict
│   ├── functions
│   ├── fvSchemes
│   └── fvSolution
├── airfoil_naca0012.msh
└── create_plots.py

3 directories, 12 files
```

The *relevant* files for this tutorial case are:
- `0` - This directory stores the initial values and boundary condition for each variables solved.
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `physicalProperties` has the physical properties of the fluid, e.g. viscosity.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `fvSolution` for the solver settings used in the Finite Volume Method.



## Mesh Import

The block-structured mesh for this case has been created using an external software and is stored in the ANSYS Fluent mesh format *.msh. It can be imported into OpenFOAM using the build-in tool `fluentMeshToFoam`:

```bash
fluentMeshToFoam airfoil_naca0012.msh
```

The resulting mesh should look like follows:

![Airfoil case geometry](figures/airfoil-mesh.png)

Since this is a two-dimensional mesh, the patches at the front and back must be of type `empty` in `constant/polyMesh/boundaries`. Therefore, open the `boundaries` file and correct the type of patch `frontAndBack` to `empty`. The other two patch types are correct and can be left as is:

```
3
(
    frontAndBack
    {
        type            empty;
        nFaces          114688;
        startFace       114208;
    }
    airfoil
    {
        type            wall;
        inGroups        List<word> 1(wall);
        nFaces          256;
        startFace       228896;
    }
    farfield
    {
        type            patch;
        nFaces          704;
        startFace       229152;
    }
)
```

{: .note }
> OpenFOAM always operates in a 3 dimensional Cartesian coordinate system and all geometries are generated in 3 dimensions. OpenFOAM solves the case in 3 dimensions by default but can be instructed to solve in 2 dimensions by specifying a special `empty` boundary condition on boundaries normal to the 3rd dimension for which no solution is required. Since the created mesh is two-dimensional, it will have a single cell layer in $$z$$-direction with the patch `frontAndBackPlanes` of type `empty`.




## Mesh Quality

Once the mesh has been created, it is always recommended to check the mesh statistics and quality. This can easily be done using the utility `checkMesh` from within the `airfoil` folder:

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
    points:           115648
    internal points:  0
    faces:            229856
    internal faces:   114208
    cells:            57344
    faces per cell:   6
    boundary patches: 3
    point zones:      0
    face zones:       0
    cell zones:       0

...

Checking patch topology for multiply connected surfaces...
    Patch               Faces    Points   Surface topology                  
    frontAndBack        114688   115648   ok (non-closed singly connected)  
    airfoil             256      512      ok (non-closed singly connected)  
    farfield            704      1408     ok (non-closed singly connected)  

Checking geometry...

    Overall domain bounding box (-484.457 -507.806 0) (501 507.806 1)
    Mesh has 2 geometric (non-empty/wedge) directions (1 1 0)
    Mesh has 2 solution (non-empty) directions (1 1 0)
    All edges aligned with or perpendicular to non-empty directions.
 ***High aspect ratio cells found, Max aspect ratio: 2.98998e+07, number of cells 7320
    Minimum face area = 5.18207e-10. Maximum face area = 3181.85.  Face area magnitudes OK.
    Min volume = 5.18207e-10. Max volume = 3181.85.  Total volume = 875555.  Cell volumes OK.
    Mesh non-orthogonality Max: 52.3838 average: 5.03403
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 0.341413 OK.
    Coupled point location match (average 0) OK.

Failed 1 mesh checks.
```

This gives us all relevant mesh statistics and quality criteria of the mesh:

- The mesh consists of 57344 hexahedral cells,
- has three different boundary patches `farfiled`, `airfoil`, and `frontAndBack`, and
- has two solution directions, e.g., a two-dimensional mesh.

As this is a hexahedral, block-structured mesh, maximum non-orthogonality and skewness are good with 52.38 and 0.34, respectively. However, aspect ratio reaches extreme values with nearly $$30 \times 10^6$$. This comes from:
 1. Very high near-wall mesh resolution for resolving the turbulent boundary layer
 2. Maintained clustering of cells downstream of the trailing edge due to the C-grid topology of the block-structured mesh.

While this contradicts the recommended values of maximum aspect ratio of 1000, this is not an issue for this simulation. High aspect ratio cells are only problematic when they are stretched across the direction of large solution gradients. In boundary layer and wake flows, the solution gradients are overwhelmingly in the wall-normal direction (velocity changes from zero at the wall to the freestream value over a short distance). The gradients in the streamwise direction are comparatively small (the flow changes slowly along the airfoil surface and downstream in the wake).

So despite the fact that `checkMesh` fails due to aspect ratio, we can continue with this mesh.




## Physical Properties

The physical properties for the fluid, such as kinematic viscosity, are stored in the `physicalProperties` file in the `constant` directory. In this tutorial, air is considered as fluid, which as a kinematic viscosity of $$\nu = 8.58 \times 10^{-6}\,\text{m}^2/\text{s}$$. Thus, the `physicalProperties` dictionary needs to read:

```
viscosityModel  Newtonian;

nu              8.58e-6;
```



## Boundary Conditions

Initial and boundary conditions have to be provided for each variable to be solved. The case starts at time $$t=0$$, so the initial field data is stored in a `0` sub-directory. This folder contains 4 files, `p` and `U` for kinematic pressure and velocity, and `nuTilda` and `nut` for the modified turbulent viscosity and the turbulent viscosity itself, respectivly.

Each file has three primitive entries for a given variable: (1) Specification of the dimensions, (2) the internal field, and (3) the boundary field.

### Dimensions

Specifies the dimensions of the field. In general, algebraic operations must be performed on properties using consistent units of measurement; in particular, addition, subtraction and equality are only physically meaningful for properties of the same dimensional units. The dimension set in OpenFOAM consists of 7 scalars delimited by square backets, e.g. for kinematic pressure:

```
[0 2 -2 0 0 0 0]
```
where each of the values corresponds to the power of each of the base units of measurement listed in the following table:

| **No.**   | Property              | SI unit   |
| --------- | --------------------- | --------- |
| 1         | Mass                  | kilogram  |
| 2         | Length                | meter     |
| 3         | Time                  | second    |
| 4         | Temperature           | kelvin    |
| 5         | Quantity              | mole      |
| 6         | Current               | ampere    |
| 7         | Luminous intensity    | candela   |

So for the example of kinematic pressure, the unit is $$\text{Length}^2 \times \text{Time}^{-2}$$.

### Internal Field

The internal field stores all the cell center values for the complete mesh. At the beginning of a simulation, this often corresponds to a uniform field as initialization. As the simulation is running, the internal field will become a non-uniform field with individual field values for each cell.

### Boundary Field

The boundary field data consists of a list of all patch names, each with an associated patch type and the corresponding entries.



## Pressure and Velocity Boundaries

We want to investigate the flow around the airfoil at a Reynolds-number of $$\text{Re} = 6 \times 10^6$$. Therefore, we have to use a pressure-velocity boundary setup, where velocity is defined at the inflow while pressure is set at the outflow. Since there is only a single boundary patch for inflow and outflow, we have to use `inletOutlet` and `outletInlet` boundary conditions for velocity and pressure, respectively. These two patch types automatically switch between fixed value and zero gradient depending on whether the flow is leaving or entering the solution domain.

The velocity at the inlet will be determined using the Reynolds-number. With an airfoil length of $$L = 1\,\text{m}$$ and a kinematic viscosity of $$\nu = 8.58 \times 10^{-6}\,\text{m}^2/\text{s}$$, the characteristic inflow velocity is as follows:

$$ \text{Re} = \frac{U_\text{in} L}{\nu} \quad \rightarrow \quad U_\text{in} = \frac{\text{Re} \, \nu}{L} = 51.48\,\text{m/s} $$


### Velocity Field

The velocity field as a unit of $$\text{meter} \times \text{second}^{-1}$$ and is initialized based on the inlet velocity to $$(51.48 \, 0 \, 0)$$. For the farfield, an `inletOutlet` boundary type is used with an inlet velocity of $$(51.48 \, 0 \, 0)$$. This boundary condition automatically switches between a fixed value boundary condition, wherever the flow is entering the solution domain, and a zero gradient in patch-normal direction, wherever the flow is leaving the domain. The flow is considered viscous, which results in a `noSlip` condition for velocity at the airfoil, e.g. the velocity directly at the airfoil surface is zero. Front and back of the computational domain are `empty` indicating a two-dimensional setup.

The concrete file for velocity in the `0` directory looks as follows:

```
dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (51.48 0 0);

boundaryField
{
    farfield
    {
        type            inletOutlet;
        inletValue      uniform (51.48 0 0);
        value           uniform (51.48 0 0);
    }
    airfoil
    {
        type            noSlip;
    }
    frontAndBack
    {
        type            empty;
    }
}
```



### Pressure Field

The kinematic pressure field has a unit of $$\text{meter}^2 \times \text{second}^{-2}$$ with a uniform internal field of 0. For the farfield, an `outletInlet` boundary type is used with an outlet pressure of zero. This boundary condition automatically switches between a zero gradient boundary condition, wherever the flow is entering the solution domain, and a fixed value boundary condition, wherever the flow is leaving the domain. At wall patches, pressure is set to a zero gradient condition, and front and back of the computational domain are `empty` consistent with the velocity boundary.

{: .note }
> OpenFOAM often uses a relative kinematic pressure of zero as initial value and at the outlet boundary as the absolute value of pressure is not of relevance for incompressible simulations.

The concrete file for pressure in the `0` directory looks as follows:

```
dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    farfield
    {
        type            outletInlet;
        outletValue     uniform 0;
        value           uniform 0;
    }

    airfoil
    {
        type            zeroGradient;
    }

    frontAndBack
    {
        type            empty;
    }
}
```



## Simulation Control

Settings related to the control of time (for transient simulations) or iterations (for steady-state simulations) and reading and writing of the solution data are read in from the `controlDict` file in the `system` folder.


### Flow Solver

The file starts with the corresponding solver to be used:
```
solver          incompressibleFluid;
```
In this tutorial case, we are using the solver `incompressibleFluid`, a pressure-based solver for incompressible, steady-state or transient, laminar or turbulent single-phase flows.


### Start and End Times

OpenFOAM offers great flexibility with time/iteration control. In this tutorial the run starts at time 0, which means that OpenFOAM needs to read field data from a directory named 0. Therefore we set the `startFrom` keyword to `startTime` and then specify the `startTime` keyword to be 0. The simulation should run until a steady state solution is reached, up to a maximum of 1000 iterations. Therefore, the `stopAt` entry is set to `endTime` and the `endTime` entry to `1000`.

The corresponding lines in the `controlDict` look as follows:

```
startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         1000;
```



### Time Step Size

The time step size is defined via the keyword `deltaT`. Since we are performing a steady-state simulation, the time step size has no physical meaning and is simply set to `1`. This way it acts as a iteration counter. The corresponding settings in `controlDict` look as follows:

```
deltaT          1;
```

{: .note }
> Regardless of whether steady-state or transient simulations are performed, OpenFOAM always referes to `startTime`, `endTime` and `deltaT`. In transient simulations, these entries possess the physical meaning of time. However, in steady state simulations time is not considered. Therefore, these entries will simply correspond to the start and end of the simulation in terms of iterations.


### Writing out Results

As the simulation progresses, results are written out at certain intervals of iterations that can later be analysed and visualized. The `writeControl` keyword presents several options for setting the iteration interval at which the results are written. Here, the `timeStep` option is selected which specifies that results are written every 100-th iteration where the value is specified under the `writeInterval` keyword. For this case, the entries in the `controlDict` are shown below:

```
writeControl    timeStep;

writeInterval   100;
```


## Discretization

The user specifies the choice of finite volume discretisation schemes in the `fvSchemes` dictionary in the `system` directory. Here, we will only cover the most relevant settings.

### Temporal derivatives

The discretization of the temporal derivatives $$(\partial / \partial t)$$ is defined within the `ddtSchemes` keyword. Since this is a steady-state simulation, the entry here is set to `steadyState`, e.g. the temporal derivative is set to zero.

```
ddtSchemes
{
    default         steadyState;
}
```

### Gradient terms

The discretization of the gradient terms is defined within the `gradSchemes` keyword. All gradient schemes are discretized equally with a second order **central differencing scheme**. Hence, the `default` discretization is set to `Gauss linear`.

```
gradSchemes
{
    default         Gauss linear;
}
```

### Convective terms

The discretization of the convective terms, e.g., convective fluxes, is defined within the `divSchemes` keyword. Here, `div(phi,U)` referes to the discretization of the convective flux $$\partial(u_i u_j)/\partial x_j$$ with `phi` being the (volumetric) flux and `U` the variable transported by the flux. In this case, the **second order upwind scheme** is employed called `Gauss linearUpwindV` combined with a non-limited Gauss linear gradient scheme.

One additional entry is required for the discretization of the convective flux $$\partial(\tilde{\nu} u_j)/\partial x_j$$ for the modified turbulent viscosity $$\tilde{\nu}$$. Similar to the convective flux of momentum, a bounded second order upwind scheme is used.

```
divSchemes
{
    div(phi,U)      bounded Gauss linearUpwindV Gauss linear;
    
    div(phi,nuTilda) bounded Gauss linearUpwind grad(nuTilda);
}
```

{: .note }
> The keyword `bounded` in front of the discretization scheme for the convective terms is only required in steady-state simulations. It helps to maintain boundedness of the solution variable and promotes a better convergence.



## Linear Solver Settings

The specification of the linear equation solvers, tolerances and other algorithm controls is made in the `fvSolution` dictionary in the `system` directory. These settings are as follows for the airfoil tutorial case.

### Solver settings

The pressure equation is solved using the **Generalised Algebraic MultiGrid method** (GAMG), which accelerates convergence by coarsening the linear system onto progressively smaller grid levels, solving cheaply on the coarsest level, and mapping the correction back. At each grid level, **Gauss-Seidel** sweeps are applied as the smoother to eliminate local, high-frequency errors. The convergence criteria are the same as before: the solver stops when the residual reaches either the absolute tolerance of $$10^{-6}$$ or 10% of its initial value (`relTol`).

```
solvers
{
    p
    {
        solver          GAMG;
        smoother        GaussSeidel;
        tolerance       1e-06;
        relTol          0.1;
    }
... 
}
```

The momentum equation is solved iteratively using **Gauss-Seidel** sweeps (`smoothSolver` defines the solver strategy, `smoother` selects the specific algorithm applied at each sweep). The solver stops when either the residual drops below the absolute tolerance of $$10^{-6}$$, or when it falls to 10% of its initial value within the current time step (`relTol`), whichever is reached first:

```
solvers
{
...

    U
    {
        solver          smoothSolver;
        smoother        GaussSeidel;
        tolerance       1e-08;
        relTol          0.1;
    }
}
```


### Pressure-velocity coupling

The `SIMPLE` block configures the outer pressure-velocity coupling loop for this steady-state case. Setting `consistent` to `yes` activates the SIMPLEC variant, which uses a more complete pressure correction and allows for less aggressive under-relaxation. This is why `p` can be set to 1.0 (no relaxation) under `relaxationFactors`. The `residualControl` entries define when the SIMPLE loop considers the solution converged: iterations continue until the residuals of all listed fields drop below $$5 \times 10^{-5}$$.

```
SIMPLE
{
    residualControl
    {
        p               1e-4;
        U               1e-5;
    }
}
```

### Relaxation factors

The `relaxationFactors` block stabilises the iterative process by blending each new solution with the previous one. The distinction between fields and equations is where the blending is applied: fields modifies the solution field directly after solving (here, pressure is unrelaxed at 1.0, enabled by SIMPLEC), while equations modifies the linear system itself before solving, which is numerically more stable for transport equations like momentum and the Spalart-Allmaras turbulence variable (both damped to 0.9, meaning each update retains 10% of the old solution).

```
relaxationFactors
{
    fields
    {
        p               1.0;
    }
    equations
    {
        U               0.9;
        nuTilda         0.9;
    }
}
```