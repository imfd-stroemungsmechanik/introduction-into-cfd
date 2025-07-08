---
layout: default
title: 6. Exhaust Gas Recirculation
nav_order: 7
---

# Exhaust Gas Recirculation

## Motivation

Exhaust Gas Recirculation (EGR) is a nitrogen oxide (NOx) reduction technique used in internal combustion engines. The system works by recirculating a portion of the engine's exhaust gas back into the combustion chamber, where it mixes with the incoming fresh air-fuel mixture. This seemingly counterintuitive approach of mixing "waste" exhaust gases with fresh intake air serves a crucial purpose in modern automotive engineering.

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

![Exhaust gas recirculation system case geometry](figures/exhaust-gas-recirculation-geometry.png)

The boundary conditions for the give problem are as follows:
- Air inlet: Volumetric flow rate of $$Q = 0.005\,\text{m}^3\text{/s}$$ at a temperature of $$300\,\text{K}$$
- Exhaust gas inlet: Volumetric flow rate of $$Q = 0.0025\,\text{m}^3\text{/s}$$ at a temperature of $$900\,\text{K}$$
- Outlet: Pressure of $$10^5\,\text{Pa}$$
- Pipe walls: Adiabatic and no-slip

## Preparation

Before starting, perform the following steps for preparation:
 1. Download the archive `6_exhaust_gas_recirculation.zip` from the Downloads folder on the [OPAL course page](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/19816513539).
 2. Extract the archive.
 3. Open a terminal, navigate to the newly created folder, and source OpenFOAM.
