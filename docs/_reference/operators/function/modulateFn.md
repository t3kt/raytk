---
layout: operator
title: modulateFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/modulateFn
redirect_from:
  - /reference/opType/raytk.operators.function.modulateFn/
op:
  category: function
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
    label: Function
    name: definition_in
    required: true
    returnTypes:
    - float
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
    - float
    - vec2
    - vec3
    - vec4
    label: Modulating Function
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
  name: modulateFn
  opType: raytk.operators.function.modulateFn
  parameters:
  - label: Enable
    name: Enable
  status: beta

---
