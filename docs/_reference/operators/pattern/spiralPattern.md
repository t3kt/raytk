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
  - label: Scale
    name: Scale
  - label: Spin
    name: Spin
  thumb: assets/images/reference/operators/pattern/spiralPattern_thumb.png

---
