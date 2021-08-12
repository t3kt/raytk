---
layout: operator
title: waveWarp
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/waveWarp
redirect_from:
  - /reference/opType/raytk.operators.filter.waveWarp/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
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
  name: waveWarp
  opType: raytk.operators.filter.waveWarp
  parameters:
  - label: Enable
    name: Enable
  - label: Wave
    menuOptions:
    - label: Sine
      name: sin
    - label: Cosine
      name: cos
    - label: Triangle
      name: tri
    - label: Ramp
      name: ramp
    - label: Square
      name: square
    name: Function
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
  - label: Period
    name: Period
  - label: Phase
    name: Phase
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  - label: Warp Amount
    name: Amount
  status: beta

---
