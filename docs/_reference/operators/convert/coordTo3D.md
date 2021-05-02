---
layout: operator
title: coordTo3D
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/coordTo3D
redirect_from:
  - /reference/opType/raytk.operators.convert.coordTo3D/
op:
  category: convert
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: coordTo3D
  opType: raytk.operators.convert.coordTo3D
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - label: Custom
      name: custom
    - label: XY Plane
      name: xy
    - label: YX Plane
      name: yx
    - label: YZ Plane
      name: yz
    - label: ZY Plane
      name: zy
    - label: XZ Plane
      name: xz
    - label: ZX Plane
      name: zx
    name: Mode
  - label: Part X
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Partx
  - label: Part Y
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Party
  - label: Plane Offset
    name: Planeoffset
  - label: Part Z
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Zero
      name: zero
    name: Partz

---
