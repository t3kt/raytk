---
layout: operator
title: spiralSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/spiralSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.spiralSdf/
op:
  name: spiralSdf
  summary: A tapering spiral squared tube.
  detail: |
    Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.
  opType: raytk.operators.sdf.spiralSdf
  category: sdf
  inputs:
    - name: definition_in_1
      label: Cross Section Shape
      required: false
      summary: |
        2D SDF used as the cross section shape of the arms instead of the default rounded square.
  parameters:
    - name: Enable
      label: Enable
    - name: Branches
      label: Branches
      summary: |
        The number of arms of the spiral. Fractional values will produce a discontinuity.
    - name: Bend
      label: Bend
      summary: |
        The tightness and direction of the spiral. Positive values are counterclockwise and negative are clockwise.
    - name: Twist
      label: Twist
      summary: |
        Twists the arms of the spiral while keeping their path the same.
    - name: Thickness
      label: Thickness
      summary: |
        Thickness of the arms of the spiral.
    - name: Exponent
      label: Exponent
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# spiralSdf

Category: sdf



A tapering spiral squared tube.

Based on [Spiral Tiling](https://www.shadertoy.com/view/ls2GRz) by Knightly.