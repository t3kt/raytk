---
layout: operator
title: limitField
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitField
redirect_from:
  - /reference/opType/raytk.operators.filter.limitField/
op:
  category: filter
  inputs:
  - contextTypes:
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
  name: limitField
  opType: raytk.operators.filter.limitField
  parameters:
  - label: Enable
    name: Enable
  - label: Limit Type
    menuOptions:
    - label: 'Off'
      name: 'off'
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    - label: Zig-Zag
      name: zigzag
    name: Limittype
  - label: Input Low
    name: Low
  - label: Input High
    name: High

---
