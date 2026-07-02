---
layout: default
title: Pre-Processing
parent: 6. Exhaust Gas Recirculation
nav_order: 1
---


# Pre-Processing

## OpenFOAM Case Structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `exhaust_gas_recirculation`. This folder contains the following subfolders and files:

```
├── 0
│   ├── alphat
│   ├── k
│   ├── nut
│   ├── omega
│   ├── p
│   ├── T
│   └── U
├── constant
│   ├── geometry
│       └── geometry.obj
│   ├── momentumTransport
│   └── physicalProperties
├── system
│   ├── blockMeshDict
│   ├── controlDict
│   ├── decomposeParDict
│   ├── functions
│   ├── fvSchemes
│   ├── fvSolution
│   ├── meshQualityDict
│   └── snappyHexMeshDict
└── create_plots.py

4 directories, 19 files
```

The *relevant* files for this tutorial case are:
- `0` - This directory stores the initial values and boundary condition for each variables solved.
- `constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:
    - `geometry` contains the geometry needed for the automated mesh generation
    - `momentumTransport` defines, which turbulence model to use for the simulation.
    - `physicalProperties` defines the thermophysical properties of the fluid.
- `system` - This folder contains files related to how the simulation is to be solved:
    - `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
    - `decomposeParDict` for specifying the number of processors in a parallel run.
    - `functions` contains function objects for runtune post-processing.
    - `fvSchemes` for the discretization schemes used in the Finite Volume Method.
    - `fvSolution` for the solver settings used in the Finite Volume Method.
    - `meshQualityDict` sets the mesh quality criteria for the meshing process.
    - `snappyHexMeshDict` configures the automated meshing tool `snappyHexMesh`.



## Mesh Generation

The hexahedral-dominant, three-dimensional mesh is created automatically with the meshing utility `snappyHexMesh` from a user provided surface geometry named `surface.obj`, which is located in the `geometry` sub-folder under `constant`.

Generating a mesh with `snappyHexMesh` is a 4-step process:
 1. A background mesh created with `blockMeshDict` must be generated that fills the entire region of interest.
 2. SnappyHexMesh refines the background mesh towards user-specified surfaces or regions by splitting the hexahedral cells and removes cells which are not within the region of interest.
 3. Cell vertex points are moved onto the surface geometry to remove the castellated surface of the mesh.
 4. Inflation layers are added at appropriate surfaces.

The complete process for this case is visualized in the following figure:

![Exhaust gas recirculation snappyHexMesh workflow](figures/snappyHexMesh_workflow.png)

The overall cell size solely depends on the cell size of the background mesh and the number of refinement steps during generation of the castellated mesh.



### Background Mesh

At first, a background mesh must be generated using `blockMesh`. The `blockMeshDict` in the `system` folder creates a structured mesh, which completely spans the provided geometry of the exhaust gas recirculation domain with $$24 \times 12 \times 3$$ cells in $$x$$-, $$y$$-, and $$z$$-direction, respectively. This results in a uniform cell size of $$\Delta = 16.67\,\text{mm}$$. This background mesh can be generated as follows:

```bash
blockMesh
```



### Automated Hex-dominated Mesh

The automated mesh generation can be started using the following command

```bash
snappyHexMesh
```

The background mesh is refined towards the wall patches `pipe_air` and `pipe_exhaust` by spliting the cells of the background mesh 3 times resulting in a cell size of $$\Delta \approx 2.1\,\text{mm}$$. At the other patches, the background mesh is refined only once for a cell size of $$\Delta \approx 8.33\,\text{mm}$$. Finally, three layers of prism cells are added at the `pipe_air` and `pipe_exhaust` wall patches with a growth ratio of 1.2.

The resulting mesh looks as follows:

![Exhaust gas recirculation coarse mesh](figures/exhaust-gas-recirculation-mesh.png)





## Mesh Quality

After mesh generation, the mesh statistics and quality are checked with `checkMesh`, run from within the case directory:

```
checkMesh
```

The relevant part of the output is:

```
Mesh stats
    points:           88119
    faces:            244816
    cells:            78617
    boundary patches: 5
...

Checking geometry...
    Overall domain bounding box (-20 -20 -20.0002) (360 160 20.0002)
    Max aspect ratio = 5.87141 OK.
    Mesh non-orthogonality Max: 63.1022 average: 8.46125
    Max skewness = 1.57355 OK.

Mesh OK.
```

The mesh has 78617 cells across 5 boundary patches, and all quality metrics are well within their limits: a maximum aspect ratio of 5.87, a maximum non-orthogonality of 63.10, and a maximum skewness of 1.57. The closing `Mesh OK`. confirms that no critical issues were found, so we can proceed to the simulation.





## Mesh Scaling

The overall bounding box of the computational mesh does not match the given dimensions of the geometry, since the latter was created in millimeters. Therefore, the mesh has to be scaled down in all three directions with a scaling factor of $$0.001$$. In order to do so, the mesh manipulation utility `transformPoints` can be used as follows:

```bash
transformPoints -scale "(0.001 0.001 0.001)"
```

{: .warning }
> If this command is executed twice, the mesh will be scaled by $$0.001 \times 0.001 = 10^{-6}$$!





## Physical Properties

Thermophysical models are concerned with:
- Thermodynamics, e.g. relating internal energy $$e$$ to temperature $$T$$
- Transport, e.g. the dependence of properties such as viscosity $$\mu$$ on temperature
- State, e.g. dependence of density on temperature $$T$$ and pressure $$p$$.

These thermophysical properties are stored in the `physicalProperties` file in the `constant` directory.

A thermophysical model required an entry named `thermoType` which specifies the package of thermophysical modelling that is used in the simulation. OpenFOAM includes a large set of pre-compiled combinations of modelling, built within the code using C++ templates.

The individual submodels chosen for this case are as follows:

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

thermoType
{
    type            hePsiThermo;
    mixture         pureMixture;
    transport       const;
    thermo          hConst;
    equationOfState perfectGas;
    specie          specie;
    energy          sensibleEnthalpy;
}
```

Depending on these submodels, specific fluid properties have to be specified. These settings are within the `mixture` dictionary in the `physicalProperties` file:

```
mixture
{
    specie
    {
        molWeight   28.9;
    }
    thermodynamics
    {
        Cp          1007;
        Hf          0;
    }
    transport
    {
        mu          1.8e-5;
        kappa       0.025;
    }
}
```

#### **Composition of each constituent**

There is currently only one option for the specie model which specifies the composition of each constituent. That model is itself named `specie`, which is specified by the entry `molWeight`, which specifies the grams per mole of the given species. Here, air is considered with a mol weight of $$28.9\,\text{g/mol}$$.

#### **Thermodynamics model**

The thermodynamic models are concerned with evaluating the specific heat $$c_p$$ from which other properties are derived. The thermodynamics model selected here is of type `hConst`, which assumes a constant $$c_p$$ and heat of fusion $$H_f$$, which is simply specified by two keywords, `cp` set to $$1007\,\text{J/(kg K)}$$ and `Hf` set to $$0$$.

#### **Equation of state**

The equation of state for the given fluid is set to perfect gas. Therefore, density is calculated based on the following relation without the need of any additional material parameter:

$$ \rho = \frac{p}{R\,T} $$

with the specific gas constant for air $$R$$.

#### **Transport model**

The transport modelling concerns evaluating dynamic viscosity $$\mu$$, thermal conductivity $$\kappa$$, and thermal diffusivity $$\alpha$$. In this case, a `const` transport model is specified, which assumes a constant dynamic viscosity $$\mu$$ and thermal conductivity $$\kappa$$. These two variables are specified by the keywords `kappa` set to $$1.8 \times 10^{-5}$$ and `kappa` to $$0.025$$.



## Turbulence Modelling

The turbulence model is set in the `momentumTransport` file in the `constant` directory. The content of the file is as follows:

```
simulationType RAS;

RAS
{
    RASModel        kOmegaSST;
}
```

For this set of simulation the Reynolds-Averaged Navier-Stokes (RANS) equations should be solved. Therefore, the entry `simulationType` is set to `RAS`, which stands for **R**eynolds-**A**veraged **S**imulation. Within the `RAS` sub-dictionary, the keyword `RASModel` set to `kOmegaSST` selects the SST $$k-\omega$$ turbulence model.



## Boundary Conditions

Since the simulation starts at time $$t=0$$, the boundary and initial field data is stored in the `0` sub-directory. This must be done for all variables solved for, such as pressure `p`, velocity `U` and temperature `T` as this is a compressible case. Furthermore, the SST $$k-\omega$$ solves two additional transport equations for turbulent kinetic energy $$k$$ and specific dissipation rate $$\omega$$. Therefore, initial and boundary conditions have to be provided for these variables as well. Finally, the treatment of the turbulent viscosity $$\nu_\text{t}$$ and turbulent thermal diffusivity $$\alpha_\text{t}$$ at the walls have to be specified as well.

### Pressure, Velocity and Temperature

For this example case, the volumetric flow rate at the air inlet as well as exhaust gas inlet are given. Instead of manually calculating the inlet velocity based on patch area (e.g., inlet velocity equal to volumetric flow rate divided by patch area), we can use the velocity inlet boundary condition `flowRateInletVelocity` and directly specify the volumetric flow rate. The setup for both inlets looks as follows:

```
inlet_air
{
    type                flowRateInletVelocity;
    volumetricFlowRate  0.005;
    value               uniform (0 0 0);
}

inlet_exhaust
{
    type                flowRateInletVelocity;
    volumetricFlowRate  0.0025;
    value               uniform (0 0 0);
}
```

Pressure at both inlets is treated as zero gradient and inlet temperature is $$300\,\text{K}$$ for the air inlet and $$900\,\text{K}$$ for the exhaust gas inlet, respectively. At the outlet, velocity and temperature are treated as zero gradient and the static pressure is set to $$10^5\,\text{Pa}$$. The walls are considered no-slip and adiabatic. Thus, the velocity is set to $$(0 \, 0 \, 0)$$, temperature and pressure to zero gradient.


### Turbulent Quantities

The turbulent kinetic energy $$k$$ at the inlet is estimated based on turbulent intensity $$I_t$$ using the `turbulentIntensityKineticEnergyInlet` boundary condition with an intensity of 2 % at the air inlet and 8 % at the exhaust gas inlet. Similarly, specific dissipation rate $$\omega$$ is estimated via turbulent length scale $$L_t$$ and the `turbulentMixingLengthFrequencyInlet` boundary condition. In both cases, the length scale is equal to the pipe diameter. Wall functions are used for the walls with the `kqRWallFunction` for turbulent kinetic energy and the `omegaWallFunction` for the specific dissipation rate. At the outlet, both variables are treated with zero gradient. Turbulent kinetic energy and specific dissipation rate are initialized with $$0.1\,\text{m}^2\text{/s}^2$$ and $$10\,000\,\text{1/s}$$, respectively.

Turbulent viscosity $$\nu_t$$ and turbulent thermal diffusivity $$\alpha_t$$ have to be specified only at the walls. Here, we are using a wall funtion approach as well with the `nutUSpaldingWallFunction` boundary condition for `mut` and the `compressible::alphatWallFunction` boundary condition for `alphat`. All other patches are set to `calculated` as they will be computed by the turbulence model itself.



## Simulation Control

Time control, solver selection and output settings are read from the `controlDict` in the `system` directory:

```
solver          fluid;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         0.08;

deltaT          1.25e-5;

writeControl    runTime;

writeInterval   0.002;
```

In this tutorial case, the solver `fluid` is used, a pressure-based solver for compressible, steady-state or transient, laminar or turbulent single-phase flows. The simulation starts at time `0`, runs until an end time of $$0.08\,\text{s}$$. Time step size `deltaT` is set to $$1.25 \times 10^{-5}\,\text{s}$$ for stability reasons. Finally, results are witten out every $$0.002\,\text{s}$$.



## Discretization

The finite-volume discretisation schemes are set in the `fvSchemes` dictionary in the `system` directory. Since this is a transient simulation, the temporal term discretization is first Euler implicit, gradients use an unlimited second order scheme `Gauss linear`, and the convective terms for momentum, energy, and turbulent scalars use a second order upwind scheme. Since the SST $$k-\omega$$ turbulence model is chosen, the distance from cell centers to the nearest wall has to be computed. For this, the `meshWave` method is selected under `wallDist`.


```
ddtSchemes
{
    default         Euler;
}

gradSchemes
{
    default         Gauss linear;
}

divSchemes
{
    div(phi,U)      Gauss linearUpwindV  Gauss linear;

    div(phi,h)      Gauss linearUpwind Gauss linear;
    div(phi,K)      Gauss linearUpwind Gauss linear;

    div(phi,k)      Gauss linearUpwind Gauss linear;
    div(phi,omega)  Gauss linearUpwind Gauss linear;
}

...

wallDist
{
    method          meshWave;
}
```


## Linear Solver Settings

The linear equation solvers, tolerances and coupling controls are set in the `fvSolution` dictionary in the `system` directory.

The pressure field in the pressure-velocity coupling is solved using a **Geometric agglomerated Algebraic MultiGrid** (short: GAMG) solver with a Gauss-Seidel solver for smoothing during the multi-grid steps. The solver is actually set up twice as the pressure-velocity equation is solved more than once. For the intermediate iterations, a relative tolerance of $$0.01$$ is used while for the final iteration a relative tolerance of $$0$$ is used. The momentum and energy equation as well as the transport equations for the turbulent properties are solved using a Gauss Seidel solver . The absolute tolerance for solving is $$10^{-6}$$ with a relative tolerance of $$0.1$$.

```
solvers
{
    p
    {
        solver          GAMG;
        smoother        GaussSeidel;
        tolerance       1e-6;
        relTol          0.01;
    }

    pFinal
    {
        $p;
        relTol          0;
    }

    "(rho|U|h|k|omega).*"
    {
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-06;
        relTol          0.01;
    }
}
```



### Pressure-velocity coupling

Pressure-based simulations in OpenFOAM rely on the PIMPLE pressure-velocity coupling algorithm. In this tutorial, the pressure correction equation is solved one additional time every iteration for improved convergence and stability with the `nCorrectors` entry set to `2`. Since this is a transient simulation, relaxation factors or residual criteria are not strictly required.

```
PIMPLE
{
    nCorrectors         2;
}
```
