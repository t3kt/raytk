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
  detail: 'The `Axis` parameter determines which axis is used to produce the waves.


    A separate wave is used for offsetting for each axis.


    The `Period` and `Phase` parameters control the spacing and position of the waves.


    The `Amplitude` and `Offset` parameters control how much each axis''s wave shifts
    coordinates on that axis.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  keywords:
  - offset
  - shift
  - sine
  - warp
  - wave
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
  - label: Wave Axis
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
    summary: The axis along which the waves are produced.
  - label: Period
    name: Period
    summary: The width of the waves for each axis.
  - label: Phase
    name: Phase
    summary: The phase of the waves for each axis.
  - label: Amplitude
    name: Amplitude
    summary: The scale of the movement for each axis.
  - label: Offset
    name: Offset
    summary: Offsets the movement for each axis.
  status: beta
  summary: Uses repeating waves to offset space.
  thumb: assets/images/reference/operators/filter/waveWarp_thumb.png

---


Uses repeating waves to offset space.

The `Axis` parameter determines which axis is used to produce the waves.

A separate wave is used for offsetting for each axis.

The `Period` and `Phase` parameters control the spacing and position of the waves.

The `Amplitude` and `Offset` parameters control how much each axis's wave shifts coordinates on that axis.