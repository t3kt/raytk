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
    summary: Optional field that can provide alternative coordinates instead of using
      the raw X/Y position.
  name: checkerPattern
  opType: raytk.operators.pattern.checkerPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Checkerboard pattern with alternating black and white rectangles.
  thumb: assets/images/reference/operators/pattern/checkerPattern_thumb.png

---


Checkerboard pattern with alternating black and white rectangles.