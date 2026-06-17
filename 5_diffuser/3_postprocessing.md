---
layout: default
title: Post-Processing
parent: 5. Diffuser
nav_order: 3
---

# Post-Processing


## Visualizing the Velocity Contour

As soon as results are written to time directories, they can be viewed using ParaView. Start ParaView in the background with the following command:

```bash
paraFoam &
```

Colour the surface by velocity magnitude `U` (Representation $$\rightarrow$$ **Surface**, Coloring $$\rightarrow$$ **U**, **Rescale to Data Range**). When inspecting the velocity field through the diffuser, the reduction in flow velocity due to the increased cross-sectional area is apparent. Notably, no recirculation appears at the lower wall even though the large opening angle of the diffuser would lead one to expect flow separation there.

![Diffuser paraview velocity contour](figures/diffuser-results-velocity-contour.png)


## Visualizing Flow Streamlines

Streamlines are a convenient way to reveal any recirculation. With the `1_diffuser.OpenFOAM` module highlighted in the **Pipeline Browser**, select the **Stream Tracer** filter from the **Common Data and Analytics** menu:

![Diffuser paraview stream tracer menu](figures/paraview-menu-stream-tracer.png)

In the **Properties** panel, trace the streamlines along the velocity field `U`, seeded on a straight line from $$(16.836 \,\, 0\,\, 0)$$ to $$(16.836 \,\, 4.7\,\, 0)$$ with a Seeding Resolution of 25, and colour them by pressure `p`. Click **Apply** to show the streamlines through the diffuser as follows:

![Diffuser paraview stream tracer](figures/diffuser-results-stream-tracer.png)

The adverse pressure gradient (an increase in pressure along the streamlines) is clearly visible, and there is no flow separation or recirculation at the lower wall. Resolving adverse pressure gradients and separation, however, is precisely the known weakness of the standard $$k-\epsilon$$ turbulence model.


## Plotting the Velocity Profile

For a quantitative comparison with experiment, plot the $$x$$-velocity along a vertical line through the diffuser. Hide the Stream Tracer, select the original `1_diffuser.OpenFOAM` module, and apply the **Plot Over Line filter** (**Filters** $$\rightarrow$$ **Data Analysis**). Use the same line as the streamline seed from $$(16.836 \,\, 0\,\, 0)$$ to $$(16.836 \,\, 4.7\,\, 0)$$ with a Resolution of 1000 points. In the plot, deselect every series except the $$x$$-velocity `U_X`, uncheck **Use Index for X Axis**, and set **X Array Name** to `Points_Y` so velocity is plotted over the $$y$$-coordinate. Increasing the Line Thickness (e.g. to 5) improves readability; line colour, title and axis labels can be adjusted as desired.

![Diffuser paraview plot over line menu](figures/paraview-menu-plot-over-line-clean.png)

The resulting diagram should look like follows:

![Diffuser paraview velocity profile](figures/diffuser-results-velocity-profile.png)



## Validating the Results

Experimental measurements for this case are provided in `velocity_profile.csv` in the `experimental_data` directory, containing three columns: row ID, velocity in m/s, and $$y$$-coordinate. Load it via **File** $$\rightarrow$$ **Open**, confirm the **CSV Reader**, and click **Apply**.

In order to add the experimental data to existing plot show the `velocity_profile.csv` entry in the diagram, set its **X Array Name** to the $$y$$-coordinate column, select only velocity, and display it as discrete points (**Line Style** $$\rightarrow$$ `None`, **Marker Style** $$\rightarrow$$ `Square`, **Marker Size** $$\rightarrow$$ 20).

![Diffuser paraview plot over line experiment menu](figures/paraview-menu-plot-over-line-experiment.png)

The resulting diagram should look like follows:

![Diffuser paraview velocity profile](figures/diffuser-results-velocity-profile-experiment.png)

These results confirms the huge discrepancy between the experimentally measured velocity profile and the numerically simulated one. First, no flow separation and thus recirculation is predicted by the numerical model. Second, the maximum flow velocity in $$x$$-direction is significantly underpredicted. This confirms the previous statement that the standard $$k-\epsilon$$ turbulence model is a poor choice for this flow problem.


## Conclusion

This concludes the fifth seminar on the simulation of an incompressible, turbulent flow through a diffuser. A two-dimensional mesh was imported using `fluentMeshToFoam` and its quality was verified with `checkMesh`. The boundary conditions were adjusted for the standard $$k-\epsilon$$ turbulence model. The simulation was then run using the solver `incompressibleFluid`, residuals were monitored, and dimensionless wall distance $$y^+$$ and wall shear stress evaluated. Finally, the flow field was visualized in ParaView and the velocity profile within the diffuser compared with experimental measurements revealing a significant modelling error due to the turbulence model.