---
layout: operator
title: rotate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rotate
redirect_from:
  - /reference/opType/raytk.operators.filter.rotate/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotate_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Pivot Field
    name: pivot_definition_in
    returnTypes:
    - vec4
  name: rotate
  opType: raytk.operators.filter.rotate
  parameters:
  - label: Enable
    name: Enable
  - label: Rotate Mode
    menuOptions:
    - label: Axis
      name: axis
    - label: Euler
      name: euler
    name: Rotatemode
  - label: Axis
    name: Axis
  - label: Rotate
    name: Rotate
  - label: Rotate Order
    menuOptions:
    - label: Rx Ry Rz
      name: xyz
    - label: Rx Rz Ry
      name: xzy
    - label: Ry Rx Rz
      name: yxz
    - label: Ry Rz Rx
      name: yzx
    - label: Rz Rx Ry
      name: zxy
    - label: Rz Ry Rx
      name: zyx
    name: Rord
  - label: Rotate XYZ
    name: Rot
  - label: Use Pivot
    name: Usepivot
  - label: Pivot
    name: Pivot

---
