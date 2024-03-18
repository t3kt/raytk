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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Shape SDF
    name: shape
    returnTypes:
    - Sdf
    supportedVariables:
    - RTK_raytk_operators_sdf_stackSdf_index
    - RTK_raytk_operators_sdf_stackSdf_normindex
    - RTK_raytk_operators_sdf_stackSdf_size
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
  - label: RTK_raytk_operators_sdf_stackSdf_index
    name: RTK_raytk_operators_sdf_stackSdf_index
  - label: RTK_raytk_operators_sdf_stackSdf_normindex
    name: RTK_raytk_operators_sdf_stackSdf_normindex
  - label: RTK_raytk_operators_sdf_stackSdf_size
    name: RTK_raytk_operators_sdf_stackSdf_size

---
