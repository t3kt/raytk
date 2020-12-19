---
layout: page
title: gridSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gridSdf
---

# gridSdf

Category: sdf



An infinite grid shape, along two axes.

## Parameters

* `Coordtype` *Coord Type*: allows the shape to be used in a 2D context.
  * `vec2` *2D*
  * `vec3` *3D*
* `Crosssectionshape` *Cross Section Shape*: choose the shape of the bars of the grid. Not available in 2D mode.
  * `circle` *Circle*
  * `diamond` *Diamond*
* `Axis` *Axis*: choose which axis the grid should face.
  * `x` *X*
  * `y` *Y*
  * `z` *Z*
* `Spacing` *Spacing*: spacing between the bars of the grid. If this value is very small and the `Thickness` is high enough, the bars can merge into a solid surface. But if it is set to zero the grid will disappear due to a calculation error.
* `Axisoffset` *Axis Offset*: shifts the grid forwards or backwards along the `Axis` that it is facing. Not available in 2D mode.
* `Offset` *Offset*: shifts the grid along its plane.
* `Thickness` *Thickness*: the thickness of the bars.
* `Contexttype` *Context Type*: advanced parameter that should usually just be set to `Context`
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Inspect` *Inspect*