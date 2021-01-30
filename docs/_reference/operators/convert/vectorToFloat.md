---
layout: operator
title: vectorToFloat
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/vectorToFloat
redirect_from:
  - /reference/opType/raytk.operators.convert.vectorToFloat/
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
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - vec4
  name: vectorToFloat
  opType: raytk.operators.convert.vectorToFloat
  parameters:
  - label: Enable
    name: Enable
  - label: Use Part
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: W
      name: w
    - label: Length(XYZ)
      name: lengthxyz
    - label: Length(XYZW)
      name: lengthxyzw
    name: Usepart

---

# vectorToFloat

Category: convert

