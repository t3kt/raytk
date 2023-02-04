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
    coordTypes:
    - vec3
    label: Shape SDF
    name: shape
    returnTypes:
    - Sdf
  name: stackSdf
  opType: raytk.operators.sdf.stackSdf
  parameters:
  - label: Count
    name: Count
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
  - label: Size Offset
    name: Sizeoffset
  status: beta
  variables:
  - label: index
    name: index
  - label: normindex
    name: normindex
  - label: size
    name: size

---
