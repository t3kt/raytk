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
* `Function` *Wave*: The type of wave.
  * `sin` *Sine*
  * `cos` *Cosine*
  * `tri` *Triangle*
  * `ramp` *Ramp*
  * `square` *Square*
* `Axis` *Axis*: If there is no input, the coordinate along this axis is used for the wave function phase.
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
* `Period` *Period*: The length of a single cycle of the wave.
* `Phase` *Phase*: Offset of the wave along the axis / coordinates.
* `Amplitude` *Amplitude*: The height of the wave, which scales the range of output values. If this is set to 3 (and `Offset` is 0), a ramp wave will produce values from 0 to 3.
* `Offset` *Offset*: Adds to the values produced by the wave. If this is set to 0.5 (and `Amplitude` is set to 1), a ramp wave will produce values from 0.5 to 1.5.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in` *Wave Coordinate Source*:  If attached, the wave will use this to determine the numbers that it passes to the wave function (instead of using the position along the chosen `Axis`).