---
layout: operator
title: spiralPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/spiralPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.spiralPattern/
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
  name: spiralPattern
  opType: raytk.operators.pattern.spiralPattern
  parameters:
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Spin
    name: Spin
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/spiralPattern_thumb.png

---
