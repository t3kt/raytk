---
layout: operator
title: waveGreekFriezePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/waveGreekFriezePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.waveGreekFriezePattern/
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
    label: Twist Field
    name: twistField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - twistField
  name: waveGreekFriezePattern
  opType: raytk.operators.pattern.waveGreekFriezePattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Twist
    name: Twist
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/waveGreekFriezePattern_thumb.png

---
