---
layout: page
title: spiralSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/spiralSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.spiralSdf/
---

# spiralSdf

Category: sdf



A tapering spiral squared tube.

Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.

## Parameters

* `Enable` *Enable*
* `Branches` *Branches*: The number of arms of the spiral. Fractional values will produce a discontinuity.
* `Bend` *Bend*: The tightness and direction of the spiral. Positive values are counterclockwise and negative are clockwise.
* `Twist` *Twist*: Twists the arms of the spiral while keeping their path the same.
* `Thickness` *Thickness*: Thickness of the arms of the spiral.
* `Exponent` *Exponent*
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1` *Cross Section Shape*:  2D SDF used as the cross section shape of the arms instead of the default rounded square.