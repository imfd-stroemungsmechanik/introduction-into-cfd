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
- Create a unstructured hexahedral-dominated mesh with `cfMesh`,
- Check the mesh quality with `checkMesh`,
- Visualize the mesh and its quality criterion in ParaView.

## Overview

This tutorial will describe how to either import a existing mesh to **OpenFOAM** or create a mesh within **OpenFOAM** itself. The first mesh is a two-dimensional elbow named `elbow.msh` created with **ANSYS ICEM CFD**. The second mesh is a hexahedral-dominated mesh of a car created with `cartesianMesh`. Once the meshes have been either imported or created, their quality will be checked using `checkMesh`. Finally, the meshes will be visualized with **ParaView**.

## Preparation

Before starting, perform the following steps for preparation:
 1. Download the corresponding **OpenFOAM** cases for the meshing tutorial from the Downloads folder on the OPAL course page.
 2. Extract the `2_mesh_generation.zip` archive.
 3. Open a terminal, navigate to the newly created folder, and source **OpenFOAM**.

Once finished, you can continue with the tutorials:

1. [Mesh Import](1_mesh_import.md)
2. [Hex-dominant Mesh Generation](2_cartesianMesh.md)
