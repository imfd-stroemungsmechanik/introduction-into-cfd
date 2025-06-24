---
layout: default
title: Post-Processing
parent: 5. Diffuser
nav_order: 3
---

# Post-Processing

## Visualizing the Results

As soon as results are written to time directories, they can be viewed using ParaView. Start ParaView in the background with the following command:

```bash
paraFoam &
```
To prepare ParaView to display the data of interest, the data at the required iteration of 547 must be loaded. If the case was run while ParaView was open, the output data in time directories will not be automatically loaded within ParaView. To load the data the user should click **Refresh** at the top **Properties** window (scroll up the panel if necessary).

The solution at the iteration 1078 can be viewed by using the **VCR Controls** at the very top of the ParaView window and click the button for **Last Frame**.

![Diffuser paraview vcr controls](figures/paraview-menu-VCR-controls.png)

To color the mesh by velocity magnitude (i.e. the velocity contour) of the flow, the following settings must be selected in the **Properties** panel, as descriped in the following figure:
1. Select **Surface** from the **Representation** menu,
2. Select **Coloring** by velocity magnitude U at the cell centers, and
3. Select **Rescale to Data Range**, if necessary.

![Diffuser paraview velocity contour settings](figures/paraview-menu-velocity-contour-settings.png)

When inspecting the velocity field through the diffuser, the reduction in flow velocity due to the incresed cross-sectional area is apparent. Furthermore, no recirculation region is noticable at the lower end of the diffuser, something which would be expected due to the large opening angle of the diffuser.ine.

![Diffuser paraview velocity contour](figures/diffuser-results-velocity-contour.png)

