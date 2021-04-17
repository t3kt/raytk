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

---
