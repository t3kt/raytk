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
    - VertexContext
    - PixelContext
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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
  name: weavePattern
  opType: raytk.operators.pattern.weavePattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/weavePattern_thumb.png

---
