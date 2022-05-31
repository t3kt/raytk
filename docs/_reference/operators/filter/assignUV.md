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
  detail: Coordinates can either be determined using the selected `UV Mode`, or using
    a vector field input.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    summary: SDF definition to which the UVs are applied.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: UV Field
    name: uvField
    returnTypes:
    - vec4
    summary: Optional field used to calculate the UV coordinates.
  keywords:
  - material
  - modularmat
  - surface
  - texture
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
  - label: Center
    name: Center
  summary: Assigns UV coordinates to an SDF surface.
  thumb: assets/images/reference/operators/filter/assignUV_thumb.png
  variables:
  - label: sdf
    name: sdf

---


Assigns UV coordinates to an SDF surface.

Coordinates can either be determined using the selected `UV Mode`, or using a vector field input.