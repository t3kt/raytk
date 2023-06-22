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
    - vec4
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
    - label: X / Red
      name: x
    - label: Y / Green
      name: y
    - label: Z / Blue
      name: z
    - label: W / Alpha
      name: w
    - label: Length(XY)
      name: lengthxy
    - description: Use the length of the XYZ part of the vector.
      label: Length(XYZ)
      name: lengthxyz
    - description: Use the length of all 4 parts of the vector.
      label: Length(XYZW)
      name: lengthxyzw
    - label: Minimum(XY)
      name: minxy
    - label: Minimum(XYZ)
      name: minxyz
    - label: Minimum(XYZW)
      name: minxyzw
    - label: Maximum(XY)
      name: maxxy
    - label: Maximum(XYZ)
      name: maxxyz
    - label: Maximum(XYZW)
      name: maxxyzw
    - label: Average(XY)
      name: avgxy
    - label: Average(XYZ)
      name: avgxyz
    - label: Average(XYZW)
      name: avgxyzw
    - label: Hue
      name: hue
    - label: Saturation
      name: sat
    - label: Value
      name: val
    - label: Luminance
      name: luma
    - label: Sum(XY)
      name: sumxy
    - label: Sum(XYZ)
      name: sumxyz
    - label: Sum(XYZW)
      name: sumxyzw
    name: Usepart
    summary: Which part of the vector to use for the float field.
  summary: Converts a vector value field to a float field using one part of the vector.

---


Converts a vector value field to a float field using one part of the vector.