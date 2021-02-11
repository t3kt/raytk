---
layout: operator
title: revolve
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/revolve
redirect_from:
  - /reference/opType/raytk.operators.convert.revolve/
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: revolve
  opType: raytk.operators.convert.revolve
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Radial Offset
    name: Radialoffset
  - label: Axis Offset
    name: Axisoffset

---

# revolve

Category: convert

