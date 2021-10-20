---
layout: operator
title: brickPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/brickPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.brickPattern/
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
  name: brickPattern
  opType: raytk.operators.pattern.brickPattern
  parameters:
  - label: Shift
    name: Shift
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending

---
