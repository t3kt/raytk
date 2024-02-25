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
    - VertexContext
    - PixelContext
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
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of arms of the spiral. Fractional values will produce a discontinuity.
  - label: Bend
    name: Bend
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The tightness and direction of the spiral. Positive values are counterclockwise
      and negative are clockwise.
  - label: Twist
    name: Twist
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Twists the arms of the spiral while keeping their path the same.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the arms of the spiral.
  - label: Exponent
    name: Exponent
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: A tapering spiral squared tube.
  thumb: assets/images/reference/operators/sdf/spiralSdf_thumb.png

---


A tapering spiral squared tube.

Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.