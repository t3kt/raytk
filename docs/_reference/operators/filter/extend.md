---
layout: operator
title: extend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/extend
redirect_from:
  - /reference/opType/raytk.operators.filter.extend/
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
    - Ray
    - Light
  name: extend
  opType: raytk.operators.filter.extend
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
  - label: Size
    name: Size

---
