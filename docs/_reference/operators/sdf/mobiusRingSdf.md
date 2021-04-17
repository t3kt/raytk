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
    coordTypes:
    - float
    - vec3
    label: Thickness Field
    name: thickness_field_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the thickness of the ring. A 1D
      field will use the angle of the ring as the coordinate, scaled to a 0..1 range.
      A 3D field will use the absolute XYZ coordinates.
  name: mobiusRingSdf
  opType: raytk.operators.sdf.mobiusRingSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Translate
    name: Translate
    summary: Moves the center of the ring.
  - label: Radius
    name: Radius
    summary: The radius of the ring as a whole.
  - label: Thickness
    name: Thickness
    summary: The thickness of the ring.
  - label: Rounding
    name: Rounding
    summary: The amount of rounding applied to the edges of the ring.
  - label: Twist
    name: Twist
    summary: The number of times to twist the ring. Fractional numbers will create
      a discontinuity in the ring where it starts/ends.
  - label: Twist Phase
    name: Twistphase
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

---


SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.