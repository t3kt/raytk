---
layout: operator
title: weavePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/weavePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.weavePattern/
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
    coordTypes:
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  name: weavePattern
  opType: raytk.operators.pattern.weavePattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  thumb: assets/images/reference/operators/pattern/weavePattern_thumb.png

---
