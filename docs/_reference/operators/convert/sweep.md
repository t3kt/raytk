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
    label: Cross-Section SDF
    name: cross_section_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: The SDF that sweeps around the path SDF.
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Path SDF
    name: path_definition_in
    required: true
    returnTypes:
    - float
    - Sdf
    summary: The SDF around which the cross-section SDF sweeps.
  name: sweep
  opType: raytk.operators.convert.sweep
  parameters:
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
  - label: Enable
    name: Enable
  summary: Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D SDF.

---


Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D SDF.