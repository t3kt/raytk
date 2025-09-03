---
layout: operator
title: planeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/planeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.planeSdf/
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
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  keywords:
  - floor
  - plane
  - sheet
  name: planeSdf
  opType: raytk.operators.sdf.planeSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Which axis the plane faces.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the plane forwards or backwards along the axis that it faces.
  - label: Depth Type
    menuOptions:
    - label: Infinite
      name: infinite
    - label: Finite
      name: finite
    name: Depthtype
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Flip
    name: Flip
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  summary: An infinite plane on the x, y, or z axis.
  thumb: assets/images/reference/operators/sdf/planeSdf_thumb.png

---


An infinite plane on the x, y, or z axis.