---
layout: operator
title: smoothUnion
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/smoothUnion
redirect_from:
  - /reference/opType/raytk.operators.combine.smoothUnion/
op:
  category: combine
  detail: Produces the combined areas of the input shapes, blended to smooth out the
    intersections.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - Sdf
    summary: The first SDF to combine.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    returnTypes:
    - float
    - Sdf
    summary: The second SDF to combine.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    - Sdf
    summary: Float value field that can vary the amount of blending at different points
      in space.
  name: smoothUnion
  opType: raytk.operators.combine.smoothUnion
  parameters:
  - label: Enable
    name: Enable
  - label: Amount
    name: Amount
    summary: Size of the blending region.
  status: deprecated
  summary: Combines SDFs using a smooth union operator.
  thumb: assets/images/reference/operators/combine/smoothUnion_thumb.png

---


Combines SDFs using a smooth union operator.

Produces the combined areas of the input shapes, blended to smooth out the intersections.