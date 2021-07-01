---
layout: operator
title: assignUV
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignUV
redirect_from:
  - /reference/opType/raytk.operators.filter.assignUV/
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
    label: UV Field
    name: uv_field_in
    returnTypes:
    - vec4
  name: assignUV
  opType: raytk.operators.filter.assignUV
  parameters:
  - label: Enable
    name: Enable
  - label: UV Mode
    menuOptions:
    - label: XYZ
      name: xyz
    - label: XY
      name: xy
    - label: YX
      name: yx
    - label: YZ
      name: yz
    - label: ZY
      name: zy
    - label: XZ
      name: xz
    - label: ZX
      name: zx
    - label: Cylindrical X
      name: cylindricalx
    - label: Cylindrical Y
      name: cylindricaly
    - label: Cylindrical Z
      name: cylindricalz
    - label: Spherical
      name: spherical
    name: Uvmode
  status: beta

---
