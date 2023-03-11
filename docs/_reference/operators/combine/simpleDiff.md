---
layout: operator
title: simpleDiff
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/simpleDiff
redirect_from:
  - /reference/opType/raytk.operators.combine.simpleDiff/
op:
  category: combine
  detail: Produces the area of the first shape minus any areas overlapped by the second
    (or vice versa).
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
    - vec4
    label: SDF 1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - Sdf
    summary: The first SDF, which has the second removed from it (unless `Swaporder`
      is used).
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
    - vec4
    label: SDF 2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - Sdf
    summary: The second SDF, which is removed from the first (unless `Swaporder` is
      used).
  name: simpleDiff
  opType: raytk.operators.combine.simpleDiff
  parameters:
  - label: Enable
    name: Enable
  - label: Swap Order
    name: Swaporder
    summary: Swaps the two inputs, subtracting the first from the second.
  summary: Combines two SDFs using the difference operator.
  thumb: assets/images/reference/operators/combine/simpleDiff_thumb.png

---


Combines two SDFs using the difference operator.

Produces the area of the first shape minus any areas overlapped by the second (or vice versa).