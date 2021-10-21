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
    - Particle
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
  status: beta
  summary: Applies rotation to the surface normals used by material elements such
    as `specularContrib`.

---


Applies rotation to the surface normals used by material elements such as `specularContrib`.