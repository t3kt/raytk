---
layout: operator
title: triangleCheckerPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/triangleCheckerPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.triangleCheckerPattern/
op:
  category: pattern
  detail: This pattern produces just float values not colors. To apply color to it,
    pass it into a `colorRampField`.
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
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  name: triangleCheckerPattern
  opType: raytk.operators.pattern.triangleCheckerPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  summary: Triangular grid checkerboard pattern.
  thumb: assets/images/reference/operators/pattern/triangleCheckerPattern_thumb.png

---


Triangular grid checkerboard pattern.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.