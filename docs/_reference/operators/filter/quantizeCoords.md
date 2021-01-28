---
layout: operator
title: quantizeCoords
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/quantizeCoords
redirect_from:
  - /reference/opType/raytk.operators.filter.quantizeCoords/
op:
  category: filter
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
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: quantizeCoords
  opType: raytk.operators.filter.quantizeCoords
  parameters:
  - label: Enable
    name: Enable
  - label: Size
    name: Size
  - label: Size Multiplier
    name: Sizemult
  - label: Offset
    name: Offset
  - label: Smoothing
    name: Smoothing
  - label: Smoothing Multiplier
    name: Smoothingmult
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the
    space.

---

# quantizeCoords

Category: filter



Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.