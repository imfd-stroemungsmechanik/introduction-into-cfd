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
- Create a unstructured hexahedral-dominated mesh with `cartesianMesh`,
- Check the mesh quality with `checkMesh`,
- Visualize the mesh and its quality criterion in ParaView.

## Overview

This tutorial will describe how to either import a existing mesh to OpenFOAM or create a mesh within OpenFOAM itself. The first mesh is a two-dimensional elbow named `elbow.msh` created with ANSYS ICEM CFD. The second mesh is a hexahedral-dominated mesh of group of buildings created with `cartesianMesh`. Once the meshes have been either imported or created, their quality will be checked using `checkMesh`. Finally, the meshes will be visualized with ParaView.

## Preparation

Before starting, perform the following steps for preparation:
 1. Download the archive `2_mesh_generation.zip` from the Downloads folder on the [OPAL course page](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/19816513539).
 2. Extract the archive.
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM.
