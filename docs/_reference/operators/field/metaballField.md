---
layout: page
title: metaballField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/metaballField
redirect_from:
  - /reference/opType/raytk.operators.field.metaballField/
---

# metaballField

Category: field



Metaball value field.

## Parameters

* `Coordtype` *Coord Type*
  * `float` *1D*
  * `vec2` *2D*
  * `vec3` *3D*
* `Center` *Center*: Center position of the ball.
* `Radius` *Radius*: Radius of the ball on each axis. In 2D mode, only x and y are used. In 1D only x is used.
* `Radiusscale` *Radius Scale*: Scales the radius on all axes.
* `Weight` *Weight*: The returned values are multiplied by this.
* `Exponent` *Exponent*: Controls the shape of the ball by applying exponential scaling to coordinates.
* `Contexttype` *Context Type*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
  * `RayContext` *Ray Context*
* `Inspect` *Inspect*
* `Help` *Help*