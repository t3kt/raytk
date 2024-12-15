---
layout: operator
title: rotateNormals
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rotateNormals
redirect_from:
  - /reference/opType/raytk.operators.filter.rotateNormals/
op:
  category: filter
  inputs:
  - contextTypes:
    - MaterialContext
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
    - Volume
    - Ray
    - Light
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
  keywords:
  - material
  - modularmat
  - normals
  - rotate
  - spin
  - transform
  name: rotateNormals
  opType: raytk.operators.filter.rotateNormals
  parameters:
  - label: Enable
    name: Enable
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
    name: Rotate
  summary: Applies rotation to the surface normals used by material elements such
    as `specularContrib`.

---


Applies rotation to the surface normals used by material elements such as `specularContrib`.