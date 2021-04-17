---
layout: operator
title: coordTo2D
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/coordTo2D
redirect_from:
  - /reference/opType/raytk.operators.convert.coordTo2D/
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
  name: coordTo2D
  opType: raytk.operators.convert.coordTo2D
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
