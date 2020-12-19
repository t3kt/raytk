---
layout: page
title: waveField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/waveField
redirect_from:
  - /reference/opType/raytk.operators.field.waveField/
---

# waveField

Category: field



A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.

## Parameters

* `Enable` *Enable*
* `Function` *Wave*
  * `sin` *Sine*
  * `cos` *Cosine*
  * `tri` *Triangle*
  * `ramp` *Ramp*
  * `square` *Square*
* `Axis` *Axis*
  * `x` *X*
  * `y` *Y*
  * `z` *Z*
* `Coordtype` *Coord Type*
  * `float` *1D*
  * `vec2` *2D*
  * `vec3` *3D*
* `Contexttype` *Context Type*
  * `useinput` *Use Input*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Period` *Period*
* `Phase` *Phase*
* `Amplitude` *Amplitude*
* `Offset` *Offset*
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`