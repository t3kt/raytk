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
    coordTypes:
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
  name: checkerPattern
  opType: raytk.operators.pattern.checkerPattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size

---
