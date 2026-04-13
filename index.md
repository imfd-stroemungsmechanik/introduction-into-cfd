---
layout: default
title: Getting Started
nav_order: 1
---

# Getting Started

## Scope of the Seminar

This repository complements the course Introduction into Computational Fluid Dynamics and provides guided tutorials to familiarize yourself with the Linux command line, OpenFOAM, and post-processing tool ParaView:

1. [An introduction to the Linux](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/1_linux_introduction/0_overview.html)
2. [Mesh generation in OpenFOAM](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/2_mesh_generation/0_overview.html)
3. [Transient flow over a backwards-facing step](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/3_backward-step/0_overview.html)
4. [Steady-state flow around a NACA 0012 airfoil](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/4_airfoil/0_overview.html)
5. [Steady-state, turbulent flow in a diffuser](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/5_diffuser/0_overview.html)
6. [Compressible flow in an exhaust gas recirculation](https://imfd-stroemungsmechanik.github.io/introduction-into-cfd/6_exhaust_gas_recirculation/0_overview.html)
7. Two-phase liquid sloshing in a tank

## How to use this guide

This repository offers a step-by-step introduction to the Linux operating system, the terminal, OpenFOAM for simulation, and ParaView for post-processing. If you are already familiar with the Linux command line, you can skip the first part and directly work on the second tutorial dealing with the mesh generation in OpenFOAM.

Each OpenFOAM tutorial case is accompanied by an archive containing the pre-configured OpenFOAM cases. These archives can be downloaded via the respective links in the tutorials. Save the archive wherever you want to run your simulations (e.g. a new simulations directory inside your home directory) and unzip them in preparation for the tutorials.

## Guide style conventions

Throughout the tutorials, the user guide will show you the content of certain files, file names and paths, the output of OpenFOAM commands, and which commands to use. To enhance clarity, this guide uses the following style conventions:

### Linux and OpenFOAM commands

Commands, which should be executed in the command line are formatted as follows:

```bash
pwd
```

In this example, type the command `pwd` into the terminal and press enter. Whenever commands, folder or file names are mentioned in the text body, they are formatted in bold monospace. Similar to the `pwd` command, the Linux home folder for example is written as `home`.

### Notes and warnings

Notes, tips, and warnings contain useful additional information:

{: .note }
> Useful information that users should know, even when skimming content.

{: .tip }
> Helpful advice for doing things better or more easily.

{: .warning }
> Informs of risks or negative outcomes of certain actions.

### Content of files and terminal output

The content of files within the user guide will be presented within a border with grey background as shown below. For example, the `controlDict` inside the `system` folder within a OpenFAOM case would start with the following lines:

```
/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website: https://www.openfoam.org
    \\  /    A nd           | Version: 13
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    format   ascii;
    class    dictionary;
    object   controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
```

The output of commands in the terminal are formatted similarly.

## OpenFOAM

**OpenFOAM (Open Field Operation And Manipulation)** is a C++ toolbox for the development of customized numerical solvers and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD).

The OpenFOAM software is used in research organisations, academic institutes and across many types of industries, for example, automotive, manufacturing, process engineering and environmental engineering.

OpenFOAM is an open-source software, which is freely available and licensed under the GNU General Public License Version 3, with the following variants and their latest version:

- [OpenFOAM 13](https://openfoam.org/) developed and maintained by the OpenFOAM Foundation with a sequence based identifier
- [OpenFOAM v2512](https://www.openfoam.com/) developed and maintained mainly by the ESI Group with a date-of-release identifier
- [The FOAM-Extend Project](http://wikki.co.uk/index.php/foam-extend/), mainly maintained by Wikki Ltd.

Both OpenFOAM versions are already installed on the PCs in the computer labs on the Linux operating system. **Throughout the seminar, we will exclusively be using OpenFOAM 13**. Unfortunately, there are certain incompatibilities between the different OpenFOAM versions and tutorial cases from OpenFOAM v2512 cannot be run using OpenFOAM 13 without a adjustments. Installation instructions for Windows, Mac and Linux can be found on the respective homepages.

## Starting OpenFOAM in the computer labs

Whenever OpenFOAM is going to be used, you have to source it at least once inside this terminal. This can be achieved by typing the following command inside the terminal:

```bash
source /app2/OpenFOAM/OpenFOAM-13/etc/bashrc
```

By using `source`, all commands, links and paths inside `bashrc` are now available to the user. Utilities and solvers can now be executed by typing their respective name in the terminal. However, this resets once the current terminal is closed and retyping the command is time-consuming. One possible solution is to use an alias, which is an individual shortcut for a longer command. To create a new alias, execute the following command in your terminal.

```bash
echo 'alias of13="source /app2/OpenFOAM/OpenFOAM-13/etc/bashrc"' >> ~/.bashrc
```

Now close this terminal. From now on, whenever you want to source OpenFOAM in a new terminal, you can simply type `of13` instead of typing the complex `source` command introduced earlier. This even persists after restarting the computer.

## Disclaimer

This offering is not approved or endorsed by OpenCFD Limited, the producer of the OpenFOAM software and owner of the OPENFOAM® and OpenCFD® trademarks.
