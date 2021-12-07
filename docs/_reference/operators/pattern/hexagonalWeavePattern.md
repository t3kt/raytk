---
layout: operator
title: hexagonalWeavePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalWeavePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalWeavePattern/
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
  name: hexagonalWeavePattern
  opType: raytk.operators.pattern.hexagonalWeavePattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Two Layer
      name: twolayer
    name: Pattern
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  - label: Randomize
    name: Randomize
  - label: Seed
    name: Seed
  thumb: assets/images/reference/operators/pattern/hexagonalWeavePattern_thumb.png

---
