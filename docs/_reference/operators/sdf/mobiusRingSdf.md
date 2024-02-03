---
layout: operator
title: mobiusRingSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mobiusRingSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mobiusRingSdf/
op:
  category: sdf
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    summary: Value field that can be used to vary the thickness of the ring.
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
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the ring.
  keywords:
  - mobius
  - ring
  - twist
  name: mobiusRingSdf
  opType: raytk.operators.sdf.mobiusRingSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the ring.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The radius of the ring as a whole.
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The thickness of the ring.
  - label: Rounding
    name: Rounding
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The amount of rounding applied to the edges of the ring.
  - label: Twist
    name: Twist
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The number of times to twist the ring. Fractional numbers will create
      a discontinuity in the ring where it starts/ends.
  - label: Twist Phase
    name: Twistphase
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shift applied to the twisting of the ring.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: SDF for a squared mobius ring, which is like a rectangular bar twisted
    and then bent into a ring.
  thumb: assets/images/reference/operators/sdf/mobiusRingSdf_thumb.png
  variables:
  - label: angle
    name: angle
  - label: normangle
    name: normangle

---


SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.