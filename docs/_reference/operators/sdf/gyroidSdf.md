---
layout: page
title: gyroidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gyroidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.gyroidSdf/
---

# gyroidSdf

Category: sdf



Gyroid shape, which is an infinitely connected periodic surface.

The Gyroid is constructed using overlapping sine and cosine waves.
See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.

## Parameters

* `Coordtype` *Coord Type*: Switches between 2D and 3D gyroids.
  * `vec2` *2D*
  * `vec3` *3D*
* `Contexttype` *Context Type*: Advanced parameter that should usually just be set to `Context`.
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Translate` *Translate*: Moves the shape as a whole.
* `Scale` *Scale*: Spacing of the shape in each dimension.
* `Enableperiod` *Enable Period*: Whether to specify periods for the waves.
* `Period1` *Period 1*: Period of the first waves on each axis.
* `Period2` *Period 2*: Period of the second waves on each axis.
* `Enablephase` *Enable Phase*: Whether to specify phase shift for the waves.
* `Phase1` *Phase 1*: Phase shift of the first waves on each axis.
* `Phase2` *Phase 2*: Phase shift of the second waves on each axis.
* `Bias` *Bias*
* `Thickness` *Thickness*: Expands the surfaces producing thicker shapes.
* `Inspect` *Inspect*
* `Help` *Help*