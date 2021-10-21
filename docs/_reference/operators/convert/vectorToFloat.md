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
    - description: Use the length of the XYZ part of the vector.
      label: Length(XYZ)
      name: lengthxyz
    - description: Use the length of all 4 parts of the vector.
      label: Length(XYZW)
      name: lengthxyzw
    name: Usepart
    summary: Which part of the vector to use for the float field.
  summary: Converts a vector value field to a float field using one part of the vector.

---


Converts a vector value field to a float field using one part of the vector.