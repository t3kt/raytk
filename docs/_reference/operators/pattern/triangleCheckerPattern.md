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
  name: triangleCheckerPattern
  opType: raytk.operators.pattern.triangleCheckerPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/triangleCheckerPattern_thumb.png

---
