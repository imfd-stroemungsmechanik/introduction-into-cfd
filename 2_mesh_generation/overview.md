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

This tutorial will describe how to either import a existing mesh to **OpenFOAM** or create a mesh within **OpenFOAM** itself. The first mesh is a two-dimensional elbow named `elbow.msh` created with **ANSYS ICEM CFD**. The second mesh is a hexahedral-dominated mesh of a car created with `cfMesh`. Once the meshes have been either imported or created, their quality will be checked using `checkMesh`. Finally, the meshes will be visualized with **ParaView**.

## Preparation

The corresponding **OpenFOAM** cases for the meshing tutorial can be downloaded on from the Downloads folder on the OPAL course page. Extract the `2_mesh_generation.zip` archive, open a terminal and navigate to the newly created folder. Once there, source **OpenFOAM** and continue with the first of three parts of this tutorial:

1. [Mesh Import]({% link mesh_import.md %})
2. [Unstructured Mesh Generation](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/19816513539/CourseNode/1714444290937796010)
