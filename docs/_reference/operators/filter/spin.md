---
layout: operator
title: spin
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/spin
redirect_from:
  - /reference/opType/raytk.operators.filter.spin/
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
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  keywords:
  - rotate
  - spin
  name: spin
  opType: raytk.operators.filter.spin
  parameters:
  - label: Enable
    name: Enable
  - label: Play
    name: Play
  - label: Spin Speed
    name: Spinspeed
  - label: Speed
    name: Speedmult
  - label: Reset
    name: Reset
  - label: Reset
    name: Resetpulse
  - label: Base Rotation
    name: Rotate
  - label: Use Pivot
    name: Usepivot
  - label: Pivot
    name: Pivot
  status: beta

---
