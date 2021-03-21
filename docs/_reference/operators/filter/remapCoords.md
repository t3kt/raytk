---
layout: operator
title: remapCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/remapCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.remapCoords/
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
    - Ray
    - Light
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
    label: Coordinate Field
    name: coord_field_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: remapCoords
  opType: raytk.operators.filter.remapCoords
  parameters:
  - label: Enable
    name: Enable
  - label: Remap Mode
    menuOptions:
    - label: Replace
      name: replace
    - label: Add
      name: add
    - label: Multiply
      name: multiply
    name: Remapmode
  - label: Mix
    name: Mix
  status: beta

---
