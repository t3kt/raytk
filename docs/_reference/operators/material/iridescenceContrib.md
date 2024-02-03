---
layout: operator
title: iridescenceContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/iridescenceContrib
redirect_from:
  - /reference/opType/raytk.operators.material.iridescenceContrib/
op:
  category: material
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Phase
    name: phaseField
    returnTypes:
    - float
    summary: Field that offsets the phase of the color pattern.
  name: iridescenceContrib
  opType: raytk.operators.material.iridescenceContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Level
    name: Level
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Overall brightness.
  - label: Phase
    name: Phase
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts the color pattern around the range of surface angles.
  - label: Period
    name: Period
    readOnlyHandling: macro
    regularHandling: runtime
    summary: How wide the rainbow series is spread across the range of angles. A period
      of 0.5 will repeat the pattern twice and a period of 2 will only go through
      half the range before jumping back to the start value.
  - label: Spread
    name: Spread
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The range from the edge where the color is applied, as a 0..1 ratio of
      how much the surface is facing the camera. The first number is the start of
      the faded range and the second is the end of it (the place where the color is
      at full brightness).
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: macro
    regularHandling: macro
    summary: Whether shadows should be applied to the color.
  status: beta
  summary: Shading element that produces a rainbow pattern around the edges of shapes,
    depending on which direction the surface is facing (the surface normal).
  thumb: assets/images/reference/operators/material/iridescenceContrib_thumb.png

---


Shading element that produces a rainbow pattern around the edges of shapes, depending on which direction the surface is facing (the surface normal).