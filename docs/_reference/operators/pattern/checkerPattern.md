---
layout: operator
title: checkerPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/checkerPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.checkerPattern/
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  name: checkerPattern
  opType: raytk.operators.pattern.checkerPattern
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
  summary: Checkerboard pattern with alternating black and white rectangles.
  thumb: assets/images/reference/operators/pattern/checkerPattern_thumb.png

---


Checkerboard pattern with alternating black and white rectangles.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.