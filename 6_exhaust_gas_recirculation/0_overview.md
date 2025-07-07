---
layout: default
title: 6. Exhaust Gas Recirculation
nav_order: 7
---

# Exhaust Gas Recirculation

## Objectives

The objectives for this tutorial are as follows:

- Create a three-dimensional mesh in OpenFOAM with `cartesianMesh` and check its quality,
- Set boundary conditions,
- Run a transient, compressible simulation with `rhoPimpleFoam` in parallel,
- Plot the maximum and average temperature at the outlet,
- Visualize the velocity field in ParaView, and
- Vary flow rate of exhaust gas and analyse impact onto flow field.

## Overview

This tutorial will describe how to pre-process, run, and post-process a case involving a transient, compressible flow of a exhaust gas recirculation. The geometry is shown in the following figure with an inlet for cold air on the left, inlet for the hot exhaust gas in the center, no-slip adiabatic walls for the air and exhaust side, and an outlet at the right. The flow will be solved using the OpenFOAM solver `rhoPimpleFoam` the suitable for laminar and turbulent, compressible, transient flows.

![Diffuser case geometry](figures/exhaust_gas_recirculation-geometry.png)

## Preparation

Before starting, perform the following steps for preparation:
 1. Download the archive `6_exhaust_gas_recirculation.zip` from the Downloads folder on the [OPAL course page](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/19816513539).
 2. Extract the archive.
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM.
