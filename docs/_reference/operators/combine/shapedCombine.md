---
layout: operator
title: shapedCombine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/shapedCombine
redirect_from:
  - /reference/opType/raytk.operators.combine.shapedCombine/
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 1
    name: definition_in_1
    required: true
    returnTypes:
    - float
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 2
    name: definition_in_2
    required: true
    returnTypes:
    - float
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
    label: Blend Shape
    name: blendShape
    required: true
    returnTypes:
    - float
    - Sdf
  name: shapedCombine
  opType: raytk.operators.combine.shapedCombine
  parameters:
  - label: Enable
    name: Enable
  - label: Radius
    name: Radius
  status: beta
  summary: Combine two SDFs, using a 2D SDF to shape the blending region.

---


Combine two SDFs, using a 2D SDF to shape the blending region.