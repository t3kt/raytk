---
layout: operator
title: hexagonalTruchetPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalTruchetPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalTruchetPattern/
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
  name: hexagonalTruchetPattern
  opType: raytk.operators.pattern.hexagonalTruchetPattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Default (FabriceNeyret2)
      name: default
    - label: Variant 1 (Shane)
      name: variant1
    - label: Variant 2 (Shane)
      name: variant2
    name: Pattern
    readOnlyHandling: baked
    regularHandling: baked
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/hexagonalTruchetPattern_thumb.png

---
