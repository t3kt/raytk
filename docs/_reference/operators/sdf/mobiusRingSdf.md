---
layout: page
title: mobiusRingSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mobiusRingSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mobiusRingSdf/
---

# mobiusRingSdf

Category: sdf



SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.

## Parameters

* `Enable` *Enable*
* `Translate` *Translate*: Moves the center of the ring.
* `Radius` *Radius*: The radius of the ring as a whole.
* `Thickness` *Thickness*: The thickness of the ring.
* `Rounding` *Rounding*: The amount of rounding applied to the edges of the ring.
* `Twist` *Twist*: The number of times to twist the ring. Fractional numbers will create a discontinuity in the ring where it starts/ends.
* `Twistphase` *Twist Phase*: Shift applied to the twisting of the ring.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `thickness_field_definition_in` *Thickness Field*:  Value field that can be used to vary the thickness of the ring. A 1D field will use the angle of the ring as the coordinate, scaled to a 0..1 range. A 3D field will use the absolute XYZ coordinates.