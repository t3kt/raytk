---
layout: operator
title: quantizeValue
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quantizeValue
redirect_from:
  - /reference/opType/raytk.operators.filter.quantizeValue/
op:
  category: filter
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
    - Sdf
  name: quantizeValue
  opType: raytk.operators.filter.quantizeValue
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
  - label: Size Multiplier
    name: Sizemult
  - label: Offset
    name: Offset
  - label: Smoothing
    name: Smoothing
  - label: Smoothing Multiplier
    name: Smoothingmult
  status: beta

---
