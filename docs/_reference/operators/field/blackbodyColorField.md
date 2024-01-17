---
layout: operator
title: blackbodyColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/blackbodyColorField
redirect_from:
  - /reference/opType/raytk.operators.field.blackbodyColorField/
op:
  category: field
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
    - float
    - vec2
    - vec3
    - vec4
    label: Temperature Field
    name: tempField
    required: true
    returnTypes:
    - float
  name: blackbodyColorField
  opType: raytk.operators.field.blackbodyColorField
  parameters:
  - label: Temperature
    name: Temp
  - label: Temperature Unit
    menuOptions:
    - label: Normalized (0..1)
      name: norm
    - label: Degrees Kelvin
      name: deg
    name: Tempunit
  - label: Exponent
    name: Exp
  thumb: assets/images/reference/operators/field/blackbodyColorField_thumb.png

---
