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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
  summary: Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the
    space.

---


Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.