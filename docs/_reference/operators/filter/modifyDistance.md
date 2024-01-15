---
layout: operator
title: modifyDistance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/modifyDistance
redirect_from:
  - /reference/opType/raytk.operators.filter.modifyDistance/
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
    label: SDF
    name: sdf_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Value Field
    name: valueField
    required: true
    returnTypes:
    - float
    - Sdf
  name: modifyDistance
  opType: raytk.operators.filter.modifyDistance
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - label: Add
      name: add
    - label: Multiply
      name: mul
    - label: Replace
      name: replace
    name: Mode
  - label: Mix
    name: Mix
    summary: Mix between the original distance and the original distance.
  status: beta
  variables:
  - label: sdf
    name: sdf
  - label: dist
    name: dist

---
