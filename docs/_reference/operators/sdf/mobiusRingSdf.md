---
layout: operator
title: mobiusRingSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mobiusRingSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mobiusRingSdf/
op:
  name: mobiusRingSdf
  summary: |
    SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.
  opType: raytk.operators.sdf.mobiusRingSdf
  category: sdf
  inputs:
    - name: thickness_field_definition_in
      label: Thickness Field
      required: false
      summary: |
        Value field that can be used to vary the thickness of the ring. A 1D field will use the angle of the ring as the coordinate, scaled to a 0..1 range. A 3D field will use the absolute XYZ coordinates.
  parameters:
    - name: Enable
      label: Enable
    - name: Translate
      label: Translate
      summary: |
        Moves the center of the ring.
    - name: Radius
      label: Radius
      summary: |
        The radius of the ring as a whole.
    - name: Thickness
      label: Thickness
      summary: |
        The thickness of the ring.
    - name: Rounding
      label: Rounding
      summary: |
        The amount of rounding applied to the edges of the ring.
    - name: Twist
      label: Twist
      summary: |
        The number of times to twist the ring. Fractional numbers will create a discontinuity in the ring where it starts/ends.
    - name: Twistphase
      label: Twist Phase
      summary: |
        Shift applied to the twisting of the ring.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# mobiusRingSdf

Category: sdf



SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.