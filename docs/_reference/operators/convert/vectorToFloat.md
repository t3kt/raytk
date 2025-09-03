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
    - VertexContext
    - PixelContext
    - PopContext
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
    - description: Use the length of the XY parts of the vector.
      label: Length(XY)
      name: lengthxy
    - description: Use the length of the XYZ parts of the vector.
      label: Length(XYZ)
      name: lengthxyz
    - description: Use the length of all 4 parts of the vector.
      label: Length(XYZW)
      name: lengthxyzw
    - description: Minimum of the X and Y.
      label: Minimum(XY)
      name: minxy
    - description: Minimum of the X, Y, and Z.
      label: Minimum(XYZ)
      name: minxyz
    - description: Minimum of all 4 parts.
      label: Minimum(XYZW)
      name: minxyzw
    - description: Maximum of the X and Y.
      label: Maximum(XY)
      name: maxxy
    - description: Maximum of the X, Y, and Z.
      label: Maximum(XYZ)
      name: maxxyz
    - description: Maximum of all 4 parts.
      label: Maximum(XYZW)
      name: maxxyzw
    - description: Average of X and Y.
      label: Average(XY)
      name: avgxy
    - description: Average of X, Y, and Z.
      label: Average(XYZ)
      name: avgxyz
    - description: Average of all 4 parts.
      label: Average(XYZW)
      name: avgxyzw
    - description: Treat the vector as an RGB color and get the hue.
      label: Hue
      name: hue
    - description: Treat the vector as an RGB color and get the saturation.
      label: Saturation
      name: sat
    - description: Treat the vector as an RGB color and get the value (as in HSV).
      label: Value
      name: val
    - description: Treat the vector as an RGB color and get the luminance.
      label: Luminance
      name: luma
    - description: Add the X and Y parts.
      label: Sum(XY)
      name: sumxy
    - description: Add the X, Y, and Z parts.
      label: Sum(XYZ)
      name: sumxyz
    - description: Add all 4 parts.
      label: Sum(XYZW)
      name: sumxyzw
    name: Usepart
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which part of the vector to use for the float field.
  summary: Converts a vector value field to a float field, e.g. using one part of
    the vector.

---


Converts a vector value field to a float field, e.g. using one part of the vector.