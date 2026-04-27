---
layout: default
title: Mesh Scripting with blockMesh
parent: 2. Mesh Generation
nav_order: 3
---


# Mesh Scripting with blockMesh

## Introduction

In the previous tutorial, every coordinate, cell count, and dimension in the `blockMeshDict` was specified as a hardcoded number. While this works, it becomes impractical for real-world cases: changing the step height, for example, requires modifying multiple vertex coordinates, and it is easy to introduce inconsistencies. In professional CFD workflows, meshes must be parameterized so that geometry and resolution changes can be applied in a single location.

This tutorial introduces three features of the OpenFOAM dictionary language that transform `blockMeshDict` from a static input file into a parametric, scriptable mesh definition:

1. **Variables** — replace repeated numerical values with named parameters.
2. **`#calc`** — evaluate C++ expressions to compute derived quantities at run-time.
3. **Curved edges** — define non-straight edges between block vertices using arcs and splines.

All three features are applied to the same backward-facing step case from the previous tutorial. Navigate with your terminal to the `2_backward-step` sub-directory within the `2_mesh_generation` directory. If you want to preserve the original case, create a copy first:

```bash
cp -r 2_backward-step 3_scripting
cd 3_scripting
```


## Variables in `blockMeshDict`

### Motivation

Consider the vertex list from the previous tutorial. The step height of $$25\,\text{mm}$$ appears as the literal number `25` in four different vertex coordinates, and as `-25` in four others. Similarly, the inlet length of $$50\,\text{mm}$$ appears as `-50` in four vertices. If the step height needs to be changed, every occurrence must be found and updated manually — a process that is tedious and error-prone.

OpenFOAM dictionaries support **variable declarations**: a name is assigned a value, and the variable can then be referenced anywhere in the file using the `$` prefix.


### Declaring variables

Variables are declared at the top of the file, after the header and before the entries that reference them. For the backward-facing step, the following variables capture all geometric dimensions:

```
// Geometric parameters
xInlet      -50;
xStep       0;
xOutlet     250;

yBottom     -25;
yMid        0;
yTop        25;

zBack       -1;
zFront      1;
```

Each variable is declared using the syntax `name value;` — the same syntax as any other OpenFOAM dictionary entry. Variable names should be descriptive and follow a consistent naming convention.


### Referencing variables

Once declared, variables are referenced with the `$` prefix. The vertex list from the previous tutorial can now be rewritten as follows:

```
vertices
(
    ($xInlet  $yMid     $zBack)     // 0
    ($xInlet  $yTop     $zBack)     // 1
    ($xStep   $yBottom  $zBack)     // 2
    ($xStep   $yMid     $zBack)     // 3
    ($xStep   $yTop     $zBack)     // 4
    ($xOutlet $yBottom  $zBack)     // 5
    ($xOutlet $yMid     $zBack)     // 6
    ($xOutlet $yTop     $zBack)     // 7

    ($xInlet  $yMid     $zFront)    // 8
    ($xInlet  $yTop     $zFront)    // 9
    ($xStep   $yBottom  $zFront)    // 10
    ($xStep   $yMid     $zFront)    // 11
    ($xStep   $yTop     $zFront)    // 12
    ($xOutlet $yBottom  $zFront)    // 13
    ($xOutlet $yMid     $zFront)    // 14
    ($xOutlet $yTop     $zFront)    // 15
);
```

Compared to the original file, this version is both more readable and more maintainable. The inline comments `// 0`, `// 1`, etc. are optional but help track the vertex indices. Changing the step height from $$25\,\text{mm}$$ to $$30\,\text{mm}$$ now requires editing only two lines (`yBottom` and `yTop`) instead of sixteen coordinates.

{: .tip }
> Adding inline comments with the vertex index next to each vertex definition makes the `blockMeshDict` much easier to debug. This is considered good practice, especially for cases with many vertices.


### Parameterizing the block resolution

Variables are not limited to vertex coordinates. The cell counts in the `blocks` entry can be parameterized in the same way. Add the following resolution variables below the geometric parameters:

```
// Mesh resolution
nxInlet     20;
nxOutlet    100;
nyHalf      10;
nz          1;
```

The `blocks` entry then becomes:

```
blocks
(
    // 1st block
    hex (0 3 4 1 8 11 12 9)
    ($nxInlet $nyHalf $nz)
    simpleGrading (1 1 1)

    // 2nd block
    hex (2 5 6 3 10 13 14 11)
    ($nxOutlet $nyHalf $nz)
    simpleGrading (1 1 1)

    // 3rd block
    hex (3 6 7 4 11 14 15 12)
    ($nxOutlet $nyHalf $nz)
    simpleGrading (1 1 1)
);
```

A mesh refinement study, where the resolution is systematically doubled, can now be performed by changing just four values instead of editing every block individually.

{: .note }
> The `boundary` and `defaultPatch` entries remain unchanged — they reference vertex indices, not coordinates or variables.


## Computing values with `#calc`

### Motivation

Some values in the `blockMeshDict` are not independent but are derived from other parameters. For example, `yBottom` is simply the negative of `yTop` when the step height equals the channel half-height. Declaring both independently introduces the risk of inconsistency. The `#calc` directive solves this by evaluating C++ expressions inline.


### Syntax

The `#calc` directive takes a C++ expression enclosed in double quotes and evaluates it at parse time. Variables can be referenced inside the expression using the `$` prefix:

```
variableName  #calc "C++ expression using $otherVariable";
```


### Deriving dependent dimensions

With `#calc`, the geometric parameters can be reduced to a set of truly independent values. The following definition derives `yBottom` and `xInlet` from the step height and inlet length and is placed at the top of `blockMeshDict`:

```
// Independent geometric parameters
stepHeight  25;
inletLength 50;
outletLength 250;
channelHalfHeight 25;

// Derived coordinates
xInlet      #calc "-$inletLength";
xStep       0;
xOutlet     $outletLength;

yBottom     #calc "-$stepHeight";
yMid        0;
yTop        $channelHalfHeight;

zBack       -1;
zFront      1;
```

Now, `yBottom` is automatically computed as the negative of `stepHeight`. If the step height changes, the bottom coordinate updates automatically, and the mesh remains consistent.


### Computing the cell count from a target cell size

In practice, the mesh resolution is often specified through a target cell size rather than a fixed number of cells. The `#calc` directive can compute the required cell count at run-time. The following lines replace the previous hard-coded mesh resolution:

```
// Mesh resolution
cellSize    2.5;
nxInlet     #calc "round($inletLength / $cellSize)";
nxOutlet    #calc "round($outletLength / $cellSize)";
nyHalf      #calc "round($channelHalfHeight / $cellSize)";
nz          1;
```

With this approach, changing `cellSize` from `2.5` to `1.25` automatically doubles the resolution in all directions. The `round()` function ensures that the result is an integer, as required by `blockMesh`.

{: .warning }
> The `#calc` directive evaluates standard C++ expressions. This means that C++ mathematical functions such as `sin()`, `cos()`, `sqrt()`, `pow()`, and `round()` are available. However, integer division follows C++ rules: `5 / 2` evaluates to `2`, not `2.5`. Use `5.0 / 2.0` for floating-point division when necessary.


### Generating the mesh

Create the new mesh by running `blockMesh` again and verify the result with `checkMesh`:

```bash
blockMesh
checkMesh
```

{: .warning }
> Running `blockMesh` automatically overwrites any previously existing mesh.
