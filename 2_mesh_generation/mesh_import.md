# Mesh Import

## Introduction

This first part explains the general OpenFOAM case structure, where the mesh information is stored and how to import a two-dimensional mesh created with an external software. At the end, the mesh will be visualized using ParaView. The geometry of the case looks as follows:

![Elbow case geometry](figures/elbow-geometry.png)

Navigate with your terminal to the extracted sub-directory `elbow` within the `1_mesh_generation` directory.

## OpenFOAM case structure

A case being simulated involves data for mesh, fields, properties, control parameters, etc. In OpenFOAM this data is stored in a set of files within a case directory rather than in a single case file, as in many other CFD packages. The case directory is given a suitably descriptive name, here `elbow`. This folder contains the following subfolders and files:

```
elbow
├── 0
│   ├── p
│   └── U
├── constant
│   └── momentumProperties
│   └── physicalProperties
└── system
    ├── controlDict
    ├── fvSchemes
    └── fvSolution
 
3 directories, 7 files
```

`0` - This folder is a special time directory that contains the initial conditions and boundary conditions for starting the simulation. In this tutorial:

- `p` and `U` for the relative, kinematic pressure and velocity fields, respectively.

`constant` - This directory contains files that are related to the physics of the problem, including the mesh and any physical properties that are required for the solver. In this case:

- `momentumProperties` configures the choice of turbulence modelling method, e.g. laminar, Reynolds-averaged Navier-Stokes (RANS) or Large Eddy simulation (LES).
- `physicalProperties` has the thermophysical properties of the fluid, e.g. rheological model, and viscosity.
- The `polyMesh` folder stores the mesh information, once a mesh has been created or imported. Therefore, it is not yet present at the start of this tutorial.

`system` - This folder contains files related to how the simulation is to be solved:

- `controlDict` for setting control parameters including start/end time, time step size and parameters for data output.
- `fvSchemes` holds the discretisation schemes used in the solution selected during runtime.
- `fvSolution` for setting the equation solvers, tolerances, relaxation factors and other algorithm controls for the run.

**Note:** This first tutorial only focuses on mesh import and visualization. Later, we will come back to this tutorial and solve the flow with OpenFOAM.

## Mesh import

The mesh for this case has been created using an external software and is stored in the ANSYS Fluent mesh format `*.msh`. OpenFOAM offers many different utilities for importing mesh files into the OpenFOAM format and storing them in the `constant/polyMesh` folder. In this case, when the terminal's working directory is the `elbow` case folder, the mesh can be imported using the following command:

```
fluentMeshToFoam elbow.msh
```

Here, `fluentMeshToFoam` is the executable for importing the mesh and `elbow.msh` is the argument pointing towards the mesh file inside the `elbow` case folder. The utlitity sucessfully imports the mesh and confirms this with the output:

```
...
Writing mesh... to "constant/polyMesh"  done.
 
End
```

The mesh has been successfully imported into the OpenFOAM format and stored within the `constant/polyMesh` folder.

## Mesh files

When a mesh is written out by OpenFOAM, the data files go into a `polyMesh` sub-directory. Usually the `polyMesh` directory is written to the the constant directory, but simulations with dynamic meshes (e.g. mesh motion, refinement, etc.) write the modified meshes into time directories along with the field data files.

The data files are based around faces rather than cells. Each face is therefore assigned an *owner* cell and *neighbour* cell so that the connectivity across a given face can simply be described by the owner and neighbour cell labels. In the case of boundaries, there is no neighbour cell. With this in mind, the I/O specification consists of the following files:

- `points`: a list of vectors describing the cell vertices, where the first vector in the list represents vertex 0, the second vector represents vertex 1, etc.;
- `faces`: a list of faces, each face being a list of indices to vertices in the points list, where again, the first entry in the list represents face 0, etc.;
- `owner`: a list of owner cell labels, starting with the owner cell of face 0, then 1, 2, ...
- `neighbour`: a list of neighbour cell labels;
- `boundary`: a list of patches, containing a dictionary entry for each patch, declared using the patch name.

## Mesh boundary

The domain boundary is defined by patches within the mesh, listed within the `boundary` mesh file. Each patch includes a `type` entry which can apply a geometric constraint to the patch. These geometric constraints include conditions that represent a geometric approximation, e.g. a symmetry plane, and conditions which form numerical connections between patches. The boundary file from this tutorial is shown below which includes some patches with geometric constraints.

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

6
(
    wall-left
    {
        type            wall;
        inGroups        List<word> 1(wall);
        nFaces          100;
        startFace       1300;
    }
    inlet-left
    {
        type            patch;
        nFaces          8;
        startFace       1400;
    }
    inlet-bottom
    {
        type            patch;
        nFaces          4;
        startFace       1408;
    }

    outlet
    {
        type            patch;
        nFaces          8;
        startFace       1412;
    }

    wall-right
    {
        type            wall;
        inGroups        List<word> 1(wall);
        nFaces          34;
        startFace       1420;
    }

    frontAndBackPlanes
    {
        type            empty;
        inGroups        List<word> 1(empty);
        nFaces          1836;
        startFace       1454;
    }
)

// ************************************************************************* //
```

Here, the mesh of the tutorial case consists of 6 individual patches:
- two inlet patches named `inlet-left` and `inlet-bottom` both of type `patch`,
- one outlet called `outlet` also of type `patch`,
- two walls named `wall-left` and `wall-right` of type `wall`, and
- a patch called `frontAndBackPlanes` of type `empty`.

### Patch types

The patch types specified in the boundary file, which are not associated with a geometric constraint are the generic `patch` and `wall`. The `patch` type is assigned to open boundaries such as an inlet or outlet which does not involve any special handling of geometric approximation or numerical connections.

The `wall` type also provides no special geometric or numerical handling, but is used for patches which coincide with a solid wall. The `wall` tag is required by some models, e.g. wall functions in turbulence modelling which require the distance to nearest wall.

OpenFOAM is designed as a code for 3D space and defines all meshes as such. However, 1D and 2D and axi-symmetric problems can be simulated in OpenFOAM by generating a mesh in 3 dimensions and applying special boundary conditions on any patch in the plane(s) normal to the direction(s) of interest. 1D and 2D problems apply the `empty` patch type to the relevant patches. Often the two regions of the boundary, on the *front* and *back* of the domain, are combined into a single patch, as in the `frontAndBackPlanes` patch in this tutorial.

## Mesh quality

After importing or generating a computational grid it is always recommended to check the mesh statistics and quality criteria. This can easily be done using the utility `checkMesh` from within the `elbow` folder. Just type in the terminal:

```
checkMesh
```

This will produce the following output to the terminal:

```
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
Create time
 
Create polyMesh for time = 0
    
Time = 0s
    
Mesh stats
    points:           1074
    internal points:  0
    faces:            3290
    internal faces:   1300
    cells:            918
    faces per cell:   5
    boundary patches: 6
    point zones:      0
    face zones:       0
    cell zones:       0
    
Overall number of cells of each type:
    hexahedra:     0
    prisms:        918
    wedges:        0
    pyramids:      0
    tet wedges:    0
    tetrahedra:    0
    polyhedra:     0
    
Checking topology...
    Boundary definition OK.
    Cell to face addressing OK.
    Point usage OK.
    Upper triangular ordering OK.
    Face vertices OK.
    Number of regions: 1 (OK).
    
Checking patch topology for multiply connected surfaces...
    Patch               Faces    Points   Surface topology                  
    wall-left           100      206      ok (non-closed singly connected)  
    inlet-left          8        18       ok (non-closed singly connected)  
    inlet-bottom        4        10       ok (non-closed singly connected)  
    outlet              8        18       ok (non-closed singly connected)  
    wall-right          34       70       ok (non-closed singly connected)  
     frontAndBackPlanes  1836     1074     ok (non-closed singly connected)  
    
Checking geometry...
    Overall domain bounding box (0 -4.53853 -0.937738) (64 64 0.937738)
    Mesh has 2 geometric (non-empty/wedge) directions (1 1 0)
    Mesh has 2 solution (non-empty) directions (1 1 0)
    All edges aligned with or perpendicular to non-empty directions.
    Boundary openness (-1.03633e-18 2.59082e-18 1.15147e-19) OK.
    Max cell openness = 1.87187e-16 OK.
    Max aspect ratio = 2.40135 OK.
    Minimum face area = 0.278218. Maximum face area = 7.72369.  Face area magnitudes OK.
    Min volume = 0.521792. Max volume = 7.36354.  Total volume = 3156.3.  Cell volumes OK.
    Mesh non-orthogonality Max: 36.302 average: 11.1868
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 0.500248 OK.
    Coupled point location match (average 0) OK.
    
 Mesh OK.
    
End
```

This gives us all relevant mesh statistics and quality criteria of the mesh. Among others, this includes starting from top:

- The mesh consists of 1074 points,
- has 3290 faces in total,
- has 918 cells with a prism shape,
- has the six boundary patches named `wall-left`, `inlet-left`, `inlet-bottom`, `outlet`, `wall-right`, and `frontAndBackPlanes`
- with 100, 8, 4, 8, 34, and 1836 faces, respectively.

Below follow various relevant mesh quality criteria, such as:

- Overall domain bounding box of `(0 -4.53853 -0.937738) (64 64 0.937738)`,
- number of non-empty solution directions of 2 (e.g. a 2-dimensional case),
- max cell aspect ratio of 2.40135,
- a minimum and maximum cell volume of 0.521792 and 7.36354, respectively,
- a maximum mesh non-orthogonality of 36.302, and
- a max cell skewness of 0.500248.

The final output `Mesh OK.` indicates that no critical problems or errors were found during `checkMesh`. Therefore, we can continue with this mesh and proceed with the simulation.

**Note:** OpenFOAM always uses SI-units. Therefore, geometric dimensions shown here are in meter.

## Mesh manipulation

Once the mesh has been imported with `fluentMeshToFoam`, the tool `checkMesh` reveals a very good mesh quality. However, the mesh is incorrectly scaled as indicated by the bounding box. It shows an overall domain size of $64\,\text{m}$ in $x$-direction (from $0\,\text{m}$ to $64\,\text{m}$), $68.54\,\text{m}$ in $y$-direction (from $-4.54\,\text{m}$ to $+64\,\text{m}$), and $1.97\,\text{m}$ in $z$-direction:

```
Checking geometry...
    Overall domain bounding box (0 -4.53853 -0.937738) (64 64 0.937738)
    Mesh has 2 geometric (non-empty/wedge) directions (1 1 0)
```

In order to manipulate the mesh, e.g. scale, translate or rotate, the OpenFOAM utility `transformPoints` can be used. In this tutorial, the overall size of the bounding box must be scaled from $64\,\text{m}$ in $x$-direction down to $64\,\text{mm}$. This results in a scaling factor of 0.001 in all three dimensions. As a result, the `transformPoints` command has to be executed using the `scale` option as follows:

```
transformPoints "scale=(0.001 0.001 0.001)"
```

Once executed, the mesh will be scaled down by a factor of 1000.

**Warning:** If this command is executed twice, the mesh will be scaled by $0.001 \times 0.001=10^{-6}$.

**Note:** It is impossible to memorize the syntax and functionality of all OpenFOAM solvers, utilities and post-processing tools. Therefore, you can always execute a command with the option `-help`. This will give you a detailed list of all options and how to use them, i.e. in this example how to use the `scale` option of the mesh manipulation utility `transformPoints`.

## Viewing the mesh

Before the case is run it is a good idea to view the mesh to check for any errors. The mesh is viewed in ParaView, the post-processing tool supplied with OpenFOAM. The ParaView post-processing is conveniently launched on OpenFOAM case data by executing the `paraFoam` executable from within the case directory.

Any UNIX/Linux executable can be run in two ways: as a foreground process, i.e. one in which the shell waits until the command has finished before giving a command prompt; or as a background process, which allows the shell to accept additional commands while it is still running. Since it is convenient to keep ParaView open while running other commands from the terminal, we will launch it in the background using the `&` operator by typing:

```
paraFoam &
```

This launches the ParaView window and opens the elbow case as shown in the following figure:

![ParaView opened](figures/elbow-paraview-start.png)

In the **Pipeline Browser** on the left, the user can see that ParaView has opened `elbow.OpenFOAM`, the module for the elbow case. Clicking on the green **Apply** button in the **Properties** panel displays the computational domain. Selecting **Surface with Edges** in the top center menu bar shows the computational mesh as follows:

![ParaView showing the elbow surface mesh](figures/elbow-paraview-mesh.png)

**Note:** Many advanced parameters in the Properties panel are only available by clicking the Advanced Properties gearwheel button at the top of the Properties window, next to the search box.

## Conclusion

This concludes the first case in the **Meshing Tutorial**. We have:
- Successfully import a **ANSYS Fluent** mesh file `*.msh` into the OpenFOAM case structure using the command `fluentMeshToFoam`,
- Checked the mesh quality with `checkMesh`,
- Reduced the scaling of the mesh by a factor of 1000 using `transformPoints`, and
- Visualized the mesh with **ParaView**.