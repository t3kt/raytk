---
layout: page
title: gridSdf (sdf)
---

An infinite grid shape, along two axes.

* `Coord Type` - allows the shape to be used in a 2D context.
* `Cross Section Shape` - choose the shape of the bars of the grid. Not available in 2D mode.
* `Axis` - choose which axis the grid should face.
* `Spacing` - spacing between the bars of the grid. If this value is very small and the `Thickness` is high enough, the bars can merge into a solid surface. But if it is set to zero the grid will disappear due to a calculation error.
* `Axis Offset` - shifts the grid forwards or backwards along the `Axis` that it is facing. Not available in 2D mode.
* `Offset` - shifts the grid along its plane.
* `Thickness` - the thickness of the bars.
* `Context Type` - advanced parameter that should usually just be set to `Context`
