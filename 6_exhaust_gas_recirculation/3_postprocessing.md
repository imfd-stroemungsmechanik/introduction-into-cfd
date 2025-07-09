---
layout: default
title: Post-Processing
parent: 6. Exhaust Gas Recirculation
nav_order: 3
---

# Post-Processing


## Visualizing the Velocity Contour

As soon as results from the processor folders are reconstructed, they can be viewed using ParaView. Start ParaView in the background with the following command:

```bash
paraFoam &
```

To prepare ParaView to display the data of interest, the data of the last time step at $$t = 0.08\,\text{s}$$ must be loaded. If the case was run while ParaView was open, the output data in time directories will not be automatically loaded within ParaView. To load the data the user should click **Refresh** at the top **Properties** window (scroll up the panel if necessary).

To color the mesh by velocity magnitude (i.e. the velocity contour) of the flow, the following settings must be selected in the **Properties** panel, as descriped in the following figure:

1. Select **Surface** from the **Representation** menu,
2. Select **Coloring** by velocity magnitude U, and
3. Select **Rescale to Data Range**, if necessary.

![Exhaust gas recirculation system paraview velocity contour settings](figures/paraview-menu-velocity-contour-settings.png)

When inspecting the velocity field, the increase of flow velocity at and downstream of the t-junction is apparent. This is simply due to conservation of mass as flow rates from both inlets have to pass through the main pipe.

![Exhaust gas recirculation system paraview velocity contour](figures/results-velocity-contour.png)

When clicking the **Play** button in the **VCR Controls** at the very top of the ParaView window, one can see the transient nature of the flow and the characteristic flow separation just below the t-junction:

![Exhaust gas recirculation system paraview velocity animation](figures/results-velocity-animation.gif)



## Visualizing the Temperature Contour

The mixing of exhaust gas and fresh air is best visualized using the temperature field. Selecting temperature `T` in the **Properties** panel and rescaling the data range gives the following temperature contour:

![Exhaust gas recirculation system paraview temperature contour](figures/results-temperature-contour.png)

Smaller flow structures with higher temperature can be seen downstream the t-junction. When selecting the time-averaged temperature field `TMean` instead, it shows a smooth temperature field and the mixing process of exhaust gas and fresh air:

![Exhaust gas recirculation system paraview temperature contour](figures/results-temperature-mean-contour.png)

