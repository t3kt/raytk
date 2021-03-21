---
layout: operator
title: sweep
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/sweep
redirect_from:
  - /reference/opType/raytk.operators.convert.sweep/
op:
  category: convert
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: First 2D SDF
    name: sdf_definition_in_1
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Second 2D SDF
    name: sdf_definition_in_2
    required: true
    returnTypes:
    - float
    - Sdf
  name: sweep
  opType: raytk.operators.convert.sweep
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
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
    name: Plane

---
