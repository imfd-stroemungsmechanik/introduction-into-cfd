---
layout: default
title: 2. Mesh Generation
nav_order: 3
---

# Meshing in OpenFOAM

## Objectives

The objectives for this tutorial are as follows:

- Familiarize yourself with the OpenFOAM case structure,
- Import a two-dimensional mesh into OpenFOAM and check its quality,
- Create a simple block-structured mesh with `blockMesh`,
- Check the mesh quality with `checkMesh`,
- Visualize the mesh in ParaView.

## Overview

This tutorial will describe how to either import an existing mesh into OpenFOAM or create a mesh within OpenFOAM itself. The first mesh is a two-dimensional elbow named `elbow.msh` created with ANSYS ICEM CFD. The second mesh is a block-structured mesh created with the OpenFOAM tool `blockMesh` for the flow over a backwards-facing step. Once the meshes have been either imported or created, their quality will be checked using `checkMesh`. Finally, the meshes will be visualized with ParaView.

## Preparation

Before starting, perform the following steps for preparation:
 1. Download the archive file [2_mesh_generation.zip](https://github.com/user-attachments/files/27125115/2_mesh_generation.zip) containing the case folders.
 2. Extract the archive and move its content to the `OpenFOAM_Projects` folder, which has been created in the first tutorial. 
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM using the `of13` alias introduced in the first tutorial.
