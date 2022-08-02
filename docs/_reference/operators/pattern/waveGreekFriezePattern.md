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
    label: Twist Field
    name: twistField
    returnTypes:
    - float
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
  name: waveGreekFriezePattern
  opType: raytk.operators.pattern.waveGreekFriezePattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Twist
    name: Twist
  - label: Blending
    name: Blending
  status: beta
  thumb: assets/images/reference/operators/pattern/waveGreekFriezePattern_thumb.png

---
