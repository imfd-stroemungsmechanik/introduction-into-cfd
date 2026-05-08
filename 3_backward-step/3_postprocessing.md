---
layout: default
title: Post-Processing
parent: 3. Backward-Step
nav_order: 3
---

# Post-Processing

## Visualizing the Velocity Contour

As soon as results are written to time directories, they can be viewed using ParaView. Start ParaView in the background with the following command:

```bash
paraFoam &
```
To prepare ParaView to display the data of interest, the data at the final time step of 1 second must be loaded. If the case was run while ParaView was open, the output data in time directories will not be automatically loaded within ParaView. To load the data, click **Refresh** at the top of the **Properties** panel (scroll up the panel if necessary).

To view the solution at the last time step of $$t = 1\,\text{s}$$, use the **VCR Controls** at the very top of the ParaView window and click the button for **Last Frame**.

![Backward-facing step paraview vcr controls](figures/paraview-menu-VCR-controls.png)



## Coloring Surfaces by Flow Property

To color the mesh by velocity magnitude (i.e. the velocity contour) of the flow, select the following settings in the **Properties** panel, as described in the following figure:
1. Select **Surface** from the **Representation** menu,
2. Select **Coloring** by velocity magnitude U at the cell centers, and
3. Select **Rescale to Data Range**, if necessary.

![Backward-facing step paraview velocity contour settings](figures/paraview-menu-velocity-contour-settings.png)

The velocity field looks as expected: The velocity magnitude at the inlet is about  $$1\,\text{m/s}$$. The flow separates at the step corner and there is a recirculation zone immediately downstream of the step. The flow reattaches to the bottom wall further downstream, after which a recovery region follows. The typical reattachment length is 6-8 step heights for a Reynolds number of 1250.




![Backward-facing step paraview velocity contour](figures/paraview-results-velocity-contour.png)

A colour legend can be added by clicking the **Toggle Color Legend Visibility** button in the **Active Variable Controls** toolbar. The legend can be repositioned in the image window by drag and drop with the mouse.

![Backward-facing step paraview variable controls](figures/paraview-menu-variable_controls.png)

The **Edit Color Map** button in the **Active Variable Controls** toolbar opens the **Color Map Editor** window, where various attributes of the colour scale and the color bar can be adjusted.

![Backward-facing step paraview color bar settings](figures/paraview-menu-color-bar.png)

ParaView defaults to using a colour scale of blue to white to red rather than the more common blue to green to red (rainbow). Therefore, you may wish to change the colour scale. This can be done by selecting the **Choose Preset** button (with the heart icon) in the **Color Map Editor**. The conventional color scale for CFD is Blue to Red Rainbow, which can be found by typing the name in the **Search** bar.

After selecting Blue to Red Rainbow and clicking **Apply** and **Close**, click the **Save as Default** button at the absolute bottom of the panel (file save symbol) so that ParaView will always adopt this type of colour bar. You can also edit the color legend properties, such as text size, font selection and numbering format for the scale, by clicking the **Edit Color Legend Properties** to the far right of the search bar, as shown in the figure above.


## Cutting Plane (Slice)

When rotating the image by holding down the left mouse button in the image window and moving the cursor, you can see that the complete geometry surface is coloured by the velocity. In order to produce a genuine 2-dimensional contour plot, first create a cutting plane, or *slice*. With the `backward-step.foam` module highlighted in the **Pipeline Browser**, select the **Slice** filter from **Common Data and Analytics** in the top menu of ParaView:

![Backward-facing step paraview common analytics](figures/paraview-menu-common_analytics.png)


The cutting plane should be centred at $$(0, 0, 0)$$ and its normal should be set to $$(0, 0, 1)$$ (click the **Z Normal** button). By default, the pressure field will now be shown. Disable **Show Plane** in the **Properties** panel as otherwise rotating the image with the mouse might change the plane orientation.


## Vector Plot (Glyph)

We now wish to generate a vector glyph for velocity at the cutting plane. With the `slice1` module highlighted in the **Pipeline Browser**, select the **Glyph** filter from the **Common Data and Analytics** menu. The **Properties** panel should appear as shown in the following figure:

![Backward-facing step paraview glyph menu](figures/paraview-menu-glyph.png)


In the resulting **Properties** panel, make sure the **Glyph Type** is set to **Arrow**, and the **Orientation Array** is the velocity field `U`. Then, set the **Scale Array** to `U` and **Vector Scale Mode** to **Scale by Magnitude**. This way, the size of the vectors will be scaled by the velocity magnitude. With a **Scaling Factor** of 0.01, the vectors will be clearly visible. At this point, click **Apply** to show the vector plot on top of the cutting plane defined previously.

The resulting vectors will be color coded by pressure, whereas a velocity color code would make much more sense. Therefore, colour the glyphs by velocity magnitude by setting **Color by** `U` in the **Properties** panel. Also select **Show Color Legend** in **Edit Color Map**. Additionally, the `slice1` module in the **Pipeline Browser** can be made invisible by clicking the **Eye** symbol next to the module name. The resulting output is shown in the following figure:

![Backward-facing step paraview vector plot](figures/paraview-results-glyph-plot.png)


## Velocity Animation

A good way to visualize the transient flow behaviour is an animation created with ParaView. For this, hide the vector plot and show the cut plane of the velocity magnitude. Then display the velocity magnitude in a range from $$(0 - 1.2) \, \text{m/s}$$. By clicking the **Play** button at the **VCR Controls** at the very top, it is possible to automatically go through every time step and see what the transient flow field looks like:

![Backward-facing step paraview velocity animation](figures/paraview-results-animation.gif)

Before creating an animation, it is recommended to add more information to the view. First, add a title by clicking on the top menu: **Sources** $$\rightarrow$$ **Annotations** $$\rightarrow$$ **Text**. Type any text in the text field inside the **Properties** panel and adjust font size and location of the text field. Second, add the current time step to the view by using the top menu: **Sources** $$\rightarrow$$ **Annotations** $$\rightarrow$$ **Annotate Time**. Choose a suitable time **Format**, such as `Time: {time:1.2f} s` to display the time with two digits and the unit in seconds. All in all, this could look like follows:

![Backward-facing step paraview velocity animation](figures/paraview-results-velocity-annotation.png)

At this point, the animation can easily be created by clicking the top menu: **File** $$\rightarrow$$ **Save Animation...**, and choosing a suitable file name and format (preferably mp4 or avi). In the following **Animation Menu**, specify video resolution, compression, and frame rate. It is recommended to change the frame rate to a higher value, such as 10 - 15. Clicking **Okay** will create the animation.

![Backward-facing step paraview vector plot](figures/paraview-menu-animation-panel.png)


## Conclusion


This concludes the second seminar on the simulation of incompressible, laminar flow over a backward-facing step. A two-dimensional mesh was generated using `blockMesh`. The fluid properties were adjusted to match a specified Reynolds number, and the time step size was chosen to maintain an appropriate Courant number. The simulation was then run using the solver `incompressibleFluid`, and residuals as well as maximum velocity were plotted. Finally, the flow field was visualized in ParaView.