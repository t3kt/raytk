---
layout: operator
title: spiralSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/spiralSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.spiralSdf/
op:
  category: sdf
  detail: Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Cross Section Shape
    name: crossSection
    returnTypes:
    - float
    - Sdf
    summary: 2D SDF used as the cross section shape of the arms instead of the default
      rounded square.
  keywords:
  - coil
  - spiral
  - swirl
  name: spiralSdf
  opType: raytk.operators.sdf.spiralSdf
  parameters:
  - name: Enable
  - label: Branches
    name: Branches
    summary: The number of arms of the spiral. Fractional values will produce a discontinuity.
  - label: Bend
    name: Bend
    summary: The tightness and direction of the spiral. Positive values are counterclockwise
      and negative are clockwise.
  - label: Twist
    name: Twist
    summary: Twists the arms of the spiral while keeping their path the same.
  - label: Thickness
    name: Thickness
    summary: Thickness of the arms of the spiral.
  - label: Exponent
    name: Exponent
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: A tapering spiral squared tube.
  thumb: assets/images/reference/operators/sdf/spiralSdf_thumb.png

---


A tapering spiral squared tube.

Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.