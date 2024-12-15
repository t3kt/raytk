---
layout: operator
title: stackSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/stackSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.stackSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Shape SDF
    name: shape
    returnTypes:
    - Sdf
    supportedVariables:
    - index
    - normindex
    - size
  name: stackSdf
  opType: raytk.operators.sdf.stackSdf
  parameters:
  - label: Count
    name: Count
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Width Mode
    menuOptions:
    - label: Total Input Width
      name: total
    - label: Normalized Width
      name: normalized
    name: Widthmode
  - label: Total Width
    name: Totalwidth
  - label: Size Multiplier
    name: Sizemult
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Size Offset
    name: Sizeoffset
    readOnlyHandling: semibaked
    regularHandling: runtime
  status: beta
  variables:
  - label: Slice Index
    name: index
  - label: Normalized Slice Index
    name: normindex
  - label: Slice Size
    name: size

---
