---
layout: default
title: Getting Started
nav_order: 1
---

# Getting Started

## Scope of the Seminar

This repository complements the course Introduction into Computational Fluid Dynamics and provides currently three guided tutorials designed for familiarizing with the Linux command line, OpenFOAM, and post-processing tool ParaView:

1. An introduction into the Linux command line
2. Meshing in OpenFOAM
3. Simulating of an incompressible flow through an elbow
4. Simulation of the transient, incompressible flow over a backward-facing step
5. Comparison of different turbulence models for predicting the drag coefficient of the DrivAer fastback vehicle

## How to use this guide

This repository offeres a step-by-step introduction both into the Linux command line as well as OpenFOAM for simulation and ParaView for post-processing. If you are already familiar with the Linux command line, you can skip the first part and directly work on the second tutorial dealing with the mesh generation in OpenFOAM.

Each OpenFOAM tutorial case is accompanied by an archive containing the pre-configured OpenFOAM cases. These archives can be downloaded from top of each tutorials page. Save the archive wherever you want to run your simulations (e.g. a new simulations directory inside your home), unzip it and keep it ready for the OpenFOAM tutorials.

## Guide style conventions

Throughout the tutorials, the user guide will show you the content of certain files, file names and path, the output of OpenFOAM commands, and which commands to use. In order to avoid any confusion, there are the following styling conventions:

### Linux and OpenFOAM commands

Commands, which should be executed in the command line are formatted in green:

```
pwd
```

This example, you should type the command `pwd` into terminal and press enter. Whenever commands, folder or file names are mentioned in the text body, they are formatted in bold monospace. Similar to the `pwd` command, the Linux home folder for example is written as `home`.

### Notes and warnings

Notes and warnings are coloured as a blue or red box. These contain useful additional information.



> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

### Content of files and terminal output

Content of files within the user guide are shown in a border with grey background and line numbers as shown below. The output of commands in the terminal are formatted similarly but without the line numbers. For example, the `blockMeshDict` inside the `system` folder within a OpenFAOM case would start with the following lines:

```
/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website: https://www.openfoam.com
    \\  /    A nd           | Version: v2412
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    format   ascii;
    class    dictionary;
    object   blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
```

## OpenFOAM

**OpenFOAM (Open Field Operation And Manipulation)** is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD).

The OpenFOAM software is used in research organisations, academic institutes and across many types of industries, for example, automotive, manufacturing, process engineering and environmental engineering.

OpenFOAM is open-source software which is freely available and licensed under the GNU General Public License Version 3, with the following variants and their latest version:

- [OpenFOAM 12](https://openfoam.org/) developed and maintained by the OpenFOAM Foundation with a sequence based identifier
- [OpenFOAM v2412](https://www.openfoam.com/) developed and maintained mainly by the ESI Group with a date-of-release identifier (e.g. v2412)
- The FOAM-Extend Project, mainly maintained by Wikki Ltd.

OpenFOAM 12 and OpenFOAM v2412 are already installed on the PCs in the computer labs under the Linux operating system. **Throughout the seminar, we will exclusively be using OpenFOAM v2412**. Unfortunately, there are certain incompatibilities between the different OpenFOAM versions. Therefore, you cannot simply take the tutorial cases and execute them on OpenFOAM 12. Installation instructions for Windows, Mac and Linux can be found on the respective homepages.

## Starting OpenFOAM in the computer labs

Whenever OpenFOAM is going to be used, you have to source it at least once inside this terminal. This can be achieved by typing the following command inside the terminal:

```
source /app2/OpenFOAM/OpenFOAM-v2412/etc/bashrc
```

Once enter is pressed, OpenFOAM will be sourced and ready for usage. Utilities and solvers can now be executed by typing their respective name in the terminal. However, typing this command inside each new terminal can be time consuming and prone to error. Therefore, an alias will be used instead. In order to create this alias, the following command has to be executed once in the terminal:

```
echo 'alias of11="source /app2/OpenFOAM/OpenFOAM-v2412/etc/bashrc"' >> ~/.bashrc
```

Now close this terminal. From this point forward, whenever you want to source OpenFOAM in a new terminal, you can simply type `of11` instead of typing the complex `source` command introduced earlier. This even persists after restarting the computer.

## Disclaimer

This offering is not approved or endorsed by OpenCFD Limited, the producer of the OpenFOAM software and owner of the OPENFOAM® and OpenCFD® trademarks.
