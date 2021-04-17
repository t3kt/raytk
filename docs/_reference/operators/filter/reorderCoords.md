---
layout: operator
title: reorderCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reorderCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.reorderCoords/
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
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: reorderCoords
  opType: raytk.operators.filter.reorderCoords
  parameters:
  - label: Enable
    name: Enable
  - label: X Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axisx
    summary: Which axis should be used as the new X axis.
  - label: Y Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axisy
    summary: Which axis should be used as the new Y axis.
  - label: Z Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axisz
    summary: Which axis should be used as the new Z axis.
  summary: Swaps axes for the input.

---


Swaps axes for the input.