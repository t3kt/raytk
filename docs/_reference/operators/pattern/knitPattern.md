---
layout: operator
title: knitPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/knitPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.knitPattern/
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
  name: knitPattern
  opType: raytk.operators.pattern.knitPattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Texture Amount
    name: Texamount
  - label: Texture Density
    name: Texdensity
  status: beta
  thumb: assets/images/reference/operators/pattern/knitPattern_thumb.png

---
