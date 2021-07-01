---
layout: operator
title: assignColor
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignColor
redirect_from:
  - /reference/opType/raytk.operators.filter.assignColor/
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
    - Sdf
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
    label: Color Field
    name: color_field_in
    returnTypes:
    - float
    - vec4
  name: assignColor
  opType: raytk.operators.filter.assignColor
  parameters:
  - label: Enable
    name: Enable
  - label: Color
    name: Color
  status: beta

---
