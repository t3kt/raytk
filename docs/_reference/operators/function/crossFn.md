---
layout: operator
title: crossFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/crossFn
redirect_from:
  - /reference/opType/raytk.operators.function.crossFn/
op:
  category: function
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: mix definition in
    name: mix_definition_in
    returnTypes:
    - float
    - vec4
  name: crossFn
  opType: raytk.operators.function.crossFn
  parameters:
  - label: Enable
    name: Enable
  - label: Mix
    name: Mix

---

# crossFn

Category: function

