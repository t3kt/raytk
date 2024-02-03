---
layout: operator
title: boundLimit
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/boundLimit
redirect_from:
  - /reference/opType/raytk.operators.combine.boundLimit/
op:
  category: combine
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
    - vec2
    - vec3
    label: SDF
    name: definition_in_1
    required: true
    returnTypes:
    - Sdf
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
    - vec2
    - vec3
    label: Bounds SDF
    name: definition_in_2
    required: true
    returnTypes:
    - Sdf
  name: boundLimit
  opType: raytk.operators.combine.boundLimit
  parameters:
  - label: Enable
    name: Enable
  - label: Margin
    name: Margin
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta

---
